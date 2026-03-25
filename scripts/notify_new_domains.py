#!/usr/bin/env python3
"""Notify (email) when a domain's latest run discovered newly-responding names.

For each top-level domain listed in `domains.txt` this script looks in
`results/<domain>/` for the two most recent runs. If the latest run contains
one or more names whose status is "ok" but which were absent or non-ok in the
previous run, an email is sent (one email per domain) describing the new
responsive names and embedding their screenshots (if present) as inline images.

SMTP configuration is read from environment variables (recommended to store as
GitHub Actions secrets when run in CI):
- SMTP_HOST
- SMTP_PORT (optional, default 587)
- SMTP_USER (optional)
- SMTP_PASSWORD (optional)
- EMAIL_FROM (required)
- EMAIL_TO (comma-separated list or single address, required)

Usage: python3 scripts/notify_new_domains.py [results_dir]
"""

from __future__ import annotations

import os
import sys
import argparse
import smtplib
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import json
from typing import Any
import base64


def load_statuses(run_dir: Path) -> dict[str, str]:
    path = run_dir / "statuses.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def send_email(smtp_host: str, smtp_port: int, smtp_user: str | None, smtp_pass: str | None,
               from_addr: str, to_addrs: list[str], subject: str, html_body: str,
               inline_images: dict[str, bytes]) -> None:
    msg_root = MIMEMultipart("related")
    msg_root["Subject"] = subject
    msg_root["From"] = from_addr
    msg_root["To"] = ", ".join(to_addrs)

    # Use the authenticated SMTP user as the envelope sender when available.
    # Some providers (e.g. Fastmail) require the MAIL FROM to match the
    # authenticated identity or a verified sender and will rewrite otherwise.
    envelope_from = smtp_user or from_addr
    # Also set the Sender header so recipients and servers see the envelope sender.
    msg_root["Sender"] = envelope_from

    msg_alt = MIMEMultipart("alternative")
    msg_root.attach(msg_alt)

    msg_alt.attach(MIMEText(html_body, "html"))

    # Attach inline images with Content-ID matching keys used in HTML: cid:name
    for cid, img_bytes in inline_images.items():
        img = MIMEImage(img_bytes, _subtype="png")
        img.add_header("Content-ID", f"<{cid}>")
        img.add_header("Content-Disposition", "inline", filename=f"{cid}.png")
        msg_root.attach(img)

    # Send
    if smtp_port == 465:
        # Implicit SSL (Fastmail recommends port 465 for SSL/TLS)
        with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=30) as smtp:
            smtp.ehlo()
            if smtp_user and smtp_pass:
                smtp.login(smtp_user, smtp_pass)
            smtp.sendmail(envelope_from, to_addrs, msg_root.as_string())
    else:
        with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as smtp:
            smtp.ehlo()
            if smtp.has_extn("STARTTLS"):
                smtp.starttls()
                smtp.ehlo()
            if smtp_user and smtp_pass:
                smtp.login(smtp_user, smtp_pass)
            smtp.sendmail(envelope_from, to_addrs, msg_root.as_string())


def load_domains_mapping() -> dict[str, Any]:
    """Load domain -> recipients mapping from domains.yml or DOMAINS_YML env.

    Expected YAML structure:
      default:
        - ops@example.com
      example.com:
        - alice@example.com
        - sec@example.com

    Returns a dict mapping domain -> list of recipient emails. If no file or env
    is present, returns an empty dict.
    """
    # Prefer local file
    ypath = Path("domains.yml")
    if ypath.exists():
        try:
            import yaml  # type: ignore
            data = yaml.safe_load(ypath.read_text(encoding="utf-8")) or {}
            return {k: (v if isinstance(v, list) else [v]) for k, v in data.items()}
        except Exception:
            return {}

    # Fallback to environment variable DOMAINS_YML (base64-encoded or raw YAML)
    env = os.environ.get("DOMAINS_YML")
    if not env:
        return {}
    try:
        import yaml  # type: ignore
        # Try base64 decode first; if it fails, treat as raw YAML
        try:
            raw = base64.b64decode(env).decode("utf-8")
        except Exception:
            raw = env
        data = yaml.safe_load(raw) or {}
        return {k: (v if isinstance(v, list) else [v]) for k, v in data.items()}
    except Exception:
        return {}


def main() -> None:
    parser = argparse.ArgumentParser(description="Email notifications for newly-responding domains")
    parser.add_argument("results_dir", nargs="?", default="results", help="Path to results/ directory")
    parser.add_argument("--lookback", type=int, default=0, help="Number of previous runs to check for prior appearance (0 = all previous runs)")
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    if not results_dir.exists():
        print("No results directory found; nothing to notify.")
        return

    lookback = args.lookback
    if lookback < 0:
        lookback = 0

    # SMTP / email config from environment
    smtp_host = os.environ.get("SMTP_HOST")
    if not smtp_host:
        print("SMTP_HOST not set; aborting notifications.")
        return
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER")
    smtp_pass = os.environ.get("SMTP_PASSWORD")
    email_from = os.environ.get("EMAIL_FROM")
    email_to = os.environ.get("EMAIL_TO")
    if not email_from or not email_to:
        print("EMAIL_FROM or EMAIL_TO not set; aborting notifications.")
        return
    to_addrs = [a.strip() for a in email_to.split(",") if a.strip()]

    # Load domains and per-domain recipients from domains.yml (preferred).
    domains_map = load_domains_mapping()
    if domains_map:
        # keys excluding 'default' are domain names
        repo_domains = [k for k in domains_map.keys() if k != "default"]
    else:
        # Fallback to old domains.txt format
        repo_domains = []
        if Path("domains.txt").exists():
            with open("domains.txt") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    repo_domains.append(line)

    # If still empty, fallback to scanning results/ subdirs
    domain_dirs = repo_domains or [d.name for d in results_dir.iterdir() if d.is_dir()]

    sent_count = 0
    now_ts = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    for domain in domain_dirs:
        domain_dir = results_dir / domain
        if not domain_dir.exists():
            continue
        runs = sorted((d for d in domain_dir.iterdir() if d.is_dir()), key=lambda d: d.name, reverse=True)
        if len(runs) < 2:
            continue
        latest, previous = runs[0], runs[1]
        latest_status = load_statuses(latest)
        # prev_status = load_statuses(previous)
        #
        # Find names that are ok in latest but absent or not ok in previous
        # newly_ok = [n for n, s in latest_status.items() if s == "ok" and prev_status.get(n) != "ok"]
        # Determine which prior runs to inspect based on lookback (0 = all previous)
        if lookback == 0:
            prior_runs = runs[1:]
        else:
            prior_runs = runs[1:1 + lookback]

        # Collect all names that appeared in the selected prior runs (regardless of status)
        prior_names: set[str] = set()
        for r in prior_runs:
            s = load_statuses(r)
            prior_names.update(s.keys())

        # Find names that are ok in latest but did not appear in any of the prior runs
        newly_ok = [n for n, s in latest_status.items() if s == "ok" and n not in prior_names]
        if not newly_ok:
            continue

        # Determine recipients for this domain: domains_map(domain) or default or EMAIL_TO
        recipients: list[str] = []
        if domains_map:
            recipients = domains_map.get(domain) or domains_map.get("default") or []
        else:
            recipients = to_addrs

        # Normalize recipients
        recipients = [r.strip() for r in (recipients or []) if r and r.strip()]
        if not recipients:
            print(f"No recipients configured for {domain}; skipping notification.")
            continue

        # Build HTML body and inline images
        inline_images: dict[str, bytes] = {}
        rows = []
        for name in newly_ok:
            cid = name.replace("@", "_")
            img_path = latest / "screenshots" / f"{name}.png"
            if img_path.exists():
                try:
                    img_bytes = img_path.read_bytes()
                    inline_images[cid] = img_bytes
                    img_tag = f'<img src="cid:{cid}" alt="{name}" style="max-width:600px; display:block; margin-bottom:8px;" />'
                except Exception:
                    img_tag = "(screenshot unavailable)"
            else:
                img_tag = "(screenshot unavailable)"
            rows.append(f"<h4>{name}</h4>\n{img_tag}")

        html_body = f"<html><body><p>New responsive domains for <strong>{domain}</strong> (latest run: {latest.name})</p>"
        html_body += "\n".join(rows)
        html_body += f"<p>Compared to previous run: {previous.name}</p><p>Generated: {now_ts}</p></body></html>"

        subject = f"New responsive domains for {domain} — {now_ts}"

        try:
            send_email(smtp_host, smtp_port, smtp_user, smtp_pass, email_from, recipients, subject, html_body, inline_images)
            print(f"Notification sent for {domain}: {len(newly_ok)} new(s) to {', '.join(recipients)}")
            sent_count += 1
        except Exception as exc:
            print(f"Failed to send notification for {domain}: {exc}")

    print(f"Done. Notifications sent: {sent_count}")


if __name__ == "__main__":
    main()
