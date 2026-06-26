# 2026-06-17 — multi-city profiles + Editorial Cream HTML

## Why

Two asks: (1) make the results page nicer, (2) let the tool search other metros
(a friend group hunting in Denver), not just SF.

## What changed

### New `profiles.py`

All city-specific data moved out of `apartment_hunt.py` into a `SearchProfile`
dataclass and a `PROFILES` registry. A profile holds criteria, neighborhood
lists, Craigslist/ZIP rules, every source seed URL, Zillow map bounds + search
term, and the Exa query neighborhoods.

- `sf` — Annabel's exact prior hunt, behavior unchanged.
- `denver` — whole-metro 3BR, wide budget (ideal $4,500 / stretch $7,000),
  `require_neighborhood_match=False`.

### `apartment_hunt.py`

- `apply_profile(profile)` rebinds the module-level config the pipeline already
  reads; SF is applied at import so importers still work. `main()` takes
  `--city {sf,denver}` (default `sf`).
- Generalized the SF-only logic:
  - ZIP helpers are now profile-driven: `_has_wrong_city_zip` (region ZIP in the
    wrong metro), `_has_nontarget_city_zip` (in-city but off-target, only when a
    target-ZIP list exists), `_in_city` (whole-metro validation).
  - `keep()` branches on `REQUIRE_NEIGHBORHOOD_MATCH`. SF still requires a target
    hood/ZIP; Denver accepts anything proven in-metro (matched hood OR in-city
    ZIP OR city name in text). A matched hood alone counts as in-city — without
    that, a Craigslist "LoHi" listing with no "Denver"/ZIP in its text was dropped.
  - Blocked-neighborhood markers, neighborhood rank, Exa query strings, Zillow
    bounds/search-term, seen/digest/archive paths all come from the profile.
  - Exa sweep collapses to one city-wide query when a profile has no curated
    `exa_neighborhoods`, so a 40-hood metro doesn't blow up credit usage.
- Per-city files: `seen_<city>.json`, `digest_<city>_latest.md`,
  `digests/<city>/<date>.md`.

### `build_html_digest.py` — Editorial Cream restyle

- Rebuilt to the global design standard: Cormorant Garamond display, Jost
  labels, monospace figures, cream background, single brass accent, squared
  corners, hairline warm borders, no helper subtitles, no dashes as punctuation.
- City-aware header + `--city`. SF keeps Top picks / Fallback; whole-metro cities
  get a single price-sorted section.
- Bug fix: it now references `apartment_hunt` config dynamically (`ah.X`) instead
  of import-time copies, and buckets into preferred/fallback/**other** so
  listings without a recognized neighborhood are never silently dropped.

## Verification

- `py_compile` on all three modules.
- Unit-style `keep()` checks for both cities: SF keeps Russian Hill, blocks
  Tenderloin, drops Oakland ZIP; Denver keeps LoHi/no-hood Denver, drops Boulder
  ZIP, drops non-Denver, drops over-budget.
- Rendered sample SF + Denver pages, screenshotted in browser, confirmed the
  Editorial Cream styling and both layouts. Computed styles checked
  (cream bg, Cormorant 46px h1, mono prices, 0px radius, brass View links).

## Not done / open

- No API keys in `.env` yet (no `.env` exists), so no live Denver pull was run.
  Add `EXA_API_KEY` (required) and `FIRECRAWL_API_KEY` (recommended) to go live.
- Denver property-manager list is empty; relies on Exa open-web + r/Denver.
- A few Denver aggregator URLs are constructed by analogy; wrong ones will show
  as error/blocked in coverage and fall back to Exa.
