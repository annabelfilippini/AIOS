# Adelitas Cocina y Cantina — Scrape Data

**Scraped:** 2026-04-14
**Primary prospect:** https://adelitasco.com/
**Companion prospect:** https://ladonamezcaleria.com/ (sister property, same owner)
**Owner/chef:** Silvia Andaya (executive chef & owner of both properties)

---

## Scope of this scrape

- **Adelitas:** 7 core pages + 2 SEO doorway samples, 3 screenshot passes per core page (desktop full, desktop viewport, mobile)
- **La Doña:** 1 page (single-page site), 3 passes
- **References:** Atomix NYC, Cosme NYC, Pujol — homepage + 1 key page each, full-page desktop + markdown only
- **Full URL inventory:** `scrape/url-inventory.json` + `scrape/url-categorized.json`
- **Raw HTML analysis:** `scrape/raw-html-analysis.json`
- **Firecrawl calls total:** ~46

---

## Top audit findings (preliminary, before SEO + analysis steps)

These surfaced during scrape and are flagged now so `/audit-seo` and `/audit-analyze` can deepen them.

### Adelitas — Critical SEO / technical

1. **`adelitasco.com` (root URL) is a "Location Picker" placeholder page.**
   - Title = `"Location Picker"` — not indexed for any branded or discovery query
   - No meta description, no h1, no JSON-LD, no OpenGraph, no h1-h6 headings at all
   - Contains only 1 image (hero) + 2 location cards (Edgewater / Broadway)
   - **Every backlink to `adelitasco.com` lands on a content-free page.** Domain authority wasted.
   - Fix direction: make root a real homepage; move the location chooser into the header nav.

2. **`/broadway` and `/edgewater` are byte-for-byte duplicate templates.**
   - Identical titles, descriptions, h1, image counts (33), script counts (6), JSON-LD (WebSite + LocalBusiness + Organization)
   - 37,837 vs 37,838 rendered markdown chars — difference is the street address
   - Google duplicate-content risk. Both self-canonical, so both get indexed as competing versions.
   - Fix direction: one canonical location hub with both addresses, OR differentiate Broadway vs Edgewater content (different photos, different menu highlights, different reviews).

3. **17 programmatic-SEO doorway pages** (all in the sitemap):
   - Examples: `/best-mexican-food-in-denver-colorado`, `/mezcal-in-denver`, `/best-margaritas-in-denver`, `/tequila-restaurant-in-denver`, `/best-authentic-tacos-in-denver`
   - Each has 5-6 h1 tags on one page (textbook doorway smell)
   - Each has 15 images with 12 empty alt attributes
   - Each loads the same WebSite/LocalBusiness/Organization JSON-LD verbatim
   - Sample markdown length: 25K chars of keyword-stuffed narrative
   - **Google's doorway-page policy explicitly flags this pattern.** Risk: manual action or site-wide ranking demotion.
   - Fix direction: consolidate into 2-3 real landing pages (menu, location, story), 301 the rest, or noindex them.

4. **JSON-LD identity is misspelled: `"name": "Adeli Tasco"`**
   - Every page carrying structured data reports the business name as `"Adeli Tasco"` (space between "Adeli" and "Tasco")
   - Google uses this name for knowledge panels and rich results
   - **Silent but real:** the restaurant's structured-data identity does not match its brand name.

5. **`/catering` raw HTML contains `<h1>Success!</h1>`** — a form-success state is leaking into the static page. Likely Showit form template bug. Users see this if the page renders before JS hides it.

6. **`/qr-code-menu` (the menu entry point) has 0 images, 0 h1s, 0 JSON-LD.**
   - Title: "Adelitas Cocina Y Cantina | Menus"
   - This is the page linked from the **"Menus"** button on Broadway/Edgewater headers
   - The menu is presumably behind clicks into Showit galleries that aren't rendering as HTML content — opaque to Google, opaque to screen readers.
   - Previously-flagged "broken Reserve Now button" confirmed from another angle: no reservation integration visible in raw HTML on any page.

7. **No reservation system detected** in raw HTML for either site.
   - Third-party script inventory: jQuery, Showit, Google Tag Manager, Mailchimp
   - No Resy, Tock, OpenTable, SevenRooms, or inline booking widget
   - Audit hook from prospect list ("broken Reserve Now button") likely points to a Showit anchor that goes nowhere.

8. **No `robots.txt`** on either domain. Search engines have no crawling hints.

9. **No viewport-mobile-rendered homepage.** Firecrawl's mobile screenshot of `adelitasco.com` is 2KB (essentially blank) — either mobile-detect JS doesn't render the location picker or the page paints white until a late JS frame. Confirm manually with DevTools device mode.

### La Doña — Critical

10. **La Doña's canonical link points to the punycode domain (`xn--ladoamezcaleria-1qb.com`).**
    - Users type `ladonamezcaleria.com`, but the canonical declares `ladoñamezcaleria.com` (with tilde) as the authoritative version
    - All PageRank, backlink signals, and Google crawl priority flow to the tilde-domain
    - **Unintentional SEO leak.** Either fix canonical to the plain-ASCII domain or commit to the tilde brand.

11. **La Doña's JSON-LD `url` is a *different* broken punycode: `xn--laoamezcaleria-1qb.com`** (missing an "n"). Not a valid domain. Schema parser treats the site as unreachable.

12. **No sitemap.xml** for La Doña (404). Single-page Showit site, effectively invisible to systematic crawlers.

13. **One-page Showit architecture** — "menu" and "reservations" links are on-page anchors, not real pages. No menu content as crawlable HTML. No online ordering, no booking flow.

14. **64 images on the La Doña page, 14 with empty alt** — mostly gallery/texture images, but several are product/food shots where alt text would add SEO and accessibility value.

---

## Adelitas — full page inventory

### Core pages (7)
| Page | URL | Title | Notes |
|------|-----|-------|-------|
| homepage | `/` | `Location Picker` | Placeholder. No content. No meta. |
| broadway | `/broadway` | Authentic Mexican Restaurant Denver Colorado \| Adelitas | Location page. 37K chars rendered. Full template. |
| edgewater | `/edgewater` | Authentic Mexican Restaurant Denver Colorado \| Adelitas | **Duplicate of broadway** — identical title, h1, template. |
| catering | `/catering` | Catering | Thin page. "Success!" h1 leaking from form state. |
| qr-code-menu | `/qr-code-menu` | Adelitas Cocina Y Cantina \| Menus | Menu entry — no HTML content, no images, no h1. |
| event | `/event` | Adelitas Cocina Y Cantina \| Event | Sip & Savor tequila dinner promo (Chef Silvia + Adolfo Aguilar). |
| tequilas-about | `/tequilas-family-mexican-restaurant` | Tequila's Family Mexican Restaurant \| Authentic at Adelitas | De-facto About page. 6 h1s. Heavy SEO copy. |

### SEO doorway pages (17, all in sitemap)
All 17 follow the same template: 5-6 h1s, 15 images, duplicated LocalBusiness/Organization/WebSite JSON-LD. Keyword-stuffed narrative copy. Self-canonical.

```
/best-authentic-tacos-in-denver
/best-breakfast-burritos-denver
/best-brunch-in-denver-colorado
/best-food-and-drinks-in-denver
/best-happy-hour-denver
/best-margaritas-in-denver
/best-mexican-breakfast-denver
/best-mexican-food-in-denver-colorado          (scraped as sample)
/best-mexican-restaurant-in-denver
/brunch-restaurants-denver
/denver-breakfast-burrito
/mexican-food-delivery-denver
/mexican-happy-hour-denver
/mexican-tacos-restaurant-denver
/mezcal-in-denver                               (scraped as sample)
/tequila-restaurant-in-denver
/top-cocktail-bars-in-denver
```

**Recommendation for analysis step:** treat these as a single category. One of them scraped is enough to critique the pattern.

---

## La Doña — page inventory

Single page: `/` (also accessible at the punycode tilde-domain `ladoñamezcaleria.com`).

- **Stack:** Showit + jQuery + GTM
- **Website designer credit in footer:** `bohemefox.com` (Boheme Fox) — shared with Adelitas. Same design shop.
- **Content highlights:**
  - Chef-led intro: "a passion project founded by matriarch owner and head chef of Adelitas Cocina Y Cantina, Silvia Andaya"
  - Address: 13 E Louisiana Ave, Denver, CO 80210 (note: the physical space is literally "behind Adelitas")
  - Hours block, contact link, mezcal-forward copy, Instagram wall, 4 customer testimonials
- **Cross-link to Adelitas:** yes, one (`https://www.adelitasco.com/`)

---

## Brand signals (visual + tonal)

From homepage + Broadway + La Doña imagery:

### Adelitas
- **Palette:** warm earth tones, muted reds/oranges, dark ink, cream. Dark evening cantina vibe on Broadway location photos.
- **Typography on site:** Lato (Google Fonts) — light, modern sans-serif. Disconnects from the rustic/festive brand claim.
- **Imagery:** food close-ups, communal tables, two locations with distinct interiors (Broadway = dim/evening cantina, Edgewater = brighter/modern).
- **Voice:** "festive", "authentic", "Michoacán recipes", "La Adelita" as a heritage anchor ("soldadera" / woman warrior). This is a strong narrative asset **not surfaced on the homepage**.

### La Doña
- **Palette:** darker, textural. Black and deep-red tones. Dark background textures in hero (`texture_dark.png`).
- **Typography:** same Lato family (shared designer).
- **Voice:** more intimate and spirits-forward. "Mezcal-centric cocktail bar serving Mexican street food in rustic digs behind Adelitas." Positions itself as a hidden gem. That *is* the brand — the redesign shouldn't sanitize it.

### Shared brand asset: The "La Adelita" story
The `/tequilas-family-mexican-restaurant` page contains a fully-developed Adelitas/La Adelita heritage story (woman-warrior iconography, Michoacán roots, Silvia's chef journey). **It's buried inside an SEO page.** The redesign should lift this narrative to the homepage — it's the single strongest differentiator.

---

## Reference sites (Atomix, Cosme, Pujol)

All three scraped successfully at homepage + 1 deeper page. Saved to `prospects/adelitas/reference/{atomix,cosme,pujol}/`.

### Atomix NYC (atomixnyc.com)
- Korean tasting menu, Junghyun Park. Heavily editorial, typography-driven.
- Screenshots: full-page hero feels like a magazine cover, extreme negative space, serif display type over monochrome photography.
- Markdown is thin — the site is an image/editorial experience, not a content-CMS.
- **Takeaway for Adelitas:** chef-as-protagonist layout. Photography-forward. Confidence through restraint. The Silvia + "La Adelita" story has this tier of narrative potential.

### Cosme NYC (cosmenyc.com)
- Enrique Olvera's NYC flagship. Mexican fine-dining positioning.
- More text-rich than Atomix. Menu page renders as a simple branded list.
- Color: deep tonal neutrals, confident typography (serif display + sans body).
- **Takeaway for Adelitas:** permission to be premium without losing Mexicanidad. Cosme proves an editorial Mexican restaurant site doesn't need decorative sombreros/agave clichés to signal identity.

### Pujol (pujol.com.mx/en)
- Enrique Olvera's Mexico City flagship. The global benchmark for modern Mexican dining.
- Extremely minimal homepage — a single hero, nav, reservation CTA.
- JS-heavy: Firecrawl markdown returned ~1K chars but screenshot captured the full layout.
- **Takeaway for Adelitas:** aspirational — not a template to copy, but a reference for what "museum-grade Mexican restaurant brand" looks like.

**Note for Step 5 (redesign):** The rule from Pepper Pong applies — elevate, don't erase. Adelitas is a neighborhood cantina, not a tasting-menu destination. The references inform *execution quality* (typography, photography hierarchy, restraint). The *identity* stays Adelitas's own — warmth, family, Michoacán, La Adelita heritage.

---

## Screenshots inventory

```
prospects/adelitas/scrape/screenshots/
  homepage-{desktop-full,desktop-viewport,mobile}.png      (mobile = 2KB, likely blank)
  broadway-{desktop-full,desktop-viewport,mobile}.png
  edgewater-{desktop-full,desktop-viewport,mobile}.png
  catering-{desktop-full,desktop-viewport,mobile}.png
  qr-code-menu-{desktop-full,desktop-viewport,mobile}.png
  event-{desktop-full,desktop-viewport,mobile}.png
  tequilas-family-mexican-restaurant-{desktop-full,desktop-viewport,mobile}.png

prospects/adelitas/companion/la-dona/scrape/screenshots/
  homepage-{desktop-full,desktop-viewport,mobile}.png

prospects/adelitas/reference/atomix/
  homepage-desktop-full.png
  about-desktop-full.png

prospects/adelitas/reference/cosme/
  homepage-desktop-full.png
  menu-desktop-full.png

prospects/adelitas/reference/pujol/
  homepage-desktop-full.png
  experience-desktop-full.png
```

**Visual-QA flag:** the Adelitas homepage mobile screenshot is 2KB — confirm whether the root URL actually renders for mobile users. If it does not, that's a major usability bug independent of SEO.

---

## Data artifacts

- `scrape/homepage.md`, `broadway.md`, `edgewater.md`, `catering.md`, `qr-code-menu.md`, `event.md`, `tequilas-family-mexican-restaurant.md`
- `scrape/seo-sample-best-mexican-food.md`, `scrape/seo-sample-mezcal-in-denver.md`
- `scrape/*-metadata.json` (per core page)
- `scrape/raw-html-analysis.json` — structured meta + headings + image alt counts + script fingerprints + JSON-LD samples for all 9 pages
- `scrape/url-inventory.json` + `scrape/url-categorized.json`
- `companion/la-dona/scrape/homepage.md` + metadata + screenshots
- `reference/{atomix,cosme,pujol}/*.md` + `*-desktop-full.png`

---

## Handoff to `/audit-seo` (Step 3)

Priority keyword clusters to research, grouped by the finding that motivated them:

1. **Michoacán cuisine in Denver** — uniqueness claim; should own this.
2. **Mezcal bar Denver** (La Doña differentiator) — check vs Mezcalli, Adelitas Meze, Los Chingones Mezcal.
3. **Chef Silvia Andaya** — personal brand SEO. How visible is she?
4. **Family-owned Mexican restaurant Denver**, **Michoacán food Denver** — narrative-matched terms.
5. **Sip & Savor tequila dinner** — event-page visibility.
6. **Do NOT chase** the existing 17 doorway-page keyword set — the audit position will be to prune, not expand, those.
7. **Generic queries:** "Mexican restaurant Denver", "best Mexican food Denver" — where does Adelitas currently rank vs competitors?
8. **Brand searches:** "Adelitas Denver", "La Doña Denver", "Adelitas Broadway", "Adelitas Edgewater" — branded queries are a leading indicator of local-SEO health.
9. **Reservation intent:** "Mexican restaurant Denver reservations" — Adelitas currently has no booking system; any reservation-intent searcher bounces.
