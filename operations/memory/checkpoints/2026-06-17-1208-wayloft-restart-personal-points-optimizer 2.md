---
date: 2026-06-17
time: 12:08
project: wayloft
status: in-progress
next-session: Build the Wayloft design comparison page (Editorial Cream vs Premium Dark, two directions across real screens, the 3 reference images embedded inline, JETRADE inspected live first, copy on the Desktop). Pending only a quick green-light on the earn+burn personal scope and on using the Duffel API key.
---

# Session: Wayloft restart scoped as a personal points optimizer

## What we worked on

Reconstructed where Wayloft left off and re-scoped it for a fresh restart.
This was a planning session, no code or files changed yet. Annabel paused
before giving the final green-light to start building.

Existing state of the project:
- Real Next.js monorepo at `projects/wayloft` (Supabase + Vercel, pnpm/turbo).
  Last code commit June 4.
- Today it is a working **credit-card optimizer** with a **travel layer
  half-built on top**, gated behind `NEXT_PUBLIC_ENABLE_TRAVEL`.
- Product framing churned three times: card optimizer -> travel decision engine
  (cash vs points) -> beginner travel mode. That churn is why a restart is on
  the table.
- Separate static design taste-test (not wired to the app):
  `projects/websites/wayloft-timeline/index.html`.

## Decisions made

**1. Make it a personal app (just Annabel).** This kills the SaaS overhead:
no affiliate model, no subscriptions, no marketing funnel, no Seller of Travel
registration, no multi-user concerns.

**2. New north star: "optimize my whole points life, just for me."** Two halves:
- **Earn** — which card to USE per category (groceries, gas, shopping, dining)
  + which card to GET next.
- **Burn** — when and where to use or transfer points, via a live deals feed +
  on-demand trip checks.
- Scope now spans everyday spend, not just travel. Personal but complete.

**3. Re-center, do not rebuild from scratch.** Keep the "brain", rebuild the
"face".
- Keep: card catalog data (`data/credit-cards.json`, `transfer-partners.json`,
  `issuer-rules.json`), the recommendation engine (`lib/recommend/engine.ts`),
  the Duffel + Seats.aero wrappers (`lib/flights/search.ts`,
  `lib/flights/seats-aero.ts`, `lib/flights/compare.ts`), transfer-bonus
  tracking, Supabase as a single user.
- Cut: marketing site, affiliate tracking, subscriptions, the card browser,
  reviews, and the amber "Signal" theme.
- Rebuild: app shell, design system, and the screens.
- Earn side likely reuses existing `/optimizer` and `/recommend` routes rather
  than building from zero (verify on resume).

**4. v1 scope (nothing deferred to v2 — Annabel pushed back on an earlier
v1/v2 split that punted live award data).**
- **Setup** — cards held (Chase Freedom now), points balances, spend by
  category, watched programs/routes (United + partners, hotel chains).
- **Earn** — wallet coach ("use Freedom Flex for groceries this quarter, card X
  for gas") + what card to get next.
- **Burn** — scraped deals feed + live trip check (cash vs points vs transfer
  for a real route/date).

**5. Data layer — lean on CLI scraping because it is personal.**
- **Seats.aero: scrape via Annabel's login** (the reddit-cli session-cookie
  pattern, hitting their JSON endpoints). It is an aggregator, so this honors
  the spirit of "don't hit airlines directly." Risks: against their ToS (worst
  case account ban, not legal), and scrapers break. Acceptable at personal low
  volume with hard caching.
- **Duffel is NOT a scrape target — it is an API.** No consumer site to curl.
  Use Annabel's Duffel key (test mode free, live cheap at her volume); wrapper
  already exists. Recommendation: use the key. (This was a correction to her
  assumption that Duffel could be curled like Seats.aero.)
- **Deals feed** = Reddit via `reddit-cli` (r/awardtravel, r/churning; cookie
  expires every few weeks, needs re-import) + Firecrawl for transfer-bonus
  trackers, Doctor of Credit, Frequent Miler (DoC scraping already allowed in
  the project's data rules).
- No new paid infrastructure needed for the earn side or the feed.

**6. Guardrail update.** Annabel deliberately reopened the project's no-scrape
rule for personal use. New rule: scrape aggregators (Seats.aero) and
blogs/Reddit via her own sessions, low volume, cache hard, still do not hit
airline.com directly.

**7. Build order (nothing cut, just sequenced).** Build the reliable earn side
+ scraped feed first (works fast, uses tools she already has), then wire the
authenticated Seats.aero + Duffel trip check (most fragile, depends on her
logins).

**8. Design direction.** Annabel gave three reference images and asked for a
comparison:
- **JETRADE** (real private-jet-charter site) — editorial cream, high-contrast
  serif, black text, generous whitespace, luxury travel. Her old-money lane.
- **Dark gold-card app** (mockup) — premium dark, soft-shadow card, single gold
  accent, numbers in mono, app-like.
- **Lavender fintech app** (mockup) — read for the card-forward layout (card on
  top, list below), NOT the colors; she wants less color than the current amber.
- Through-line: card-forward, premium, restrained color, beautiful type.
- Plan: ONE self-contained HTML comparison page, two directions —
  **A: Editorial Cream** (JETRADE) and **B: Premium Dark** (gold card) — applied
  to real Wayloft screens (card + points, a deal item, a card-pick result,
  wallet coach, trip check). Embed her 3 references inline as base64, brand it
  Wayloft, drop a copy on the Desktop, and **inspect the live JETRADE site
  first** so type and spacing are accurate.

## Open questions

- Final green-light from Annabel on (a) the earn+burn personal scope and (b)
  Duffel = use the API key. She paused mid-decision; nothing was objected to.
- Mobile vs desktop priority for the design (references were mixed: JETRADE is
  desktop web, the other two are mobile).
- Keep Supabase (single-user) or simplify to local-first. Leaning keep Supabase.
- Seats.aero: does she have a Pro account? Session-scrape vs a Pro API token.
- Stack-reality check before the trip-check build: is the Duffel key actually
  set/live in the repo env, or just a stub?
- The 3 design reference images were pasted into chat, not saved to disk. On
  resume, re-request them (or pull from this session's transcript) before
  building the comparison page.

## Next steps

1. Get the one-line green-light on scope + Duffel.
2. Inspect the live JETRADE site (real reference) before designing.
3. Build the two-direction design comparison page (refs embedded, Wayloft
   branded, Desktop copy).
4. After design is chosen: re-center the app — strip SaaS scaffolding, rebuild
   the shell and the three screens (Setup / Earn / Burn) in the chosen lane.
5. Wire the data layer in build order: earn engine + scraped feed first, then
   authenticated Seats.aero + Duffel trip check.

## Context to preserve

- Repo anchors: routes `/optimizer`, `/recommend`, `/travel`, `/cards`,
  `/bonuses`, `/dashboard`; engine `lib/recommend/engine.ts`; flight wrappers in
  `lib/flights/`; catalog in `data/`.
- The old master plan (`knowledge/wiki/wayloft-master-plan-v3.md`) is the SaaS-era
  strategy — most of its revenue/audience machinery is now intentionally cut.
  Read it only for catalog/data facts, not product direction.
- Annabel's current real situation: holds a Chase Freedom card; new job coming
  with higher spend; wants the app to tell her what card to get, which card to
  use per category, and when/where to use or transfer points. United + partners
  are a stated interest.
- Domain note baked into the card-pick logic: Chase Freedom points only become
  transferable to United etc. once she also holds a Chase Sapphire — so "what
  card to get" likely starts with a Sapphire.
