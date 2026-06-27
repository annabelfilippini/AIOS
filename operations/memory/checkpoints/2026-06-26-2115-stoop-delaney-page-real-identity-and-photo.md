---
date: 2026-06-26 21:15
project: stoop
status: in-progress
type: checkpoint
slug: stoop-delaney-page-real-identity-and-photo
---

# Stoop — cousin page is now Delaney's, with her real details + photo

Follows `2026-06-26-2045-stoop-deeper-lacrosse-theming.md`. Same v1 file
(`projects/stoop/cousin-lacrosse.html`), now populated with the real kid's
identity, her photo, and a younger voice. Annabel reviewed live in-browser.

## Who the page is for (real, locked)
- **Delaney Sherry, 14**, goes to **Kent** (Kent Denver). Plays **attack for
  Concept** (club team) and loves it. Teaches all levels and all positions,
  super enthusiastic, just wants to help neighborhood kids get better.
- **Country Club neighborhood** (Denver). Lessons usually at **Cheesman Park**
  but flexible on location. **$30 / 1-hour** lesson.
- **No loaner sticks** — students bring their own (she can't lend). Shown as a
  `🥍 Bring your own stick` fact chip + in the About copy.

## What changed this session (on top of prior theming work)
- **Avatar = her real photo.** Annabel dropped a phone screenshot on the
  Desktop (IMG_3365.PNG, a share-sheet screen with a circular action photo of
  Delaney playing). Cropped the circle out with PIL (box 210,760,950,1500),
  saved as `projects/stoop/delaney.jpg`, wired via `const PHOTO='delaney.jpg'`.
- **Killed the crossed-stick SVG entirely** (avatar + faint watermark). Annabel:
  "the sticks look bad and mis shaped." Also rejected her own supplied reference
  `shots/lax stick image.jpeg` — it's a **watermarked dreamstime stock JPEG**
  (baked watermark, white bg, unlicensed), can't use. Kept only the clean
  theme-tinted **field center-line** behind the hero. Removed dead motif CSS.
- **About rewritten young + fun** (her voice, exclamation points, casual). Tone
  was too grown-up before.
- **"Make it yours" is owner-only** — the swatch/color bar is hidden on the
  public profile and only shows in edit mode: `cousin-lacrosse.html?edit=1`.
  (Gated via `?edit` query param. Note: chosen theme persists only in that
  browser's localStorage; visitors see the default until there's a backend.)
- **Hourly slots** (was 45-min): weekdays 4/5/6pm, Sat 9/10/11am.
- **Request-bar overlap fixed** — was `position:sticky;bottom:0` floating over
  the calendar on mobile. Made it static + smaller. Verified 18px gap, all 30
  day cells render.
- Title font is **Anton** (varsity/jersey) on the hero H1; Fredoka section
  headers; Nunito body. Removed several em-dashes (no-dash rule).

## Verified
Playwright at 1200px + 390px, plus opened in Annabel's real browser. Photo
loads (img 200), calendar/booking/theme-swap all fire. Only console error is
favicon 404. Shots: `projects/stoop/shots/delaney-v3-hero.png`,
`delaney-v3-mobile.png` (+ v2/editmode earlier).

## Open / NEXT
- **Avatar photo is a full-motion action crop** — reads as "girl mid-play," not
  a face close-up. Offered a tighter face/upper-body re-crop; Annabel hasn't
  decided. Also offered to bump avatar size larger. Both pending.
- Still the original NEXT options: availability editor (pattern hardcoded),
  builder flow (4-5 questions → page), the feed (hyperlocal scoping).
- Theme-follows-visitor needs a backend (localStorage is per-browser).

Still no code committed (concept/preview stage). Working tree: edits to
cousin-lacrosse.html + new `delaney.jpg`; her `shots/lax stick image.jpeg` is
unused (watermarked, do not ship).
