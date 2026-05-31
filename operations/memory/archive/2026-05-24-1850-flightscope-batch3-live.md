---
date: 2026-05-24
time: 18:50
project: cli-connections/flights (flightscope)
status: complete
next-session: Optional polish — split catalog `airports` into nonstop `airport` vs drive-away `airports_nearby` so RAK-type results get a "+drive" flag; update connector docs (CONNECTION.md / commands.md) to document `plan` + `routes --kiteable`/`--to` and the consent-flake caveat.
---

# Session: Flightscope Batch 3 — live scraping wired + Tarifa query run

## What we worked on

Completed batch 3 of flightscope (`tools/flightscope/bin/flightscope`): installed
`fast-flights`, wired live `price` + `routes`, added a `plan` command, and ran the
live Tarifa query end-to-end. All four batch-3 tasks done.

## Decisions made

- **Price engine = fast-flights `local` mode**, not `fallback`. Google serves a
  consent/language page to the plain HTTP path; `fallback` relies on a flaky
  third-party hosted browser. Playwright + Chromium are already installed locally,
  so the CLI now defaults to `local` when Playwright is present (`default_fetch_mode()`),
  with a `--fetch-mode` override. `doctor` reports `price_fetch_mode`.
- **Routes endpoint found:** `airports_url.php?iata=<code>` → `{"c": <id>}`, then
  `rt<id>.json` whose `pts` array = directly-reachable destination airport ids.
  Plain curl works — **no Cloudflare gate, no cookie needed.** IATA→id cache lives
  at `~/.config/flightscope/fc-airport-ids.json` (outside repo).
- `routes --kiteable` intersects direct destinations with the windy catalog;
  `routes --to A,B` checks specific dests; skips a spot if origin is its own airport.
- `plan` is resilient: one flaky leg is recorded (`price_error`) not fatal; retries
  fetch once; sleeps 2s between legs (politeness per safety doc).

## Open questions

- Catalog conflates nonstop airports with drive-away ones (RAK listed under
  Essaouira but is ~2.5–3h from the coast). Split into `airport` vs `airports_nearby`?
- SVQ→ESU price consistently flakes on Google's consent interstitial — fast-flights
  local-mode limitation, not our bug. Leave as-is.

## Next steps

1. (Optional) Catalog airport split + "+drive" flag.
2. Update `cli-connections/flights/CONNECTION.md` + `references/commands.md` to
   document `plan`, `routes --kiteable`/`--to`, fetch-mode, and consent caveat.
3. Mark routes/price as wired in `tools/flightscope/PROGRESS.md`.

## Context to preserve

- **Live result (depart June 3 2026, one-way, AGP/SVQ, June-windy + direct, cheapest nonstop):**
  €15 Essaouira via RAK*(+drive)* | €24 Lanzarote SVQ→ACE | €26 Gran Canaria AGP→LPA |
  €35 Fuerteventura SVQ→FUE | €56 Fuerteventura AGP→FUE | €129 Sicily SVQ→TPS.
  No nonstop that date: Lanzarote AGP→ACE, Sardinia SVQ→OLB. Couldn't price: ESU.
- Practical picks for a flatwater/lagoon trip: **Fuerteventura** or **Lanzarote**
  (true nonstop, €24–56). Essaouira tops on price alone but is a wave spot + road transfer.
- Resume engine check: `tools/flightscope/bin/flightscope doctor`.
- macOS has no `timeout` binary — bit me once; use the tool's own timeout instead.

## System refinement candidates

- Proposed `~/.claude/CLAUDE.md` Operating Rules note: "macOS (darwin) has no
  `timeout` binary; use `gtimeout` or the tool's own timeout/run_in_background."
  (Awaiting Annabel's go-ahead — not yet applied.)
