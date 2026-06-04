# Redesign Spec — The Hen (Ann Arbor)

Redesign-only run. No audit.md; findings inferred from scrape + facts.

## Design Library References

**Vertical:** Restaurant — premium-casual brunch café, multi-location (3 Ann Arbor spots).

**Primary refs for THIS prospect:**
- **Cutler & Co** (primary — editorial photo-forward) — constrained hero, compact info block (location/hours/contact as plain text columns), 8-image grid replaces gallery, underlined text-link CTAs
- **Sadelle's** (secondary — warmth + portrait anchor) — oversized portrait-style hero, flat uppercase location list, short emotive origin paragraph on the homepage

**Execution cues to pull:**
1. **Hero:** one constrained photo (not full-bleed) + compact headline. Brand warmth from signature "Mom please send money" neon if usable; otherwise a single hero dish.
2. **Type pair:** one editorial serif for display + Inter for UI/body (NEVER Montserrat — SaaS-y per feedback_mockup_aesthetics).
3. **Location strip:** flat, text-only, uppercased — "ANN ARBOR · ON THE FLY · AT VALOR" — no map cards. Each is a tab/anchor to that location's address/hours/menu.
4. **Photo grid:** 6–8 image grid below hero carries identity. Pastries, lattes, interior neon, smiling staff. No stock.
5. **CTAs as underlined links for secondary actions** (Menu PDF, directions). Keep one button CTA for ORDER ONLINE (primary flow).
6. **Origin story:** short, emotionally specific — reference rebrand from Stray Hen, Jan 2025 ("new name, same great flavors").

**Anti-patterns to avoid:**
- All-Montserrat, all-magenta SaaS look of the current site
- Generic "Craving Food? We Got You" hero copy
- PDF-only menus behind one button (split: on-page teaser + PDF button per location)
- Stock food photography
- Emoji in copy or nav
- Burying hours in FAQ

**Do NOT copy from refs:**
- Cutler's white-tablecloth formality / $240 rib eye vibe — The Hen is walk-in counter-service daytime
- Sadelle's luxury-hotel global-locations swagger — The Hen is Ann Arbor neighborhood

---

## Brand DNA (survives the redesign)

- Playful neon ("Mom please send money") as identity anchor
- Warm, bright, people-first (not minimalist/cold)
- Ann Arbor-local, college-town energy
- Color accent kept: magenta/pink used sparingly as brand accent (not dominant)
- Name shift from Stray Hen → The Hen is recent (Jan 2025) — address in origin paragraph

---

## Inferred Audit Findings (drive section plan, NOT rendered on mockup)

1. **Hours confusion across sources cost a real customer a 30-min drive** (Deb M., Apr 8 2026, Yelp). Hours must be above the fold, per-location, unambiguous.
2. **3 locations buried.** Homepage opens with a confusing "ATTENTION: Your order will be ready at The Hen On The Fly NOT The Hen Ann Arbor" blocker — you can't tell what the 3 locations are or how they differ.
3. **No clear nav to 3 menus.** "SEE MENU" points to one location only.
4. **No identity/story on homepage.** Visitor learns nothing about the people, the rebrand, or why the café exists.
5. **Stray Hen artifacts** in filenames and Facebook URL — rebrand still incomplete on the website.
6. **SaaS-template typography** (Montserrat everywhere) at odds with the café's warm photo/neon identity.
7. **"Craving food? We Got You" hero** is generic — could be any restaurant.
8. **Order gating is confusing.** Current homepage *starts* with an ordering gate, then asks you to read it. Gate should live on the order-online flow, not block the homepage.

---

## Section Inventory (in render order)

### SECTION 1 — NAV
Sticky top nav, transparent over hero, solid on scroll. Left: The Hen wordmark (serif). Center links (uppercase, letter-spaced, Inter 12px): `DO NOT REWRITE: "MENU"`, `DO NOT REWRITE: "LOCATIONS"`, `DO NOT REWRITE: "ORDER ONLINE"`, `DO NOT REWRITE: "GIFT CARDS"`, `DO NOT REWRITE: "EMPLOYMENT"`. Right: small Instagram SVG + small Order Online button (pink outline).
Menu link → scrolls to #menus anchor on page (but each location's "See full menu" within that section targets `assets/the-hen-<location>-menu.pdf`).

### SECTION 2 — HERO
Constrained hero (not full-bleed). 1400px max-width centered, 70vh. Single photo of pastry spread + iced matcha from homepage (cinnamon roll / sprinkle donut / apple fritter / iced matcha / latte / iced coffee on wood table). Photo takes right 55%. Left 45%:
  - Eyebrow: `DO NOT REWRITE: "ANN ARBOR BRUNCH, THREE WAYS"`
  - Headline (serif display, ~72px): `DO NOT REWRITE: "Nourishing all souls, one plate at a time."`
  - Subhead (Inter, ~18px): `DO NOT REWRITE: "Fluffy pancakes, savory omelettes, and modern avocado toast — served daily 8 AM to 3 PM. Closed Wednesdays."`
  - Two CTAs: underlined text link `DO NOT REWRITE: "See the menu →"` (targets #menus); pink outline button `DO NOT REWRITE: "Order online"` (targets order.toasttab.com URL).
Audit finding (internal): #1 hours visible above fold; #4 replaces generic "We Got You" hero; #8 removes blocking order gate.

### SECTION 3 — LOCATION STRIP
Flat text-only row beneath hero. Full-bleed horizontal band, ~120px tall, off-white background. Three columns separated by thin dividers. Each column:
  - Location name (uppercased Inter 11px, letter-spaced): `DO NOT REWRITE: "THE HEN ANN ARBOR"` / `DO NOT REWRITE: "THE HEN ON THE FLY"` / `DO NOT REWRITE: "THE HEN AT VALOR"`
  - Address (serif, 15px)
  - Phone (Inter, 14px, `tel:` link)
  - "See details ↓" underlined link (anchors to per-location block in Section 5)
Column 1: `DO NOT REWRITE: "403 E Washington St"`, `DO NOT REWRITE: "(734) 929-2590"`, tag: `DO NOT REWRITE: "Dine in"`
Column 2: `DO NOT REWRITE: "1906 Packard St"`, `DO NOT REWRITE: "(734) 368-9591"`, tag: `DO NOT REWRITE: "Carry out"`
Column 3: `DO NOT REWRITE: "573 State Circle"`, `DO NOT REWRITE: "Inside Valor Pilates"`, tag: `DO NOT REWRITE: "Weekend pop-up"`
Audit finding: #2 all 3 locations surfaced; #1 phones clickable.

### SECTION 4 — ORIGIN STORY
Short, emotionally specific. Two-column: left column serif display label (`DO NOT REWRITE: "A new name. The same early mornings."`). Right column Inter body (~16px, ~3 paragraphs):

Paragraph 1: `DO NOT REWRITE: "In January 2025, Stray Hen became The Hen — new name, same pancakes worth waking up for. What started as a single cafe in downtown Ann Arbor is now three places to meet us: a dine-in room on Washington, a carryout counter on Packard, and a weekend pop-up inside Valor Pilates."`

Paragraph 2: `DO NOT REWRITE: "We open at 8. We close at 3. We take Wednesdays off, because even hens need a day. And we don't take reservations — pick any seat you like."`

Paragraph 3: `DO NOT REWRITE: "Gluten-friendly. Vegan-friendly. Dog-friendly on the patio. Mostly just friendly."`
Audit finding: #4 identity anchor; #5 addresses rebrand; #4 hours now prominent in prose too.

### SECTION 5 — SIGNATURE (PHOTO GRID)
Section header (serif display, centered, 48px): `DO NOT REWRITE: "What's on the table"`
Subhead (Inter 16px, centered, muted): `DO NOT REWRITE: "A taste of what's inside — full menus per location below."`
Below: 6-image grid, 3 cols × 2 rows on desktop (collapses to 2×3 tablet, 1×6 mobile). No captions, no hover text, no prices. Square or 4:3 crop, gap 12px.
Agent: pull 6 best food/drink/interior photos from scrape markdown + homepage CDN. Minimum 1 of: pastry spread; pancake/waffle dish; latte/coffee close-up; the "Mom please send money" neon; breakfast sandwich or avocado toast; interior/dining room shot.
Audit finding: #6 photography carries identity over typography.

### SECTION 6 — MENUS (PER LOCATION)
Section header (serif display, centered, 48px): `DO NOT REWRITE: "Three menus, three moods"`
Three stacked location blocks. Each block has a plain divider at the top and a 2-column layout inside:

**Block A — The Hen Ann Arbor (dine-in flagship)**
Left column (Inter):
  - Label: `DO NOT REWRITE: "DINE IN — 403 E WASHINGTON ST"`
  - Hours: `DO NOT REWRITE: "Mon–Tue, Thu–Sun · 8 AM–3 PM · Closed Wednesdays"`
  - Phone: `DO NOT REWRITE: "(734) 929-2590"`
  - A one-liner: `DO NOT REWRITE: "Walk in, pick a seat, stay a while. Counter service, full coffee bar, outdoor patio."`
  - CTA: underlined link `DO NOT REWRITE: "See the full menu (PDF) →"` → `assets/the-hen-ann-arbor-menu.pdf`
  - CTA: underlined link `DO NOT REWRITE: "Get directions →"` → Google Maps
Right column: 3 verbatim dish mentions from verified-facts.md as a teaser (plain list, serif italic):
  - `DO NOT REWRITE: "Banana & Nutella pancakes"`
  - `DO NOT REWRITE: "Breakfast burritos"`
  - `DO NOT REWRITE: "The Greek-ish salad — chicken, olives, crunchy garbanzos, capers"`

**Block B — The Hen On The Fly (Packard, carryout)**
Left column:
  - Label: `DO NOT REWRITE: "CARRY OUT — 1906 PACKARD ST"`
  - Hours: `DO NOT REWRITE: "Daily · 8 AM–3 PM · Closed Wednesdays"`
  - Phone: `DO NOT REWRITE: "(734) 368-9591"`
  - One-liner: `DO NOT REWRITE: "Fresh, fast, and delicious take out for every craving. Pickup in 15–20 minutes."`
  - CTA: pink outline button `DO NOT REWRITE: "Order online"` → `https://order.toasttab.com/online/hen-on-the-fly-1906-packard-street`
  - CTA: underlined link `DO NOT REWRITE: "See the full menu (PDF) →"` → `assets/the-hen-on-the-fly-menu.pdf`
Right column: 3 teaser items:
  - `DO NOT REWRITE: "Croissant sandwich"`
  - `DO NOT REWRITE: "Breakfast sliders (add avocado)"`
  - `DO NOT REWRITE: "Egg nog latte"` (seasonal)

**Block C — The Hen at Valor (weekend pop-up)**
Left column:
  - Label: `DO NOT REWRITE: "WEEKEND POP-UP — 573 STATE CIRCLE"`
  - Hours: `DO NOT REWRITE: "Inside Valor Pilates — hours vary. Follow us for pop-up dates."`
  - One-liner: `DO NOT REWRITE: "Coffee and breakfast alongside Mat Pilates and community events. Two years strong as of January 2026."`
  - CTA: underlined link `DO NOT REWRITE: "Follow on Instagram →"` → https://www.instagram.com/thehenannarbor/

Audit finding: #2 + #3 all locations, all menus surfaced; #1 per-location hours explicit.

### SECTION 7 — SOCIAL PROOF
Full-bleed band, off-white (not dominant magenta). Section header (serif display, 32px): `DO NOT REWRITE: "What folks are saying"`
Three testimonial cards side-by-side (stacks on mobile). Each card: quote in serif 18px italic, attribution in Inter 14px below.

Card 1:
  Quote: `DO NOT REWRITE: "Clean and bright environment with plenty of seating. Friendly staff, nice menu, and excellent food!"`
  Attribution: `DO NOT REWRITE: "— Seth Galentine, Google"`

Card 2:
  Quote: `DO NOT REWRITE: "A delightful find with cute meets quirky decor and a tasty breakfast menu."`
  Attribution: `DO NOT REWRITE: "— Marisa U, Google"`

Card 3:
  Quote: `DO NOT REWRITE: "While not a particularly large spot, it clearly is a local favorite. Expect a long queue, but the staff will get you through quickly. Reasonably priced and the food is excellent."`
  Attribution: `DO NOT REWRITE: "— Timothy S., Yelp"`

Below cards, a small summary line (Inter 14px, muted): `DO NOT REWRITE: "4.5 stars across 826 Google reviews · 4.4 stars across 274 Yelp reviews"`

### SECTION 8 — FAQ (kept, simplified)
Section header (serif display, 32px): `DO NOT REWRITE: "Good to know"`
4 plain accordion rows (not bubbled cards — thin dividers, serif question, Inter answer). Use the homepage FAQ verbatim:

Row 1 (open by default):
  Q: `DO NOT REWRITE: "What are your hours?"`
  A: `DO NOT REWRITE: "We're open daily from 8 AM to 3 PM, with a well-deserved rest on Wednesdays. Stop by and enjoy our fresh offerings any other day!"`

Row 2:
  Q: `DO NOT REWRITE: "Do you take reservations?"`
  A: `DO NOT REWRITE: "At this time, we operate on a first-come, first-served basis. Simply walk in, we'll take your order and you can pick any seat you'd like."`

Row 3:
  Q: `DO NOT REWRITE: "Do you have gluten-free options?"`
  A: `DO NOT REWRITE: "We have gluten-friendly choices that are sure to please. Feel free to browse our menu to find a dish that suits your needs."`

Row 4:
  Q: `DO NOT REWRITE: "Do you offer vegan options?"`
  A: `DO NOT REWRITE: "Absolutely. We've curated a selection of flavorful vegan dishes, so there's always something for everyone."`

### SECTION 9 — FOOTER
Dark charcoal background (#1A1A1A), cream text (#F8F3EB). Four columns:
Col 1: The Hen wordmark (serif, cream) + one-liner: `DO NOT REWRITE: "Ann Arbor brunch, three ways."`
Col 2 header `DO NOT REWRITE: "Visit"` — 3 addresses stacked (address + `tel:` phone each)
Col 3 header `DO NOT REWRITE: "Eat with us"` — links: Menu (anchors to #menus), Order Online (Toast URL), Gift Cards, Employment, Merch
Col 4 header `DO NOT REWRITE: "Follow along"` — Instagram SVG + `DO NOT REWRITE: "@thehenannarbor"` link; Facebook SVG
Bottom strip (Inter 12px muted): `DO NOT REWRITE: "© 2026 The Hen Ann Arbor · hello@theheneats.com"`

---

## Assets to collect (agent)

From `scrape/homepage.md` CDN URLs + `https://www.theheneats.com/` direct fetch:
- `67715e101aae5b8ed1107756_MomPleaseSendMoney.png` — neon sign (hero candidate or interior photo slot)
- `6879e76fc44a117f003a06e6_67715e101aae5b8ed110773e_Stray Hen 10_23 16 (1).avif` — pastry spread with coffee (hero primary)
- Logo from branding.json: `67715e101aae5b8ed11076c6_TheHen-Logo-Black-Transp Cropped.avif`
- OG image: `6775a863cd28293507398a7b_GraphImage2.jpg`
- Any additional interior/food shots embedded in homepage

If homepage asset set is thin (<6 food photos), agent may pull 1–2 from Google knowledge panel images referenced in `facts/google-hen-*.md` markdown image URLs. No stock. No hotlinking.

Chef/portrait note: no named chef surfaces in verified-facts.md. Origin section uses no portrait — the neon + pastry spread carry identity instead. (Avoiding portrait-slot failure per feedback_redesign_deliverable_polish.)

---

## Type + Color System

**Typography (real stack — not Montserrat):**
- Display/serif: `"EB Garamond", "Playfair Display", Georgia, serif` (editorial warm serif) OR `"Fraunces", Georgia, serif` — agent chooses; both warm and appropriate.
- UI/body: `"Inter", -apple-system, BlinkMacSystemFont, sans-serif` (14–18px range)
- Wordmark: same serif as display, uppercase letter-spaced

**Color palette:**
- Background: `#FDFBF7` (warm cream)
- Surface: `#FFFFFF`
- Ink: `#1A1A1A`
- Muted ink: `#6E6A65`
- Accent pink (kept as brand DNA, used sparingly): `#E63A82` (softer than branding.json's `#F93262`) — used for: one primary CTA button, underlines on focus, neon callouts
- Accent off-white strip: `#F2EDE4`
- Footer: `#1A1A1A` with cream text

**Buttons:**
- Primary: pink outline (`border: 1.5px solid #E63A82`, text `#E63A82`, hover fill `#E63A82` + white text)
- No drop shadows. No pill border-radius (use 4px).
- Underlined text-link CTAs: `border-bottom: 1px solid currentColor`, hover darkens to accent pink

**Spacing:**
- Max content width: 1280px (sections can go wider for full-bleed bands)
- Section padding: 96px top/bottom desktop, 48px mobile
- Consistent horizontal gutters — gate A1 in QA

---

## QA Must Catch

- All verbatim fenced strings appear byte-for-byte
- All 3 location phones are `tel:` links
- All 3 location menus point to `assets/the-hen-<slug>-menu.pdf` (files will 404 until client supplies — this is fine per Phase B rules)
- Order Online button points to real Toast URL (not placeholder)
- Hero photo + 6 grid photos load locally from `mockups/assets/`
- No Montserrat in final CSS
- No emoji anywhere
- No audit-tag pills or diff annotations
- Responsive at 768px
- Exactly one nav above hero
- Location strip columns share gutters with nav (≤2px drift)
