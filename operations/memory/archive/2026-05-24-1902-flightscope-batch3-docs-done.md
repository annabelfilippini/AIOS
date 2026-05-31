---
date: 2026-05-24
time: 19:02
project: cli-connections/flights (flightscope)
status: complete
next-session: Flightscope batch 3 + docs are fully done. Only two parked items remain (both optional, neither blocking): (1) split catalog `airports` into nonstop `airport` vs drive-away `airports_nearby` so "via RAK" gets a "+drive" flag; (2) apply the pending macOS `timeout` note to ~/.claude/CLAUDE.md (awaiting Annabel's OK). Nothing committed yet.
---

# Session: Flightscope batch 3 — wired, queried, documented (closed out)

## What we worked on

Completed batch 3 of flightscope and then updated all connector docs + PROGRESS
to match. Code is wired and verified live; docs are current. This supersedes the
2026-05-24-1850 checkpoint (which captured the code work before docs).

## Decisions made

- Price engine defaults to fast-flights `local` mode (headless Playwright,
  already installed) — plain HTTP hits Google's consent page. `--fetch-mode` overrides.
- Routes wired via flightconnections `airports_url.php?iata=` → `rt<id>.json`
  (`pts` = direct dest ids). Plain requests; no Cloudflare gate, no cookie.
  IATA→id cache at `~/.config/flightscope/fc-airport-ids.json` (outside repo).
- `plan` is the fast path (catalog → routes → price, cheapest-first, resilient).
- RAK-vs-Essaouira airport conflation left as a documented caveat, not fixed yet.

## Open questions

- Whether to do the `airport` vs `airports_nearby` catalog split now or leave parked.
- Whether to apply the macOS `timeout` note to global CLAUDE.md (proposed, not applied).

## Next steps

1. (Optional) Catalog airport split + "+drive" flag in `data/kite-spots.json` and
   the route/plan output.
2. (Optional) Apply CLAUDE.md Operating Rules note re: no `timeout` on macOS.
3. Commit when Annabel asks (nothing committed this session).

## Context to preserve

- Files touched this session:
  - `tools/flightscope/bin/flightscope` (price local mode, routes engine, plan, retry/resilience)
  - `tools/flightscope/PROGRESS.md` (batch 3 → Done)
  - `cli-connections/flights/CONNECTION.md`, `references/commands.md`, `references/safety.md`
- Live result (depart June 3 2026, one-way, AGP/SVQ, windy + direct, cheapest nonstop):
  €15 Essaouira via RAK*(+drive)* | €24 Lanzarote SVQ→ACE | €26 Gran Canaria AGP→LPA |
  €35 Fuerteventura SVQ→FUE | €56 Fuerteventura AGP→FUE | €129 Sicily SVQ→TPS.
  No nonstop that date: Lanzarote AGP→ACE, Sardinia SVQ→OLB. Couldn't price: SVQ→ESU.
- Practical flatwater picks: Fuerteventura or Lanzarote (true nonstop, €24–56).
- Resume engine check: `tools/flightscope/bin/flightscope doctor`.
- Fast path to re-run the whole query: `flightscope plan AGP,SVQ --depart 2026-06-03`.

## System refinement candidates

- Proposed `~/.claude/CLAUDE.md` Operating Rules note: "macOS (darwin) has no
  `timeout` binary; use `gtimeout` or the tool's own timeout/run_in_background."
  Awaiting Annabel's go-ahead — not yet applied.
