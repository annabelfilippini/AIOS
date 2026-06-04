---
prospect: hop-alley
date: 2026-04-15
purpose: Canonical copy spec for /audit-redesign Phase A (Stitch) and Phase B (agent rebuild). Every fence below is binding — Stitch and the agent must reproduce verbatim.
fact_source: prospects/hop-alley/facts/verified-facts.md
brand_source: prospects/hop-alley/branding.json
audit_source: prospects/hop-alley/audit.md
---

# Hop Alley — Homepage Redesign Spec

## Brand tokens (from branding.json)

- Background: `#000000` (true black ground)
- Magenta primary: `#FA00D9`
- Magenta accent: `#FB04E7` (use sparingly — links + hovers)
- Off-white text on dark: `#F2F2F2`
- Muted body on dark: `#A6A6A6`
- Display headings: DIN Condensed (heading) + Brandon Grotesque (display caps)
- Body: Raleway 400/500/600
- Wordmark "HOP ALLEY": magenta neon outline (signature — must survive)

## Brand DNA — must survive

1. **Magenta neon wordmark on black.** Hero treatment cannot lose this. It is the brand.
2. **ALL-CAPS punchy house voice.** "WE ACCEPT TAKE OUT ORDERS OVER THE PHONE AT 3:30P" stays as a tone reference — not the hero, but the voice.
3. **Awards confidence.** Seven accolades stay above the fold. They earn it.
4. **Chinatown history weight.** The ghosted "Denver Chinatown / Original / Torn Down" block elevates to an editorial section, not background pattern.
5. **Photography is the only saturated color.** Magenta is chrome accent only — food and interior photos carry chroma. (Reference: fatcow.)

## Layout grid

- Max content width: 1280px
- Section padding: 120px top/bottom desktop, 64px mobile
- Two-column splits: 50/50 with 80px gutter

---

=== SECTION 1: NAV ===
Sticky black nav bar, height 72px. Logo left (small magenta wordmark), nav links right.

Nav links (text only, ALL CAPS, Raleway 600 12px, letter-spacing 0.12em):
- `DO NOT REWRITE: "MENUS"`
- `DO NOT REWRITE: "CHEF'S COUNTER"`
- `DO NOT REWRITE: "ABOUT"`
- `DO NOT REWRITE: "PRESS"`
- `DO NOT REWRITE: "GALLERY"`
- `DO NOT REWRITE: "RESERVATIONS"` (rendered as magenta pill button, 36px height, 16px horizontal padding)

Audit tag: `DO NOT REWRITE: "FIX — One H1 + clean heading hierarchy"` (color: yellow) — anchored to nav, calls out the H1 cleanup happening below.

=== SECTION 2: HERO ===
Full-viewport black ground. Centered stack:

Wordmark (signature): `DO NOT REWRITE: "HOP ALLEY"` rendered as oversized magenta neon outline, ~120px desktop, letter-spacing 0.18em. This is the brand — do not replace with text-styled H1.

Beneath wordmark, three lines of stacked copy, centered, max-width 720px:

Eyebrow: `DO NOT REWRITE: "DENVER · RINO · SINCE 2015"`

Headline (H1, this is the ONLY H1 on the page — fixes Audit T1):
`DO NOT REWRITE: "Denver's Michelin Bib Gourmand Sichuan kitchen."`

Subhead:
`DO NOT REWRITE: "Three-time Bib Gourmand. James Beard semifinalist. Regional Chinese cooking with the heat dialed in, served on the bones of the original Denver Chinatown."`

CTA row (two buttons side by side, 24px gap):
- Primary (magenta fill): `DO NOT REWRITE: "Reserve a table"` → href `https://www.exploretock.com/hop-alley-denver`
- Secondary (magenta outline): `DO NOT REWRITE: "Order takeout"` → href `https://www.toasttab.com/hop-alley/v2/online-order`

Below the CTA row, one line of small muted body text:
`DO NOT REWRITE: "Mon–Sat · 5–10pm · Closed Sundays · 720-379-8340"`

Audit tag: `DO NOT REWRITE: "NEW — Category + place + Bib Gourmand in the H1"` (color: green)

=== SECTION 3: AWARDS RAIL ===
Below hero, full-width black band with 1px magenta-tinted top/bottom borders. 7 award rows, monospaced-ish layout: year (left, DIN Condensed 32px magenta) + award title (center, Raleway 500 16px white) + body source line (right, Raleway 400 12px muted).

Eyebrow above the rail: `DO NOT REWRITE: "ACCOLADES"`

Awards (verbatim from verified-facts.md):

Row 1: `DO NOT REWRITE: "2025 — James Beard Semifinalist · Outstanding Wine & Beverage"`
Row 2: `DO NOT REWRITE: "2025 — Michelin Exceptional Cocktails Award"`
Row 3: `DO NOT REWRITE: "2025 — Michelin Bib Gourmand"`
Row 4: `DO NOT REWRITE: "2024 — Michelin Bib Gourmand"`
Row 5: `DO NOT REWRITE: "2023 — Michelin Bib Gourmand"`
Row 6: `DO NOT REWRITE: "2020 — James Beard Semifinalist · Best Chef Mountain Region"`
Row 7: `DO NOT REWRITE: "2016 — 5280 #1 Restaurant in Denver/Boulder"`

Below the rail, small note:
`DO NOT REWRITE: "Three-peat Bib Gourmand: 2023, 2024, 2025."`

Audit tag: `DO NOT REWRITE: "FIX — Structured awards (machine-readable)"` (color: yellow, positioned offset so it doesn't overlap any row)

=== SECTION 4: THE CHINATOWN STORY ===
Editorial two-column. Left: oversized condensed display caps phrase, ghost-magenta on black. Right: short paragraph in Raleway 400 17px line-height 1.7.

Display phrase (left column — make this the visual anchor, ~80px DIN Condensed, magenta outline only, no fill):
`DO NOT REWRITE: "DENVER'S CHINATOWN. ORIGINAL. TORN DOWN."`

Right column body:
`DO NOT REWRITE: "In 1880, Denver's Chinatown stood on Wazee Street — boarding houses, opium dens, joss houses, and a network of alleyways including the original Hop Alley. On Halloween night, an anti-Chinese mob of 3,000 leveled it. We took the name on purpose. The food is regional Sichuan and Northern Chinese. The setting is a quiet act of remembrance."`

Below the body, a small attribution line:
`DO NOT REWRITE: "Read more in our /about page."`

Audit tag: `DO NOT REWRITE: "SIGNATURE — Chinatown story made editorial"` (color: blue)

=== SECTION 5: MENU PREVIEW (REPLACES CANVA PDFS) ===
Two-column layout. Left column: eyebrow + headline + subhead + five menu buttons (CTA-styled magenta-outline pills, ~44px height, 20px padding, 12px gap, wraps to two rows on mobile). Right column: 1px magenta-tinted divider, sub-eyebrow, verbatim dish list, short MP footnote.

Eyebrow: `DO NOT REWRITE: "MENU"`
Section headline: `DO NOT REWRITE: "What we're cooking."`
Subhead (muted body, one line): `DO NOT REWRITE: "Five menus. Updated seasonally."`

Five menu buttons (each an `<a>` with href `#menus`, matching the original site's five-menu pattern):
`DO NOT REWRITE: "Main Menu"` `DO NOT REWRITE: "Vegan"` `DO NOT REWRITE: "Pescatarian"` `DO NOT REWRITE: "Vegetarian"` `DO NOT REWRITE: "Gluten-Free"`

Right column divider (1px magenta-tinted line, 32px margin top/bottom) followed by sub-eyebrow:
`DO NOT REWRITE: "FEATURED DISHES"`

Dish list (verbatim names + prices from verified-facts.md). Format each row as: dish name (bold) + " · " + dietary tags (small caps muted) + price (right-aligned magenta):

`DO NOT REWRITE: "Wood Grilled Gai Lan · GF · $30"`
`DO NOT REWRITE: "Fried Wontons · $17"`
`DO NOT REWRITE: "Wood Grilled Pork Chop · GF · $57"`
`DO NOT REWRITE: "Infamous Duck Roll · MP"`
`DO NOT REWRITE: "Bone Marrow Fried Rice · MP"`
`DO NOT REWRITE: "La Zi Ji · MP"`
`DO NOT REWRITE: "Beijing Duck Rolls · MP"`
`DO NOT REWRITE: "Chilled Tofu · V · MP"`
`DO NOT REWRITE: "Soft Shell Crab · P · MP"`
`DO NOT REWRITE: "Pork Dumplings · MP"`
`DO NOT REWRITE: "Hong You Chao Shou · MP"`
`DO NOT REWRITE: "Garlic Shrimp Noodles · P · MP"`
`DO NOT REWRITE: "Dan Dan Noodles · MP"`
`DO NOT REWRITE: "Mapo Tofu · V · MP"`

Below the list, one short line:
`DO NOT REWRITE: "MP — market price."`

Audit tag: `DO NOT REWRITE: "FIX — Real menu buttons (no more Canva PDFs)"` (color: yellow)

=== SECTION 6: CHEF'S COUNTER ===
Two-column. Left: large landscape interior photo of the chef's counter (use scrape image of the dining room — counter visible). Right: editorial copy block.

Eyebrow: `DO NOT REWRITE: "SIX SEATS · NIGHTLY"`
Headline: `DO NOT REWRITE: "The Chef's Counter."`

Body:
`DO NOT REWRITE: "A six-seat tasting room tucked off the main dining room. Currently anchored by Chef Doug Rankin (formerly of Bar Chelou, Pasadena) — multi-course, wine-paired, à-la-minute cooking three feet from the pass."`

Pull-quote:
`DO NOT REWRITE: "TLDR: the Chef's Counter experience with Chef Douglas and Somm. Jacob was MAGICAL. Can't wait to come back to eat à la carte in the dining room!"`
Attribution:
`DO NOT REWRITE: "— Rie U., Yelp Elite, March 2026"`

CTA (magenta fill): `DO NOT REWRITE: "Book the counter on Tock"` → href `https://www.exploretock.com/hop-alley-denver`

Audit tag: `DO NOT REWRITE: "NEW — Dedicated Chef's Counter section"` (color: green)

=== SECTION 7: PRESS WALL ===
Single horizontal row of 5 publication wordmarks (text-styled if logos unavailable), centered on black ground. Below, one row of pull-quotes in italic.

Eyebrow: `DO NOT REWRITE: "IN THE PRESS"`

Logos row (text-rendered, Brandon Grotesque caps 14px, muted, 60px gap between):
`DO NOT REWRITE: "5280"` · `DO NOT REWRITE: "WESTWORD"` · `DO NOT REWRITE: "THE DENVER POST"` · `DO NOT REWRITE: "MICHELIN GUIDE"` · `DO NOT REWRITE: "STANLEY MARKETPLACE"`

Below the row, one rotating-feel pull-quote (static in mockup):
`DO NOT REWRITE: "Hop Alley Still Has It 10 Years In."`
Attribution: `DO NOT REWRITE: "— 5280 Magazine"`

Outbound CTA (text link, magenta underline): `DO NOT REWRITE: "See our Michelin Guide listing →"` → href `https://guide.michelin.com/`

Audit tag: `DO NOT REWRITE: "NEW — Press wall + Michelin Guide link"` (color: green)

=== SECTION 8: ABOUT — TOMMY LEE ===
Two-column, image left (square portrait, 35% width max — per QA rule), copy right.

Eyebrow: `DO NOT REWRITE: "OWNER · CHEF"`
Headline: `DO NOT REWRITE: "Tommy Lee."`

Body:
`DO NOT REWRITE: "Hop Alley opened in late 2015 on the site Denver's original Chinese community once called home. Tommy Lee is a 2026 James Beard Award semifinalist for Outstanding Restaurateur and a 2020 Best Chef: Mountain Region semifinalist. He cooks regional Chinese — Sichuan-leaning — and has spent a decade building a coaching tree of Denver chefs."`

Small text below: `DO NOT REWRITE: "Follow @tommyminglee on Instagram."`

Audit tag: `DO NOT REWRITE: "NEW — Chef bio (Tommy Lee surfaced)"` (color: green)

(NOTE for Phase B: portrait image — use placeholder grey block if no clean Tommy Lee photo in scrape. Do not invent or pull from external CDN.)

=== SECTION 9: REVIEWS ===
Three-card row, all dark cards with thin magenta top border. Each card: pull-quote (italic, Raleway 400 18px), attribution (small caps muted).

Eyebrow: `DO NOT REWRITE: "WHAT GUESTS SAY"`

Card 1:
Quote: `DO NOT REWRITE: "Beijing Duck Roll cannot be recommended enough — refreshing and easy to share."`
Attribution: `DO NOT REWRITE: "Samantha B. · Yelp · Dec 2025"`

Card 2:
Quote: `DO NOT REWRITE: "Hop Alley is definitely one of my more favorite places to eat in Denver and in the city, worthy of its Bibs. Hip hop vibes between the art and music."`
Attribution: `DO NOT REWRITE: "Will X. · Yelp Elite · Nov 2025"`

Card 3:
Quote: `DO NOT REWRITE: "Interesting, inventive Chinese joint catering towards a memorable dining experience."`
Attribution: `DO NOT REWRITE: "Yelp reviewer · Aug 2025"`

Audit tag: `DO NOT REWRITE: "NEW — Verified review pull-quotes"` (color: green)

=== SECTION 10: FAQ ===
Stacked accordion list, 5 rows. Magenta plus-icon on the right. Each row: question (Raleway 600 17px white) + answer (Raleway 400 16px muted, revealed on click). In the mockup, render the first one expanded so the pattern is visible.

Eyebrow: `DO NOT REWRITE: "FREQUENTLY ASKED"`

Q1 (expanded):
Question: `DO NOT REWRITE: "Does Hop Alley have a Michelin star?"`
Answer: `DO NOT REWRITE: "No. Hop Alley is a Michelin Bib Gourmand restaurant — recognized in 2023, 2024, and 2025 — which honors restaurants offering exceptional food at moderate prices. Bib Gourmand is a separate distinction from the Michelin star rating."`

Q2:
Question: `DO NOT REWRITE: "Is the tasting menu the same as the Chef's Counter?"`
Answer: `DO NOT REWRITE: "Yes. Our tasting menu is served exclusively at the six-seat Chef's Counter, currently anchored by Chef Doug Rankin. Reservations through Tock."`

Q3:
Question: `DO NOT REWRITE: "What are your hours?"`
Answer: `DO NOT REWRITE: "Monday through Saturday, 5pm to 10pm. Closed Sundays. Takeout phone orders open at 3:30pm; online ordering opens at 5pm."`

Q4:
Question: `DO NOT REWRITE: "Can you accommodate dietary restrictions?"`
Answer: `DO NOT REWRITE: "Yes. We publish dedicated vegan, vegetarian, pescatarian, and gluten-free menus alongside the main menu. For severe allergies, please call the restaurant — online orders cannot accommodate allergy modifications."`

Q5:
Question: `DO NOT REWRITE: "Where do I make a reservation?"`
Answer: `DO NOT REWRITE: "Reservations are through Tock at exploretock.com/hop-alley-denver — including for the Chef's Counter and large parties of 9 or more."`

Audit tag: `DO NOT REWRITE: "NEW — FAQ (answers AI search, fixes Tock vs Resy mix-up)"` (color: green)

=== SECTION 11: VISIT (FOOTER LEAD-IN) ===
Three-column on a black ground. Each column: small caps eyebrow + content.

Column 1 — ADDRESS:
Eyebrow: `DO NOT REWRITE: "FIND US"`
Content: `DO NOT REWRITE: "3500 Larimer Street\nDenver, CO 80205\nRiNo · Five Points"`

Column 2 — HOURS:
Eyebrow: `DO NOT REWRITE: "WHEN WE'RE OPEN"`
Content: `DO NOT REWRITE: "Mon–Sat · 5–10pm\nClosed Sundays\nTakeout phone: 3:30pm\nOnline orders: 5pm"`

Column 3 — CONTACT:
Eyebrow: `DO NOT REWRITE: "GET IN TOUCH"`
Content: `DO NOT REWRITE: "720-379-8340\ninfo@hopalleydenver.com\nReservations via Tock"`

Audit tag: `DO NOT REWRITE: "FIX — Takeout, delivery & contact in one block"` (color: yellow)

=== SECTION 12: FOOTER ===
Slim black bar. Left: small magenta "HOP ALLEY" wordmark. Center: 4 social SVG icons (Instagram, Facebook only — no IG embed grid). Right: legal text.

Social icons (inline SVG only, no emoji, no text abbreviations):
- Instagram → href `https://instagram.com/hopalleydenver`
- Facebook → href `https://facebook.com/`

Legal: `DO NOT REWRITE: "© 2026 Hop Alley · Denver, CO"`

Audit tag: `DO NOT REWRITE: "FIX — Stale 2022 Instagram embed replaced with live link"` (color: yellow)

---

## What was REMOVED from the current site (and why)

| Removed | Why |
|---|---|
| Stale May 2022 Instagram embed (4 hand-picked posts) | Audit T4 — Replaced with live IG link in footer. |
| 5 Canva PDF menu links above the fold | Audit S1, AX1 — Replaced with inline menu preview + dietary filter. PDFs stay accessible via Menus tab for now. |
| Self-link broken delivery CTA | Audit T3 — Removed entirely; future Section will route through Toast online order. |
| Three-paragraph takeout explainer | Audit C4 — Compressed to one line in hero subhead + Visit column. |
| "FOLLOW US" H1 | Audit T1 — Demoted; only one H1 (the Sichuan kitchen tagline). |
| Operational notice "WE ACCEPT TAKE OUT ORDERS OVER THE PHONE AT 3:30P" as hero | Audit C2, C6 — Voice preserved in subhead/Visit, not above the wordmark. |

## What was ADDED (audit-driven net-new)

| Added | Audit ref |
|---|---|
| Single H1 with category + place + Bib Gourmand framing | T1, C2, C6, S2 |
| Structured awards rail (year + award + source) | A2 |
| Chinatown story as editorial section | C5 (signature elevation) |
| Inline menu preview with dietary tags | S1, AX1, A1 |
| Dedicated Chef's Counter section + Doug Rankin name | S4, C3, A3 |
| Press wall + Michelin Guide outbound link | C5, S6 |
| Tommy Lee bio block | S3, A3 |
| Three verbatim review pull-quotes | C5, A7 |
| 5-question FAQ accordion | A4, S5, C1 |
| Three-column Visit block (address, hours, contact) | C4, T3 |
| SVG social icons (no emoji, no text "IG/FB") | Brand polish |

## Phase B notes for the agent

- **Wordmark rendering.** The "HOP ALLEY" hero wordmark is the brand. Render with `-webkit-text-stroke: 2px #FA00D9; color: transparent;` on Brandon Grotesque (or DIN Condensed) at ~120px desktop, ~64px mobile. Do not import Stitch's placeholder treatment.
- **No imagery beyond what's in scrape/screenshots and verified Yelp gallery URLs.** No invented stock food photos. If a section needs imagery and no asset exists, use a tasteful dark grey block with a one-line caption rather than a stock image.
- **No emoji anywhere.** SVG only for social icons. (Global rule from feedback memory.)
- **Single accent color.** Magenta `#FA00D9` is the only saturated color in the chrome. Photos carry food chroma. Do not introduce a second brand color (no orange, no green) for "energy."
- **Awards rail and FAQ are critical for AI discoverability.** Keep them text-heavy, not graphic — Perplexity needs to crawl them.
- **Mobile.** Two-column splits stack at 768px. Awards rail collapses to single-column rows. Menu preview becomes full-width single column. Nav condenses to magenta hamburger SVG.
- **NO Uncle Ramen section on this page.** Uncle Ramen is a separate property (uncleramen.com); it appears only in the internal audit.md as a companion finding.
