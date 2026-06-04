# Mani Osteria — Redesign Direction
Date: 2026-04-21. Feeds into index.html in this folder.

## Annabel's verbatim ask
> "I like https://www.viacarota.com/ because of the images below the initial image. I think Mani could look really good with that but I love how https://donangie.com/ looks when you first open it. The images are really pretty and appealing but I don't love how you can't scroll down to anything. Can you mix these a bit? Ensure that as you scroll the words appear like you did for Black Pearl."

## The mix
- **Don Angie's opener**: full-viewport hero image, centered wordmark, no text competing with the photo. Photo carries the emotion.
- **Via Carota's payoff**: dense grid of atmospheric restaurant images directly below the hero. Scroll reveals the warmth.
- **Black Pearl's motion**: scroll-triggered word reveals via `[data-reveal]` + `[data-reveal-group]` IntersectionObserver. Eyebrow → title → copy → CTA cascade in sequence.
- **Fix for Don Angie's weakness**: the page continues below the fold — about, menu, hours, reservations — all editorial, all photographed.

## Content architecture (top to bottom)
1. **Top bar** — minimal. MANI wordmark (left) · Menus / Reservations / Private Events / Visit (right). No reservations strip — Mani is 6+ only, put that in context.
2. **Hero** — full viewport height. Single image (mani-crostini.jpg, the 15-crostini board overhead — already editorial, already Mani's). Centered wordmark + one-line eyebrow. Small "Scroll" cue at bottom.
3. **Image grid** — 4×2 square grid, full-bleed. Mix of owned food photography + interior + exterior shots. No captions. Staggered reveal as they enter viewport.
4. **Welcome prose** — one line in large light serif (verbatim from site): "Wood-fired pizzas, handmade pastas, and signature antipasti — since 2011, on East Liberty." Three short paragraphs below.
5. **Menu preview** — three stacked rows (Pizza · Pasta · Antipasti), each with 3-4 dish names pulled from verified Yelp "Popular Dishes." Underlined CTA: "Full menu (PDF)" linking to the current PDF from homepage scrape.
6. **Dine in / Dine out** — two-column split. Left: reservation rules (6+ only, otherwise walk-in) + OpenTable link. Right: pickup via Toast + phone number.
7. **Visit** — hours list, address, phone. Photo to the right (exterior MANI signage). Big underlined "Make a Reservation" CTA.
8. **Events / Graduation 2027** — one short block, link to Google Form (graduation interest) and Tripleseat (private events). Don't bury this — Mani's key revenue driver is events.
9. **Footer** — address, phone, hours, social. Small MANI wordmark.

## Visual system
- **Palette**
  - Ink: `#1A1715` (warm near-black for body + headings)
  - Cream: `#F5EFE6` (background, warm off-white — replaces Mani's current pure white)
  - Gold: `#B7985B` (Mani's existing brand gold — KEEP, used sparingly for accents and one CTA underline)
  - Soft gray: `#8A8078` (captions, hours list secondaries)
- **Typography**
  - Headings: **Fraunces** (editorial serif, optical sizing, light-to-normal weight only). Replaces Josefin Sans.
  - Body: **Inter** (per Annabel's "Mockup Aesthetics" feedback — Inter over Montserrat, lighter weights).
  - Wordmark: Fraunces italic, tight letterspacing.
- **Motion**
  - `[data-reveal]` → `opacity: 0` + `translateY(24px)` → `opacity: 1` + `translateY(0)` over 700ms ease-out.
  - `[data-reveal-group]` → stagger children by 80ms.
  - Apply to: hero eyebrow + wordmark + scroll cue; every grid tile (fade + tiny scale); welcome prose paragraphs; menu sections; hours block.
  - One subtle kinetic touch: the "Scroll" cue in hero has a slow pulse (opacity 0.4 → 1 → 0.4 over 2.4s).
- **Photography**
  - Hero: mani-crostini.jpg (overhead 15-crostini board on wood — the one strong editorial food shot Mani owns).
  - Grid (8 tiles): mani-tomatoes, mani-cocktails, interior-1 (gold wall), interior-2 (pizza oven + wood stack), interior-3 (bar), interior-4 (packed room), outside-2 (MANI sign awning), dining-room.
  - Visit-section image: outside-1 (MANI signage with sky).
  - Yelp food close-ups with "Photo by Lena J" watermarks EXCLUDED — not licensed.
- **Spacing**
  - Hero: 100vh. Grid tiles: no gap between (tight-packed, editorial). Section padding: 160px top/bottom on desktop. Max content width: 1240px for prose, 100% for image grid.
- **No emojis.** Per feedback, never in web deliverables.

## What we keep from Mani's current site (elevate, don't erase)
- Gold brand color (#B7985B)
- "MANI" wordmark text treatment (lightweight, uppercase)
- Verbatim tagline ("Wood-fired pizzas, handmade pastas, and signature antipasti")
- Liberty St address + phone + Toast pickup + Tripleseat events flow
- Graduation programming callout

## What we fix
- Text-heavy gold stripe hero → photo-forward hero
- Buried food photography → image grid is the second viewport
- Disjointed sections → continuous editorial flow with motion
- Josefin Sans + Open Sans → Fraunces + Inter (editorial, not SaaS)
- FAQs + Jobs + map clutter → moved to footer / dedicated pages (not homepage)
- Every block in its own box → tighter, full-bleed editorial

## Hard rules (from prior feedback)
- No fabricated facts — every dish name, hour, phone came from verified-facts.md
- No emojis anywhere
- No watermarked third-party photos
- All CTAs either link to real PDFs/forms from scrape, or use `href="#"` with a clear label (no broken promises)
- Menu CTA links to the PDF scraped from homepage (MAN_DIN_20260414_v2.pdf)
- Reservation CTA: link to OpenTable with disclaimer "Parties of 6 or more — smaller parties walk in"
