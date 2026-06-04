# Frita Batidos -- Internal Audit
**Date:** 2026-04-17
**Site:** fritabatidos.com (503 -- SITE DOWN)
**Location:** 117 W Washington St, Ann Arbor, MI 48104
**Owner:** Eve Aronoff | Est. 2010
**Yelp:** 4.4 stars, 2,521 reviews | **AI Discoverability:** 18/100

---

## Summary

Frita Batidos is one of Ann Arbor's most awarded restaurants -- 11 consecutive "Best Burger" wins, #31 on Yelp's national Top 100, certified halal meat, a Top Chef alum founder -- and it is currently invisible to every AI system on the internet. The website returns 503 on all 38 mapped URLs, meaning zero structured data, zero crawlable content, and zero conversion from organic search. A third-party squatter domain (fritabatidosannarbor.shop) is ranking on the brand name while the real site is dead. The halal certification -- a massive differentiator in a university town with one of the Midwest's largest Muslim student populations -- exists nowhere in structured data and is completely absent from halal search results.

---

## Technical Health

| Finding | Severity | Effort | Details |
|---|---|---|---|
| 503 on all pages | CRITICAL | Trivial (hosting fix) | Every URL returns "503 Service Unavailable." Not bot-blocking -- the server itself is down. 79 chars of generic error HTML per page. |
| WordPress platform | Medium | N/A (informational) | Site runs WordPress with per-location subdirectory structure (/ann-arbor/, /detroit/, /air/). 38 total URLs mapped via Firecrawl before outage. |
| Toast external dependency | Medium | Moderate | Online ordering, gift cards, and catering all redirect to toasttab.com. Transactional content lives on a domain Frita doesn't control. |
| No robots.txt | High | Trivial | Even before the 503, no robots.txt was configured for AI crawlers. |
| No sitemap.xml | High | Trivial | No sitemap to help crawlers discover the 38 pages efficiently. |
| No llms.txt | High | Trivial | No LLM guidance file. Emerging standard adopted by Anthropic, Cloudflare, and others. |
| Squatter domain active | High | Moderate | fritabatidosannarbor.shop ranks for brand queries while the real site is dead. Potential trademark issue. |

---

## SEO

### Keyword Visibility

| # | Keyword | Intent | Frita Appears? | Position | Gap | Priority |
|---|---------|--------|----------------|----------|-----|----------|
| 1 | frita batidos ann arbor | Navigational | Yes (Yelp, IG, Toast, TripAdvisor, FB) | #1 is fritabatidos.com (503) | CRITICAL -- site is down, users hit error | P0 |
| 2 | best burger ann arbor | Transactional | Yes -- Michigan Daily article, Yelp lists | ~#9 (article mention only) | SHOULD OWN -- 11x consecutive Best Burger winner | P1 |
| 3 | cuban food ann arbor | Transactional | Yes -- Yelp list #1, direct site #2, FB #3 | #1-5 (via aggregators) | DOMINATE -- they ARE Cuban food in A2 | P1 |
| 4 | best restaurant ann arbor | Informational | Mentioned in list articles | Deep (mentioned, not featured) | HIGH VALUE -- should appear in top 5 lists | P2 |
| 5 | ann arbor lunch | Transactional | Mentioned in blog post | ~#1 in Epicurean Traveler blog | OPPORTUNITY -- high volume, low presence | P2 |
| 6 | cuban burger near me | Transactional | Yes -- dominates results | #1-8 (all results are Frita) | OWNED -- but site 503 kills conversion | P0 |
| 7 | halal restaurant ann arbor | Transactional | No | Not present | MISSED -- certified halal, invisible to halal queries | P3 |
| 8 | best batidos michigan | Informational | Yes -- all top 10 results | #1-10 (total domination) | OWNED -- brand monopoly on term | P0 |
| 9 | eve aronoff chef | Navigational | Yes -- chef page, press, wiki | #2 (fritabatidos.com/chef -- 503) | OWNED -- but site 503 kills it | P1 |
| 10 | ann arbor happy hour | Transactional | Mentioned in Yelp list | Deep mention only | OPPORTUNITY -- they have cocktails + bar | P2 |

### Gap Analysis

**Keywords they own but can't convert (site 503):** "frita batidos ann arbor," "cuban burger near me," "best batidos michigan," "eve aronoff chef." Traffic bleeds to Yelp, Toast, and aggregators.

**Keywords they should own but don't:** "best burger ann arbor" (despite winning 11 years, they rank ~#9 via a Michigan Daily article -- Blimpy Burger, Taystee's, Casey's Tavern all outrank with direct websites). "halal restaurant ann arbor" (certified halal, zero presence).

**Keywords with opportunity:** "ann arbor happy hour" (have a cocktail program, no dedicated page), "ann arbor lunch" (open at 11am daily, no targeted content), "best restaurant ann arbor" (TripAdvisor #1 of 423 but no direct ranking).

**Competitive landscape:** Sava's strongest organic competitor for "best restaurant." Taystee's Burgers captures both "best burger" AND "halal" -- the dual-keyword strategy Frita should study. Zingerman's dominates local food SEO with content marketing. Blimpy Burger and Casey's Tavern outrank Frita on "best burger" despite having no comparable awards.

---

## AI Discoverability

### Overall Score: 18 / 100

| Category | Score | Max | Status |
|---|---|---|---|
| Crawler Access | 0 | 25 | CRITICAL FAILURE |
| Schema Coverage | 2 | 25 | CRITICAL FAILURE |
| Content Structure | 4 | 25 | SEVERE |
| AI Visibility | 12 | 25 | POOR |

### Subscores Detail

**Crawler Access (0/25):** Every URL returns 503. No robots.txt, no llms.txt, no sitemap.xml. AI crawlers get nothing. Score rationale: zero -- not degraded, not partial, zero.

**Schema Coverage (2/25):** Even when site was live, Wayback cache reveals zero JSON-LD, zero LocalBusiness/Restaurant/Menu/FAQPage/Review/Award schema. Only WordPress meta keywords (ignored by Google since 2009). The 2 points are for meta keywords containing relevant terms. Missing schema types: Restaurant, Menu + MenuSection + MenuItem, AggregateRating, Award, FAQPage, LocalBusiness (per location), Person (Eve Aronoff).

**Content Structure (4/25):** Menu as PNG images (uncrawlable), multi-location confusion (three concepts, no location picker, no hreflang), Toast dependency for transactional content, no semantic heading hierarchy, photos without alt text. The 4 points are for logical URL structure (/ann-arbor/food, /ann-arbor/chef).

**AI Visibility (12/25):** Appears in most queries via Yelp/Michigan Daily, but never from own website. Completely absent from "halal restaurant ann arbor." 5 of 10 branded search results are dead 503 links. Squatter domain filling the void.

### Verbatim AI Search Results

**"best burger in ann arbor":** Appears via TripAdvisor, Yelp lists, Michigan Daily headline "Frita Batidos wins 2025 Best Ann Arbor Burger." Own website link is dead. Competitors Krazy Jim's Blimpy Burger, Taystee's, Casey's Tavern, HopCat, Shake Shack all mentioned.

**"cuban restaurant ann arbor":** Dominates -- Yelp #1 for Cuban in A2. But fritabatidos.com returns 503. fritabatidosannarbor.shop (third-party) IS working and ranking. La Cocina Cubana, Vicente's Cuban Cuisine, Sweet Havana mentioned as alternatives.

**"frita batidos ann arbor" (brand search):** 5 of 10 results are dead fritabatidos.com links (503). Working results: Yelp, Toast ordering, TripAdvisor, Facebook, annarbor.org.

**"best restaurant ann arbor michigan":** Mentioned in aggregated lists (TripAdvisor, annarbor.org, Cozymeal). Competitors Echelon, Miss Kim, Zingerman's, Gandy Dancer get richer AI descriptions. Frita gets one-line mentions. Eleven consecutive awards invisible because they exist only as a banner image.

**"halal restaurant ann arbor":** ABSENT. Does not appear anywhere. Taystee's Burgers, Palm Palace, Aladdin's, La Marsa, Haifa Falafel dominate. Despite certified halal chicken and beef.

**"where to eat near university of michigan":** Mentioned in UMich Admissions blog ("houses the best burger in Ann Arbor according to the Michigan Daily"). Gets a single line. Zingerman's gets a full paragraph. Competitors with structured data get multi-sentence descriptions.

### Recommended JSON-LD: Restaurant Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Frita Batidos",
  "description": "Cuban-inspired street food restaurant in downtown Ann Arbor. Home of the frita -- a Cuban-style burger topped with shoestring fries, served with tropical batido milkshakes and craft cocktails.",
  "url": "https://fritabatidos.com/ann-arbor/",
  "telephone": "+1-734-761-2882",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "117 W Washington St",
    "addressLocality": "Ann Arbor",
    "addressRegion": "MI",
    "postalCode": "48104",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 42.2808,
    "longitude": -83.7497
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"],
      "opens": "11:00",
      "closes": "23:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Friday", "Saturday"],
      "opens": "11:00",
      "closes": "00:00"
    }
  ],
  "servesCuisine": ["Cuban", "Burgers", "Cocktails"],
  "priceRange": "$$",
  "acceptsReservations": false,
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.4",
    "reviewCount": "2521",
    "bestRating": "5"
  },
  "award": [
    "Best Burger, Michigan Daily -- 2014-2025 (11 consecutive years)",
    "Best Cuban Restaurant, Metro Times -- 2020-2024",
    "Best Specialty Burger, Hour Magazine -- 2025",
    "#31 on Yelp's Top 100 Burger Spots -- 2023"
  ],
  "sameAs": [
    "https://www.yelp.com/biz/frita-batidos-ann-arbor",
    "https://www.instagram.com/fritabatidos/",
    "https://www.facebook.com/FritaBatidos/",
    "https://www.tripadvisor.com/Restaurant_Review-g29556-d1989898-Reviews-Frita_Batidos-Ann_Arbor_Michigan.html"
  ],
  "founder": {
    "@type": "Person",
    "name": "Eve Aronoff",
    "description": "Top Chef Season 6 contestant and Slow Food advocate who created Frita Batidos in 2010."
  },
  "hasMenu": {
    "@type": "Menu",
    "url": "https://fritabatidos.com/ann-arbor/food/",
    "hasMenuSection": [
      {
        "@type": "MenuSection",
        "name": "Fritas",
        "hasMenuItem": [
          { "@type": "MenuItem", "name": "Chorizo Frita", "suitableForDiet": "https://schema.org/HalalDiet" },
          { "@type": "MenuItem", "name": "Beef Frita", "suitableForDiet": "https://schema.org/HalalDiet" },
          { "@type": "MenuItem", "name": "Black Bean Frita", "suitableForDiet": "https://schema.org/VegetarianDiet" },
          { "@type": "MenuItem", "name": "Chicken Frita", "suitableForDiet": "https://schema.org/HalalDiet" },
          { "@type": "MenuItem", "name": "Fish Frita" }
        ]
      },
      {
        "@type": "MenuSection",
        "name": "Batidos",
        "hasMenuItem": [
          { "@type": "MenuItem", "name": "Coconut Cream Batido" },
          { "@type": "MenuItem", "name": "Chocolate Espanol Batido" },
          { "@type": "MenuItem", "name": "Cajeta Batido" }
        ]
      }
    ]
  }
}
```

### Recommended JSON-LD: FAQPage Schema

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Frita Batidos halal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. All chicken and beef at Frita Batidos is certified Halal."
      }
    },
    {
      "@type": "Question",
      "name": "What is a frita?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A frita is a Cuban-style burger, typically made from spicy chorizo, topped with crispy shoestring fries and served on a soft egg bun."
      }
    },
    {
      "@type": "Question",
      "name": "Does Frita Batidos take reservations?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Frita Batidos is counter service and walk-in only."
      }
    },
    {
      "@type": "Question",
      "name": "Does Frita Batidos offer vegetarian options?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The Black Bean Frita is vegetarian, along with sides like Plantain Chips, Mexico City Corn, and Crisped Plantains."
      }
    },
    {
      "@type": "Question",
      "name": "Does Frita Batidos cater events?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Frita Batidos offers full catering for events. Visit fritabatidos.com/ann-arbor/catering or call (734) 761-2882."
      }
    }
  ]
}
```

### Recommended llms.txt

```
# Frita Batidos

> Cuban-inspired street food in downtown Ann Arbor since 2010. Chef Eve Aronoff's fritas (Cuban-style burgers topped with shoestring fries) and tropical batido milkshakes have won Best Burger from the Michigan Daily for 11 consecutive years (2014-2025).

## Locations

- Ann Arbor: 117 W Washington St, Ann Arbor, MI 48104 | (734) 761-2882
- Detroit: 66 W Columbia, Detroit, MI 48201
- Frita Air: HOMES Campus, Ann Arbor

## Key Facts

- All chicken and beef is certified Halal
- Counter service, walk-in only (no reservations)
- Online ordering: order.toasttab.com/online/fritabatidos
- Catering available

## Awards

- Best Burger, Michigan Daily: 2014-2025 (11 consecutive years)
- Best Cuban Restaurant, Metro Times: 2020-2024
- Best Specialty Burger, Hour Magazine: 2025
- #31 on Yelp's Top 100 Burger Spots: 2023
```

---

## Content & UX

| Finding | Severity | Effort | Details |
|---|---|---|---|
| Menu as PNG images | High | Moderate | Food menu, bar menu, and menu guide are all PNG files (AA-FOOD-1.png, AA-BAR-UPDATED.png, AA-MENU-GUIDE.png). AI crawlers cannot read them. Most common AI question about restaurants ("what's on the menu?") is unanswerable from the website. |
| Multi-location confusion | Medium | Moderate | Three concepts (Ann Arbor, Detroit, Frita Air) share one domain with separate WordPress subdirectories. No clear location picker, no hreflang tags, no canonical structure. AI systems may conflate the three or ignore two. |
| No heading hierarchy | Medium | Easy | Site relies on WordPress theme templates without semantic HTML headings. No H1/H2/H3 hierarchy for crawlers to parse content structure. |
| Awards as banner image | High | Easy | "Best Burger 2014-2025" displayed in a yellow banner -- not in structured data. AI cannot parse this. When asked "most-awarded burger place in Ann Arbor?" AI has no way to find this from the website. |
| Photos without alt text | Medium | Easy | 1,991 Yelp photos exist, but website imagery shows no descriptive alt attributes. |
| Halal cert buried in body text | High | Easy | "All of our chicken and beef is certified Halal!" exists as plain text on the food page, not in schema, not in page title, not in any structured format AI can surface. |
| No dedicated awards/press page | Medium | Moderate | Extensive press (Top Chef, Michigan Daily, Metro Times, Hour Magazine) with no consolidated page for search engines to index. |
| No happy hour page | Medium | Easy | Cocktail program exists but no dedicated /happy-hour page to compete for "ann arbor happy hour" queries. |

---

## AI Opportunities

| Opportunity | Impact | Effort | Details |
|---|---|---|---|
| Restaurant JSON-LD schema | Critical | Easy | Single code block makes the restaurant machine-readable: name, hours, address, menu, awards, ratings. Unlocks rich results in Google and AI citations. |
| FAQPage schema (halal + dietary) | Critical | Easy | Opens Frita to the entire halal search market in Ann Arbor. One JSON block answers "Is Frita Batidos halal?" for every AI system. |
| Convert PNG menus to HTML text | High | Moderate | Every menu item, price, and description locked in images. HTML menu with MenuItem schema lets AI answer "what's on the menu?" and "does Frita have X?" |
| Add llms.txt | High | Trivial | 10-minute task. Puts Frita ahead of 99% of restaurants nationally for AI discoverability. |
| "Best Burger" landing page | High | Moderate | Dedicated page for 11-year winning streak with award schema. Target "best burger ann arbor" directly instead of relying on Michigan Daily articles. |
| Halal landing page / section | High | Easy | Dedicated content targeting "halal restaurant ann arbor" and "halal burger ann arbor." Taystee's currently wins this by default. |
| Happy hour page | Medium | Easy | Dedicated /happy-hour with specials, hours, drink photography. Competes for "ann arbor happy hour" -- currently missing entirely. |
| Catering page optimization | Medium | Moderate | Catering page exists but routes to Toast. Dedicated on-site content with Event/FoodService schema captures corporate/event market. |
| Per-location LocalBusiness schema | Medium | Easy | Separate LocalBusiness JSON-LD for each of three locations prevents AI from conflating Ann Arbor, Detroit, and Frita Air. |
| Person schema for Eve Aronoff | Low | Trivial | Top Chef connection is searchable. Person schema with founder details strengthens brand entity in AI knowledge graphs. |

---

## Priority Action List

### This Week

1. **Restore the website.** 503 is an emergency. Every hour down, Google deindexes more pages and AI systems skip the domain. (CRITICAL / Trivial)
2. **Add Restaurant JSON-LD to homepage.** Copy the schema block above into the WordPress header. Immediate machine-readability. (CRITICAL / Easy)
3. **Add FAQPage JSON-LD.** Halal certification, what is a frita, reservations, vegetarian options, catering. Unlocks halal market. (CRITICAL / Easy)
4. **Add robots.txt and sitemap.xml.** Basic crawler infrastructure. (HIGH / Trivial)
5. **Monitor fritabatidosannarbor.shop.** Assess whether trademark action is needed. (HIGH / Trivial)

### This Month

6. **Convert PNG menus to HTML text with Menu schema.** Keep visual menu as supplement; primary menu must be crawlable. (HIGH / Moderate)
7. **Add llms.txt at domain root.** 10-minute task, outsized AI discoverability return. (HIGH / Trivial)
8. **Create dedicated /best-burger page.** 11 consecutive wins, award schema, target "best burger ann arbor" keyword directly. (HIGH / Moderate)
9. **Create dedicated /halal page.** Target halal queries with structured content and dietary schema. (HIGH / Easy)
10. **Add alt text to all images.** 1,991 Yelp photos demonstrate visual appeal; website images should be equally descriptive. (MEDIUM / Easy)

### This Quarter

11. **Create /happy-hour page with cocktail content.** Target "ann arbor happy hour" keyword. (MEDIUM / Easy)
12. **Optimize catering page.** Move content on-site from Toast, add FoodService/Event schema. (MEDIUM / Moderate)
13. **Implement per-location LocalBusiness schema.** Prevent AI conflation of three concepts. (MEDIUM / Easy)
14. **Build consolidated press/awards page.** Index Top Chef, Michigan Daily, Metro Times, Hour Magazine coverage. (MEDIUM / Moderate)
15. **Content marketing: lunch, date night, UMich guides.** Target "ann arbor lunch," "ann arbor date night," "where to eat near UMich" with owned blog content. (MEDIUM / Hard)
16. **Pitch list-article authors.** TimeOut, Infatuation, Food Network -- update "best of" lists with current Frita info. (LOW / Moderate)
17. **Add Person schema for Eve Aronoff.** Strengthen brand entity in AI knowledge graphs. (LOW / Trivial)

---

*Estimated score improvement: 18/100 to ~72/100 with This Week + This Month items implemented.*
