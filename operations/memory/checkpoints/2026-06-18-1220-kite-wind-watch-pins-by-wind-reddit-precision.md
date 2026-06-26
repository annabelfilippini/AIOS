---
date: 2026-06-18
time: 12:20
project: websites / kite-wind-watch
status: SHIPPED — pins coloured by live wind, station-aware live-now dedup, Reddit panel trimmed to important spot-threads, scraper narrowed to kitesurfing-only. All verified on localhost:8804 (eval + headless Chrome).
supersedes: 2026-06-18-1118-kite-wind-watch-map-first-real-google-satellite.md
---

# Session: kite-wind-watch — pins-by-wind + Reddit precision

Annabel's four asks, all done:
1. change the colour of the pins → colour by current wind
2. why are there two green things (Loveland live-now) → station dedup
3. Reddit panel: only NEW important ones, hide if none
4. scraper: kitesurfing only, no snowkiting / random sports

## What shipped (index.html + scraper/scrape_reddit.py)

- **Pins coloured by wind.** One batched Open-Meteo `current=wind_speed_10m`
  (knots) call on map load → each tracked pin coloured by tier vs the rideable
  threshold: light(<thr-7) / marg(<thr) / good(<thr+10) / strong(<thr+19) /
  nuke. Re-tiers live on threshold change. New fns: `windColor`,
  `fetchSpotsWindNow`, `applyWindColors`, `colorPinsByWind`.
  `highlightSelectedMarker` now only enlarges the selected pin. Legend rewritten
  to the wind scale.
- **Reddit-tip pins** = hollow ring (white fill, coloured outline), wind-coloured,
  limited to 2+ mentions / max 8. `pinIcon(color, selected, hollow)`.
- **"Two green things" = same station twice.** NWS + Synoptic both resolve to
  KFNL at Loveland → `dedupeStations()` collapses same-station readings into one
  pill, keeps freshest, labels "NWS · Synoptic" (they agree). Different stations
  (Aurora K8KF vs AURC2) still both show.
- **Chatter panel** shows only `relevance==='high' && spots.length`, newest first
  (`created`), max 5, empty when none. Annabel chose "only spot-relevant threads."
- **Scraper kitesurf-only.** SPORT_SUBS = Kiteboarding+kitesurfing only;
  SPORT_TERMS narrowed; `KITE_RX` now requires a kitesurf/kiteboard compound (bare
  "kite" pulled toy-kite/Red Rocks/UFO junk); `SNOW_TITLE_RX` drops snow/wing
  threads; removed snowkite spots (Lizard Head, Rabbit Ears, Bighorns); added
  `created` to posts. `--no-sync` re-mine → 5 clean r/Kiteboarding threads.
- **Cache-bust:** `loadDiscourse()` fetches `data/discourse.json` with
  `cache:"no-store"` on init (static `<script src=discourse.js>` was serving stale
  data and hiding fresh scrapes). Script tag kept as fast fallback.

## Verified (localhost:8804)
11/11 pins wind-coloured (calm day → mostly gray/blue; Dillon 11kt, Williams
Fork 14.6kt blue). Loveland/Boyd live-now → one pill "NWS · Synoptic KFNL".
Panel → 5 clean kiteboarding spot threads (no snowkite/wingfoil). Headless PNG
at /tmp/kww-final.png.

## Open / next
- **Fresh reddit-cli sync DONE** (12:25, cookie 2.1d old, valid). Full
  `scrape_reddit.py` re-synced under the narrowed kitesurf-only terms/subs →
  mined 144 threads, 24 posts, 13 panel-eligible. Live app shows 5 clean
  r/Kiteboarding spot threads, scanned 2026-06-18. No snowkite/wingfoil residual
  in the panel. Cookie re-import needed every few weeks (`reddit-cli auth import`).
- On a windy day, confirm green/amber/red pin tiers look right (today was calm).
- Mobile layout still not phone-reviewed (carried from prior checkpoint).
