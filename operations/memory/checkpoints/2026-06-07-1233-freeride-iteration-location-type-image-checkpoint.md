---
date: 2026-06-07
time: 12:33
project: websites / freeride-tarifa
status: in-progress
next-session: Continue reviewing the Freeride homepage and Lessons page visually from http://127.0.0.1:8097/, starting with whether the local Tarifa locator map and About image feel right.
---

# Session: Freeride homepage and Lessons polish

## What we worked on

- Continued iterating `projects/websites/freeride-tarifa/` from the hybrid direction:
  cinematic Freeride hero, calmer Santic-style left rail homepage, Lessons as a separate page.
- Read the latest Freeride checkpoints and used `client-website-refresh` for the iteration workflow.
- Updated `projects/websites/freeride-tarifa/index.html`.
- Updated `projects/websites/freeride-tarifa/lessons.html`.
- Tweaked `projects/websites/design.md` wording where the session produced reusable preference corrections.

## Decisions made

- Keep the old cinematic Freeride homepage hero, but reduce the `Freeride` type scale so it is not page-consuming.
- Remove duplicate green section kicker/title rows such as "The team", "Location", and "Trip options" because the left rail already names sections.
- Avoid generated-feeling catchy copy like "Tarifa kite school, kept practical." Use plain section labels such as `About`, `Instructors`, `Location`, and `Options`.
- Keep the four stats in About, but align them consistently and avoid text wrapping or column overlap.
- Do not reuse the same Freeride beach image across major sections. The homepage now keeps that image only as the hero background.
- Replace the About image with a different official Freeride image from the live Freeride site assets.
- The Location section should include a map of where Tarifa is, but not a fake or inaccurate drawn Spain map.
- The final Location version uses a local SVG locator map based on approximate Iberia lon/lat projection, with Tarifa marked on Spain's southern coast and Portugal, Morocco, Madrid, and Lisbon as context.
- Location content should use verified Freeride facts: Freeride is based in Tarifa town, and their official teaching spots are Los Lances and Valdevaqueros. Remove Palmones from this section.
- Lessons page typography should match the smaller Freeride homepage heading and lead scale.

## Verification completed

- Local preview server is running at `http://127.0.0.1:8097/`.
- Homepage and `lessons.html` returned `200`.
- Browser QA with bundled Playwright verified:
  no desktop or mobile horizontal overflow.
- Verified About image loads.
- Verified the local locator map renders in screenshots.
- Verified the old repeated beach image appears only once on the homepage.
- Verified Lessons computed heading and lead font sizes match the Freeride page scale.
- Checked official Freeride source page: `https://freeridetarifa.com/kite-school-in-tarifa/`.

## Open questions

- Whether Annabel likes the local SVG locator map visually, or wants a more photographic / embedded map style later.
- Whether the About image crop feels right, or should be swapped for a different verified Freeride asset.
- Whether the Instructors section should use the real individual team photos from the official Freeride page instead of generic action images.
- Whether the Location section should include a button/link to Google Maps or the Freeride contact page.

## Next steps

- Review the homepage visually from the top through Options.
- Review `http://127.0.0.1:8097/lessons.html` after the font-size sync.
- Continue polishing section by section instead of rebuilding the whole site.
- If Annabel has to correct the same issue again, add a stronger good/bad example to website design guidance.

## Context to preserve

- Annabel is correcting "AI tells" very specifically: too-big type everywhere, catchy generic lines, duplicate labels, misaligned stats, repeated imagery, and inaccurate decorative geography.
- `projects/websites/design.md` now includes updated guidance on proportionate hero type, plain client copy, aligned stats, verified maps, and not reusing the same image across major sections.
- Do not treat a map request as permission to invent geography. If a real embed is blank or unavailable, use verified coordinates and clearly keep the graphic as a locator.

## System refinement candidates

- Add a reusable website QA check: scan for repeated image URLs across major sections and flag duplicates before review.
- Add a reusable location QA rule: if a map is custom-drawn, verify the geography or use a real map/source-linked locator instead.
