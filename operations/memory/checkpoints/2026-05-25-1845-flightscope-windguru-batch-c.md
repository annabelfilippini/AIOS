---
date: 2026-05-25
time: 18:45
project: cli-connections/flights (flightscope) + cli-connections/windguru
status: complete
next-session: Flightscope feature work (Windguru live-wind, batches A–C) is done. Open follow-ups are all pre-existing/parked, not new — see "Known / parked" below. Natural next steps if Annabel returns to this: split catalog `airports` into `airport` vs `airports_nearby` (the RAK road-transfer ambiguity), and harden the `local`-mode Google price scrape against the `.eQ35Ce` timeout.
---

# Session: Flightscope Windguru — Batch C (windguru connector + flights doc + truncation)

## What happened this session

Resumed at Batch C (read the real latest checkpoint via `ls -t`, per the
operating rule). Completed the last batch of the Windguru work: a standalone
`cli-connections/windguru/` connector, a flights CONNECTION update for the new
live-wind `plan`, and the parked cosmetic column-truncation fix. No flightscope
behavior changed except the one cosmetic format line; the connector is docs.

## What Batch C delivered

1. **New connector `cli-connections/windguru/`** — mirrors `flights/` and
   `github/` exactly (CONNECTION.md + references/commands.md + references/safety.md
   + scripts/check-installed.sh + scripts/check-auth.sh). Shares the flightscope
   binary (`binary: tools/flightscope/bin/flightscope`); documents the `wind`
   command and the public Windguru GFS source:
   - `windguru.cz/int/iapi.php`, **no key / no login / no cookie / no browser**,
     plain `urllib` JSON (stdlib only → `approval_required: []`).
   - `q=search_spots` (name→id, one-time mapping) and `q=forecast&id_model=3`
     (GFS 13km, ~16-day horizon, knots).
   - Defaults documented: 12 kt, daytime 9–20h local, 3-day window, ≥3 kiteable
     daytime hours = kiteable day; out-of-horizon → `covered:false` → season
     fallback; modal-step-spacing scaling for honest clock-hours.
   - Scripts made executable and **live-verified**: `check-installed` → `0.2.0`;
     `check-auth` → doctor shows 13/13 spots with `windguru_id`, `wind
     (windguru): true`.
2. **`cli-connections/flights/CONNECTION.md` updated** — the `plan` bullet now
   says it filters + ranks by live Windguru wind (hard filter at `--min-wind`
   default 12kt, windiest-first primary sort, price after the wind gate, out-of-
   horizon → season fallback flagged not dropped, `--no-wind` escape hatch).
   Added `--min-wind` / `--no-wind` to `safe_commands`, added a Windguru entry to
   Data Sources, cross-linked `../windguru/CONNECTION.md` both ways.
3. **Cosmetic truncation (the parked item)** — `fmt_row` in `cmd_plan` now caps
   the spot name at the 22-col width (`name[:21] + "…"`) so long names like
   "Gran Canaria (Pozo Izquierdo)" no longer shove the `origin->dest` / airline /
   duration columns out of alignment. Verified by unit check: all catalog names
   render ≤22 chars, columns line up.

## Verification

- `python3 -m py_compile tools/flightscope/bin/flightscope` → OK; `--version` →
  0.2.0 (binary unchanged in behavior).
- `flightscope wind "Tarifa" --when 2026-06-03` → live output matches the
  documented header/per-day/verdict format (Tarifa 0/3 kiteable, 9kt avg, lead
  9d on today's GFS init).
- Did NOT run a full live `plan` (price scrapes are slow + the known `.eQ35Ce`
  flake); the truncation is a pure format change, unit-verified against real
  names instead.

## Decisions

- Windguru is its own connector even though it shares the flightscope binary —
  it's a distinct data source (free stdlib JSON) vs the flights price/route
  engines, and `audience`/`safe_commands` differ. Kept the binary pointer shared
  rather than duplicating.

## Known / parked (pre-existing, unchanged)

- `local`-mode Google price scrape still flakes on `.eQ35Ce`; re-running clears it.
- `airports` mixes nonstop + drive-away airports (RAK under Essaouira ~2.5–3h
  away) — `airport` vs `airports_nearby` split still parked.
- dashboard.html is a 2026-05-24-priced snapshot; regenerate after price re-runs.

## Resume with

- `cli-connections/windguru/scripts/check-auth.sh`  (doctor + windguru readiness)
- `tools/flightscope/bin/flightscope wind "Lanzarote" --when 2026-06-03`
- `tools/flightscope/bin/flightscope plan AGP --depart 2026-06-03`  (full live run)
