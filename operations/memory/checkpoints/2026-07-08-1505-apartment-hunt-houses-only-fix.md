---
date: 2026-07-08
time: 15:05
project: apartment-hunt
status: House-mode leak FIXED + assert-tested. Zillow apartment complexes (bare-address titles, zillow.com/apartments/ URLs) no longer pass houses-only searches; Zillow map query now excludes apartment/condo/multifamily server-side. Per-seed yield now printed to run.log for data-driven seed trimming. CREDITS: 184 left, ~220/search — effectively zero searches until 2026-07-13 reset unless topped up.
supersedes: 2026-07-08-1450-apartment-hunt-friend-search-server.md
---

# Session: apartment-hunt — houses-only leak fixed

## Problem
The 14:25 houses-mode run ("3BR, 2+ bath, $5,000, houses") showed 6 of 8 top
picks as Zillow apartment complexes (Modera, Gables, Griffis, etc.). Root
cause: (a) the Zillow map search pre-filters price/beds server-side but not
home type; (b) complex pages are titled with bare street addresses, so the
text-only `_NON_HOUSE_RE` haystack (title+hood+snippet) never sees the word
"apartment" — the only signal is the URL, which `keep_basic` never read.

## Fixes (apartment_hunt.py, build_html_digest.py — uncommitted)
1. `_fetch_zillow_page`: when `LISTING_NOUN == "house"`, filterState now sets
   apa/apco/con/mf/manu/land to false (unset types default ON). Townhomes stay,
   matching the text filter. Complexes are never fetched → also stops wasting
   enrichment credits on them. `--any-type` unaffected.
2. `keep_basic` house check now also drops by URL:
   `_NON_HOUSE_URL_RE = zillow\.com/(apartments|b)/` — belt-and-braces for
   complex pages arriving via Exa/other channels.
3. `build_html_digest.py` now prints per-seed SourceReport lines
   ("seed X: ok, N listings") — visible in web/run.log and /status tail, so
   dead seeds (~7.6 credits each) can be trimmed on evidence.

## Verified
Replay test (scratchpad test_house_filter.py): all 6 leaked complexes dropped
in house mode, real house (/homedetails/) kept, any-type mode still keeps
complexes. Syntax + --help OK. NOT re-run against live Firecrawl (credits).

## Next
1. After next run, read the "seed …: 0 listings" lines and cut dead seeds —
   the 3 self-tour platforms (rently/showmojo/tenantturner) are prime suspects
   (~23 credits/run).
2. Credit decision: top up only if friends need searches before 2026-07-13.
3. Still open from prior checkpoint: launchd plist for server+funnel reboot
   survival; commit the uncommitted files.
