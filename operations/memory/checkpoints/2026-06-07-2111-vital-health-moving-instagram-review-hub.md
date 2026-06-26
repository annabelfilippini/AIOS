---
date: 2026-06-07
time: 21:11
project: vital-health-instagram-carousel
status: complete
next-session: Use the Vital Health tabbed review hub for intro, hormone optimization, and the single moving announcement post; keep the moving post as one image, not a carousel.
---

# Session: Vital Health moving announcement and review hub update

## What we worked on

- Created a new Vital Health Instagram location announcement for the move to:
  - `500 N Capital of Texas Hwy`
  - `Bldg 6, Suite 125`
  - `Austin, TX 78746`
- Started with a 4-slide carousel, then simplified it per Annabel's direction into one single Instagram image.
- Added the final moving announcement into the existing Vital Health Instagram review hub as a new tab.
- Adjusted the review hub so the moving image displays smaller on-screen for easy screenshotting.
- Removed the intro tab metadata/header block Annabel had screenshotted from the intro review iframe.

## Decisions made

- The moving announcement should be a single image, not a carousel.
- Final image path:
  - `projects/websites/vital-health-review/media/2026-06-07-new-location-announcement/we-are-moving.png`
- Review hub path:
  - `projects/websites/vital-health-review/media/2026-06-07-hormone-optimization-carousel-fresh/review.html`
- The review hub now has three tabs:
  - `Intro Carousel`
  - `Hormone Optimization`
  - `Moving Announcement`
- The moving tab uses a small centered preview (`max-width: 360px`) so Annabel can screenshot it more easily.
- The white address area in the moving image should be a smaller square-like block around the address, not a tall blank panel.
- Removed the `Save this post...` line from the image and notes.
- Address text inside the white block should use the same type size across all lines.

## Open questions

- Whether Vital Health has an official move/opening date that should be added to the caption or future version.
- Whether `vitalhealth.md-hq.com` remains the preferred public booking/portal URL for all social CTAs.
- Whether the intro carousel's old caption still needs updating because it references a `free thirty-minute call` and `vitalhealthaustin.com`, while newer site guidance uses a complimentary 60 minute consultation and `vitalhealth.md-hq.com`.

## Next steps

- Refresh the browser at:
  - `file:///Users/annabelfilippini/Documents/AI-OS/projects/websites/vital-health-review/media/2026-06-07-hormone-optimization-carousel-fresh/review.html`
- Use the `Moving Announcement` tab to screenshot the smaller preview, or use the full PNG directly from:
  - `projects/websites/vital-health-review/media/2026-06-07-new-location-announcement/we-are-moving.png`
- If continuing Vital Health social work, read:
  - `projects/websites/vital-health-review/media/design.md`
  - `skills/instagram-carousel/SKILL.md`
  - `skills/instagram-carousel/references/style.md`

## Context to preserve

- Final moving image visual direction:
  - Deep forest background.
  - Large editorial serif `Vital Health is moving.`
  - Small hummingbird mark on dark background using light treatment.
  - Smaller cream/white square around the address.
  - Address is the main practical information.
- The first intro tab header/meta block hidden in:
  - `projects/websites/vital-health-review/media/2026-06-07-hormone-optimization-carousel-fresh/intro-carousel-review.html`
- The moving post folder contains:
  - `index.html`
  - `render.mjs`
  - `review.html`
  - `post.md`
  - `preship-audit.md`
  - `we-are-moving.png`
  - `vh-bird-logo.png`

## System refinement candidates

- For single Instagram announcements, do not force the `instagram-carousel` arc. Start with one image unless Annabel asks for a carousel.
- Review hubs should offer a small screenshot-friendly preview size for social posts, while keeping full-resolution PNGs linked separately.
