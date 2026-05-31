---
name: windguru
display_name: Windguru (live GFS wind forecast)
binary: tools/flightscope/bin/flightscope
audience:
  - annie
  - business-partner
runtime:
  - claude
  - codex
visibility: private
related_skills: []
safe_commands:
  - tools/flightscope/bin/flightscope doctor --json
  - tools/flightscope/bin/flightscope wind "<spot>" --json
  - tools/flightscope/bin/flightscope wind "<spot>" --when "<YYYY-MM-DD>" --json
  - tools/flightscope/bin/flightscope wind "<spot>" --when "<YYYY-MM-DD>" --days 5 --min-wind 15 --json
  - tools/flightscope/bin/flightscope wind --id <windguru_id> --json
approval_required: []   # stdlib-only (urllib); no install, no key, no browser
---

# Windguru Connection

Live wind forecast for kite spots, read from Windguru's public GFS model. This
is the **wind** half of flightscope: it answers "will it actually be windy at
this spot during my travel window?" while the [flights](../flights/CONNECTION.md)
connector answers "can I get there and what does it cost?". The two share one
binary — `tools/flightscope/bin/flightscope` — and Windguru data also drives the
`plan` command's wind ranking.

Use this connection when the task is: "is spot X kiteable on these dates?" or
"rank these reachable spots by how windy they'll be."

## What It Does

- `wind <spot> [--when DATE] [--days N] [--min-wind KT] [--id ID]` — live GFS
  forecast for a catalog spot over a travel window. Resolves the spot name (or
  region substring) to its `windguru_id` from the local catalog; falls back to a
  name search and prints candidate ids if there's no catalog match. Output is a
  per-day mean/peak/direction line plus a `kiteable_days / window` verdict.
- The same forecast layer is consumed by `flightscope plan` as a **hard wind
  filter + primary ranking** (see the flights connector). `wind` is the
  standalone, single-spot view of that data.

## Data Source & Engine

- **Windguru** via `https://www.windguru.cz/int/iapi.php` — public, **no API key,
  plain `urllib` JSON, no browser**. Same cheap-fetch profile as the
  flightconnections route source; nothing to install beyond Python stdlib.
- Two query types:
  - `?q=search_spots&search=<name>` → name → numeric `id_spot` (used **one-time**
    to map a new catalog spot to its id; not on the hot path).
  - `?q=forecast&id_model=3&id_spot=<id>` → `fcst` with `WINDSPD` / `GUST` /
    `WINDDIR` arrays in **knots/degrees** plus `hours` offsets from `initdate`.
- **Model 3 = GFS 13 km**: free, global, **~16-day horizon**, so dates a week or
  two out are covered — with a lead-time caveat that is always surfaced, never
  hidden. Longer lead = softer forecast.
- Local time is approximated from longitude (`tz_off = round(lon / 15)`), so the
  daytime window filter is roughly right **without a timezone database**.
- GFS steps are hourly near-term but **3-hourly past ~7 days**, so `wind` measures
  the modal step spacing *inside the window* and scales by it — `kiteable_hours`
  is honest clock-hours whether the date is tomorrow or ten days out.

## Defaults (kiteability judgement)

- `KITEABLE_MIN_KT = 12` kt sustained — the lower bound for a "kiteable" hour.
- Daytime window `9–20h` local; only daytime hours are judged.
- 3-day travel window unless `--days` overrides.
- A day counts as kiteable when it has **≥ 3 kiteable daytime hours** (a few
  hours, not a single gust).
- Out-of-horizon dates report `covered: false` so callers fall back to the
  catalog's wind season instead of treating "no data" as "no wind."

## Catalog

Spot → `windguru_id` mappings live in
`tools/flightscope/data/kite-spots.json` (13 spots, each coordinate-verified
against the search hit's forecast lat/lon, all inside the 13 km GFS grid). Add a
new spot by running a one-time `search_spots` query (or `wind "<name>"` and
reading the printed candidate ids), then dropping the id into the catalog entry.

## Safety Model

- Personal-use tool. Fetch at human pace — one forecast per spot; do not loop
  high-volume polling against `iapi.php`.
- Read-only public JSON. No login, no key, no cookie, no token — so there is
  nothing to commit by accident, but still **never** add credentials to this
  folder.
- Treat forecast values as forecasts: surface model init time and lead days, and
  never present a far-out value as a guarantee.

## Verification

- Run `scripts/check-installed.sh` before assuming the CLI is runnable.
- Run `scripts/check-auth.sh` to confirm the Windguru forecast path is reachable
  and how many catalog spots carry a `windguru_id` (it just runs `doctor`; there
  is no auth to check).
