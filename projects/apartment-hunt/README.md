# apartment-hunt

Pulls SF rental listings from Craigslist, 8 directly-fetched aggregator/manager
pages, 21 anti-bot-blocked or JS-only sites via Firecrawl structured extraction,
Exa neural search across the rental web + Reddit, and Zillow via Firecrawl
(paginated across 3 pages). It dedupes against a local seen-set, writes
`digest_latest.md`, and archives dated markdown digests in `digests/`.

## Sources (37 total)

- **Craigslist** sfbay/sfc
- **Direct fetch** (8): apartmentguide.com, homefinder.com, redfin.com,
  rentable.co, rentberry.com, rentcafe.com, rentsfnow.com, structureproperties.com
- **Firecrawl-routed** (21): apartments.com, apartmentfinder.com,
  apartmenthomeliving.com, apartmentlist.com, avaloncommunities.com, compass.com,
  equityapartments.com, forrent.com, hotpads.com, padmapper.com, realtor.com,
  rent.com, renthop.com, trulia.com, zumper.com, chandlerproperties.com,
  gaetanirealestate.com, jwavro.com, sfcityrents.com, trinitysf.com, yeeproperties.com
- **Zillow via Firecrawl** (paginated, 3 pages)
- **Exa neural search** across 7 target neighborhoods + Reddit + property
  managers + aggregator detail pages

## Criteria (edit in `apartment_hunt.py`)

- 3BR only
- ideal max $7,500/mo ($2,500/person for 3 people)
- stretch max $9,000/mo for unusually good fits
- top priority: Russian Hill, North Beach
- fallback: Hayes Valley, Marina, Pacific Heights, Cow Hollow, Nob Hill
- hard no: Tenderloin, TenderNob, Lower Nob, Polk Gulch, Civic Center, South Beach
- Move-in by 2026-06-15

## Setup

```bash
cd ~/Documents/AI-OS/projects/apartment-hunt
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Add your Exa key
cp .env.example .env
# edit .env, paste EXA_API_KEY
```

**Strongly recommended:** paste a `FIRECRAWL_API_KEY` (from
<https://www.firecrawl.dev/app/api-keys>) into `.env`. Without it, **22 of 37
sources are skipped** (Zillow + the 21 Firecrawl-routed aggregators and
managers). The pipeline still runs on the rest, but you'll miss most of the
real inventory.

## Run

```bash
# Full run (writes digest + dated archive, then updates seen-set)
.venv/bin/python apartment_hunt.py

# Dry run (writes digest only, no seen-set update)
.venv/bin/python apartment_hunt.py --dry

# Wipe seen-set (next run resurfaces everything)
.venv/bin/python apartment_hunt.py --reset
```

Latest digest is always at `digest_latest.md`. Dated archives in `digests/`.

Each digest includes a **Direct source coverage** section showing which public
source pages were reachable directly, which were blocked/rate-limited, and how
many raw listing candidates were parsed before the normal criteria filters ran.

## Schedule

To run daily at 9am, add to `~/Documents/AI-OS/projects/apartment-hunt/crontab.txt`:

```
0 9 * * * cd ~/Documents/AI-OS/projects/apartment-hunt && .venv/bin/python apartment_hunt.py >> logs/cron.log 2>&1
```

Then `crontab crontab.txt` to install.

## What it doesn't do

- **No login bypass or anti-bot evasion.** Authenticated sources can be added
  when Annabel explicitly provides access and the site permits it, but this tool
  does not bypass CAPTCHAs, scrape private sessions without permission, or evade
  access controls.
- **No guaranteed complete aggregator inventory.** The tracker directly checks
  public source pages where possible and uses Exa as fallback coverage for
  sites that serve block pages or JavaScript-only shells.
- **No images.** Listings link out; click through to see photos.
- **No price history or trend tracking.** Just "what's new since yesterday."

## Files

- `apartment_hunt.py` — the whole tool
- `seen_3br_sf_core.json` — listing IDs we've already shown for this 3BR SF search (auto-managed)
- `notes/` — change notes for each material edit to the pipeline (one file per change)
- `digest_latest.md` — most recent digest
- `digests/YYYY-MM-DD.md` — archive
