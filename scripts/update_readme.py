#!/usr/bin/env python3
"""Regenerate the top-level README.md from the results directory.

This script now produces a concise README that only shows the Results summary for
each monitored domain. Full setup, workflow and configuration documentation is
written to `SETUP.md` (linked from the bottom of README.md).

Optional flags:
  --docs-dir <path>   Also write a GitHub Pages index to <path>/index.md,
                      with links pointing to the GitHub repository rather than
                      relative paths (so they work from the docs/ Pages root).
  --repo-url <url>    Base GitHub repository URL used when --docs-dir is given.
                      Defaults to https://github.com/dfbr/screenshot_certificate_list
"""

from collections.abc import Callable
from datetime import datetime, timezone
from pathlib import Path
import json
import re

HEADER = """# Screenshot Certificate List

Automated screenshots of domains found in certificate transparency logs via
[crt.sh](https://crt.sh/).
"""

FOOTER_RESULTS = """

---

Full documentation, setup and operational details are available in [SETUP.md](../SETUP.md).
"""

FOOTER_DOCS = """

---

Full documentation, setup and operational details are available in
[SETUP.md]({repo_url}/blob/main/SETUP.md).
"""

DEFAULT_REPO_URL = "https://github.com/dfbr/screenshot_certificate_list"


def _parse_args() -> tuple[Path, Path | None, str]:
    """Return (results_dir, docs_dir | None, repo_url)."""
    import argparse

    parser = argparse.ArgumentParser(description="Regenerate README and optional docs index.")
    parser.add_argument("results_dir", nargs="?", default="results", help="Path to the results directory")
    parser.add_argument("--docs-dir", default=None, help="Also write a GitHub Pages index to <path>/index.md")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL, help="Base GitHub repository URL for docs links")
    parsed = parser.parse_args()

    docs_dir = Path(parsed.docs_dir) if parsed.docs_dir else None
    return Path(parsed.results_dir), docs_dir, parsed.repo_url


def _normalize_error(err: str) -> str:
    """Normalize error messages to grouped types (HTTP <code>, ERR_*, timeout, etc.)."""
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


def _build_content(
    results_dir: Path,
    domain_dirs: list[Path],
    run_link_fn: Callable[[Path, Path], str],
    footer: str,
) -> list[str]:
    """Build the README/index content lines.

    run_link_fn(domain_dir, run_dir) -> str  returns the URL for a run README.
    """
    now = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        HEADER,
        "",
        f"> Last updated: {now}",
        "",
        "## Results",
        "",
    ]

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
            lines.append(f"### [{domain_dir.name}]({run_link_fn(domain_dir, latest)})")
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
                lines.append(f"| `{run.name}` | [{run.name}]({run_link_fn(domain_dir, run)}) |")
            lines.append("")
            lines.append("")
    else:
        lines += ["*No results yet.*", ""]

    lines.append(footer)
    return lines


def main() -> None:
    results_dir, docs_dir, repo_url = _parse_args()
    readme_path = results_dir / "README.md"

    domain_dirs = sorted(d for d in results_dir.iterdir() if d.is_dir()) if results_dir.exists() else []

    # Write results/README.md with relative links
    def _relative_link(domain_dir: Path, run_dir: Path) -> str:
        return str(run_dir.relative_to(results_dir) / "README.md")

    lines = _build_content(results_dir, domain_dirs, _relative_link, FOOTER_RESULTS)
    readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"results/README.md updated ({len(domain_dirs)} domain(s))")

    # Optionally write docs/index.md with absolute GitHub.com links
    if docs_dir is not None:
        docs_dir.mkdir(parents=True, exist_ok=True)
        index_path = docs_dir / "index.md"

        def _github_link(domain_dir: Path, run_dir: Path) -> str:
            rel = run_dir.relative_to(results_dir)
            return f"{repo_url}/blob/main/results/{rel}/README.md"

        footer_docs = FOOTER_DOCS.format(repo_url=repo_url)
        docs_lines = _build_content(results_dir, domain_dirs, _github_link, footer_docs)
        index_path.write_text("\n".join(docs_lines) + "\n", encoding="utf-8")
        print(f"docs/index.md updated ({len(domain_dirs)} domain(s))")


if __name__ == "__main__":
    main()

