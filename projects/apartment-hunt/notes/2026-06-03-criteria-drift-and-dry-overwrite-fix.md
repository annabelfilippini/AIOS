# 2026-06-03 — Criteria fix + dry-overwrite fix

## Why yesterday's archive showed 58 then today showed 2

Three issues compounded during today's investigation:

1. **`--dry` was writing to the dated archive** (`digests/{date}.md`) the same way a real run does. The 2026-06-02 morning cron's 58-match digest got overwritten that evening by a 3-match dry run, so the morning's actual data was permanently lost from the archive.
2. **The criteria string in the digest header was hardcoded `"3BR"`** rather than computed from `MIN_BEDS`/`MAX_BEDS`. Now driven from the constants.
3. **A 2-3BR test detour** happened mid-investigation. Annabel confirmed the real intent is **3BR only**. The May cron log URL showing `min_bedrooms=2` is from the legacy criteria; the current intent (and now the code) is 3BR. Reverted to `MIN_BEDS = 3, MAX_BEDS = 3`.

## What's set now

- `MIN_BEDS = 3, MAX_BEDS = 3` (3BR only).
- `main()`: dry runs write `digest_latest.md` only; the dated `digests/{today}.md` archive and the seen-set update happen **only** on real runs.
- `render_markdown`: criteria string reads `f"{MIN_BEDS}-{MAX_BEDS}BR"` (renders as `3-3BR`, or could be simplified to `3BR` if MIN==MAX is detected; left as-is for now).
- README: 3BR only.

## The honest assessment for 3BR in target neighborhoods

When the criteria is 3BR + (Russian Hill, North Beach, Hayes Valley, Marina, Pac Heights, Cow Hollow, Nob Hill) + price band, the SF market today returns ~2 matches. That's the real inventory, not a scraping bug. Verified by:

- Zillow returned 41 SF 3BR listings; zero in target neighborhoods (heavy on Outer Richmond, Excelsior, Bayview, Sunset).
- Aggregators (Redfin 79, Rentable 61, Rentberry 47, etc.) mostly miss the target neighborhoods at 3BR.
- The 2 matches that *do* surface are both Craigslist J.Wavro property-manager listings.

## Two pre-existing issues NOT fixed in this pass

- **Cron has been silent since 2026-05-07** (Craigslist DNS error then; Telegram 401 persists).
- **Property-manager direct fetches return 0** despite real inventory because their pages are JS-rendered. Routing them through Firecrawl the way Zillow now goes through would surface the off-market pool.

## To verify

```bash
cd ~/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py --reset
.venv/bin/python apartment_hunt.py --dry
head -10 digest_latest.md
```
