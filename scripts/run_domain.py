#!/usr/bin/env python3
"""Process a single domain: query crt.sh, take screenshots, generate README, prune old runs."""

import json
import random
import re
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import requests
import argparse
from typing import Optional


def _parse_retry_after_seconds(value: Optional[str]) -> Optional[float]:
    """Parse Retry-After header to seconds.

    Supports either integer seconds or HTTP-date format.
    """
    if not value:
        return None
    raw = value.strip()
    if not raw:
        return None
    try:
        return max(0.0, float(raw))
    except ValueError:
        pass
    try:
        dt = parsedate_to_datetime(raw)
    except Exception:  # noqa: BLE001
        return None
    if dt.tzinfo is None:
        return None
    now = datetime.now(tz=timezone.utc)
    return max(0.0, (dt - now).total_seconds())


def _crtsh_sleep_seconds(attempt: int, status_code: Optional[int], retry_after: Optional[float]) -> float:
    """Compute retry sleep with exponential backoff and jitter.

    429 responses receive a larger floor to avoid hammering crt.sh.
    """
    base = float(2 ** min(attempt - 1, 6))
    if status_code == 429:
        base = max(base, 10.0)
    sleep_for = base + random.uniform(0.0, 2.0)
    if retry_after is not None:
        sleep_for = max(sleep_for, retry_after)
    return min(sleep_for, 300.0)


def query_crtsh(domain: str, timeout: int = 10, max_retries: int = 10) -> list[str]:
    """Return sorted list of unique, non-wildcard names from crt.sh for *domain*.

    Retries up to *max_retries* times with a short back-off to handle the
    intermittent availability of crt.sh.
    """
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    headers = {
        "User-Agent": "screenshot_certificate_list/1.0 (+https://github.com/dfbr/screenshot_certificate_list)",
        "Accept": "application/json",
    }
    retryable_statuses = {408, 425, 429, 500, 502, 503, 504}
    non_retryable_statuses = {400, 401, 403, 404, 422}

    data = None
    session = requests.Session()

    # Small initial jitter reduces synchronized bursts when several domains
    # start querying crt.sh at the same time.
    time.sleep(random.uniform(0.0, 1.2))

    for attempt in range(1, max_retries + 1):
        response = None
        status_code: Optional[int] = None
        retry_after_seconds: Optional[float] = None
        try:
            response = session.get(url, timeout=(10, timeout), headers=headers)
            status_code = response.status_code

            if status_code == 200:
                try:
                    data = response.json()
                    break
                except ValueError:
                    # crt.sh sometimes returns HTML/error pages with 200.
                    print(
                        f"WARNING: crt.sh returned non-JSON response on attempt {attempt}/{max_retries} for {domain}",
                        file=sys.stderr,
                    )
                    retry_after_seconds = _parse_retry_after_seconds(response.headers.get("Retry-After"))
            elif status_code in non_retryable_statuses:
                print(
                    f"ERROR: non-retryable crt.sh response for {domain}: HTTP {status_code}",
                    file=sys.stderr,
                )
                return []
            elif status_code in retryable_statuses:
                retry_after_seconds = _parse_retry_after_seconds(response.headers.get("Retry-After"))
                print(
                    f"WARNING: crt.sh query attempt {attempt}/{max_retries} failed for {domain}: HTTP {status_code}",
                    file=sys.stderr,
                )
            else:
                # Unknown status: treat as retryable, but report clearly.
                print(
                    f"WARNING: crt.sh query attempt {attempt}/{max_retries} failed for {domain}: HTTP {status_code}",
                    file=sys.stderr,
                )
        except requests.exceptions.Timeout as exc:
            print(
                f"WARNING: crt.sh query attempt {attempt}/{max_retries} failed for {domain}: {exc}",
                file=sys.stderr,
            )
        except requests.exceptions.RequestException as exc:
            print(
                f"WARNING: crt.sh query attempt {attempt}/{max_retries} failed for {domain}: {exc}",
                file=sys.stderr,
            )

        if data is None and attempt < max_retries:
            sleep_time = _crtsh_sleep_seconds(attempt, status_code, retry_after_seconds)
            print(
                f"INFO: waiting {sleep_time:.1f}s before retrying crt.sh for {domain}",
                file=sys.stderr,
            )
            time.sleep(sleep_time)

    session.close()
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
                    response = page.goto(url, timeout=goto_timeout_ms, wait_until="load")
                    if response is not None and response.status >= 400:  # HTTP error (4xx/5xx)
                        last_err = f"HTTP {response.status}"
                        print(f"    {last_err}: {url}")
                        # don't retry on HTTP error from server for this scheme
                        break
                    # Wait for any post-load network activity (e.g. JSON/JS) to settle.
                    # A 5-second timeout is used so that sites with continuous background
                    # requests (analytics, websockets) don't block the screenshot.
                    try:
                        page.wait_for_load_state("networkidle", timeout=5_000)
                    except PWTimeout:
                        pass  # networkidle didn't settle; proceed with screenshot anyway
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

    # Tally results (group domain-specific errors into normalized types)
    def _normalize_error(err: str) -> str:
        if not err:
            return "(screenshot unavailable)"
        e = err.strip()
        # HTTP status
        m = re.search(r"HTTP\s*(\d{3})", e, re.I)
        if m:
            return f"HTTP {m.group(1)}"
        # Playwright/net errors like net::ERR_NAME_NOT_RESOLVED
        m = re.search(r"net::([A-Z0-9_]+)", e, re.I)
        if m:
            return m.group(1)
        if "timeout" in e.lower():
            return "timeout"
        if "navigation" in e.lower() and "interrupt" in e.lower():
            return "navigation interrupted"
        m = re.search(r"Page\.goto:\s*(.+?)\s+at\s+", e)
        if m:
            token = m.group(1)
            m2 = re.search(r"net::([A-Z0-9_]+)", token, re.I)
            if m2:
                return m2.group(1)
            return token
        # strip urls and chrome-error tokens
        e2 = re.sub(r"https?://\S+", "", e)
        e2 = re.sub(r"chrome-error://\S+", "", e2)
        e2 = e2.strip()
        if not e2:
            return "(screenshot unavailable)"
        return e2 if len(e2) <= 200 else e2[:197] + "..."

    total = len(names)
    counts: dict[str, int] = {}
    normalized_map: dict[str, str] = {}
    for k, v in results.items():
        if v == "ok":
            normalized_map[k] = "ok"
            counts["ok"] = counts.get("ok", 0) + 1
        else:
            norm = _normalize_error(v)
            normalized_map[k] = norm
            counts[norm] = counts.get(norm, 0) + 1

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
            # show normalized error for clarity
            err = normalized_map.get(name, None) or "(screenshot unavailable)"
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
    parser = argparse.ArgumentParser(description="Query crt.sh and take screenshots for a domain")
    parser.add_argument("domain", help="Top-level domain to process (e.g. uib.no)")
    parser.add_argument("--results-dir", default="results", dest="results_dir", help="Directory to store results")
    parser.add_argument("--max-runs", type=int, default=5, help="Keep this many most-recent runs (default: 5, 0 = unlimited)")
    parser.add_argument("--max-domains", type=int, default=0, help="Screenshot at most this many domains (0 = unlimited)")
    parser.add_argument("--concurrency", type=int, default=12, help="Number of screenshots to take in parallel (default: 12)")
    parser.add_argument("--crtsh-timeout", type=int, default=45, help="Request timeout in seconds for crt.sh queries (default: 45)")
    parser.add_argument("--crtsh-max-retries", type=int, default=12, help="Maximum retry attempts for crt.sh queries (default: 12)")
    args = parser.parse_args()

    domain = args.domain.strip().lower()
    if domain.startswith("#"):
        print(
            f"ERROR: invalid domain '{domain}'. Remove comment markers and pass only the hostname.",
            file=sys.stderr,
        )
        raise SystemExit(2)

    domain_re = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?(?:\.[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)+$")
    if not domain_re.match(domain):
        print(f"ERROR: invalid domain '{domain}'.", file=sys.stderr)
        raise SystemExit(2)

    base_dir = Path(args.results_dir)
    max_runs = args.max_runs
    max_domains = args.max_domains
    concurrency = args.concurrency
    crtsh_timeout = args.crtsh_timeout
    crtsh_max_retries = args.crtsh_max_retries

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

    # Randomize checking order so screenshots are taken in a non-deterministic order
    # (helps distribute transient failures across runs and avoids always starting
    # with the same host). Persist the shuffled order.
    random.shuffle(names)
    print(f"Shuffled {len(names)} name(s) for checking")

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
