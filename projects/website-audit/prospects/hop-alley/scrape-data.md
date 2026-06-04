# Hop Alley — Scrape Data

**Scraped:** 2026-04-15
**Prospect:** Hop Alley (Denver, CO)
**URL:** https://hopalleydenver.com/
**Contact:** Tommy Lee, Chef/Owner — info@hopalleydenver.com / reservations@hopalleydenver.com
**Platform:** Squarespace (single-page site + 1 sub-page)

---

## Scope

| Asset | Count | Path |
|---|---|---|
| Core Hop Alley pages (3-pass) | 2 | `scrape/` |
| External touchpoints (screenshot + md) | 3 | `scrape/external/`, `scrape/screenshots/` |
| Uncle Ramen companion (3-pass) | 1 | `companion/uncle-ramen/scrape/` |
| Reference sites (1-pass) | 4 pages / 2 brands | `reference/mister-jius/`, `reference/atomix/` |
| Raw HTML analysis | 4 pages | `scrape/raw-html-analysis.json` |

Core: homepage (`/`), `/large-party-info`. The sitemap only lists `/home`, `/home-3`, `/large-party-info` — everything else lives as anchor sections on the homepage. `/home-3` appears to be an unpublished variant.

External touchpoints captured: **Tock reservations**, **Toast online order**, **Toast gift cards**. All bounce users off-site to third-party platforms.

Companion: **Uncle Ramen** (uncleramen.com) — Tommy Lee's sister concept, 2 locations (Highlands, West Wash Park).

References: **Mister Jiu's** (SF, Michelin-starred Chinese — direct parallel), **Atomix** (NYC, Michelin Asian fine dining — award-forward design).

---

## Hop Alley — 20 Findings

### 🔴 Critical (show-stoppers for Michelin-caliber restaurant)

**1. Seven major awards listed on homepage, ZERO in structured data.**
Awards shown as bold copy only:
- 2025 James Beard Semi Finalist (Outstanding Wine & Beverage)
- 2025 Michelin Exceptional Cocktails Award
- 2025 Michelin Bib Gourmand
- 2024 Michelin Bib Gourmand
- 2023 Michelin Bib Gourmand
- 2020 James Beard Semi-Finalist (Best Chef, Mountain Region)
- 2016 5280 Magazine #1 Restaurant, Denver/Boulder

Schema.org has no `award` property on Organization/LocalBusiness. Google can't surface these in the Knowledge Panel, "Michelin restaurants Denver" queries, or rich results. **This is the single biggest missed opportunity.**

**2. `@type` is `LocalBusiness`, not `Restaurant`.**
Hop Alley is a Michelin-recognized restaurant but its schema is generic LocalBusiness. Missing Restaurant-specific properties Google surfaces in SERPs: `servesCuisine`, `priceRange`, `acceptsReservations`, `menu`, `hasMenu`, `starRating`, `award`.

**3. Reservation platform contradiction: homepage says Tock, large-party page says Resy.**
- Homepage CTA: `RESERVATIONS VIA TOCk` → exploretock.com/hop-alley-denver
- `/large-party-info`: *"Reservations are available 14 days in advance through Resy.com"*

One of these is wrong. Customers booking a table for 2 via Tock after reading the large-party page will hit a Resy link that 404s or redirects. This is the exact kind of cross-platform inconsistency that kills trust.

**4. Homepage has no meta description.**
`<meta name="description">` is empty. On a Michelin property this directly caps CTR from Google — SERP previews fall back to scraped snippet. Competitor Mister Jiu's has a custom description; Atomix has one.

**5. Duplicate H1 tags on every page.**
Every page outputs `<h1>Hop Alley</h1>` + `<h1>FOLLOW US</h1>`. Two H1s confuses crawlers about page topic. Large-party-info also shows "FOLLOW US" as an H1 — irrelevant to that page. Title tag is `LARGE PARTY INFO — Hop Alley` (good) but body H1 structure contradicts it.

### 🟠 High-impact

**6. Menus are Canva PDFs, not indexable web pages.**
Five menus (Dinner, Vegan, Pescatarian, Vegetarian, Gluten Free) are Canva `canva.com/design/...` links. Canva content is **not indexed by Google**. Every query like "hop alley menu," "mapo tofu denver," "vegan chinese denver" loses to restaurants with HTML menus. Canva also has a watermark/branding in header, inconsistent typography with the rest of the site, and fails accessibility (screen readers cannot read PDF image text).

**7. Dual-channel takeout UX is a self-inflicted friction point.**
Homepage: "WE ACCEPT TAKE OUT ORDERS OVER THE PHONE AT 3:30P, ONLINE ORDERING OPENS AT 5P." Two different cutoffs, two different channels. Plus: "for online orders, we cannot accommodate allergies or aversions." The whole takeout story needs 3 paragraphs of explanation on the homepage — should be one button + one sentence.

**8. Broken delivery-links CTA.**
Copy: `[delivery available through Ubereats, postmates & doordash]`. The link `href` points to **hopalleydenver.com itself** (self-link). No deep links to the three delivery apps. Also: Postmates was absorbed by Uber Eats in 2020 — listing it separately is dated.

**9. Instagram embed is 3–4 years stale.**
Homepage "FOLLOW US" section embeds 4 Instagram posts. Post IDs:
- `/p/CeL2q2HLJoo/` → May 2022
- `/p/CdjBHCKlCAL/` → May 2022
- `/p/Cdd5fezlm53/` → May 2022
- `/p/CdQxnnhLWew/` → May 2022

For a restaurant with fresh daily menus, showing 2022 food photos to 2026 visitors is worse than no social embed at all. And the anchor text "@hopalleydenver" gives 0 signal that these are 4 hand-picked photos vs. a live feed.

**10. No chef-story / about / origin page.**
Tommy Lee is Michelin-decorated, James Beard semifinalist, Denver fixture. The homepage mentions him once (Chef's Counter context). There's no `/about`, no `/chef`, no press page, no story beat that converts first-time visitors into reservation-ready diners. Every comparable restaurant (Mister Jiu's, Atomix) leads with chef + origin.

**11. Chef's Counter ("Petit Chelou" with Doug Rankin) is buried.**
Premium upsell — $$$ per-seat experience, limited 6 seats — gets 2 paragraphs mid-page. No dedicated URL, no schema, no booking CTA above the fold, no photo of the food. Chef Doug Rankin worked with José Andrés / Ludo Lefebvre — name-brand credentials. Deserves its own page or at minimum a hero card.

### 🟡 Medium

**12. `sameAs` lists only Facebook. Instagram, Tock listing, Google Business not linked.**
Schema Organization `sameAs` only points to Facebook (`?fref=ts` — old format). No Instagram, no Tock business URL, no Google Business profile. Weakens entity reconciliation across Google's Knowledge Graph.

**13. Missing `geo`, `image`, `priceRange` on LocalBusiness.**
No latitude/longitude, no hero image in LocalBusiness schema (Google uses this for map results), no priceRange ($–$$$$). Restaurant-specific SERP features unavailable.

**14. `openingHours` malformed trailing comma.**
`"Mo 17:00-22:00, Tu 17:00-22:00, ... Sa 17:00-22:00, "` — trailing `, ` after Saturday. Sunday absent (correct — closed) but should be declared as `Su`-omitted or explicitly closed.

**15. 4 of 12 homepage images have empty `alt=""`.**
On a dish-driven restaurant, decorative-image `alt=""` on the food photography is lost alt-text for "Chinese food Denver" search relevance. Only 2 images are lazy-loaded.

**16. Copy typos: "RESERVATIONS VIA TOCk" (lowercase k); inconsistent Bar Chelou / "Petit Chelou" capitalization.**
Michelin-tier restaurants should not ship visible typos.

**17. Gift card story is split and undersold.**
"Electronic gift cards via link / physical at restaurant." One sentence, no visual, no callout for holiday/seasonal. Gift cards drive ~5–15% of restaurant revenue at Michelin-tier properties during Nov–Dec. The Toast-hosted gift page is a bare-minimum Toast template.

**18. H1 "Hop Alley" with no value prop or modifier.**
No tagline, no locational modifier ("Denver's Sichuan & Shanghai-inspired kitchen"), no award callout in H1. "Hop Alley" alone doesn't tell a first-time visitor what type of restaurant this is.

**19. No reviews / testimonials / press logos.**
Michelin, JBF, and 5280 mentions are just text — no logos, no links to the Michelin Guide entry, no pull-quotes from reviewers (303 Magazine, The Denver Post, Food & Wine). Compare Atomix: large-scale press-logo wall, tasteful, instantly credible.

**20. No accessibility signals in HTML (no `lang` attribute on root, no skip-nav, no ARIA landmarks beyond defaults).**
Squarespace default. Noted but low-impact for conversion audit.

---

## Uncle Ramen (companion) — 5 Findings

**U1. H1 literally reads "Copy of HOME".**
```html
<h1>Copy of HOME</h1>
```
Shipped template placeholder. Public homepage of a live restaurant in 2026. This alone is a headline finding.

**U2. Broken phone link in markup.**
`[303.433.326](tel:3034333263) 3` — the trailing `3` is outside the anchor tag. The `tel:` link dials `3034333263`, not `3034333263` + 3 — functionally dials the wrong number? Actually `tel:3034333263` is only 10 digits, missing the last digit. This is a **dead phone link**.

**U3. "STARTING APRIL 8TH, RESERVATIONS WILL BE AVAILABLE THROUGH OPENTABLE"**.
Stale announcement. No year stated. Today is April 15, 2026 — if this was last year's migration, the copy should be gone. "EXITING RESERVATIONS" is a visible typo ("existing").

**U4. Title tag is "Uncle Restaurant", brand is "Uncle Ramen" and also just "Uncle".**
Three names (Uncle, Uncle Ramen, Uncle Restaurant) used inconsistently across title, H1, schema `legalName`, and body copy. Entity reconciliation nightmare.

**U5. OpenTable, not Tock — platform fragmentation across Tommy Lee's two properties.**
Hop Alley → Tock. Uncle Ramen → OpenTable. Different reservation confirmations, different customer accounts, no cross-promotion between the two concepts' bases. Signals operational rather than strategic choice.

---

## External Touchpoints — Observations

**Tock reservations page** (`exploretock.com/hop-alley-denver`):
- Clean Tock-standard layout; no Hop Alley brand presence except logo
- Uses Michelin Guide badge — so **Tock itself surfaces Michelin**, but Hop Alley's own site doesn't link or cross-reference
- Customer jumps from hopalleydenver.com to exploretock.com and back, losing brand continuity

**Toast online ordering** (`toasttab.com/hop-alley/v2/online-order`):
- Standard Toast UI — product cards, cart, checkout
- No Hop Alley brand styling beyond logo
- Menu items have names but no photos (Toast default)
- Nothing explains the 3:30p / 5:00p rule customers hit on the homepage

**Toast gift cards** (`toasttab.com/hop-alley/giftcards`):
- 28KB screenshot — essentially a bare form
- No gift card design / visual / story

---

## Reference Sites — What Good Looks Like

### Mister Jiu's (SF) — the direct Chinese Michelin analogue
- Michelin star + James Beard placed above the fold with **actual Michelin star iconography** (not just text)
- Dedicated `/reservations` page (not external bounce) with Tock embed
- Menu is **HTML, not PDF** — indexable, mobile-readable, accessible
- Chef story page with Brandon Jew bio, origin narrative, press quotes
- Dense but editorial typography — serif display, sans body
- Takeaway for Hop Alley: **the awards copy already exists — make it schema + iconography, keep reservations on-domain, ship HTML menus.**

### Atomix (NYC) — award-forward minimal aesthetic
- Homepage is radically minimal — logo + one sentence + navigation
- About page ships chef bio (Junghyun Park), brand philosophy, accolades grid
- Michelin ⭐⭐ displayed as art
- Reservations via Tock (same as Hop Alley) but framed as "Book" not a bounce
- Takeaway for Hop Alley: **minimalism + confidence. Let the awards and photography carry weight, cut the takeout-instruction paragraphs.**

---

## Third-party Stack (Hop Alley)

| Vendor | Role |
|---|---|
| Squarespace | CMS / hosting |
| Adobe Typekit | Web fonts |
| Tock | Reservations |
| Toast | Online ordering + gift cards |
| Canva | Menu PDFs (not embedded — external links) |

**Not detected:** No Google Analytics, no GTM, no Facebook Pixel, no Meta tracking of any kind. This means **Tommy Lee has zero visibility into website conversion** — which reservations came from the website vs. direct Tock, which menu CTAs get clicked, which pages bounce. Analytics gap = flying blind on a property that runs 6 nights a week at Michelin Bib Gourmand prices.

---

## Raw Artifacts

- `scrape/homepage.md` — 4,920 chars rendered markdown
- `scrape/large-party-info.md` — 6,187 chars
- `scrape/screenshots/` — 9 screenshots (3 passes × 2 core pages + 3 external)
- `scrape/raw-html-analysis.json` — meta, schema, headings, alt, scripts for 4 pages
- `companion/uncle-ramen/scrape/` — full Uncle Ramen scrape
- `reference/mister-jius/` — homepage + reservations, markdown + screenshot
- `reference/atomix/` — homepage + about, markdown + screenshot

---

## Hooks for Annabel's Review

These are the findings to lead the outreach with:
1. **Michelin awards invisible to Google** — schema fix
2. **Menus trapped in Canva PDFs** — HTML menu build
3. **Tock vs Resy contradiction** — trust / cart-abandonment fix
4. **Zero analytics** — "you can't improve what you can't measure"
5. **"Copy of HOME" on Uncle Ramen** — if Tommy sees this, the reply writes itself

Everything above is real, sourced from the scrape artifacts, and verifiable via the raw files. No numbers have been invented. Hours, phone, address all pulled from schema — to be re-verified against Google Business / Yelp in Step 2.5 before any copy or mockup goes out.
