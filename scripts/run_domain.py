#!/usr/bin/env python3
"""Process a single domain: query crt.sh, take screenshots, generate README, prune old runs."""

import json
import random
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests


def query_crtsh(domain: str, timeout: int = 10, max_retries: int = 10) -> list[str]:
    """Return sorted list of unique, non-wildcard names from crt.sh for *domain*.

    Retries up to *max_retries* times with a short back-off to handle the
    intermittent availability of crt.sh.
    """
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    data = None
    for attempt in range(1, max_retries + 1):
        try:
            headers = {"User-Agent": "screenshot_certificate_list/1.0 (+https://github.com/your/repo)"}
            resp = requests.get(url, timeout=timeout, headers=headers)
            resp.raise_for_status()
            try:
                data = resp.json()
            except ValueError:
                # crt.sh sometimes returns HTML/error pages despite a 200/503; treat as retryable
                print(
                    f"WARNING: crt.sh returned non-JSON response on attempt {attempt}/{max_retries} for {domain}",
                    file=sys.stderr,
                )
                if attempt < max_retries:
                    sleep_time = (2 ** min(attempt - 1, 4)) + random.random()
                    time.sleep(sleep_time)
                continue
            break
        except Exception as exc:  # noqa: BLE001
            print(
                f"WARNING: crt.sh query attempt {attempt}/{max_retries} failed for"
                f" {domain}: {exc}",
                file=sys.stderr,
            )
            if attempt < max_retries:
                sleep_time = (2 ** min(attempt - 1, 4)) + random.random()
                time.sleep(sleep_time)  # back-off with small jitter
    if data is None:
        print(f"ERROR: crt.sh query failed for {domain} after {max_retries} attempt(s)", file=sys.stderr)
        return []

    names: set[str] = set()
    for cert in data:
        for field in ("common_name", "name_value"):
            raw_val = cert.get(field)
            if raw_val is None:
                continue
            # Normalize to list of lines regardless of whether crt.sh returned
            # a single string with newlines or a list of strings.
            raws: list[str] = []
            if isinstance(raw_val, list):
                for item in raw_val:
                    raws.extend(str(item).splitlines())
            else:
                raws = str(raw_val).splitlines()

            for raw in raws:
                name = _normalize_name(raw)
                if not name or name.startswith("*"):
                    continue
                # Keep any name that equals or is a subdomain of the requested domain
                if name == domain or name.endswith(f".{domain}"):
                    names.add(name)
    return sorted(names)


def take_screenshot(hostname: str, output_path: Path) -> tuple[bool, str]:
    """Try HTTPS then HTTP. Save screenshot to *output_path*.

    Return (True, "ok") on success or (False, <error string>) on failure.
    """
    from playwright.sync_api import TimeoutError as PWTimeout  # noqa: PLC0415
    from playwright.sync_api import sync_playwright  # noqa: PLC0415

    last_err = "unreachable"
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--no-sandbox", "--disable-dev-shm-usage"])
        # Allow pages with invalid/expired certificates to be loaded in CI
        ctx = browser.new_context(viewport={"width": 1280, "height": 800}, ignore_https_errors=True)
        # Try each scheme, with a small number of retries per URL to handle
        # transient navigation interruptions. Use a longer timeout per attempt.
        attempts_per_scheme = 2
        goto_timeout_ms = 30_000
        for scheme in ("https", "http"):
            url = f"{scheme}://{hostname}"
            for attempt in range(1, attempts_per_scheme + 1):
                page = ctx.new_page()
                try:
                    response = page.goto(url, timeout=goto_timeout_ms, wait_until="domcontentloaded")
                    if response is not None and response.status >= 400:  # HTTP error (4xx/5xx)
                        last_err = f"HTTP {response.status}"
                        print(f"    {last_err}: {url}")
                        # don't retry on HTTP error from server for this scheme
                        break
                    page.screenshot(path=str(output_path), full_page=False)
                    try:
                        page.close()
                    except Exception:
                        pass
                    try:
                        ctx.close()
                    except Exception:
                        pass
                    try:
                        browser.close()
                    except Exception:
                        pass
                    return True, "ok"
                except PWTimeout:
                    last_err = "timeout"
                    print(f"    timeout ({attempt}/{attempts_per_scheme}): {url}")
                except Exception as exc:  # noqa: BLE001
                    # Clean exception message: keep only first line and truncate to avoid call logs
                    raw = str(exc)
                    first = raw.splitlines()[0].strip()
                    # truncate to reasonable length
                    last_err = (first[:200] + "...") if len(first) > 200 else first
                    print(f"    error ({attempt}/{attempts_per_scheme}) {url}: {first}")
                finally:
                    try:
                        if not page.is_closed():
                            page.close()
                    except Exception:
                        pass
                if attempt < attempts_per_scheme:
                    time.sleep(1 + random.random())
            # next scheme
        try:
            ctx.close()
        except Exception:
            pass
        try:
            browser.close()
        except Exception:
            pass
    return False, last_err


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
    results: dict[str, str],
) -> None:
    """Write README.md for a single run inside *run_dir*.

    Produce a small summary table (counts per result type) followed by a table
    listing each domain with either an embedded screenshot or the error string.
    """
    timestamp = run_dir.name

    # Tally results
    total = len(names)
    counts: dict[str, int] = {}
    for v in results.values():
        counts[v] = counts.get(v, 0) + 1

    # Build summary table
    lines: list[str] = [
        f"# {domain} — {timestamp}",
        "",
        f"Certificates queried from [crt.sh](https://crt.sh/?q=%.{domain}).",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|-------:|------:|",
        f"| Total domains found | {total} |",
    ]

    # Ensure 'ok' appears as Successes
    success = counts.pop("ok", 0)
    lines.append(f"| Successes | {success} |")

    # Add other error types sorted by name
    for err_type in sorted(counts.keys()):
        lines.append(f"| {err_type} | {counts[err_type]} |")

    # Per-domain table
    lines.extend([
        "",
        "## Details",
        "",
        "| Domain | Result |",
        "|--------|--------|",
    ])

    for name in names:
        result = results.get(name)
        if result == "ok":
            img = f"screenshots/{name}.png"
            lines.append(f"| `{name}` | ![{name}]({img}) |")
        else:
            err = result or "(screenshot unavailable)"
            lines.append(f"| `{name}` | `{err}` |")

    (run_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _normalize_name(name: str) -> str:
    """Normalize a domain/name value for deduplication.

    - strip whitespace
    - lowercase
    - remove a trailing dot (fully-qualified form)
    """
    n = (name or "").strip().lower()
    if n.endswith('.'):
        n = n[:-1]
    return n


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: run_domain.py <domain> [results_dir] [max_runs] [max_domains]"
            " [concurrency] [crtsh_timeout] [crtsh_max_retries]\n"
            "  max_runs         – keep this many most-recent runs (default 5, 0 = unlimited)\n"
            "  max_domains      – screenshot at most this many domains (default 0 = unlimited)\n"
            "  concurrency      – number of screenshots to take in parallel (default 12)\n"
            "  crtsh_timeout    – request timeout in seconds for crt.sh queries (default 10)\n"
            "  crtsh_max_retries – maximum retry attempts for crt.sh queries (default 10)"
        )
        sys.exit(1)

    domain = sys.argv[1].strip().lower()
    base_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("results")
    max_runs = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    max_domains = int(sys.argv[4]) if len(sys.argv) > 4 else 0  # 0 = unlimited
    concurrency = int(sys.argv[5]) if len(sys.argv) > 5 else 12
    crtsh_timeout = int(sys.argv[6]) if len(sys.argv) > 6 else 10
    crtsh_max_retries = int(sys.argv[7]) if len(sys.argv) > 7 else 10

    print(f"=== Processing: {domain} ===")

    # Create timestamped run directory
    timestamp = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
    domain_dir = base_dir / domain
    run_dir = domain_dir / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir = run_dir / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    # Query crt.sh
    print("Querying crt.sh…")
    names = query_crtsh(domain, timeout=crtsh_timeout, max_retries=crtsh_max_retries)
    print(f"Found {len(names)} unique name(s)")

    # create run_dir early to ensure errors get written into a place under results/
    (run_dir / "domains.json").parent.mkdir(parents=True, exist_ok=True)

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
    screenshot_results: dict[str, str] = {}
    print(f"Taking screenshots with concurrency={concurrency}…")

    def _screenshot_task(name: str) -> tuple[str, str]:
        out = screenshots_dir / f"{name}.png"
        ok, reason = take_screenshot(name, out)
        status = "ok" if ok else reason
        print(f"  {'✓' if ok else '✗'} {name}" + ("" if ok else f" ({reason})"), flush=True)
        return name, status

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {executor.submit(_screenshot_task, name): name for name in names}
        for future in as_completed(futures):
            try:
                name, status = future.result()
            except Exception as exc:  # noqa: BLE001
                name = futures.get(future, "<unknown>")
                status = str(exc)
                print(f"ERROR: screenshot task for {name} raised: {exc}", file=sys.stderr)
            screenshot_results[name] = status

    # Persist per-domain statuses for this run so the top-level README can summarise results
    try:
        (run_dir / "statuses.json").write_text(
            json.dumps(screenshot_results, indent=2, sort_keys=True), encoding="utf-8"
        )
    except Exception as exc:  # noqa: BLE001
        print(f"WARNING: could not write statuses.json: {exc}", file=sys.stderr)

    # Generate per-run README
    generate_run_readme(run_dir, domain, names, screenshot_results)
    print(f"README written → {run_dir / 'README.md'}")

    # Prune old runs
    cleanup_old_runs(domain_dir, keep=max_runs)

    print(f"Done: {run_dir}")


if __name__ == "__main__":
    main()
