---
date: 2026-06-02
time: 09:38
project: apartment-hunt
status: active-needs-telegram-token
next-session: refresh Telegram bot token, then run apartment_hunt.py once without --dry to send current listings and advance seen-set
---

# Session: apartment-hunt restart

## What changed

- Rechecked `projects/apartment-hunt/` after Annabel started looking for places to live in SF again.
- Cron is still installed for daily 9am:
  `0 9 * * * cd /Users/annabelfilippini/Documents/AI-OS/projects/apartment-hunt && .venv/bin/python apartment_hunt.py >> logs/cron.log 2>&1`
- Live no-write health check succeeded on 2026-06-02:
  - Craigslist: 226 raw listings.
  - Exa: 134 raw listings.
  - Post-filter matches: 58.
  - New relative to May `seen.json`: 56.
- Refreshed `digest_latest.md` and `digests/2026-06-02.md` with `--dry`.
- `seen.json` stayed at 76 entries, so the 56 current listings remain eligible to send after Telegram is fixed.

## Fixes made

- Updated `apartment_hunt.py` so failed Telegram delivery no longer advances `seen.json`.
- `--dry` now skips Telegram and does not update the seen-set.
- Updated README criteria from stale `$5,100-$7,500` to current `$3,200-$7,500`.
- Updated README cron path from stale `logs.txt` to `logs/cron.log`.

## Current criteria

- 2-3BR.
- $3,200-$7,500/month.
- Move by 2026-06-15.
- Target neighborhoods: Mission, Marina, North Beach, Nob Hill, Russian Hill, Pacific Heights, Cow Hollow.
- Preferred/top-sorted: North Beach and Nob Hill.

## Blocker

- Telegram bot token exists in the local Telegram env, but Telegram `getMe` returns `401 Unauthorized`.
- Refresh via BotFather before running the non-dry send:
  1. Open `@BotFather`.
  2. Use `/token` for the apartment tracker bot.
  3. Update `~/.claude/channels/telegram/.env` with the new `TELEGRAM_BOT_TOKEN`.
  4. Revoke the old token if BotFather still shows it as active.

## Next step

After the token is refreshed, run:

```bash
cd /Users/annabelfilippini/Documents/AI-OS/projects/apartment-hunt
.venv/bin/python apartment_hunt.py
```

Expected result: digest sends to Telegram, then `seen.json` advances so the next 9am cron only sends genuinely new matches.
