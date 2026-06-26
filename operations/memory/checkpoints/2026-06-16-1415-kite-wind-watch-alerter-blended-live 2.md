---
date: 2026-06-16
time: 14:15
project: websites / kite-wind-watch
status: SHIPPED — hourly alerter upgraded to blended forecast + live "blowing now"; Synoptic live readings live on dashboard + alerts.
supersedes: 2026-06-16-1345-kite-wind-watch-accuracy-stack-hrrr-live-obs.md
---

# Session: kite-wind-watch alerter — blended + live

## What shipped
- **Synoptic live readings now active** on the dashboard. Annabel pasted her
  Synoptic API *key*; I generated a request *token* from it
  (`/v2/auth?apikey=...`) and put the TOKEN in `config.js` `synopticToken` (the
  key must NOT live in client JS). Verified: Aurora → station AURC2 (0.8 mi from
  the lake). Two live pills now show under each spot: NWS + Synoptic.
- **`scraper/wind_alert.py` upgraded** to match the dashboard:
  - Forecast now BLENDS Best Match + NOAA HRRR (`ncep_hrrr_conus`) + GFS,
    averaged per hour.
  - Pulls LIVE readings (Synoptic preferred via token read from config.js by
    regex; else NWS walking nearest ~5 stations).
  - New **🟢 BLOWING NOW** trigger: alerts when a spot is currently ≥18kn
    (daylight only), separate from the forecast trigger. Each line shows the real
    current reading. Dedup: forecast once/spot/windy-day (re-ping +3kn); live-now
    once/spot/day.
- Verified real send: Lake Hattie/Twin Buttes 27kn now, Lake Dillon 24kn now all
  flagged BLOWING NOW; Telegram + macOS delivered. launchd job runs same script.

## Still open
- Kept map spots (browser localStorage) don't feed `wind_alert.py` (hardcoded
  SPOTS) — needs a shared spots source both sides read.
- iKitesurf not integrated (paid + owner-gated).

## Operate
- Test alerter: `python3 scraper/wind_alert.py --dry`. Synoptic token lives in
  `config.js` (gitignored); regenerate at `/v2/auth?apikey=KEY` if it fails.
- Dashboard: localhost:8804 (one canonical index.html; see project CLAUDE.md).
