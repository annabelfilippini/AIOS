# Windguru Commands

Live GFS wind for kite spots, served by the shared flightscope binary at
`tools/flightscope/bin/flightscope`. All commands accept `--json`.

## Environment

```bash
tools/flightscope/bin/flightscope doctor          # includes wind/windguru readiness
```

`doctor` reports `kite_spots_with_windguru_id` and a `wind (windguru)` ready
flag (true once at least one catalog spot has an id).

## Is this spot kiteable? (wind)

```bash
# default: today + 3 days, ≥12 kt, daytime 9–20h local
tools/flightscope/bin/flightscope wind "Tarifa"

# a specific travel window
tools/flightscope/bin/flightscope wind "Lanzarote" --when 2026-06-03

# longer window, stricter threshold
tools/flightscope/bin/flightscope wind "Essaouira" --when 2026-06-03 --days 5 --min-wind 15
```

Output per day shows mean kt, peak kt + direction, and kiteable daytime hours,
ending in a `kiteable_days / window` verdict. The header always prints the model
init time and **lead days** — longer lead means a softer forecast.

## Spot not in the catalog? (search by name)

If the name/region substring matches no catalog spot, `wind` falls back to a
Windguru name search and prints candidate ids:

```bash
tools/flightscope/bin/flightscope wind "Jericoacoara"
# -> No catalog spot matches 'Jericoacoara'.
#      windguru search hits (re-run with --id to force one):
#         <id>  Jericoacoara (BR)
```

Force a specific Windguru id directly (bypasses the catalog):

```bash
tools/flightscope/bin/flightscope wind --id 113924 --when 2026-06-03   # Tarifa
```

To make a spot permanent, add its `windguru_id` to the matching entry in
`tools/flightscope/data/kite-spots.json`.

## Out-of-horizon dates

GFS reaches ~16 days. For a window beyond that, `wind` prints a "beyond the
forecast horizon — no live data for these dates" notice and marks days
`covered: false` rather than reporting them as un-windy. In `plan`, those spots
fall back to the catalog's wind season and are flagged, never dropped.

## How this feeds `plan`

`flightscope plan` fetches this same forecast once per reachable in-season spot
(cached by `windguru_id`), uses it as a hard filter at `--min-wind`, and ranks
survivors windiest-first. See the flights connector's `commands.md` for the
`plan` flags (`--days`, `--min-wind`, `--no-wind`).
