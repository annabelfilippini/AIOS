---
date: 2026-06-16
time: 14:35
project: websites / kite-wind-watch
status: STABLE — map dashboard + accuracy stack + 24/7 VPS alerts all shipped and verified. One small seam open.
supersedes: 2026-06-16-1430-kite-wind-watch-alerter-on-vps-247.md
---

# Session: kite-wind-watch — full state snapshot

Big session. Where everything stands:

## Shipped + verified this session
1. **Google Map is now the hero** of `index.html`. Navy pins = tracked spots
   (click → forecast in the panel below); green = selected; **yellow = spots
   Reddit mentioned but not tracked** (geocoded via keyless Nominatim). Click a
   yellow pin → Reddit quote + "Add to my spots" (persists to localStorage, then
   feeds nothing-yet on alerts — see open seam) or "Just preview the forecast".
   Tabs retired. Google key in gitignored `config.js`.
2. **Accuracy stack.** Forecast now blends **7 sources**: Windguru + Open-Meteo
   (Best/ECMWF/GFS/ICON) + **NOAA HRRR** (added) + NWS. Plus a **live "now" row**
   per spot from real stations: **NWS** + **Synoptic** (token in config.js;
   Synoptic found AURC2 0.8mi from Aurora Reservoir). Research-backed: kiters rate
   Windy/HRRR + iKitesurf(live); iKitesurf is paid/owner-gated so skipped.
3. **Alerter is 24/7 on the VPS.** `wind_alert.py` blends HRRR/GFS + live, adds a
   🟢 BLOWING-NOW trigger (currently ≥18kn, daylight only), runs hourly via cron
   on Hetzner `root@5.78.218.220:/root/kite-wind-watch/` (tokens in `.env`,
   chmod 600). Telegram → her phone anywhere. Mac launchd alert job DISABLED
   (plist `.disabled`) to avoid doubles. TZ bug fixed (server is UTC; now reasons
   in Denver via zoneinfo).

## Canonical-file rule (project CLAUDE.md)
ONE html: `projects/websites/kite-wind-watch/index.html`. Never make a copy /
Desktop snapshot (a stale `~/Desktop/kite-wind-watch.html` caused confusion; now
deleted). Always serve at **localhost:8804** to view — never `file://` (Google
Map needs a real origin; key restricted to `localhost:8804/*`).

## Open seams (not blockers)
- **Kept map spots don't feed alerts.** Dashboard keeps spots in browser
  localStorage; `wind_alert.py` has its own hardcoded SPOTS. A newly kept spot
  won't auto-alert. Fix = a shared spots file both read.
- Dashboard viewing is still local-only. Optional future: deploy to Vercel for a
  permanent URL (would need the deploy domain added to the Google key referrers).

## Operate
- View dashboard: `preview_start kite-wind-watch` → localhost:8804.
- Update alerter: edit `scraper/wind_alert.py` → `scp` to VPS path above.
- Test alerter: `python3 scraper/wind_alert.py --dry`.
- VPS logs/state: `tail /root/kite-wind-watch/wind_alert.log`;
  `/root/.local/share/kite-wind-watch/alert_state.json`.
