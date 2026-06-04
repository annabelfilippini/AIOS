# Redesign Spec — Frita Batidos Homepage (Ann Arbor primary)

**Date:** 2026-04-19
**Path:** Path 2 — blue/white/futuristic palette; 4 editorial refs contribute layout/type/motion only.
**Prospect vertical:** Restaurant / Hospitality (Premium casual, chef-driven, multi-location).
**Audit findings this mockup must visibly address:** menu-as-PNG, awards-as-banner-image, halal buried in body text, multi-location confusion, photos without alt text, no dedicated best-burger/halal/happy-hour content, site was 503 (now up — show it can be beautiful).

---

## Design Library References

**Vertical:** Restaurant → Premium Casual, chef-driven, multi-location. Not fine dining (King), not British heritage (Bull & Last), not farm-to-table Latin (La Semilla), not rooftop luxury (Rare Bird). Frita's positioning is **college-town iconic, award-winning, chef-driven, Cuban-inspired counter service.**

**Execution cues (extracted from 4 refs + design-library.md):**

1. **Hero pattern** — Full-bleed food-as-art photography with centered serif display headline. Cool color grade (blue-leaning), not warm. Subtle parallax on scroll. Scroll indicator ("Taste it ↓" in Inter micro-caps).
2. **Type pair** — Fraunces (variable serif display) for headlines + eyebrows' hero number treatments; Inter for body, UI, and small caps. Headlines uppercase with tight tracking on large sizes (lesson from Bull & Last); eyebrows 10–11px with 0.24em letter-spacing (lesson from Rare Bird).
3. **Social-proof treatment** — Single critic pull-quote woven into body copy (King) + press-logo strip with clickable links below (design-library canon). Not a card carousel.
4. **Motion discipline** — Parallax hero, marquee on awards strip, fade-in on section reveal, smooth-scroll anchor nav. Zero hover-flip cards, zero confetti, zero gradient backgrounds. Restraint everywhere except motion.
5. **Palette discipline** — Two-tone blue (navy #0E3A8A + signature mid-blue #3B7DD8), ice-blue tint #E8F1FB, paper #F7F9FC, ink #0A0F1C. Gold #D4A843 reserved for awards/press callouts (≤3 occurrences). NO warm creams, NO browns, NO wine.

**Anti-patterns (MUST NOT appear in mockup):**
- White card boxes with drop shadows.
- Emojis (knife-and-fork, sparkles, chef hat, flame).
- All-Inter sans-only display (kills editorial feel — prior mockup's failure).
- PDF-behind-a-button menu link.
- Stock Unsplash food photography (we have Frita's real shots — use them).
- Testimonial carousel cards.
- "Experience our cuisine" generic hero copy.
- Card-based menu with "Add to Cart" buttons (Frita is counter-service; no e-commerce UI).

---

## Brand DNA (must survive the redesign)

These are the fingerprints that make it Frita, not a generic "editorial restaurant mockup":

1. **Flower / 6-petal pinwheel mark** — appears in nav, hero signature block, location picker, footer.
2. **Exact tagline** `DO NOT REWRITE: "Cuban Inspired Street Food!"` (from Wayback homepage, verified).
3. **The frita hero shot** (IMG_1497-1.jpg — frita with shoestring fries on top + vibrant slaw bowl). This one image is the brand.
4. **Chef Eve Aronoff's voice** — Slow Food, halal, Great Lakes dairy, Michigan-first, Top Chef alum. Chef section is a narrative, not a bio.
5. **Award stack — 2014–2025 Michigan Daily Best Burger, 11 consecutive years.** Must live above the fold OR in fold #2. Never as a banner PNG.
6. **Three cities** — Ann Arbor (primary), Detroit, Brooklyn. Location picker.
7. **Picnic-bench communal seating personality** — casual, chef-driven, playful. Copy voice matches. No "Experience" or "Elevated" or "Journey."

---

## Section Inventory (Spec Order) — every section maps to an audit finding

### SECTION 1 — Announcement Bar
**Layout:** Thin (36px) full-width bar above nav. Ink background #0A0F1C, ice-blue text, centered.
**Content:** `DO NOT REWRITE: "All chicken & beef certified Halal · Online ordering via Toast · (734) 761-2882"`
**Audit tag (top-right of bar, small pill, gold):** `DO NOT REWRITE: "NEW — Audit #1"` (addresses: halal buried, no structured callout)
**Motion:** Static. Persistent.

---

### SECTION 2 — Navigation
**Layout:** Sticky top, 72px tall, paper #F7F9FC background with backdrop-blur(14px). One row: flower mark + "FRITA BATIDOS" (left) | anchor nav (center: Food · Batidos · Chef · Locations · Press) | "Order Online" pill CTA (right, signature blue).
**Logo lockup:** `frita-flower.png` (28px) + wordmark "FRITA BATIDOS" in Fraunces 600, 15px, 0.14em tracking, navy.
**Reservation CTA:** `DO NOT REWRITE: "Order Online"` → links to https://order.toasttab.com/online/fritabatidos
**Phone CTA (smaller, text-only):** `DO NOT REWRITE: "(734) 761-2882"` → tel: link
**Responsive:** Mobile collapses to hamburger SVG (not "☰" emoji).
**Audit tag (below nav right, subtle pill):** none — nav is structural, not a finding fix.

---

### SECTION 3 — Hero
**Layout:** Full-bleed 100vh. Background = `frita-IMG_1497-1.jpg` with 18% dark cool overlay (linear-gradient from rgba(10,15,28,0.35) top to rgba(14,58,138,0.25) bottom — keeps food legible, tints cool). Parallax: background translates at 0.5x scroll speed. Copy block horizontally centered, bottom-aligned at 64% viewport height.
**Eyebrow (11px Inter 600 uppercase, 0.28em tracking, ice-blue):** `DO NOT REWRITE: "CUBAN INSPIRED STREET FOOD · ANN ARBOR SINCE 2010"`
**Headline (Fraunces Italic 500, responsive 72→120px, white, line-height 1.0, tight -0.02em tracking):** `DO NOT REWRITE: "The frita."`
  (One dish. Name it. That's the brand.)
**Subhead (Fraunces 400, 22→28px, ice-blue, max-width 620px, line-height 1.4):** `DO NOT REWRITE: "Cuban-style chorizo burger, shoestring fries on top, a batido in the other hand. Ann Arbor's Best Burger eleven years running."`
**Primary CTA (pill, signature blue bg, white text, Inter 600 14px):** `DO NOT REWRITE: "See the menu"` → #menu
**Secondary CTA (text link, white, underline):** `DO NOT REWRITE: "Order Online"` → Toast link
**Scroll indicator (bottom center, 24px above edge):** small Inter eyebrow `DO NOT REWRITE: "TASTE IT"` + 1px vertical line 44px tall fading to transparent. Animates a 12px dot falling then resetting every 2.4s.
**Audit tag (top-right of hero, gold pill, 12px Inter 600):** `DO NOT REWRITE: "NEW — Audit #2"` (addresses: site was 503 → usable hero; replaces banner-image awards with typographic claim)

---

### SECTION 4 — Press/Awards Marquee
**Layout:** Full-width strip, 132px tall, navy background (#0E3A8A), ice-blue text. Auto-scrolling horizontal marquee at ~40s per loop, pause on hover. Each entry: publication name + year(s) + accolade, separated by small flower-mark dividers (`frita-flower.png` inverted to white, 18px).
**Entries (fence EACH — every string verbatim):**
  - `DO NOT REWRITE: "MICHIGAN DAILY · Best Burger · 2014–2025"`
  - `DO NOT REWRITE: "METRO TIMES · Best Cuban Restaurant · 2020–2024"`
  - `DO NOT REWRITE: "HOUR MAGAZINE · Best Specialty Burger · 2025"`
  - `DO NOT REWRITE: "THE LO TIMES · Best New Burger NYC · Frita Brooklyn"`
  - `DO NOT REWRITE: "YELP · #31 Top 100 Burger Spots · 2023"`
**Motion:** Marquee. Pause on hover. Respects `prefers-reduced-motion`.
**Audit tag (top-right of section, gold pill):** `DO NOT REWRITE: "NEW — Audit #3"` (addresses: awards-as-banner-image → structured, crawlable, linkable)

---

### SECTION 5 — The Frita (Signature Editorial)
**Layout:** Two-column, image-left 58% / text-right 42%. 1280px max-width. 140px vertical padding top/bottom. Image = `frita-IMG_7968-3.jpg` (alt frita with fried egg, close-up). Cool-grade filter applied via CSS (hue-rotate(-8deg) saturate(0.92) — subtle). Text column left-aligned, ragged right.
**Eyebrow (Inter 600 11px uppercase, 0.28em tracking, signature blue):** `DO NOT REWRITE: "THE DISH"`
**Headline (Fraunces 500, 52→68px, navy, line-height 1.05):** `DO NOT REWRITE: "A Cuban-style burger, shoestring fries on top."`
**Body (Inter 400, 18px, ink-soft #1F2937, line-height 1.65, max-width 480px):**
  Paragraph 1: Explain the frita — chorizo or beef or chicken or black bean or fish, topped with crispy shoestring fries, served on a soft egg bun. Melted Muenster from Great Lakes dairy. Reference the shoestring-fries-on-top signature.
  Paragraph 2: `DO NOT REWRITE: "All chicken and beef is certified Halal."` (bold this line inline — audit #4)
**Critic pull-quote (Fraunces Italic 400, 28px, navy, 56px left border — 2px signature blue bar):** `DO NOT REWRITE: "The best (Cuban) burger isn't in Miami, it's in Ann Arbor. This is one of the best burgers possible!"`
**Attribution (Inter 500 13px, 0.1em tracking, ink-soft):** `DO NOT REWRITE: "— Ali Khan, Cheap Eats (Cooking Channel)"`
**CTA (text link with arrow, Inter 600 14px, signature blue, underline on hover):** `DO NOT REWRITE: "See the full menu →"` → #menu
**Audit tag (top-right of image, gold pill):** `DO NOT REWRITE: "NEW — Audit #4"` (addresses: halal buried in body text → surfaced in signature section)

---

### SECTION 6 — Menu Preview (Fritas + Batidos, HTML not PNG)
**Layout:** Two-column grid. Left column = "FRITAS" heading + 5-item list. Right column = "BATIDOS" heading + 3-item list. No card boxes. Items separated by 1px hairline borders. 1200px max-width, 120px vertical padding. Paper #F7F9FC background.
**Section eyebrow (Inter 600 11px uppercase, 0.28em tracking, signature blue, centered):** `DO NOT REWRITE: "THE MENU · ANN ARBOR"`
**Section headline (Fraunces 500, 52→68px, navy, centered):** `DO NOT REWRITE: "What we serve"`
**Section sub (Inter 400 16px ink-soft, centered, max-width 560px):** One line on sourcing philosophy — reference: "We strive to source our meat, cheese and produce from Michigan or the Midwest whenever possible."

**Left column — "FRITAS" (Fraunces 600 24px uppercase navy, 0.08em tracking):**
Each row: item name (Fraunces 500 20px ink) + diet badge (Inter 600 10px pill, ice-blue bg, navy text) + one-line description (Inter 400 14px ink-soft).
  1. `DO NOT REWRITE: "Chorizo Frita"` — badge: `DO NOT REWRITE: "HALAL"` — desc: "The original. House-made chorizo, soft egg bun, shoestring fries on top."
  2. `DO NOT REWRITE: "Beef Frita"` — badge: `DO NOT REWRITE: "HALAL"` — desc: "Halal beef patty with Muenster and crisped plantains."
  3. `DO NOT REWRITE: "Chicken Frita"` — badge: `DO NOT REWRITE: "HALAL"` — desc: "Grilled halal chicken with tropical slaw."
  4. `DO NOT REWRITE: "Black Bean Frita"` — badge: `DO NOT REWRITE: "VEGETARIAN"` — desc: "House-made black bean patty, avocado spread optional."
  5. `DO NOT REWRITE: "Fish Frita"` — badge: none — desc: "Whitefish, tropical slaw, garlic cilantro aioli."

**Right column — "BATIDOS" (Fraunces 600 24px uppercase navy):**
  1. `DO NOT REWRITE: "Coconut Cream Batido"` — desc: "Tropical milkshake, shredded coconut, condensed milk."
  2. `DO NOT REWRITE: "Chocolate Espanol Batido"` — desc: "Dark chocolate, cinnamon, whole milk."
  3. `DO NOT REWRITE: "Cajeta Batido"` — desc: "Mexican caramel, vanilla, crushed ice."

**CTA row (centered below grid, 40px space above):**
  Primary: `DO NOT REWRITE: "Order Online →"` (pill, signature blue) → Toast
  Secondary (text link, navy underline on hover): `DO NOT REWRITE: "Download the bar menu PDF"` → links to AA-BAR-UPDATED.png fallback

**Audit tag (top-right of section, gold pill):** `DO NOT REWRITE: "NEW — Audit #5"` (addresses: PNG menu → readable HTML + MenuItem schema capable)

---

### SECTION 7 — Chef Story (Eve Aronoff)
**Layout:** Asymmetric. Image-right 44%, text-left 56%. Image = `frita-background_eve.jpg` (B&W chef portrait) with a duotone CSS filter overlay (navy → ice-blue, 70% opacity — keeps the portrait but shifts to cool palette). 1280px max-width, 140px vertical padding.
**Eyebrow (Inter 600 11px uppercase, 0.28em tracking, signature blue):** `DO NOT REWRITE: "THE CHEF"`
**Headline (Fraunces Italic 500, 52→68px, navy, line-height 1.05):** `DO NOT REWRITE: "Chef Eve Aronoff built Frita around one idea:"`
**Sub-headline (Fraunces 500, 36→48px, signature blue, continuation):** `DO NOT REWRITE: "source it here, serve it right."`
**Body (Inter 400, 18px, ink-soft, line-height 1.65, max-width 500px):**
  Paragraph 1: Top Chef Season 6 alum. Opened Frita in 2010 after running Eve the Restaurant in Kerrytown. Slow Food advocate.
  Paragraph 2: `DO NOT REWRITE: "We strive to source our meat, cheese and produce from Michigan or the Midwest whenever possible."` (indented pull-quote, Fraunces Italic 22px)
  Paragraph 3: Second location opened in Detroit. Newest: Brooklyn.
**Stat strip (below body, 3 columns, 56px gap, Inter 600):**
  Stat 1: big number "15" (Fraunces 48px navy) + label "YEARS OPEN" (Inter 600 11px, 0.2em tracking, ink-soft)
  Stat 2: big number "3" + label "CITIES"
  Stat 3: big number "11" + label "BEST BURGER YEARS"
**Audit tag (top-right of image, gold pill):** `DO NOT REWRITE: "NEW — Audit #6"` (addresses: Person schema / chef entity not in AI knowledge graphs)

---

### SECTION 8 — Press (Critic Grid)
**Layout:** 3-column grid of critic pull-quotes, no cards, 1px hairline dividers between. 1200px max-width. Ice-blue #E8F1FB background strip (feels like a magazine interior spread). 140px vertical padding.
**Section eyebrow (centered):** `DO NOT REWRITE: "WHAT CRITICS SAY"`
**Section headline (Fraunces 500, 52→68px, navy, centered):** `DO NOT REWRITE: "Not just a burger."`

**Quote 1 (Fraunces Italic 400 22px, navy, line-height 1.4):** `DO NOT REWRITE: "If there's one restaurant you won't want to miss, it's Frita Batidos, a Cuban restaurant in the heart of downtown Ann Arbor."`
  Attribution: `DO NOT REWRITE: "— Intelligent Travel, National Geographic"`

**Quote 2:** `DO NOT REWRITE: "To find a good burger, see where students are eating. The Cuban-style spot is a college-town favorite."`
  Attribution: `DO NOT REWRITE: "— USA Today"`

**Quote 3:** `DO NOT REWRITE: "Frita Batidos is firing on all the current trend cylinders, from the fast casual, order-at-the-counter service style and the clean, modern decor to the Latin-linked flavors and value messaging."`
  Attribution: `DO NOT REWRITE: "— Ron Ruggless, Nation's Restaurant News"`

**Audit tag (top-right of section, gold pill):** `DO NOT REWRITE: "NEW — Audit #7"` (addresses: awards/press not structured → real critics, real attributions, Schema.org/Review-ready)

---

### SECTION 9 — Three Cities (Location Picker)
**Layout:** 3-column equal-width cards (but no card boxes — just image + text stacked). 1280px max-width. 120px vertical padding. Between cards: 40px gap. White background.
**Section eyebrow (centered, Inter 600 11px uppercase, 0.28em tracking, signature blue):** `DO NOT REWRITE: "FIND US"`
**Section headline (Fraunces 500, 52→68px, navy, centered):** `DO NOT REWRITE: "Three cities, one frita."`

**Card 1 — Ann Arbor:**
  Image: `frita-FRITA-SPACE2.jpg` (interior — white brick + BATIDOS sign) OR `frita-FRITAANNARBOR.png` fallback, aspect 4:5 landscape-crop.
  Eyebrow (Inter 600 11px uppercase, 0.24em tracking, signature blue): `DO NOT REWRITE: "THE ORIGINAL · SINCE 2010"`
  Name (Fraunces 600 32px navy): `DO NOT REWRITE: "Ann Arbor"`
  Address line (Inter 400 15px ink-soft): `DO NOT REWRITE: "117 W Washington St, Ann Arbor, MI 48104"`
  Hours (Inter 400 15px ink-soft): `DO NOT REWRITE: "Mon–Thu & Sun · 11AM–11PM · Fri–Sat · 11AM–12AM"`
  Phone (Inter 500 15px navy, tel: link): `DO NOT REWRITE: "(734) 761-2882"`
  CTA row (2 small links): `DO NOT REWRITE: "Get directions →"` (Google Maps) · `DO NOT REWRITE: "Order online →"` (Toast)

**Card 2 — Detroit:**
  Image: `frita-FRITADETROIT.png` (location logo as placeholder, aspect 4:5)
  Eyebrow: `DO NOT REWRITE: "DOWNTOWN DETROIT"`
  Name: `DO NOT REWRITE: "Detroit"`
  Address: `DO NOT REWRITE: "66 W. Columbia, Detroit, MI 48201"`
  Hours: `DO NOT REWRITE: "See location page for current hours"` (we do NOT fabricate hours we haven't verified)
  Phone: none (not in verified-facts)
  CTA: `DO NOT REWRITE: "Visit the Detroit location →"` → /detroit/

**Card 3 — Brooklyn:**
  Image: `frita-fritabknew-23.png` (Brooklyn logo placeholder, aspect 4:5)
  Eyebrow: `DO NOT REWRITE: "NEW · BROOKLYN NY"`
  Name: `DO NOT REWRITE: "Brooklyn"`
  Address: `DO NOT REWRITE: "See location for address"` (we have not verified a street address)
  Accolade line (replaces hours, Fraunces Italic 14px, ink-soft): `DO NOT REWRITE: '"Best New Burger NYC" — The Lo Times'`
  CTA: `DO NOT REWRITE: "Coming online soon →"` (placeholder — do not invent URL)

**Audit tag (top-right of section, gold pill):** `DO NOT REWRITE: "NEW — Audit #8"` (addresses: multi-location confusion → clear picker, distinct per-location LocalBusiness schema-ready)

---

### SECTION 10 — Halal Callout
**Layout:** Full-width band, ice-blue #E8F1FB background. 120px vertical padding. Two columns: left = icon + headline + body (66%), right = FAQ list (34%).
**Eyebrow (Inter 600 11px uppercase, 0.28em tracking, signature blue):** `DO NOT REWRITE: "DIETARY"`
**Headline (Fraunces 500, 44→56px, navy):** `DO NOT REWRITE: "Halal — always, not asterisk-always."`
**Body (Inter 400 18px ink-soft, max-width 560px):** `DO NOT REWRITE: "All chicken and beef at Frita Batidos is certified Halal. The chorizo frita, beef frita, and chicken frita all qualify. Vegetarian options include the Black Bean Frita, Plantain Chips, Mexico City Corn, and Crisped Plantains."`
**FAQ list (right column, 3 questions, Fraunces 500 20px + Inter 400 15px answer, each separated by 1px hairline):**
  - Q: `DO NOT REWRITE: "Is Frita Batidos halal?"`
    A: `DO NOT REWRITE: "Yes. All chicken and beef is certified Halal."`
  - Q: `DO NOT REWRITE: "What is a frita?"`
    A: `DO NOT REWRITE: "A Cuban-style burger, typically chorizo, topped with crispy shoestring fries on a soft egg bun."`
  - Q: `DO NOT REWRITE: "Do you take reservations?"`
    A: `DO NOT REWRITE: "No. Counter service, walk-in only."`
**Audit tag (top-right, gold pill):** `DO NOT REWRITE: "NEW — Audit #9"` (addresses: halal missing from FAQPage schema / AI halal queries return zero)

---

### SECTION 11 — Instagram Strip (live-feel social proof)
**Layout:** Full-width, 6 square tiles in a row. 180px each. No card boxes. 64px vertical padding. Navy background #0E3A8A, ice-blue accent on eyebrow.
**Eyebrow (centered, Inter 600 11px uppercase, 0.28em tracking, ice-blue):** `DO NOT REWRITE: "@FRITABATIDOS · INSTAGRAM"`
**Headline (Fraunces 500 36px, white, centered):** `DO NOT REWRITE: "See what's on the pass."`
**Tiles:** 6 square food/interior photos from Frita's own inventory — reuse from `mockups/assets/` (bowl, batido, drinks, snack, etc. from Yelp fallback + IMG_1497 cropped + IMG_7968 cropped + IMG_8534 interior). All square-cropped. Hover: subtle 1.04 scale.
**CTA (centered below tiles, Inter 500 14px ice-blue, underline on hover):** `DO NOT REWRITE: "Follow @fritabatidos on Instagram →"` → https://www.instagram.com/fritabatidos/
**Audit tag (top-right, gold pill):** `DO NOT REWRITE: "NEW — Audit #10"` (addresses: no social-proof pattern on site, 1,991 Yelp photos invisible)

---

### SECTION 12 — Footer
**Layout:** Full-width, ink #0A0F1C background, ice-blue text. 3 columns + bottom nav. 1280px max-width, 100px top padding, 40px bottom.
**Column 1 — Frita lockup:** flower.png (40px) + "FRITA BATIDOS" Fraunces 600 22px + tagline `DO NOT REWRITE: "Cuban Inspired Street Food!"` in Caveat/Homemade Apple 22px, ice-blue at 70% opacity.
**Column 2 — Visit:**
  Heading (Fraunces 600 14px uppercase tracked): `DO NOT REWRITE: "VISIT"`
  Lines (Inter 400 15px): address, phone (tel:), hours (Mon–Thu & Sun 11–11; Fri–Sat 11–12a), Get Directions link.
**Column 3 — Order + Follow:**
  Heading: `DO NOT REWRITE: "CONNECT"`
  Lines: Order Online (Toast), Catering, Gift Cards (Toast), Instagram, Facebook, Yelp.
  Social icons: inline SVG (Instagram, Facebook, Yelp) — 18px, ice-blue, hover white.
**Bottom nav strip (56px tall, hairline above, separated):** legal copy (© 2026 Frita Batidos · All rights reserved) + anchor links (Food, Batidos, Chef, Locations, Press) in Inter 400 13px.

---

## Copy Voice Rules

1. **Named, not abstract.** "The frita." wins over "Our signature sandwich." Use dish names wherever possible.
2. **Confident, not shouty.** 11-year streak is stated matter-of-fact ("Ann Arbor's Best Burger eleven years running"), not exclamation.
3. **Never use:** "Experience," "Elevated," "Journey," "Curated," "Artisan," "Handcrafted," "Discover," "Welcome."
4. **Sourcing language must match Chef Eve's actual statements.** "Sourced from Michigan or the Midwest whenever possible" is verified — paraphrasing risks losing "whenever possible."
5. **Halal is stated bluntly** in body and in FAQ and in menu badges — three placements per audit #9.
6. **No emojis anywhere.** Flower mark SVG is the only ornament.

---

## Image Usage Plan

| Image file (in `mockups/assets/`) | Used at | Purpose |
|---|---|---|
| `frita-IMG_1497-1.jpg` (5184x3456) | Section 3 (Hero) | Primary hero — frita + fries + slaw bowl |
| `frita-IMG_7968-3.jpg` (4272x2848) | Section 5 (The Dish) | Signature close-up (fried egg frita) |
| `frita-IMG_8534.jpg` (4272x2848) | Section 11 (Instagram strip tile) | Interior BATIDOS letters — atmospheric |
| `frita-background_batidos.jpg` | Section 11 tile | Drinks shot |
| `frita-background_eve.jpg` (B&W) | Section 7 (Chef) | Duotone-treated portrait |
| `frita-FRITA-SPACE2.jpg` | Section 9 Ann Arbor card | Interior shot |
| `frita-FRITAANNARBOR.png` | Section 9 AA fallback | Location lockup |
| `frita-FRITADETROIT.png` | Section 9 Detroit card | Location lockup |
| `frita-fritabknew-23.png` | Section 9 Brooklyn card | Location lockup |
| `frita-flower.png` (transparent) | Nav, footer, award marquee dividers | Brand mark |
| `frita-logo.png` | Footer secondary lockup | Wordmark |
| Existing Yelp images (frita-batido-yelp, frita-bowl-yelp, frita-coconut-batido-yelp, frita-drinks-yelp, frita-hero-yelp, frita-snack-yelp) | Section 11 Instagram tiles | Supplementary tiles |

**Every image used must have descriptive alt text** (audit finding: photos without alt text).

---

## Typography Load Plan

```
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600;700&family=Caveat&display=swap" rel="stylesheet">
```

- Fraunces: variable, optical-size capable, editorial serif. Italic 500 for hero headline.
- Inter: body, UI, micro-caps.
- Caveat: tagline accent only (footer). One place total.

---

## CSS Variables (color tokens)

```css
:root {
  --navy: #0E3A8A;
  --blue: #3B7DD8;
  --ice: #E8F1FB;
  --white: #FFFFFF;
  --paper: #F7F9FC;
  --ink: #0A0F1C;
  --ink-soft: #1F2937;
  --gold: #D4A843;
  --hairline: rgba(10, 15, 28, 0.09);
}
```

---

## Motion Spec

- **Hero parallax:** background `translateY(calc(var(--scroll) * 0.5))` on scroll. JS listener or CSS scroll-driven animation.
- **Scroll indicator:** 12px dot animates `translateY(0 → 44px)` over 2.4s ease-in-out, resets with opacity 0 → 1. Infinite.
- **Awards marquee:** `animation: scroll-x 40s linear infinite;` Pauses on `:hover`. Respects `@media (prefers-reduced-motion: reduce)` with animation-play-state: paused.
- **Section fade-in reveal:** IntersectionObserver at 12% visibility threshold. Each section gets `opacity: 0 → 1` and `translateY(24px → 0)` over 700ms ease-out. Once only.
- **Button hover:** signature-blue pill darkens to navy on hover over 180ms.
- **Instagram tile hover:** `scale(1 → 1.04)` over 240ms cubic-bezier(.4,0,.2,1).
- **Nav scroll-collapse:** none (stays fixed, backdrop-blur constant).

---

## Accessibility Baseline

- Contrast: navy-on-paper ≥ 12:1. Ice-blue-on-navy ≥ 4.7:1 (AA Large). All body text AA at 4.5:1 min.
- Every image has `alt=""`. Decorative marks (flower divider in marquee) use `alt=""` empty per WAI rules; content images get descriptive alt (e.g., "Chorizo frita with shoestring fries served on banana leaf").
- Nav is `<nav role="navigation">`, sections use semantic `<section>` with `<h2>` per section.
- Skip-to-content link at top (visually hidden until focused).
- Buttons are `<button>` or `<a>` with `role="button"` — never div onclick.
- All `@media (prefers-reduced-motion: reduce)` paths kill parallax + marquee + reveal.

---

## Responsive Breakpoints

- **Desktop ≥ 1200px:** Full 2-column / 3-column layouts, 1280px max-width container.
- **Tablet 768–1199px:** Sections remain 2-col but tighter gaps, hero font scales to 84px, marquee speed unchanged.
- **Mobile < 768px:**
  - Nav collapses to hamburger SVG (NOT text "☰" character; inline `<svg viewBox="0 0 24 24">` with 3 lines).
  - 2-col sections stack (image always first).
  - 3-col menu, location picker, critic grid all stack to 1 col.
  - Hero headline scales to 52px, subhead 18px.
  - Awards marquee halves speed (80s) since less horizontal distance.
  - Instagram strip collapses from 6 tiles to 3 rows of 2.
  - Announcement bar text reduces to 11px, may 2-line.
  - 24px horizontal padding everywhere.

---

## Page-level Meta + SEO

- `<title>`: `DO NOT REWRITE: "Frita Batidos — Cuban Inspired Street Food | Ann Arbor, Detroit, Brooklyn"`
- `<meta description>`: `DO NOT REWRITE: "Chef Eve Aronoff's Cuban-inspired counter-service kitchen. Home of the frita — a chorizo burger with shoestring fries on top. Ann Arbor's Best Burger 11 years running. All chicken and beef certified halal. Locations in Ann Arbor, Detroit, and Brooklyn."`
- `<link rel="canonical">`: https://fritabatidos.com/ann-arbor/
- `<meta property="og:*">`: title + description above + og:image = IMG_1497 hero.
- Include Restaurant JSON-LD (from audit.md) inside `<head>` (supports audit #5 indirectly). Include FAQPage JSON-LD (from audit.md) inside `<head>` (supports audit #9).

---

## Audit-Finding-to-Section Traceability

| Audit Finding | Section addressed | Audit-pill# |
|---|---|---|
| Halal certification buried / no structured callout | Announcement bar + Section 5 bold line + Section 10 FAQ | #1, #4, #9 |
| Site was 503 / no usable landing | Section 3 (hero exists) | #2 |
| Awards as banner PNG / not machine-readable | Section 4 (marquee with real text) | #3 |
| Menu as PNG / AI can't parse | Section 6 (HTML menu + badges) | #5 |
| Person schema missing for Eve Aronoff | Section 7 (chef entity narrative) | #6 |
| Press not structured / one-line mentions | Section 8 (3 critic pull-quotes, attributed) | #7 |
| Multi-location confusion / no picker | Section 9 (three-city picker) | #8 |
| No halal landing / halal FAQs | Section 10 (dedicated halal callout with FAQs) | #9 |
| No social-proof pattern / 1,991 Yelp photos invisible | Section 11 (Instagram strip) | #10 |

Every audit-pill position MUST NOT overlap any button, link, CTA, logo, or form element (QA A-check).

---

## Phase B Agent Brief (next step — for reference)

Build `prospects/frita-batidos/mockups/homepage-redesign.html` from this spec.

Sources of truth (in priority order):
1. This spec (`redesign-spec.md`)
2. `facts/verified-facts.md` (only facts allowed; no fabrication)
3. `branding.json` (colors + fonts locked)
4. `audit.md` (what to fix)
5. `reference/reference-summary.md` (style cues)
6. `mockups/assets/frita-*.{jpg,png}` (all local)

Hard rules:
- Every `DO NOT REWRITE:` string appears byte-for-byte.
- Zero facts outside `verified-facts.md`. Missing → softer language, never invent.
- No emojis. No text social icons. No `lh3.googleusercontent.com`. No hotlinks.
- All images served from `mockups/assets/` relative paths.
- Exactly one nav above hero.
- Motion spec wired. `prefers-reduced-motion` respected.
- Responsive @768px confirmed via visual check.
- Audit-pill QA: no collisions with interactive elements.
- Run QA Phase 4 checklist to green BEFORE returning.
