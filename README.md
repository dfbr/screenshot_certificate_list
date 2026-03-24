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

> Last updated: 2026-03-24 09:42 UTC

### [dfbp.co.uk](results/dfbp.co.uk/2026-03-24_09-33-12/README.md)

Latest run: `2026-03-24_09-33-12`

| Metric | Count |
|-------:|------:|
| Total domains found | 1 |
| Successes | 0 |
| Page.goto: Navigation to "http://dfbp.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-33-12` | [2026-03-24_09-33-12](results/dfbp.co.uk/2026-03-24_09-33-12/README.md) |


### [dfbr.co.uk](results/dfbr.co.uk/2026-03-24_09-33-31/README.md)

Latest run: `2026-03-24_09-33-31`

| Metric | Count |
|-------:|------:|
| Total domains found | 2 |
| Successes | 1 |
| Page.goto: Navigation to "http://dfbr.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-33-31` | [2026-03-24_09-33-31](results/dfbr.co.uk/2026-03-24_09-33-31/README.md) |


### [experian.co.uk](results/experian.co.uk/2026-03-24_09-33-18/README.md)

Latest run: `2026-03-24_09-33-18`

| Metric | Count |
|-------:|------:|
| Total domains found | 581 |
| Successes | 70 |
| HTTP 400 | 1 |
| HTTP 401 | 1 |
| HTTP 403 | 132 |
| HTTP 404 | 15 |
| HTTP 502 | 2 |
| HTTP 503 | 7 |
| Page.goto: Navigation to "http://car.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://engage.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://outsystems.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://retirementplan.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://www.engage.experian.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: net::ERR_ABORTED at http://data.experian.co.uk/ | 1 |
| Page.goto: net::ERR_ABORTED at http://tags.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://analytics2.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://designstudio.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://emsuweb.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://neartime.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://stg.neartime.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://uat-designstudio.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.identityalarm.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.identitytheft.experian.co.uk/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.privacyguard.experian.co.uk/ | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://goad.experian.co.uk/ | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://mtls-api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://sandbox-mtls-api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_EMPTY_RESPONSE at http://uat-mtls-api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://accdata.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.prestg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.stg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://affordabilitycheck.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://agentux.qat.dsardatacapture.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://analytics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://api-floodre.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://api.prestg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://api.stg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://app.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://app.stg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://archiver-voy.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://automation-companies.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://autonoe-analytics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://autonoe-notebook.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://beta-developer.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://companies.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://creditreporthelp.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev-api-floodre.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev-entitlements-api-enterprise.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev-regulation.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.garlik.api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dqc-dev.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dqc.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dqc.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dsardatacapture.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://earthworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://economics.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://emsquit.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://enrichment-api-enterprise.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eurydome-analytics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://experian-hub.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://help.creditreport.cpp.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hunter.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identityalarm.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitycare.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitycare.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitytheft.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://identitytheft.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://incomeexpend.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://insurance.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jupiterworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://marsworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mercuryworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://morrisonslp.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mortgagesavingstool.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://namstrvrec.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://neptuneworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://openai-app.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://plutoworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://premium.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://preprod.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prestg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://privacyguard.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://privacyguard.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://protectmyidentity.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://protectmyidentity.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://qa-companies.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://qa.garlik.api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://regulation.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://retirementplansecure.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rp.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rpa.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sandboxanalytics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://saturnworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://search.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smetrics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sparkdevlb.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sso-uat-proxy.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sso-uat-proxy.uk.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stage.garlik.api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stat.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stg.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supportportal.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://targetiq.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-archiver-voy.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-entitlements-api-enterprise.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tmp.creditmatcher.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tmp.ins.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tst-outsystems.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tst-regulation.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-api-floodre.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-beta-developer.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-companies.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-enrichment-api-enterprise.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-enrichmentui.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat-experian-hub.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat.dsardatacapture.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uat.identityalarm.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uatworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://venusworkbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://workbench.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.accdata.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.account.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilitycheck.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilitypassport.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilitypassportuserauth.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.affordabilityportal.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.agentux.dsardatacapture.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.agentux.uat.dsardatacapture.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ais.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.alerts.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.analytics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.analytics2.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.analyticsondemand.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ariel-notebook.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.beta-developer.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.boost.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.c1.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.car.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.creditmatcher.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.dashboard.pfs.poc.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.datadisputes.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.designstudio.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.dev-regulation.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.dev.service.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.economics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.economics.uat.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.email.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsquit.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsuquit.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsuweb.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsuweb2.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsweb.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.emsweb2.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.experian-hub.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fedsso.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.forgerock.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fulfillcredit.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fulfilldataaccess.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fulfillment.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.goad.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.home.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.homepage.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.hunter.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.identity.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.incomeexpend.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ins.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.links.rewards.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.lock.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.mbnaidcs.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.mmonline.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.morrisonslocn.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.morrisonslp.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.mtls-api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.myhome.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.neartime.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.offers.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.openai-app.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.pmidvalidation.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.preprod.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.prestg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.preview.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.prodmove.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.profile.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.protect.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.protectmyidentity.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.provider.pfs.poc.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.qa-content.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.qat.dsardatacapture.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.report.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.reportsaver.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.retirementplan.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.retirementplansecure.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.retro-on-demand.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.rp.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sandbox-mtls-api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sandboxanalytics.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.savings.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sbslive.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.score.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.search.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.service.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.servicing.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sfs-e-series.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sso-uat-proxy.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sso-uat-proxy.uk.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg-fedsso.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg-retro-on-demand.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg.neartime.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg.pcod.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg1-preview.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stg1.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.support.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.supporthub.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.trusso.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.tst-regulation.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-beta-developer.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-designstudio.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-experian-hub.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-investigatoronline.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-mtls-api.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat-supporthub.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat.mbnaidcs.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.uat.service.experian.co.uk/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.ukrsotsbank.experian.co.uk/ | 1 |
| timeout | 130 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-33-18` | [2026-03-24_09-33-18](results/experian.co.uk/2026-03-24_09-33-18/README.md) |
| `2026-03-24_09-06-20` | [2026-03-24_09-06-20](results/experian.co.uk/2026-03-24_09-06-20/README.md) |
| `2026-03-24_04-21-03` | [2026-03-24_04-21-03](results/experian.co.uk/2026-03-24_04-21-03/README.md) |
| `2026-03-23_14-35-34` | [2026-03-23_14-35-34](results/experian.co.uk/2026-03-23_14-35-34/README.md) |


### [rowanpage.co.uk](results/rowanpage.co.uk/2026-03-24_09-33-16/README.md)

Latest run: `2026-03-24_09-33-16`

| Metric | Count |
|-------:|------:|
| Total domains found | 2 |
| Successes | 0 |
| Page.goto: Navigation to "http://rowanpage.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://www.rowanpage.co.uk/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-33-16` | [2026-03-24_09-33-16](results/rowanpage.co.uk/2026-03-24_09-33-16/README.md) |


### [uib.no](results/uib.no/2026-03-24_09-33-14/README.md)

Latest run: `2026-03-24_09-33-14`

| Metric | Count |
|-------:|------:|
| Total domains found | 1086 |
| Successes | 159 |
| HTTP 401 | 1 |
| HTTP 403 | 22 |
| HTTP 404 | 3 |
| HTTP 502 | 1 |
| HTTP 503 | 2 |
| Page.goto: Navigation to "http://anno.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://autodiscover.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://board.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://bsj.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://chat.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://dialin.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://epos-no.geo.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://esignering.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://esm.dev.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://esm.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://faktura.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://files.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://geoip.app.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://grind.h.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://hackmd.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://half.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://holberg.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://ithjelp.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://kb.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://konferanse.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://koronachat.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://mautic.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://meet.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://mirrors.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://nettkurs.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://nettspansk.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://ordapi.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://ordbank-api.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://p1masterlb.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://pgboard.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://ping.app.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://pita.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://registry-bgo.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://rino.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://search.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://sfb-webext01.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://skjemaker.test.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://soju.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://stats.test.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://streaming.videonotat.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://sujo-test.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://sujo.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://tilbakemelding.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://tm.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://ujour.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://venner.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://videoconference.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://vlerce.skytest.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://vurdering.test.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://webmail.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://wptest2.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://wptest3.skyapp.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://www.jper.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://www.sars.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://www2.ii.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: Navigation to "http://yum.uib.no/" is interrupted by another navigation to "chrome-error://chromewebdata/" | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://c.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://w3.pilot.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://www.fragment.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_COMMON_NAME_INVALID at http://www.pilot.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://bldl.ii.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://dataviz.app.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://gitops.skyapp.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://lesebag.skyapp.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://news.skyapp.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://read.app.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://rebell.app.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://rebell.skyapp.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://vault.skyapp.uib.no/ | 1 |
| Page.goto: net::ERR_CERT_DATE_INVALID at http://wptest1.skyapp.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://ganeti.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://i2s.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://munin.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://nagios.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://newsangler.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://noralf.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://puppet.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.i2s.uib.no/ | 1 |
| Page.goto: net::ERR_CONNECTION_REFUSED at http://www.newsangler.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://adm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://admin.bjerknes.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://agamemnon.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ajax.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://akuttmedisin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://alertmanager.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://alexandria.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://alumni.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://angelica.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://antivirus.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://apendix2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://apicanvas.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://apsara.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://arkiv.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://atrium.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://attika.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://attila.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://audionovela.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://baia-lab.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bdcj.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bergmus.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bgrg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bigfoot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bigs.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts02.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts03.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts04.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts05.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts06.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://biostudent-ts07.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bjerknes.pilot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blak.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blak.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blowfly-test.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bluesky.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://blustar.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://booking.infomedia.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://boolean.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://borodino.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://brage.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://britannic.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://brokk.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://brosing.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://buf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://buoyant.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://bure.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://callmoo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://camperdown.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cerberus.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cgps.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://char.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cisco.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cismacinternal.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ck-vi.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://clortho.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cmc.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://cmg01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://collingwood.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://colossus6.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://colossus7.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://convection.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://corellia.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://crush.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://crypt.clortho.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://crysis.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dac2000.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dashboard.iaas.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://datatest.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dbh.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dep.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dev.supermag.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dhcpadmintest.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dig.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://digital-ub.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dikultba.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dill.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dimp.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dioto.skolelab.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dioto.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://docs.hpc.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://docs.ub.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dorothyjdankel.b.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://double6.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://dreistadt.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://driva.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eclipse.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://edgepool.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eecrg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://efn2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eiktorn.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eitre.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eksamen.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eksark.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ekstern-filer.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ekt.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://elkat.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://emojivoto.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://engfly.bccs.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://enterprise.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://epay.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eplebakst.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eplebakst1.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://epletre.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eprint.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://essdata.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://eurosphere.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exch.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exchange01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exchange02.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://exchange03.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://executor.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://f.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fdu.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://felleskalender.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ferdighetssenteret.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fft.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://flightgear.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://float.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://flyt.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://folk7.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://foobar.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://foreman.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://forskerskolen.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://fulla.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://g.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gdcj.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gfi063011.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ggzgamingzone.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://git.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://git.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlab-ci.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlab.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlab.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gitlabp1.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gnome.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://grafana.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gran.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://grind.app.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gru.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://gunnlod.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://havanna.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hibagon.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hild.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hilton.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hogushg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hoguslg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hospits.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hostel.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hoth.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://humle.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hvitgran.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://hyperion.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.rf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.samfunnet.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.student.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imbooking.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imdb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://impero.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://impmail.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://industri.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://inf101.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://inn.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://interaktiv.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://interaktiv6.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://intern-filer.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-admin-292.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-policy-292.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-policy-351.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ise-pxgrid-351.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://itida.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://itschemistry.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ivalde.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://iwanttousetheoldversion.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jb.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jenkins.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jensen.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jira.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jupyter-test.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://jupyter.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://karib.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://karlh.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ki.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kibana.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kirishima.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://knutsinserver.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kurs7.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://kvase.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lakrisrot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lelle.publisering-test.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://leuven.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lingo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://link.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://linkerd.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://logstash.clortho.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://logstash.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lunde.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lydia2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lydiatest2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lync.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lync02.video.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lyncadmin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lyncdiscover.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lyncdiscoverinternal.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lynctlf1.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://lynctlf2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://m.grind.app.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://m.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://macadmin.clortho.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://macadmin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://magneto.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mail.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mailman.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://marat.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://marimbaconsole.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://masterark.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mattermost.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mdm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mediasite.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://medvizvcbm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://meet.gfi.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://melon.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://melonny.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://meltzer.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://metiri.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://micromdm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://min.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mine.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://minside.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mirror.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://miside.felleskalender.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://miside.pilot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://miside.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mobileprint.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mobilprint.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://monarch.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://moodle.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://moodlehost.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munki.clortho.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munkiwebadmin.clortho.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://munkiwebadmin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mx1.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://my.traefik.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://my.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://myspace.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://mysql.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://naf2009.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nafa.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://naglfar.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://namur.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nav-repo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://neolatin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nesstar-dev.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://netdata.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://netdata.publisering-test.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://netdata.publisering.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nett8.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nettfransk.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nettitaliensk.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nito.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nominasjonsweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nominationweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nomweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://normt.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://norpol.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://norvana.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nps.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nps1.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nps2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ntl.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://nybs.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ocs.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://olivetree.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://olympiade.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://omod.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://oncomatrix.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://onedrive.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://opencsw.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ordbruker.testapp.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://org7.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://orontes.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://outlook.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://outlook2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1box01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1eia01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1gitlab01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1masterlb01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1oppdrag01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1ordlb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1osd01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1piwik01.app.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1redirect01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1rts01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1sak01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p1wiki01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2gitlab01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2masterlb01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2oppdrag01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2ordlb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2redirect01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2rts01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://p2sak01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://people.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pepperrot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://perepigenomics.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://persille.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://phdportal.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://piwik.app.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pkg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://plikt.gfi.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pollen.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.rf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.student.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://portal.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://portal.video.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://postgres.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://preface.b.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://presence.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pretest.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prom.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.eia.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.it.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosjekt.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prosopopeia.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://prospective.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://proxy-gw.privnett.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://proxy-gw1.privnett.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://proxy-gw2.privnett.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://puffin-test.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://puffin.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://purlmoo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pushgateway.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radiance.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radisson.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radisson7.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radius.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radius1.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://radius2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ramillies.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rasmus.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rd-sh02.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rdb.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://real.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://record.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://redirect.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://redirect1.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://redmine.it.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://regler.publisering-test.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://replay.video.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://resources.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://resp.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://resp2.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://retting.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rettspraksis.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rhel.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rk-drupal.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://romulus.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rosenrot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rosmarin.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rowan.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://rts.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://safir.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sandwich.medicine.b.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sardis2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sba.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sba.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-ac1.klient.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-ac2.klient.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-cm.klient.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sc12-cm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://scalacm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://scholar.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://scom-sql02.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sddownloads.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://search.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sebra.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sebrapilot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://secure-video.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sefas.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://seqlab.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://seqlab.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://serveradm.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://serveradmin.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://service.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fe01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fe02.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fe03.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-fepool01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sfb-webpool01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://shepherd.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker-skjema.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker-vbackend.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker-vturn.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikker.filer.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikkert-video.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sikre.filer.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sinmara.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sip.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sip2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://siv.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skjema.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skjemaker.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skolevalg1.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skolevalg2.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://skrotogskriv.app.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smtp.asf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smtp.rf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://smtp.samfunnet.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://snipeit-test.dig.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://software.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sokogskriv.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sokweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://space.rokkan.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://spaced.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ssis.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stargazer.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stats.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stats2.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stjerne.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://stokkstein.ss.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://strategi.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://streaming.mh.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://streaming.videonotat.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://string.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://structure.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studblogg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studentblogg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studentportal.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://studweb0.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://substr.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://subversion.ift.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://subversion.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sudan.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sunlight.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supermag.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supermagx.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://supertimon.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://support.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sus.infomedia.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://svar.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://svn.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://sw.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology1.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology2.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology3.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology4.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology5.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology6.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology7.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology8.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://synology9.geo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://t1masterlb01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://t2masterlb01.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://task.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://techblog.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://techblog.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://terminator.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://terrene.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://terrier.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-app2.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test-fe.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test.iaas.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testapp.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testbool.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testevuw.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testfpweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testing.publisering-test.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testnominasjonsweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testnominationweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testnomweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testportal.video.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testsokw.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testsokweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://teststudweb.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://testsw.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://thon.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://titanic.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tk.beta.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tlt07.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tms.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tor.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://trac.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://traefik.publisering-test.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://traefik.publisering.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://trud.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://trygg.nsd.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ts4500-hib.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tsm4500-hib.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://tsm4500.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://turing.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ubbstat.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ubo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ubsc.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-guest.privnett.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-guest.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-san1.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-san2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://uib-vpn-gw.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ultros.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.app.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.app.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.publisering-test.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://um.publisering.aws.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://unix.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://valiant.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://var.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://ve.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://vedlegg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://venkman.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://vide.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://videoarkiv.dig.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://videokonferanse.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://videonotat.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://vivarium.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://voices.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://von.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://w2.pilot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://w2.sky.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://w3docs.h.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://watson.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://web-test.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.asf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.rf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webmail.testapp.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://webscheme.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://whitespire.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://wiki.ii.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://wiki.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://wikihost.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.bjerknes.pilot.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.blak.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.bsj.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.eecrg.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fft.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.fribyte.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.h2.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.lingo.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.nettkurs.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.norpol.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.norvana.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.regler.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sba.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sky.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.sokogskriv.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.stats.cbu.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.student.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.test.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://www.voices.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://zen.ii.uib.no/ | 1 |
| timeout | 258 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-24_09-33-14` | [2026-03-24_09-33-14](results/uib.no/2026-03-24_09-33-14/README.md) |
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


