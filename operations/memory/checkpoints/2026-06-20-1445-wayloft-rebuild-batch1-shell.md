---
date: 2026-06-20
time: 14:45
project: wayloft
status: in-progress
next-session: Batch 2 — rebuild onboarding into the design's Setup screen (your cards / points balances / spend by category / what you're watching) in apps/web, matching design/screens.html (#setup, #setup-first). This batch ALSO needs a NEW migration for watched programs/routes (no table exists yet — it drives the "because you watch United" Today lead + the Burn deals filter). Generate the migration SQL → Annabel runs it in the Supabase SQL editor (per database.md: never run migrations directly). After Setup is built, walk through it in the browser logged in (annabelflip1@gmail.com / WL-8MOue7mx!7) to enter Annabel's REAL data: Chase Freedom Flex, points balances, monthly spend by category, watched programs (United + Star Alliance partners, Hyatt, Marriott) + routes. That real data then feeds Today/Earn/Burn (Batches 3–5). Dev server: preview `wayloft-web` (:3000). Design served on :8911 (python http.server in design/ — kill when done).
supersedes: 2026-06-20-1410-wayloft-supabase-stood-up-rebuild-start.md
---

# Session: Wayloft rebuild — Supabase live + Batch 1 (app shell) shipped

## Done this session

1. **Reframed the project.** `projects/wayloft/CLAUDE.md` rewritten from the stale
   "travel decision engine" framing to the personal points optimizer scope
   (Setup/Today/Earn/Burn, Editorial Cream, keep-brain/rebuild-face, Stack section,
   personal-use scrape guardrail). The stale framing had previously misled a session
   into treating the marketing landing page as "the project."

2. **Stood up Supabase (live + verified).**
   - Project ref `adsvto…` (`https://adsvto….supabase.co`).
   - Keys in `apps/web/.env.local`: anon (role=anon) + service_role (role=service_role).
     GOTCHA caught: first attempt had the anon key pasted into BOTH slots ("User not
     allowed" on admin API). A 208-char eyJ… key is necessary but NOT sufficient —
     decode the JWT `role` claim to confirm anon vs service_role.
   - Schema: `projects/wayloft/scripts/supabase-setup.sql` = migrations 001–012
     (packages/db/migrations) + transfer-bonus seed, run once in SQL editor.
     22 tables, RLS on, transfer_bonuses seeded (10 rows).
   - Account: admin-created, email_confirm:true —
     `annabelflip1@gmail.com` / `WL-8MOue7mx!7` (auto-gen, change in-app).
     Profile auto-created by trigger.
   - Verified: dev server restarted on real keys, logged in via form, authed route
     rendered. Full stack works.

3. **Batch 1 · App shell (shipped + verified logged-in, desktop + mobile, 0 console errors).**
   - `components/nav/app-nav-links.ts` (new) — shared nav model. Route map:
     Today=/dashboard, Setup=/onboarding, Earn=/recommend, Burn=/travel.
   - `components/nav/app-sidebar.tsx` (rebuilt) — Cormorant WAYLOFT wordmark, nav with
     diamond markers (◇/◆), active = ink block (bg-foreground), bronze-avatar user
     block at bottom → dropdown (Settings / dark-mode toggle / sign out). Matches the
     design `.side` spec exactly (236px col, bg-secondary, border #DDD5C2).
   - `components/nav/app-bottom-nav.tsx` (new) — mobile bottom tabs Today/Earn/Burn
     (Setup omitted; reached from Today).
   - `app/(app)/layout.tsx` — md:grid 236px/1fr with sidebar + main; bottom nav.
     Replaced AppTopNav (now unused).

## Stack reality (keep)

- Duffel key is a **test** key (`duffel_t…`) — sandbox flight data, not live fares.
  Swap to `duffel_live_` for real availability.
- Schema still carries SaaS-era cruft (subscription_tier, stripe_customer_id,
  affiliate_clicks). Left untouched (code refs some). Prune AFTER rebuild.

## Rebuild plan (tracker: design/in-progress.md)

- [x] Batch 1 · App shell
- [ ] Batch 2 · Setup (onboarding) + watched-programs/routes migration + enter real data
- [ ] Batch 3 · Today (dashboard)
- [ ] Batch 4 · Earn (recommend — wallet coach + get-next-card)
- [ ] Batch 5 · Burn (travel — deals feed + trip check)
- [ ] Batch 6 · strip (marketing)/affiliate/card-browser + polish + mobile

## Keep the brain (do not rebuild)

`lib/recommend/engine.ts` (scoreCards), `lib/optimizer/*` (wallet coach),
`lib/flights/*` (Duffel + Seats.aero + compare), `lib/supabase/*`, `app/actions/*`,
`data/` catalog. Design source of truth: `design/screens.html`.
