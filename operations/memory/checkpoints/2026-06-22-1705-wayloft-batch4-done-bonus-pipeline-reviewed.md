---
date: 2026-06-22
time: 17:05
project: wayloft
status: in-progress
next-session: Two open threads. (A) DECIDE the transfer-bonus data source before
  investing more: the current pipeline is a brittle blog SCRAPER
  (lib/bonuses/scraper.ts, plain fetch of Frequent Miler + Doctor of Credit HTML
  with hand-written parsers) driven by a Vercel cron (vercel.json ->
  /api/cron/scrape-bonuses, CRON_SECRET auth). It has NEVER run successfully here
  (live table was 100% expired -> I hand-seeded). Likely causes: not deployed to
  Vercel (local dev only), CRON_SECRET unset, or FM/DoC pages 429 / HTML drifted.
  Options to weigh: harden+debug the scraper vs swap to a more durable bonus
  source. The seeded bonuses are temporary (bilt/Hyatt 100% ends 2026-06-29;
  chase/UR->United 30% ends 2026-07-13) - after that the Today lead goes quiet
  again. (B) Build Batch 5 · Burn (travel) to match design/screens.html #burn
  (deals feed + live trip check). Dev server FLAKY: preview_start name
  "wayloft-web" (pnpm dev, apps/web, port 3000), login annabelflip1@gmail.com /
  WL-8MOue7mx!7; the preview browser drifts to localhost:8849 (fym-tarifa) - fix
  by navigating with ABSOLUTE url window.location.assign('http://localhost:3000/..').
supersedes: 2026-06-22-1645-wayloft-batch4-earn-built.md
---

# Session: Wayloft — Batch 4 Earn shipped, bonus pipeline reviewed

## Done this session (all verified live)

1. **Bonus data refreshed** (Batch 3 blocker). 10 stale rows deactivated, 6
   current June-2026 bonuses seeded incl. chase/UR->United 30% (ends Jul 13) via
   `data/transfer-bonus-seed.sql` + JS admin client. Today lead fires:
   "Because you watch United / Move Chase points to United at 30% extra".

2. **Batch 4 · Earn built.** `/recommend` is now a server-computed persistent
   results view; quiz moved to `/recommend/edit` (redirects back on save). Three
   panels (Wallet coach / Best for ongoing value / Get your next card). New lens
   `bestByOngoingValue` (ranks by existing `year2Value`) surfaces **Bilt Obsidian
   - $738/yr on rent, $1,160/yr ongoing, $95 AF**, which the first-year ranking
   buries. Real "because you watch United" reason chip from transfer-partners data.
   New: `lib/earn/{derive,reason}.ts`, `components/earn/*`. Tests +14 (210/210),
   tsc clean. Resolves memory `project_wayloft_ranking_metric` (marked RESOLVED).

3. **Removed dead `components/recommend/results.tsx`** (wizard now redirects to
   `/recommend` instead of rendering it; confirmed no importers; `git rm`).

## Bonus-data architecture (clarified this session)

"United points info" is three separate layers - don't conflate them:
- **Transfer bonuses** (drives the Today lead) = a **SCRAPER**, not a CLI.
  `lib/bonuses/scraper.ts` `safeFetch()` is plain server `fetch()` (no Firecrawl,
  no auth) over Frequent Miler + Doctor of Credit (per-bank + tag pages), each
  with a bespoke HTML `parse()`. United is never scraped on its own - it appears
  only as a partner row inside Chase UR / Amex MR bonus lists. Run by Vercel cron.
- **Award seat availability** (United routes "watching for award space") =
  **seats.aero Partner API** (`lib/flights/seats-aero.ts`, SEATS_AERO_API_KEY,
  Partner-Authorization header). An API, not a scrape/CLI. Not wired into the
  Today routes panel yet.
- **Cash flight prices** = Duffel API. **United miles balance** = manual entry in
  Setup. The reddit-cli/skool-curl cookie-CLI pattern is NOT used by the bonus
  pipeline (it was the planned approach for seats.aero session-scraping).

## Rebuild plan status (tracker: design/in-progress.md)

- [x] Batch 1 App shell · [x] Batch 2 Setup · [x] Batch 3 Today + bonus refresh
- [x] Batch 4 · Earn (persistent results + ongoing-value lens)  ← done
- [ ] Batch 5 · Burn (travel)  ← NEXT (or resolve bonus-source decision first)
- [ ] Batch 6 · strip cruft + polish + mobile

## Keep the brain (do not rebuild)

`lib/recommend/engine.ts`, `lib/optimizer/*`, `lib/flights/*`, `lib/supabase/*`,
`app/actions/*`, `data/` catalog. Design source of truth: `design/screens.html`.
