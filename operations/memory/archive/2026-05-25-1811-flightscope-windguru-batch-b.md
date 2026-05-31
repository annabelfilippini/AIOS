---
date: 2026-05-25
time: 18:11
project: cli-connections/flights (flightscope)
status: in-progress
next-session: Batch C — add cli-connections/windguru/ connector (CONNECTION.md + references/ + scripts/, mirroring flights/ and github/), and update flights CONNECTION.md to mention that `plan` now ranks by live wind. Optional: truncate long spot names in the `plan` human table (cosmetic column drift).
---

# Session: Flightscope Windguru Live Wind — Batch B (plan ranking)

## What happened this session

Picked up flightscope at Batch B (read the real latest checkpoint via `ls -t`,
not the stale recall top-match). Wired live Windguru wind into the `plan`
command end-to-end and live-verified all three decision branches. Bumped
flightscope to **v0.2.0**.

## What Batch B did (tools/flightscope/bin/flightscope)

Live wind is now a **hard filter + primary ranking** inside `plan`, exactly per
Annabel's recorded choice:

- Per reachable in-season spot, fetch the Windguru GFS forecast **once**, cached
  by `windguru_id` in a `wg_cache` dict (a spot reachable from multiple
  origins/dests isn't refetched).
- `classify(spot)` returns `(keep, source, wind_summary, note)`:
  - live + covered + `kiteable_days >= 1` → **keep**, `source="live"`.
  - live + covered + 0 kiteable days → **DROP** (and skip pricing it — saves the
    expensive browser scrape). Recorded in new `plan["wind_filtered"]`.
  - **not covered** (date beyond ~16-day GFS horizon) → keep, `source="season"`,
    flagged "beyond forecast horizon" — **never dropped**.
  - fetch failure / `no_forecast` / no `windguru_id` → keep, `source="season"`
    (don't punish a spot for a network blip or a missing id).
- Pricing now happens **after** the wind gate, so dropped spots cost no scrape.
- Human output: live spots ranked windiest-first (kiteable_days desc, then mean
  kt desc, then price asc); season-fallback spots in a separate section below
  ("season says windy — no live forecast for these dates yet"); a "filtered out"
  section lists wind-cut spots + why. Each row still shows price + airline +
  duration, with a `· 3/3 kiteable, 19kt avg peak 27 (lead 9d)` wind tail.
- New flags: `--days` (window, default 3), `--min-wind` (threshold kt, default
  12), `--no-wind` (restore old price-only behavior). JSON gains
  `wind_ranking`, `days`, `min_kt`, `wind_filtered`, and per-result
  `wind_source` / `wind_note` / trimmed `wind` (via new `_trim_wind`).
- `fc_kiteable_from` rows now carry `windguru_id` so `plan` can resolve forecasts
  without re-searching.

## Live verification (all 3 branches, real Windguru data)

- **Keep + rank** — `plan AGP --depart 2026-06-03`: Essaouira 19kt/€15 (AGP→RAK) >
  Gran Canaria 18kt/€26 (LPA) > Fuerteventura 14kt/€56 (FUE), all 3/3 kiteable,
  lead 9d. **Lanzarote (ACE) leg hit the known `.eQ35Ce` Playwright price-scrape
  timeout** — surfaced as an error row, not a crash (resilient-not-fail held).
- **Out-of-horizon fallback** — window 2026-07-15 (~51d out): all four spots
  `covered=False` → season fallback, none dropped. The guardrail works.
- **Hard drop** — `--min-wind 25` on June 3: Fuerteventura/Lanzarote/Gran Canaria
  dropped (peaks 21–22 < 25), only Essaouira survives (peak 27, 1 kiteable day).

## Dashboard regenerated (tools/flightscope/dashboard.html, v0.2.0)

Updated to reflect the new `plan` behavior (Annabel asked to see the changes):
- Decision board heading → "ranked by live wind (windiest first)"; added a **#
  rank column** (1–4). Rows reordered by mean kt: Essaouira 19kt (#1, €15) > Gran
  Canaria 18kt (#2, €26) > Lanzarote 17kt (#3, €24) > Fuerteventura 14kt (#4, €35).
- **Sicily** pulled into a dimmed `✕ hard-filtered out` row ("peaks 11 kt, never
  reaches the 12 kt bar") — the hard filter made visible.
- Legend rewritten: wind-first ordering (price no longer the sort key), the 12kt
  filter (+ filtered spots skipped before the slow scrape), and the out-of-horizon
  → season-fallback guardrail. Prices kept labeled "2026-05-24 query (not re-run)";
  wind matches today's live GFS init.
- Verified by a throwaway headless-Chrome screenshot (the Playwright MCP profile
  is held by a stale Chrome PID 46019 from the earlier price scrapes; Annabel said
  leave it). dashboard.html is just a snapshot — regenerate after future changes.

## Decisions

- Wind ranking is **primary**; price stays visible per row (Annabel's "hard
  filter + rank" choice from Batch A, now implemented). `--no-wind` is the escape
  hatch when Windguru is down or you only care about price.
- Drop a spot **only** on live+covered data below threshold; missing/uncovered/
  failed always falls back to season and is flagged.

## Known / parked (unchanged from before)

- `local`-mode Google price scrape still flakes on `.eQ35Ce` (Lanzarote leg this
  run); 2x in-code retry doesn't always catch it. Re-running usually clears it.
- Long spot names ("Gran Canaria (Pozo Izquierdo)") overflow the `:<22` column —
  cosmetic drift, not truncated yet.

## Resume with

- `tools/flightscope/bin/flightscope plan AGP --depart 2026-06-03`
- `tools/flightscope/bin/flightscope plan AGP --depart 2026-07-15`  (season fallback)
- `tools/flightscope/bin/flightscope plan AGP --depart 2026-06-03 --min-wind 25`  (drop demo)
- `tools/flightscope/bin/flightscope plan AGP --depart 2026-06-03 --no-wind`  (old behavior)
