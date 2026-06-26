---
date: 2026-06-07
time: 11:46
project: websites / freeride-tarifa
status: in-progress
next-session: Continue from the hybrid direction: earlier cinematic hero on the homepage, Santic-style rail content below, Lessons as a separate page.
---

# Session: Freeride Tarifa design iteration checkpoint

## What we worked on

- Iterated the Freeride Tarifa static preview in `projects/websites/freeride-tarifa/`.
- Read the latest Freeride checkpoint from `operations/memory/checkpoints/2026-06-07-1058-freeride-tarifa-editorial-preview.md`.
- Started by changing the hero from "Born in the wind" to the business name, adding Rental Gear to nav, correcting lodging copy, and testing a Tarifa locator map.
- Annabel then clarified the page still felt too busy and liked the Santic Group flow: top tabs plus a sticky left scroll rail.
- Rebuilt the preview into a calmer structure, then corrected again after Annabel said the old hero was the part she liked and Lessons should be a separate tab/page.

## Decisions made

- Do not treat a new reference as a full-site replacement instruction. Mix and match the best parts across drafts.
- Keep the earlier Freeride full-bleed hero on the homepage.
- After the hero, use the calmer Santic-style rail structure for homepage content: About Freeride, Instructors, Location, Options.
- Lessons should live on its own top-level page/tab, not below the homepage scroll.
- Fact-check concrete content before putting it into the site, especially lodging, pricing, locations, instructors, and course details.
- Avoid cheesy poetic hero lines like "Born in the wind" for client sites unless Annabel explicitly asks for that tone.

## Files changed

- `projects/websites/freeride-tarifa/index.html`
- `projects/websites/freeride-tarifa/lessons.html`
- `projects/websites/design.md`
- `operations/memory/checkpoints/2026-06-07-1141-freeride-mix-match-two-page-direction.md`

## Verification completed

- Local homepage returns `200` at `http://127.0.0.1:8097/`.
- Local Lessons page returns `200` at `http://127.0.0.1:8097/lessons.html`.
- Static checks passed for both HTML pages: no duplicate IDs, no missing hash anchors, and zero `border-radius` mentions.
- Final image URLs used in the pages were checked with `curl -I` during the session.
- Browser screenshot QA remained blocked by the app's locked Playwright browser profile.

## Open questions

- Whether the after-hero homepage rail content should stay mostly white or reintroduce one darker/editorial reset.
- Whether the Lessons page pricing table should remain restrained or become more visual while staying less busy than Freeride's current colored cards.
- Whether Freeride can provide real team/instructor photos so the Instructors section is more accurate and personal.

## Next steps

- Review both local pages visually.
- If the hybrid structure feels right, polish spacing, copy, and verified images rather than rebuilding again.
- Consider turning the current static preview into a platform-ready rebuild only after Annabel approves the direction.

## System refinement candidates

- Add a stronger reusable iteration rule to website workflows: preserve liked sections across drafts, and compose references instead of resetting the whole design.
