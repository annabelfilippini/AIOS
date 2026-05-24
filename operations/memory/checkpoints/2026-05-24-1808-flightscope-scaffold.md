---
date: 2026-05-24
time: 18:08
project: cli-connections/flights (flightscope)
status: in-progress
next-session: Install fast-flights, wire live scraping, run the live query — depart Tarifa June 3 2026 (one-way), find the next windy kite spot reachable by direct flight from AGP/SVQ.
---

# Session: Flightscope Scaffold (flight routes + prices CLI)

## What this is

A reusable CLI scraper in the `skool-pp-cli` mold, built as Annabel's personal
travel-decision tool. Customer #1: solo kiter in Tarifa deciding where to go
next based on where flights actually reach + cost + where the wind is.
NOT the Wayloft project (Wayloft's no-airline-scrape rule is scoped to that repo).

## What we built (scaffold complete, runnable)

- `tools/flightscope/bin/flightscope` — Python stdlib CLI. Commands: `version`,
  `doctor`, `airports`, `spots`, `routes`, `price`.
- `tools/flightscope/data/kite-spots.json` — 13 real kite spots → airports + wind months.
- `cli-connections/flights/` connector mirroring github/skool: `CONNECTION.md`
  (binary, safe_commands, approval_required, safety model), `references/commands.md`,
  `references/safety.md`, `scripts/check-installed.sh`, `scripts/check-auth.sh`.
- `tools/flightscope/PROGRESS.md` — build log.

**Working offline now:** `version`, `doctor`, `airports`, `spots --wind`.
**Stubbed, not wired:** `routes` (flightconnections.com) and `price` (Google Flights).

## Decisions made

- Build approach: full connector scaffold first, then wire scraping + test (Annabel chose this).
- Two sources: flightconnections.com (routes) + Google Flights via `fast-flights` (prices).
- Self-contained like skool-pp-cli — no MCP needed at runtime.
- Cookie pattern mirrors skool: optional `FLIGHTCONNECTIONS_CURL_FILE` env (kept outside repo) only if Cloudflare gates requests.
- `fast-flights` install is approved (in connector's approval_required list).

## Next steps (batch 3 — next session)

1. `pip install fast-flights`, then verify/wire `price`.
2. Finalize `routes` against live flightconnections.com (find route-data endpoint; add cookie only if gated).
3. **Live query:** depart Tarifa **June 3 2026, one-way**. Tarifa has no airport →
   origins **AGP / SVQ** (also GIB/XRY). Find June-windy spots reachable direct, then price them.
4. Optional `plan <place> --depart` command chaining spots → routes → price.

## Context to preserve

- June-windy spots in the catalog (wind_months includes 6): Fuerteventura, Lanzarote,
  Gran Canaria, Sardinia, Sicily, Rhodes, Naxos/Paros, Lefkada, Dakhla, Essaouira, Sal.
- Resume the CLI via: `tools/flightscope/bin/flightscope doctor`.
- Catalog is `edit_freely` — add spots as needed.

## Also this session

- Added one line to `~/.claude/CLAUDE.md` (Operating Rules): on ambiguous/failed
  `/resume`, read newest `~/.claude/projects/<cwd-slug>/*.jsonl` transcripts before
  guessing from memory/git.
