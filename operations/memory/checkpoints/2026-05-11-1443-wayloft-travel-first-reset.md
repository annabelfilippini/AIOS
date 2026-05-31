# Checkpoint: Wayloft Travel-First Reset

**Date:** 2026-05-11
**Project:** `/Users/annabelfilippini/Documents/AI-OS/projects/wayloft`
**Purpose:** Handoff for starting a new session on the Wayloft product reset.

## Core Decision

Do not rebuild Wayloft from scratch. Rebuild the product hierarchy.

Wayloft should move from **credit-card optimizer** to **travel decision engine**:

> Should I book this trip with cash, points, or perks/advisor benefits?

Credit cards remain valuable, but as supporting infrastructure:

- what points the user has
- where those points transfer
- which card earns or replenishes the right points
- whether a transfer bonus changes the trip math
- which card to use if cash is the better booking path

## User Motivation

Annabel had a recent Santa Clara trip where flights were about `$400` cash or
`15,000` points. That is roughly `2.7 cpp`, an excellent redemption, but she did
not know that option was available at the time.

This is the core Wayloft magic:

> Cash: $400. Points: 15,000. Verdict: use points.

## Repo Reality

The repo already has important travel foundations:

- Duffel cash flight search: `apps/web/lib/flights/search.ts`
- Seats.aero award search: `apps/web/lib/flights/seats-aero.ts`
- Cash-vs-points comparison: `apps/web/lib/flights/compare.ts`
- Travel page/client: `apps/web/app/(app)/travel/page.tsx`,
  `apps/web/components/travel/travel-client.tsx`
- Transfer bonuses: `apps/web/lib/bonuses/scraper.ts`,
  `transfer_bonuses`, `transfer_bonus_history`
- User points: `loyalty_balances`
- Credit card wallet/catalog: `user_cards`, `data/credit-cards.json`
- Transfer partner catalog: `data/transfer-partners.json`
- Booked-trip/check-in foundation: `user_flights`, `upcoming_flights`,
  `scripts/checkin-alert.py`

The issue is positioning: the current app shell and dashboard still frame
Wayloft as a card/portfolio optimizer, while the strongest product is the
travel decision layer already emerging in `/travel`.

## Plan

### Phase 1: Recenter Flights

Make `/travel` the primary Wayloft experience.

Build around:

- cash price
- best points price
- cents-per-point value
- verdict: use cash, use points, or close call
- transfer path from user's actual balances
- relevant transfer-bonus impact
- best card to use if paying cash

### Phase 2: Add Trip Watch

Let users save a route/date search and monitor it.

Use authorized data sources only:

- Duffel for cash fare context
- Seats.aero/commercial or partner API for award availability
- no direct airline website scraping under current project rules

Alerts should fire when:

- points become unusually good
- cash drops enough that cash beats points
- booked award prices drop enough to rebook

### Phase 3: Hotels

Add a hotel decision engine after flights prove the pattern.

Question:

> Should I book this hotel with cash, hotel points, credit-card portal points, or advisor perks?

Hotel model should account for:

- cash price
- hotel award price
- cpp value
- taxes/resort fees
- elite benefits
- breakfast, credits, upgrades, late checkout
- cancellation policy
- portal option
- advisor option

### Phase 4: Fora / Travel Advisor Layer

Annabel's dad became a travel advisor through Fora. This can become a real
Wayloft differentiator.

Potential features:

- compare points booking vs cash booking vs advisor booking
- estimate advisor perk value
- flag hotels where advisor perks likely beat points
- generate a "send to advisor" trip brief
- eventually support referral/lead flow for high-value hotel cash bookings

Example decision:

> Park Hyatt cash: $700/night. Hyatt points: 35,000/night = 2.0 cpp.
> Advisor cash booking: $700/night + breakfast + $100 credit + possible upgrade.
> Verdict depends on whether cash preservation or perks matter more.

### Phase 5: Travel-First Shell

Only after the product center is clear:

- make Travel the default signed-in landing surface
- move dashboard toward next trip, current opportunities, urgent actions
- demote cards into supporting context
- rework homepage around "cash vs points vs perks" trip examples

Suggested nav:

1. Travel
2. Trips
3. Points
4. Cards
5. Reviews
6. Settings

## Current Docs Created/Updated

- `docs/TRAVEL-FIRST-RESET-AUDIT.md`
- `docs/AWARD-INTEL-PIPELINE-PLAN.md`
- `docs/FLIGHT-TRACKER-PLAN.md`
- `scripts/award-intel-probe.mjs`

Note: repo had unrelated dirty files before this work. Do not assume every dirty
file belongs to this reset.

## Next Session Start

Start in:

```bash
cd /Users/annabelfilippini/Documents/AI-OS/projects/wayloft
```

Read first:

1. `CLAUDE.md`
2. `docs/TRAVEL-FIRST-RESET-AUDIT.md`
3. `docs/AWARD-INTEL-PIPELINE-PLAN.md`
4. `apps/web/app/(app)/travel/page.tsx`
5. `apps/web/components/travel/travel-client.tsx`
6. `apps/web/lib/flights/compare.ts`

Recommended next implementation move:

> Rework `/travel` into a first-class "Trip Decision" screen before touching
> hotels or marketing.

## Guardrail

Current Wayloft rules say not to scrape airline websites directly. Use
authorized APIs and aggregator/commercial sources unless Annabel deliberately
reopens that legal/product decision.
