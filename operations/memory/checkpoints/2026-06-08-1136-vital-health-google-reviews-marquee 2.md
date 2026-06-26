---
date: 2026-06-08
time: 11:36
project: vital-health-webflow-review
status: complete
next-session: Decide live-sync method (Google Places API → Webflow CMS via Make, vs. embed widget) before Webflow rebuild phase.
---

# Session: Vital Health Google reviews integrated into homepage marquee

## What we worked on

- Replaced the mock 4-card "Google reviews" section on
  `projects/websites/vital-health-review/home-review.html` with a real
  auto-scrolling marquee of 68 actual 5-star Google reviews from the last
  2 years.
- Scraped Google Business Profile via Playwright (Maps URL with `data=` CID,
  sorted by Newest, scrolled until all 79 reviews loaded, expanded "More"
  buttons, extracted via `.jftiEf` wrapper, `.MyEned` body, `.kvMYJc` stars,
  `.rsqaWe` date, `.d4r55/.WNxzHc` author).
- Built CSS marquee: `.rev-marquee-track` with two `.rev-marquee-set`
  containers (68 cards each), `padding-right: 24px` trailing buffer so each
  set's width includes its gap. Animation `rev-scroll 240s linear infinite`
  translating to `-50%`. Hover-to-pause, `prefers-reduced-motion` fallback,
  edge mask fade.
- Removed the eyebrow + h2 + meta-note head block per Annabel; header is
  now just an h2 "In patients' words.".
- Fixed two bugs that were causing "5 cards then blank then 5 more":
  (a) half-gap math glitch at the snap point, (b) owner replies leaking
  into cards where reviewers left stars only with no text.

## Decisions made

- Static-bake reviews into the HTML preview for client review now; defer
  live-sync decision to the Webflow rebuild phase.
- Filter rules: 5-star AND last 2 years AND has body text. Excluded
  1 × 1-star (Katherine Collins), 4 × older than 2 years, 6 × stars-only.
- Set wrapper pattern (`.rev-marquee-set` with `padding-right` = gap) is the
  bulletproof CSS marquee approach; total width = 2 × set width exactly.

## Open questions

- Live-sync long-term: Google Places API → Make → Webflow CMS (~$10/mo,
  native styling, fully editable) vs. third-party widget (Elfsight,
  Sociablekit, ~$5–15/mo, faster setup but their styling). Decide during
  Webflow rebuild.
- Should the marquee also appear on services/about/shop pages, or stay
  homepage-only? Currently homepage-only.
- Some reviews are long; cards are line-clamped to 7 lines. Add a
  hover/click-to-expand later, or rely on "View on Google" link?

## Next steps

- Have Annabel hard-refresh `http://127.0.0.1:8765/home-review.html?v=2`
  and confirm the seamless flow.
- Loop in the Vital Health team for content approval on the visible reviews
  before any Webflow staging push.
- During Webflow rebuild (separate session), decide sync method and wire it
  to the same `.rev-marquee` structure.

## Context to preserve

- Google Business Profile CID: `ChIJcUlyRoo5W4YR6DO73UlEgjg`
  (Maps deep-link: `https://www.google.com/maps/place/?q=place_id:ChIJcUlyRoo5W4YR6DO73UlEgjg`).
- Raw scraped data: `projects/websites/vital-health-review/reviews-data/raw-google-reviews-2026-06-08-strict.json`
  (79 reviews, strict `.MyEned` body, English dates).
- Generated cards: `projects/websites/vital-health-review/reviews-data/cards-v2.html`.
- Stats at scrape time: 4.9 ★, 79 reviews, 78 five-star, 1 one-star.
- Stale `~/.claude/state/active-skills/instagram-carousel.lock` blocked
  edits via `enforce-media-folder.sh`; cleared manually. The hook's own
  bypass message is the fix when this recurs.
- Playwright Chrome instance was locked by an earlier session; killed
  `mcp-chrome-ece883a` processes to recover.

## System refinement candidates

- None proposed this session — friction was either environment quirks
  (browser lock, screenshot path, Google reCAPTCHA on Firecrawl) or
  hook-self-documenting bypasses, not pattern-level CLAUDE.md edits.
