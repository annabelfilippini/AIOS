---
date: 2026-06-17
time: 15:37
project: apartment-hunt
status: DONE (pending live run) — Multi-city refactor + Editorial Cream HTML restyle shipped and verified against sample data in browser. Cannot do a live Denver pull until API keys are added to .env (none exists yet).
---

# Session: apartment-hunt — multi-city profiles + Editorial Cream UX

## Context

Annabel asked to find her apartment finder, improve the UX, and make it search
other metros (a friend group hunting in Denver). The whole `projects/apartment-hunt/`
folder had been **deleted from the working tree** by the big AI-OS restructure
(2009 uncommitted changes); it was safe in git. Restored with
`git checkout HEAD -- projects/apartment-hunt/`.

## Decisions (via AskUserQuestion)

- Denver: **3BR**, budget **wide / not sure**, UX **polish only** (restyle the
  existing static page, no interactive/dashboard rebuild).

## What shipped

1. **`profiles.py`** (new) — `SearchProfile` dataclass + `PROFILES` registry.
   Holds everything city-specific: criteria, neighborhoods, ZIP rules, every
   source URL, Zillow bounds/search-term, Exa query hoods. Ships `sf` (unchanged)
   and `denver` (whole-metro, `require_neighborhood_match=False`).
2. **`apartment_hunt.py`** — `apply_profile()` rebinds the module globals the
   pipeline reads; `--city {sf,denver}` flag (default sf). Generalized the
   SF-only ZIP/neighborhood/"divide by 3" logic; `keep()` branches on
   `REQUIRE_NEIGHBORHOOD_MATCH`. Per-city seen/digest/archive files.
3. **`build_html_digest.py`** — restyled to the global Editorial Cream standard
   (Cormorant + Jost + mono figures, cream bg, one brass accent, squared corners,
   no helper subtitles). City-aware; fixed a latent bug that dropped listings
   with no recognized neighborhood (now bucketed into preferred/fallback/other,
   and reads `ah.X` dynamically instead of stale import-time copies).

## Verification

- `py_compile` all three modules; `--city` choices wired before the key gate.
- `keep()` spot-checks pass for both cities (SF blocks Tenderloin/Oakland-ZIP;
  Denver keeps no-hood Denver, drops Boulder-ZIP/non-Denver/over-budget).
- Rendered sample SF + Denver HTML, screenshotted in browser at 1180px:
  Editorial Cream confirmed. SF = Top picks / Fallback; Denver = single
  price-sorted metro section. Computed styles verified (cream bg, Cormorant 46px,
  mono prices, 0px radius, brass View links).

## Next / open

- **Add `.env`** with `EXA_API_KEY` (required) + `FIRECRAWL_API_KEY` (recommended),
  then `python apartment_hunt.py --city denver` for the first live Denver digest,
  and `build_html_digest.py --city denver` for the page (also copies to Desktop).
- Tighten Denver budget/neighborhoods in `profiles.py` once friends decide.
- Denver property-manager list is empty (relies on Exa + r/Denver); some Denver
  aggregator URLs are by-analogy and may show as error/blocked in coverage.
- Change note: `projects/apartment-hunt/notes/2026-06-17-multi-city-profiles-and-editorial-cream-ux.md`.
