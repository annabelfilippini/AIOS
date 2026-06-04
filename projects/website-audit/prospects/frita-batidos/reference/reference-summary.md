# Reference Sites — Frita Batidos (Path 2 — Apr 19 2026)

**Path 2 direction (Annabel, 2026-04-19):** Keep Frita's blue/white/futuristic palette. The 4 refs below contribute **layout, typography discipline, motion, and social-proof treatment** only. Their warm/earthy/hospitality-heritage palettes do NOT transfer.

**One-line synthesis:** Four refs are united by editorial restraint, serif display type, full-bleed food-as-art photography, confident whitespace, and restrained motion. Frita inherits the structure, inverts the palette to cool tones, and adds smooth motion as its one differentiator.

---

## Rare Bird Rooftop — https://www.rarebirdrooftop.com/nashville
**Scraped:** `reference/rare-bird/` — screenshot + markup + computed styles.

**STEAL (execution only):**
- 3-column info strip: `LOCATION / HOURS / MENU` with tiny uppercase eyebrow (10px, 4px letter-spacing) over centered serif values. Answers visitor's practical questions without cluttering the hero.
- Full-bleed hero photo + scroll indicator ("Scroll" + caret).
- Display serif with very tight line-height (~100%) at large sizes (~120px on desktop).
- Generous whitespace between sections — airiness as luxury cue.

**AVOID for Frita:**
- Whispered lowercase serif headlines. Frita's identity is loud, playful, award-winning — going quiet would erase the edge.
- Zero social proof. Frita has 11 Best Burger awards + 5 press quotes + 2,521 Yelp reviews — must be visible.

---

## The Bull & Last — https://thebullandlast.co.uk/pages/menus
**Scraped:** `reference/bull-and-last/` — screenshot + markup + computed styles.

**STEAL (execution only):**
- **Unified heading treatment** — one display font for EVERY heading, always uppercase, always tight-tracked (negative letter-spacing on large sizes). Creates a confident brand voice across sections.
- Full-bleed hero with centered uppercase serif headline + a small ornamental divider (we sub the flower mark).
- Alternating image-left / text-right rhythm for narrative sections.

**AVOID for Frita:**
- Sparse hospitality restraint: tiny beige buttons, beige-on-beige, Instagram CTA as only social proof. Frita SHOUTS its awards; this site whispers.
- British-pub typographic flourishes (sparkle dividers). We keep the flower mark as the only ornament.

---

## King NYC — https://kingrestaurant.nyc/
**Scraped:** `reference/king-nyc/` — screenshot + markup + computed styles.

**STEAL (execution only):**
- **Single critic pull-quote woven into body copy.** More credible than a logo wall. For Frita: pull one punchy sentence from each major critic (Ali Khan, Nat Geo, USA Today, Chicago Tribune, Ann Arbor Observer).
- Letter-spacing as hierarchy (not just size). Tracking wide on eyebrows, tight on display.

**AVOID for Frita:**
- Ultra-narrow 400px single-column — kills Frita's energy instantly.
- Monochromatic all-serif austerity (Adobe Garamond everywhere, zero motion). Frita sells beach-party burgers, not hushed fine dining.

---

## La Semilla — https://www.lasemilla.kitchen/
**Scraped:** `reference/la-semilla/` — screenshot + markup + computed styles.

**STEAL (execution only):**
- **Live Instagram strip above footer.** Social proof + proof-of-life + secondary content in one. Frita has strong IG content across locations. Auto-updating.
- Scroll indicator in hero (subtle motion cue).
- Letter-spaced uppercase eyebrow as section orienter.

**AVOID for Frita:**
- Decorative patterned tile borders. La Semilla is Latin-earthy (Mexican-tile motifs); Frita is Cuban-cool (blue/white). Ornate frames would read cliché.
- Multi-font maximalism (4 distinct type families). Frita uses one serif display + Inter, nothing else.

---

## Design-library cues drawn from `wiki/wiki/design-library.md` (Restaurant vertical)

- Hero = ONE food photo, full-bleed. Not grid, not carousel. (All 4 refs confirm.)
- Menu on-site as readable HTML with MenuItem schema — never PDF-behind-a-button. (Audit finding: Frita's PNG menus are invisible to AI.)
- Hours + address + order CTA above the fold AND in footer.
- Press/awards as real publication logos with clickable links (not banner images).
- Typography pair: distinctive serif (editorial) + clean sans (UI). Never all-sans-Montserrat.

## Anti-patterns from design-library (must not appear)

- White card boxes with drop shadows — #1 AI-generated dead giveaway.
- Emojis (knife-and-fork, sparkles, chef hat).
- "Experience our cuisine" generic hero copy.
- Three-column feature grids borrowed from SaaS templates.
- Stock food photography.

## What Frita must do that the 4 refs DON'T

- **Motion.** All 4 refs are essentially static. Frita's "futuristic" brief means Frita's single signature motion is the differentiator: parallax on hero, marquee on awards strip, fade-in on reveal, and smooth scroll on anchor nav. Restraint on everything else.
- **Announce the 11-year streak.** No ref has a comparable award stack. Frita's hero subhead or second-fold section must lead with the 2014–2025 Michigan Daily Best Burger claim.
- **Structured halal.** Audit finding: "halal restaurant ann arbor" returns zero results for Frita. Dedicated halal callout with FAQPage-schema-worthy content.
- **Three-city navigation.** No ref has multi-location pressure. Frita has AA + Detroit + Brooklyn — location picker above fold.
