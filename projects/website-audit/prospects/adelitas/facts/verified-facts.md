# Verified Facts — Adelitas Cocina y Cantina
Scraped 2026-04-14 (raw sources), consolidated 2026-04-16. Every fact cites a file in this directory or `../scrape/`.

## Sources
- ✓ Yelp (Broadway) — `facts/yelp-broadway.md`
- ✓ Yelp (Edgewater) — `facts/yelp-edgewater.md`
- ✓ Prospect site homepage — `../scrape/homepage.md`
- ✓ Prospect site Broadway page — `../scrape/broadway.md`
- ✓ Prospect site Edgewater page — `../scrape/edgewater.md`
- ✓ Prospect site /event — `../scrape/event.md`
- ✓ Prospect site /tequilas-family-mexican-restaurant — `../scrape/tequilas-family-mexican-restaurant.md`
- ✓ La Doña homepage (sister property) — `../companion/la-dona/scrape/homepage.md`
- ✗ Google Business Profile — reCAPTCHA-blocked (`facts/google-broadway-search.md`, `facts/google-edgewater-search.md`)
- ✗ OpenTable — not scraped; listing confirmed at `opentable.com/r/adelitas-cocina-y-cantina-denver` per audit

## Identity
- Legal / display name: **Adelitas Cocina Y Cantina**  [source: yelp-broadway.md, yelp-edgewater.md]
  - Note: JSON-LD on prospect site renders name as `"Adeli Tasco"` (space injected) — schema-level brand-identity bug, NOT an alternate spelling. Do NOT use anywhere in mockup. [source: audit.md]
- Cuisine / category: Mexican, Breakfast & Brunch, Cocktail Bars  [source: yelp-broadway.md]
- Price tier: $$  [source: yelp-broadway.md]
- Neighborhood (Broadway): Platt Park / Southwest Denver  [source: yelp-broadway.md "Southwest"; owner bio "Platt Park neighborhood"]

## Locations
### Broadway
- Address: **1294 S Broadway, Denver, CO 80210**  [source: yelp-broadway.md line 281-283; scrape/homepage.md]
- Phone: **303.778.1294**  [source: scrape/homepage.md line 12; scrape/seo-sample-best-mexican-food.md line 264; scrape/tequilas-family-mexican-restaurant.md line 216]
  - Published format is dot-separated. Match exactly. No parens, no hyphens.
- Google Maps: confirmed via adelitasco.com/broadway  [source: scrape/homepage.md line 12]

### Edgewater
- Address: **5495 W 20th Ave, Edgewater, CO 80214**  [source: yelp-edgewater.md line 197-199; scrape/homepage.md line 8]
- Phone: **303.778.1294** (shared number across both locations)  [source: scrape/homepage.md line 8]

## Hours

### Broadway  [source: yelp-broadway.md lines 289-301]
- Mon: Closed
- Tue–Thu: 11:00 AM – 9:00 PM
- Fri: 11:00 AM – 10:00 PM
- Sat: 10:00 AM – 10:00 PM
- Sun: 10:00 AM – 9:00 PM

### Edgewater  [source: yelp-edgewater.md lines 203-215]
- Mon: Closed
- Tue–Thu: 11:00 AM – 9:00 PM
- Fri: 11:00 AM – 10:00 PM
- Sat: 10:00 AM – 10:00 PM
- Sun: 10:00 AM – 8:00 PM  *(1 hour earlier close than Broadway)*

**Source conflict:** Yelp owner bio claims "brunch, lunch, and dinner 7 days a week" [source: yelp-broadway.md line 329], but Yelp hours panel on the same page shows Monday closed. Trust the hours panel (more recently maintained than the bio blurb). Do not claim "7 days a week" in mockup copy.

## Email
- **info@adelitasco.com**  [source: scrape/seo-sample-best-mexican-food.md line 264]

## Reservations / Booking
- OpenTable listing exists at `opentable.com/r/adelitas-cocina-y-cantina-denver`  [source: audit.md line 28]
- **Not integrated into site HTML** — no Resy/Tock/OpenTable/SevenRooms embed detected  [source: audit.md line 28; scrape-data.md line 62]
- In mockup: CTA "Reserve" should link directly to OpenTable URL above (that is the only real booking destination that exists today).

## Menu / Popular Dishes  [source: yelp-broadway.md lines 93-207 — Yelp "Popular Dishes" module, photo + review counts]
- Carne Asada Tacos (13 photos, 31 reviews)
- Puerco Con Chile Colorado (9 photos, 17 reviews)
- Tres Leches Cake (6 photos, 14 reviews)
- Chile Rellenos (7 photos, 24 reviews)
- Al Pastor Tacos (10 photos, 22 reviews)
- Chips and Salsa Trio (2 photos, 17 reviews)
- Street Tacos (1 photo, 23 reviews)
- Queso Fundido (7 photos, 14 reviews)

Do NOT fabricate menu descriptions, prices, or dish descriptors beyond what Yelp surfaces. Prospect's own `/qr-code-menu` page has zero HTML content [source: audit.md line 27] — cannot cite menu detail beyond the popular-dish names above.

## Reviews
- Aggregate: **4.2 stars / 1,073 Yelp reviews** (Broadway)  [source: yelp-broadway.md line 10 "4.2 (1.1k reviews)", line 437 "1073 reviews"]
  - Use `1,073` exact count, not the rounded "1.1k" or the v1 mockup's invented "1,100+".
- Aggregate: **45 Yelp reviews** (Edgewater)  [source: yelp-edgewater.md line 278]

### Verified Review Quotes (verbatim)

1. "Think taco quality of a good street taco spot but with the ambiance of a cute tex mex bar." — Sarah W., Yelp (Broadway), 2026-02-22  [source: yelp-broadway.md line 581]
2. "Yum yum and more yum. This place is incredible for every reason a successful restaurant thrives! Service Food Prices Quality . Everything we ordered was a hit!" — Le H., Yelp (Broadway)  [source: yelp-broadway.md line 1181-1183]
3. "One of the best Mexican restaurants ever!!! Five stars and then some!!! Very reasonably priced, amazing service, and delicious food." — Nikki D., Yelp (Broadway), 2025-12-19  [source: yelp-broadway.md lines 1960, 1982]
4. "The ambiance is lively and welcoming, making it a great spot for a casual night out or a group dinner." — Kathleen K., Yelp (Broadway), 2026-01-29  [source: yelp-broadway.md lines 2694, 2716]
5. "Always yummy, great service and chill ambiance. They now offer all day happy hour on Wednesdays!" — Deborah M., Yelp (Broadway), 2026-01-21  [source: yelp-broadway.md lines 3378, 3410]
6. "The chile rellenos were excellent! Two peppers stuffed with white cheddar and then battered and fried." — Casey D., Yelp (Broadway), 2026-01-31  [source: yelp-broadway.md lines 1624, 1658]

### Mixed / Negative Signal (audit-only, do NOT use in mockup)
- One recent 2026-04-01 review dropped from 5 stars: "YUGE let down. Flavorless food, shipped in from Sysco - doctored up to look fancy." — Elizabeth M.  [source: yelp-broadway.md lines 909, 921-923]. Relevant to "quality-slipped?" hypothesis in audit; never appears in redesign copy.

## Team
- **Silvia Andaya** — owner and executive chef; founder of Adelitas and La Doña Mezcaleria  [source: yelp-broadway.md lines 321-329 (Yelp "Business Owner" block, first-person bio); companion/la-dona/scrape/homepage.md line 4 "matriarch owner and head chef of Adelitas Cocina Y Cantina"]
  - Heritage: Michoacán, Mexico — "traditional Mexican food from the state of Michocan, Mexico" (spelling from source)  [source: yelp-broadway.md line 327-329]
  - Additional narrative: Adelita / woman-warrior / Michoacán roots  [source: scrape/tequilas-family-mexican-restaurant.md — buried inside SEO doorway page per audit.md]
- **Amarillo / Chio Aguilar** — appears on broadway.md, edgewater.md, qr-code-menu.md; role not stated in raw scrape  [source: scrape/broadway.md line 1590; scrape/edgewater.md line 1590]. Do NOT assign a role in mockup without further verification.

## Press / Editorial
- No press coverage verified in current scrape set. Audit notes Uncover Colorado mentions Michoacán food, but source not scraped.  [source: audit.md line 53]
- **Do not invent press logos or publication names.**

## Programming / Events

### Sip & Savor tequila dinner
- **Event name:** "Adelitas Sip & Savor"  [source: scrape/event.md line 12]
- **Date on page:** Monday, November 13, 2023, 6:00 PM, $125 per person  [source: scrape/event.md lines 46-52]
  - **This is a PAST event.** The /event page has not been updated in ~2.5 years. Do NOT present as active/upcoming in the redesign without confirming with Annabel whether a current event exists.
- Chefs: Silvia Andaya & **Adolfo Aguilar** (co-hosting chef)  [source: scrape/event.md line 12]
- Tequila partners on page: **Wild Common** and **Volans Tequila**  [source: scrape/event.md lines 6, 18]
  - ⚠️ v1 mockup copy used **"Adictivo Tequila"** — this is NOT in any source file. Fabricated. Correct names are Wild Common + Volans.

### Recurring (inferred from Yelp reviews only — soft citation)
- Taco Tuesday  [source: yelp-broadway.md line 581 (Sarah W.); line 3068 (Niles C.) "The taco Tuesday deal is so so hard to beat"]
- Happy hour, including all-day Wednesday  [source: yelp-broadway.md line 3410 (Deborah M.) "all day happy hour on Wednesdays"]
- Flag in mockup: use soft language ("guests mention Taco Tuesday and Wednesday happy hour") or verify with prospect before asserting as official programming.

## Sister Property (for context only — NOT Adelitas)
- **La Doña Mezcaleria** — 13 E Louisiana Ave, Denver, CO 80210  [source: companion/la-dona/scrape/homepage.md line 12]
- Hours: Tue–Thu 4 PM–9 PM, Fri–Sat 4 PM–10 PM, Sun–Mon CLOSED  [source: companion/la-dona/scrape/homepage.md line 16]
- Copy: "Mezcal-centric cocktail bar also serving Mexican street food in rustic digs behind Adelitas."  [source: companion/la-dona/scrape/homepage.md line 22]
- Same owner/chef (Silvia Andaya). Included here only because Adelitas audit recommends surfacing the shared-brand-universe story. Facts about La Doña belong in its own file if that property gets its own redesign.

## Amenities (Broadway)  [source: yelp-broadway.md lines 305-313]
- Offers take-out
- Takes reservations (platform: OpenTable — see Reservations section)
- Vegan options
- Many vegetarian options
- "38 More Attributes" listed on Yelp (not fully captured in scrape)

## Amenities (Edgewater)  [source: yelp-edgewater.md lines 219-225]
- Casual dress
- Validated parking
- Dogs allowed
- Outdoor seating

## Photography
- Yelp photo library: 855 Broadway photos, 82 Edgewater photos  [source: yelp-broadway.md line 23; yelp-edgewater.md line 185]
- Do not hotlink Yelp CDN (`s3-media0.fl.yelpcdn.com`) in the final mockup — license risk. Use prospect's own Showit assets or re-request photos from Silvia.

## Known fact gaps (remain `— (not verified)` until resolved)
- Year founded: — (not verified in any source)
- Exact menu prices: — (QR menu page has zero HTML; cannot verify)
- Current active events / promotions: — (prospect's /event is stale from Nov 2023)
- Press / editorial coverage: — (no press file scraped)
- Staff beyond Silvia Andaya, Adolfo Aguilar, and Amarillo/Chio Aguilar: — (not verified)
- Social media handles: — (not captured in current scrape)

Anything NOT listed above does NOT enter the mockup. If Phase 4 A2 finds a claim not cited here, it is a P0 bug.
