#!/usr/bin/env python3
"""Regenerate results/README.md and the standalone GitHub Pages site under docs/.

The docs/ site is a self-contained Jekyll/Minima website.  Screenshots are stored
*only* in docs/<domain>/<run>/screenshots/ (moved from results/ on first build) so
that no files are duplicated.

Optional flags:
  --docs-dir <path>   Write the Jekyll site under <path>/ (default: none, only
                      results/README.md is written).
  --repo-url <url>    Base GitHub repository URL used in footer links.
                      Defaults to https://github.com/dfbr/screenshot_certificate_list
"""

import argparse
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_REPO_URL = "https://github.com/dfbr/screenshot_certificate_list"

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _normalize_error(err: str) -> str:
    """Normalize error messages to grouped types (HTTP <code>, ERR_*, timeout, etc.)."""
    if not err:
        return "(screenshot unavailable)"
    e = str(err).strip()
    m = re.search(r"HTTP\s*(\d{3})", e, re.I)
    if m:
        return f"HTTP {m.group(1)}"
    m = re.search(r"net::([A-Z0-9_]+)", e, re.I)
    if m:
        return m.group(1)
    m2 = re.search(r"ERR_[A-Z0-9_]+", e, re.I)
    if m2:
        return m2.group(0)
    if "timeout" in e.lower():
        return "timeout"
    if "navigation" in e.lower() and "interrupt" in e.lower():
        return "navigation interrupted"
    e2 = re.sub(r"https?://\S+", "", e)
    e2 = re.sub(r"chrome-error://\S+", "", e2)
    e2 = e2.strip()
    if not e2:
        return "(screenshot unavailable)"
    return e2 if len(e2) <= 200 else e2[:197] + "..."


def _load_statuses(run_dir: Path) -> dict[str, str]:
    path = run_dir / "statuses.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _tally(status_map: dict[str, str]) -> tuple[int, int, dict[str, int]]:
    """Return (total, successes, {normalized_error: count})."""
    total = len(status_map)
    success = sum(1 for v in status_map.values() if v == "ok")
    counts: dict[str, int] = {}
    for v in status_map.values():
        if v != "ok":
            norm = _normalize_error(v)
            counts[norm] = counts.get(norm, 0) + 1
    return total, success, counts


def _display_date(run_name: str) -> str:
    """Convert run folder timestamp (YYYY-MM-DD_HH-MM-SS) to dd.MM.yyyy for display."""
    date_part = run_name.split("_", 1)[0]
    try:
        dt = datetime.strptime(date_part, "%Y-%m-%d")
    except ValueError:
        return date_part
    return dt.strftime("%d.%m.%Y")


# ---------------------------------------------------------------------------
# results/README.md  (plain Markdown, relative links)
# ---------------------------------------------------------------------------

_RESULTS_HEADER = """\
# Screenshot Certificate List

Automated screenshots of domains found in certificate transparency logs via
[crt.sh](https://crt.sh/).
"""

_RESULTS_FOOTER = """

---

Full documentation, setup and operational details are available in [SETUP.md](../SETUP.md).
"""


def _write_results_readme(results_dir: Path, domain_dirs: list[Path]) -> None:
    now = datetime.now(tz=timezone.utc).strftime("%d.%m.%Y")
    lines: list[str] = [
        _RESULTS_HEADER,
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
            rel_readme = str(latest.relative_to(results_dir) / "README.md")
            lines.append(f"### [{domain_dir.name}]({rel_readme})")
            lines.append("")
            lines.append(f"Latest run: `{_display_date(latest.name)}`")
            lines.append("")

            status_map = _load_statuses(latest)
            total, success, counts = _tally(status_map)

            lines += [
                "| Metric | Count |",
                "|-------:|------:|",
                f"| Total domains found | {total} |",
                f"| Successes | {success} |",
            ]
            for err in sorted(counts.keys()):
                lines.append(f"| {err} | {counts[err]} |")
            lines.append("")
            lines.append("Previous runs:")
            lines.append("")
            lines.append("| Run | Link |")
            lines.append("|-----|------|")
            for run in runs:
                rel = str(run.relative_to(results_dir) / "README.md")
                lines.append(f"| `{_display_date(run.name)}` | [{_display_date(run.name)}]({rel}) |")
            lines.append("")
            lines.append("")
    else:
        lines += ["*No results yet.*", ""]

    lines.append(_RESULTS_FOOTER)
    (results_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"results/README.md updated ({len(domain_dirs)} domain(s))")


# ---------------------------------------------------------------------------
# docs/ screenshot migration
# ---------------------------------------------------------------------------

def _move_screenshots(results_dir: Path, docs_dir: Path) -> None:
    """Move screenshots from results/<domain>/<run>/screenshots/ to docs/<domain>/<run>/screenshots/.

    Operates only when the destination does not already exist, so re-runs are safe.
    """
    for domain_dir in sorted(results_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        for run_dir in sorted(domain_dir.iterdir()):
            if not run_dir.is_dir():
                continue
            src = run_dir / "screenshots"
            if not src.is_dir():
                continue
            dst = docs_dir / domain_dir.name / run_dir.name / "screenshots"
            if dst.exists():
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            print(f"Moved screenshots -> {dst}")


def _sync_docs_cleanup(results_dir: Path, docs_dir: Path) -> None:
    """Remove docs/<domain>/<run>/ directories whose run no longer exists in results/.

    This keeps docs/ in sync when run_domain.py prunes old runs from results/.
    Only directories whose names match the timestamp pattern are considered.
    """
    _TS = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$")
    if not docs_dir.is_dir():
        return
    for docs_domain_dir in sorted(docs_dir.iterdir()):
        if not docs_domain_dir.is_dir():
            continue
        # Skip Jekyll/asset directories
        if docs_domain_dir.name.startswith(("_", ".")):
            continue
        results_domain_dir = results_dir / docs_domain_dir.name
        if not results_domain_dir.is_dir():
            continue
        existing_runs = {d.name for d in results_domain_dir.iterdir() if d.is_dir()}
        for docs_run_dir in sorted(docs_domain_dir.iterdir()):
            if docs_run_dir.is_dir() and _TS.match(docs_run_dir.name):
                if docs_run_dir.name not in existing_runs:
                    shutil.rmtree(docs_run_dir)
                    print(f"Removed old docs run: {docs_run_dir}")


# ---------------------------------------------------------------------------
# docs/ Jekyll page generators
# ---------------------------------------------------------------------------

def _write_run_page(
    docs_run_dir: Path,
    domain: str,
    run_name: str,
    status_map: dict[str, str],
) -> None:
    """Write docs/<domain>/<run>/index.md for a single run."""
    docs_run_dir.mkdir(parents=True, exist_ok=True)

    total, success, error_counts = _tally(status_map)

    display_date = _display_date(run_name)

    lines: list[str] = [
        "---",
        f'title: "{domain} \u2014 {display_date}"',
        "layout: default",
        "---",
        "",
        f"# {domain} \u2014 {display_date}",
        "",
        f"[\u2190 {domain}](../) &middot; [\u2190 All domains](../../)",
        "",
        f"Subdomains queried from [crt.sh](https://crt.sh/?q=%.{domain}).",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|-------:|------:|",
        f"| Total subdomains found | {total} |",
        f"| Online | {success} |",
    ]
    for err in sorted(error_counts.keys()):
        lines.append(f"| {err} | {error_counts[err]} |")

    # Online subdomains with screenshots
    ok_names = sorted(n for n, v in status_map.items() if v == "ok")
    if ok_names:
        lines += [
            "",
            "## Online Subdomains",
            "",
            "| Subdomain | Screenshot |",
            "|-----------|-----------|",
        ]
        for name in ok_names:
            img = f"screenshots/{name}.png"
            lines.append(f"| `{name}` | [![{name}]({img})]({img}) |")

    # Non-ok results
    error_names = sorted((n, _normalize_error(v)) for n, v in status_map.items() if v != "ok")
    if error_names:
        lines += [
            "",
            "## Other Results",
            "",
            "| Subdomain | Status |",
            "|-----------|--------|",
        ]
        for name, err in error_names:
            lines.append(f"| `{name}` | `{err}` |")

    (docs_run_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_domain_page(
    docs_domain_dir: Path,
    domain: str,
    runs_data: list[tuple[str, dict[str, str]]],
) -> None:
    """Write docs/<domain>/index.md with full run history."""
    docs_domain_dir.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        "---",
        f'title: "{domain}"',
        "layout: default",
        "---",
        "",
        f"# {domain}",
        "",
        "[\u2190 All domains](../)",
        "",
        f"Subdomains from [crt.sh](https://crt.sh/?q=%.{domain}).",
        "",
    ]

    if runs_data:
        latest_name, latest_status = runs_data[0]
        total, success, error_counts = _tally(latest_status)

        lines += [
            f"## Latest Run: {_display_date(latest_name)}",
            "",
            "| Metric | Count |",
            "|-------:|------:|",
            f"| Total subdomains found | {total} |",
            f"| Online | {success} |",
        ]
        for err in sorted(error_counts.keys()):
            lines.append(f"| {err} | {error_counts[err]} |")
        lines.append("")

        lines += [
            "## Run History",
            "",
            "| Run | Subdomains | Online | Details |",
            "|-----|-----------|--------|---------|",
        ]
        for run_name, status_map in runs_data:
            t, s, _ = _tally(status_map)
            lines.append(f"| `{_display_date(run_name)}` | {t} | {s} | [View]({run_name}/) |")
    else:
        lines += ["*No runs yet.*", ""]

    (docs_domain_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_index(
    docs_dir: Path,
    domains_data: list[tuple[str, list[tuple[str, dict[str, str]]]]],
    repo_url: str,
) -> None:
    """Write the main docs/index.md homepage."""
    now = datetime.now(tz=timezone.utc).strftime("%d.%m.%Y")

    lines: list[str] = [
        "---",
        'title: "Screenshot Certificate List"',
        "layout: default",
        "---",
        "",
        "# Screenshot Certificate List",
        "",
        "Automated screenshots of domains discovered via certificate transparency logs",
        "([crt.sh](https://crt.sh/)).",
        "",
        f"> Last updated: {now}",
        "",
        "## Monitored Domains",
        "",
    ]

    if domains_data:
        lines += [
            "| Domain | Latest Run | Subdomains | Online |",
            "|--------|------------|-----------|--------|",
        ]
        for domain, runs in domains_data:
            if runs:
                latest_name, latest_status = runs[0]
                total, success, _ = _tally(latest_status)
                lines.append(
                    f"| [{domain}]({domain}/) | `{_display_date(latest_name)}` | {total} | {success} |"
                )
            else:
                lines.append(f"| [{domain}]({domain}/) | \u2014 | \u2014 | \u2014 |")
        lines.append("")

        # Per-domain detail sections
        lines += ["## Domain Details", ""]
        for domain, runs in domains_data:
            if not runs:
                continue
            latest_name, latest_status = runs[0]
            total, success, error_counts = _tally(latest_status)

            lines.append(f"### [{domain}]({domain}/)")
            lines.append("")
            lines.append(f"Latest run: [`{_display_date(latest_name)}`]({domain}/{latest_name}/)")
            lines.append("")
            lines += [
                "| Metric | Count |",
                "|-------:|------:|",
                f"| Total subdomains found | {total} |",
                f"| Online | {success} |",
            ]
            for err in sorted(error_counts.keys()):
                lines.append(f"| {err} | {error_counts[err]} |")
            lines.append("")

            lines += [
                "Previous runs:",
                "",
                "| Run | Subdomains | Online |",
                "|-----|-----------|--------|",
            ]
            for run_name, status_map in runs:
                t, s, _ = _tally(status_map)
                lines.append(f"| [`{_display_date(run_name)}`]({domain}/{run_name}/) | {t} | {s} |")
            lines.append("")
            lines.append("")
    else:
        lines += ["*No results yet.*", ""]

    lines += [
        "---",
        "",
        f"Full documentation available in [SETUP.md]({repo_url}/blob/main/SETUP.md).",
        "",
    ]

    (docs_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regenerate results/README.md and optional GitHub Pages docs/ site."
    )
    parser.add_argument(
        "results_dir", nargs="?", default="results", help="Path to the results directory"
    )
    parser.add_argument(
        "--docs-dir", default=None, help="Write the Jekyll Pages site under this directory"
    )
    parser.add_argument(
        "--repo-url",
        default=DEFAULT_REPO_URL,
        help="Base GitHub repository URL for footer links",
    )
    parsed = parser.parse_args()
    results_dir = Path(parsed.results_dir)
    docs_dir = Path(parsed.docs_dir) if parsed.docs_dir else None
    repo_url = parsed.repo_url

    domain_dirs = (
        sorted(d for d in results_dir.iterdir() if d.is_dir())
        if results_dir.is_dir()
        else []
    )

    # Always regenerate results/README.md
    _write_results_readme(results_dir, domain_dirs)

    if docs_dir is None:
        return

    docs_dir.mkdir(parents=True, exist_ok=True)

    # Move screenshots into docs/ (idempotent -- skips if already moved)
    _move_screenshots(results_dir, docs_dir)

    # Remove docs/ run dirs that were pruned from results/
    _sync_docs_cleanup(results_dir, docs_dir)

    # Build data and generate per-run + per-domain pages
    domains_data: list[tuple[str, list[tuple[str, dict[str, str]]]]] = []
    for domain_dir in domain_dirs:
        runs = sorted(
            (d for d in domain_dir.iterdir() if d.is_dir()),
            key=lambda d: d.name,
            reverse=True,
        )
        runs_data: list[tuple[str, dict[str, str]]] = []
        for run_dir in runs:
            status_map = _load_statuses(run_dir)
            run_name = run_dir.name
            docs_run_dir = docs_dir / domain_dir.name / run_name
            _write_run_page(docs_run_dir, domain_dir.name, run_name, status_map)
            runs_data.append((run_name, status_map))

        _write_domain_page(docs_dir / domain_dir.name, domain_dir.name, runs_data)
        domains_data.append((domain_dir.name, runs_data))

    # Generate the homepage
    _write_index(docs_dir, domains_data, repo_url)

    print(f"docs/ site updated ({len(domain_dirs)} domain(s))")


if __name__ == "__main__":
    main()
