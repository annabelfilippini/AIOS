---
date: 2026-05-05
time: 18:30
project: apartment-hunt
status: paused
next-session: pick up at telegram-token refresh + (optional) Zumper / wider Exa coverage
---

# Session: apartment-hunt scraper build

## What we worked on
Built `~/Documents/AI-OS/projects/apartment-hunt/` — a daily SF rental scraper.
Sources: Craigslist HTML (RSS is hard-blocked) + Exa neural search across the open web (Realtor.com, RentSFNow, Engel & Völkers, Movoto, Relisto, ismrem, etc.) + Reddit user-post sweep via Exa.

Outputs `digest_latest.md` and dated archives in `digests/`. Daily cron at 9am.

## Decisions made
- Skip FB Marketplace entirely (auth-walled, ToS-violating, fragile). Annabel checks it manually.
- Craigslist via static-HTML parsing with Safari User-Agent — RSS feed returns 403.
- Exa: removed `includeDomains` whitelist; it was starving the search. Let it loose, then filter.
- Validate target neighborhoods via canonical Craigslist location whitelist + ZIP-code map (94133 / 94109 / 94108 / 94110 / 94123). Substring matching let in "outer mission" and "lower nob hill" — gone.
- "Nob Hill" listings under $4,500 get a ⚠️ flag (almost always TenderNob/Polk Gulch).
- Criteria: 2–3BR, **$3,200–$7,500**, move by 2026-06-15. Top priority: North Beach + Nob Hill (sorted to top of digest).
- Telegram delivery wraps in try/except — failures don't break the digest pipeline.
- Daily cron: `0 9 * * * cd ~/Documents/AI-OS/projects/apartment-hunt && .venv/bin/python apartment_hunt.py >> logs/cron.log 2>&1`

## Open questions
- Exa coverage of major aggregators (Zillow, Apartments.com, Hotpads) is sparse — they're JS-rendered and lightly indexed. Worth adding a Zumper direct-scrape source?
- Reddit sweep still pulls some Reddit corporate marketing pages despite the `/r/.../comments/` filter. Query phrasing could be tuned further.
- Should the bed-count parser pull from snippet, not just title? A few 1BRs slipped through (e.g. RentSFNow 1454-1464 Union #01 at $4,595).
- Worth using Exa's agentic `/research` endpoint as a weekly "deep dig"?

## Next steps
1. **Annabel:** refresh Telegram bot token via `@BotFather` → `/token`, paste new token into `~/.claude/channels/telegram/.env`. Also `/revoke` the old one (it leaked into stderr during session).
2. Verify the 9am cron fires tomorrow morning — check `logs/cron.log` and `digests/2026-05-06.md`.
3. (Optional) Add Zumper scraper as a third source.
4. (Optional) Tune Reddit query and bed-count parsing.

## Context to preserve
- Hunt is for whole 2–3BR apartment for **3 people** at total rent $3,200–$7,500 (per-person $1,067–$2,500), move-in by **June 15, 2026**.
- Telegram chat ID is already configured in the local `.env`; only the token
  needs refreshing. Do not commit chat IDs or bot tokens.
- Project Python env: `.venv/` (system Python 3.13, anaconda); deps `requests`, `python-dotenv`. No `feedparser` (was removed).
- Exa key lives in project `.env` (not committed — `.gitignore` covers it).

## System refinement candidates
- Pattern: when a scraper target hard-blocks programmatic UAs but serves to a normal browser, fall back to HTML parsing with a Safari UA before reaching for paid scraping infrastructure. Worth keeping in mind for future scrape jobs.
