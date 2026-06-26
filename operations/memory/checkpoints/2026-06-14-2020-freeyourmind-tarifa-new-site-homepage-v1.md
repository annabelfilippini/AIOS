---
date: 2026-06-14
time: 20:20
project: websites / freeyourmind-tarifa
status: in-progress (homepage v1 built + verified; awaiting Annabel's reaction to the vibe)
next-session: Get Annabel's read on the soft-editorial/wellness direction. If approved, build inner pages mirroring the real IA (Courses, Offers, Accommodation, Tarifa, Contact). Confirm IKO/VDWS + prices before they go live; request FyM's own photos (IG @fym_experience) + logo to replace the Unsplash placeholders.
---

# Session: New site for "Free your Mind" kite school (different vibe from Freeride)

## The ask

Annabel wanted a NEW website project for a second Tarifa kitesurf company,
kitesurf-tarifa-spain.com, with "a little bit of a different vibe from the
freeride site." She told me to choose a vibe from the websites `design.md` inspo
and start updating the site.

## What I did

- Scraped the live site (Firecrawl). It is **Free your Mind** (FyM), an IKO/VDWS
  kite + surf school in Tarifa & Morocco, run by Tanja, Max & Carole. Signature:
  **"No Wind? No Pay!"** Strong holistic angle (kite + yoga, girls courses,
  Morocco camps, "open all year"). Facts saved to `content.md`.
- **Vibe decision: soft editorial / luxury (warm wellness-retreat lane).** This
  is the deliberate point of difference from Freeride, which lives in the
  cinematic / kinetic-documentary lane (black, acid-lime, adrenaline, Work Sans).
  The brand is literally called *Free your Mind* and built on kite+yoga, so the
  calm/retreat read is true to the business. Anchored in the global design.md
  lane that is named best for "wellness, hospitality, retreats."
- Scaffolded `projects/websites/freeyourmind-tarifa/` from `_template` and wrote
  `design.md` (brand direction + iteration log) and `content.md` (verified facts).
- Built `index.html` homepage. Palette: warm ivory `#F5EEE2` + warm ink `#2B2420`
  - terracotta `#C26A45` + sea-teal `#2E5854`. Type: **Fraunces** display serif
  (italic on "Free your *Mind*") + **Inter** body. Sharp corners, hairline rules,
  faint film grain, lots of air. Flow: full-bleed golden-hour hero → clay
  "No wind, no pay" ribbon → philosophy band ("Learning to kite should feel calm,
  not scary", yoga image) → offerings grid ("Four ways into the water": learn /
  kite+yoga / camps / rent+supervise) → teal "Our promise" reset (IKO+VDWS, open
  all year, no wind no pay, tailor made, TripAdvisor) → "Tarifa, and then Morocco"
  editorial spread → "Stay a few minutes from the beach" list (5 real properties
  with $/$$/$$$ tiers) → full-bleed contact CTA → designed footer.
- Gentle scroll-reveal (IntersectionObserver, reduced-motion + no-IO fallback,
  calmer than Freeride's). WhatsApp-first CTAs throughout (wa.me/34669261678).

## Decisions made

- Chose ONE lane and stayed in it (soft editorial/wellness), per global design.md
  "pick one dominant vibe for client work." Did NOT mix in any black/poster or
  adrenaline treatment.
- No invented facts: prices routed to WhatsApp (real site hides them too);
  IKO/VDWS shown but flagged to verify; TripAdvisor linked, no fabricated rating;
  team named (Tanja, Max, Carole) without invented roles/bios.
- No dashes anywhere in copy (Annabel's voice rule).
- Imagery = free-license Unsplash placeholders, downloaded locally so the page is
  self-contained. Flagged in content.md + footer ("images are placeholders") to
  swap for FyM's own before any live launch. Did NOT use the live site's
  copyrighted Jimdo photos.

## Context to preserve

- Preview: local server on **port 8848**,
  `http://localhost:8848/index.html` (cache-bust with `?v=` — recurring python
  http.server stale-cache trap). Server may still be running. File is also in the
  Claude Launch preview panel.
- Verified with Playwright (the inline preview only paints the top of long pages;
  full-page screenshots need force-reveal of `.reveal` els or they read blank,
  which is a capture artifact, not a user bug). Checked desktop 1440 + mobile 390:
  hero legible, all sections render, single-column stacking clean, console 0
  errors (added an inline SVG favicon to clear the lone favicon 404).
- 11 Unsplash images in `assets/web/` (hero-kite-golden, kite-jump-sunset,
  kite-beach-sunset, kite-jump-2, kite-silhouette, yoga-calm-water,
  yoga-pose-beach, yoga-portrait, coast-turquoise, morocco-earth-sea,
  dunes-oasis).
- Open / next: confirm IKO/VDWS + prices; get real FyM photos + logo; build inner
  pages if she likes the direction. Could vary the offerings grid later (global
  design.md warns against repeating identical cream image grids).
- Tree note: AI-OS working tree remains large/dirty (1770+ files from prior
  sessions); untouched here. Only the new freeyourmind-tarifa files + this
  checkpoint were added this session.
