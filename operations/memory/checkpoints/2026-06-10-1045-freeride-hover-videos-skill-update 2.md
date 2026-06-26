---
date: 2026-06-10
time: 10:45
project: websites / freeride-tarifa
status: in-progress
next-session: Get Annabel's review of the full set (unified header, tarifa.html, real-voice copy, clean images, hover-to-play crew videos). If approved, build proper instructor tabs from the 5 real team bios and confirm guest/instructor photo permissions with Free Ride. Optional polish: swap the crew-video badge to "Tap for sound" on touch via @media (hover: none).
---

# Session: Freeride hover videos, skill update, full refresh polish

## What we worked on (this session, cumulative)

- Reviewed homepage v2; removed text-baked-in still images and rewrote copy in
  Free Ride's real voice (scraped freeridetarifa.com homepage + team page).
- Unified the header across all four pages; made Tarifa its own page.
- Found a clean yoga photo on their own site and put it back in the homepage grid.
- Made the crew videos (Oleg, Leah) hover-to-play-with-sound instead of autoplay.
- Added a reusable guardrail to the client-website-refresh skill.

## Decisions made

- Crew videos: NO autoplay. Default = paused on poster + a "Hover for sound" badge.
  Hover plays with sound (unmuted), mouse-out pauses and re-mutes. Touch devices
  get a tap toggle. Implemented with mouseenter/mouseleave/click; muted-playback
  fallback if a browser blocks unmuted play.
- Leah card restored to "Meet the riders / Leah, from Lake Constance". Her name and
  age ("Leah, 27, from the lake of Constance") are baked into Free Ride's own reel,
  so they are a published detail, not our invention. Used the name, dropped the age
  for a cleaner heading. (Earlier I had wrongly stripped it as fabricated.)
- Header model: transparent over a dark hero, then becomes the same paper color as
  the page on scroll. Same tabs (Freeride, Lessons, Rent gear, Tarifa) + WhatsApp on
  every page. Old "browser-tab" inner-page header and external Book button removed.
- Tarifa.html uses their real "wind capital" copy, the three real beaches
  (Los Lances, Valdevaqueros, Balneario) with beach-bar names, after-kite grid, CTA.

## Files changed / created

- `index.html` (real-voice copy, clean grid images incl. clean yoga, Tarifa tab ->
  tarifa.html, Discover Tarifa button, hover-to-play crew videos + cue badge,
  Leah card restored)
- `tarifa.html` (new dedicated page)
- `lessons.html`, `rent.html` (unified header CSS + markup)
- `skills/client-website-refresh/SKILL.md` (new Guardrail: reuse real client copy;
  never invent bios for real, identifiable people)
- `assets/web/ride.jpg`, `cafe.jpg`, `grab.jpg`, `yoga-clean.jpg`
- `assets/site-originals/` (downloaded yoga banner + crops)
- `.claude/launch.json` (freeride preview server on port 8792)

## Verification completed

- Crew videos: DOM-confirmed default paused+muted with "HOVER FOR SOUND" cue;
  hover -> is-playing + muted=false; mouse-out -> paused + muted again.
- Header: tarifa transparent-over-hero then paper on scroll; lessons/rent
  DOM-confirmed Tarifa tab + WhatsApp action + paper bg, old browser-tab style gone.
- Homepage: hero/band/cards/crew/grid copy updated; grid clean (aerial, old town,
  ride, clean yoga); Discover Tarifa button -> tarifa.html.
- Skill edit applied.

## Open questions

- Build instructor tabs next from the 5 real bios? (Olivier founder, Vanessa
  co-founder, Magali, Basti, Johanes.)
- Which guest/instructor faces are cleared for production? Yoga photo is their own
  published image; IG guest faces still need Free Ride's yes.
- Touch badge still says "Hover for sound" (tap works); swap via @media (hover:none)?

## Next steps

- Annabel reviews the full set on the live preview (port 8792, all four pages).
- If approved: instructor tabs from real bios; request original full-res yoga/team
  assets from Free Ride over WhatsApp; mobile-width QA pass.

## Notes / gotchas

- Preview screenshot tool renders at reduced/mobile scale after cross-page
  navigation; reload + explicit resize is the workaround.
- Re-serve preview with: `python3 -m http.server 8792` from the freeride folder,
  or preview_start "freeride" via .claude/launch.json.
