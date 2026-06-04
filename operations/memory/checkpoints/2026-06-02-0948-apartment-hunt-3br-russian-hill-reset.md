---
date: 2026-06-02
time: 09:48
project: apartment-hunt
status: active-needs-telegram-token
next-session: refresh Telegram bot token, then run apartment_hunt.py without --dry to send the new 3BR Russian Hill/North Beach digest and create seen_3br_sf_core.json
---

# Session: apartment-hunt 3BR Russian Hill reset

## New search intent
- Annabel is looking for 3BR apartments in San Francisco.
- Favorite neighborhood: Russian Hill. Emphasize it first.
- Second priority: North Beach.
- Also looking a bit in Hayes Valley.
- Marina and Pacific Heights are acceptable fallback neighborhoods if necessary.
- Hard no: Tenderloin. Also block TenderNob, Lower Nob, Polk Gulch, and Civic Center spillover.
- Budget: ideal max $7,500/month total ($2,500/person for 3 people); stretch max $8,250/month for unusually good fits.

## Code changes
- Updated `projects/apartment-hunt/apartment_hunt.py` criteria to exact 3BR, $3,200-$8,250, ideal max $7,500.
- Reordered priorities to Russian Hill, North Beach, then fallback neighborhoods.
- Removed Mission and Nob Hill from target neighborhoods.
- Added Hayes Valley.
- Added hard blocked location markers for Tenderloin/TenderNob/Lower Nob/Polk Gulch/Civic Center.
- Stopped treating ambiguous 94109 and 94102 ZIP-only results as positive matches.
- Added non-SF California ZIP blocking after a false `Marina, CA 93933` result leaked in.
- Expanded Exa source coverage with more apartment aggregator and SF property-manager domains.
- Switched seen-state to `seen_3br_sf_core.json` so old May `seen.json` does not suppress the new search.
- Updated README to match the new hunt and access-boundary rules.

## Verification
- `python -m py_compile apartment_hunt.py` passed.
- Live dry run on 2026-06-02:
  - Craigslist: 52 raw listings.
  - Exa: 139 raw listings.
  - Post-filter matches: 3.
  - New: 3.
- Current dry digest has:
  - 2 Russian Hill / North Beach matches.
  - 1 fallback Pacific Heights match.
  - No Tenderloin/TenderNob/Lower Nob/Polk/Civic/Marina-CA false positives found by text check.
- Dry run did not create or advance `seen_3br_sf_core.json`.

## Access boundary
- Authenticated apartment sources can be added when Annabel explicitly provides access and the site permits that use.
- Do not implement login bypass, CAPTCHA evasion, private-session scraping without permission, or access-control circumvention.

## Next steps
1. Refresh Telegram bot token in `~/.claude/channels/telegram/.env`.
2. Run:

```bash
cd /Users/annabelfilippini/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py
```

3. Consider adding a `--deep` mode later if the daily expanded Exa sweep feels too slow or too sparse.
