#!/usr/bin/env python3
"""Run the full local pipeline: process domains, notify, and build docs site.

This mirrors the main GitHub Actions flow locally:
1) Read domains from domains.yml / DOMAINS_YML / domains.txt
2) Run scripts/run_domain.py in parallel per top-level domain
3) Run scripts/notify_new_domains.py
4) Run scripts/update_readme.py with --docs-dir
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

DOMAIN_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)+$")


def _domains_from_yaml_text(raw: str) -> list[str]:
    try:
        data = yaml.safe_load(raw) or {}
    except Exception:
        return []
    if not isinstance(data, dict):
        return []

    out: list[str] = []
    for key in data.keys():
        if not isinstance(key, str):
            continue
        domain = key.strip().lower()
        if not domain or domain == "default":
            continue
        if domain.startswith("#") or " " in domain:
            continue
        if DOMAIN_RE.match(domain):
            out.append(domain)
    return sorted(set(out))


def load_domains() -> list[str]:
    ypath = Path("domains.yml")
    if ypath.exists():
        try:
            domains = _domains_from_yaml_text(ypath.read_text(encoding="utf-8"))
            if domains:
                return domains
        except Exception:
            pass

    env = os.environ.get("DOMAINS_YML")
    if env:
        try:
            try:
                raw = base64.b64decode(env).decode("utf-8")
            except Exception:
                raw = env
            domains = _domains_from_yaml_text(raw)
            if domains:
                return domains
        except Exception:
            pass

    txt = Path("domains.txt")
    if txt.exists():
        out: list[str] = []
        with txt.open("r", encoding="utf-8") as fh:
            for line in fh:
                domain = line.strip().lower()
                if not domain or domain.startswith("#"):
                    continue
                if DOMAIN_RE.match(domain):
                    out.append(domain)
        return sorted(set(out))

    return []


def run_cmd(cmd: list[str], env: dict[str, str] | None = None) -> int:
    proc = subprocess.run(cmd, text=True, capture_output=True, env=env)
    if proc.stdout:
        print(proc.stdout.rstrip())
    if proc.stderr:
        print(proc.stderr.rstrip(), file=sys.stderr)
    return proc.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Run local full pipeline (process + notify + build docs)")
    parser.add_argument("--results-dir", default="results", help="Results directory (default: results)")
    parser.add_argument("--docs-dir", default="docs", help="Docs output directory (default: docs)")
    parser.add_argument("--max-runs", type=int, default=10, help="Max runs to keep per domain (default: 10)")
    parser.add_argument("--max-domains", type=int, default=0, help="Max domains per run (0 = unlimited)")
    parser.add_argument("--concurrency", type=int, default=12, help="Screenshot concurrency per domain (default: 12)")
    parser.add_argument("--domain-concurrency", type=int, default=2, help="Parallel top-level domain workers (default: 2)")
    parser.add_argument("--crtsh-timeout", type=int, default=45, help="crt.sh read timeout seconds (default: 45)")
    parser.add_argument("--crtsh-max-retries", type=int, default=12, help="crt.sh max retries (default: 12)")
    parser.add_argument("--lookback", type=int, default=0, help="Notify lookback runs (0 = all previous)")
    parser.add_argument("--skip-notify", action="store_true", help="Skip notify_new_domains.py")
    parser.add_argument("--skip-build", action="store_true", help="Skip update_readme.py docs build")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if any domain processing fails")
    args = parser.parse_args()

    domains = load_domains()
    if not domains:
        print("No domains found. Add domains.yml, DOMAINS_YML, or domains.txt.", file=sys.stderr)
        raise SystemExit(1)

    workers = max(1, min(args.domain_concurrency, len(domains)))
    print(f"Processing {len(domains)} domain(s) with domain_concurrency={workers}")

    failures: list[str] = []

    def run_one(domain: str) -> tuple[str, int, str, str]:
        cmd = [
            sys.executable,
            "scripts/run_domain.py",
            domain,
            "--results-dir",
            args.results_dir,
            "--max-runs",
            str(args.max_runs),
            "--max-domains",
            str(args.max_domains),
            "--concurrency",
            str(args.concurrency),
            "--crtsh-timeout",
            str(args.crtsh_timeout),
            "--crtsh-max-retries",
            str(args.crtsh_max_retries),
        ]
        proc = subprocess.run(cmd, text=True, capture_output=True)
        return domain, proc.returncode, proc.stdout, proc.stderr

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(run_one, domain) for domain in domains]
        for future in as_completed(futures):
            domain, rc, out, err = future.result()
            print(f"\n=== Domain: {domain} (exit={rc}) ===")
            if out:
                print(out.rstrip())
            if err:
                print(err.rstrip(), file=sys.stderr)
            if rc != 0:
                failures.append(domain)

    if failures:
        print(
            "WARNING: one or more domains failed (continuing): " + ", ".join(sorted(failures)),
            file=sys.stderr,
        )

    if not args.skip_notify:
        print("\n=== Notify new responsive domains ===")
        notify_rc = run_cmd([
            sys.executable,
            "scripts/notify_new_domains.py",
            args.results_dir,
            "--lookback",
            str(args.lookback),
        ])
        if notify_rc != 0:
            print(f"WARNING: notifications step exited with {notify_rc}", file=sys.stderr)

    if not args.skip_build:
        print("\n=== Build website/docs ===")
        build_rc = run_cmd([
            sys.executable,
            "scripts/update_readme.py",
            args.results_dir,
            "--docs-dir",
            args.docs_dir,
        ])
        if build_rc != 0:
            print(f"ERROR: docs build step exited with {build_rc}", file=sys.stderr)
            raise SystemExit(build_rc)

    if failures and args.strict:
        raise SystemExit(1)

    print("\nPipeline complete.")


if __name__ == "__main__":
    main()
