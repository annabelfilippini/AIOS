---
date: 2026-05-24
time: 21:07
project: cli-connections/flights (flightscope)
status: in-progress
next-session: Add a Windguru CLI connection (live wind forecasts) so flightscope filters/ranks spots by actual forecast wind for the travel dates, not just static wind_months. Then optionally harden Google Flights local-fetch timeouts.
---

# Session: Flightscope Live Scraping Wired + EUR Fix

## What happened this session

Picked up the flightscope scaffold and got the full pipeline working live,
end-to-end, against both real sources. The checkpoint before this was stale:
`routes` and `price` were already fully implemented in code (not stubs), and
`fast-flights` + Playwright were already installed.

## Sources confirmed working (this is the architecture)

1. **flightconnections.com** — `routes` cmd. Hits internal JSON endpoints via
   plain `urllib` (no browser, ~1s): `airports_url.php?iata=agp` resolves IATA →
   internal id (AGP=188), then `rt<id>.json`'s `pts` array = all nonstop
   destinations. Answers "does a nonstop route exist", NOT price or date.
2. **Google Flights** — `price` cmd, via `fast-flights` driving a **local
   headless Chromium (Playwright)**. ~7s per fetch. Real prices/airlines/
   durations/stops for an exact date.
3. **Local catalog** `data/kite-spots.json` — 13 spots → airports + windy
   months. The wind filter that narrows 169 generic dests down to kite spots.

`plan` chains them: flightconnections routes ∩ windy catalog → price only the
survivors via Google Flights (direct-only) → rank cheapest-first. Design point:
never browser-scrape 169 dests; scrape ~8.

## Code changes made (tools/flightscope/bin/flightscope)

- **EUR fix (real bug):** Google was returning prices in **Mexican pesos**
  (geo-detected). Public `get_flights` hides the currency param, so switched to
  `get_flights_from_filter(TFSData.from_interface(...), currency=...)`. Added
  `--currency` flag, default **EUR**, on both `price` and `plan`.
- Pushed `max_stops=0` into `plan` so Google filters to nonstop at the source.
- Added `currency` to the price payload.

## Live query result (depart Tarifa June 3 2026, one-way, nonstop)

Origins AGP/SVQ. Cheapest-first windy spots reachable nonstop that day:
- €15 Essaouira AGP/SVQ→RAK (but RAK=Marrakech, ~3h drive to spot)
- €24 Lanzarote SVQ→ACE · €26 Gran Canaria AGP→LPA · €35 Fuerteventura SVQ→FUE
- €56 Fuerteventura AGP→FUE · €58 Gran Canaria SVQ→LPA · €129 Sicily SVQ→TPS
- No nonstop June 3: AGP→ACE (Lanzarote from Málaga), SVQ→OLB (Sardinia).
- Recommendation given: Lanzarote €24 or Fuerteventura €35 from Sevilla =
  best reliable-June-wind + cheap + lands at the spot.

## Decisions

- Currency defaults to EUR (Annabel travels from Spain). Overridable per-run.
- `plan` is nonstop-only by design (max_stops=0).
- Keep flightconnections as the cheap pre-filter before paying Google-fetch cost.

## Next steps

1. **Windguru CLI connection (next focus).** Add a `cli-connections/windguru/`
   connector + wire flightscope to live Windguru forecasts so spots are
   filtered/ranked by ACTUAL forecast wind for the travel window, replacing the
   static `wind_months` heuristic. Windguru = windguru.cz; each spot has a
   numeric station id — likely needs a station-id mapping in the catalog.
2. Harden Google Flights local-fetch timeouts (3 of 11 fetches hit a 30s
   Playwright `.eQ35Ce` locator timeout; in-code 2x retry didn't catch all).
3. Optional: surface "route exists but no nonstop on date" more cleanly in
   `plan` (currently can show as a fetch error rather than a clean "no nonstop").

## Open questions

- Windguru data access: public page scrape vs. their API (API may need a
  key/account) vs. an existing CLI. Confirm stack reality before building —
  don't assume an API key exists.
- Map each catalog spot to its Windguru station id (manual lookup, one-time).

## Resume with

- `tools/flightscope/bin/flightscope doctor`
- Re-run the live query: `tools/flightscope/bin/flightscope plan AGP,SVQ --depart 2026-06-03`
