# Setup and configuration

This document describes how to configure the repository and GitHub Actions for
notifications, domain lists and runtime options. The top-level `README.md` is
kept concise — follow these instructions to set up `domains.yml`, secrets and
how to test notifications.

## Overview

- The workflow queries certificate transparency (crt.sh) for each monitored
  top-level domain, takes screenshots and stores results under `results/<domain>/`.
- Per-run artifacts include `statuses.json`, `domains.json`, `README.md` and
  a `screenshots/` directory.
- Notification recipients can be configured per-domain via `domains.yml` or
  provided as a repository secret (`DOMAINS_YML`).

## `domains.yml` format

Create a YAML mapping where keys are domain names and values are lists of
recipient email addresses. A special `default:` key is used when a monitored
domain has no explicit recipients.

Example `domains.yml` (replace addresses with your real recipients):

```yaml
# Example domains.yml
# `default` recipients are notified for domains that don't have per-domain entries
default:
  - dfbr@example.com
  - dfbp@example.com

# Per-domain recipient lists (optional)
uib.no:
  - alice@uib.no
  - security@uib.no

rowanpage.co.uk:
  - notify@rowanpage.co.uk
```

Notes:
- If `domains.yml` is present in the repository it will be used by the
  workflows and scripts.
- To keep recipient lists private, do not commit `domains.yml` and instead
  save the YAML in the `DOMAINS_YML` repository secret (see below).
- The script accepts either raw YAML or a base64-encoded YAML string in the
  `DOMAINS_YML` secret; it will try base64 decode first and fall back to raw
  YAML if decoding fails.

## Multiple recipients

Just provide multiple entries under a domain or under `default` (as a YAML
list). The notification script will send one email per domain to the list of
recipients configured for that domain (or to `default` if no per-domain list
is configured).

## Repository secret: `DOMAINS_YML`

To keep addresses private, add the YAML above as a repository secret instead
of committing `domains.yml`.

1. In GitHub: Repository → Settings → Secrets and variables → Actions → New
   repository secret.
2. Secret name: `DOMAINS_YML`.
3. Value: paste the raw YAML (or paste a base64-encoded version of the YAML).

The code will prefer a checked-in `domains.yml` when present; to force using
only the secret, remove or rename the committed `domains.yml`.

## SMTP / email configuration (required for notifications)

Set the following repository secrets (or env vars when running locally):

- `SMTP_HOST` (required)
- `SMTP_PORT` (optional, default `587`) — use `465` for implicit SSL if required
- `SMTP_USER` (optional)
- `SMTP_PASSWORD` (optional)
- `EMAIL_FROM` (required) — the From header used in emails
- `EMAIL_TO` (optional fallback) — comma-separated list used when no domains.yml/DOMAINS_YML is present

Important: Some providers require the envelope MAIL FROM to match the
authenticated user — the scripts set the envelope sender to `SMTP_USER` when
present and also set the `Sender` header accordingly.

## How notifications work

- After results are merged, `scripts/notify_new_domains.py` compares the
  latest run to prior runs and sends an email for each top-level domain with
  newly-responding names.
- The script will embed available screenshots as inline images.
- The `--lookback` parameter controls how many previous runs are considered
  when deciding whether a name is "newly responding". `--lookback 0` means
  consider all previous runs (default behavior).

The workflow now exposes a `lookback` workflow_dispatch input (default `0`) —
this is passed to `notify_new_domains.py` when the workflow runs.

## Testing email configuration

Use the `Test SMTP Notification` workflow (`.github/workflows/test_notify.yml`)
from the Actions tab to verify SMTP settings. The test workflow will try to
send a small plaintext message using the configured secrets.

## Workflow inputs (manual trigger)

When manually dispatching the `Screenshot Certificate List` workflow you may
override these inputs:

- `max_runs` — number of runs to keep per domain (default: set in workflow)
- `max_domains` — maximum names to screenshot per run (0 = unlimited)
- `concurrency` — number of concurrent screenshot workers
- `crtsh_timeout` — HTTP timeout for crt.sh queries
- `crtsh_max_retries` — retry attempts for crt.sh
- `lookback` — lookback runs for notifications (0 = all previous runs)

Defaults are configured in the workflow manifest; change them there if you
wish.

## Local testing / running

To run locally:

1. Install Python dependencies from `scripts/requirements.txt`.
2. Install Playwright browsers (`playwright install --with-deps chromium`).
3. Run per-domain processing:

   - `python3 scripts/run_domain.py <domain> --results-dir results` will
     produce a timestamped run under `results/<domain>/`.

4. Regenerate the top-level README locally:

   - `python3 scripts/update_readme.py results`

5. Test notifications locally by setting SMTP-related environment variables
   and running:

   - `python3 scripts/notify_new_domains.py results --lookback 0`

(If you need exact shell commands, tell me and I will provide ready-to-run
examples for macOS / zsh.)

## Where results are written

- Results for each domain are written under `results/<domain>/<timestamp>/`.
- Each run contains `README.md`, `domains.json`, `statuses.json` and the
  `screenshots/` directory.

## Security considerations

- Keep `domains.yml` out of the repository if it contains personal or
  internal email addresses — use the `DOMAINS_YML` secret instead.
- Protect SMTP credentials using repository secrets. Do not store passwords in
  plaintext in the repo.

## Troubleshooting

- If notifications are not sent, check the workflow logs for the notify step
  and ensure `SMTP_HOST` and `EMAIL_FROM` are set.
- Use the `Test SMTP Notification` workflow to validate SMTP credentials.
- If no domains are being processed, ensure your domain list is present via
  `domains.yml`, `DOMAINS_YML` or `domains.txt` in that preference order.

---

If you want, I can create a ready-to-commit `domains.yml` derived from your
existing `domains.txt` populated with `dfbr`/`dfbp` as default recipients.
