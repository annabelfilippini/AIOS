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
  - tools/flightscope/bin/flightscope routes "<IATA>" --kiteable --json
  - tools/flightscope/bin/flightscope routes "<IATA>" --to "<A,B,C>" --json
  - tools/flightscope/bin/flightscope price "<FROM>" "<TO>" --depart "<YYYY-MM-DD>" --json
  - tools/flightscope/bin/flightscope plan "<FROM,FROM2>" --depart "<YYYY-MM-DD>" --json
  - tools/flightscope/bin/flightscope plan "<FROM,FROM2>" --depart "<YYYY-MM-DD>" --min-wind 15 --json
  - tools/flightscope/bin/flightscope plan "<FROM,FROM2>" --depart "<YYYY-MM-DD>" --no-wind --json
approval_required:
  - pip install fast-flights   # already installed 2026-05-24; listed for re-provisioning
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
  - `--kiteable [--when DATE] [--all-seasons]` — intersect with the windy-spot
    catalog: which kite spots are reachable direct from here.
  - `--to A,B,C` — reachability check for specific destination IATA codes.
- `price <FROM> <TO> --depart DATE [--return DATE] [--fetch-mode M]` — Google
  Flights price. Defaults to `local` (headless browser) when Playwright is present.
- `plan <FROM,FROM2> --depart DATE [--all-seasons] [--days N] [--min-wind KT]
  [--no-wind]` — one-shot: for each origin, find windy catalog spots reachable
  direct, **filter and rank them by live Windguru wind** for the travel window,
  then price the survivors. Live wind is a hard filter at `--min-wind` (default
  12 kt) and the **primary sort** (windiest-first), with price shown per row;
  pricing runs only after the wind gate, so spots cut for low wind cost no
  scrape. Spots whose dates fall beyond the GFS horizon fall back to the catalog
  wind season and are flagged, never dropped. `--no-wind` restores the old
  price-only behavior. Resilient — a flaky leg is reported, not fatal. See the
  [windguru](../windguru/CONNECTION.md) connector for the wind source.

## Data Sources & Engines

- **Google Flights** via the `fast-flights` Python package. The plain-HTTP path
  hits a Google consent/language page, so flightscope defaults to fast-flights'
  `local` fetch mode — a real local headless browser (needs the `playwright`
  package + Chromium, both already installed). Override with `--fetch-mode`.
  Known limitation: `local` mode occasionally times out on Google's consent
  interstitial for a given leg; `plan` retries once and continues past failures.
- **flightconnections.com** for direct-route maps. Wired via two endpoints:
  `airports_url.php?iata=<code>` → internal airport id, then `rt<id>.json` whose
  `pts` array is the list of directly-reachable destination ids. Plain requests
  work today — **no Cloudflare gate, no cookie needed**. IATA→id lookups are
  cached at `~/.config/flightscope/fc-airport-ids.json` (outside the repo). If
  the site ever starts gating, pass a browser cookie export via
  `FLIGHTCONNECTIONS_CURL_FILE` (same idea as skool-pp-cli's `SKOOL_CURL_FILE`).
- **Local catalog** at `tools/flightscope/data/kite-spots.json` — edit freely.
  Note: `airports` mixes nonstop airports with drive-away ones (e.g. RAK is
  listed under Essaouira but is ~2.5–3h away), so a cheap "via RAK" result can
  hide a road transfer. A future split into `airport` vs `airports_nearby` is parked.
- **Windguru** live GFS wind powers the `plan` wind filter/ranking and the
  standalone `wind` command. Stdlib-only public JSON — see the
  [windguru](../windguru/CONNECTION.md) connector for the engine and catalog
  details.

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
