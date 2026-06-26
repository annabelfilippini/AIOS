---
date: 2026-06-20
time: 14:10
project: wayloft
status: in-progress
next-session: Rebuild apps/web screens to match design/screens.html (Editorial Cream), verified logged-in against live Supabase. Build order: Batch 1 app shell (sidebar Today/Setup/Earn/Burn + mobile bottom tabs, replace old AppTopNav PLAN/POINTS/TRIPS), Batch 2 Setup (onboarding) + enter Annabel's real data through it, Batch 3 Today (dashboard), Batch 4 Earn (recommend — wallet coach + get-next-card), Batch 5 Burn (travel — deals feed + trip check), Batch 6 strip marketing scaffolding + polish + mobile. Route map: dashboard=Today, onboarding=Setup, recommend=Earn, travel=Burn. Keep the "brain" (lib/recommend/engine.ts, lib/optimizer, lib/flights, data/, supabase queries). NEW backend gap: no table for "Watching" (programs/routes) — needs a new migration when building Setup/Today (drives "because you watch United" lead + deals filter).
supersedes: 2026-06-18-2037-wayloft-amber-bronze-sweep-warn-token.md
---

# Session: Wayloft — Supabase stood up, rebuild kicked off

## What happened

Picked up the redesigned Wayloft (personal points optimizer, Editorial Cream).
Annabel approved the design system (design/screens.html, 4 batches done) and said
rebuild. Chose to **stand up Supabase first** so every rebuilt screen verifies
against live data rather than mock.

## Supabase standup (DONE + verified)

- Real project created by Annabel: ref `adsvto…` (`https://adsvto….supabase.co`).
- Keys fixed in `apps/web/.env.local`: anon (role=anon) + service_role
  (role=service_role) — first attempt had the anon key pasted into BOTH slots
  ("User not allowed" on admin API; caught by decoding the JWT `role` claim).
  Lesson: a 208-char eyJ… key is necessary but NOT sufficient — decode the role
  claim to confirm anon vs service_role.
- Schema: assembled `projects/wayloft/scripts/supabase-setup.sql` = migrations
  001–012 (packages/db/migrations) + transfer-bonus seed, run once in the SQL
  editor. 22 tables created, RLS on. transfer_bonuses seeded (10 rows).
- Account: created via admin API (email_confirm:true) —
  `annabelflip1@gmail.com` / `WL-8MOue7mx!7` (auto-gen, change in-app).
  Profile row auto-created by trigger (full_name "Annabel",
  onboarding_completed false).
- Verified: restarted dev server (preview `wayloft-web`, :3000) on real keys,
  logged in via the form, redirected into an authed route and rendered. Full
  stack works.

## Stack reality notes

- Duffel key is a **test** key (`duffel_t…`, 55 chars) — sandbox flight data,
  not live fares. Swap to `duffel_live_` when real availability is wanted.
- Anthropic + Seats.aero keys present.
- Schema still carries SaaS-era columns/tables (subscription_tier,
  stripe_customer_id, affiliate_clicks) — left untouched (code still refs some);
  prune as a cleanup pass AFTER the rebuild, not now.

## Framing fix (DONE)

`projects/wayloft/CLAUDE.md` rewritten from the stale "travel decision engine"
framing to the personal points optimizer scope (Setup/Today/Earn/Burn, Editorial
Cream lane, keep-brain/rebuild-face, Stack section with Duffel approved,
personal-use scrape guardrail). The old apps/web framing had misled a prior
session into rendering the marketing page as "the project."

## Next steps

1. Batch 1: app shell — new sidebar (Today/Setup/Earn/Burn) + mobile bottom
   tabs, replace AppTopNav, in `app/(app)/layout.tsx` + components/nav.
2. Batch 2: Setup (onboarding) rebuild + walk through it to enter real data.
3. Batches 3–5: Today, Earn, Burn against the data.
4. Batch 6: strip marketing/(marketing) + affiliate + card browser; polish; mobile.
5. Add the watched-programs/routes migration when Setup/Today need it.

## Context to preserve

- Design source of truth: `projects/wayloft/design/screens.html` (served via a
  python http.server on :8911 during review — kill when done).
- Full app structure map captured this session (routes, engine, data, flights,
  components). apps/web already mirrors the screens: dashboard/onboarding/
  recommend/travel/settings under route group `(app)`.
