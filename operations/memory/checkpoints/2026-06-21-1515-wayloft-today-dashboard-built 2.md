---
date: 2026-06-21
time: 15:15
project: wayloft
status: in-progress
next-session: Batch 4 · Earn — rebuild /recommend (app/(app)/recommend or wherever the quiz wizard lives) to match design/screens.html #earn. Two locked requirements (design/in-progress.md): (1) PERSISTENT RESULTS — a complete profile shows recs immediately (server-computed), quiz becomes an "edit inputs" path like Setup; today /recommend always opens the wizard at step 1 and only computes on submit. (2) ONGOING-VALUE / "best for rent" lens so no-fee earners like Bilt Blue (~$738/yr on her rent) surface despite the firstYearValue ranking burying them. See memory project_wayloft_ranking_metric. ALSO outstanding: transfer_bonuses table is all expired (seed dates Feb/Mar 2026) so the Today lead shows "Nothing to move today" — re-seed or run scrape-bonuses cron to make the "because you watch United" lead fire. Dev server: preview_start name "wayloft-web" (pnpm dev, apps/web, port 3000), login annabelflip1@gmail.com / WL-8MOue7mx!7. Preview server drops on navigation via window.location.href — restart with preview_start; reload via location.reload() not href.
supersedes: 2026-06-21-1500-wayloft-rent-category-and-save-fix.md
---

# Session: Wayloft — Batch 3 Today dashboard built + rent double-count fixed

## Done this session (verified live against real Supabase + browser)

1. **Batch 3 · Today dashboard rebuilt.** Replaced the old SaaS "Points Command
   Center" (`app/(app)/dashboard/page.tsx`) with the Today design from
   `design/screens.html` (#today): time-aware greeting + date, a derived **lead
   card**, and two panels **Watching | Wallet**.
   - **New `lib/today/lead.ts`** — `deriveLead(bonuses, watchedPrograms,
     userCurrencies)` matches active `transfer_bonuses` to programs she watches
     AND can transfer to (holds the source currency), preferring actionable >
     higher % > sooner end. Produces "Because you watch United" eyebrow +
     "Move Chase points to United at 30% extra" headline + countdown + CTA→/travel.
     `liveBonusForProgram` drives per-program "Transfer bonus live · X%" status.
     Three lead states: first-run setup gate, live lead, calm "Nothing to move".
   - **New `lib/today/best-use.ts`** — `deriveBestUse(walletGuide, spend)` →
     wallet footer "best card to use now" from `generateWalletGuide` (the
     optimizer brain) + real spend; only fires when a spent category beats 1x.
   - **New components** `components/today/{lead-card,watching-panel,wallet-panel}.tsx`.
   - Routes panel shows watched routes as "Watching for award space" — no faked
     seat data (no award-availability source wired yet).
   - **Tests** `tests/today/{lead,best-use}.test.ts` (11). One caught a real bug:
     eyebrow said "United" but headline said "United Airlines" (bonus partner
     string vs program name) — fixed to use the watched program's short name
     everywhere. Full suite **196/196**, tsc clean.
   - Verified logged-in desktop: real United/Delta programs, Chase UR 13,000
     balance, footer "Chase Freedom Flex, 3x on Dining", 0 console errors.
     Layout matches design (sidebar/Today active, full-width lead, 2-col panels).

2. **Fixed the $3,000 rent double-count** (loose end from prior checkpoint).
   "Everything else" (`monthly_other_spend`) held $3,000 — same as rent, double
   counting it. Zeroed via the live Setup UI save path (the one fixed last
   session). Verified persisted across reload; rent still $3,000, other now 0.
   Her real spend now: Groceries 1,300 / Dining 100 / Gas 0 / Travel 250 /
   Rent 3,000 / Everything else 0.
   - **Gotcha for next time:** the spend inputs save on React `onBlur`, which
     listens for bubbling `focusout` — dispatching a plain `blur` event does NOT
     trigger the save. Use `new FocusEvent('focusout',{bubbles:true})` after the
     native value setter + `input` event.

## Key open finding

`transfer_bonuses` is entirely **expired** (seed dates 2026-02/03), so the Today
lead correctly resolves to "Nothing to move today" and all watched programs show
"No change". The lead/status code is correct and tested — it just has no live
data. Refresh the table (re-seed current bonuses or run the `scrape-bonuses`
cron) to light up the "because you watch United" lead.

## Rebuild plan status (tracker: design/in-progress.md)

- [x] Batch 1 · App shell
- [x] Batch 2 · Setup (real-data entry: rent done, other zeroed; balances/
      routes/rest-of-spend still partial — only Chase UR balance + United/Delta
      programs entered so far)
- [x] Batch 3 · Today (dashboard)  ← done this session
- [ ] Batch 4 · Earn (recommend) — persistent results + ongoing-value lens  ← NEXT
- [ ] Batch 5 · Burn (travel)
- [ ] Batch 6 · strip cruft + polish + mobile

## Still-open data entry (needs Annabel's real numbers)

Balances beyond Chase UR, watched routes (none entered — routes panel is empty),
and any remaining cards. Earn/Today get richer once these land.

## Keep the brain (do not rebuild)

`lib/recommend/engine.ts`, `lib/optimizer/*`, `lib/flights/*`, `lib/supabase/*`,
`app/actions/*`, `data/` catalog. Design source of truth: `design/screens.html`.
