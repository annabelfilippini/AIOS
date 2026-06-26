---
date: 2026-06-07
time: 20:37
project: vital-health-instagram-carousel
status: complete
next-session: Use the tabbed review HTML as the current Vital Health carousel review hub, and start future service carousels from the updated health-service defaults.
---

# Session: Vital Health hormone carousel and carousel style refinement

## What we worked on

- Created a fresh 4-slide Vital Health Instagram carousel for hormone optimization.
- Iterated the slides with Annabel's visual and copy corrections until the set matched the desired Vital Health style more closely.
- Built a tabbed review HTML combining the prior Vital Health intro carousel and the new hormone optimization carousel.
- Updated durable guidance so future Vital Health carousels should require fewer micro-adjustments.

## Decisions made

- Current review hub:
  - `projects/websites/vital-health-review/media/2026-06-07-hormone-optimization-carousel-fresh/review.html`
- Tab 1 embeds the prior intro carousel copied locally as:
  - `projects/websites/vital-health-review/media/2026-06-07-hormone-optimization-carousel-fresh/intro-carousel-review.html`
- Tab 2 shows the hormone optimization PNGs:
  - `slide-1.png` through `slide-4.png` in the same folder.
- Hormone cover direction:
  - Headline is the service name, `Hormone Optimization`.
  - Do not use `Vital Health helps with...` as the headline.
  - Use a simple close like `Vital Health can help.`
- Logo direction:
  - Use the real hummingbird mark, not a fake `VH` text lockup.
  - Keep hummingbird size consistent across all slides in a carousel.
- Layout direction:
  - Remove redundant small kickers such as `For Women`, `For Men`, and `Hormone Care`.
  - Align actual text edges, not just outer containers.
  - Pre-control important line breaks for medical terms, support phrases, and URLs.
  - Equalize bullet spacing before showing list-heavy slides.
- Visual direction:
  - Avoid abstract filler panels with only leaves or vague circles.
  - Use fresh Vital Health-style still life imagery for warmth: cream linen, amber glass, clean lab paper, brass pen, botanical stem, warm natural light, no readable text.
- Copy direction:
  - Rewrite technically accurate but awkward copy into plain patient-facing sentences.
  - Keep public medical claims careful: `may be involved`, `can help`, `supports care around`, and `risk conversations` instead of guarantees.

## Open questions

- Whether `vitalhealth.com` is the final public URL for all future social CTAs.
- Whether the prior intro carousel should be migrated from the copied self-contained Desktop HTML into normal project PNG assets later.
- Whether future Vital Health service posts should stay square or use 4:5 unless Annabel specifies square.

## Next steps

- If Annabel approves the tabbed review page, use it as the current client-facing carousel proof hub.
- For the next Vital Health service carousel, read:
  - `projects/websites/vital-health-review/media/design.md`
  - `skills/instagram-carousel/SKILL.md`
  - `skills/instagram-carousel/references/style.md`
- Start from the new `4-slide health service arc` instead of inventing a layout from scratch.
- Before showing a first draft, run a manual preflight for logo size, line breaks, text alignment, bullet spacing, and whether any visual panel feels generic.

## Context to preserve

- Updated Vital Health media guide:
  - `projects/websites/vital-health-review/media/design.md`
- Updated Instagram carousel skill:
  - `skills/instagram-carousel/SKILL.md`
  - `skills/instagram-carousel/references/style.md`
  - `skills/instagram-carousel/references/README.md`
- Logged use of `instagram-carousel` in:
  - `operations/annabel-press/usage/events.jsonl`

## System refinement candidates

- The carousel skill should reliably read project-level `media/design.md`; this was added to the style stack docs during this session.
- The correction-listener hook did not run because this work happened outside the old active-skill lock flow. Future Codex-native carousel work should either use the skill formally or manually append important corrections, as done here.
- Consider adding a deterministic preflight script for rendered carousel PNGs that checks repeated logo width, square vs 4:5 format, and existence of `review.html`.
