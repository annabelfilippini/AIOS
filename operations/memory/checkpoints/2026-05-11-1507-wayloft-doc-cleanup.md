---
date: 2026-05-11
time: 15:07
project: unknown
status: draft
next-session: ""
---

# Checkpoint: Wayloft Doc Cleanup And Travel-First Reset

**Project:** `/Users/annabelfilippini/Documents/AI-OS/projects/wayloft`
**Purpose:** Fresh-terminal handoff after organizing Wayloft docs and reducing
default context load.

## Start Here

```bash
cd /Users/annabelfilippini/Documents/AI-OS/projects/wayloft
```

Read in this order:

1. `CLAUDE.md`
2. `docs/README.md`
3. For current product work: `docs/TRAVEL-FIRST-RESET-AUDIT.md`

Only read `Research/README.md` when a task needs legal, data-source, affiliate,
trademark, design-research, or card-rule context.

## What Changed

The Wayloft docs were reorganized so new sessions do not bulk-load old plans.

Active routing/docs:

- `CLAUDE.md` now frames Wayloft as a travel decision engine and points agents
  to `docs/README.md`.
- `docs/README.md` is the project doc map.
- `Research/README.md` marks research as pull-only.
- `docs/FLIGHT-TRACKER-PLAN.md` was trimmed from a long implementation/risk
  dump to a scoped active plan.
- `DESIGN.md` remains active because it is compact and useful for UI work.

Archived older plans/hand-offs into `docs/archive/2026-05-doc-cleanup/` so the default read-path stays small.

## Current Product Direction

The current Wayloft center is still the travel-first reset:

> Should I book this trip with cash, points, or a better travel path?

Credit cards, transfer partners, balances, bonuses, and reviews are supporting
infrastructure, not the primary product frame.

Primary active docs:

- `docs/TRAVEL-FIRST-RESET-AUDIT.md`
- `docs/AWARD-INTEL-PIPELINE-PLAN.md`
- `docs/FLIGHT-TRACKER-PLAN.md`

## Guardrails

Do not scrape airline websites directly. Do not automate airline login sessions,
check-in flows, seat maps, CAPTCHA handling, bot-detection workarounds, or
direct airline award searches unless Annabel deliberately reopens that legal and
product decision.

Allowed travel data sources for current work:

- Duffel for cash fare context.
- Seats.aero partner/commercial API for award availability.
- Manual user-entered/current price data.
- Public aggregator/editorial sources with attribution where appropriate.

## Worktree Note

The worktree was already dirty before this doc cleanup. Do not assume every
dirty file belongs to this pass.

Known in-flight work includes travel UI tweaks + doc edits; repo also had pre-existing unrelated dirty files before this pass.

## Verification

After doc cleanup: default read path is `CLAUDE.md` + `docs/README.md`, then one task-specific doc. (Prior travel UI pass had type-check + targeted lint passing.)

## Recommended Next Move

In the new terminal, continue product work from:

`docs/TRAVEL-FIRST-RESET-AUDIT.md`

Recommended next implementation move remains:

> Rework `/travel` into a first-class Trip Decision screen before touching
> hotels, marketing, or deeper alert infrastructure.
