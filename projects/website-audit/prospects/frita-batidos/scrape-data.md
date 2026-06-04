# Frita Batidos — Scrape Data
**Date:** 2026-04-17
**URL:** https://fritabatidos.com/ann-arbor
**Status:** SITE DOWN (503 Service Unavailable on all pages)
**Fallback sources:** Wayback Machine (cached Mar 27 2026), Yelp (2,521 reviews), Firecrawl map metadata

## Critical Finding: Site Is Down

fritabatidos.com returns 503 "Service Unavailable" on every page — homepage, all location subpages, food, chef, contact. Both Firecrawl (headless browser) and raw HTTP (urllib) get the same error. This is not bot-blocking — the server itself is down.

**Audit implication:** This is the single most urgent finding. A restaurant with 2,521 Yelp reviews and "Best Burger" awards 11 years running has zero web presence right now. Anyone searching for them gets nothing. AI systems (ChatGPT, Perplexity, Gemini) that try to crawl their site for recommendations will get 503 and skip them entirely.

## Site Architecture (from Firecrawl map — before 503)

WordPress-based site with three location hubs:
- `/ann-arbor/` — primary (food, chef, philosophy, praise, contact, catering, photos, menu-guide, gear)
- `/detroit/` — secondary (same structure + happy-hour, breakfast)
- `/air/` — newest concept at HOMES Campus (food, chef, photos, contact)

38 total URLs mapped. Each location has its own WordPress subdirectory structure.

## Pages Attempted (10 pages, 30 Firecrawl calls — all returned 503)

| Page | URL | Result |
|---|---|---|
| Homepage (main) | fritabatidos.com/ | 503 — 79 chars |
| Ann Arbor Home | fritabatidos.com/ann-arbor | 503 — 79 chars |
| Ann Arbor Food | fritabatidos.com/ann-arbor/food | 503 — 79 chars |
| Ann Arbor Chef | fritabatidos.com/ann-arbor/chef | 503 — 79 chars |
| Ann Arbor Philosophy | fritabatidos.com/ann-arbor/philosophy | 503 — 79 chars |
| Ann Arbor Praise | fritabatidos.com/ann-arbor/praise | 503 — 79 chars |
| Ann Arbor Contact | fritabatidos.com/ann-arbor/contact | 503 — 79 chars |
| Ann Arbor Catering | fritabatidos.com/ann-arbor/catering | 503 — 79 chars |
| Detroit Home | fritabatidos.com/detroit | 503 — 79 chars |
| Detroit Food | fritabatidos.com/detroit/food | 503 — 79 chars |

## Wayback Machine Recovery

### Homepage (cached Mar 27, 2026)
- **Hero image:** B&W photo of Eve Aronoff in "FRITA" t-shirt with food tray, vintage Coca-Cola cooler
- **Logo:** "FRITA BATIDOS" wordmark with blue flower/pinwheel icon, "Cuban Inspired Street Food!" tagline in cursive
- **Awards banner (yellow):** "Best Burger Michigan Daily Consecutively 2014-2025 | Metro Times Best Cuban Restaurant 2020-2024 | Best Specialty Burger Hour Magazine 2025 | Best New Burger NYC Frita Brooklyn The Lo Times"
- **Top bar links:** Gift cards (Toast), Takeaway (Toast), Catering (Toast)
- **Metadata keywords:** downtown ann arbor, cuban restaurant, fritas, batidos, eve aronoff, top chef, james beard, burgers, best burger ann arbor, slow food movement, mojitos, sangria

### Food & Drinks Page (cached Mar 27, 2026)
- Online ordering link: toasttab.com/fritabatidos
- Sourcing statement: "We strive to source our meat, cheese and produce from Michigan or the Midwest whenever possible."
- Halal certification: "All of our chicken and beef is certified Halal!"
- Menu images (PNGs hosted in WordPress theme): food menu, bar menu, menu guide
- Menu image URLs: `/wp-content/uploads/2026/02/AA-FOOD-1.png`, `AA-BAR-UPDATED.png`, `AA-MENU-GUIDE.png`

### Chef & Praise Pages
- Not recoverable from Wayback (redirected to bot-protection on archive.org)
- Chef info sourced from Yelp: Eve Aronoff, established 2010, "wanted to express her love for Cuban food in a casual, fun setting"

## Raw HTML Analysis

All 8 target URLs returned HTTP 503. No meta tags, JSON-LD, headings, or alt text could be analyzed. Results in `scrape/raw-html-analysis.json` (all entries have `"error": "HTTP Error 503: Service Unavailable"`).

**AI-SEO implication:** With the site down, there is literally zero structured data, zero JSON-LD, zero schema markup being served. Any AI system crawling right now gets nothing.

## Yelp Data (primary fact source)

- **Rating:** 4.4 stars / 2,521 reviews
- **Address:** 117 W Washington St, Ann Arbor, MI 48104
- **Phone:** (734) 761-2882
- **Hours:** Mon-Thu 11am-11pm, Fri-Sat 11am-12am, Sun 11am-11pm
- **Categories:** Cuban, Burgers, Cocktail Bars
- **Price:** $$
- **Photos:** 1,991 (148 inside, 54 outside)
- **Top items by reviews:** Chorizo Frita (229), Beef Frita (218), Avocado Spread (122)
- **Yelp accolade:** #31 on Yelp's 2023 Top 100 Burger Spots

See `facts/verified-facts.md` for complete review quotes, menu items, and sourced details.

## Reference Sites Scraped

### Au Cheval (auchevaldiner.com)
- Scraped successfully: 893 chars markdown, 9KB screenshot
- Minimal website — likely a single-page or very concise design
- Saved to `reference/au-cheval/`

### Mighty Fine (mightyfineburgers.com)
- Scraped successfully: 10,930 chars markdown, 3MB screenshot
- Full content captured
- Saved to `reference/mighty-fine/`

## Screenshots Captured

### Frita Batidos (all 503 error pages)
- 30 screenshots total (10 pages × 3 passes: desktop-full, desktop-viewport, mobile)
- All show the generic "503 Service Unavailable" page
- 1 Wayback Machine screenshot of actual homepage saved as `ann-arbor-home-wayback.png` (588KB)

### Yelp Photos Downloaded (for mockup use)
- `mockups/assets/frita-hero-yelp.jpg` — Beef frita with fried egg + batido (71KB, portrait)
- `mockups/assets/frita-drinks-yelp.jpg` — Bar interior with blue menu boards (160KB, landscape)
- `mockups/assets/frita-bowl-yelp.jpg` — Pulled pork bowl with tropical slaw (76KB, landscape)
- `mockups/assets/frita-batido-yelp.jpg` — Cajeta batido (73KB)
- `mockups/assets/frita-snack-yelp.jpg` — "Best Snack Ever" (72KB)
- `mockups/assets/frita-coconut-batido-yelp.jpg` — Coconut cream batido (47KB)

## Branding Summary

- **Colors:** Blue (menu boards) + white (brick walls) — confirmed from interior photos
- **Logo:** Flower/pinwheel icon in light blue, "FRITA BATIDOS" wordmark
- **Aesthetic:** Current site is retro/nostalgic (B&W photography, vintage elements). Annabel wants futuristic direction.
- **Full branding tokens:** `branding.json`

## Key Audit Angles (for /audit-analyze)

1. **SITE IS DOWN** — #1 finding. 503 on all pages. Complete web presence failure.
2. **Zero AI discoverability** — no structured data being served, no JSON-LD, no schema markup (even when site was up, metadata keywords suggest no schema implementation)
3. **Awards not in structured data** — "Best Burger 2014-2025" banner has no schema markup, so Google/AI can't surface it
4. **Multi-location confusion** — three concepts (Ann Arbor, Detroit, Frita Air) under one domain with separate WordPress installs, no clear location picker
5. **Toast dependency** — ordering, gift cards, catering all route through Toast external links
6. **Menu as images** — food/drink menus are PNG images, not crawlable text
7. **Strong Yelp presence** — 4.4 stars, 2,521 reviews, but site itself doesn't leverage this social proof
