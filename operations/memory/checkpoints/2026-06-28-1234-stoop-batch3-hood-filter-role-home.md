---
date: 2026-06-28
time: 12:34
project: stoop
status: in-progress
next-session: Pick a deferred item — most impactful is multi-stand feed (needs a backend) or hood-tag the NEIGHBORS teaser stubs
---

# Session: Stoop — Batch 3 (neighborhood filter + role-aware home) + reqbar cleanup

Follows `2026-06-28-1245-stoop-product-vs-service-builder.md`. All work in the single
file `projects/stoop/index.html`. Tracker: `projects/stoop/in-progress.md`.

## What we worked on
Quick reqbar cleanup, then Batch 3: make the feed hyperlocal-real instead of
hardcoded "Country Club" everywhere.

## What shipped
**Cleanup:** product reqbar centers the lone "Request this" button (was shoved to the
edge by the leftover service-layout `justify-content:space-between`). One line in
renderProfile: `reqB.closest('.reqbar').style.justifyContent=isSvc?'':'center'`.

**Batch 3 — hood filter + role-aware home:**
- **Tag stands:** `profile.hood`. `DEFAULT.hood='country-club'` (reseeds Delaney);
  seller's new stand inherits `account.hoods[0]` at ob-go (fallback country-club).
- **Feed filter:** new `inFeed(p)` — buyer sees a stand only if `account.hoods`
  includes its hood; seller always sees own; no account = no filter. renderHome guards
  the stand card with it; empty feed → just the CTA (the "too quiet" valve, minimal).
- **Top-bar `.place`:** `renderPlace()` called from `go()` — seller: their one hood +
  "verified neighbor"; buyer: hood name (1) or "N neighborhoods" (many); no account
  falls back to the demo default. Replaces hardcoded "Country Club neighborhood".
- **Role-aware CTA:** add-stand card reads "Open your own stand" for buyers (was "Add
  your stand", which framed Delaney's seeded demo as theirs); seller keeps "Add your stand".

## Decisions made
- Kept the single-profile-slot model (deferred limitation): for now a seller still sees
  the seeded Delaney as the only feed stand. Real multi-stand feed needs a backend.
- Empty feed shows just the CTA rather than a designed empty state — minimal valve for now.

## Open questions
- Empty-feed UX: is "just the CTA" enough, or does a buyer in a quiet hood need a
  "no stands yet, invite a neighbor" prompt?

## Next steps (deferred, none picked)
- **Multi-stand feed** — single profile slot → multi-kid/multi-stand (needs a backend).
- **Hood-tag the NEIGHBORS teaser** (Mateo/Priya stubs) so they can join the real feed.
- Real SMS/backend confirmations; per-week "copy to next 4 weeks"; richer empty-feed state.

## Context to preserve
- Verified in preview (port 8762), no console errors: buyer country-club+hilltop → sees
  Delaney + "2 neighborhoods" + "Open your own stand"; buyer washington-park → empty
  feed + CTA + "Washington Park neighborhood"; seller hilltop → own stand + "Hilltop
  neighborhood · verified neighbor" + "Add your stand"; product reqbar centered; fresh
  visitor lands on welcome.
- Data model: `account = {role:'buyer'|'seller', hoods:[id,...], contact?, name?}` in
  localStorage `stoop-account-v1`; `profile` (one stand) in `stoop-profile-v2`.
- `CITY.hoods` (9 Denver neighborhoods, id+name+lat/lng) + `hoodName(id)` helper already existed.

## System refinement candidates
- None this session.
