# apartment-hunt

Pulls rental listings for a chosen city from Craigslist, directly-fetched
aggregator/manager pages, anti-bot-blocked or JS-only sites via Firecrawl
structured extraction, Exa neural search across the rental web + Reddit, and
Zillow via Firecrawl (paginated across 3 pages). It dedupes against a per-city
seen-set, writes `digest_<city>_latest.md`, and archives dated markdown digests
in `digests/<city>/`.

## Cities

Everything city-specific (criteria, neighborhoods, ZIP rules, every source URL,
Zillow bounds, Exa query strings) lives in `profiles.py`. Two ship today:

- **`sf`** (default) — Annabel's 3BR Russian Hill / North Beach hunt, unchanged.
- **`denver`** — whole-metro 3BR, wide budget, no required neighborhood.

Pick one with `--city`:

```bash
.venv/bin/python apartment_hunt.py --city denver
.venv/bin/python build_html_digest.py --city denver
```

To add a city, copy a `SearchProfile` in `profiles.py`, swap the URLs/labels,
and add it to `PROFILES`. Craigslist, Zillow, and the Exa city sweep are the
robust backbone; hand-tuned aggregator URLs that turn out wrong just show up as
`error`/`blocked` in the coverage report and fall back to Exa.

## Sources

Each profile names its own seed URLs. The shapes are the same per city:

- **Craigslist** the city's CL region
- **Direct fetch** aggregator/manager pages that return inventory in raw HTML
- **Firecrawl-routed** anti-bot-blocked or JS-only aggregators + property managers
- **Zillow via Firecrawl** (paginated, 3 pages, per-city map bounds)
- **Exa neural search** across the city (per-hood where curated) + Reddit +
  aggregator detail pages

SF ships the full ~37-source set. Denver ships the cross-city backbone (CL,
Zillow, the major aggregators, Exa); add local property managers to its profile
as you find them.

## Criteria (edit in `profiles.py`)

**SF** (`sf`):
- 3BR, ideal max $7,500/mo ($2,500/person for 3), stretch $9,000
- top priority Russian Hill, North Beach; fallback Hayes Valley, Marina,
  Pacific Heights, Cow Hollow, Nob Hill
- hard no: Tenderloin, TenderNob, Lower Nob, Polk Gulch, Civic Center, South Beach
- move by 2026-06-15

**Denver** (`denver`):
- 3BR, wide budget (ideal max $4,500, stretch $7,000), whole metro (no required
  neighborhood). Tighten these in `profiles.py` once the friends settle on a
  budget/area.

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
<https://www.firecrawl.dev/app/api-keys>) into `.env`. Without it, Zillow and
every Firecrawl-routed aggregator/manager is skipped. The pipeline still runs on
the rest, but you'll miss most of the real inventory.

## Run

```bash
# Full run for SF (writes digest + dated archive, then updates seen-set)
.venv/bin/python apartment_hunt.py

# Run Denver instead
.venv/bin/python apartment_hunt.py --city denver

# Dry run (writes digest only, no seen-set update)
.venv/bin/python apartment_hunt.py --city denver --dry

# Wipe a city's seen-set (next run resurfaces everything)
.venv/bin/python apartment_hunt.py --city denver --reset

# Styled HTML page (writes digest_<city>_latest.html + a copy on the Desktop)
.venv/bin/python build_html_digest.py --city denver
```

Latest markdown digest is at `digest_<city>_latest.md`; styled HTML at
`digest_<city>_latest.html`. Dated archives in `digests/<city>/`.

Each digest includes a **Direct source coverage** section showing which public
source pages were reachable directly, which were blocked/rate-limited, and how
many raw listing candidates were parsed before the normal criteria filters ran.

## Schedule

To run both cities daily at 9am, add to
`~/Documents/AI-OS/projects/apartment-hunt/crontab.txt`:

```
0 9 * * * cd ~/Documents/AI-OS/projects/apartment-hunt && .venv/bin/python apartment_hunt.py --city sf >> logs/cron.log 2>&1
5 9 * * * cd ~/Documents/AI-OS/projects/apartment-hunt && .venv/bin/python apartment_hunt.py --city denver >> logs/cron.log 2>&1
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

- `apartment_hunt.py` — the scrape/filter/digest pipeline
- `profiles.py` — per-city search profiles (criteria, neighborhoods, source URLs)
- `build_html_digest.py` — renders the styled HTML page (Editorial Cream)
- `seen_<city>.json` — listing IDs already shown for that city (auto-managed)
- `notes/` — change notes for each material edit to the pipeline (one file per change)
- `digest_<city>_latest.md` / `digest_<city>_latest.html` — most recent digest
- `digests/<city>/YYYY-MM-DD.md` — archive
