# Miss Kim Ann Arbor — Redesign Spec
Author: redesign Phase A (scrape + synthesize). Date: 2026-04-19.
Scope: Single-page homepage redesign of misskimannarbor.com. NO audit-tag pills anywhere — this is a redesign, not an audit.

All verbatim strings in this spec are fenced as `DO NOT REWRITE: "..."` and trace to `facts/verified-facts.md`. Every factual claim cites a source file in `prospects/miss-kim/`.

---

## Brand DNA to Preserve

The Miss Kim identity elements that MUST survive elevation. Do not swap, soften, or upmarket these.

1. **"Really Great Korean Food."** [source: scrape/homepage.md] — The deliberately understated tagline IS the voice. Do not replace with "Elevated Korean Cuisine," "A New Chapter in Korean Dining," or any other AI-luxury phrase. The plain-language confidence is Zingerman's-family signature.
2. **Zingerman's Community of Businesses lineage.** [source: facts/zingermans-profile.md] — Miss Kim is part of the ZCoB family; the trust credit for service ("…being as it's associated with Zingermans so the staff are well trained, attentive and knowledgeable" — Kirsten F.) flows through this. Surface it in the About and Footer; do NOT hide it as if Miss Kim is a standalone concept.
3. **Chef Ji Hye Kim's perspective.** [source: facts/google-search.md] — "Obsessed with ancient Korean culinary texts and the finer points of fermentation" is the philosophy. This is not "Korean-American fusion" — it's Korean tradition interpreted through fermentation rigor and local Michigan ingredients.
4. **Korean-inspired + Michigan ingredients.** [source: facts/yelp.md — "About the Business"] — The sourcing ethos ("local Michigan ingredients!") is a material brand claim, not a tagline flourish. Preserve it.
5. **Kerrytown / Ann Arbor warmth.** [sources: facts/yelp.md, facts/google-search.md, scrape/homepage.md] — "Cozy," "communal tables," "family dining style," "booths" — the restaurant is a neighborhood restaurant with scale-appropriate aspirations, not a destination fine-dining room. Redesign should feel like Ann Arbor on a Tuesday night, not Manhattan on a Friday.
6. **Monthly chef pop-ups.** [source: scrape/homepage.md] — This is active, ongoing programming. Give it a real block, not a footer mention.

---

## Design Library References

Cues drawn from `wiki/wiki/design-library.md` — Restaurant / Hospitality > "Premium / approachable luxury" sub-category.

**Execution cues to adopt:**
1. Hero is ONE food or space photo, full-bleed, warm color grade — not a grid, not a carousel. [design-library.md L68]
2. Typography pair: one distinctive serif (editorial) + one clean sans (UI). Never all-sans Montserrat (or Lato). [design-library.md L69] — Current site is all-Lato per scrape/branding.json; redesign shifts to serif display + sans UI.
3. Menu is on-site, readable HTML — never a PDF link behind a button. [design-library.md L70]
4. Hours + reservation CTA above the fold. Location + hours repeat in footer with `tel:` and maps links. [design-library.md L71]
5. Reservation CTA (OpenTable) appears in nav AND hero AND footer — never buried. [design-library.md L72]

**Anti-patterns to avoid:**
1. "Experience our cuisine" generic hero copy — replace with named dishes, location, or a critic quote. [design-library.md L77] — Miss Kim alternative: use the existing "Really Great Korean Food" as hero headline with a verified dish or Zingerman's-blog line as subhead.
2. Menu items rendered as e-commerce product cards with prices and "Add" buttons. [design-library.md L78]
3. Emojis (knife-and-fork, sparkles, chef hat). [design-library.md L79] — Reinforces global feedback rule no-emojis-websites.
4. Stock food photography (the same 10 Unsplash plates every restaurant uses). [design-library.md L81]

---

## Reference Takeaways

Condensed from `reference/reference-summary.md`. For the Phase B build agent.

- **Typography strategy:** Distinctive serif for display + book-weight sans for body. Section labels set small and bold-caps, not H-tag-huge. Pull from Bull & Last and King pages' restraint.
- **Color strategy:** One signature accent on warm cream ground. Recommend: warm clay / fermented-pepper orange-red accent (reads Korean gochujang, not generic brand red) on a bone-cream ground (~#F3EEE4). Keep a deep charcoal-black for body type. Avoid continuing the bright cyan (#1191B8) in branding.json — it's the Toast default, not a brand decision.
- **Hero strategy:** One full-bleed food photo (cacio e pepe tteokbokki is the natural hero given the Zingerman's blog feature) with "Really Great Korean Food" set in serif over it, two CTAs (Reserve on OpenTable / Order To-Go). NOT a hero grid.
- **Photography strategy:** Use real Miss Kim photography — the `jamesbeard.jpg` chef portrait is an existing asset (scrape/homepage.md line 114), plus the dining-room and plated-food photos already referenced in homepage.md. Do NOT insert stock.
- **Nav strategy:** Nearly invisible — wordmark centered, single "Reserve" button right-aligned, 3-4 text links (Menu / About / Events / Visit). No dropdown mega-menu.
- **Proof strategy:** Press + Instagram, not testimonial carousel. Inline Pete-Wells-style critic-quote prose inside the Chef block.

---

## Section Inventory

Single-page scroll. Order top to bottom. NO audit pills.

### 1. Hero — signature photo + tagline + dual CTA

- **Layout:** Full-bleed food photograph (vertical 3:4 or 4:5 aspect ratio, mobile-safe crop). Tagline H1 overlaid bottom-left or bottom-center in distinctive serif, cream color, sized ~72–96px desktop. One-line context subhead immediately under. Two CTA buttons side by side — primary "Reserve on OpenTable" (solid warm accent), secondary "Order To-Go" (outlined cream). Fixed-position wordmark top-center, reservation phone top-right (tel:).
- **H1 (verbatim):** `DO NOT REWRITE: "Really Great Korean Food"` [source: scrape/homepage.md]
- **Subhead (verbatim):** `DO NOT REWRITE: "Korean-inspired food made with local Michigan ingredients"` [source: facts/yelp.md — About the Business]
- **Primary CTA label (verbatim):** `DO NOT REWRITE: "Make a Reservation"` → links to https://www.opentable.com/r/miss-kim-korean-restaurant-reservations-ann-arbor?restref=1210180 [source: scrape/homepage.md]
- **Secondary CTA label (verbatim):** `DO NOT REWRITE: "Order now"` → links to https://misskimannarbor.com/order [source: scrape/homepage.md]
- **Phone in nav (verbatim):** `DO NOT REWRITE: "(734) 275-0099"` (tel:+17342750099) [source: scrape/homepage.md]
- **Image direction:** Use the existing Miss Kim "Table of Miss Kim's Korean Food" overhead spread photo already hosted on Toast CDN (scrape/homepage.md line 6 refers to `miss_kim__overlays_-_draft.1-01_720.png`). If unavailable, fall back to Cacio e Pepe Tteokbokki close-up — the Zingerman's blog asset `cacio-e-pepe.jpg` [source: facts/zingermans-profile.md].
- **Do NOT:** Stock food plates. Generic cyan-blue pill buttons (current Toast default). Carousel.

---

### 2. Today's Hours / Quick-Open Strip

- **Layout:** Single thin band directly below hero. Warm cream background, charcoal type. Two columns on desktop (Open Today + Quick Actions), stacked on mobile. Day-aware: show "Today — 11:30 am – 9:00 pm" based on system date; Tuesday displays "Closed today — open Wednesday 11:30 am."
- **Full hours copy (verbatim, used in tooltip / expand):**
  - `DO NOT REWRITE: "Monday — 11:30 am – 9:00 pm"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Tuesday — Closed"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Wednesday — 11:30 am – 9:00 pm"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Thursday — 11:30 am – 9:00 pm"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Friday — 11:30 am – 9:30 pm"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Saturday — 11:00 am – 9:30 pm"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Sunday — 11:30 am – 9:00 pm"` [source: scrape/homepage.md]
- **Quick-action labels:** "Reserve", "Order To-Go", "Directions" — all deep-link.
- **Do NOT:** Build a pulsing "OPEN NOW" neon dot. No emoji clocks.

---

### 3. Signature Dish Spotlight — Cacio e Pepe Tteokbokki

- **Layout:** Two-column on desktop — 60% image left (close-up plated shot with warm natural light), 40% prose right. Stacked on mobile. Cream ground; accent color used only on the small "Signature" eyebrow label and a text link.
- **Eyebrow (verbatim-adjacent, new framing):** `DO NOT REWRITE: "A Southern Italian Twist on a Korean Classic"` [source: facts/zingermans-profile.md — Jan 2025 Zingerman's blog title]
- **Dish title (verbatim):** `DO NOT REWRITE: "Cacio e Pepe Tteokbokki"` [source: facts/yelp.md — popular-dishes grid; facts/zingermans-profile.md]
- **Price callout (verbatim):** `DO NOT REWRITE: "$18"` [source: facts/yelp.md — popular-dishes grid]
- **Context prose (write fresh around these verified anchors):**
  - Chef Ji Hye Kim's philosophy: `DO NOT REWRITE: "obsessed with ancient Korean culinary texts and the finer points of fermentation"` [source: facts/google-search.md — From Miss Kim blurb]
  - Most-popular peer dish (street style): `DO NOT REWRITE: "As in Korea, one of the most popular dishes at Miss Kim has been the spicy, pork-scented, gochujang-laced Street Style Tteokbokki."` [source: facts/google-search.md — People-also-ask / Zingerman's Oct 2025 blog]
- **Image direction:** Use the Zingerman's blog photo `cacio-e-pepe.jpg` [source: facts/zingermans-profile.md] or own-site equivalent. Warm, overhead or 3/4, plated shot with visible rice cakes and cheese.
- **Do NOT:** Emojis. "Must-try!" exclamation copy. Stars or "★★★★★" decoration.

---

### 4. Chef Ji Hye Kim — portrait + bio + press prose

- **Layout:** Left column chef portrait (use existing `jamesbeard.jpg` asset — Chef Ji Hye candid in kitchen), right column one tight paragraph of running prose with the Pete-Wells-style press citation inline (like King Restaurant does). Below the paragraph, three small press mentions listed as plain text lines.
- **Eyebrow:** `DO NOT REWRITE: "Chef"` or `DO NOT REWRITE: "About"`
- **Headline (verbatim):** `DO NOT REWRITE: "Chef Ji Hye Kim"` [source: facts/google-search.md]
- **Bio anchors (write fresh paragraph around these verified strings):**
  - `DO NOT REWRITE: "Chef Ji Hye Kim grew up in Seoul, South Korea and is obsessed with ancient Korean culinary texts and the finer points of fermentation."` [source: facts/google-search.md — From Miss Kim blurb]
  - `DO NOT REWRITE: "Miss Kim, opened in 2016 as a proud part of the Zingerman's Community of Businesses."` [source: facts/google-search.md — From Miss Kim blurb]
- **Press mentions (plain-text lines, no logo chips):**
  - `DO NOT REWRITE: "NYT writer Eric Kim and award-winning author Matt Rodbard come to Miss Kim's in Ann Arbor."` — April 2024 [source: facts/zingermans-profile.md]
  - `DO NOT REWRITE: "A Southern Italian Twist on a Korean Classic"` — Zingerman's Community of Businesses, January 2025 [source: facts/zingermans-profile.md]
  - `DO NOT REWRITE: "Royale Style Tteokbokki at Miss Kim"` — Zingerman's Community of Businesses, October 2025 [source: facts/google-search.md]
- **James Beard note:** The homepage hero image file is `jamesbeard.jpg` (scrape/homepage.md line 114) — PHOTO is usable, but DO NOT write "James Beard nominee" or "James Beard semifinalist" into copy. The nomination is not verified in this scrape set. Use the photo; cite nothing.
- **Image direction:** Chef candid in kitchen, mid-action if possible. NOT a static professional headshot.
- **Do NOT:** Emojis. Large press-logo bar. Fabricated awards.

---

### 5. Menu Anchor — 5 category strips with verified dishes

- **Layout:** Five horizontal strip rows. Each strip: left-aligned category name (set as a small bold-caps label in distinctive serif), right-aligned 2–3 dish bullets each with dish name + one-line description + price where verified. Thin horizontal hairline between strips. Cream ground. No image cards — this is typographic menu, like Bull & Last's menus list.
- **Header (verbatim-adjacent):** `DO NOT REWRITE: "Menu"` with subhead `DO NOT REWRITE: "415 North 5th Avenue, Ann Arbor, MI"` [source: scrape/menu.md]
- **View-full-menu CTA (verbatim):** `DO NOT REWRITE: "Order To Go"` → https://misskimannarbor.com/order [source: scrape/menu.md]

**Category 1 — Banchan & Small Plates**
- `DO NOT REWRITE: "Moo Radish Kimchi — $5"` [source: facts/yelp.md — popular-dishes grid]
- `DO NOT REWRITE: "Beet + Avocado Salad"` — `DO NOT REWRITE: "Roasted local beets, avocado, pickled red onions, toasted walnuts, garlic dressing."` ~$14 [source: facts/yelp.md — photo caption]
- `DO NOT REWRITE: "Buddhist Lotus Roots"` [source: facts/yelp.md — review by Kirsten F.]

**Category 2 — Tteokbokki**
- `DO NOT REWRITE: "Street Style Tteokbokki — $19"` [source: facts/yelp.md — popular-dishes grid]
- `DO NOT REWRITE: "Cacio e Pepe Tteokbokki — $18"` [source: facts/yelp.md — popular-dishes grid]
- (Royale Style Tteokbokki is referenced in reviews as a seasonal/rotating variant) [source: facts/yelp.md — Kirsten F., Alina S. reviews]

**Category 3 — Chicken, Pork & Beef**
- `DO NOT REWRITE: "Korean Fried Chicken"` — soy glaze option [source: facts/yelp.md — photo caption, Kirsten F. review]
- `DO NOT REWRITE: "Pork Belly"` [source: facts/yelp.md — photos category, 50 reviews]
- `DO NOT REWRITE: "Braised Short Ribs"` / `DO NOT REWRITE: "Baby Back Ribs"` [source: facts/yelp.md]

**Category 4 — Vegetables, Tofu & Rice**
- `DO NOT REWRITE: "Crispy Broccolini"` in fish caramel [source: facts/yelp.md — Linda I. review]
- `DO NOT REWRITE: "Korean Fried Tofu Sandwich"` — `DO NOT REWRITE: "tofu, carrots, cucumbers, jalapeño, spicy mayo on challah bun"` ~$15 [source: facts/yelp.md — photo caption]
- `DO NOT REWRITE: "Kimchi Pork Fried Rice — $24"` [source: facts/yelp.md — popular-dishes grid]
- `DO NOT REWRITE: "Mushroom Japchae"` [source: facts/yelp.md — Linda I. review]

**Category 5 — For the Table / Kids**
- `DO NOT REWRITE: "Kids Soy Butter Rice W/ Egg — $8"` [source: facts/yelp.md — popular-dishes grid]
- `DO NOT REWRITE: "Bao Buns"` (Mushroom / Pork / Steamed) [source: facts/yelp.md]
- `DO NOT REWRITE: "Bibimbap"` [source: facts/yelp.md — Emmit P. review]

**Weekly specials callout** (secondary small box):
- `DO NOT REWRITE: "Tuesday Banh Mi Special — $13"` [source: facts/google-search.md — Products panel] — NOTE: Miss Kim is CLOSED Tuesdays (per hours); Google's Products panel may reference Little Kim or a legacy menu. **Flag for Phase B verification before publishing the Tuesday special.** If uncertain, drop the Tuesday item and keep only Wednesday.
- `DO NOT REWRITE: "Wednesday Chicken Dinner Special — $20"` [source: facts/google-search.md — Products panel]
- `DO NOT REWRITE: "Ssam Plates — $22–$29"` [source: facts/google-search.md — "NEW TO THE DINNER MENU: SSAM PLATES"]

**Do NOT:** Generate phantom menu items. Add "Add to Cart" or "+" icons. Use star ratings on dishes.

---

### 6. Review Wall — four verified Yelp quotes

- **Layout:** Four quote blocks in a 2×2 grid on desktop, stacked on mobile. Each block: large italic opening-quote mark (distinctive serif), quote body in book-weight serif, attribution line in small caps sans below ("— First Name L., Elite 26 · Ann Arbor · Dec 2025"). No star decoration, no profile photos, no card shadows. Single hairline separating the quotes.
- **Section eyebrow:** `DO NOT REWRITE: "Guests"`
- **Section headline:** one line — consider `DO NOT REWRITE: "4.4 on Google · 373 on Yelp"` [sources: facts/google-search.md, facts/yelp.md] — use ratings as headline, not "What Our Guests Are Saying!"

**Quote 1 (Alina S., Dec 17 2025):**
> `DO NOT REWRITE: "An absolute gem of a restaurant in Ann Arbor. The food is so tasteful and delicious. The staff is so friendly and kind. I love the coziness and vibe and always have the best time when I eat there!"`
— Alina S., Yelp Elite · Ann Arbor, MI [source: facts/yelp.md]

**Quote 2 (Linda I., Oct 25 2025):**
> `DO NOT REWRITE: "Outstanding! Love the food, the care and intention that goes into the food, the friendly service, and the whole dining experience at Miss Kim."`
— Linda I., Yelp Elite · MI [source: facts/yelp.md]

**Quote 3 (Kirsten F., Dec 4 2025):**
> `DO NOT REWRITE: "The food here is so fresh and classic Korean with a little twist sometimes. It's the perfect balance of salty, spicy, umami in every bite."`
— Kirsten F., Yelp Elite · Troy, MI [source: facts/yelp.md]

**Quote 4 (Sergio R., Jan 30 2026):**
> `DO NOT REWRITE: "The soy butter rice was a stand out. My wife says 'that is the best rice I've ever had.'"`
— Sergio R., Yelp Elite · Las Vegas, NV [source: facts/yelp.md]

**Do NOT:** Fabricate attributions. Use unsourced star ratings. Run as a carousel.

---

### 7. Private Events + Chef Pop-Ups — two-up split

- **Layout:** Two equal-width blocks side by side (stacked on mobile). Each block: small photo (top), eyebrow label, short headline, one-paragraph descriptor, single CTA link.
- **Block A — Large Party or Catering**
  - Eyebrow: `DO NOT REWRITE: "Private & Catering"`
  - Headline (verbatim): `DO NOT REWRITE: "Large Party or Catering"` [source: scrape/homepage.md]
  - Body (verbatim): `DO NOT REWRITE: "Miss Kim can offer larger party reservations at the restaurant or offer catering for your event, If you are interested, please fill out the form below!"` [source: scrape/homepage.md]
  - CTA label: `DO NOT REWRITE: "Inquiries Form"` → the existing Google Form [source: scrape/homepage.md]
- **Block B — Special Events / Chef Pop-Ups**
  - Eyebrow: `DO NOT REWRITE: "Monthly"`
  - Headline (verbatim): `DO NOT REWRITE: "Special Events"` [source: scrape/homepage.md]
  - Body (verbatim): `DO NOT REWRITE: "Each month we're inviting some incredible local Chefs to pop-up in the Miss Kim kitchen and share their incredible food with you!"` [source: scrape/homepage.md]
  - CTA label (verbatim): `DO NOT REWRITE: "Upcoming Events"` → https://misskimannarbor.com/events [source: scrape/homepage.md]

**Do NOT:** Invent dates for specific chef pop-ups. Use sparkle or star icons.

---

### 8. Visit — address / hours / phone / email / parking / map

- **Layout:** Two-column desktop, stacked mobile. Left column = address block, hours table, phone + email contact list. Right column = static map image with pin (existing Toast CDN asset `misskimmap2020.3_*.webp` referenced in scrape/homepage.md line 64 is available). Below the two columns: the parking-instructions block in a full-width cream band — this copy is LOAD-BEARING because Miss Kim's entrance is not where the street address points.
- **Eyebrow:** `DO NOT REWRITE: "Visit"`
- **Address (verbatim):**
  - `DO NOT REWRITE: "415 N. Fifth Ave"` [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Ann Arbor, Michigan 48104"` [source: scrape/homepage.md]
- **Phone (verbatim):** `DO NOT REWRITE: "(734) 275-0099"` as tel: link [source: scrape/homepage.md]
- **Email (verbatim):** `DO NOT REWRITE: "misskim@zingermans.com"` as mailto link [source: scrape/homepage.md]
- **Directions CTA (verbatim):** `DO NOT REWRITE: "Get Directions!"` → existing Google Maps link [source: scrape/homepage.md]
- **Hours table:** full 7-day list using the verbatim strings in Section 2 above.
- **Parking block (verbatim, full copy — do NOT paraphrase):**
  > `DO NOT REWRITE: "How to get here"`
  >
  > `DO NOT REWRITE: "HAVING TROUBLE FINDING US?"`
  >
  > `DO NOT REWRITE: "Our street address is on Fifth Avenue but our entrance is closer to Kingsley and directly off of the one way parking lot located at Kingsley (entrance) and Fourth Ave (exit). We suggest that you park in this small lot when you come to pick up your food."`
  >
  > `DO NOT REWRITE: "If you've already parked on Fifth, you can still find us by walking all the way through the courtyard between Sweetwaters and Found to the small parking lot on the other side."`
  [source: scrape/homepage.md]
- **Neighborhood context (secondary line):** `DO NOT REWRITE: "Kerrytown Ann Arbor"` [source: facts/yelp.md]
- **Image direction:** Use the existing stylized map asset from Toast CDN, or replace with a warm-toned Google Static Maps embed keyed to the pin at 42.284642, -83.746426. Keep it static — not an interactive iframe.
- **Do NOT:** Re-word the parking copy. Compress it. Move it to the footer.

---

### 9. Little Kim Cross-Link — sister concept

- **Layout:** Single slim band below Visit. Left: small circular photo of Little Kim food. Center: headline + one-line description. Right: outlined CTA button. Pine-green accent stripe — differentiate visually from Miss Kim's accent so the two identities stay distinct.
- **Eyebrow (verbatim):** `DO NOT REWRITE: "Sister concept"` or `DO NOT REWRITE: "Next door"`
- **Headline (verbatim):** `DO NOT REWRITE: "Little Kim"` [source: facts/zingermans-profile.md]
- **Tagline (verbatim):** `DO NOT REWRITE: "Really great vegetarian food"` [source: facts/zingermans-profile.md]
- **CTA label:** `DO NOT REWRITE: "Visit Little Kim"` → https://littlekimannarbor.com/ [source: facts/zingermans-profile.md]
- **Do NOT:** Frame Little Kim as a "vegan offshoot" — Zingerman's wording is specifically "vegetarian."

---

### 10. Footer — Zingerman's family, Instagram, utility

- **Layout:** Three-row footer on cream or dark-charcoal ground (designer's call). Row 1 = Instagram grid strip (4–8 square tiles pulling @misskimannarbor) with "Follow @misskimannarbor" label. Row 2 = three columns: (a) Miss Kim wordmark + tagline + phone/email, (b) quick links (Menu / Reservations / Events / Visit), (c) Zingerman's Community of Businesses text-block with 2-3 sister-business text links. Row 3 = fine-print utility row (privacy, terms, © Miss Kim Korean Restaurant 2026).
- **Instagram headline (verbatim):** `DO NOT REWRITE: "Explore Our Instagram!"` or simply `DO NOT REWRITE: "@misskimannarbor"` [source: scrape/homepage.md]
- **Instagram CTA (verbatim):** `DO NOT REWRITE: "See Full Feed"` → https://www.instagram.com/misskimannarbor/ [source: scrape/homepage.md]
- **ZCoB block (verbatim):**
  - `DO NOT REWRITE: "Miss Kim, opened in 2016 as a proud part of the Zingerman's Community of Businesses."` [source: facts/google-search.md — From Miss Kim blurb]
- **ZCoB links:** `DO NOT REWRITE: "Our Businesses"` → https://www.zingermanscommunity.com/about-us/our-businesses/?crf=MissKim [source: scrape/homepage.md]
- **Legal (verbatim):**
  - `DO NOT REWRITE: "Privacy Policy"` → existing Zingerman's privacy URL [source: scrape/homepage.md]
  - `DO NOT REWRITE: "Terms of Use"` → existing Zingerman's terms URL [source: scrape/homepage.md]
- **Social icons:** Instagram, Facebook (facebook.com/misskimannarbor), TikTok (@misskimannarbor), LinkedIn [source: facts/google-search.md — Profiles panel]
- **Do NOT:** Emojis. An "As Seen In" logo bar. A newsletter signup (not verified in any scrape source).

---

## Build notes for Phase B

1. **Typography stack (recommendation):** Display = a distinctive editorial serif (candidates: Canela, GT Super, Tiempos Headline). Body = a warm book-weight sans (candidates: Inter, Söhne, National). Do NOT keep Lato from branding.json.
2. **Color tokens (recommendation, designer to finalize):**
   - Ground: `#F3EEE4` (bone cream)
   - Ink: `#1A1715` (soft black)
   - Accent: warm clay / gochujang red — approx `#B4412B` (designer to refine — should feel pigmented, not digital)
   - Secondary accent (Little Kim only): pine green, approx `#2F5240`
   - Explicitly RETIRE the Toast default `#1191B8` cyan from branding.json
3. **Nav items (final):** wordmark (center), "Menu" / "About" / "Events" / "Visit" (text links), "Reserve" (solid-filled CTA button), phone (tel:) top-right utility.
4. **Facts to double-check before build:** (a) Tuesday Banh Mi Special conflicts with Tuesday-closed hours — verify with client or drop; (b) James Beard status — do NOT write "nominee" into copy without external verification even though the homepage uses `jamesbeard.jpg`; (c) live menu prices for non-grid items (short ribs, pork belly, broccolini) — these are referenced in reviews but no price is verified.
5. **Assets reusable from current site (Toast CDN):** chef photo (`jamesbeard.jpg`), map image (`misskimmap2020.3_*.webp`), "Friends eating together" interior shot, KFC close-up, overhead table spread. Use these first before commissioning new photography.
6. **Accessibility:** tel:, mailto:, and map href must be present. Hours section must be semantic (not an image). Quote attributions must be accessible (not just visual).
