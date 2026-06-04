# 2026-06-03 — Added Cow Hollow + Nob Hill as target neighborhoods

## What changed

Added two neighborhoods to the target list after a market scan showed only 2 listings matched the original 5-neighborhood filter today.

- `NEIGHBORHOODS`: added `"cow hollow"`, `"nob hill"`.
- `FALLBACK_NEIGHBORHOODS`: added both (not promoted to preferred — Russian Hill and North Beach stay on top).
- `_CL_LOCATION_TO_HOOD`: added `"nob hill"` → `"nob hill"` and `"russian hill / nob hill"` → `"nob hill"` (Craigslist sellers sometimes label boundary listings this way). Cow Hollow was already present.

## What did NOT change

**No new ZIP added to `SF_TARGET_ZIPS`.** Nob Hill is in ZIP 94108, but 94108 also covers Chinatown and the Financial District. Using it as a positive-ZIP fallback would tag those listings as Nob Hill. Following the same logic the existing comment uses for 94109 ("can be Russian Hill, Nob Hill, Polk Gulch, or Tenderloin"), Nob Hill requires an explicit neighborhood-name match in the title or snippet.

Cow Hollow doesn't need a new ZIP either: 94123 is already mapped to Marina, and most Cow Hollow listings either say "Cow Hollow" outright or sit in that ZIP.

## Safety check: hard-no neighborhoods

Adding `"nob hill"` to `NEIGHBORHOODS` raises a substring-match concern — "Lower Nob Hill" and "TenderNob" contain "nob hill" as a substring. Confirmed safe because `_BLOCKED_LOCATION_MARKERS` (line ~1049) is checked **before** the positive neighborhood match in `keep()`, and it already includes `tenderloin|tendernob|tender nob|lower nob hill|polk gulch|civic center|south beach`. So a listing tagged "Lower Nob Hill" gets rejected before the positive match can fire.

## Why the Zillow scraper looked broken (spoiler: it wasn't)

The 2026-06-03 market scan returned 41 Zillow raw candidates and 0 matches, which prompted a "is the Zillow scraper working?" question. Answer: yes, it's working — all 41 listings are real SF 3BR rentals with prices, addresses, and ZIPs. None of them are in the original 5 target neighborhoods.

Distribution of the 41 Zillow listings by ZIP:
- 94121 (Outer Richmond): 7
- 94112 (Excelsior/Outer Mission): 6
- 94124 (Bayview): 4
- 94122 (Sunset): 3
- 94116 (Parkside): 3
- 94132 (Lake Merced): 3
- 94118 (Inner Richmond): 3
- 94110 (Mission): 2
- 94109: 2 (both TenderNob/Tenderloin — blocked correctly)
- 94117, 94114, 94127, 94134, 94133: 1 each (one in 94133 / North Beach but it didn't title-match — worth a manual check next run)

This is just the reality of Zillow's SF 3BR inventory: heavy in west-side family neighborhoods, very thin in Russian Hill / North Beach / Hayes Valley / Marina / Pac Heights / Cow Hollow / Nob Hill.

## To verify

```bash
cd ~/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py --reset
.venv/bin/python apartment_hunt.py --dry
```

Look at `digest_latest.md` — match count should rise above 2.
