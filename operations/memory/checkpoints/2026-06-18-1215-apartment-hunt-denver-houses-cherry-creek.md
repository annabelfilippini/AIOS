---
date: 2026-06-18
time: 12:15
project: apartment-hunt
status: LIVE & WORKING — Denver retargeted from apartments to single-family HOUSES near Cherry Creek, capped at $5,000/mo. Last run produced 84 houses (3 in Cherry Creek, 12 in the ~10-min ring). Digest on Desktop. SF profile untouched.
supersedes: 2026-06-18-1016-apartment-hunt-keys-live.md
---

# Session: apartment-hunt — Denver houses near Cherry Creek, under $5K

## Where this stands

First live runs are done and the Denver profile is now a **single-family house**
hunt (not apartments), centered on Cherry Creek, under $5,000/mo. Latest run:
**84 houses** — 3 in Cherry Creek (80206, e.g. 238 Harrison St, 245 N Jackson
St, 551 Cook St), 12 in the ~10-min ring, 69 elsewhere in metro. Highest price
$4,995; nothing over $5K except 4 listings with no parsed price (shown anyway).

Output files (overwritten each run):
- `projects/apartment-hunt/digest_denver_latest.html`
- `~/Desktop/apartment-hunt-denver-2026-06-18.html` (opened in browser for review)

## What changed this session

Annabel's requirements: 3 bed / 2 bath, **house**, near Cherry Creek (~10-min
drive), garage, office, open floor plan, **under $5,000/mo**. She said soft items
are OK to miss.

Implemented as firm targeting + soft scored features:

1. **profiles.py** — added 3 dataclass fields (defaults keep SF unchanged):
   `listing_noun`, `craigslist_extra_params`, `preferred_keywords`. Retargeted
   the DENVER profile: `listing_noun="house"`; Craigslist `housing_type=6`
   (house) + `min_bathrooms=2` server-side; Cherry Creek + Cherry Creek North as
   preferred hoods, the ~10-min ring (Hilltop, Hale, Mayfair, Crestmoor, Belcaro,
   Country Club, Congress Park, Wash Park, Bonnie Brae, Cory-Merrill, Observatory
   Park, Glendale, Cherry Hills, Lowry) as fallback; expanded `_DENVER_HOODS`,
   `cl_location_to_hood`, `target_zips`; house-rental source seeds; Zillow bounds
   tightened to the ring; `min_price=1000, ideal_max_price=5000, max_price=5000`.
2. **apartment_hunt.py** — bound the new globals; `Listing.feature_matches()`
   (word-boundary regex); Exa queries use `LISTING_NOUN` + a feature bias phrase;
   Craigslist merges extra params; **house-mode hard filter** in `keep()`
   (`_NON_HOUSE_RE` drops apartment/condo/hub listings unless `_HOUSE_RE`
   matches); render sorts feature-rich first + shows a `✓` feature line;
   budget-aware criteria line.
3. **build_html_digest.py** — feature-aware sort, `✓` feature badges (`.tag.feat`),
   house/budget-aware header ("≤ $5,000/mo").
4. Deleted throwaway `sample_sf.html` / `sample_denver.html`.

## Two bugs found & fixed mid-run (why the output is trustworthy now)

- **"den" matched inside "Denver"** → every listing falsely badged "office".
  Fixed feature matching to word boundaries (`\b...\b`).
- **Apartment complexes flooded "Top picks"** (e.g. "3 bed condo", "Seasons of
  Cherry Creek Apartments", "16 Three-Bedroom Apartments for Rent"). House was a
  fundamental requirement, so added the `_NON_HOUSE_RE` hard filter. Top picks
  are now real house addresses.

## Known caveats / open questions

- **Exa partially rate-limited** — some queries 403 (burst limits, NOT a bad
  key; ~10 Exa results still come through each run). Coverage would widen with
  paced retries.
- **Feature badges (garage/office/open floor plan) are sparse** — most listing
  snippets are thin text, so a missing badge ≠ feature absent. Must click through
  to confirm. **2-bath is hard-guaranteed only on the 25 Craigslist results**
  (filtered server-side); soft elsewhere — a few "1 Bath" houses slip into the
  wider list.
- **Counts vary run-to-run** (73 → 91 → 84) due to Zillow/Trulia/Exa
  rate-limiting (non-deterministic firecrawl scraping).
- 4 no-price listings shown (unverified vs $5K cap). Annabel asked whether to
  drop them — undecided.

## Next steps

- Decide: drop no-price listings? Hard-drop <2-bath everywhere (not just CL)?
  Narrow to Cherry Creek + ring only (hide the 69 "elsewhere")?
- Offered but not yet set up: a **daily auto-run** wrapping
  `python3 build_html_digest.py --city denver` (Annabel hasn't confirmed).
- If Exa coverage matters, add retry/backoff for 403s.

## Reference

- Build details + multi-city design: `projects/apartment-hunt/notes/2026-06-17-multi-city-profiles-and-editorial-cream-ux.md`
- Run command: `cd projects/apartment-hunt && python3 build_html_digest.py --city denver`
