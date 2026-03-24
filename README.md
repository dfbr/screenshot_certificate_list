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

---

## Results

> Last updated: 2026-03-24 09:15 UTC

### [experian.co.uk](results/experian.co.uk/2026-03-24_09-06-20/README.md)

Latest run: `2026-03-24_09-06-20`

| Metric | Count |
|-------:|------:|
| Total domains found | 581 |
| Successes | 69 |
| HTTP 400 | 1 |
| HTTP 401 | 1 |
| HTTP 403 | 132 |
| HTTP 404 | 15 |
| HTTP 502 | 2 |
| HTTP 503 | 7 |
| Page.goto: Navigation to "http://car.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://car.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://engage.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://engage.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://outsystems.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://outsystems.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://retirementplan.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://retirementplan.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://www.engage.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://www.engage.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_ABORTED at http://data.experian.co.uk/
Call log:
  - navigating to "http://data.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_ABORTED at http://tags.experian.co.uk/
Call log:
  - navigating to "http://tags.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://analytics2.experian.co.uk/
Call log:
  - navigating to "http://analytics2.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://designstudio.experian.co.uk/
Call log:
  - navigating to "http://designstudio.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://emsuweb.experian.co.uk/
Call log:
  - navigating to "http://emsuweb.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://neartime.experian.co.uk/
Call log:
  - navigating to "http://neartime.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://stg.neartime.experian.co.uk/
Call log:
  - navigating to "http://stg.neartime.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://uat-designstudio.experian.co.uk/
Call log:
  - navigating to "http://uat-designstudio.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.identityalarm.experian.co.uk/
Call log:
  - navigating to "http://www.identityalarm.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.identitytheft.experian.co.uk/
Call log:
  - navigating to "http://www.identitytheft.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.privacyguard.experian.co.uk/
Call log:
  - navigating to "http://www.privacyguard.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://goad.experian.co.uk/
Call log:
  - navigating to "http://goad.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://mtls-api.experian.co.uk/
Call log:
  - navigating to "http://mtls-api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://sandbox-mtls-api.experian.co.uk/
Call log:
  - navigating to "http://sandbox-mtls-api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://uat-mtls-api.experian.co.uk/
Call log:
  - navigating to "http://uat-mtls-api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://accdata.experian.co.uk/
Call log:
  - navigating to "http://accdata.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.pcod.experian.co.uk/
Call log:
  - navigating to "http://admin.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.prestg.pcod.experian.co.uk/
Call log:
  - navigating to "http://admin.prestg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.stg.pcod.experian.co.uk/
Call log:
  - navigating to "http://admin.stg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://affordabilitycheck.experian.co.uk/
Call log:
  - navigating to "http://affordabilitycheck.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://agentux.qat.dsardatacapture.experian.co.uk/
Call log:
  - navigating to "http://agentux.qat.dsardatacapture.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://analytics.experian.co.uk/
Call log:
  - navigating to "http://analytics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://api-floodre.experian.co.uk/
Call log:
  - navigating to "http://api-floodre.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://api.prestg.pcod.experian.co.uk/
Call log:
  - navigating to "http://api.prestg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://api.stg.pcod.experian.co.uk/
Call log:
  - navigating to "http://api.stg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://app.pcod.experian.co.uk/
Call log:
  - navigating to "http://app.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://app.stg.pcod.experian.co.uk/
Call log:
  - navigating to "http://app.stg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://archiver-voy.experian.co.uk/
Call log:
  - navigating to "http://archiver-voy.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://automation-companies.experian.co.uk/
Call log:
  - navigating to "http://automation-companies.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://autonoe-analytics.experian.co.uk/
Call log:
  - navigating to "http://autonoe-analytics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://autonoe-notebook.experian.co.uk/
Call log:
  - navigating to "http://autonoe-notebook.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://beta-developer.experian.co.uk/
Call log:
  - navigating to "http://beta-developer.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://companies.experian.co.uk/
Call log:
  - navigating to "http://companies.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://creditreporthelp.experian.co.uk/
Call log:
  - navigating to "http://creditreporthelp.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev-api-floodre.experian.co.uk/
Call log:
  - navigating to "http://dev-api-floodre.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev-entitlements-api-enterprise.experian.co.uk/
Call log:
  - navigating to "http://dev-entitlements-api-enterprise.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev-regulation.experian.co.uk/
Call log:
  - navigating to "http://dev-regulation.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.api.experian.co.uk/
Call log:
  - navigating to "http://dev.api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.experian.co.uk/
Call log:
  - navigating to "http://dev.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.garlik.api.experian.co.uk/
Call log:
  - navigating to "http://dev.garlik.api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dqc-dev.experian.co.uk/
Call log:
  - navigating to "http://dqc-dev.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dqc.experian.co.uk/
Call log:
  - navigating to "http://dqc.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dqc.uat.experian.co.uk/
Call log:
  - navigating to "http://dqc.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dsardatacapture.experian.co.uk/
Call log:
  - navigating to "http://dsardatacapture.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://earthworkbench.experian.co.uk/
Call log:
  - navigating to "http://earthworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://economics.uat.experian.co.uk/
Call log:
  - navigating to "http://economics.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://emsquit.experian.co.uk/
Call log:
  - navigating to "http://emsquit.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://enrichment-api-enterprise.experian.co.uk/
Call log:
  - navigating to "http://enrichment-api-enterprise.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eurydome-analytics.experian.co.uk/
Call log:
  - navigating to "http://eurydome-analytics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://experian-hub.experian.co.uk/
Call log:
  - navigating to "http://experian-hub.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://help.creditreport.cpp.experian.co.uk/
Call log:
  - navigating to "http://help.creditreport.cpp.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hunter.experian.co.uk/
Call log:
  - navigating to "http://hunter.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identityalarm.experian.co.uk/
Call log:
  - navigating to "http://identityalarm.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitycare.experian.co.uk/
Call log:
  - navigating to "http://identitycare.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitycare.uat.experian.co.uk/
Call log:
  - navigating to "http://identitycare.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitytheft.experian.co.uk/
Call log:
  - navigating to "http://identitytheft.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitytheft.uat.experian.co.uk/
Call log:
  - navigating to "http://identitytheft.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://incomeexpend.experian.co.uk/
Call log:
  - navigating to "http://incomeexpend.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://insurance.experian.co.uk/
Call log:
  - navigating to "http://insurance.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jupiterworkbench.experian.co.uk/
Call log:
  - navigating to "http://jupiterworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://marsworkbench.experian.co.uk/
Call log:
  - navigating to "http://marsworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mercuryworkbench.experian.co.uk/
Call log:
  - navigating to "http://mercuryworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://morrisonslp.experian.co.uk/
Call log:
  - navigating to "http://morrisonslp.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mortgagesavingstool.experian.co.uk/
Call log:
  - navigating to "http://mortgagesavingstool.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://namstrvrec.experian.co.uk/
Call log:
  - navigating to "http://namstrvrec.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://neptuneworkbench.experian.co.uk/
Call log:
  - navigating to "http://neptuneworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://openai-app.experian.co.uk/
Call log:
  - navigating to "http://openai-app.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pcod.experian.co.uk/
Call log:
  - navigating to "http://pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://plutoworkbench.experian.co.uk/
Call log:
  - navigating to "http://plutoworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://premium.experian.co.uk/
Call log:
  - navigating to "http://premium.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://preprod.pcod.experian.co.uk/
Call log:
  - navigating to "http://preprod.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prestg.pcod.experian.co.uk/
Call log:
  - navigating to "http://prestg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://privacyguard.experian.co.uk/
Call log:
  - navigating to "http://privacyguard.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://privacyguard.uat.experian.co.uk/
Call log:
  - navigating to "http://privacyguard.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://protectmyidentity.experian.co.uk/
Call log:
  - navigating to "http://protectmyidentity.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://protectmyidentity.uat.experian.co.uk/
Call log:
  - navigating to "http://protectmyidentity.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://qa-companies.experian.co.uk/
Call log:
  - navigating to "http://qa-companies.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://qa.garlik.api.experian.co.uk/
Call log:
  - navigating to "http://qa.garlik.api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://regulation.experian.co.uk/
Call log:
  - navigating to "http://regulation.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://retirementplansecure.experian.co.uk/
Call log:
  - navigating to "http://retirementplansecure.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rp.experian.co.uk/
Call log:
  - navigating to "http://rp.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rpa.experian.co.uk/
Call log:
  - navigating to "http://rpa.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sandboxanalytics.experian.co.uk/
Call log:
  - navigating to "http://sandboxanalytics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://saturnworkbench.experian.co.uk/
Call log:
  - navigating to "http://saturnworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://search.experian.co.uk/
Call log:
  - navigating to "http://search.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smetrics.experian.co.uk/
Call log:
  - navigating to "http://smetrics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sparkdevlb.experian.co.uk/
Call log:
  - navigating to "http://sparkdevlb.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sso-uat-proxy.experian.co.uk/
Call log:
  - navigating to "http://sso-uat-proxy.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sso-uat-proxy.uk.experian.co.uk/
Call log:
  - navigating to "http://sso-uat-proxy.uk.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stage.garlik.api.experian.co.uk/
Call log:
  - navigating to "http://stage.garlik.api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stat.experian.co.uk/
Call log:
  - navigating to "http://stat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stat.uat.experian.co.uk/
Call log:
  - navigating to "http://stat.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stg.experian.co.uk/
Call log:
  - navigating to "http://stg.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stg.pcod.experian.co.uk/
Call log:
  - navigating to "http://stg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supportportal.experian.co.uk/
Call log:
  - navigating to "http://supportportal.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://targetiq.uat.experian.co.uk/
Call log:
  - navigating to "http://targetiq.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-archiver-voy.experian.co.uk/
Call log:
  - navigating to "http://test-archiver-voy.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-entitlements-api-enterprise.experian.co.uk/
Call log:
  - navigating to "http://test-entitlements-api-enterprise.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tmp.creditmatcher.experian.co.uk/
Call log:
  - navigating to "http://tmp.creditmatcher.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tmp.ins.experian.co.uk/
Call log:
  - navigating to "http://tmp.ins.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tst-outsystems.experian.co.uk/
Call log:
  - navigating to "http://tst-outsystems.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tst-regulation.experian.co.uk/
Call log:
  - navigating to "http://tst-regulation.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-api-floodre.experian.co.uk/
Call log:
  - navigating to "http://uat-api-floodre.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-beta-developer.experian.co.uk/
Call log:
  - navigating to "http://uat-beta-developer.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-companies.experian.co.uk/
Call log:
  - navigating to "http://uat-companies.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-enrichment-api-enterprise.experian.co.uk/
Call log:
  - navigating to "http://uat-enrichment-api-enterprise.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-enrichmentui.experian.co.uk/
Call log:
  - navigating to "http://uat-enrichmentui.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-experian-hub.experian.co.uk/
Call log:
  - navigating to "http://uat-experian-hub.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat.dsardatacapture.experian.co.uk/
Call log:
  - navigating to "http://uat.dsardatacapture.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat.identityalarm.experian.co.uk/
Call log:
  - navigating to "http://uat.identityalarm.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uatworkbench.experian.co.uk/
Call log:
  - navigating to "http://uatworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://venusworkbench.experian.co.uk/
Call log:
  - navigating to "http://venusworkbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://workbench.experian.co.uk/
Call log:
  - navigating to "http://workbench.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.accdata.experian.co.uk/
Call log:
  - navigating to "http://www.accdata.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.account.experian.co.uk/
Call log:
  - navigating to "http://www.account.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilitycheck.experian.co.uk/
Call log:
  - navigating to "http://www.affordabilitycheck.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilitypassport.experian.co.uk/
Call log:
  - navigating to "http://www.affordabilitypassport.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilitypassportuserauth.experian.co.uk/
Call log:
  - navigating to "http://www.affordabilitypassportuserauth.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilityportal.experian.co.uk/
Call log:
  - navigating to "http://www.affordabilityportal.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.agentux.dsardatacapture.experian.co.uk/
Call log:
  - navigating to "http://www.agentux.dsardatacapture.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.agentux.uat.dsardatacapture.experian.co.uk/
Call log:
  - navigating to "http://www.agentux.uat.dsardatacapture.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ais.experian.co.uk/
Call log:
  - navigating to "http://www.ais.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.alerts.experian.co.uk/
Call log:
  - navigating to "http://www.alerts.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.analytics.experian.co.uk/
Call log:
  - navigating to "http://www.analytics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.analytics2.experian.co.uk/
Call log:
  - navigating to "http://www.analytics2.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.analyticsondemand.experian.co.uk/
Call log:
  - navigating to "http://www.analyticsondemand.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ariel-notebook.experian.co.uk/
Call log:
  - navigating to "http://www.ariel-notebook.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.beta-developer.experian.co.uk/
Call log:
  - navigating to "http://www.beta-developer.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.boost.experian.co.uk/
Call log:
  - navigating to "http://www.boost.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.c1.experian.co.uk/
Call log:
  - navigating to "http://www.c1.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.car.experian.co.uk/
Call log:
  - navigating to "http://www.car.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.creditmatcher.experian.co.uk/
Call log:
  - navigating to "http://www.creditmatcher.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.dashboard.pfs.poc.experian.co.uk/
Call log:
  - navigating to "http://www.dashboard.pfs.poc.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.datadisputes.experian.co.uk/
Call log:
  - navigating to "http://www.datadisputes.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.designstudio.experian.co.uk/
Call log:
  - navigating to "http://www.designstudio.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.dev-regulation.experian.co.uk/
Call log:
  - navigating to "http://www.dev-regulation.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.dev.service.experian.co.uk/
Call log:
  - navigating to "http://www.dev.service.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.economics.experian.co.uk/
Call log:
  - navigating to "http://www.economics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.economics.uat.experian.co.uk/
Call log:
  - navigating to "http://www.economics.uat.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.email.experian.co.uk/
Call log:
  - navigating to "http://www.email.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsquit.experian.co.uk/
Call log:
  - navigating to "http://www.emsquit.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsuquit.experian.co.uk/
Call log:
  - navigating to "http://www.emsuquit.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsuweb.experian.co.uk/
Call log:
  - navigating to "http://www.emsuweb.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsuweb2.experian.co.uk/
Call log:
  - navigating to "http://www.emsuweb2.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsweb.experian.co.uk/
Call log:
  - navigating to "http://www.emsweb.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsweb2.experian.co.uk/
Call log:
  - navigating to "http://www.emsweb2.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.experian-hub.experian.co.uk/
Call log:
  - navigating to "http://www.experian-hub.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fedsso.experian.co.uk/
Call log:
  - navigating to "http://www.fedsso.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.forgerock.experian.co.uk/
Call log:
  - navigating to "http://www.forgerock.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fulfillcredit.experian.co.uk/
Call log:
  - navigating to "http://www.fulfillcredit.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fulfilldataaccess.experian.co.uk/
Call log:
  - navigating to "http://www.fulfilldataaccess.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fulfillment.experian.co.uk/
Call log:
  - navigating to "http://www.fulfillment.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.goad.experian.co.uk/
Call log:
  - navigating to "http://www.goad.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.home.experian.co.uk/
Call log:
  - navigating to "http://www.home.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.homepage.experian.co.uk/
Call log:
  - navigating to "http://www.homepage.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.hunter.experian.co.uk/
Call log:
  - navigating to "http://www.hunter.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.identity.experian.co.uk/
Call log:
  - navigating to "http://www.identity.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.incomeexpend.experian.co.uk/
Call log:
  - navigating to "http://www.incomeexpend.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ins.experian.co.uk/
Call log:
  - navigating to "http://www.ins.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.links.rewards.experian.co.uk/
Call log:
  - navigating to "http://www.links.rewards.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.lock.experian.co.uk/
Call log:
  - navigating to "http://www.lock.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.mbnaidcs.experian.co.uk/
Call log:
  - navigating to "http://www.mbnaidcs.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.mmonline.experian.co.uk/
Call log:
  - navigating to "http://www.mmonline.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.morrisonslocn.experian.co.uk/
Call log:
  - navigating to "http://www.morrisonslocn.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.morrisonslp.experian.co.uk/
Call log:
  - navigating to "http://www.morrisonslp.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.mtls-api.experian.co.uk/
Call log:
  - navigating to "http://www.mtls-api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.myhome.experian.co.uk/
Call log:
  - navigating to "http://www.myhome.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.neartime.experian.co.uk/
Call log:
  - navigating to "http://www.neartime.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.offers.experian.co.uk/
Call log:
  - navigating to "http://www.offers.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.openai-app.experian.co.uk/
Call log:
  - navigating to "http://www.openai-app.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.pcod.experian.co.uk/
Call log:
  - navigating to "http://www.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.pmidvalidation.experian.co.uk/
Call log:
  - navigating to "http://www.pmidvalidation.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.preprod.pcod.experian.co.uk/
Call log:
  - navigating to "http://www.preprod.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.prestg.pcod.experian.co.uk/
Call log:
  - navigating to "http://www.prestg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.preview.experian.co.uk/
Call log:
  - navigating to "http://www.preview.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.prodmove.experian.co.uk/
Call log:
  - navigating to "http://www.prodmove.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.profile.experian.co.uk/
Call log:
  - navigating to "http://www.profile.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.protect.experian.co.uk/
Call log:
  - navigating to "http://www.protect.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.protectmyidentity.experian.co.uk/
Call log:
  - navigating to "http://www.protectmyidentity.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.provider.pfs.poc.experian.co.uk/
Call log:
  - navigating to "http://www.provider.pfs.poc.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.qa-content.experian.co.uk/
Call log:
  - navigating to "http://www.qa-content.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.qat.dsardatacapture.experian.co.uk/
Call log:
  - navigating to "http://www.qat.dsardatacapture.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.report.experian.co.uk/
Call log:
  - navigating to "http://www.report.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.reportsaver.experian.co.uk/
Call log:
  - navigating to "http://www.reportsaver.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.retirementplan.experian.co.uk/
Call log:
  - navigating to "http://www.retirementplan.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.retirementplansecure.experian.co.uk/
Call log:
  - navigating to "http://www.retirementplansecure.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.retro-on-demand.experian.co.uk/
Call log:
  - navigating to "http://www.retro-on-demand.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.rp.experian.co.uk/
Call log:
  - navigating to "http://www.rp.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sandbox-mtls-api.experian.co.uk/
Call log:
  - navigating to "http://www.sandbox-mtls-api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sandboxanalytics.experian.co.uk/
Call log:
  - navigating to "http://www.sandboxanalytics.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.savings.experian.co.uk/
Call log:
  - navigating to "http://www.savings.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sbslive.experian.co.uk/
Call log:
  - navigating to "http://www.sbslive.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.score.experian.co.uk/
Call log:
  - navigating to "http://www.score.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.search.experian.co.uk/
Call log:
  - navigating to "http://www.search.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.service.experian.co.uk/
Call log:
  - navigating to "http://www.service.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.servicing.experian.co.uk/
Call log:
  - navigating to "http://www.servicing.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sfs-e-series.experian.co.uk/
Call log:
  - navigating to "http://www.sfs-e-series.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sso-uat-proxy.experian.co.uk/
Call log:
  - navigating to "http://www.sso-uat-proxy.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sso-uat-proxy.uk.experian.co.uk/
Call log:
  - navigating to "http://www.sso-uat-proxy.uk.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg-fedsso.experian.co.uk/
Call log:
  - navigating to "http://www.stg-fedsso.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg-retro-on-demand.experian.co.uk/
Call log:
  - navigating to "http://www.stg-retro-on-demand.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg.neartime.experian.co.uk/
Call log:
  - navigating to "http://www.stg.neartime.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg.pcod.experian.co.uk/
Call log:
  - navigating to "http://www.stg.pcod.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg1-preview.experian.co.uk/
Call log:
  - navigating to "http://www.stg1-preview.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg1.experian.co.uk/
Call log:
  - navigating to "http://www.stg1.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.support.experian.co.uk/
Call log:
  - navigating to "http://www.support.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.supporthub.experian.co.uk/
Call log:
  - navigating to "http://www.supporthub.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.trusso.experian.co.uk/
Call log:
  - navigating to "http://www.trusso.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.tst-regulation.experian.co.uk/
Call log:
  - navigating to "http://www.tst-regulation.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-beta-developer.experian.co.uk/
Call log:
  - navigating to "http://www.uat-beta-developer.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-designstudio.experian.co.uk/
Call log:
  - navigating to "http://www.uat-designstudio.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-experian-hub.experian.co.uk/
Call log:
  - navigating to "http://www.uat-experian-hub.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-investigatoronline.experian.co.uk/
Call log:
  - navigating to "http://www.uat-investigatoronline.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-mtls-api.experian.co.uk/
Call log:
  - navigating to "http://www.uat-mtls-api.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-supporthub.experian.co.uk/
Call log:
  - navigating to "http://www.uat-supporthub.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat.mbnaidcs.experian.co.uk/
Call log:
  - navigating to "http://www.uat.mbnaidcs.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat.service.experian.co.uk/
Call log:
  - navigating to "http://www.uat.service.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ukrsotsbank.experian.co.uk/
Call log:
  - navigating to "http://www.ukrsotsbank.experian.co.uk/", waiting until "domcontentloaded"
 | 1 |
| timeout | 131 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-06-20` | [2026-03-24_09-06-20](results/experian.co.uk/2026-03-24_09-06-20/README.md) |
| `2026-03-24_04-21-03` | [2026-03-24_04-21-03](results/experian.co.uk/2026-03-24_04-21-03/README.md) |
| `2026-03-23_14-35-34` | [2026-03-23_14-35-34](results/experian.co.uk/2026-03-23_14-35-34/README.md) |


### [uib.no](results/uib.no/2026-03-24_09-06-13/README.md)

Latest run: `2026-03-24_09-06-13`

| Metric | Count |
|-------:|------:|
| Total domains found | 1086 |
| Successes | 157 |
| HTTP 401 | 1 |
| HTTP 403 | 22 |
| HTTP 404 | 3 |
| HTTP 502 | 1 |
| HTTP 503 | 2 |
| Page.goto: Navigation to "http://anno.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://anno.skytest.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://autodiscover.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://autodiscover.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://board.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://board.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://bsj.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://bsj.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://chat.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://chat.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://dialin.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://dialin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://epos-no.geo.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://epos-no.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://esignering.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://esignering.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://esm.dev.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://esm.dev.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://esm.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://esm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://faktura.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://faktura.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://files.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://files.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://friends.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://friends.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://geoip.app.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://geoip.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://grind.h.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://grind.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://hackmd.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://hackmd.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://half.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://half.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://holberg.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://holberg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://ithjelp.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://ithjelp.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://kb.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://kb.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://konferanse.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://konferanse.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://koronachat.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://koronachat.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://mautic.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://mautic.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://meet.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://meet.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://mirrors.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://mirrors.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://nettkurs.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://nettkurs.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://p1masterlb.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://p1masterlb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://pgboard.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://pgboard.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://ping.app.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://ping.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://pita.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://pita.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://registry-bgo.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://registry-bgo.skytest.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://rino.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://rino.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://search.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://search.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://sfb-webext01.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://sfb-webext01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://skjemaker.test.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://skjemaker.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://soju.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://soju.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://stats.test.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://stats.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://streaming.videonotat.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://streaming.videonotat.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://sujo-test.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://sujo-test.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://sujo.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://sujo.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://tilbakemelding.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://tilbakemelding.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://ujour.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://ujour.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://venner.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://venner.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://videoconference.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://videoconference.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://vurdering.test.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://vurdering.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://webmail.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://webmail.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://wptest2.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://wptest2.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://wptest3.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://wptest3.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://www.jper.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://www.jper.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://www.sars.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://www.sars.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://www2.ii.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://www2.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: Navigation to "http://yum.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/"
Call log:
  - navigating to "http://yum.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://c.uib.no/
Call log:
  - navigating to "http://c.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://w3.pilot.uib.no/
Call log:
  - navigating to "http://w3.pilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://www.fragment.uib.no/
Call log:
  - navigating to "http://www.fragment.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://www.pilot.uib.no/
Call log:
  - navigating to "http://www.pilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://bldl.ii.uib.no/
Call log:
  - navigating to "http://bldl.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://dataviz.app.uib.no/
Call log:
  - navigating to "http://dataviz.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://gitops.skyapp.uib.no/
Call log:
  - navigating to "http://gitops.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://lesebag.skyapp.uib.no/
Call log:
  - navigating to "http://lesebag.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://news.skyapp.uib.no/
Call log:
  - navigating to "http://news.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://read.app.uib.no/
Call log:
  - navigating to "http://read.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://rebell.app.uib.no/
Call log:
  - navigating to "http://rebell.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://rebell.skyapp.uib.no/
Call log:
  - navigating to "http://rebell.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://vault.skyapp.uib.no/
Call log:
  - navigating to "http://vault.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://wptest1.skyapp.uib.no/
Call log:
  - navigating to "http://wptest1.skyapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://ganeti.fribyte.uib.no/
Call log:
  - navigating to "http://ganeti.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://i2s.uib.no/
Call log:
  - navigating to "http://i2s.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://munin.fribyte.uib.no/
Call log:
  - navigating to "http://munin.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://nagios.fribyte.uib.no/
Call log:
  - navigating to "http://nagios.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://newsangler.uib.no/
Call log:
  - navigating to "http://newsangler.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://noralf.uib.no/
Call log:
  - navigating to "http://noralf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://puppet.fribyte.uib.no/
Call log:
  - navigating to "http://puppet.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.i2s.uib.no/
Call log:
  - navigating to "http://www.i2s.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.newsangler.uib.no/
Call log:
  - navigating to "http://www.newsangler.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://adm.uib.no/
Call log:
  - navigating to "http://adm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.bjerknes.uib.no/
Call log:
  - navigating to "http://admin.bjerknes.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://agamemnon.uib.no/
Call log:
  - navigating to "http://agamemnon.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ajax.uib.no/
Call log:
  - navigating to "http://ajax.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://akuttmedisin.uib.no/
Call log:
  - navigating to "http://akuttmedisin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://alertmanager.app.aws.uib.no/
Call log:
  - navigating to "http://alertmanager.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://alexandria.uib.no/
Call log:
  - navigating to "http://alexandria.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://alumni.uib.no/
Call log:
  - navigating to "http://alumni.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://angelica.uib.no/
Call log:
  - navigating to "http://angelica.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://antivirus.uib.no/
Call log:
  - navigating to "http://antivirus.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://apendix2.uib.no/
Call log:
  - navigating to "http://apendix2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://apicanvas.uib.no/
Call log:
  - navigating to "http://apicanvas.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://apsara.uib.no/
Call log:
  - navigating to "http://apsara.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://arkiv.uib.no/
Call log:
  - navigating to "http://arkiv.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://atrium.uib.no/
Call log:
  - navigating to "http://atrium.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://attika.uib.no/
Call log:
  - navigating to "http://attika.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://attila.uib.no/
Call log:
  - navigating to "http://attila.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://audionovela.h.uib.no/
Call log:
  - navigating to "http://audionovela.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://baia-lab.uib.no/
Call log:
  - navigating to "http://baia-lab.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bdcj.uib.no/
Call log:
  - navigating to "http://bdcj.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bergmus.uib.no/
Call log:
  - navigating to "http://bergmus.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://beta.asf.uib.no/
Call log:
  - navigating to "http://beta.asf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bgrg.uib.no/
Call log:
  - navigating to "http://bgrg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bigfoot.uib.no/
Call log:
  - navigating to "http://bigfoot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bigs.uib.no/
Call log:
  - navigating to "http://bigs.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts.uib.no/
Call log:
  - navigating to "http://biostudent-ts.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts01.uib.no/
Call log:
  - navigating to "http://biostudent-ts01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts02.uib.no/
Call log:
  - navigating to "http://biostudent-ts02.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts03.uib.no/
Call log:
  - navigating to "http://biostudent-ts03.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts04.uib.no/
Call log:
  - navigating to "http://biostudent-ts04.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts05.uib.no/
Call log:
  - navigating to "http://biostudent-ts05.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts06.uib.no/
Call log:
  - navigating to "http://biostudent-ts06.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts07.uib.no/
Call log:
  - navigating to "http://biostudent-ts07.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bjerknes.pilot.uib.no/
Call log:
  - navigating to "http://bjerknes.pilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blak.h.uib.no/
Call log:
  - navigating to "http://blak.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blak.uib.no/
Call log:
  - navigating to "http://blak.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blowfly-test.cbu.uib.no/
Call log:
  - navigating to "http://blowfly-test.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bluesky.uib.no/
Call log:
  - navigating to "http://bluesky.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blustar.uib.no/
Call log:
  - navigating to "http://blustar.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://booking.infomedia.uib.no/
Call log:
  - navigating to "http://booking.infomedia.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://boolean.h.uib.no/
Call log:
  - navigating to "http://boolean.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://borodino.uib.no/
Call log:
  - navigating to "http://borodino.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://brage.uib.no/
Call log:
  - navigating to "http://brage.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://britannic.uib.no/
Call log:
  - navigating to "http://britannic.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://brokk.uib.no/
Call log:
  - navigating to "http://brokk.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://brosing.h.uib.no/
Call log:
  - navigating to "http://brosing.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://buf.uib.no/
Call log:
  - navigating to "http://buf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://buoyant.uib.no/
Call log:
  - navigating to "http://buoyant.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bure.uib.no/
Call log:
  - navigating to "http://bure.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://callmoo.uib.no/
Call log:
  - navigating to "http://callmoo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://camperdown.uib.no/
Call log:
  - navigating to "http://camperdown.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cerberus.uib.no/
Call log:
  - navigating to "http://cerberus.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cgps.uib.no/
Call log:
  - navigating to "http://cgps.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://char.uib.no/
Call log:
  - navigating to "http://char.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cisco.uib.no/
Call log:
  - navigating to "http://cisco.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cismacinternal.uib.no/
Call log:
  - navigating to "http://cismacinternal.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ck-vi.uib.no/
Call log:
  - navigating to "http://ck-vi.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://clortho.uib.no/
Call log:
  - navigating to "http://clortho.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cmc.uib.no/
Call log:
  - navigating to "http://cmc.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cmg01.uib.no/
Call log:
  - navigating to "http://cmg01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://collingwood.uib.no/
Call log:
  - navigating to "http://collingwood.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://colossus6.uib.no/
Call log:
  - navigating to "http://colossus6.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://colossus7.uib.no/
Call log:
  - navigating to "http://colossus7.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://convection.uib.no/
Call log:
  - navigating to "http://convection.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://corellia.uib.no/
Call log:
  - navigating to "http://corellia.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://crush.uib.no/
Call log:
  - navigating to "http://crush.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://crypt.clortho.uib.no/
Call log:
  - navigating to "http://crypt.clortho.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://crysis.uib.no/
Call log:
  - navigating to "http://crysis.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dac2000.uib.no/
Call log:
  - navigating to "http://dac2000.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dashboard.iaas.uib.no/
Call log:
  - navigating to "http://dashboard.iaas.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://datatest.uib.no/
Call log:
  - navigating to "http://datatest.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dbh.nsd.uib.no/
Call log:
  - navigating to "http://dbh.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dep.uib.no/
Call log:
  - navigating to "http://dep.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.supermag.uib.no/
Call log:
  - navigating to "http://dev.supermag.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dhcpadmintest.uib.no/
Call log:
  - navigating to "http://dhcpadmintest.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dig.uib.no/
Call log:
  - navigating to "http://dig.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://digital-ub.uib.no/
Call log:
  - navigating to "http://digital-ub.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dikultba.h.uib.no/
Call log:
  - navigating to "http://dikultba.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dill.uib.no/
Call log:
  - navigating to "http://dill.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dimp.nsd.uib.no/
Call log:
  - navigating to "http://dimp.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dioto.skolelab.uib.no/
Call log:
  - navigating to "http://dioto.skolelab.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dioto.uib.no/
Call log:
  - navigating to "http://dioto.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://docs.hpc.uib.no/
Call log:
  - navigating to "http://docs.hpc.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://docs.ub.uib.no/
Call log:
  - navigating to "http://docs.ub.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dorothyjdankel.b.uib.no/
Call log:
  - navigating to "http://dorothyjdankel.b.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://double6.uib.no/
Call log:
  - navigating to "http://double6.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dreistadt.uib.no/
Call log:
  - navigating to "http://dreistadt.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://driva.uib.no/
Call log:
  - navigating to "http://driva.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eclipse.uib.no/
Call log:
  - navigating to "http://eclipse.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://edgepool.uib.no/
Call log:
  - navigating to "http://edgepool.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eecrg.uib.no/
Call log:
  - navigating to "http://eecrg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://efn2.uib.no/
Call log:
  - navigating to "http://efn2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eiktorn.uib.no/
Call log:
  - navigating to "http://eiktorn.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eitre.uib.no/
Call log:
  - navigating to "http://eitre.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eksamen.test.uib.no/
Call log:
  - navigating to "http://eksamen.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eksark.uib.no/
Call log:
  - navigating to "http://eksark.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ekstern-filer.uib.no/
Call log:
  - navigating to "http://ekstern-filer.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ekt.uib.no/
Call log:
  - navigating to "http://ekt.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://elkat.uib.no/
Call log:
  - navigating to "http://elkat.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://emojivoto.app.aws.uib.no/
Call log:
  - navigating to "http://emojivoto.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://engfly.bccs.uib.no/
Call log:
  - navigating to "http://engfly.bccs.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://enterprise.uib.no/
Call log:
  - navigating to "http://enterprise.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://epay.uib.no/
Call log:
  - navigating to "http://epay.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eplebakst.uib.no/
Call log:
  - navigating to "http://eplebakst.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eplebakst1.uib.no/
Call log:
  - navigating to "http://eplebakst1.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://epletre.uib.no/
Call log:
  - navigating to "http://epletre.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eprint.uib.no/
Call log:
  - navigating to "http://eprint.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://essdata.nsd.uib.no/
Call log:
  - navigating to "http://essdata.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eurosphere.nsd.uib.no/
Call log:
  - navigating to "http://eurosphere.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exch.uib.no/
Call log:
  - navigating to "http://exch.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exchange01.uib.no/
Call log:
  - navigating to "http://exchange01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exchange02.uib.no/
Call log:
  - navigating to "http://exchange02.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exchange03.uib.no/
Call log:
  - navigating to "http://exchange03.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://executor.uib.no/
Call log:
  - navigating to "http://executor.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://f.uib.no/
Call log:
  - navigating to "http://f.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fd.uib.no/
Call log:
  - navigating to "http://fd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fdu.h.uib.no/
Call log:
  - navigating to "http://fdu.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://felleskalender.uib.no/
Call log:
  - navigating to "http://felleskalender.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ferdighetssenteret.uib.no/
Call log:
  - navigating to "http://ferdighetssenteret.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fft.uib.no/
Call log:
  - navigating to "http://fft.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://flightgear.uib.no/
Call log:
  - navigating to "http://flightgear.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://float.uib.no/
Call log:
  - navigating to "http://float.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://flyt.nsd.uib.no/
Call log:
  - navigating to "http://flyt.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://folk7.uib.no/
Call log:
  - navigating to "http://folk7.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://foobar.h.uib.no/
Call log:
  - navigating to "http://foobar.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://foreman.ii.uib.no/
Call log:
  - navigating to "http://foreman.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://forskerskolen.uib.no/
Call log:
  - navigating to "http://forskerskolen.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fulla.uib.no/
Call log:
  - navigating to "http://fulla.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://g.uib.no/
Call log:
  - navigating to "http://g.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gdcj.uib.no/
Call log:
  - navigating to "http://gdcj.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gfi063011.uib.no/
Call log:
  - navigating to "http://gfi063011.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ggzgamingzone.uib.no/
Call log:
  - navigating to "http://ggzgamingzone.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://git.ii.uib.no/
Call log:
  - navigating to "http://git.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://git.uib.no/
Call log:
  - navigating to "http://git.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlab-ci.nsd.uib.no/
Call log:
  - navigating to "http://gitlab-ci.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlab.nsd.uib.no/
Call log:
  - navigating to "http://gitlab.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlab.uib.no/
Call log:
  - navigating to "http://gitlab.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlabp1.uib.no/
Call log:
  - navigating to "http://gitlabp1.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gnome.uib.no/
Call log:
  - navigating to "http://gnome.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://grafana.app.aws.uib.no/
Call log:
  - navigating to "http://grafana.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gran.ii.uib.no/
Call log:
  - navigating to "http://gran.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://grind.app.uib.no/
Call log:
  - navigating to "http://grind.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gru.uib.no/
Call log:
  - navigating to "http://gru.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gunnlod.uib.no/
Call log:
  - navigating to "http://gunnlod.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://havanna.uib.no/
Call log:
  - navigating to "http://havanna.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hibagon.uib.no/
Call log:
  - navigating to "http://hibagon.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hild.uib.no/
Call log:
  - navigating to "http://hild.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hilton.uib.no/
Call log:
  - navigating to "http://hilton.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hogushg.uib.no/
Call log:
  - navigating to "http://hogushg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hoguslg.uib.no/
Call log:
  - navigating to "http://hoguslg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hospits.uib.no/
Call log:
  - navigating to "http://hospits.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hostel.uib.no/
Call log:
  - navigating to "http://hostel.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hoth.uib.no/
Call log:
  - navigating to "http://hoth.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://humle.h.uib.no/
Call log:
  - navigating to "http://humle.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hvitgran.ii.uib.no/
Call log:
  - navigating to "http://hvitgran.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hyperion.uib.no/
Call log:
  - navigating to "http://hyperion.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ii.uib.no/
Call log:
  - navigating to "http://ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.rf.uib.no/
Call log:
  - navigating to "http://imap.rf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.student.uib.no/
Call log:
  - navigating to "http://imap.student.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.uib.no/
Call log:
  - navigating to "http://imap.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imbooking.uib.no/
Call log:
  - navigating to "http://imbooking.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imdb.uib.no/
Call log:
  - navigating to "http://imdb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://impero.uib.no/
Call log:
  - navigating to "http://impero.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://impmail.uib.no/
Call log:
  - navigating to "http://impmail.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://industri.uib.no/
Call log:
  - navigating to "http://industri.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://inf101.ii.uib.no/
Call log:
  - navigating to "http://inf101.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://inn.uib.no/
Call log:
  - navigating to "http://inn.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://interaktiv.uib.no/
Call log:
  - navigating to "http://interaktiv.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://interaktiv6.uib.no/
Call log:
  - navigating to "http://interaktiv6.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://intern-filer.uib.no/
Call log:
  - navigating to "http://intern-filer.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-admin-292.uib.no/
Call log:
  - navigating to "http://ise-admin-292.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-policy-292.uib.no/
Call log:
  - navigating to "http://ise-policy-292.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-policy-351.uib.no/
Call log:
  - navigating to "http://ise-policy-351.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-pxgrid-351.uib.no/
Call log:
  - navigating to "http://ise-pxgrid-351.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://itida.uib.no/
Call log:
  - navigating to "http://itida.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://itschemistry.uib.no/
Call log:
  - navigating to "http://itschemistry.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ivalde.uib.no/
Call log:
  - navigating to "http://ivalde.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://iwanttousetheoldversion.uib.no/
Call log:
  - navigating to "http://iwanttousetheoldversion.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jb.nsd.uib.no/
Call log:
  - navigating to "http://jb.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jenkins.uib.no/
Call log:
  - navigating to "http://jenkins.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jensen.uib.no/
Call log:
  - navigating to "http://jensen.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jira.uib.no/
Call log:
  - navigating to "http://jira.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jupyter-test.ii.uib.no/
Call log:
  - navigating to "http://jupyter-test.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jupyter.ii.uib.no/
Call log:
  - navigating to "http://jupyter.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://karib.h.uib.no/
Call log:
  - navigating to "http://karib.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://karlh.ii.uib.no/
Call log:
  - navigating to "http://karlh.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ki.ii.uib.no/
Call log:
  - navigating to "http://ki.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kibana.uib.no/
Call log:
  - navigating to "http://kibana.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kirishima.uib.no/
Call log:
  - navigating to "http://kirishima.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://knutsinserver.uib.no/
Call log:
  - navigating to "http://knutsinserver.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kurs7.uib.no/
Call log:
  - navigating to "http://kurs7.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kvase.uib.no/
Call log:
  - navigating to "http://kvase.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lakrisrot.uib.no/
Call log:
  - navigating to "http://lakrisrot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lelle.publisering-test.aws.uib.no/
Call log:
  - navigating to "http://lelle.publisering-test.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://leuven.uib.no/
Call log:
  - navigating to "http://leuven.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lingo.uib.no/
Call log:
  - navigating to "http://lingo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://link.uib.no/
Call log:
  - navigating to "http://link.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://linkerd.app.aws.uib.no/
Call log:
  - navigating to "http://linkerd.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://logstash.clortho.uib.no/
Call log:
  - navigating to "http://logstash.clortho.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://logstash.uib.no/
Call log:
  - navigating to "http://logstash.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lunde.ii.uib.no/
Call log:
  - navigating to "http://lunde.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lydia2.uib.no/
Call log:
  - navigating to "http://lydia2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lydiatest2.uib.no/
Call log:
  - navigating to "http://lydiatest2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lync.uib.no/
Call log:
  - navigating to "http://lync.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lync02.video.uib.no/
Call log:
  - navigating to "http://lync02.video.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lyncadmin.uib.no/
Call log:
  - navigating to "http://lyncadmin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lyncdiscover.uib.no/
Call log:
  - navigating to "http://lyncdiscover.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lyncdiscoverinternal.uib.no/
Call log:
  - navigating to "http://lyncdiscoverinternal.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lynctlf1.uib.no/
Call log:
  - navigating to "http://lynctlf1.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lynctlf2.uib.no/
Call log:
  - navigating to "http://lynctlf2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://m.grind.app.uib.no/
Call log:
  - navigating to "http://m.grind.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://m.uib.no/
Call log:
  - navigating to "http://m.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://macadmin.clortho.uib.no/
Call log:
  - navigating to "http://macadmin.clortho.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://macadmin.uib.no/
Call log:
  - navigating to "http://macadmin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://magneto.uib.no/
Call log:
  - navigating to "http://magneto.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mail.uib.no/
Call log:
  - navigating to "http://mail.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mailman.uib.no/
Call log:
  - navigating to "http://mailman.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://marat.uib.no/
Call log:
  - navigating to "http://marat.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://marimbaconsole.uib.no/
Call log:
  - navigating to "http://marimbaconsole.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://masterark.uib.no/
Call log:
  - navigating to "http://masterark.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mattermost.ii.uib.no/
Call log:
  - navigating to "http://mattermost.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mdm.uib.no/
Call log:
  - navigating to "http://mdm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mediasite.uib.no/
Call log:
  - navigating to "http://mediasite.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://medvizvcbm.uib.no/
Call log:
  - navigating to "http://medvizvcbm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://meet.gfi.uib.no/
Call log:
  - navigating to "http://meet.gfi.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://melon.uib.no/
Call log:
  - navigating to "http://melon.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://melonny.uib.no/
Call log:
  - navigating to "http://melonny.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://meltzer.uib.no/
Call log:
  - navigating to "http://meltzer.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://metiri.uib.no/
Call log:
  - navigating to "http://metiri.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://micromdm.uib.no/
Call log:
  - navigating to "http://micromdm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://min.uib.no/
Call log:
  - navigating to "http://min.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mine.uib.no/
Call log:
  - navigating to "http://mine.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://minside.uib.no/
Call log:
  - navigating to "http://minside.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mirror.ii.uib.no/
Call log:
  - navigating to "http://mirror.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://miside.felleskalender.uib.no/
Call log:
  - navigating to "http://miside.felleskalender.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://miside.pilot.uib.no/
Call log:
  - navigating to "http://miside.pilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://miside.uib.no/
Call log:
  - navigating to "http://miside.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mobileprint.uib.no/
Call log:
  - navigating to "http://mobileprint.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mobilprint.uib.no/
Call log:
  - navigating to "http://mobilprint.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://monarch.uib.no/
Call log:
  - navigating to "http://monarch.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://moodle.uib.no/
Call log:
  - navigating to "http://moodle.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://moodlehost.uib.no/
Call log:
  - navigating to "http://moodlehost.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munin.uib.no/
Call log:
  - navigating to "http://munin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munki.clortho.uib.no/
Call log:
  - navigating to "http://munki.clortho.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munkiwebadmin.clortho.uib.no/
Call log:
  - navigating to "http://munkiwebadmin.clortho.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munkiwebadmin.uib.no/
Call log:
  - navigating to "http://munkiwebadmin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mx1.test.uib.no/
Call log:
  - navigating to "http://mx1.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://my.traefik.app.aws.uib.no/
Call log:
  - navigating to "http://my.traefik.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://my.uib.no/
Call log:
  - navigating to "http://my.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://myspace.uib.no/
Call log:
  - navigating to "http://myspace.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mysql.uib.no/
Call log:
  - navigating to "http://mysql.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://naf2009.uib.no/
Call log:
  - navigating to "http://naf2009.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nafa.h.uib.no/
Call log:
  - navigating to "http://nafa.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://naglfar.uib.no/
Call log:
  - navigating to "http://naglfar.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://namur.uib.no/
Call log:
  - navigating to "http://namur.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nav-repo.uib.no/
Call log:
  - navigating to "http://nav-repo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://neolatin.uib.no/
Call log:
  - navigating to "http://neolatin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nesstar-dev.nsd.uib.no/
Call log:
  - navigating to "http://nesstar-dev.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://netdata.app.aws.uib.no/
Call log:
  - navigating to "http://netdata.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://netdata.publisering-test.aws.uib.no/
Call log:
  - navigating to "http://netdata.publisering-test.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://netdata.publisering.aws.uib.no/
Call log:
  - navigating to "http://netdata.publisering.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nett8.uib.no/
Call log:
  - navigating to "http://nett8.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nettfransk.uib.no/
Call log:
  - navigating to "http://nettfransk.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nettitaliensk.uib.no/
Call log:
  - navigating to "http://nettitaliensk.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nito.uib.no/
Call log:
  - navigating to "http://nito.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nominasjonsweb.uib.no/
Call log:
  - navigating to "http://nominasjonsweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nominationweb.uib.no/
Call log:
  - navigating to "http://nominationweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nomweb.uib.no/
Call log:
  - navigating to "http://nomweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://normt.uib.no/
Call log:
  - navigating to "http://normt.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://norpol.uib.no/
Call log:
  - navigating to "http://norpol.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://norvana.uib.no/
Call log:
  - navigating to "http://norvana.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nps.uib.no/
Call log:
  - navigating to "http://nps.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nps1.uib.no/
Call log:
  - navigating to "http://nps1.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nps2.uib.no/
Call log:
  - navigating to "http://nps2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ntl.uib.no/
Call log:
  - navigating to "http://ntl.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nybs.uib.no/
Call log:
  - navigating to "http://nybs.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ocs.uib.no/
Call log:
  - navigating to "http://ocs.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://olivetree.ii.uib.no/
Call log:
  - navigating to "http://olivetree.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://olympiade.ii.uib.no/
Call log:
  - navigating to "http://olympiade.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://omod.uib.no/
Call log:
  - navigating to "http://omod.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://oncomatrix.uib.no/
Call log:
  - navigating to "http://oncomatrix.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://onedrive.uib.no/
Call log:
  - navigating to "http://onedrive.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://opencsw.uib.no/
Call log:
  - navigating to "http://opencsw.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ordbruker.testapp.uib.no/
Call log:
  - navigating to "http://ordbruker.testapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://org7.uib.no/
Call log:
  - navigating to "http://org7.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://orontes.uib.no/
Call log:
  - navigating to "http://orontes.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://outlook.uib.no/
Call log:
  - navigating to "http://outlook.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://outlook2.uib.no/
Call log:
  - navigating to "http://outlook2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1box01.uib.no/
Call log:
  - navigating to "http://p1box01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1eia01.uib.no/
Call log:
  - navigating to "http://p1eia01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1gitlab01.uib.no/
Call log:
  - navigating to "http://p1gitlab01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1masterlb01.uib.no/
Call log:
  - navigating to "http://p1masterlb01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1oppdrag01.uib.no/
Call log:
  - navigating to "http://p1oppdrag01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1ordlb.uib.no/
Call log:
  - navigating to "http://p1ordlb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1osd01.uib.no/
Call log:
  - navigating to "http://p1osd01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1piwik01.app.uib.no/
Call log:
  - navigating to "http://p1piwik01.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1redirect01.uib.no/
Call log:
  - navigating to "http://p1redirect01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1rts01.uib.no/
Call log:
  - navigating to "http://p1rts01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1sak01.uib.no/
Call log:
  - navigating to "http://p1sak01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1wiki01.uib.no/
Call log:
  - navigating to "http://p1wiki01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2gitlab01.uib.no/
Call log:
  - navigating to "http://p2gitlab01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2masterlb01.uib.no/
Call log:
  - navigating to "http://p2masterlb01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2oppdrag01.uib.no/
Call log:
  - navigating to "http://p2oppdrag01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2ordlb.uib.no/
Call log:
  - navigating to "http://p2ordlb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2redirect01.uib.no/
Call log:
  - navigating to "http://p2redirect01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2rts01.uib.no/
Call log:
  - navigating to "http://p2rts01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2sak01.uib.no/
Call log:
  - navigating to "http://p2sak01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://people.uib.no/
Call log:
  - navigating to "http://people.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pepperrot.uib.no/
Call log:
  - navigating to "http://pepperrot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://perepigenomics.cbu.uib.no/
Call log:
  - navigating to "http://perepigenomics.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://persille.uib.no/
Call log:
  - navigating to "http://persille.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://phdportal.uib.no/
Call log:
  - navigating to "http://phdportal.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://piwik.app.uib.no/
Call log:
  - navigating to "http://piwik.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pkg.uib.no/
Call log:
  - navigating to "http://pkg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://plikt.gfi.uib.no/
Call log:
  - navigating to "http://plikt.gfi.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pollen.uib.no/
Call log:
  - navigating to "http://pollen.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.asf.uib.no/
Call log:
  - navigating to "http://pop.asf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.rf.uib.no/
Call log:
  - navigating to "http://pop.rf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.student.uib.no/
Call log:
  - navigating to "http://pop.student.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.uib.no/
Call log:
  - navigating to "http://pop.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://portal.ii.uib.no/
Call log:
  - navigating to "http://portal.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://portal.video.uib.no/
Call log:
  - navigating to "http://portal.video.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://postgres.uib.no/
Call log:
  - navigating to "http://postgres.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://preface.b.uib.no/
Call log:
  - navigating to "http://preface.b.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://presence.uib.no/
Call log:
  - navigating to "http://presence.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pretest.uib.no/
Call log:
  - navigating to "http://pretest.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prom.app.aws.uib.no/
Call log:
  - navigating to "http://prom.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.eia.uib.no/
Call log:
  - navigating to "http://prosjekt.eia.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.it.uib.no/
Call log:
  - navigating to "http://prosjekt.it.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.nsd.uib.no/
Call log:
  - navigating to "http://prosjekt.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.test.uib.no/
Call log:
  - navigating to "http://prosjekt.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosopopeia.uib.no/
Call log:
  - navigating to "http://prosopopeia.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prospective.uib.no/
Call log:
  - navigating to "http://prospective.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://proxy-gw.privnett.uib.no/
Call log:
  - navigating to "http://proxy-gw.privnett.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://proxy-gw1.privnett.uib.no/
Call log:
  - navigating to "http://proxy-gw1.privnett.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://proxy-gw2.privnett.uib.no/
Call log:
  - navigating to "http://proxy-gw2.privnett.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://puffin-test.ii.uib.no/
Call log:
  - navigating to "http://puffin-test.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://puffin.ii.uib.no/
Call log:
  - navigating to "http://puffin.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://purlmoo.uib.no/
Call log:
  - navigating to "http://purlmoo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pushgateway.app.aws.uib.no/
Call log:
  - navigating to "http://pushgateway.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radiance.uib.no/
Call log:
  - navigating to "http://radiance.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radisson.uib.no/
Call log:
  - navigating to "http://radisson.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radisson7.uib.no/
Call log:
  - navigating to "http://radisson7.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radius.uib.no/
Call log:
  - navigating to "http://radius.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radius1.uib.no/
Call log:
  - navigating to "http://radius1.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radius2.uib.no/
Call log:
  - navigating to "http://radius2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ramillies.uib.no/
Call log:
  - navigating to "http://ramillies.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rasmus.uib.no/
Call log:
  - navigating to "http://rasmus.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rd-sh02.uib.no/
Call log:
  - navigating to "http://rd-sh02.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rdb.nsd.uib.no/
Call log:
  - navigating to "http://rdb.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://real.uib.no/
Call log:
  - navigating to "http://real.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://record.uib.no/
Call log:
  - navigating to "http://record.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://redirect.test.uib.no/
Call log:
  - navigating to "http://redirect.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://redirect1.test.uib.no/
Call log:
  - navigating to "http://redirect1.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://redmine.it.uib.no/
Call log:
  - navigating to "http://redmine.it.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://regler.publisering-test.aws.uib.no/
Call log:
  - navigating to "http://regler.publisering-test.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://replay.video.uib.no/
Call log:
  - navigating to "http://replay.video.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://resources.uib.no/
Call log:
  - navigating to "http://resources.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://resp.nsd.uib.no/
Call log:
  - navigating to "http://resp.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://resp2.nsd.uib.no/
Call log:
  - navigating to "http://resp2.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://retting.ii.uib.no/
Call log:
  - navigating to "http://retting.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rettspraksis.h.uib.no/
Call log:
  - navigating to "http://rettspraksis.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rhel.uib.no/
Call log:
  - navigating to "http://rhel.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rk-drupal.test.uib.no/
Call log:
  - navigating to "http://rk-drupal.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://romulus.uib.no/
Call log:
  - navigating to "http://romulus.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rosenrot.uib.no/
Call log:
  - navigating to "http://rosenrot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rosmarin.uib.no/
Call log:
  - navigating to "http://rosmarin.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rowan.ii.uib.no/
Call log:
  - navigating to "http://rowan.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rts.test.uib.no/
Call log:
  - navigating to "http://rts.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://safir.uib.no/
Call log:
  - navigating to "http://safir.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sandwich.medicine.b.uib.no/
Call log:
  - navigating to "http://sandwich.medicine.b.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sardis2.uib.no/
Call log:
  - navigating to "http://sardis2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sb.uib.no/
Call log:
  - navigating to "http://sb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sba.h.uib.no/
Call log:
  - navigating to "http://sba.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sba.uib.no/
Call log:
  - navigating to "http://sba.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-ac1.klient.uib.no/
Call log:
  - navigating to "http://sc12-ac1.klient.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-ac2.klient.uib.no/
Call log:
  - navigating to "http://sc12-ac2.klient.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-cm.klient.uib.no/
Call log:
  - navigating to "http://sc12-cm.klient.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-cm.uib.no/
Call log:
  - navigating to "http://sc12-cm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://scalacm.uib.no/
Call log:
  - navigating to "http://scalacm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://scholar.uib.no/
Call log:
  - navigating to "http://scholar.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://scom-sql02.uib.no/
Call log:
  - navigating to "http://scom-sql02.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sddownloads.uib.no/
Call log:
  - navigating to "http://sddownloads.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://search.test.uib.no/
Call log:
  - navigating to "http://search.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sebra.uib.no/
Call log:
  - navigating to "http://sebra.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sebrapilot.uib.no/
Call log:
  - navigating to "http://sebrapilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://secure-video.uib.no/
Call log:
  - navigating to "http://secure-video.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sefas.uib.no/
Call log:
  - navigating to "http://sefas.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://seqlab.test.uib.no/
Call log:
  - navigating to "http://seqlab.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://seqlab.uib.no/
Call log:
  - navigating to "http://seqlab.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://serveradm.uib.no/
Call log:
  - navigating to "http://serveradm.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://serveradmin.test.uib.no/
Call log:
  - navigating to "http://serveradmin.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://service.uib.no/
Call log:
  - navigating to "http://service.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fe01.uib.no/
Call log:
  - navigating to "http://sfb-fe01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fe02.uib.no/
Call log:
  - navigating to "http://sfb-fe02.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fe03.uib.no/
Call log:
  - navigating to "http://sfb-fe03.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fepool01.uib.no/
Call log:
  - navigating to "http://sfb-fepool01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-webpool01.uib.no/
Call log:
  - navigating to "http://sfb-webpool01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://shepherd.ii.uib.no/
Call log:
  - navigating to "http://shepherd.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker-skjema.uib.no/
Call log:
  - navigating to "http://sikker-skjema.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker-vbackend.uib.no/
Call log:
  - navigating to "http://sikker-vbackend.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker-vturn.uib.no/
Call log:
  - navigating to "http://sikker-vturn.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker.filer.uib.no/
Call log:
  - navigating to "http://sikker.filer.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikkert-video.uib.no/
Call log:
  - navigating to "http://sikkert-video.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikre.filer.uib.no/
Call log:
  - navigating to "http://sikre.filer.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sinmara.uib.no/
Call log:
  - navigating to "http://sinmara.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sip.uib.no/
Call log:
  - navigating to "http://sip.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sip2.uib.no/
Call log:
  - navigating to "http://sip2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://siv.uib.no/
Call log:
  - navigating to "http://siv.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skjema.uib.no/
Call log:
  - navigating to "http://skjema.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skjemaker.uib.no/
Call log:
  - navigating to "http://skjemaker.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skolevalg1.nsd.uib.no/
Call log:
  - navigating to "http://skolevalg1.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skolevalg2.nsd.uib.no/
Call log:
  - navigating to "http://skolevalg2.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skrotogskriv.app.uib.no/
Call log:
  - navigating to "http://skrotogskriv.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smtp.rf.uib.no/
Call log:
  - navigating to "http://smtp.rf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smtp.samfunnet.uib.no/
Call log:
  - navigating to "http://smtp.samfunnet.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://snipeit-test.dig.uib.no/
Call log:
  - navigating to "http://snipeit-test.dig.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://software.ii.uib.no/
Call log:
  - navigating to "http://software.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sokogskriv.uib.no/
Call log:
  - navigating to "http://sokogskriv.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sokweb.uib.no/
Call log:
  - navigating to "http://sokweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://space.rokkan.uib.no/
Call log:
  - navigating to "http://space.rokkan.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://spaced.uib.no/
Call log:
  - navigating to "http://spaced.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ssis.uib.no/
Call log:
  - navigating to "http://ssis.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stargazer.uib.no/
Call log:
  - navigating to "http://stargazer.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stats.cbu.uib.no/
Call log:
  - navigating to "http://stats.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stats2.ii.uib.no/
Call log:
  - navigating to "http://stats2.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stjerne.uib.no/
Call log:
  - navigating to "http://stjerne.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stokkstein.ss.uib.no/
Call log:
  - navigating to "http://stokkstein.ss.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://strategi.uib.no/
Call log:
  - navigating to "http://strategi.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://streaming.mh.uib.no/
Call log:
  - navigating to "http://streaming.mh.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://streaming.videonotat.test.uib.no/
Call log:
  - navigating to "http://streaming.videonotat.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://string.uib.no/
Call log:
  - navigating to "http://string.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://structure.uib.no/
Call log:
  - navigating to "http://structure.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studblogg.uib.no/
Call log:
  - navigating to "http://studblogg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studentblogg.uib.no/
Call log:
  - navigating to "http://studentblogg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studentportal.uib.no/
Call log:
  - navigating to "http://studentportal.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studweb.uib.no/
Call log:
  - navigating to "http://studweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studweb0.uib.no/
Call log:
  - navigating to "http://studweb0.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://substr.uib.no/
Call log:
  - navigating to "http://substr.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://subversion.ift.uib.no/
Call log:
  - navigating to "http://subversion.ift.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://subversion.uib.no/
Call log:
  - navigating to "http://subversion.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sudan.uib.no/
Call log:
  - navigating to "http://sudan.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sunlight.uib.no/
Call log:
  - navigating to "http://sunlight.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supermag.uib.no/
Call log:
  - navigating to "http://supermag.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supermagx.uib.no/
Call log:
  - navigating to "http://supermagx.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supertimon.cbu.uib.no/
Call log:
  - navigating to "http://supertimon.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://support.ii.uib.no/
Call log:
  - navigating to "http://support.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sus.infomedia.uib.no/
Call log:
  - navigating to "http://sus.infomedia.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://svar.nsd.uib.no/
Call log:
  - navigating to "http://svar.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://svn.uib.no/
Call log:
  - navigating to "http://svn.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sw.uib.no/
Call log:
  - navigating to "http://sw.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology1.geo.uib.no/
Call log:
  - navigating to "http://synology1.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology2.geo.uib.no/
Call log:
  - navigating to "http://synology2.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology3.geo.uib.no/
Call log:
  - navigating to "http://synology3.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology4.geo.uib.no/
Call log:
  - navigating to "http://synology4.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology5.geo.uib.no/
Call log:
  - navigating to "http://synology5.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology6.geo.uib.no/
Call log:
  - navigating to "http://synology6.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology7.geo.uib.no/
Call log:
  - navigating to "http://synology7.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology8.geo.uib.no/
Call log:
  - navigating to "http://synology8.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology9.geo.uib.no/
Call log:
  - navigating to "http://synology9.geo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://t1masterlb01.uib.no/
Call log:
  - navigating to "http://t1masterlb01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://t2masterlb01.uib.no/
Call log:
  - navigating to "http://t2masterlb01.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://task.uib.no/
Call log:
  - navigating to "http://task.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://techblog.fribyte.uib.no/
Call log:
  - navigating to "http://techblog.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://techblog.ii.uib.no/
Call log:
  - navigating to "http://techblog.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://terminator.uib.no/
Call log:
  - navigating to "http://terminator.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://terrene.uib.no/
Call log:
  - navigating to "http://terrene.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://terrier.uib.no/
Call log:
  - navigating to "http://terrier.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-app2.cbu.uib.no/
Call log:
  - navigating to "http://test-app2.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-fe.cbu.uib.no/
Call log:
  - navigating to "http://test-fe.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test.iaas.uib.no/
Call log:
  - navigating to "http://test.iaas.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test.uib.no/
Call log:
  - navigating to "http://test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testapp.uib.no/
Call log:
  - navigating to "http://testapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testbool.uib.no/
Call log:
  - navigating to "http://testbool.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testevuw.uib.no/
Call log:
  - navigating to "http://testevuw.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testfpweb.uib.no/
Call log:
  - navigating to "http://testfpweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testing.publisering-test.aws.uib.no/
Call log:
  - navigating to "http://testing.publisering-test.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testnominasjonsweb.uib.no/
Call log:
  - navigating to "http://testnominasjonsweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testnominationweb.uib.no/
Call log:
  - navigating to "http://testnominationweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testnomweb.uib.no/
Call log:
  - navigating to "http://testnomweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testportal.video.uib.no/
Call log:
  - navigating to "http://testportal.video.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testsokw.uib.no/
Call log:
  - navigating to "http://testsokw.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testsokweb.uib.no/
Call log:
  - navigating to "http://testsokweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://teststudweb.uib.no/
Call log:
  - navigating to "http://teststudweb.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testsw.uib.no/
Call log:
  - navigating to "http://testsw.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://thon.uib.no/
Call log:
  - navigating to "http://thon.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://titanic.uib.no/
Call log:
  - navigating to "http://titanic.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tk.beta.uib.no/
Call log:
  - navigating to "http://tk.beta.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tlt07.uib.no/
Call log:
  - navigating to "http://tlt07.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tms.uib.no/
Call log:
  - navigating to "http://tms.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tor.uib.no/
Call log:
  - navigating to "http://tor.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://trac.ii.uib.no/
Call log:
  - navigating to "http://trac.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://traefik.publisering-test.aws.uib.no/
Call log:
  - navigating to "http://traefik.publisering-test.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://traefik.publisering.aws.uib.no/
Call log:
  - navigating to "http://traefik.publisering.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://trud.uib.no/
Call log:
  - navigating to "http://trud.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://trygg.nsd.uib.no/
Call log:
  - navigating to "http://trygg.nsd.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ts4500-hib.uib.no/
Call log:
  - navigating to "http://ts4500-hib.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tsm4500-hib.uib.no/
Call log:
  - navigating to "http://tsm4500-hib.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tsm4500.uib.no/
Call log:
  - navigating to "http://tsm4500.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://turing.uib.no/
Call log:
  - navigating to "http://turing.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ubbstat.h.uib.no/
Call log:
  - navigating to "http://ubbstat.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ubo.uib.no/
Call log:
  - navigating to "http://ubo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ubsc.uib.no/
Call log:
  - navigating to "http://ubsc.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-guest.privnett.uib.no/
Call log:
  - navigating to "http://uib-guest.privnett.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-guest.uib.no/
Call log:
  - navigating to "http://uib-guest.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-san1.uib.no/
Call log:
  - navigating to "http://uib-san1.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-san2.uib.no/
Call log:
  - navigating to "http://uib-san2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-vpn-gw.uib.no/
Call log:
  - navigating to "http://uib-vpn-gw.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ultros.uib.no/
Call log:
  - navigating to "http://ultros.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.app.aws.uib.no/
Call log:
  - navigating to "http://um.app.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.app.uib.no/
Call log:
  - navigating to "http://um.app.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.publisering-test.aws.uib.no/
Call log:
  - navigating to "http://um.publisering-test.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.publisering.aws.uib.no/
Call log:
  - navigating to "http://um.publisering.aws.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://unix.uib.no/
Call log:
  - navigating to "http://unix.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://valiant.uib.no/
Call log:
  - navigating to "http://valiant.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://var.uib.no/
Call log:
  - navigating to "http://var.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ve.uib.no/
Call log:
  - navigating to "http://ve.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://vedlegg.uib.no/
Call log:
  - navigating to "http://vedlegg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://venkman.uib.no/
Call log:
  - navigating to "http://venkman.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://vide.uib.no/
Call log:
  - navigating to "http://vide.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://videoarkiv.dig.uib.no/
Call log:
  - navigating to "http://videoarkiv.dig.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://videokonferanse.uib.no/
Call log:
  - navigating to "http://videokonferanse.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://videonotat.uib.no/
Call log:
  - navigating to "http://videonotat.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://vivarium.h.uib.no/
Call log:
  - navigating to "http://vivarium.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://voices.uib.no/
Call log:
  - navigating to "http://voices.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://von.uib.no/
Call log:
  - navigating to "http://von.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://w2.pilot.uib.no/
Call log:
  - navigating to "http://w2.pilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://w2.sky.uib.no/
Call log:
  - navigating to "http://w2.sky.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://w3docs.h.uib.no/
Call log:
  - navigating to "http://w3docs.h.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://watson.uib.no/
Call log:
  - navigating to "http://watson.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://web-test.fribyte.uib.no/
Call log:
  - navigating to "http://web-test.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.asf.uib.no/
Call log:
  - navigating to "http://webmail.asf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.rf.uib.no/
Call log:
  - navigating to "http://webmail.rf.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.test.uib.no/
Call log:
  - navigating to "http://webmail.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.testapp.uib.no/
Call log:
  - navigating to "http://webmail.testapp.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webscheme.uib.no/
Call log:
  - navigating to "http://webscheme.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://whitespire.ii.uib.no/
Call log:
  - navigating to "http://whitespire.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://wiki.ii.uib.no/
Call log:
  - navigating to "http://wiki.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://wiki.test.uib.no/
Call log:
  - navigating to "http://wiki.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://wikihost.uib.no/
Call log:
  - navigating to "http://wikihost.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.bjerknes.pilot.uib.no/
Call log:
  - navigating to "http://www.bjerknes.pilot.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.blak.uib.no/
Call log:
  - navigating to "http://www.blak.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.bsj.uib.no/
Call log:
  - navigating to "http://www.bsj.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.eecrg.uib.no/
Call log:
  - navigating to "http://www.eecrg.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fft.uib.no/
Call log:
  - navigating to "http://www.fft.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fribyte.uib.no/
Call log:
  - navigating to "http://www.fribyte.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.h2.uib.no/
Call log:
  - navigating to "http://www.h2.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.lingo.uib.no/
Call log:
  - navigating to "http://www.lingo.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.nettkurs.uib.no/
Call log:
  - navigating to "http://www.nettkurs.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.norpol.uib.no/
Call log:
  - navigating to "http://www.norpol.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.norvana.uib.no/
Call log:
  - navigating to "http://www.norvana.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.regler.uib.no/
Call log:
  - navigating to "http://www.regler.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sba.uib.no/
Call log:
  - navigating to "http://www.sba.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sky.uib.no/
Call log:
  - navigating to "http://www.sky.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sokogskriv.uib.no/
Call log:
  - navigating to "http://www.sokogskriv.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stats.cbu.uib.no/
Call log:
  - navigating to "http://www.stats.cbu.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.student.uib.no/
Call log:
  - navigating to "http://www.student.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.test.uib.no/
Call log:
  - navigating to "http://www.test.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.voices.uib.no/
Call log:
  - navigating to "http://www.voices.uib.no/", waiting until "domcontentloaded"
 | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://zen.ii.uib.no/
Call log:
  - navigating to "http://zen.ii.uib.no/", waiting until "domcontentloaded"
 | 1 |
| timeout | 264 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-06-13` | [2026-03-24_09-06-13](results/uib.no/2026-03-24_09-06-13/README.md) |
| `2026-03-24_04-20-56` | [2026-03-24_04-20-56](results/uib.no/2026-03-24_04-20-56/README.md) |
| `2026-03-23_14-35-34` | [2026-03-23_14-35-34](results/uib.no/2026-03-23_14-35-34/README.md) |
| `2026-03-23_14-17-35` | [2026-03-23_14-17-35](results/uib.no/2026-03-23_14-17-35/README.md) |


### [uio.no](results/uio.no/2026-03-23_14-17-50/README.md)

Latest run: `2026-03-23_14-17-50`

| Metric | Count |
|-------:|------:|
| Total domains found | 0 |
| Successes | 0 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-23_14-17-50` | [2026-03-23_14-17-50](results/uio.no/2026-03-23_14-17-50/README.md) |


