---
date: 2026-06-22
time: 16:45
project: wayloft
status: in-progress
next-session: Batch 5 · Burn (travel) — rebuild the travel/deals surface to match
  design/screens.html #burn (deals feed + live trip check). The "brain" stays
  (lib/flights/*, Duffel wrapper, seats.aero). Design source of truth:
  design/screens.html; tracker design/in-progress.md. ALSO outstanding from this
  session: (a) delete now-dead components/recommend/results.tsx (wizard redirects
  to /recommend instead of rendering it); (b) the seeded transfer_bonuses are
  representative June-2026 data, not live — re-seed or wire the scrape-bonuses
  cron before relying on them long-term (bilt/Hyatt 100% bonus ends 2026-06-29,
  chase/UR->United 30% ends 2026-07-13). Dev server is FLAKY: preview_start name
  "wayloft-web" (pnpm dev, apps/web, port 3000), login annabelflip1@gmail.com /
  WL-8MOue7mx!7. The preview BROWSER kept drifting to localhost:8849 (the
  fym-tarifa static server) and to relative-path 404s — fix by navigating with an
  ABSOLUTE url: preview_eval window.location.assign('http://localhost:3000/...').
  Confirm Next is alive with `curl -s localhost:3000/recommend` (307->login = up).
supersedes: 2026-06-21-1515-wayloft-today-dashboard-built.md
---

# Session: Wayloft — bonus data refreshed + Batch 4 Earn built

## Done this session (verified live against real Supabase + browser)

1. **Refreshed `transfer_bonuses` (the Batch 3 blocker).** Every row was expired
   (seed dates Feb/Mar 2026), so the Today lead resolved to "Nothing to move."
   Rewrote `data/transfer-bonus-seed.sql` to current June-2026 bonuses and applied
   via the JS admin client (service role, Annabel authorized): 10 stale rows
   deactivated, 6 current seeded incl. **chase/UR -> United 30% (ends Jul 13)**.
   Verified live: Today lead now fires "Because you watch United / Move Chase
   points to United at 30% extra · Ends Jul 13 · 21 days left"; Watching panel
   United row = "Transfer bonus live · 30%". 0 console errors.

2. **Batch 4 · Earn rebuilt.** `/recommend` is now a **server-computed persistent
   results view** (was a quiz wizard that only computed on submit). The quiz moved
   to `/recommend/edit` ("Edit inputs" link) and redirects to `/recommend` on save.
   Three panels match `design/screens.html` #earn:
   - **Wallet coach** — per spent category, best held card + rate, "No card earns
     extra here yet" on gaps. Her data: Rent/Groceries/Travel = Freedom Flex 1x
     (gap); Dining = Freedom Flex 3x.
   - **Best for ongoing value** (NEW lens) — surfaces the buried no-fee/ongoing
     earner. Live result: **Bilt Obsidian, "earns on your rent" chip, $738/yr on
     rent, $1,160/yr ongoing, $95 AF.**
   - **Get your next card** — first-year top-3 with reason chips. Real "because
     you watch United" chip derived from transfer-partners data (UR -> UA).
   - Engine (additive, low-risk): `scoreAllCandidates` (unsliced ranked) +
     `bestByOngoingValue` (ranks by existing `year2Value`; suppressed when it ==
     the #1 first-year pick). `scoreCards` unchanged so the 196 prior tests stay
     green. New libs `lib/earn/{derive,reason}.ts`; new components
     `components/earn/{wallet-coach,ongoing-callout,next-card}.tsx`. Quiz wizard
     trimmed (dropped client-side scoreCards/inline Results; redirects instead).
   - Tests: `tests/recommend/ongoing-value.test.ts` (6) + `tests/earn/derive.test.ts`
     (8). Full suite **210/210**, tsc clean. Resolves memory
     `project_wayloft_ranking_metric` (now marked RESOLVED).

## Gotchas for next time

- **Preview browser origin drift.** The shared Chrome kept sitting on
  localhost:8849 (fym-tarifa static server) producing Python "Error response 404"
  pages; relative fetch/nav inside preview_eval hit that wrong origin. Playwright
  MCP shares the same Chrome ("Browser already in use"). Fix: navigate with an
  absolute URL via `window.location.assign('http://localhost:3000/...')`, then
  snapshot. Next itself stayed alive the whole time (curl confirmed 307->login).

## Rebuild plan status (tracker: design/in-progress.md)

- [x] Batch 1 · App shell
- [x] Batch 2 · Setup
- [x] Batch 3 · Today (dashboard) + bonus data refresh
- [x] Batch 4 · Earn (recommend) — persistent results + ongoing-value lens  ← done
- [ ] Batch 5 · Burn (travel)  ← NEXT
- [ ] Batch 6 · strip cruft + polish + mobile

## Keep the brain (do not rebuild)

`lib/recommend/engine.ts`, `lib/optimizer/*`, `lib/flights/*`, `lib/supabase/*`,
`app/actions/*`, `data/` catalog. Design source of truth: `design/screens.html`.
