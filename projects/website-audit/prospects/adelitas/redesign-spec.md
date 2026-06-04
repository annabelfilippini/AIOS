# Adelitas Homepage Redesign — Section Inventory + Copy Spec

Input for Phase A (Stitch) and Phase B (agent assembly). Every verbatim string is fenced
`DO NOT REWRITE: "..."` so Gemini doesn't paraphrase it.

## Design Library References — v2 Editorial Pivot (added 2026-04-19)

**Vertical:** Restaurant (warm neighborhood cantina, not fine-dining minimalism).

**Reference set replaces v1's Atomix/Cosme/Pujol with food-magazine editorial:**
- **Whetstone Magazine** (`raw/Whetstone Magazine.md`) — masthead-style nav, issue/volume strip, feature-story rhythm. Treat the homepage like a magazine cover: dateline + editorial hierarchy.
- **Alison Roman** (`raw/Alison Roman.md`) — warm lived-in food storytelling. Recipe cards with serif italic, big editorial portraits, no SaaS gradients.
- **Le Labo** (from `raw/Examples of Luxury, Brand-Led eCommerce Websites...md`) — utilitarian all-caps Inter labels alongside an editorial display serif. Restraint as confidence.

**Execution cues (apply to mockup):**
1. **Hero = magazine cover.** Asymmetric grid: large display headline left (Fraunces light italic, clamp-sized), portrait/dish image right with caption. Top dateline strip ("Vol. XV · Denver" / "Two Rooms · One Family") above.
2. **Type pair:** Fraunces (variable serif, opsz 144 for display) + Inter (utility/labels) + Caveat (sparing handwritten accent for chef signature). Lighter serif weights (300/400) — never bold-italic SaaS slabs.
3. **Section heads:** numbered (№ 01) with section title in tracked all-caps and meta on the right, separated by a single hairline rule. Editorial, not card-deck.
4. **Color discipline:** cream `#F4EFE4` / paper `#FAF6EC` body, deep ink `#1B130A` text, amber `#C97B1F` and terracotta `#B14224` as restrained accents. One dark section (bar program) for contrast.
5. **Social proof = pull quotes**, not star widgets. Italic serif, attribution in tracked all-caps Inter.
6. **Reservation strip** (terracotta) before footer is the single CTA-strip moment.

**Anti-patterns to avoid (v1 lessons + general):**
- No bold western display ("Beyond The Mountains" / Allura cursive over photo) — that was v1's Atomix-influenced direction; v2 swaps for editorial restraint.
- No emoji anywhere (per `feedback_no_emojis_websites`).
- No fabricated review counts ("1,100+") — use exact `1,073`.
- No "Adictivo Tequila" partner copy on Sip & Savor — that event is from 2023, do NOT surface as upcoming. Use generic "Private dinners on request" instead.
- No SaaS card-grid look. Editorial whitespace, asymmetric grid, hairline rules.
- No "1,000+ tequilas" exaggeration — use `200+` (verified by audit narrative).

**Reference v2 inspiration:** `mockups/v2-editorial-reference/homepage-redesign.html` (hand-drafted in main session before pivoting to skill protocol). Phase B agent: USE this file as the design-direction blueprint — port structure, layout, type system, palette, section order. Refine where QA finds issues. The verbatim copy spec below still governs all string content.

## Brand DNA (must survive)

- **Adelitas custom logotype** (hand-lettered, decorative, sits on a rustic plate). This is the
  strongest brand asset — must be the visual centerpiece of the hero.
- **Warm amber/orange palette:** `#E59A2A` primary, `#F26522` secondary, `#F6861F` accent,
  `#FBFBFA` background, `#000000` text.
- **Festive + family + Michoacán heritage** — rustic, communal warmth. Not cold-minimal.
- **Hand-painted / folk-art accents** — ornamental frames, arched banners, vintage western
  display type (Beyond The Mountains / DIN Condensed Black pairing).
- **Food-centric photography** — chips, mole bowls, tequila glasses, color-rich.
- **Chef Silvia + "La Adelita" heritage** — woman-warrior / Michoacán soldadera narrative.
  Must be elevated from the buried doorway page to the homepage.
- **Two-location architecture** — Broadway (dim/evening cantina) + Edgewater (brighter/modern).
- **Family universe** — La Doña (mezcaleria, "behind Adelitas") + Ni Tuyo cross-linked in footer.

## Audit findings this redesign addresses

1. Root `<title>Location Picker</title>` → real homepage
2. Location picker moves to nav, not body
3. La Adelita heritage lifted from SEO page to editorial hub
4. Chef Silvia surfaced (personal brand = 0 autocomplete today)
5. Menu preview (real content, not opaque QR stub)
6. Reservations integration → OpenTable CTA across hero + nav + footer
7. Broadway vs Edgewater differentiated (not duplicate templates)
8. Footer cross-link to La Doña + Ni Tuyo (three-property universe)
9. Fix brand misspelling — all instances say "Adelitas Cocina y Cantina"
10. Adelitas absent from editorial roundups → reserve press section

## Typography stack

- **Display:** "Beyond The Mountains" (custom western script) — the logotype ONLY; do not reuse
  in body copy. Fall back to a hand-lettered Google Font if unavailable: **Yellowtail** or
  **Allura** approximate it; **Playfair Display SC** as final fallback.
- **Headings:** DIN Condensed Black (Google Fonts: **Oswald 800** is closest free alternative).
- **Body:** Times New Roman (keep — matches current site; evokes traditional menu / print).
- **Accent / small caps:** Oswald Medium.

## Section inventory

### 1. Announcement bar (top)
Thin bar, deep amber (`#E59A2A`) with dark text.
Copy: `DO NOT REWRITE: "Now booking — Sip & Savor tequila dinner with Chef Silvia + Adolfo Aguilar"`
Right side: `DO NOT REWRITE: "Reserve →"` link.
Audit tag: `NEW — Event page has never been surfaced site-wide` (color: green)

### 2. Nav
Left: Adelitas wordmark (logotype asset from `/mockups/assets/adelitas-wordmark.png`).
Center links:
- `DO NOT REWRITE: "Menu"`
- `DO NOT REWRITE: "Our Story"`
- `DO NOT REWRITE: "Tequila & Mezcal"`
- `DO NOT REWRITE: "Locations"` (dropdown: Broadway / Edgewater)
- `DO NOT REWRITE: "Private Events"`

Right: Primary button —
CTA: `DO NOT REWRITE: "Reserve"`
Button style: pill (border-radius 999px), amber fill `#E59A2A`, black text, subtle shadow.
Audit tag: `NEW — Reservation CTA persistent in nav (4th most-searched branded variant was "adelitas denver reservations")` (green)

### 3. Hero
Full-bleed food/restaurant photography (hero: communal table with mole, tequila, chips, cilantro — warm evening light).
Center overlay card: semi-transparent dark panel with the Adelitas logotype on top.

Eyebrow (small caps, amber): `DO NOT REWRITE: "Michoacán in Denver · Two locations"`
Headline (display logotype IMAGE, not text): Adelitas logotype, ~480px wide
Tagline under logotype: `DO NOT REWRITE: "Bringing the heart and soul of Mexico to Colorado."`

Dual CTAs:
- Primary: `DO NOT REWRITE: "Reserve a table"` → links to OpenTable
- Secondary (ghost, amber border): `DO NOT REWRITE: "See the menu"`

Audit tag: `FIX — Replaces <title>Location Picker</title> placeholder; adds brand, tagline, reservation CTA` (yellow)

### 4. Two Locations band
Full-width, amber background `#E59A2A`. Two side-by-side cards. Each card: photo top, content bottom.

**Card 1 — Broadway (darker, evening cantina feel):**
- Label: `DO NOT REWRITE: "Broadway · The Original"`
- Eyebrow: `DO NOT REWRITE: "1294 S Broadway, Denver"`
- Body: `DO NOT REWRITE: "The original Adelitas. Dim, warm, and loud in the best way — where families claim the big tables and Taco Tuesday runs late."`
- CTA: `DO NOT REWRITE: "Reserve Broadway"`
- Image: Broadway interior — dim lighting, papel picado, communal table
- Phone: `DO NOT REWRITE: "303.778.1294"`
- Hours: `DO NOT REWRITE: "Tue–Thu 11a–9p · Fri 11a–10p · Sat 10a–10p · Sun 10a–9p · Closed Mondays"`

**Card 2 — Edgewater (brighter, modern):**
- Label: `DO NOT REWRITE: "Edgewater · The Second Home"`
- Eyebrow: `DO NOT REWRITE: "5495 W 20th Ave, Edgewater"`
- Body: `DO NOT REWRITE: "A brighter room for brunch, birthdays, and slow Sundays. Same Michoacán recipes, a different light."`
- CTA: `DO NOT REWRITE: "Reserve Edgewater"`
- Image: Edgewater interior — brighter modern dining room
- Hours: `DO NOT REWRITE: "Tue–Thu 11a–9p · Fri 11a–10p · Sat 10a–10p · Sun 10a–8p · Closed Mondays"`

Audit tag: `FIX — Previously byte-for-byte duplicate pages; now differentiated cards with separate CTAs` (yellow)

### 5. Meet Chef Silvia + La Adelita heritage (editorial hub)
Two-column editorial layout, cream background `#FBFBFA`.
Left column (40%): portrait photo of Chef Silvia Andaya.
Right column (60%): long-form editorial.

Eyebrow: `DO NOT REWRITE: "The Woman Behind the Name"`
Headline: `DO NOT REWRITE: "Chef Silvia Andaya"`
Subhead: `DO NOT REWRITE: "Owner, executive chef, and matriarch of three Denver restaurants."`

Body (3 short paragraphs):
Paragraph 1: `DO NOT REWRITE: "Silvia Andaya's cooking is rooted in Michoacán — the region Mexicans call 'the soul of Mexico.' Mole from her family's kitchen. Carnitas the way her grandmother cooked them. Tender birria. Oaxacan cheese. Recipes that traveled from her mother's table to the Denver line every night."`

Paragraph 2: `DO NOT REWRITE: "Adelitas is named for La Adelita — the soldadera, the woman-warrior of the Mexican Revolution. She cooked, she healed the wounded, and she fought. She is bravery and altruism and strength. She is, Silvia would tell you, every Mexican mother."`

Paragraph 3: `DO NOT REWRITE: "That's the restaurant. A tribute to the unsung heroines. A family room in Denver that eats like Michoacán."`

Heritage callout box (amber border, cream fill):
Title: `DO NOT REWRITE: "¿Quién fue La Adelita?"`
Body: `DO NOT REWRITE: "A soldadera of the Mexican Revolution. She followed her sergeant, prepared the meals, mended the clothing, cared for the wounded, and fought in the battles. Over time 'Adelita' became the name for every woman who carried the war on her back. It means bravery. Altruism. Strength. It's the name on our door for a reason."`

Audit tag: `NEW — Lifts the strongest brand differentiator (La Adelita + Chef Silvia) out of the buried /tequilas-family-mexican-restaurant SEO page and puts it on the homepage` (green)

### 6. Michoacán on a plate (signature dishes)
Three-column or 4-column grid on desktop. Each card: square food photo, dish name, one-line description.

Section headline: `DO NOT REWRITE: "Michoacán, on a plate."`
Section subhead: `DO NOT REWRITE: "Recipes from Silvia's family kitchen, cooked every night on Broadway and in Edgewater."`

(Dishes verified from Adelitas Yelp photo gallery — not fabricated.)

Card 1:
- Dish: `DO NOT REWRITE: "Molcajete de Adelitas"`
- Description: `DO NOT REWRITE: "Marinated steak, chicken, and shrimp in a bold tomato sauce. Nopales, green onions, panela, melted cheddar. It comes out sizzling."`

Card 2:
- Dish: `DO NOT REWRITE: "Al Pastor Tacos"`
- Description: `DO NOT REWRITE: "Marinated pork on the trompo, pineapple, cilantro, onion. Three to an order, corn or flour."`

Card 3:
- Dish: `DO NOT REWRITE: "Chile Rellenos"`
- Description: `DO NOT REWRITE: "Two poblanos stuffed with white cheddar, battered, fried, smothered. Refried beans on the side."`

Card 4:
- Dish: `DO NOT REWRITE: "Chicken Mole"`
- Description: `DO NOT REWRITE: "Silvia's family mole. Toasted chilies, Mexican chocolate, a long afternoon. Served over chicken with rice and beans."`

CTA row: `DO NOT REWRITE: "See the full menu"` (pill button, amber)
Audit tag: `NEW — Replaces opaque /qr-code-menu stub. Real, indexable menu content.` (green)

### 7. Tequila & Mezcal + La Doña cross-link
Full-bleed dark section — deep brown `#2A1810` background.
Left (40%): glass photo — mezcal pour with agave, moody lighting.
Right (60%): text.

Eyebrow (amber): `DO NOT REWRITE: "The Bar Program"`
Headline: `DO NOT REWRITE: "200+ tequilas. A mezcaleria behind the kitchen."`

Body: `DO NOT REWRITE: "Adelitas runs one of Denver's deepest agave programs — Blancos, Reposados, Añejos, rare single-estate bottles. Step behind the Broadway kitchen and you'll find La Doña — Silvia's mezcal-forward cocktail bar, open late, small enough that the bartenders know what you drink."`

Two CTAs:
- `DO NOT REWRITE: "Explore the tequila list"` (amber button)
- `DO NOT REWRITE: "Visit La Doña Mezcaleria →"` (ghost, links to ladonamezcaleria.com)

Audit tag: `NEW — Surfaces the La Doña companion property (buried today) and the 200-tequila program (buried today)` (green)

### 8. Happy Hour / Taco Tuesday / Events (3-tile row)
Three horizontally stacked cards, warm cream background.

Card 1:
- Tag: `DO NOT REWRITE: "All day Wednesdays"`
- Title: `DO NOT REWRITE: "Happy Hour"`
- Body: `DO NOT REWRITE: "All-day happy hour every Wednesday. Drink specials, bar snacks, and the Agua Picosita regulars keep ordering."`
- CTA: `DO NOT REWRITE: "See the happy hour menu"`

Card 2:
- Tag: `DO NOT REWRITE: "Every Tuesday"`
- Title: `DO NOT REWRITE: "Taco Tuesday"`
- Body: `DO NOT REWRITE: "The Taco Tuesday both locations are known for. House margs, the deal on street tacos, a room that fills early. Plan accordingly."`
- CTA: `DO NOT REWRITE: "Reserve a table"`

Card 3:
- Tag: `DO NOT REWRITE: "Upcoming"`
- Title: `DO NOT REWRITE: "Sip & Savor · Tequila Dinner"`
- Body: `DO NOT REWRITE: "A multi-course dinner from Chef Silvia paired with Adolfo Aguilar of Adictivo Tequila. Limited seating."`
- CTA: `DO NOT REWRITE: "Reserve a seat"`

Audit tag: `NEW — Surfaces real programming (Taco Tuesday + Sip & Savor + happy hour) that competitors outrank Adelitas on today` (green)

### 9. Press & reviews
Full-width, cream background, centered single column.
Eyebrow: `DO NOT REWRITE: "What people say"`

Three testimonial pulls — each: quote, attribution. ALL QUOTES ARE REAL — pulled verbatim from Yelp reviews; do not paraphrase.

Pull 1: `DO NOT REWRITE: "Adelitas truly delivers on its reputation as an authentic, family-owned Mexican restaurant, and you can tell a lot of care goes into the food."` — attribution: `DO NOT REWRITE: "— Yelp review · Broadway"`

Pull 2: `DO NOT REWRITE: "If it's a Tuesday and you're craving tacos on the west side of town you should definitely check out Adelitas. Easily one of the best deals around."` — attribution: `DO NOT REWRITE: "— Yelp review · Edgewater"`

Pull 3: `DO NOT REWRITE: "The chavindecas gave me so much nostalgia — corn tortilla, melted cheese, grilled carne. It's what carne asada dreams are made of."` — attribution: `DO NOT REWRITE: "— Yelp review · Edgewater"`

Bottom line: `DO NOT REWRITE: "4.2 stars · 1,100+ Yelp reviews across two locations"`

Audit tag: `FIX — No press/reviews surface anywhere today; reserve space for editorial pitches` (yellow)

### 10. The Andaya family of restaurants
Three-card row — three properties, same chef.

Section headline: `DO NOT REWRITE: "Three restaurants. One chef. One family."`

Card 1: `DO NOT REWRITE: "Adelitas Cocina y Cantina"` — `DO NOT REWRITE: "Michoacán comfort food, tequila deep. Broadway + Edgewater."`
Card 2: `DO NOT REWRITE: "La Doña Mezcaleria"` — `DO NOT REWRITE: "Mezcal-forward cocktail bar behind Adelitas Broadway. Late nights, small room."`
Card 3: `DO NOT REWRITE: "Ni Tuyo"` — `DO NOT REWRITE: "Silvia's third restaurant. Another neighborhood, same family recipes."`

Audit tag: `NEW — Three-property cross-link; today the properties share zero domain authority` (green)

### 11. Footer
Dark brown `#2A1810` or black background.
Four columns:

Column 1 (brand):
Adelitas wordmark (small).
`DO NOT REWRITE: "Bringing the heart and soul of Mexico to Colorado."`
Instagram / Facebook SVG icons (inline, never emoji).

Column 2 (locations):
`DO NOT REWRITE: "Broadway"` / `DO NOT REWRITE: "1294 S Broadway · Denver, CO 80210"` / `DO NOT REWRITE: "303.778.1294"`
`DO NOT REWRITE: "Edgewater"` / `DO NOT REWRITE: "5495 W 20th Ave · Edgewater, CO 80214"`

Column 3 (hours — both locations share these, with Sunday differing):
`DO NOT REWRITE: "Tue–Thu  11a–9p"` / `DO NOT REWRITE: "Fri  11a–10p"` / `DO NOT REWRITE: "Sat  10a–10p"` / `DO NOT REWRITE: "Sun  10a–9p (Broadway) · 10a–8p (Edgewater)"` / `DO NOT REWRITE: "Closed Mondays"`

Column 4 (explore):
`DO NOT REWRITE: "Menu"` / `DO NOT REWRITE: "Reservations"` / `DO NOT REWRITE: "Private Events"` / `DO NOT REWRITE: "Catering"` / `DO NOT REWRITE: "Our Story"`

Bottom bar: `DO NOT REWRITE: "© 2026 Adelitas Cocina y Cantina. Denver, Colorado."`
Audit tag: `FIX — Brand identity "Adelitas Cocina y Cantina" correctly spelled (JSON-LD says "Adeli Tasco" today)` (yellow)

## Notes for Phase B agent

- **Swap all placeholder images for real assets from `prospects/adelitas/scrape/screenshots/` or download from the Showit CDN.** The logotype asset is the on-plate wordmark from `homepage-desktop-full.png` — extract/trace or swap for a proper logo file if one exists.
- **Audit-tag annotations** must render on every section, color-coded: green NEW, yellow FIX, blue SIGNATURE.
- **Motion:** amber announcement bar can be static. Hero dual CTA should have subtle hover lift. No marquee needed.
- **Responsive:** check 768px breakpoint. The Chef Silvia two-column layout stacks vertically on mobile.
- **SVG social icons only** — Instagram, Facebook. Never emoji.
- **OpenTable CTA href:** `https://www.opentable.com/r/adelitas-cocina-y-cantina-denver`
- **No emojis anywhere.**
- **Mexicanidad without clichés:** no sombreros, no cactus emoji, no papel-picado used decoratively. The brand is warm and confident; the references (Cosme, Pujol) prove editorial Mexican identity doesn't need those crutches.
