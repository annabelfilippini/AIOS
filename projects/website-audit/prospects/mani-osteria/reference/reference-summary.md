# Reference Sites — Mani Osteria
Chosen 2026-04-21. Scraped to `reference/<brand>/` (may be pruned by /audit-cleanup).

## Via Carota — https://www.viacarota.com/
**Why chosen:** Annabel specifically called out the "images below the initial image" pattern — huge hero photo + "Scroll" cue, then an **image-dense grid** (16 small square dishes) beneath, followed by prose about the restaurant. Exactly the structure Mani should adopt.
**Execution takeaways for Mani:**
- Oversized hero image that takes the full viewport, minimal chrome — logo top-left only.
- Subtle "Scroll" affordance in the hero (not a button, just a word) — signals there's more below, fixes the Don Angie dead-end.
- Grid of uniform square thumbnails of actual dishes/ingredients (12–16 images) immediately after hero — tactile, editorial, no captions needed.
- Single-sentence welcome lines set in a light serif, wide leading, left-aligned. No marketing voice. "Your neighborhood place for a leisurely lunch with a friend, family dinners or a late-night amaro."
- About copy is three short paragraphs, same serif, no subheads.
- Menu thumbnails are small square images that link out — clickable, not decorative.
**Do NOT copy:** the Squarespace default chrome or the decorative rays logo mark — that's Via Carota's identity, not Mani's.

## Don Angie — https://donangie.com/
**Why chosen:** Annabel loves the **first-open impression** — large centered wordmark over a 4-slide gallery carousel of atmospheric restaurant photos (dining room, plated dishes, close-ups). Warm, moody, photo-forward. Feels like a magazine cover.
**Execution takeaways for Mani:**
- Centered wordmark as the first thing you see (not a nav bar).
- Hero is photography, not text. Let the image carry the emotion.
- 4–5 atmospheric slides, slow crossfade — not typical marketing carousel.
- Reservation note is one small line above the fold ("Reservations become available 7 days in advance at 9am on OpenTable").
**Do NOT copy:** the fact that the page **stops after the carousel** — Annabel explicitly flagged this as the problem. Our version keeps the photo-forward opening but adds scrollable content below (the Via Carota grid + prose + menu + hours), with scroll-triggered reveals.

## Black Pearl (our own build) — `prospects/black-pearl/mockups/index.html`
**Why chosen:** reuse the `data-reveal` + `data-reveal-group` scroll pattern (IntersectionObserver). Elements fade up as they enter the viewport, grouped so a section's contents reveal in sequence. Annabel explicitly asked for this animation behavior.
**Execution takeaways for Mani:**
- `[data-reveal]` starts with `opacity: 0` + `translateY(24px)`; intersection adds `.is-visible` class → animates to `opacity: 1` + `translateY(0)` over ~700ms.
- `[data-reveal-group]` staggers children by ~80ms so a section cascades in.
- Apply to: eyebrow → title → subtitle → CTAs (hero group), each image in grid (stagger), section labels + body text (about block).
**Do NOT copy:** Black Pearl's dark oxblood/cream palette — Mani's palette is warm gold + off-white + ink.

## Combined direction
Don Angie's photo-first opening + Via Carota's image-grid-below-hero + Black Pearl's scroll-reveal animations. Mani's existing gold (#B7985B) stays as the single accent; serif headings replace Josefin Sans for editorial feel.
