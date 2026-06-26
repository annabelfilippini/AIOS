# Kite Wind Watch Content

## Purpose

Personal dashboard for Annabel to check whether nearby Colorado and driveable
high-plains kitesurf spots look worth watching over the next few days.

## Spots

Split across two region tabs in the UI (each spot carries an `area`):

**Front Range wind** (Denver area, all have coordinate-verified Windguru ids):

- Aurora Reservoir
- Cherry Creek Reservoir
- Chatfield Reservoir
- Union Reservoir
- Boyd Lake

**Colorado + Wyoming** (mountains / plains / driveable, plus Dad's tips):

- Lake Dillon, Pueblo Reservoir, Lake McConaughy (have Windguru ids)
- Lake Hattie Reservoir — Wyoming · Laramie — `41.2435, -105.9285` — Dad's tip
- Twin Buttes Lake — Wyoming · Laramie — `41.2387, -105.8622` — Dad's tip
- Williams Fork Reservoir — Colorado · Grand County — `40.0178, -106.2116` — Dad's tip

Dad's three spots had their coordinates verified via OSM Nominatim (2026-06-14).
They have no Windguru id yet, so they run on the 5 non-Windguru sources
(Open-Meteo ×4 + NWS); the dashboard shows Windguru as gracefully unavailable for
them. Add Windguru ids later via `cli-connections/windguru` if found.

## Community spot chatter (Colorado + Wyoming tab)

`scraper/scrape_reddit.py` searches Reddit (via Firecrawl — Reddit 403s direct
unauthenticated access) for people talking about CO/WY kite + snowkite spots and
writes `data/discourse.js`, which the dashboard reads into the "What people are
saying" panel: Dad's-spots chatter/quiet status, a "spots people mention" chip
row (new finds badged), and recent Reddit threads with snippets.

First scan (2026-06-14) confirmed Dad's **Lake Hattie** ("windy but gusty"),
found **no chatter yet** for Twin Buttes or Williams Fork, and surfaced two spots
not on the list: **Sloan Lake** (Denver, in-city) and **Georgetown Lake**
(snowkite). McConaughy is the most-recommended driveable spot.

## Forecast Sources

- Windguru GFS 13 km, by Windguru spot id.
- Open-Meteo Best Match.
- ECMWF IFS via Open-Meteo.
- NOAA GFS via Open-Meteo.
- DWD ICON via Open-Meteo.
- NWS official hourly forecast via `api.weather.gov`.

## Kiteability Heuristic

The page defaults to a 15 kt sustained wind threshold. A day counts as watchable
when at least three daytime hours meet or exceed the threshold. This is only a
screening heuristic; it does not account for lake launch rules, water level,
storm cells, rescue coverage, cold water, or gust quality.
