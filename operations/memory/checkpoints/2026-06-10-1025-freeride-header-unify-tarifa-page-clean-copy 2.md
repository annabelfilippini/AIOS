---
date: 2026-06-10
time: 10:25
project: websites / freeride-tarifa
status: in-progress
next-session: Get Annabel's review of the unified header, the new tarifa.html page, the real-voice copy, and the clean yoga photo. If approved, decide whether to build out proper instructor tabs using the real team bios (Olivier, Vanessa, Magali, Basti, Johanes) and whether to confirm guest/instructor photo permissions with Free Ride before production.
---

# Session: Freeride header unify, Tarifa page, real-voice copy, clean images

## What we worked on

- Reviewed homepage v2 with Annabel. Two asks: (1) remove text-baked-in images,
  (2) reuse Free Ride's real website wording so it reads as a refresh, not a rewrite.
- Then a second round: fix the inconsistent header across pages, make Tarifa its own
  page (not a #trip anchor), and find clean yoga photos.

## Decisions made

- Text in still images is out; videos keep their captions (motion carries them).
  Swapped the "KITE & YOGA" and "KITE CAMP" text collages for clean shots.
- Pulled real copy from freeridetarifa.com (homepage + kite-school team page):
  hero tagline "Let yourself be gone with the wind and discover the freedom of
  kitesurfing", "wind capital of Europe / 300+ days", radio headsets, max 4 students
  per instructor, IKO/FAV certified, the three real beaches (Los Lances,
  Valdevaqueros, Balneario) and their beach bars.
- De-fabricated the "Leah, 27, solo traveler" card (invented name/age on a real
  identifiable person) to an experiential "Join our kite family / Bring back lifelong
  memories" framing. Oleg kept (real, from their IG reel).
- Unified the header across index/lessons/rent + new tarifa: transparent over a dark
  hero, then becomes the same paper color as the page on scroll. Same tabs
  (Freeride, Lessons, Rent gear, Tarifa) and a WhatsApp action on every page.
  Dropped the old "browser-tab" solid header and the external Book button on inner pages.
- Tarifa is now its own page (tarifa.html) with the real "wind capital" copy, the three
  beaches, an after-kite lifestyle grid, and a WhatsApp CTA. Homepage trip section keeps
  a teaser grid with a "Discover Tarifa" button to the full page.
- Yoga: their Instagram only had the text yoga collage, but their own site has a clean
  yoga photo (kite-yoga-retreat page). Cropped the clean yoga-pose panel and put it back
  in the homepage trip grid ("Kite and yoga to reset the body"). Already cleared since it
  is their own published image.

## Files changed / created

- `index.html` (real-voice copy throughout, clean grid images, Tarifa tab -> tarifa.html,
  Discover Tarifa button, clean yoga in grid)
- `tarifa.html` (new dedicated Tarifa page)
- `lessons.html`, `rent.html` (unified header CSS + markup: Tarifa tab, WhatsApp, paper
  header, mobile tabs hidden)
- `assets/web/ride.jpg`, `grab.jpg`, `cafe.jpg` (clean action + old-town crops)
- `assets/web/yoga-clean.jpg` (clean yoga, cropped from their site banner)
- `assets/site-originals/` (downloaded site yoga banner + crops)

## Verification completed

- Local preview on port 8792 (python http.server via .claude/launch.json).
- Tarifa page: transparent header over aerial hero, turns paper on scroll, beaches and
  after-kite grid render with real copy.
- Lessons/rent: DOM-confirmed tabs now include Tarifa, action = WhatsApp (wa.me),
  topbar bg = paper rgba(251,251,248,0.94), old box-shadow browser-tab style gone.
- Homepage: hero copy updated, trip grid clean (aerial, old town, ride, clean yoga),
  Discover Tarifa button -> tarifa.html.

## Open questions

- Build proper instructor tabs next, using the 5 real team bios? (Olivier founder,
  Vanessa co-founder, Magali, Basti, Johanes.)
- Confirm with Free Ride which featured guest/instructor faces are cleared for production
  (the yoga photo is their own published image; IG guest faces still need a yes).
- Preview screenshot tool keeps rendering at reduced/mobile scale after cross-page
  navigation; reload + explicit resize is the workaround.

## Next steps

- Annabel reviews unified header, tarifa.html, real-voice copy, clean yoga.
- If approved: draft instructor tabs from real bios; consider requesting original
  full-res yoga/team assets from Free Ride over WhatsApp.
- Mobile-width QA pass before client review.
