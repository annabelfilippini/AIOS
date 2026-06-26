---
date: 2026-06-18
time: 12:30
project: wayloft
status: in-progress
next-session: Finish the apps/web re-center — sweep the 25 component files that still use hardcoded amber-*/yellow-* Tailwind utility classes (they don't read the bronze token), mapping each to primary/accent (bronze) or a warm warn color per use. Then verify the logged-in app screens (dashboard / recommend / travel) render correctly in Editorial Cream — needs a Supabase session (no test login was available this pass). Static spec at projects/wayloft/design/screens.html is the visual source of truth. Dev server: `cd apps/web && npm run dev` (port 3000); public pages /login /about render the new skin without auth.
supersedes: 2026-06-18-1215-wayloft-batch4-mobile-design-system-complete.md
---

# Session: apps/web re-center — Editorial Cream foundation shipped

Annabel's call this session: **drop the locked Geist typography rule** ("we are
switching things up"), make the real app match the Editorial Cream static spec,
and re-center `apps/web`. Direction A (Editorial Cream squared), locked tokens
in the 2026-06-17-1300 checkpoint.

## What shipped (foundation — highest leverage)

The app is cleanly tokenized (Tailwind v4, CSS-first; nav + shadcn components
read `--background`/`--primary`/`--border` etc.), so repainting the tokens +
fonts cascades across the whole app. Changes:

1. **Fonts** (`app/layout.tsx`): Geist/Geist_Mono → **Jost** (`--font-sans`),
   **JetBrains_Mono** (`--font-mono`), **Cormorant_Garamond** (`--font-display`,
   weights 300–600), all via `next/font/google`.
2. **Tokens** (`app/globals.css`): `:root` repainted to Editorial Cream — paper
   `#F3EFE6`, panel `#FBF9F3`, ink `#0F0D0C`, bronze accent `#846340` (primary +
   accent + ring), secondary/muted `#EFEADF`, warm hairline `#E6DECC`, success
   `#4F6B3E`, warm-brick destructive `#A23E2C`, bronze-led charts. **`--radius:
   0px`** (squared). Added `--font-display` to `@theme inline`.
3. **Base layer**: `h1–h4` now render in Cormorant; `::selection` is bronze
   tint; added `.serif`/`.font-display` utility; `.mono`/`.label-signal`/
   `.badge-signal` fallback updated Geist Mono → JetBrains Mono.
4. **Dark mode** (`.dark`): repainted to an espresso/bronze variant so no amber
   lingers. NOTE: app forces light (`defaultTheme="light"`, `enableSystem=false`)
   so dark is effectively unused.
5. **Wordmark** (`components/nav/app-topnav.tsx`): mono amber → Cormorant
   (`font-display`) tracked caps in bronze.
6. **Typography rule** (`apps/web/.claude/rules/typography.md`): fully rewritten
   from the Geist mandate to the Cormorant / Jost / JetBrains Mono trio, with
   the static spec named as visual source of truth.
7. **Exact old brand amber `#D4A020`** swapped to bronze in the 3 files that had
   it: marketing /login, /signup, and the OG image route. (issuer-colors.ts and
   other amber-ish hexes intentionally untouched — those are card-issuer brand
   colors.)

## Verified

Dev server on :3000. `/login` + `/about` (public, no auth) render correctly:
computed `--background #f3efe6`, `--primary #846340`, `--radius 0px`, body =
Jost, headings = Cormorant Garamond, figures = JetBrains Mono. Zero console
errors. Screenshot: `projects/wayloft/design/screenshots/recenter-login.png` —
cream paper, Cormorant headline, bronze squared Sign-in button, bronze wordmark.

## Not yet done (next batch)

- **25 component files still use hardcoded `amber-*`/`yellow-*` Tailwind utility
  classes** (heaviest: components/cards/, travel/, optimizer/, dashboard/,
  onboarding/, marketing/). These do NOT read the token, so they still look
  amber. Sweep them to bronze `primary`/`accent`, deciding per use whether each
  amber is a semantic warning (use a warm tan/warn) or an accent (use bronze).
  Worth a careful pass, not a blind sed — `bg-amber-900` etc. carry meaning.
- **Logged-in app screens unverified.** The `(app)` routes call `requireUser()`
  and redirect to /login without a Supabase session; no test login was available
  this pass. The theme is global so they WILL inherit the skin, but confirm
  dashboard / recommend / travel visually once there's a session.

## Context to preserve

- Visual source of truth: `projects/wayloft/design/screens.html` (9 screens,
  design system complete). Design standard: `~/.claude/design.md`.
- Re-center is token-driven: `app/globals.css` + `app/layout.tsx` are the
  foundation; per-component amber classes are the cleanup tail.
- Real setup drives content: Freedom Flex held, 38,420 Chase UR locked, Sapphire
  is the next-card unlock, watching United / Star Alliance / Hyatt / Marriott.
</content>
