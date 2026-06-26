# CLAUDE — kite-wind-watch

## Canonical file: ONE html, never a copy

The live app is **`projects/websites/kite-wind-watch/index.html`**. That single
file is the only source of truth. Always edit it in place.

- Do NOT create a new HTML, a renamed variant, or a Desktop/`_inbox` copy. A
  stale `~/Desktop/kite-wind-watch.html` snapshot caused real confusion (it
  showed an old, map-less version on `file://` while the real app moved on).
- To show Annabel the app, serve this file at **localhost:8804**
  (`preview_start kite-wind-watch`) and open `http://localhost:8804/index.html`.
  Never hand her a `file://` path — the Google Map needs a real origin
  (key is referrer-restricted to `localhost:8804/*`) and the page loads
  `config.js` + `data/` by relative path, so a double-clicked file shows a blank
  map.

## Stack / non-assumptions

- Static single-page app: `index.html` + `config.js` (gitignored, holds the
  Google Maps key) + `data/discourse.js` (Reddit scrape) + `scraper/`.
- Google Maps JS API for the map; keyless Nominatim/OSM for geocoding discovered
  spots; live forecasts from Open-Meteo / Windguru / NWS (client-side fetch).
- Scheduled jobs:
  - **Wind alerts run on the always-on VPS** (Hetzner `root@5.78.218.220`),
    hourly cron at `:05` → `/root/kite-wind-watch/wind_alert.py`. Tokens live in
    `/root/kite-wind-watch/.env` (TELEGRAM_BOT_TOKEN, SYNOPTIC_TOKEN; chmod 600).
    Telegram-only there (macOS notification auto-skips on Linux). This is what
    makes alerts work 24/7 with the laptop closed. The Mac launchd job is
    disabled (`com.kitewindwatch.windalert.plist.disabled`) to avoid double pings.
    To update: edit `scraper/wind_alert.py`, then
    `scp scraper/wind_alert.py root@5.78.218.220:/root/kite-wind-watch/`.
  - `com.kitewindwatch.scrape` (daily Reddit) stays on the Mac — it needs
    Annabel's browser reddit-cli cookie, which isn't on the VPS.
- Per-project docs: `design.md` (how it looks/works + iteration log),
  `content.md` (facts). Read those before building.
