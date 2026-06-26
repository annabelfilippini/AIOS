---
date: 2026-06-10
time: 09:45
project: websites / freeride-tarifa
status: in-progress
next-session: Get Annabel's review of the new directed-film homepage (index.html, served at http://localhost:8791/index.html). If approved, propagate the same approach to Lessons and Rent pages, then upgrade the Freeride design.md through the new brief-generator (add Reconstruction Level, Emotional Target, Vibe Lane; repoint Asset Strategy at assets/web + instagram-originals).
---

# Session: Freeride generator system, Instagram scrape, homepage v2

## What we worked on

- Reframed Annabel's request: she wants a general design.md that can auto-generate
  project-specific design.mds from a target site + her taste. Diagnosed that the
  existing `projects/websites/design.md` is a strong taste library but NOT a
  generator. It was missing two layers: a generation protocol and an output template.
- Built the missing machinery (both placed in the freeride folder per Annabel's
  instruction, written to be reusable / promotable to `projects/websites/` later):
  - `brief-generator.md` — 10-step protocol: audit site, pick ONE vibe lane, set
    reconstruction level (full/partial/light), translate references into mechanics.
    Leads with the core rule: every instruction must name a behavior, not a feeling.
  - `brief-template.md` — the skeleton every project brief fills, extracted from the
    already-strong Freeride brief structure.
- Scraped Free Ride's Instagram (they consented). Pulled the 10 shortlisted posts as
  full-res originals: 5 reels (video) + 17 carousel images, ~89MB.
- Built a clean web-asset set (`assets/web/`): compressed muted H.264 videos
  (hero 3.8MB, oleg 5.9MB, lea 11.7MB), poster frames, and renamed stills.
- Rebuilt the homepage (`index.html`) from the old static screenshot collage into a
  directed-film sequence using the real footage. Old version backed up to
  `index-collage-backup.html`.

## Decisions made

- design.md system is now three layers: taste (design.md) + protocol (brief-generator.md)
  - output shape (brief-template.md). This is the repeatable "URL in, brief out" machine.
- The cinematic money shots are the CLEAN, no-text assets: aerial Tarifa (05) and the
  action jump (10). Reel videos (Oleg, Leah) have IG caption text baked in — fine for
  "meet the crew" proof moments, not for clean feature stills. Skipped interior/bedroom
  camp frames with promo text overlays.
- Scrape tooling: gallery-dl for photos + yt-dlp for reels, authenticated via Chrome
  browser cookies. Pause 6-12s between posts to dodge IG 429 / login-redirect blocks.
- Homepage approach: video hero (autoplay muted loop), dark positioning band, full-bleed
  "THE WIND DOES THE REST" chapter on the jump shot, learn/rent/stay routing, Oleg+Leah
  in-view-autoplay video proof, Tarifa editorial image grid, single WhatsApp close.
- No-dash copy rule applied throughout. WhatsApp number wa.me/34601655993 reused from
  current site.

## Files changed / created

- `projects/websites/freeride-tarifa/index.html` (rebuilt)
- `projects/websites/freeride-tarifa/index-collage-backup.html` (backup of prior version)
- `projects/websites/freeride-tarifa/brief-generator.md` (new)
- `projects/websites/freeride-tarifa/brief-template.md` (new)
- `projects/websites/freeride-tarifa/research/instagram-originals-inventory.md` (new)
- `projects/websites/freeride-tarifa/assets/instagram-originals/` (new, 22 media files, ~89MB)
- `projects/websites/freeride-tarifa/assets/web/` (new, compressed videos + posters + stills)

## Verification completed

- Local homepage returns 200 at `http://localhost:8791/index.html` (python http.server).
- Full-page desktop screenshot at 1440px confirms the directed-film sequence renders:
  video hero, positioning band, WIND chapter, choice cards, crew videos, Tarifa grid, CTA.
- All 10 IG posts confirmed downloaded and visually spot-checked for frame quality before
  selecting which to use.

## Open questions

- Identifiable guests (e.g. Leah) need usage permission confirmed with Free Ride before
  production use.
- The .webp camp frames (folder 07) and yoga still have Free Ride's own baked-in promo
  text. Acceptable for preview; for production prefer client originals without overlays.
- Does Annabel want the brief-generator + template promoted to `projects/websites/` root
  now, or proven on a second site (e.g. re-running it on Vital Health / Cooldown) first?

## Next steps

- Annabel reviews the new homepage at `http://localhost:8791/index.html` (server running
  in background; re-serve with `python3 -m http.server 8791` from the freeride folder if down).
- If approved: apply the directed-film approach to Lessons and Rent, request original
  full-res assets from Free Ride over WhatsApp (per the asset request list in design.md).
- Upgrade `freeride-tarifa/design.md` through brief-generator.md: add the three missing
  named sections (Reconstruction Level, Emotional Target, Vibe Lane) and repoint Asset
  Strategy from screenshots to `assets/web` + `assets/instagram-originals`.
- Consider mobile-width QA screenshot before client review.

## System refinement candidates

- Promote `brief-generator.md` + `brief-template.md` to `projects/websites/` and add a
  one-line pointer from `design.md` so every new site runs through the generator.
- Add an asset-prep convention to the website workflow: scrape originals → compress to
  muted web H.264 + poster frames → prefer clean no-text frames for cinematic feature slots.
