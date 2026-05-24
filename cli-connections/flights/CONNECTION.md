---
name: flights
display_name: Flightscope (flight routes + prices CLI)
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
  - tools/flightscope/bin/flightscope --version
  - tools/flightscope/bin/flightscope doctor --json
  - tools/flightscope/bin/flightscope airports "<place>" --json
  - tools/flightscope/bin/flightscope spots --wind --json
  - tools/flightscope/bin/flightscope routes "<IATA>" --json
  - tools/flightscope/bin/flightscope price "<FROM>" "<TO>" --depart "<YYYY-MM-DD>" --json
approval_required:
  - pip install fast-flights
---

# Flightscope Connection

A reusable CLI scraper for flight **routes** (flightconnections.com) and flight
**prices** (Google Flights), in the `skool-pp-cli` mold. Built as Annabel's
personal travel-decision tool — customer #1 is a solo kitesurfer deciding where
to go next based on where flights actually reach, what they cost, and where the
wind is.

Use this connection when the task is: "from where I am, which kiteable spots are
reachable by direct flight and what do they cost?"

## What It Does

- `doctor` — environment + per-command readiness (no network).
- `airports <place>` — resolve a place to nearby IATA codes (e.g. Tarifa →
  GIB/XRY/AGP/SVQ). Tarifa has no airport of its own.
- `spots [--wind] [--region R] [--when DATE]` — local kite-spot catalog with
  nearest airports and wind season; `--wind` keeps only spots kiteable that month.
- `routes <IATA>` — direct destinations from an airport (flightconnections.com).
- `price <FROM> <TO> --depart DATE [--return DATE]` — Google Flights price.

## Data Sources & Engines

- **Google Flights** via the `fast-flights` Python package (hits Google's
  internal `TFS` endpoint; no browser). Installing it requires approval.
- **flightconnections.com** for direct-route maps. Cloudflare-protected and
  client-rendered; if it starts gating requests, pass a browser cookie export
  via `FLIGHTCONNECTIONS_CURL_FILE` (same idea as skool-pp-cli's
  `SKOOL_CURL_FILE`).
- **Local catalog** at `tools/flightscope/data/kite-spots.json` — edit freely.

## Safety Model

- Personal-use tool. Scrape only at human pace; do not hammer either source.
- This is NOT the Wayloft project — Wayloft's "do not scrape airline sites" rule
  is project-scoped to that repo. Flightscope reads Google Flights and
  flightconnections (aggregators/search), not airline-owned booking/login flows.
  Do not extend it to airline login, checkout, seat maps, or CAPTCHA bypass.
- Do not commit cookies, cURL exports, or any session token into AI-OS. Store a
  cookie file outside the repo and reference it via `FLIGHTCONNECTIONS_CURL_FILE`.
- Config (if used) lives at `~/.config/flightscope/config.toml`.

## Verification

- Run `scripts/check-installed.sh` before assuming the CLI is runnable.
- Run `scripts/check-auth.sh` to see whether the price engine and the optional
  flightconnections cookie are present.
