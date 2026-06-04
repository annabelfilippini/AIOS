# 2026-06-03 — Firecrawl source rollout (21 sites)

## What changed

Migrated 21 sites from direct-fetch (which was returning 403, 429, or empty React shells) to Firecrawl's `/v1/scrape` with structured JSON extraction. Same approach as Zillow, but generalized so one LLM-extraction schema works across all 21 layouts.

## Why

Spot-check on 2026-06-03 showed two confirmed cases where direct fetch returned 0 listings but Firecrawl-rendered HTML had real inventory:

- **compass.com**: direct 0, Firecrawl 84 SF rentals (~8 are 3BR)
- **avaloncommunities.com**: direct 0, Firecrawl 81 SF apartments (~11 are 3BR)

Annabel asked "those sites really have nothing?" — they didn't have nothing, my scraper just couldn't see them.

## Architecture

Three source tiers now:

1. **Direct-fetch** (`DIRECT_SOURCE_SEEDS`): sites that return inventory in raw HTML. 8 sites remaining (apartmentguide, homefinder, redfin, rentable, rentberry, rentcafe, rentsfnow, structureproperties). Cheap, no per-call API cost.
2. **Firecrawl-routed** (`FIRECRAWL_SEEDS`): anti-bot-blocked or JS-only sites. 21 sites. Each call uses Firecrawl's `formats: ["json"]` + `jsonOptions.schema` to ask the LLM to pull `{title, url, price_per_month, bedrooms, address, neighborhood}` from each page. ~5-10 credits per call.
3. **Zillow** (`fetch_zillow_firecrawl`): special-cased with pagination across pages 1-3 because Zillow embeds everything in a stable `__NEXT_DATA__` JSON blob and a regex parse is cheaper + more reliable than LLM extraction for them.

Plus Craigslist and Exa stay as before.

## Sites migrated to Firecrawl

**Anti-bot blocked (return 403/429 to direct fetch):**
apartments.com · apartmentfinder.com · apartmenthomeliving.com · apartmentlist.com · equityapartments.com · forrent.com · hotpads.com · realtor.com · renthop.com · trulia.com

**JS-only aggregators (return 200 but empty React shell):**
avaloncommunities.com · compass.com · padmapper.com · rent.com · zumper.com

**SF property managers (JS-only listing widgets):**
chandlerproperties.com · gaetanirealestate.com · jwavro.com · sfcityrents.com · trinitysf.com · yeeproperties.com

## Sites left as direct-fetch

apartmentguide.com · homefinder.com · redfin.com · rentable.co · rentberry.com · rentcafe.com · rentsfnow.com · structureproperties.com — all return real inventory in raw HTML; no benefit from Firecrawl.

## Sites dropped entirely (commented out)

anchorrealtyinc.com (DNS dead) · brickandtimber.com (404) · kinetic-re.com (DNS dead) · laphamcompany.com (404). Re-add if their URLs come back to life.

## Cost

Per run: 21 Firecrawl calls (LLM extraction) + 3 Zillow calls (HTML parsing) ≈ 150-200 credits per run.
Per month (daily cron): ~4,500-6,000 credits/month. Firecrawl free tier is 500/month; paid tiers start at 100K for $19/mo. Well within reason.

## Filter compatibility

Added `firecrawl:` to the same `keep()` guard that already applies to `direct:` and `exa:` sources (requires rental hints in haystack + parseable bed count). This keeps the LLM extraction honest — if it hallucinates a non-listing, the filter drops it.

## To verify

```bash
cd ~/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py --reset
.venv/bin/python apartment_hunt.py --dry
```

Expect: pipeline now prints `Fetching 21 JS-only / blocked sources via Firecrawl…` followed by a candidate count.

## Honest result on first run

Match count did NOT rise meaningfully (still ~12 vs. pre-rollout's 12). The rollout returned 85-130 raw candidates from Firecrawl-routed sources but nearly all were correctly dropped because:

- Most aggregator SF 3BR inventory is in SoMa / Mission / Bayview / Parkmerced / Dogpatch / Civic — outside the target 7 neighborhoods.
- The ones that landed in target hoods were over the $9,000 ceiling (e.g., 1935 Jefferson Marina at $12,700, 1107 Broadway at $23,589).
- Large complexes (Avalon, Equity) had the LLM extract their cheapest "starting at" 1BR price rather than the 3BR-specific listing, so beds/price both filtered them out.

**The off-Zillow 3BR market in Russian Hill / North Beach / Hayes Valley / Marina / Pac Heights / Cow Hollow / Nob Hill at ≤$9,000 is genuinely thin.** The 12-listing surface is close to complete coverage for that combination.

## Bugs found and fixed during the rollout

1. **`-1` price sentinel.** LLM uses `-1` (and sometimes `0`) for "no price shown" listings. Now normalized to `None` so they don't trip the `< MIN_PRICE` check.
2. **Renthop returned NYC listings.** Their SF URL appears to fall back to NYC inventory. Dropped from `FIRECRAWL_SEEDS`.
3. **5 sites timed out at 408 SCRAPE_TIMEOUT** (apartmentfinder, apartmenthomeliving, trulia, compass, zumper). Bumped Firecrawl `waitFor` from 3500ms → 5000ms and added explicit Firecrawl-side `timeout: 90000`. Request-side timeout raised from 120s → 180s.
