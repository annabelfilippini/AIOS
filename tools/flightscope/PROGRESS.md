# Flightscope Build Progress

Personal flight routes + prices CLI (skool-pp-cli mold) for the kitesurf
travel-decision tool. Customer #1: solo kiter in Tarifa deciding where next.

## Done
- Batch 1: core CLI (`bin/flightscope`) + kite-spot seed (`data/kite-spots.json`, 13 spots).
  Offline commands verified: `version`, `doctor`, `airports`, `spots --wind`.
- Batch 2: connector scaffold under `cli-connections/flights/` (CONNECTION.md,
  references/, scripts/). Both check scripts run.

## Next (batch 3)
1. `pip install fast-flights` (approved) → wire/verify `price` (Google Flights).
2. Finalize `routes` against live flightconnections.com (find route-data
   endpoint; add `FLIGHTCONNECTIONS_CURL_FILE` cookie path only if Cloudflare gates it).
3. Live Tarifa test: from AGP/SVQ, which windy spots are reachable direct + price them.
4. Optional `plan <place>` command that chains spots → routes → price.

## Notes
- Tarifa has no airport; origins are GIB/XRY/AGP/SVQ.
- Not the Wayloft repo — Wayloft's no-airline-scrape rule is project-scoped there.
