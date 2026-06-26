---
date: 2026-06-16
time: 12:40
project: websites / kite-wind-watch
status: SHIPPED — Google Map is now the hero; pins drive spot selection + Reddit-spot approval. One known seam (kept spots don't feed alerts yet).
supersedes: 2026-06-16-1155-kite-wind-watch-hourly-wind-alerter.md
---

# Session: kite-wind-watch — Google Map hero

## What shipped (index.html)
The map is the main component. Navy pins = tracked spots (click → forecast loads
in the panel below). Green pin = current selection. Yellow pins = spots Reddit
mentioned but not tracked; click → InfoWindow with the Reddit quote + "Add to my
spots" (permanent, navy, persisted to localStorage) or "Just preview the
forecast" (temporary). Front Range / CO+WY tabs retired — the spot menu lists
all spots; chatter card always visible.

All forecast/fetch/consensus code was preserved untouched; selection now routes
through `chooseSpotObject()` and `highlightSelectedMarker()` (called in
setLoading so every path — pin, menu, chip — highlights consistently).

## Tech decisions
- **Engine: real Google Maps JS API** (Annabel chose it over free Leaflet).
- **Key:** gitignored `config.js` → `window.KWW_CONFIG.googleMapsKey` (her key is
  in there now). `config.example.js` committed as template. Bot... no — key MUST
  stay HTTP-referrer-restricted to `localhost:8804/*` (+ deploy domain) since it
  ships in client HTML.
- Classic `google.maps.Marker` + SVG data-URI pins (no Cloud mapId needed).
- Discovered-spot geocoding: **keyless Nominatim/OSM**, client-side, cached in
  localStorage, biased by `region_guess` — avoids forcing the Google Geocoding
  API on her account.

## Verified (preview, localhost:8804)
11 navy + 3 yellow markers; map terrain renders; clicking Lake Dillon switched
forecast + green-highlighted its pin; keep-flow added Lost Lake (SPOTS 11→12,
menu + localStorage updated, marker→navy). No console errors. Brainard/Lost/Swan
geocoded to real CO coords but are snowshoeing chatter (good demo of why the
approve-gate matters). Map greys on container-resize → added window resize
listener.

## KNOWN SEAM / next
- **Kept spots feed the dashboard only, NOT the hourly alerts.** `wind_alert.py`
  has its own hardcoded SPOTS list; browser localStorage is invisible to it. To
  make kept spots alert: introduce a shared spots source both the page and the
  Python alerter read, OR add kept spots to wind_alert.py manually. Flag to
  Annabel — earlier I implied keeping auto-feeds alerts; it does not yet.
- Optional: bake geocoded coords into discourse.js at scrape time (so yellow pins
  don't depend on per-load Nominatim); a "live now / it's blowing" alert variant.

## Operate
- Preview: `preview_start kite-wind-watch` (port 8804). Verify map via DOM eval;
  screenshot only after an explicit `preview_resize` (1px viewport bug).
- Key file `config.js` is gitignored; never commit it.
