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
    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as smtp:
        smtp.ehlo()
        if smtp.has_extn("STARTTLS"):
            smtp.starttls()
            smtp.ehlo()
        if smtp_user and smtp_pass:
            smtp.login(smtp_user, smtp_pass)
        # Use envelope_from as the MAIL FROM (envelope sender) to satisfy providers
        # that enforce authenticated/verified senders.
        smtp.sendmail(envelope_from, to_addrs, msg_root.as_string())


def main() -> None:
    parser = argparse.ArgumentParser(description="Email notifications for newly-responding domains")
    parser.add_argument("results_dir", nargs="?", default="results", help="Path to results/ directory")
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    if not results_dir.exists():
        print("No results directory found; nothing to notify.")
        return

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

    # Read domains.txt from repository root (if present)
    repo_domains = []
    if Path("domains.txt").exists():
        with open("domains.txt") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                repo_domains.append(line)

    # If domains.txt is missing, fallback to scanning results/ subdirs
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
        prev_status = load_statuses(previous)

        # Find names that are ok in latest but absent or not ok in previous
        newly_ok = [n for n, s in latest_status.items() if s == "ok" and prev_status.get(n) != "ok"]
        if not newly_ok:
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
            send_email(smtp_host, smtp_port, smtp_user, smtp_pass, email_from, to_addrs, subject, html_body, inline_images)
            print(f"Notification sent for {domain}: {len(newly_ok)} new(s)")
            sent_count += 1
        except Exception as exc:
            print(f"Failed to send notification for {domain}: {exc}")

    print(f"Done. Notifications sent: {sent_count}")


if __name__ == "__main__":
    main()
