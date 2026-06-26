---
date: 2026-06-02
time: 15:54
project: apartment-hunt
status: active-direct-source-coverage
next-session: review digest_latest.md direct source coverage, then tune slow/erroring local manager URLs or add source-specific parsers for high-value reachable sites
---

# Session: apartment-hunt direct source coverage

## What changed

- Annabel asked to directly scrape apartment aggregators and local property managers, with the goal of seeing every qualifying SF apartment rental.
- Updated `projects/apartment-hunt/apartment_hunt.py` to add a direct public-source pass before Exa:
  - Directly checks 34 public aggregator/property-manager source pages.
  - Parses JSON-LD records and listing-looking links with nearby context.
  - Records per-source coverage status in the markdown digest.
  - Keeps Exa as fallback for blocked/rate-limited/JS-only aggregator pages.
- Tightened filters so direct/Exa candidates must state bedroom count, preventing neighborhood hub pages from passing as exact 3BR matches.
- Updated `projects/apartment-hunt/README.md` to document direct source coverage and the no-guaranteed-complete-inventory boundary.

## Verification

- `python -m py_compile apartment_hunt.py` passed.
- Final dry run:
  - Craigslist: 51 raw listings.
  - Direct public sources: 261 raw listing candidates across 34 source pages.
  - Exa: 140 raw listings.
  - Post-filter matches: 3.
  - New since last run: 3.
  - Dry run wrote `digest_latest.md` and skipped seen-set update.
- Direct source coverage in latest dry run:
  - 19 reachable.
  - 11 blocked/rate-limited.
  - 4 errored.

## Important constraints

- Direct public scraping cannot guarantee complete coverage of large aggregators that return HTTP 403/429 or JS-only shells.
- Do not add login bypass, CAPTCHA evasion, private-session scraping, or access-control circumvention.
- If "for sale" is meant literally instead of rental, this needs a separate condo/home-buying tracker with different sources and filters.

## Next improvements

- Add source-specific parsers for reachable high-value sites such as Redfin, Rentable, RentCafe, ApartmentGuide, and RentSFNow.
- Fix or replace local-manager seeds that still error: Anchor Realty, Brick + Timber, Kinetic RE, Lapham Company.
- Consider per-source shorter timeouts or a `--fast` mode so daily cron remains quick.
