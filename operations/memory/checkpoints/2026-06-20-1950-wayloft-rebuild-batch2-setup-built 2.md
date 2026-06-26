---
date: 2026-06-20
time: 19:50
project: wayloft
status: in-progress
next-session: Batch 2 has ONE thing left — enter Annabel's REAL data through the live Setup UI (localhost:3000/onboarding, dev server preview `wayloft-web`, logged in annabelflip1@gmail.com / WL-8MOue7mx!7): Chase Freedom Flex (add card), points balances, monthly spend by category, watched programs (United + Star Alliance partners, Hyatt, Marriott) + routes (NY→Lisbon, NY→London). Offered two paths last session — (1) Annabel enters it herself as a real UX test, or (2) Claude drives the browser to populate it then Annabel corrects. NOT YET DECIDED. After real data is in, move to Batch 3 · Today (dashboard) — rebuild app/(app)/dashboard to match design/screens.html #today / #today-first, wiring the "because you watch United" lead from watched_programs + the wallet balances. Read ~/.claude/design.md before design work. Design source of truth: design/screens.html. Tracker: design/in-progress.md.
supersedes: 2026-06-20-1445-wayloft-rebuild-batch1-shell.md
---

# Session: Wayloft rebuild — Batch 2 (Setup screen) built + verified

## Done this session

1. **Migration 013 (watched programs + routes) written + run.**
   - `packages/db/migrations/013_watched_programs_routes.sql` — two new tables:
     - `watched_programs` (program_code/program_name/program_type airline|hotel|alliance,
       include_partners bool) — drives Today "because you watch United" lead + Burn filter.
     - `watched_routes` (origin/destination IATA metro codes, label).
     - Both: UUID PK, RLS user-owns-data, `set_updated_at` trigger, unique index.
     - **Hard delete on purpose** (no deleted_at) — these are toggleable preference
       chips, not financial/lifecycle data, so they fall outside the soft-delete rule.
   - Annabel ran it in the Supabase SQL editor. Verified live (see below).

2. **Spend needed NO new migration.** `card_quiz_responses` already has all
   `monthly_*_spend` columns and is upsertable on user_id (onboarding already
   upserts travel_goal there). Setup's Spend panel writes straight into it.

3. **Setup screen rebuilt** (replaces the old 3-step experience→cards→goals wizard).
   It is now a persistent "edit anytime" page, NOT a one-time wizard — removed the
   `onboarding_completed` redirect-away. Route stays Setup = `/onboarding`.
   - `app/(app)/onboarding/page.tsx` (rewritten) — server-loads cards, balances,
     spend, watched_programs, watched_routes in parallel (named columns, no SELECT *).
   - `components/setup/setup-view.tsx` — shared types + composes 4 panels.
   - `components/setup/cards-panel.tsx` — mini espresso card art + Opened/AF/Earns
     meta; reuses `AddCardDialog` (controlled) + `removeCard`.
   - `components/setup/balances-panel.tsx` — on-blur `updateLoyaltyBalance`, "updated/
     not set yet" stamps, ×-remove; reuses `AddBalanceDialog` for adding.
   - `components/setup/spend-panel.tsx` — 5 categories, on-blur upsert.
   - `components/setup/watching-panel.tsx` — Programs (curated picker incl. alliance
     "partners" options) + Routes (origin/dest inputs) as add/remove chips.
   - New actions: `app/actions/watching.ts` (add/remove program + route),
     `app/actions/setup.ts` (`updateCategorySpend`). Both match the repo's
     `{success,error{category,message,isRetryable}}` action shape.

4. **Verified logged-in (desktop), 0 console errors.**
   - Page renders all 4 panels; desktop sidebar + Editorial Cream styling correct.
   - Added "United" watched program → chip persists across a full reload
     (confirms table 013 is live + watching.ts works end-to-end).
   - Set Groceries = 600 → persists to card_quiz_responses (confirms setup.ts).

## Stack reality (unchanged, keep)

- Duffel key is TEST (`duffel_t…`) — sandbox data, swap to `duffel_live_` for real.
- Schema still carries SaaS-era cruft (subscription_tier, stripe_customer_id,
  affiliate_clicks) — left untouched, prune AFTER rebuild.

## Rebuild plan (tracker: design/in-progress.md)

- [x] Batch 1 · App shell
- [~] Batch 2 · Setup — UI built + verified; **real-data entry still pending**
- [ ] Batch 3 · Today (dashboard)
- [ ] Batch 4 · Earn (recommend — wallet coach + get-next-card)
- [ ] Batch 5 · Burn (travel — deals feed + trip check)
- [ ] Batch 6 · strip (marketing)/affiliate/card-browser + polish + mobile

## Keep the brain (do not rebuild)

`lib/recommend/engine.ts` (scoreCards), `lib/optimizer/*`, `lib/flights/*`,
`lib/supabase/*`, `app/actions/*` (existing), `data/` catalog.
Design source of truth: `design/screens.html`.
