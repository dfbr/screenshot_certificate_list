#!/usr/bin/env python3
"""Regenerate the top-level README.md from the results directory."""

import sys
from datetime import datetime, timezone
from pathlib import Path
import json

HEADER = """\
# Screenshot Certificate List

Automated screenshots of domains found in certificate transparency logs via
[crt.sh](https://crt.sh/).

The workflow runs daily (and can be triggered manually). For every domain in
[`domains.txt`](domains.txt) it:

1. Queries **crt.sh** for all current certificates whose common name ends with
   that domain (e.g. `%.uib.no`).
2. Filters out wildcard entries and deduplicates the list.
3. Takes a **screenshot** of each reachable site (HTTPS first, then HTTP).
4. Saves everything to a date-stamped directory under `results/<domain>/`.
5. Generates a **README.md** inside that directory with an image gallery.
6. Keeps only the most recent **5 runs** per domain (configurable).

Multiple domains are processed **concurrently** as separate GitHub Actions
matrix jobs.

---

## Adding / Removing Domains

Edit [`domains.txt`](domains.txt) — one domain per line; lines starting with
`#` are ignored.

## Manual Triggering

Go to **Actions → Screenshot Certificate List → Run workflow** and optionally
override:

| Input | Default | Description |
|-------|---------|-------------|
| `max_runs` | `5` | Runs to keep per domain |
| `max_domains` | `50` | Max domains to screenshot per run (`0` = unlimited) |

## Repository Layout

```
domains.txt            # Domains to monitor
scripts/
  run_domain.py        # Per-domain processing (crt.sh query + screenshots)
  update_readme.py     # Regenerates this README from results/
  requirements.txt     # Python dependencies
.github/workflows/
  screenshot.yml       # GitHub Actions workflow
results/
  <domain>/
    <YYYY-MM-DD_HH-MM-SS>/
      README.md        # Screenshot gallery for this run
      domains.json     # Raw list of names from crt.sh
      screenshots/
        <name>.png
```
"""


def main() -> None:
    results_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results")
    readme_path = Path("README.md")

    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        HEADER,
        "---",
        "",
        "## Results",
        "",
        f"> Last updated: {now}",
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
            counts: dict[str, int] = {}
            for v in status_map.values():
                counts[v] = counts.get(v, 0) + 1
            total = sum(counts.values())
            success = counts.pop("ok", 0)

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

    readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"README.md updated ({len(domain_dirs)} domain(s))")


if __name__ == "__main__":
    main()

