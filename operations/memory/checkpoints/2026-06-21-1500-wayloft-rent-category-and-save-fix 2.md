---
date: 2026-06-21
time: 15:00
project: wayloft
status: in-progress
next-session: Batch 3 · Today (dashboard) — rebuild app/(app)/dashboard to match design/screens.html #today / #today-first, wiring the "because you watch United" lead from watched_programs + the wallet balances. Read ~/.claude/design.md before design work. Design source of truth: design/screens.html. Tracker: design/in-progress.md. BEFORE/AROUND that, two user loose ends still open in Setup data entry: (1) zero out the $3,000 still sitting in "Everything else" — it double-counts rent; (2) finish entering the rest of real data (balances, watched programs/routes, remaining spend). Dev server: pnpm dev in apps/web, port 3000, login annabelflip1@gmail.com / WL-8MOue7mx!7. NOTE the server stops if the process is interrupted (logged her out twice this session) — restart on demand.
supersedes: 2026-06-20-1950-wayloft-rebuild-batch2-setup-built.md
---

# Session: Wayloft — rent as first-class category + save-path bug fixed

## Done this session (all verified live against real Supabase + browser)

1. **Root-caused & fixed the Setup save failure.** `card_quiz_responses` had NO
   unique constraint on `user_id`, but both `updateCategorySpend` (Setup spend
   panel) and `submitQuiz` (recommend) upsert with `onConflict: "user_id"` →
   every save failed (Postgres 42P10). Silent in the spend panel (it swallows
   the action result), so last session's "Groceries saved" was never persisted —
   live table had 0 rows. **Migration 014** adds the unique constraint. Annabel
   pasted it; verified a real onBlur save lands a row (grocery 1300 persisted).

2. **Date picker → styled Month/Year control.** The card-opened field was a
   native `<input type="date">` (unstyleable browser calendar). New
   `components/ui/month-year-field.tsx` (two Radix Selects, emits `YYYY-MM-01`),
   swapped into `add-card-dialog.tsx`. Card-opened only needs month precision.
   Verified: 0 native date inputs, hidden `card_since` emits correct value.

3. **EARNS clarity.** `cards-panel.tsx` showed bare "5x · 3x · 1x". Rewrote to a
   grouped per-category breakdown ("5x Travel portal, Rotating categories / 3x
   Dining, Drugstores / 1x Everything else"). Verified rendered.

4. **Rent is now a first-class category** (Annabel: she Zelles $3k/mo rent, earns
   0 points today). End-to-end:
   - **Migration 015**: `monthly_rent_spend INTEGER DEFAULT 0` on
     card_quiz_responses. Pasted + verified column live.
   - **Engine** (`lib/recommend/engine.ts`): added `rent` to
     `SPENDING_CATEGORY_MAP` with `fallbackToOther: false`; `getBestRate` now
     respects it → rent earns ONLY an explicit `rent` rate (the Bilt family),
     **0 on every other card** (no "other" fallback). Catalog already had `rent`
     keys on bilt-blue/obsidian/palladium.
   - Wired through: `types.ts` QuizInput.spending, `setup-view.tsx` SetupSpend,
     `spend-panel.tsx` (Rent row + "Only earns points with a Bilt card" note),
     `setup.ts` SPEND_FIELDS, `onboarding/page.tsx` SPEND_COLUMNS,
     `next-card-widget.tsx`, `quiz-wizard.tsx`.
   - Tests: fixed 5 fixtures + added 2 new (no-fallback rule locked). 26/26 pass,
     type-check clean. Verified $3,000 rent saves and persists.

## Key product finding (saved to memory `project_wayloft_ranking_metric`)

Making rent dedicated revealed the next-card ranking is by **firstYearValue**
(signup-bonus heavy), which **buries no-fee ongoing earners**. For her real
profile, scored against the real catalog:
- Top 5 are broad earners (Cap One Venture #1, $2065/yr ongoing + $1387 signup),
  all correctly showing **rent $0/yr**.
- **Bilt Blue** ($0 AF) earns ~$1,882/yr ongoing incl. **$738/yr from rent** —
  but lands outside top-5 because it has ~no signup bonus.
Interpretation: rent feature is correct (no faked value); Bilt is a no-fee
"free money on rent" add, not a replace-everything card. The ranking metric is
the real issue.

## Queued for Batch 4 · Earn (in design/in-progress.md)

- **Persistent results view** — `/recommend` always opens the quiz wizard at
  step 1 and only computes on submit; rebuild so a complete profile shows recs
  immediately, quiz becomes an "edit inputs" path like Setup. (Annabel hit this:
  "do I have to retake the quiz to see them again?")
- **Ongoing-value / "best for rent" lens** so Bilt-type opportunities surface.

## Rebuild plan status (tracker: design/in-progress.md)

- [x] Batch 1 · App shell
- [x] Batch 2 · Setup — UI + save path now actually works; real-data entry still
      partial (rent done; balances/programs/routes/rest-of-spend pending)
- [ ] Batch 3 · Today (dashboard)  ← NEXT
- [ ] Batch 4 · Earn (+ the two queued items above)
- [ ] Batch 5 · Burn
- [ ] Batch 6 · strip cruft + polish + mobile

## Keep the brain (do not rebuild)

`lib/recommend/engine.ts` (scoreCards), `lib/optimizer/*`, `lib/flights/*`,
`lib/supabase/*`, `app/actions/*`, `data/` catalog.
Design source of truth: `design/screens.html`.

## Known UX debt noted this session

`spend-panel.tsx` save is fire-and-forget — a failed save shows the user nothing
(this is why the broken saves went unnoticed). Worth surfacing an inline error
like the rest of the app when Earn/Setup get more polish.
