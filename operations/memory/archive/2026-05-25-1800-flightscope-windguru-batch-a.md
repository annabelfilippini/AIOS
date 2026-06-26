---
date: 2026-05-25
time: 18:00
project: cli-connections/flights (flightscope)
status: in-progress
next-session: Batch B — wire live Windguru wind into `plan` ranking. Hard-filter spots below 12kt for the travel window (Annabel's choice), rank survivors by forecast wind; out-of-horizon dates fall back to wind_months + flag (do NOT drop). Then Batch C — add cli-connections/windguru/ connector docs + update flights CONNECTION.
---

# Session: Flightscope Windguru Live Wind — Batch A + Dashboard

## What happened this session

Picked up flightscope (note: startup recall surfaced the STALE 18:08 scaffold
checkpoint; the real latest was 21:07 — caught via `ls -t` + PROGRESS.md). Built
the Windguru live-wind layer (Batch A of 3) and a visualization dashboard
Annabel asked for mid-session.

## Windguru data access — RESOLVED (was the open blocker)

`windguru.cz/int/iapi.php` is **public, no API key, plain urllib JSON** (same
cheap-fetch profile as flightconnections — no browser):

- `?q=search_spots&search=<name>` → name → numeric spot id (one-time mapping).
- `?q=forecast&id_model=3&id_spot=<id>` → `fcst` with `WINDSPD`/`GUST`/`WINDDIR`
  arrays in **knots** + `hours` offsets from `initdate`. Model 3 = GFS 13km,
  **~16-day horizon** so far-out dates (Jun 3 = 9d out) ARE covered — with a
  lead-time caveat that must be surfaced, not hidden.

## Code added (tools/flightscope/bin/flightscope)

- `windguru` engine: `_wg_get`, `windguru_search`, `windguru_forecast`
  (builds per-hour series; local time approximated via longitude→tz offset =
  `round(lon/15)`, no tz database), `wind_window` (summarizes a travel window),
  `_deg_to_compass`, `resolve_wg_spot`.
- `wind <spot> [--when --days --min-wind --id]` command + dispatch + parser +
  doctor checks (`kite_spots_with_windguru_id`, `wind (windguru)` readiness).
- **Units bug fixed (real):** GFS steps go 3-hourly past ~day 7, so a raw point
  count mislabeled far-out days (e.g. "3h" was 3 steps = 9h). Now scales by the
  **modal step spacing measured inside the window** (not the global series min,
  which would wrongly pick the 1h near-term spacing). `kiteable_hours` is honest
  clock-hours at any lead.
- Defaults: `KITEABLE_MIN_KT=12`, daytime window 9–20h local, 3-day window,
  `is_kite` = ≥3 kiteable daytime hours.

## Catalog (data/kite-spots.json)

Added `windguru_id` to all 13 spots, each **coordinate-verified** (search hit's
forecast lat/lon vs the real spot, all within 0.7–12.7km; Fuerteventura/Sotavento
loosest at 12.7km, still inside the 13km GFS grid). Added `_meta.windguru_id` doc.
Map: Tarifa 113924, Fuerteventura 49329, Lanzarote 800467, Gran Canaria 123902,
Leucate 48582, Sardinia 49162, Sicily 1177450, Rhodes 1335221, Naxos/Paros 36,
Lefkada 4448, Dakhla 49317, Essaouira 58432, Sal 206839.

## Dashboard (tools/flightscope/dashboard.html)

Self-contained HTML Annabel requested to visualize current state. Sections:
decision board (June 3 from AGP/SVQ joining price + LIVE wind, cheapest-first,
per-day peak-wind sparkline bars), 3-source architecture + join pipeline, full
13-spot catalog with wind-season month chips + windguru ids. Honesty baked in:
live wind = fresh (GFS, 9d lead, flagged soft); **prices labeled "from 2026-05-24
query"** (re-pricing is a slow scrape, not re-run). Generated snapshot — regenerate
after changes. Live-screenshot-verified before presenting.

## Live results confirmed (June 3 window, fresh wind)

All Canary spots 3/3 kiteable days: Lanzarote 17kt avg / NNE, Gran Canaria,
Fuerteventura, Essaouira 19kt. Tarifa today 21–23kt Levante (E), 3/3.

## Decisions

- Wind feeds ranking as **hard filter + rank** (Annabel chose), with the
  out-of-horizon → wind_months fallback guardrail so far-out dates don't wrongly
  delete every spot.
- GFS model 3 (free, global, 16-day) is the wind source; surface init+lead always.
- Prices not re-run for the dashboard; labeled with their query date instead.

## Also this session

- Added one line to `~/.claude/CLAUDE.md` (Operating Rules): when told to read
  "the most recent checkpoint," `ls -t` the checkpoints dir and trust that — the
  startup recall brief's top match can be a superseded older checkpoint.

## Resume with

- `tools/flightscope/bin/flightscope doctor`
- `tools/flightscope/bin/flightscope wind "Lanzarote" --when 2026-06-03`
- Open `tools/flightscope/dashboard.html`
