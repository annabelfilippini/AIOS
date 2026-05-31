# Flightscope Commands

All commands accept `--json` for machine-readable output. Binary lives at
`tools/flightscope/bin/flightscope`.

## Environment

```bash
tools/flightscope/bin/flightscope --version
tools/flightscope/bin/flightscope doctor          # checks + per-command readiness
```

## Where am I? (place → airports)

```bash
tools/flightscope/bin/flightscope airports "Tarifa"
# -> Tarifa (ES): GIB, XRY, AGP, SVQ
```

## Where's the wind? (kite-spot catalog)

```bash
tools/flightscope/bin/flightscope spots                       # all spots
tools/flightscope/bin/flightscope spots --wind                # only kiteable this month
tools/flightscope/bin/flightscope spots --wind --when 2026-07-01
tools/flightscope/bin/flightscope spots --region canary
```

## Where can I fly direct? (routes)

```bash
tools/flightscope/bin/flightscope routes AGP --json        # count of direct dests

# which windy kite spots are reachable direct from here?
tools/flightscope/bin/flightscope routes AGP --kiteable
tools/flightscope/bin/flightscope routes AGP --kiteable --when 2026-06-03
tools/flightscope/bin/flightscope routes AGP --kiteable --all-seasons

# is a specific destination reachable direct?
tools/flightscope/bin/flightscope routes AGP --to FUE,ACE,RHO
```

Routes uses plain requests today (no cookie needed). If flightconnections ever
gates the request, supply a browser cookie export:

```bash
FLIGHTCONNECTIONS_CURL_FILE=/path/outside/repo/fc-curl.txt \
  tools/flightscope/bin/flightscope routes AGP --json
```

## What does it cost? (Google Flights price)

```bash
# one-way
tools/flightscope/bin/flightscope price AGP FUE --depart 2026-06-01

# round-trip, 2 adults
tools/flightscope/bin/flightscope price SVQ RHO \
  --depart 2026-06-10 --return 2026-06-20 --adults 2 --json

# force a fetch engine (default is local headless browser)
tools/flightscope/bin/flightscope price AGP FUE --depart 2026-06-01 --fetch-mode local
```

## One shot: where should I go? (plan)

Chains catalog → direct routes → price for each origin, sorted cheapest-first.

```bash
tools/flightscope/bin/flightscope plan AGP,SVQ --depart 2026-06-03
tools/flightscope/bin/flightscope plan AGP,SVQ --depart 2026-06-03 --all-seasons --json
```

Each leg that has no nonstop on the date, or whose price fetch flakes, is listed
separately rather than aborting the run.

## The intended workflow (Tarifa example)

Fast path: `plan AGP,SVQ --depart DATE` does the whole thing. The manual steps:

1. `airports "Tarifa"` → get GIB/XRY/AGP/SVQ.
2. `spots --wind` → which kite spots have wind this month.
3. `routes AGP --kiteable` (and SVQ) → which windy spots are reachable direct.
4. `price AGP <spot-airport> --depart …` → price the reachable, windy ones.
