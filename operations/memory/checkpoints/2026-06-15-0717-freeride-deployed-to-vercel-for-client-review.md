---
date: 2026-06-15
time: 07:17
project: websites / freeride-tarifa
status: in-progress
next-session: The static Freeride Tarifa site is now LIVE on Vercel so Annabel can share it with Free Ride for feedback. URL (production alias, public, NO auth gate): https://freeride-tarifa.vercel.app — verified all 5 pages (index/lessons/rent/stay/tarifa) return 200, assets serve, and the homepage renders in a real browser (Playwright load + correct title). Vercel project: annabel-filippinis-projects/freeride-tarifa, created/linked this session (Vercel wrote a `.vercel/` dir in the project and added it to that project's local .gitignore; CLI v51.2.1, authed as annabelfilippini). TO REDEPLOY after edits: `cd projects/websites/freeride-tarifa && vercel --prod` (already linked, no setup prompts). A `.vercelignore` was added so the public deploy ships ONLY the 5 pages + referenced assets (assets/web, assets/instagram-collage, assets/videos). It EXCLUDES: internal docs (brief-generator.md, brief-template.md, content.md, design.md), old backups (homepage-draft.html, index-collage-backup.html), research/, .claude/, .DS_Store, and the two UNREFERENCED source-footage folders assets/instagram-originals (~89M) + assets/site-originals (776K). That trimmed the upload from 142M to ~52M; confirmed those excluded paths 404 on the live URL. CAVEAT: the homepage logo still hotlinks from freeridetarifa.com WordPress (external <img src>), works but is not self-hosted. This is a FEEDBACK PREVIEW, not a final launch — the prior checkpoint's clearance items still stand before any permanent public site: sponsor action-photo clearance (Eleveight/Ketos/Mystic/Kitetrip/Nereide are editorial/brand-site preview assets), partner-logo trademark clearance, Oleg/Leah name confirmation, hotel Google review-count checks. Carried open design items: Hotels section (next build ask), Shopping section (skipped, needs better photos), OSM-vs-Google map decision. Work is uncommitted in a large dirty tree (~1770 files) — do not blind-commit.
---

# Session: Freeride Tarifa static site deployed to Vercel for client review

## What we worked on

Annabel asked to push the Freeride site to Vercel to share with Free Ride for their
feedback. Confirmed Vercel CLI was already installed + authed (not assumed), located
the site, deployed it cleanly, and verified it is publicly reachable.

## What changed

- **Deployed to Vercel production.** `vercel --prod --yes` from
  `projects/websites/freeride-tarifa/`. Live at the clean alias
  **<https://freeride-tarifa.vercel.app>** (also a long immutable deploy URL).
  Project `annabel-filippinis-projects/freeride-tarifa` created + linked this session.
- **Added `.vercelignore`** (new file in the project) so only public pages + referenced
  assets ship. Excludes internal markdown, old HTML backups, research/, .claude/,
  .DS_Store, and the two unreferenced source-footage folders (instagram-originals,
  site-originals). Upload dropped 142M -> ~52M.

## Verified (all on the live URL)

- Homepage HTTP 200 with the real title (not a Vercel login wall) — deploy is PUBLIC.
- lessons / rent / stay / tarifa pages all 200; an asset (hero-poster.jpg) serves as
  image/jpeg. Homepage also loaded in Playwright with correct title.
- Excluded files (content.md, design.md, index-collage-backup.html, homepage-draft.html,
  an instagram-originals .mp4) all return 404 — the ignore list worked.

## Open questions / next

1. This is a feedback preview. Before any *permanent* public launch, the carried
   clearance items still apply: sponsor action-photo licensing, partner-logo trademark,
   Oleg/Leah name confirmation, hotel Google review-count checks.
2. Homepage logo hotlinks from freeridetarifa.com WordPress — self-host it before launch.
3. Carried design asks: Hotels section (next build), Shopping section (needs photos),
   OSM-vs-Google map decision.
4. Redeploy after any edit with `vercel --prod` from the project dir (already linked).
5. Work is uncommitted in a large dirty tree (~1770 files); review before any commit.
