# Culantro — Redesign Spec

**Target URL:** https://www.culantroperu.com/ (two locations: Ferndale + Ann Arbor)
**Mode:** Interactive. Stitch OFF (default per Apr 16 2026 decision). Agent-built from scratch.
**Date:** 2026-04-21

---

## Scope & Audit Findings

**In scope (this spec fixes):**
1. No hours anywhere on homepage → must surface per location above fold
2. No addresses on homepage → must surface per location above fold
3. No menu preview on homepage (two different external links: Square storefront for Ferndale, PDF for Ann Arbor) → must include on-page signature-dish teaser + PDF CTA per location
4. No reservations affordance → Ferndale CTA must link to reservations (OpenTable per scrape), Ann Arbor = "walk-in / order at counter" copy
5. No named signature dishes → hero must name pollo a la brasa / ceviche / lomo saltado etc.
6. No social proof → surface Yelp 4.2★ (Ferndale), 303 reviews, 2,895 FB likes, TripAdvisor quote
7. No story / owner content → the build-out/mural gallery becomes a narrative "Hand-crafted in Michigan" strip
8. Photo gallery has no hierarchy → editorial food strip for hero photos, separate mural/build strip for story
9. Current black background + tiny orange logo reads as low-budget → keep dark-warm palette but use rich terracotta/rust ground instead of pure black, elevate type hierarchy
10. No mobile-first layout → responsive stack at 768px

**Out of scope (not this mockup):**
- Dashboard / analytics preview (separate skill)
- Email / outreach draft (separate skill)
- Full menu transcription into HTML (PDF link is correct per /audit-redesign Phase 4 check #8)
- Press / awards callout — no press coverage found in scrape

---

## Design Library References

**Vertical:** Restaurant / Hospitality (casual-premium, owner-operator, two-location)

**Primary refs from library (restaurant/hospitality):**
- Quintonil → regional identity via restrained clay/terracotta, NOT kitschy cultural clichés (no llamas, no textile overlays). Direct lesson for Peruvian palette.
- Tacombi → street-food warmth + playful confidence, validates keeping a casual tier even while elevating.
- Cosme → modern-Latin editorial hero + chef storytelling pattern.
- Fat Cow → dark moody palette done right (from Hop Alley mapping) — proves dark backgrounds can feel premium when type + whitespace discipline holds.

**Prospect-specific refs (scraped for this run, see `reference/reference-summary.md`):**
- Cutler & Co → editorial restraint, bordered "specialty" blocks, centered vertical layout
- Mission Ceviche → two-location picker IA (Annabel's explicit anchor pattern)
- Gjelina → warm-cream multi-location hub with red-coral accent (bridges editorial + color)

**Execution cues (apply all):**
1. **Hero:** one full-bleed food photo (pollo a la brasa OR ceviche), named dish + origin city copy. No carousel. Warm color grade (not high-contrast).
2. **Type pair:** warm serif display (EB Garamond / Cormorant / Playfair) + clean humanist sans body (Inter). Never all-sans Montserrat.
3. **Two-location picker high on page:** Mission Ceviche pattern. Per-location card with photo + address + hours + Menu + Reserve CTAs.
4. **Signatures block:** Cutler-style bordered "From the Rotisserie" / "From the Sea" vertical list with dotted-leader pricing. Teaser, not full menu. "See full menu (PDF)" CTA below.
5. **Mural/process strip:** Horizontal photo strip turning Culantro's existing build-out gallery into a "Hand-crafted" narrative — elevates the noise into an identity moment.
6. **Social proof:** real Yelp rating + FB check-in count + one verified pull quote. Clickable. No fake stars.
7. **Palette discipline:** max 3 colors on page — rust/terracotta ground, cream type, single flame-orange accent. Culantro's gold logo preserved as-is at hero.

**Anti-patterns to avoid:**
- Generic "Experience our cuisine" hero copy. Use named dishes + neighborhood specifics ("Pollo a la Brasa. Ferndale + Kerrytown.")
- PDF-only menu with zero on-page teaser — pair PDF CTA with dish-name list.
- Menu as e-commerce product cards with "Add" buttons.
- Emojis (no 🌶️ 🔥 🍗 etc.). SVG icons only.
- Stock Unsplash food photography — Culantro has 400+ Yelp photos + their own gallery. Use the real ones.
- Llama/poncho/textile cultural cliché imagery.
- Carousel / slider heroes.

---

## Brand DNA (preserve these)

**Must-survive signature elements:**
- **Ornate gold/orange logo** — centerpiece of current homepage, keep as hero mark
- **Warm dark palette** — rust/terracotta background, NOT stark white or navy
- **Peruvian flame aesthetic** — pollo a la brasa fire shot is their strongest image
- **Hand-crafted mural identity** — door art, walls, signage are visible in gallery; keep as a narrative block
- **Bilingual confidence** — Spanish dish names used verbatim (Aji de Gallina, Patacones Picantes, Chicha Morada, Tres Leches)
- **Two-location pride** — "Downtown Ferndale and Downtown Ann Arbor" is their own Facebook positioning copy

---

## Palette (proposed — test in mockup)

- **Background:** `#2A1410` (deep rust) OR `#F5EEE3` (warm cream) — mockup uses rust-dominant with cream cards, per Gjelina × Fat Cow hybrid direction
- **Type primary (on rust):** `#F5EEE3` (warm cream)
- **Type primary (on cream blocks):** `#1A1410` (charcoal)
- **Accent CTA:** `#E8661F` (flame orange — slightly warmer than brand's #FF8924)
- **Gold preserve:** `#C59D5F` (brand primary — for section marks, logo, dividers)
- **Secondary accent:** `#B14B2D` (deep terracotta — underlines, hover states)

## Typography

- **Display (hero + section marks):** EB Garamond or Cormorant Garamond — warm serif, Italic for "Peruvian Eatery" type roles
- **Body / UI:** Inter (400, 500, 600)
- **Small caps section labels:** Inter with `letter-spacing: 0.12em`, all-caps — replaces current Alegreya Sans SC
- **Logo/wordmark:** keep existing Culantro SVG/PNG as-is — do not redraw

## Logo

- Use existing logo at `scrape/screenshots/homepage-desktop-full.png` crop OR download `https://www.culantroperu.com/img/culantro.png` to `mockups/assets/logo.png`
- Hero mark size: ~180px height. Nav mark size: ~44px height.

---

## Section Inventory (copy spec — build in this order)

### SECTION 1: NAV

- Left: Culantro wordmark (logo.png, 44px tall)
- Center-right links: `MENU` `LOCATIONS` `STORY` `RESERVE`
- Right CTA: `ORDER ONLINE` (pill button, flame-orange fill)
- Sticky on scroll, background with subtle rust/cream tint
- Menu link → `#locations` (because menu is per-location, the click scrolls to location picker)

### SECTION 2: HERO

Layout: full-bleed food photograph, content overlay bottom-left, warm color grade.

Eyebrow: `DO NOT REWRITE: "FERNDALE  +  ANN ARBOR"`
Headline: `DO NOT REWRITE: "The taste of Peru, hand-built in Michigan."`
Subhead: `DO NOT REWRITE: "Pollo a la Brasa from the rotisserie. Ceviche cured in fresh lime. Lomo Saltado over the fire. Two neighborhood spots, family-run."`
Primary CTA: `DO NOT REWRITE: "Choose a location"` → `#locations`
Secondary CTA: `DO NOT REWRITE: "See the menu"` → `assets/culantro-menu-ferndale.pdf` (target="_blank")

Image: hero photo of pollo a la brasa on the rotisserie (from Yelp Ferndale gallery — `https://s3-media0.fl.yelpcdn.com/bphoto/Qn8Xn6obKdzXCWCGjyrIuA/l.jpg` or similar) — agent picks most appetizing via shortlist.

Audit finding (internal): fixes #1, #2, #3, #5.

### SECTION 3: LOCATION PICKER ("Two spots. Pick yours.")

Layout: 2-up card grid. Each card = location photo header + info block + CTAs. On mobile, stack vertically.

Section label: `DO NOT REWRITE: "VISIT"`
Section headline: `DO NOT REWRITE: "Two spots. One kitchen. Pick yours."`

**Card 1 — Ferndale:**
- Photo: Culantro Ferndale storefront or interior (from Yelp Ferndale gallery — pick "Small, colorful space" interior shot or the exterior at `https://s3-media0.fl.yelpcdn.com/bphoto/mbVE3fCDVoCwU1zCm6imxw/l.jpg`)
- Name: `DO NOT REWRITE: "Ferndale"`
- Subtitle: `DO NOT REWRITE: "Flagship · Downtown"`
- Address: `DO NOT REWRITE: "22939 Woodward Ave, Ferndale, MI 48220"`
- Hours block (render as a small table):
  - `DO NOT REWRITE: "Mon–Wed  11am – 9pm"`
  - `DO NOT REWRITE: "Thu  11am – 10pm"`
  - `DO NOT REWRITE: "Fri  11am – 10pm"`
  - `DO NOT REWRITE: "Sat  12pm – 10pm"`
  - `DO NOT REWRITE: "Sun  12pm – 9pm"`
- Rating badge: `DO NOT REWRITE: "4.2 ★ · 303 Yelp reviews"` (linked to yelp page)
- CTA 1: `DO NOT REWRITE: "Menu"` → `assets/culantro-menu-ferndale.pdf` target="_blank"
- CTA 2: `DO NOT REWRITE: "Order online"` → `https://culantro.square.site/`
- CTA 3: `DO NOT REWRITE: "Directions"` → maps link for Woodward Ave address

**Card 2 — Ann Arbor:**
- Photo: Culantro Ann Arbor storefront (from Yelp Ann Arbor gallery — `https://s3-media0.fl.yelpcdn.com/bphoto/-UjOkGqvHQ_QMRftjhR2ng/l.jpg` main entrance)
- Name: `DO NOT REWRITE: "Ann Arbor"`
- Subtitle: `DO NOT REWRITE: "Kerrytown · Corner of Main & Miller"`
- Address: `DO NOT REWRITE: "223 N Main St, Ann Arbor, MI 48104"`
- Same hours block as Ferndale (identical schedule)
- Rating badge: `DO NOT REWRITE: "3.7 ★ · 65 Yelp reviews"` (linked)
- CTA 1: `DO NOT REWRITE: "Menu"` → `https://www.culantroperu.com/img/menu/MenuAnnArbor.pdf` target="_blank"
- CTA 2: `DO NOT REWRITE: "Order at counter"` (non-link, caption-style — per Yelp review: "Order at the counter and grab a seat. They bring it to you.")
- CTA 3: `DO NOT REWRITE: "Directions"` → maps link for N Main St address

Audit finding (internal): fixes #1, #2, #4.

### SECTION 4: SIGNATURES ("From the rotisserie")

Layout: Cutler-style bordered vertical list, cream card on rust ground. Centered max-width ~720px. Dotted-leader pricing. Dish name left, price right.

Section label: `DO NOT REWRITE: "SIGNATURES"`
Section headline: `DO NOT REWRITE: "Dishes we're known for."`

**Block A — "From the Rotisserie":**
- `DO NOT REWRITE: "Pollo a la Brasa — marinated overnight, charcoal-fired. Served with aji verde.   $18.70"`
- `DO NOT REWRITE: "Sandwich de Chicharrón — pork belly, sweet potato, salsa criolla on pan francés.   $18.40"`

**Block B — "From the Sea":**
- `DO NOT REWRITE: "Ceviche — fresh fish cured in lime, red onion, Peruvian corn, sweet potato.   $18.40"`
- `DO NOT REWRITE: "Arroz con Mariscos — shellfish-laden saffron rice, the Peruvian paella.   $22.40"`

**Block C — "From the Wok":**
- `DO NOT REWRITE: "Lomo Saltado — beef, red onion, tomato, soy, stir-fried over french fries.   $23.70"`
- `DO NOT REWRITE: "Arroz Chaufa — Peruvian–Chinese fried rice, our chifa classic.   $18.40"`
- `DO NOT REWRITE: "Tallarín Saltado — stir-fried noodles, tender beef, Peruvian aji.   $23.70"`

**Block D — "From the Home Kitchen":**
- `DO NOT REWRITE: "Aji de Gallina — shredded chicken in a creamy walnut-chili sauce. The dish that tastes like home.   $18.70"`
- `DO NOT REWRITE: "Seco a la Norteña — slow-braised beef in cilantro, served with canary beans + rice.   $21.10"`
- `DO NOT REWRITE: "Carne a la Plancha — grilled sirloin, salsa criolla, plantains.   $24.90"`

**Block E — "Sides & Sweets":**
- `DO NOT REWRITE: "Patacones Picantes — crispy green plantains, spicy dip.   $11.90"`
- `DO NOT REWRITE: "Yuca Frita — fried yuca, aji amarillo mayo."`
- `DO NOT REWRITE: "Tres Leches — three-milk cake, the dessert.   $10.50"`
- `DO NOT REWRITE: "Alfajores — dulce de leche between shortbread.   $5.30"`

CTA below blocks: `DO NOT REWRITE: "See the full Ferndale menu"` → `assets/culantro-menu-ferndale.pdf` target="_blank"
CTA (second line): `DO NOT REWRITE: "See the full Ann Arbor menu"` → `https://www.culantroperu.com/img/menu/MenuAnnArbor.pdf` target="_blank"

Audit finding (internal): fixes #3, #5.

### SECTION 5: HAND-CRAFTED STRIP ("Hand-crafted in Michigan")

Layout: Horizontal photo strip, 5-6 images in a row, hover-to-reveal caption pattern. Images pulled from Culantro's own gallery. Header block left-aligned above strip.

Section label: `DO NOT REWRITE: "STORY"`
Section headline: `DO NOT REWRITE: "Hand-crafted in Michigan."`
Section body: `DO NOT REWRITE: "Every wall painted, every sign carved, every rotisserie fired by a small family team. Ferndale opened in 2018. Ann Arbor followed — Kerrytown's newest corner kitchen. Peru on the plate. Michigan on the door."`

*Note: "opened in 2018" is SOFT — not verified. Agent should either remove the year claim or replace with "A few years in Ferndale. Still hand-crafted." If agent can verify via a quick WebFetch of the Facebook about section during build, great. Otherwise soften.*

**Image strip (use Culantro's own images from `https://www.culantroperu.com/img/gallery/`):**
- `AnnArbor-Before.jpg` — caption: `DO NOT REWRITE: "Ann Arbor, day one."`
- `AnnArbor-After.jpg` — caption: `DO NOT REWRITE: "Ann Arbor, finished."`
- `sign.jpg` — caption: `DO NOT REWRITE: "The sign, carved by hand."`
- `door.jpg` — caption: `DO NOT REWRITE: "The door, painted by a friend."`
- `walls.jpg` — caption: `DO NOT REWRITE: "Murals, Ferndale."`
- `oven.jpg` — caption: `DO NOT REWRITE: "The rotisserie. The heart."`

*Agent: download all six from `https://www.culantroperu.com/img/gallery/` to `mockups/assets/gallery/`. Verify each is >1200px wide; if smaller, use `https://www.culantroperu.com/img/gallery/` base URL (non-thumb).*

Audit finding (internal): fixes #7, #8.

### SECTION 6: SOCIAL PROOF ("What Michigan says")

Layout: 3-up pull quote row on cream card block. Each quote has attribution + source badge (Yelp star icon or TripAdvisor). No fabricated quotes — pull from verified-facts.md verbatim.

Section label: `DO NOT REWRITE: "REVIEWS"`
Section headline: `DO NOT REWRITE: "What Michigan says."`

**Quote 1 (Ferndale):**
- Quote: `DO NOT REWRITE: "Every single one was so flavorful and delicious. I particularly loved the tallarín saltado. The food is reasonably priced for a good portion as well."`
- Attribution: `DO NOT REWRITE: "Ashley T. · Yelp Elite · Troy, MI"`
- Source badge: Yelp 5-star SVG + "Ferndale"

**Quote 2 (Ferndale / displaced-LA):**
- Quote: `DO NOT REWRITE: "I used to frequent a Peruvian restaurant in Los Angeles and thought I'd never find it in Michigan — so I'm happy I found this place."`
- Attribution: `DO NOT REWRITE: "Yelp reviewer · Ferndale"`
- Source badge: Yelp SVG

**Quote 3 (Ann Arbor):**
- Quote: `DO NOT REWRITE: "The experience here was phenomenal. This restaurant deserves any attention it can get — it's one of the only genuine Latin American food spots in the area."`
- Attribution: `DO NOT REWRITE: "Yelp reviewer · Ann Arbor"`
- Source badge: Yelp SVG

Below row, stat strip:
- `DO NOT REWRITE: "4.2 ★ Yelp Ferndale"`  ·  `DO NOT REWRITE: "303 reviews"`  ·  `DO NOT REWRITE: "2,895 Facebook likes"`  ·  `DO NOT REWRITE: "2,492 check-ins"`

Audit finding (internal): fixes #6.

### SECTION 7: FIND US / FOLLOW ("Peruvian, the Michigan way")

Layout: Dark rust block with cream type. Split 60/40: left = social/IG promo, right = email newsletter or catering inquiry.

Section headline: `DO NOT REWRITE: "Peruvian, the Michigan way."`
Body: `DO NOT REWRITE: "Follow @eatculantro on Instagram for specials, private events, and the next hand-painted wall."`
IG CTA: `DO NOT REWRITE: "Follow on Instagram"` → `https://www.instagram.com/eatculantro/`
FB CTA: `DO NOT REWRITE: "We're on Facebook too"` → `https://www.facebook.com/culantroperu/`

(Right column): Contact card with a `DO NOT REWRITE: "Planning something bigger?"` headline and a single copy line: `DO NOT REWRITE: "We cater private events and large-party dinners. Reach out at info@culantroperu.com."` — email is SOFT (not verified). Agent may soften to just "Reach out via Instagram DM" if no email surface is confirmed in scrape. Check `scrape/homepage.md` + `facts/google-*.md` for any `@culantroperu.com` or `@` pattern before committing.

### SECTION 8: FOOTER

- Left: Culantro wordmark + short tagline `DO NOT REWRITE: "The taste of Peru, from Ferndale to Kerrytown."`
- Center: two address columns — Ferndale address + Ann Arbor address
- Right: nav links (Menu Ferndale / Menu Ann Arbor / Order Online / Reserve / Instagram / Facebook)
- Bottom strip: `DO NOT REWRITE: "© Culantro Peruvian Eatery. Family-owned, hand-built."` + small legal line if applicable

---

## Global requirements

- Responsive at 768px: nav collapses to hamburger (SVG), 2-col sections stack vertically, signatures block remains readable at mobile width, photo strip becomes horizontal scroll
- No audit-tag pills on the final mockup
- No emojis. SVG icons only (Instagram, Facebook, star for Yelp, map pin, arrow)
- Every image downloaded to `mockups/assets/` — zero hotlinks to yelpcdn / culantroperu.com
- Menu CTAs → PDFs, never to `#menu` anchor
- Max-width container: 1280px, with 1100px for text blocks
- Type scale: hero 72px display, H2 48px, H3 28px, body 17px/1.6
- Section padding: 120px top/bottom desktop, 72px mobile
- Smooth scroll on anchor links
- Hover states: CTAs transition `background-color` + subtle 2px `translateY`
- Image motion: hero food photo has a subtle 20s `ken burns` scale from 1.0 → 1.05
- Signatures block: borders animate in on scroll (Intersection Observer, opacity 0 → 1 + translateY)

---

## Asset collection plan (for agent)

**Priority 1 (Culantro's own):** Download from `https://www.culantroperu.com/img/`:
- `culantro.png` (logo)
- `rotisserie.jpg` (homepage hero background)
- `gallery/AnnArbor-Before.jpg`, `AnnArbor-After.jpg`, `sign.jpg`, `door.jpg`, `walls.jpg`, `oven.jpg`, `manager.jpg`, `facebook.jpg`

**Priority 2 (Yelp food/interior photos — real customer photos, public CDN):** Download from `https://s3-media0.fl.yelpcdn.com/bphoto/<id>/l.jpg` — list of candidate IDs from scrape:
- Pollo a la Brasa: `jsTeN1rCOOClSDGZgljnBA`, `Qn8Xn6obKdzXCWCGjyrIuA`, `rHixp86LqBPldTRu6bClMw`
- Lomo Saltado: `ezrD3BTdLCdwJw8D2ebA1g`, `4fdT-ehsdj7OlbqyTfVrHg`
- Ceviche: `s1rhs-dyWeyboZjIaInAGg`, `0HTdQo4kiUeWXjDjj8O5bA`
- Aji de Gallina: `oZM2cqqa3yrkT--cayOExg`, `9utQ8e4baeDJssAyL-l8iw`
- Arroz con Mariscos: `mBANDtxd2xhBbRy5xcLN1A`
- Patacones Picantes: `ulUjiyb786WBNcihl4WXcg`, `xVxhGISReTS-EDdL4W8g4g`
- Tres Leches: `QqOKNyC6xGlMHqvbXLJdCw`, `40KzNg2hTJOyro0r6v8sbg`
- Interior: `UjE5mH_3QatNOBkQf4AopA` (Booths, Ann Arbor), `9Qupug8wMmDVavQj7Zj5Yw` (colorful space, Ferndale)
- Exterior: `-UjOkGqvHQ_QMRftjhR2ng` (Ann Arbor main entrance), `mbVE3fCDVoCwU1zCm6imxw` (Ferndale outside)

**Priority 3 (from branding.json):** logo + favicon paths already resolved.

**Verify before placing (appetite test for hero):** shortlist 3-4 hero candidates from Pollo a la Brasa photos, pick the most visually appetizing (clear dish in frame, golden skin visible, not a top-down plate with too many sides). When in doubt pick the rotisserie-fire shot from Culantro's own site (`rotisserie.jpg`).

---

## Out-of-scope reminders

- No founder portrait slot in this mockup — we don't have a real portrait of Betty S. or the owner-operator team on file. If a "Meet the team" section were added, it would need the dashed-placeholder per the skill's portrait rule. We're omitting that section entirely instead.
- No press logo bar — no press hits surfaced in scrape.
- No phone number anywhere on mockup — not verified.
- No claimed opening year — soften to "A few years in Ferndale" unless agent verifies via Facebook About during build.

---

## Deliverable

- `prospects/culantro/mockups/homepage-redesign.html`
- `prospects/culantro/mockups/assets/` (all images local, no hotlinks)
- Phase 4 QA green before returning
