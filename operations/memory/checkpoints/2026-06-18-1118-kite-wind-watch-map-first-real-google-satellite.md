---
date: 2026-06-18
time: 11:18
project: websites / kite-wind-watch
status: SHIPPED — index.html re-centered into the map-first layout with the REAL Google satellite (hybrid) map full-bleed + floating right forecast panel. Verified live on localhost:8804 (headless-Chrome PNG). Forecast-on-click and the week both confirmed working.
supersedes: 2026-06-17-1525-kite-wind-watch-map-first-restructure-mockup.md
---

# Session: kite-wind-watch — map-first re-center (real Google satellite)

Annabel said she didn't like how the app looked and wanted it to "look more like
a map," with two hard requirements: click a pin → forecast appears **without
leaving the app**, and show **the good hours + the rest of the week**. She first
asked to embed her personal Google My Map; I explained an embedded My Map is a
sealed iframe the app can't read clicks from, so forecast-on-click is only
possible with the Google Maps **JS API** (which the app already uses). She agreed
the goal is the in-app experience.

## What shipped (index.html — layout/CSS only, zero forecast-logic change)

- `#map` full-bleed (`position:absolute; inset:0`). The app IS the map.
- Map default `terrain` → **`hybrid`** (satellite + labels).
- Forecast moved into a **floating right panel** (`.spot-panel`, frosted/squared)
  reusing every existing id (spotName, chart, otherDays, sources, chatter).
- Left stack: serif **"The map."** wordmark + Settings + "What the pins mean"
  legend. Cormorant display + JetBrains mono added; structural surfaces squared.
- Google controls moved off the panels: map-type TOP_CENTER, zoom LEFT_BOTTOM,
  fullscreen off; `fitBounds` padded (left 280 / right 400).
- Pins still colored by ROLE (navy tracked / green selected / orange Reddit), NOT
  by wind. Mockup's wind-tier pin coloring + bottom day strip NOT built.

## Verified (localhost:8804)

Satellite tiles + all pins render; Aurora loads by default with full panel
(Now readings, Best window, chart, Other days = 7). Switched to Lake McConaughy
via the Settings submit path → panel + region + week updated. chart svg present.
Pin-click path (`chooseSpotObject → run`) unchanged from the verified 2026-06-16
build.

## Operate / gotchas

- Added `.claude/launch.json` entry **`kite-wind-watch`** (http.server on **8804**,
  the referrer-restricted origin the Maps key needs). `preview_start
  kite-wind-watch` had been reusing the apartment-hunt config on 8753 (map dead).
- The preview-MCP screenshotter renders full-viewport `position:fixed` layouts
  tiny in the corner (looks broken, isn't). Verify sizes with `preview_eval`;
  capture the real visual with headless Chrome:
  `"…/Google Chrome" --headless=new --window-size=1440,900 --screenshot=/tmp/x.png --virtual-time-budget=6000 http://localhost:8804/index.html`.

## Side artifact (NOT in the app)

`~/Downloads/kite-spots.kml` — all 11 spots (blue tracked / green Dad's tips),
each with a Windguru/Windy forecast link — for Annabel to import into her personal
Google **My Maps** and drag/add pins. If she corrects coords there, export KML
back and sync `SPOTS`.

## Open / next (Annabel's call)

- Optional: color pins by current wind (needs fetching all spots' wind on load)
  + the bottom day strip from the mockup, so the map shows conditions at a glance.
- Mobile layout is a basic top-bar + bottom-sheet; not yet reviewed on a phone.
- Reddit scraping improvements still deferred from the prior checkpoint.
