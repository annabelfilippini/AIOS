---
date: 2026-06-16
time: 11:55
project: websites / kite-wind-watch
status: SHIPPED — hourly wind alerter built + scheduled (launchd). macOS notifications live; Telegram blocked on a stale token.
supersedes: 2026-06-16-1120-reddit-cli-shipped-kite-spot-discovery-live.md
---

# Session: kite-wind-watch hourly wind alerter

## Context / why
Annabel asked to "refresh data every hour to stay up to date on very windy
places." Key distinction surfaced: the dashboard already fetches **live**
Windguru/Open-Meteo/NWS forecasts in-browser on every page load, and the Reddit
scraper only updates evergreen community chatter (daily is right; hourly would
risk the cookie). So the real need was a **wind-alert routine**, not a faster
Reddit refresh.

## What shipped
`scraper/wind_alert.py` (Python stdlib, read-only). Hourly it pulls Open-Meteo
forecasts for all 11 tracked spots, and if any spot is forecast **gusts ≥ 18kn
within the next 48h** (daylight hours 6:00–21:00 local) it sends one
consolidated alert. De-dupes via `~/.local/share/kite-wind-watch/alert_state.json`
so a windy day pings once per spot (re-pings only if peak climbs ≥3kn). Prunes
past days from state each run.

Settings (Annabel's choices): 18kn gust threshold, 48h lookahead, all 11 spots.

Two delivery channels:
- **macOS notification** (osascript) — working now, no creds. ASCII-only strings
  (emoji broke osascript parsing — fixed).
- **Telegram** — coded against `~/.claude/channels/telegram/.env` token + chat
  `8519804405`, but that token returns **401 Unauthorized** (getMe fails too).
  Stale/regenerated. State saves if *either* channel delivers.

Scheduled: `~/Library/LaunchAgents/com.kitewindwatch.windalert.plist`, hourly at
:05, loaded. (Sits alongside the existing `com.kitewindwatch.scrape` daily 7am
Reddit job.)

## Verified
Dry-run + real run: all 11 spots flagged for a big **Wed 2026-06-17** blow
(26–40kn gusts everywhere; Twin Buttes peak 40kn). macOS banner posted cleanly,
state written, dedup confirmed.

## Open / next (needs Annabel)
- **Refresh the Telegram bot token** to get phone alerts: run `/telegram:configure`
  and paste a fresh BotFather token into `~/.claude/channels/telegram/.env`. The
  alerter will start delivering to Telegram automatically (no code change). Until
  then alerts are macOS-only (only seen at the Mac).
- Tune later if noisy: threshold/lookahead/ride-hours are constants at the top of
  `wind_alert.py`.

## Operate
- Manual test: `cd projects/websites/kite-wind-watch && python3 scraper/wind_alert.py --dry`
- Logs: `scraper/wind_alert.log`. Unload: `launchctl unload ~/Library/LaunchAgents/com.kitewindwatch.windalert.plist`
