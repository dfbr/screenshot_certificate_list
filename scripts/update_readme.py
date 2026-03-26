#!/usr/bin/env python3
"""Regenerate the top-level README.md from the results directory.

This script now produces a concise README that only shows the Results summary for
each monitored domain. Full setup, workflow and configuration documentation is
written to `SETUP.md` (linked from the bottom of README.md).
"""

import sys
from datetime import datetime, timezone
from pathlib import Path
import json
import re

HEADER = """# Screenshot Certificate List

Automated screenshots of domains found in certificate transparency logs via
[crt.sh](https://crt.sh/).
"""

FOOTER = """

---

Full documentation, setup and operational details are available in `SETUP.md`.
"""


def main() -> None:
    results_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results")
    readme_path = Path("README.md")

    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        HEADER,
        "",
        f"> Last updated: {now}",
        "",
        "## Results",
        "",
    ]

    domain_dirs = sorted(d for d in results_dir.iterdir() if d.is_dir()) if results_dir.exists() else []

    if domain_dirs:
        for domain_dir in domain_dirs:
            runs = sorted(
                (d for d in domain_dir.iterdir() if d.is_dir()),
                key=lambda d: d.name,
                reverse=True,
            )
            if not runs:
                continue
            latest = runs[0]
            # Domain header linking to latest run README
            lines.append(f"### [{domain_dir.name}]({latest / 'README.md'})")
            lines.append("")
            lines.append(f"Latest run: `{latest.name}`")
            lines.append("")

            # Load latest statuses.json if present to display the per-domain summary
            statuses_path = latest / "statuses.json"
            if statuses_path.exists():
                try:
                    status_map = json.loads(statuses_path.read_text(encoding="utf-8"))
                except Exception:
                    status_map = {}
            else:
                status_map = {}

            # Summary table for this domain (mirrors per-run README)
            # Normalize error messages to grouped types (HTTP <code>, ERR_*, timeout, etc.)
            def _normalize_error(err: str) -> str:
                if not err:
                    return "(screenshot unavailable)"
                e = str(err).strip()
                # HTTP status like 'HTTP 403' or 'HTTP 403 ...'
                m = re.search(r"HTTP\s*(\d{3})", e, re.I)
                if m:
                    return f"HTTP {m.group(1)}"
                # Playwright/net errors containing net::TOKEN
                m = re.search(r"net::([A-Z0-9_]+)", e, re.I)
                if m:
                    return m.group(1)
                # Generic ERR_* tokens
                m2 = re.search(r"ERR_[A-Z0-9_]+", e, re.I)
                if m2:
                    return m2.group(0)
                if "timeout" in e.lower():
                    return "timeout"
                if "navigation" in e.lower() and "interrupt" in e.lower():
                    return "navigation interrupted"
                # Strip URLs and chrome-error tokens to avoid spurious unique messages
                e2 = re.sub(r"https?://\S+", "", e)
                e2 = re.sub(r"chrome-error://\S+", "", e2)
                e2 = e2.strip()
                if not e2:
                    return "(screenshot unavailable)"
                return e2 if len(e2) <= 200 else e2[:197] + "..."

            counts: dict[str, int] = {}
            total = 0
            success = 0
            for v in status_map.values():
                total += 1
                if v == "ok":
                    success += 1
                else:
                    norm = _normalize_error(v)
                    counts[norm] = counts.get(norm, 0) + 1

            lines.append("| Metric | Count |")
            lines.append("|-------:|------:|")
            lines.append(f"| Total domains found | {total} |")
            lines.append(f"| Successes | {success} |")
            for err in sorted(counts.keys()):
                lines.append(f"| {err} | {counts[err]} |")
            lines.append("")

            # Historical runs table
            lines.append("Previous runs:")
            lines.append("")
            lines.append("| Run | Link |")
            lines.append("|-----|------|")
            for run in runs:
                lines.append(f"| `{run.name}` | [{run.name}]({run / 'README.md'}) |")
            lines.append("")
            lines.append("")
    else:
        lines += ["*No results yet.*", ""]

    # Footer pointing to full documentation
    lines.append(FOOTER)

    readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"README.md updated ({len(domain_dirs)} domain(s))")


if __name__ == "__main__":
    main()

