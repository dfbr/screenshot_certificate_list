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

> Last updated: 2026-03-25 17:39 UTC

### [dfbp.co.uk](results/dfbp.co.uk/2026-03-25_17-10-28/README.md)

Latest run: `2026-03-25_17-10-28`

| Metric | Count |
|-------:|------:|
| Total domains found | 1 |
| Successes | 0 |
| HTTP 404 | 1 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-25_17-10-28` | [2026-03-25_17-10-28](results/dfbp.co.uk/2026-03-25_17-10-28/README.md) |
| `2026-03-25_13-21-26` | [2026-03-25_13-21-26](results/dfbp.co.uk/2026-03-25_13-21-26/README.md) |
| `2026-03-25_10-40-33` | [2026-03-25_10-40-33](results/dfbp.co.uk/2026-03-25_10-40-33/README.md) |
| `2026-03-25_04-21-54` | [2026-03-25_04-21-54](results/dfbp.co.uk/2026-03-25_04-21-54/README.md) |
| `2026-03-24_14-02-25` | [2026-03-24_14-02-25](results/dfbp.co.uk/2026-03-24_14-02-25/README.md) |
| `2026-03-24_12-35-29` | [2026-03-24_12-35-29](results/dfbp.co.uk/2026-03-24_12-35-29/README.md) |
| `2026-03-24_09-33-12` | [2026-03-24_09-33-12](results/dfbp.co.uk/2026-03-24_09-33-12/README.md) |


### [dfbr.co.uk](results/dfbr.co.uk/2026-03-25_17-10-25/README.md)

Latest run: `2026-03-25_17-10-25`

| Metric | Count |
|-------:|------:|
| Total domains found | 2 |
| Successes | 1 |
| HTTP 404 | 1 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-25_17-10-25` | [2026-03-25_17-10-25](results/dfbr.co.uk/2026-03-25_17-10-25/README.md) |
| `2026-03-25_13-21-41` | [2026-03-25_13-21-41](results/dfbr.co.uk/2026-03-25_13-21-41/README.md) |
| `2026-03-25_10-40-25` | [2026-03-25_10-40-25](results/dfbr.co.uk/2026-03-25_10-40-25/README.md) |
| `2026-03-25_04-21-54` | [2026-03-25_04-21-54](results/dfbr.co.uk/2026-03-25_04-21-54/README.md) |
| `2026-03-24_14-02-26` | [2026-03-24_14-02-26](results/dfbr.co.uk/2026-03-24_14-02-26/README.md) |
| `2026-03-24_12-35-31` | [2026-03-24_12-35-31](results/dfbr.co.uk/2026-03-24_12-35-31/README.md) |
| `2026-03-24_09-33-31` | [2026-03-24_09-33-31](results/dfbr.co.uk/2026-03-24_09-33-31/README.md) |


### [fitforhospital.co.uk](results/fitforhospital.co.uk/2026-03-25_17-10-22/README.md)

Latest run: `2026-03-25_17-10-22`

| Metric | Count |
|-------:|------:|
| Total domains found | 1 |
| Successes | 1 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-25_17-10-22` | [2026-03-25_17-10-22](results/fitforhospital.co.uk/2026-03-25_17-10-22/README.md) |
| `2026-03-25_13-21-30` | [2026-03-25_13-21-30](results/fitforhospital.co.uk/2026-03-25_13-21-30/README.md) |
| `2026-03-25_10-40-29` | [2026-03-25_10-40-29](results/fitforhospital.co.uk/2026-03-25_10-40-29/README.md) |


### [onlythestoriesyouwant.link](results/onlythestoriesyouwant.link/2026-03-25_17-10-18/README.md)

Latest run: `2026-03-25_17-10-18`

| Metric | Count |
|-------:|------:|
| Total domains found | 2 |
| Successes | 2 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-25_17-10-18` | [2026-03-25_17-10-18](results/onlythestoriesyouwant.link/2026-03-25_17-10-18/README.md) |
| `2026-03-25_13-21-36` | [2026-03-25_13-21-36](results/onlythestoriesyouwant.link/2026-03-25_13-21-36/README.md) |
| `2026-03-25_10-40-41` | [2026-03-25_10-40-41](results/onlythestoriesyouwant.link/2026-03-25_10-40-41/README.md) |


### [rowanpage.co.uk](results/rowanpage.co.uk/2026-03-25_17-10-18/README.md)

Latest run: `2026-03-25_17-10-18`

| Metric | Count |
|-------:|------:|
| Total domains found | 2 |
| Successes | 0 |
| HTTP 404 | 2 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-25_17-10-18` | [2026-03-25_17-10-18](results/rowanpage.co.uk/2026-03-25_17-10-18/README.md) |
| `2026-03-25_13-21-41` | [2026-03-25_13-21-41](results/rowanpage.co.uk/2026-03-25_13-21-41/README.md) |
| `2026-03-25_10-40-31` | [2026-03-25_10-40-31](results/rowanpage.co.uk/2026-03-25_10-40-31/README.md) |
| `2026-03-25_04-21-59` | [2026-03-25_04-21-59](results/rowanpage.co.uk/2026-03-25_04-21-59/README.md) |
| `2026-03-24_14-02-19` | [2026-03-24_14-02-19](results/rowanpage.co.uk/2026-03-24_14-02-19/README.md) |
| `2026-03-24_12-35-27` | [2026-03-24_12-35-27](results/rowanpage.co.uk/2026-03-24_12-35-27/README.md) |
| `2026-03-24_09-33-16` | [2026-03-24_09-33-16](results/rowanpage.co.uk/2026-03-24_09-33-16/README.md) |


### [uib.no](results/uib.no/2026-03-25_17-10-36/README.md)

Latest run: `2026-03-25_17-10-36`

| Metric | Count |
|-------:|------:|
| Total domains found | 1086 |
| Successes | 210 |
| HTTP 400 | 1 |
| HTTP 401 | 1 |
| HTTP 403 | 23 |
| HTTP 404 | 4 |
| HTTP 409 | 2 |
| HTTP 502 | 10 |
| HTTP 503 | 5 |
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
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://beta.asf.uib.no/ | 1 |
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
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://imap.asf.uib.no/ | 1 |
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
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.asf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.rf.uib.no/ | 1 |
| Page.goto: net::ERR_NAME_NOT_RESOLVED at http://pop.samfunnet.uib.no/ | 1 |
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
| timeout | 259 |

Previous runs:

| Run | Link |
|-----|------|
| `2026-03-25_17-10-36` | [2026-03-25_17-10-36](results/uib.no/2026-03-25_17-10-36/README.md) |
| `2026-03-25_13-21-31` | [2026-03-25_13-21-31](results/uib.no/2026-03-25_13-21-31/README.md) |
| `2026-03-25_10-40-30` | [2026-03-25_10-40-30](results/uib.no/2026-03-25_10-40-30/README.md) |
| `2026-03-25_04-21-54` | [2026-03-25_04-21-54](results/uib.no/2026-03-25_04-21-54/README.md) |
| `2026-03-24_14-02-35` | [2026-03-24_14-02-35](results/uib.no/2026-03-24_14-02-35/README.md) |
| `2026-03-24_12-35-32` | [2026-03-24_12-35-32](results/uib.no/2026-03-24_12-35-32/README.md) |
| `2026-03-24_09-33-14` | [2026-03-24_09-33-14](results/uib.no/2026-03-24_09-33-14/README.md) |
| `2026-03-24_09-06-13` | [2026-03-24_09-06-13](results/uib.no/2026-03-24_09-06-13/README.md) |


