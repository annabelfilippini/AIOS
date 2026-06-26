---
date: 2026-06-16
time: 13:45
project: websites / kite-wind-watch
status: SHIPPED — HRRR model + live NWS station observations added (free); Synoptic wired behind a token; iKitesurf documented.
supersedes: 2026-06-16-1240-kite-wind-watch-google-map-hero.md
---

# Session: kite-wind-watch accuracy stack

## Research (what kiters trust)
Web search (indexes r/Kiteboarding far better than the reddit-cli mirror, which
is spot-discovery-only — site-wide reddit-cli search returned junk):
- **Windy** = community favorite, mainly for comparing **HRRR + ECMWF + GFS**.
- **Windguru** = detailed standard (already have).
- **iKitesurf** = best for LIVE station readings (paid, owner-gated API).
- Live-sensor networks: **Synoptic/MesoWest** (170k stations, free tier is
  edu/research else trial→paid), **NWS station obs** (free, keyless), Holfuy
  (sparse in CO), WeatherFlow/Tempest (owner-gated).

## What shipped (index.html)
1. **HRRR model** added to the consensus — Open-Meteo `models=ncep_hrrr_conus` on
   the `/v1/gfs` endpoint. Free. Now **7 sources** (WG, Best, ECMWF, GFS, ICON,
   HRRR, NWS).
2. **Live "now" layer** — green pill(s) under the spot name showing REAL current
   wind from the nearest reporting station (observation, not forecast).
   - **NWS** (free, keyless): `points → observationStations`, then walk the
     nearest ~5 stations until one reports wind (closest is often blank, e.g.
     KCCU/Copper Mtn near Dillon). Cached per spot.
   - **Synoptic** (optional, denser): `stations/latest?radius=lat,lon,30&units=
     speed|kts`, behind `config.js` → `synopticToken`. Skipped gracefully without
     a token. Both render as labelled pills (NWS / Synoptic).

## Verified (localhost:8804, no console errors)
Aurora → "Now 10 kt NW · NWS KBKF". Lake Dillon → "Now 8 kt WNW · NWS KLXV"
(fell through blank KCCU — the multi-station walk is what makes mountain spots
work). HRRR present in sourcesLive. Synoptic correctly skipped (placeholder
token).

## Open / next (needs Annabel)
- **Synoptic token** (optional, denser live readings): sign up at
  synopticdata.com → API token → paste into `config.js` `synopticToken`. Then a
  2nd live pill appears. Free tier is edu/research; else 14-day trial → paid.
- **iKitesurf**: not built (paid sub + owner-gated API). Only worth it if she
  pays for their app.
- Still-open earlier seam: kept map spots don't feed `wind_alert.py` yet; and the
  hourly alerter still uses Open-Meteo only (could add HRRR there too for parity).

## Files
index.html (HRRR model entry, live-obs functions, livewrap pills), config.js +
config.example.js (synopticToken slot). design.md Data Rules + iteration log
updated.
