---
date: 2026-05-11
time: 14:43
project: unknown
status: draft
next-session: ""
---

# Checkpoint: Wayloft Travel-First Reset

**Project:** `/Users/annabelfilippini/Documents/AI-OS/projects/wayloft`
**Purpose:** Handoff for resuming the travel-first reset.

## Core Decision

Do not rebuild Wayloft from scratch. Rebuild the product hierarchy.

Wayloft should move from **credit-card optimizer** to **travel decision engine**:

> Should I book this trip with cash, points, or perks/advisor benefits?

Credit cards remain valuable as supporting inputs (balances, transfer partners, transfer bonuses, “best card to pay cash”).

## User Motivation

Anchor example: Santa Clara flight was ~$400 cash vs ~15,000 points (~2.7 cpp). The product should surface that option automatically.

This is the core Wayloft magic:

> Cash: $400. Points: 15,000. Verdict: use points.

## Repo anchors (start here)

- `apps/web/app/(app)/travel/page.tsx` + `apps/web/components/travel/travel-client.tsx`
- `apps/web/lib/flights/compare.ts` (cash vs points logic)
- `apps/web/lib/flights/search.ts` (Duffel cash)
- `apps/web/lib/flights/seats-aero.ts` (award availability)

Core issue: product framing still reads “card optimizer” while `/travel` is the strongest emerging product.

## Plan

### Phase 1 (now): Recenter flights

- Make `/travel` the primary surface.
- For a route/date search, show: cash, best points, cpp, verdict, transfer path + bonus impact, “best card if paying cash”.

### Phase 2: Trip watch

- Save searches + alert on: unusually good points, cash drop, rebook-worthy changes.
- Data sources: Duffel + Seats.aero/commercial APIs only (no airline scraping).

### Phase 3+: Hotels + advisor layer

- After flights work, apply the same “cash vs points vs perks” decision engine to hotels.
- Longer-term: add “send to advisor” brief + perk valuation (Fora angle).

## Next Session Start

Start in:

```bash
cd /Users/annabelfilippini/Documents/AI-OS/projects/wayloft
```

Read first:

1. `CLAUDE.md`
2. `docs/TRAVEL-FIRST-RESET-AUDIT.md`
3. `apps/web/app/(app)/travel/page.tsx`
4. `apps/web/lib/flights/compare.ts`

Recommended next implementation move:

> Rework `/travel` into a first-class "Trip Decision" screen before touching
> hotels or marketing.

## Guardrail

Current Wayloft rules say not to scrape airline websites directly. Use
authorized APIs and aggregator/commercial sources unless Annabel deliberately
reopens that legal/product decision.
