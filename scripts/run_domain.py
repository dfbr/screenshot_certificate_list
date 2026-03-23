#!/usr/bin/env python3
"""Process a single domain: query crt.sh, take screenshots, generate README, prune old runs."""

import json
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests


def query_crtsh(domain: str) -> list[str]:
    """Return sorted list of unique, non-wildcard names from crt.sh for *domain*."""
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: crt.sh query failed for {domain}: {exc}", file=sys.stderr)
        return []

    names: set[str] = set()
    for cert in data:
        for field in ("common_name", "name_value"):
            for raw in (cert.get(field) or "").split("\n"):
                name = raw.strip().lower()
                if not name or name.startswith("*"):
                    continue
                if name == domain or name.endswith(f".{domain}"):
                    names.add(name)
    return sorted(names)


def take_screenshot(hostname: str, output_path: Path) -> bool:
    """Try HTTPS then HTTP. Save screenshot to *output_path*. Return True on success."""
    from playwright.sync_api import TimeoutError as PWTimeout  # noqa: PLC0415
    from playwright.sync_api import sync_playwright  # noqa: PLC0415

    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        ctx = browser.new_context(viewport={"width": 1280, "height": 800})
        page = ctx.new_page()
        success = False
        for scheme in ("https", "http"):
            url = f"{scheme}://{hostname}"
            try:
                page.goto(url, timeout=15_000, wait_until="domcontentloaded")
                page.screenshot(path=str(output_path), full_page=False)
                success = True
                break
            except PWTimeout:
                print(f"    timeout: {url}")
            except Exception as exc:  # noqa: BLE001
                print(f"    error {url}: {exc}")
        ctx.close()
        browser.close()
    return success


def cleanup_old_runs(domain_dir: Path, keep: int) -> None:
    """Delete the oldest run directories so that only *keep* remain."""
    if keep <= 0:
        return
    runs = sorted(d for d in domain_dir.iterdir() if d.is_dir())
    for old in runs[:-keep]:
        shutil.rmtree(old)
        print(f"Removed old run: {old.name}")


def generate_run_readme(
    run_dir: Path,
    domain: str,
    names: list[str],
    results: dict[str, bool],
) -> None:
    """Write README.md for a single run inside *run_dir*."""
    timestamp = run_dir.name
    lines = [
        f"# {domain} — {timestamp}",
        "",
        f"Certificates queried from [crt.sh](https://crt.sh/?q=%.{domain}).",
        "",
        f"**{len(names)} unique domain(s) found.**",
        "",
        "| Domain | Screenshot |",
        "|--------|-----------|",
    ]
    for name in names:
        if results.get(name):
            img = f"screenshots/{name}.png"
            lines.append(f"| `{name}` | ![{name}]({img}) |")
        else:
            lines.append(f"| `{name}` | *(screenshot unavailable)* |")
    (run_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: run_domain.py <domain> [results_dir] [max_runs] [max_domains] [concurrency]\n"
            "  max_runs    – keep this many most-recent runs (default 5, 0 = unlimited)\n"
            "  max_domains – screenshot at most this many domains (default 0 = unlimited)\n"
            "  concurrency – number of screenshots to take in parallel (default 12)"
        )
        sys.exit(1)

    domain = sys.argv[1].strip().lower()
    base_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("results")
    max_runs = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    max_domains = int(sys.argv[4]) if len(sys.argv) > 4 else 0  # 0 = unlimited
    concurrency = int(sys.argv[5]) if len(sys.argv) > 5 else 12

    print(f"=== Processing: {domain} ===")

    # Create timestamped run directory
    timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    domain_dir = base_dir / domain
    run_dir = domain_dir / timestamp
    screenshots_dir = run_dir / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    # Query crt.sh
    print("Querying crt.sh…")
    names = query_crtsh(domain)
    print(f"Found {len(names)} unique name(s)")

    if max_domains and len(names) > max_domains:
        print(f"Limiting to first {max_domains} of {len(names)} names")
        names = names[:max_domains]

    if not names:
        print(f"No names found; defaulting to [{domain}]")
        names = [domain]

    # Persist domain list
    (run_dir / "domains.json").write_text(
        json.dumps(names, indent=2), encoding="utf-8"
    )

    # Take screenshots concurrently
    screenshot_results: dict[str, bool] = {}
    print(f"Taking screenshots with concurrency={concurrency}…")

    def _screenshot_task(name: str) -> tuple[str, bool]:
        out = screenshots_dir / f"{name}.png"
        ok = take_screenshot(name, out)
        print(f"  {'✓' if ok else '✗'} {name}", flush=True)
        return name, ok

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {executor.submit(_screenshot_task, name): name for name in names}
        for future in as_completed(futures):
            name, ok = future.result()
            screenshot_results[name] = ok

    # Generate per-run README
    generate_run_readme(run_dir, domain, names, screenshot_results)
    print(f"README written → {run_dir / 'README.md'}")

    # Prune old runs
    cleanup_old_runs(domain_dir, keep=max_runs)

    print(f"Done: {run_dir}")


if __name__ == "__main__":
    main()
