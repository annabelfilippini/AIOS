# Flightscope Build Progress

Personal flight routes + prices CLI (skool-pp-cli mold) for the kitesurf
travel-decision tool. Customer #1: solo kiter in Tarifa deciding where next.

## Done
- Batch 1: core CLI (`bin/flightscope`) + kite-spot seed (`data/kite-spots.json`, 13 spots).
  Offline commands verified: `version`, `doctor`, `airports`, `spots --wind`.
- Batch 2: connector scaffold under `cli-connections/flights/` (CONNECTION.md,
  references/, scripts/). Both check scripts run.
- Batch 3 (2026-05-24): live scraping wired + Tarifa query run.
  - `price`: installed `fast-flights`; defaults to `local` fetch mode (headless
    browser via already-installed Playwright). `--fetch-mode` override. Verified live.
  - `routes`: wired against flightconnections.com via `airports_url.php` → `rt<id>.json`
    (`pts` = direct dest ids). No Cloudflare gate, no cookie needed. IATA→id cached at
    `~/.config/flightscope/fc-airport-ids.json` (outside repo). Added `--kiteable`/`--to`.
  - `plan <FROM,FROM2> --depart`: chains catalog → routes → price, cheapest-first,
    resilient to flaky legs (retry once, report-not-fail). Added.
  - Live query ran (depart June 3 2026, one-way, AGP/SVQ): cheapest nonstop windy
    spots = Essaouira €15 (via RAK +drive), Lanzarote €24, Gran Canaria €26,
    Fuerteventura €35. Full table in the 2026-05-24-1850 checkpoint.
- Batch 4 (2026-05-24, 21:07): currency fix + re-ran live query.
  - **EUR fix:** Google returned Mexican pesos (geo-detected). Public `get_flights`
    hides the currency param → switched to `get_flights_from_filter(TFSData..., currency=)`.
    Added `--currency` (default EUR) on `price` and `plan`; `plan` now pushes `max_stops=0`.
  - Re-ran `plan AGP,SVQ --depart 2026-06-03` in EUR; results confirmed. See
    2026-05-24-2107-flightscope-live-wired checkpoint.

- Batch 5 (2026-05-25): Windguru live wind — Batch A done.
  - Data access confirmed: `windguru.cz/int/iapi.php` is public, no key. `q=search_spots`
    maps name→id; `q=forecast&id_model=3` returns WINDSPD/GUST/WINDDIR in knots, ~16-day
    (GFS) horizon (covers far-out dates like Jun 3, with lead-time caveat surfaced).
  - Added `windguru` engine + `wind <spot>` command (daytime filter via longitude→tz
    offset; honest hour-scaling for 3-hourly far-out steps). All 13 catalog spots mapped
    to coordinate-verified `windguru_id`. Live-tested.
  - Generated `dashboard.html` (decision board joining price + live wind, architecture,
    catalog). Snapshot — regenerate after changes.
  - Batch B done (2026-05-25): live wind wired into `plan` (v0.2.0). Per reachable spot,
    fetch Windguru forecast once (cached by `windguru_id`); wind is a HARD FILTER (drop +
    skip pricing spots forecast below `--min-wind`, default 12kt) and the PRIMARY RANKING
    (windiest first: kiteable_days, then mean kt). Out-of-horizon dates, fetch failures,
    and no-id spots fall back to season (`wind_months`) and are flagged `season` — never
    dropped for missing live data. Added `--days`, `--min-wind`, `--no-wind` (old price-only
    path). New `wind_filtered` list shows what got cut and why. Live-verified all 3 branches:
    June 3 AGP ranks Essaouira 19kt/€15 > Gran Canaria 18kt/€26 > Fuerteventura 14kt/€56
    (Lanzarote leg hit the known `.eQ35Ce` price-scrape flake, reported not crashed);
    July 15 (51d out) → all season-fallback, not dropped; `--min-wind 25` drops all but Essaouira.

## Parked / next
- **Batch C (next):** add `cli-connections/windguru/` connector (CONNECTION.md, references/,
  scripts/) mirroring flights/github; update flights CONNECTION.md to mention wind ranking.
- Harden `local`-mode Google fetch timeouts: 3 of 11 legs hit a 30s Playwright
  `.eQ35Ce` locator timeout; the 2x in-code retry didn't catch all.
- Split catalog `airports` into nonstop `airport` vs drive-away `airports_nearby`
  so "via RAK" results get a "+drive" flag (RAK is ~2.5–3h from Essaouira).

## Notes
- Tarifa has no airport; origins are GIB/XRY/AGP/SVQ.
- Not the Wayloft repo — Wayloft's no-airline-scrape rule is project-scoped there.
