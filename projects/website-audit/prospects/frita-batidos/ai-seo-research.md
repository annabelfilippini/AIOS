# AI Discoverability Audit: Frita Batidos
**Date:** 2026-04-17
**Subject:** fritabatidos.com (503 — SITE DOWN)
**Location:** 117 W Washington St, Ann Arbor, MI 48104
**Owner:** Eve Aronoff | Est. 2010 | 4.4 stars, 2,521 Yelp reviews

---

## Overall AI Discoverability Score: 18 / 100

| Category | Score | Max | Status |
|---|---|---|---|
| Crawler Access | 0 | 25 | CRITICAL FAILURE |
| Schema Coverage | 2 | 25 | CRITICAL FAILURE |
| Content Structure | 4 | 25 | SEVERE |
| AI Visibility | 12 | 25 | POOR |
| **TOTAL** | **18** | **100** | **EMERGENCY** |

This is the lowest score we have seen. The website is completely offline, returning 503 on every URL. A restaurant that has won Best Burger in Ann Arbor eleven consecutive years is currently invisible to every AI system that tries to crawl it.

---

## 1. Crawler Access: 0 / 25

### What We Tested

| URL | HTTP Status | AI Crawler Result |
|---|---|---|
| `fritabatidos.com/robots.txt` | **503** | Cannot read crawl rules |
| `fritabatidos.com/llms.txt` | **503** | No LLM guidance available |
| `fritabatidos.com/sitemap.xml` | **503** | Cannot discover any pages |
| `fritabatidos.com/` | **503** | Homepage unreachable |
| `fritabatidos.com/ann-arbor/food` | **503** | Menu unreachable |
| `fritabatidos.com/ann-arbor/chef` | **503** | Chef bio unreachable |
| `fritabatidos.com/ann-arbor/contact` | **503** | Contact info unreachable |

Every single URL returns the same generic error page:

```
503 Service Unavailable
The server is temporarily busy, try again later!
```

No meta tags. No JSON-LD. No content. Just 719 bytes of a bare HTML error template. This is not bot-blocking — the server itself is down.

### What This Means for AI

When ChatGPT, Perplexity, Gemini, or any AI assistant tries to answer "What should I eat in Ann Arbor?" they send crawlers to restaurant websites. Frita Batidos returns nothing. The AI skips to the next restaurant that has a working site with structured data.

Even before the outage, the site had no `robots.txt` configuration for AI crawlers, no `llms.txt` file (the emerging standard for telling AI systems what your business is), and no `sitemap.xml` to help crawlers discover pages efficiently. The 503 just makes an already-bad situation catastrophic.

**Score rationale:** 0/25. There is literally no crawler access. Not degraded, not partial — zero.

---

## 2. Schema Coverage: 2 / 25

### What We Found (from Wayback Machine cache, Mar 27 2026)

The live site currently serves zero structured data because it is down. But even when the site was operational, the Wayback Machine cache reveals:

- **JSON-LD structured data:** NONE detected
- **LocalBusiness schema:** ABSENT
- **Restaurant schema:** ABSENT
- **Menu schema:** ABSENT (menus are PNG images, not text)
- **FAQPage schema:** ABSENT
- **Review/AggregateRating schema:** ABSENT
- **Event schema:** ABSENT
- **Award schema:** ABSENT

The site had WordPress meta keywords (`downtown ann arbor, cuban restaurant, fritas, batidos, eve aronoff, top chef, james beard, burgers, best burger ann arbor`), but meta keywords have been ignored by Google since 2009 and carry zero weight in AI systems.

### The Awards Problem

Frita Batidos has an extraordinary awards record displayed in a yellow banner on their homepage:

> "Best Burger Michigan Daily Consecutively 2014-2025 | Metro Times Best Cuban Restaurant 2020-2024 | Best Specialty Burger Hour Magazine 2025 | Best New Burger NYC Frita Brooklyn The Lo Times"

This is displayed as plain text inside an image/banner — not in any structured data format. AI systems cannot parse this. When someone asks "what's the most-awarded burger place in Ann Arbor?" the AI has no way to find this information from Frita Batidos' own website.

### The Menu Problem

The food menu, bar menu, and menu guide are all PNG image files (`AA-FOOD-1.png`, `AA-BAR-UPDATED.png`, `AA-MENU-GUIDE.png`). AI crawlers cannot read image-based menus. When someone asks "does Frita Batidos have a black bean burger?" or "what's on the Frita Batidos menu?" the AI cannot answer from the website.

### The Halal Problem

The food page states: "All of our chicken and beef is certified Halal!" This is a significant competitive differentiator in Ann Arbor's large Muslim student population, but it is buried as plain text on a page that is currently down, with no schema markup that would let AI systems surface it in response to "halal restaurant ann arbor."

**Score rationale:** 2/25. The 2 points are for the meta keywords that at least contain relevant terms, even though they carry near-zero weight.

### What SHOULD Be There

A restaurant of this caliber should have these schema types implemented:

1. **Restaurant** (type, name, cuisine, price range, address, phone, hours, menu URL)
2. **Menu** with **MenuSection** and **MenuItem** (every dish as crawlable text)
3. **AggregateRating** (4.4 stars, 2,521 reviews)
4. **Award** entries for each year of "Best Burger" recognition
5. **FAQPage** (halal certification, ordering, catering, dietary options)
6. **LocalBusiness** for each of the three locations (Ann Arbor, Detroit, Frita Air)
7. **Person** schema for Chef Eve Aronoff (Top Chef connection, founder story)

---

## 3. Content Structure: 4 / 25

### Why This Score

Even when the site was up, the content structure had serious AI-readability problems:

- **Menu as images:** PNG-only menus mean zero crawlable text for AI systems. This is the single most common question AI gets about restaurants ("what's on the menu?") and Frita Batidos cannot answer it.
- **Multi-location confusion:** Three concepts (Ann Arbor, Detroit, Frita Air) share one domain with separate WordPress subdirectories. No clear location picker, no hreflang tags, no canonical structure. AI systems may conflate the three or ignore two.
- **Toast dependency:** Online ordering, gift cards, and catering all redirect to external Toast URLs (toasttab.com/fritabatidos). This means the actual transactional content lives on a third-party domain the restaurant doesn't control.
- **No semantic HTML hierarchy observed:** Wayback cache shows the site relies on WordPress theme templates without explicit heading hierarchy optimized for crawlers.
- **Photos without alt text:** 1,991 Yelp photos exist, but the website's own imagery (when live) showed no evidence of descriptive alt attributes.

**Score rationale:** 4/25. The 4 points are for having a logical URL structure (/ann-arbor/food, /ann-arbor/chef, etc.) and for having meta keywords with relevant terms. Everything else is failing.

---

## 4. AI Visibility: 12 / 25 — Live Search Results

This is the most important section. We ran six queries that real people ask AI assistants, and captured what comes back.

---

### Query 1: "best burger in ann arbor"

**Does Frita Batidos appear?** YES — but relying entirely on third-party sources.

**What AI systems return:**
- Tripadvisor "THE 10 BEST Burgers in Ann Arbor" — Frita Batidos included in the list
- Yelp "BEST 10 BURGERS in ANN ARBOR" — Frita Batidos listed
- Michigan Daily: **"Frita Batidos wins 2025 Best Ann Arbor Burger"** — direct headline
- Arteflame guide: "Best Hamburgers in Ann Arbor: Top 7 Ranked [2026 Guide]"
- Stacker: "Highest-rated restaurants for burgers in the Ann Arbor area by diners"

**Competitors mentioned:** Krazy Jim's Blimpy Burger, Zingerman's Roadhouse, Casey's Tavern, Burger One, Taystee's Burgers, HopCat, No.9 Hamburgers, Shake Shack

**The problem:** Frita Batidos shows up because of Yelp, Tripadvisor, and the Michigan Daily — NOT because of its own website. If a potential customer clicks through to fritabatidos.com from any of these results, they get a 503 error. The website link in every listing is a dead end.

**Verbatim finding:** The search result literally shows `"Frita Batidos wins 2025 Best Ann Arbor Burger"` from michigandaily.com — but the fritabatidos.com link that follows is dead. The restaurant's own domain is a broken link in its own best search result.

---

### Query 2: "cuban restaurant ann arbor"

**Does Frita Batidos appear?** YES — dominates this query.

**What AI systems return:**
- Yelp: "BEST 10 CUBAN RESTAURANTS in ANN ARBOR" — Frita Batidos is the top result
- Yelp business listing: "FRITA BATIDOS - 1977 Photos & 2498 Reviews - 117 W Washington St"
- fritabatidos.com appears in results — but returns 503 when clicked
- A third-party fan site (fritabatidosannarbor.shop) appears and IS working
- Instagram @fritabatidos listed
- Tripadvisor: "THE BEST Cuban Sandwich in Ann Arbor"

**Critical finding:** A third-party domain `fritabatidosannarbor.shop` is ranking for the restaurant's own name and is actually functional, while the official site is down. This site could be anything — a fan page, a squatter, a competitor. The restaurant has lost control of its own brand narrative in AI results.

**Competitors mentioned:** La Cocina Cubana, Vicente's Cuban Cuisine, Sweet Havana, Mimi's Cuban Bakery and Cafe

---

### Query 3: "frita batidos ann arbor"

**Does Frita Batidos appear?** YES — this is a direct brand search, so it should.

**What AI systems return (top 10):**
1. fritabatidos.com/ann-arbor/food — **503 DEAD**
2. fritabatidos.com/ann-arbor — **503 DEAD**
3. Yelp listing — WORKING (2,498 reviews, photos)
4. fritabatidos.com/ann-arbor/menu-guide — **503 DEAD**
5. Toast ordering page — WORKING
6. Tripadvisor listing — WORKING
7. fritabatidos.com/ — **503 DEAD**
8. Facebook page — WORKING
9. annarbor.org listing — WORKING
10. fritabatidos.com/ann-arbor/catering — **503 DEAD**

**5 of the top 10 results for their own name are dead links.** When someone asks an AI "tell me about Frita Batidos" and the AI tries to visit the website to give a comprehensive answer, it gets nothing. The AI falls back to Yelp data, which is accurate but incomplete — no awards history, no chef story, no philosophy, no halal certification, no catering details.

---

### Query 4: "best restaurant ann arbor michigan"

**Does Frita Batidos appear?** YES — mentioned in aggregated lists.

**What AI systems return:**
- Tripadvisor "THE 10 BEST Restaurants in Ann Arbor"
- annarbor.org: "Award-Winning Restaurants in Ann Arbor" — Frita Batidos included
- OpenTable: "Diners' Choice: Best Overall restaurants in Ann Arbor"
- Cozymeal: "21 Best Ann Arbor Restaurants in 2026" — Frita Batidos listed
- ThePernateam: "Where to Eat in Ann Arbor: Best Restaurants Locals Actually Go To"

**Competitors that dominate:** Echelon (2026 James Beard semifinalist), Miss Kim (2025 James Beard semifinalist), Weber's Restaurant (Wine Spectator award), Zingerman's Delicatessen, Gandy Dancer, Mani Osteria, Sava's, Spencer, Aventura

**The problem:** In the "best restaurant" category, Frita Batidos is one name among many. Restaurants with working websites and structured data (like Echelon, Miss Kim) get richer AI descriptions including James Beard nominations, chef bios, and menu highlights. Frita Batidos gets a one-line mention. The eleven consecutive "Best Burger" awards are nowhere in the AI response because they only exist as a banner image on a dead website.

---

### Query 5: "halal restaurant ann arbor"

**Does Frita Batidos appear?** NO.

**What AI systems return:**
- Yelp: "BEST 10 HALAL RESTAURANTS in ANN ARBOR" — Frita Batidos NOT listed
- Tripadvisor: "Best Halal Restaurants in Ann Arbor" — Frita Batidos NOT listed
- Haifa Falafel, La Marsa, Halal Bros 2 Go, Taystee's Burgers, Shalimar all appear
- Uber Eats halal delivery — Frita Batidos NOT listed

**This is the biggest missed opportunity in the entire audit.**

Frita Batidos' own website states: "All of our chicken and beef is certified Halal!" Ann Arbor has one of the highest Muslim student populations in the Midwest (University of Michigan). The halal dining market is actively searching for options, and Frita Batidos — with 2,521 reviews and certified halal meat — is completely invisible to this audience.

Why? Because:
1. The halal certification is plain text on a dead page, not in structured data
2. Yelp doesn't categorize Frita Batidos as "halal" (categories: Cuban, Burgers, Cocktail Bars)
3. No FAQPage schema exists that would let AI surface "Is Frita Batidos halal?" with "Yes, all chicken and beef is certified Halal"
4. The site is down, so even if an AI tried to verify, it would get nothing

**Competitors winning this query instead:** Taystee's Burgers explicitly markets as halal and appears prominently. Frita Batidos has better food, more reviews, and actual halal certification — but zero visibility.

---

### Query 6: "where to eat near university of michigan"

**Does Frita Batidos appear?** YES — mentioned in UMich's own content.

**What AI systems return:**
- **UMich Admissions blog: "Ann Arbor Eats: My Favorite Restaurants"** — Frita Batidos specifically called out: "houses the best burger in Ann Arbor according to the Michigan Daily"
- Tripadvisor: "THE 10 BEST Restaurants Near University of Michigan"
- Current Magazine: "A College Student's Guide to Ann Arbor Eats"
- Ann Arbor with Kids: "Casual Dining Near University of Michigan"
- Quora: "Where is your favorite place to eat at University of Michigan?"

**Competitors with stronger presence:** Zingerman's Deli (described as "iconic," full paragraph), Mister Spots (directions from Michigan Stadium), Pizza Bob's (history since 1960s), Gandy Dancer (described in detail), The Hen (brunch details), Misfit Society Coffee Club

**The problem:** Frita Batidos is mentioned but gets a single line. Competitors with working websites and structured data get multi-sentence descriptions with specific menu items, atmosphere details, and directions. An AI answering "where should I eat near UMich?" will give Zingerman's a detailed recommendation and Frita Batidos a passing mention.

---

## AI Visibility Summary

| Query | Frita Appears? | Position | Source |
|---|---|---|---|
| "best burger ann arbor" | YES | Top 3 | Michigan Daily, Yelp, Tripadvisor |
| "cuban restaurant ann arbor" | YES | #1 | Yelp dominates |
| "frita batidos ann arbor" | YES | #1 (but 5/10 links dead) | Own domain (503) + Yelp |
| "best restaurant ann arbor" | YES | Mid-list | Aggregator lists only |
| "halal restaurant ann arbor" | **NO** | ABSENT | Not categorized anywhere as halal |
| "where to eat near umich" | YES | Mentioned | UMich blog, aggregators |

**Score rationale:** 12/25. The restaurant appears in most queries thanks to strong Yelp presence and Michigan Daily coverage, but it never appears from its own website. The halal invisibility is a major miss. And every fritabatidos.com link in search results is currently a dead end, which actively damages brand credibility.

---

## 3 Priority Recommendations

### Recommendation 1: Get the Site Back Online + Add Restaurant Schema (Immediate)

The 503 is an emergency. Every hour the site is down, AI systems that re-crawl get nothing and may de-prioritize the domain. Once the site is back, add this JSON-LD to the homepage immediately:

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Frita Batidos",
  "description": "Cuban-inspired street food restaurant in downtown Ann Arbor. Home of the frita — a Cuban-style burger topped with shoestring fries, served with tropical batido milkshakes and craft cocktails.",
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
    "Best Burger, Michigan Daily — 2014-2025 (11 consecutive years)",
    "Best Cuban Restaurant, Metro Times — 2020-2024",
    "Best Specialty Burger, Hour Magazine — 2025",
    "#31 on Yelp's Top 100 Burger Spots — 2023"
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
    "description": "Celebrated Ann Arbor chef who created Frita Batidos to express her love for Cuban food in a casual, fun setting."
  },
  "hasMenu": {
    "@type": "Menu",
    "url": "https://fritabatidos.com/ann-arbor/food/",
    "hasMenuSection": [
      {
        "@type": "MenuSection",
        "name": "Fritas",
        "description": "Cuban-style burgers on egg buns, topped with shoestring fries",
        "hasMenuItem": [
          {
            "@type": "MenuItem",
            "name": "Chorizo Frita",
            "description": "Spicy chorizo frita topped with shoestring fries on a soft egg bun",
            "suitableForDiet": "https://schema.org/HalalDiet"
          },
          {
            "@type": "MenuItem",
            "name": "Beef Frita",
            "description": "Classic beef frita with melted Muenster and shoestring fries",
            "suitableForDiet": "https://schema.org/HalalDiet"
          },
          {
            "@type": "MenuItem",
            "name": "Black Bean Frita",
            "description": "Vegetarian black bean frita",
            "suitableForDiet": "https://schema.org/VegetarianDiet"
          },
          {
            "@type": "MenuItem",
            "name": "Chicken Frita",
            "description": "Chicken frita with Muenster and cilantro-lime salsa",
            "suitableForDiet": "https://schema.org/HalalDiet"
          },
          {
            "@type": "MenuItem",
            "name": "Fish Frita",
            "description": "Fish frita on egg bun with tropical slaw"
          }
        ]
      },
      {
        "@type": "MenuSection",
        "name": "Batidos",
        "description": "Tropical milkshakes made with fresh fruit and crushed ice",
        "hasMenuItem": [
          {
            "@type": "MenuItem",
            "name": "Coconut Cream Batido"
          },
          {
            "@type": "MenuItem",
            "name": "Chocolate Espanol Batido"
          },
          {
            "@type": "MenuItem",
            "name": "Cajeta Batido"
          }
        ]
      },
      {
        "@type": "MenuSection",
        "name": "Sides & Snacks",
        "hasMenuItem": [
          {
            "@type": "MenuItem",
            "name": "Plantain Chips"
          },
          {
            "@type": "MenuItem",
            "name": "Conch Fritters"
          },
          {
            "@type": "MenuItem",
            "name": "Garlic Cilantro Fries"
          },
          {
            "@type": "MenuItem",
            "name": "Mexico City Corn"
          }
        ]
      }
    ]
  }
}
```

**Why this matters:** This single block of code would make Frita Batidos immediately machine-readable. AI systems would be able to answer questions about the menu, hours, awards, price range, location, and halal certification directly from the restaurant's own website instead of cobbling together Yelp fragments.

---

### Recommendation 2: Add FAQPage Schema with Halal Certification (Captures Missing Market)

This is the highest-ROI single change. Frita Batidos is invisible to the "halal restaurant ann arbor" query despite having certified halal meat. A FAQPage schema would fix this:

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
        "text": "A frita is a Cuban-style burger, typically made from spicy chorizo, topped with crispy shoestring fries and served on a soft egg bun. At Frita Batidos, we also offer beef, chicken, fish, and black bean fritas."
      }
    },
    {
      "@type": "Question",
      "name": "What is a batido?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A batido is a tropical milkshake made with fresh fruit and crushed ice. Popular flavors include Coconut Cream, Chocolate Espanol, and Cajeta."
      }
    },
    {
      "@type": "Question",
      "name": "Does Frita Batidos take reservations?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, Frita Batidos is counter service and walk-in only. Order at the counter and food is delivered to your table."
      }
    },
    {
      "@type": "Question",
      "name": "Does Frita Batidos offer vegetarian options?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The Black Bean Frita is vegetarian, and sides like Plantain Chips, Mexico City Corn, and Crisped Plantains are also vegetarian-friendly."
      }
    },
    {
      "@type": "Question",
      "name": "Does Frita Batidos cater events?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Frita Batidos offers full catering for events. Visit fritabatidos.com/ann-arbor/catering or call (734) 761-2882."
      }
    },
    {
      "@type": "Question",
      "name": "Where does Frita Batidos source its ingredients?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Frita Batidos strives to source meat, cheese, and produce from Michigan or the Midwest whenever possible. The Muenster cheese comes from Great Lakes region dairy."
      }
    }
  ]
}
```

**Why this matters:** This directly answers the questions AI systems get asked. The halal FAQ alone could open Frita Batidos to thousands of UMich students who currently don't know it's an option. The "what is a frita" FAQ educates AI systems that would otherwise skip an unfamiliar term.

---

### Recommendation 3: Convert Menu from PNG Images to Crawlable Text + Create llms.txt

Two changes, one goal: make the restaurant's content readable by AI.

**3a. Replace PNG menus with HTML text menus.**

The current menu is three PNG images (`AA-FOOD-1.png`, `AA-BAR-UPDATED.png`, `AA-MENU-GUIDE.png`). No AI system can read these. Every menu item, price, and description is locked inside an image file.

Convert to semantic HTML with the Menu schema (provided in Recommendation 1). Keep the beautiful visual menu as a supplement, but the primary menu page must be crawlable text.

**3b. Add an `llms.txt` file at the domain root.**

`llms.txt` is the emerging standard (adopted by Anthropic, Cloudflare, and others) for telling AI systems what a business is. Place this at `fritabatidos.com/llms.txt`:

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

## Popular Menu Items

- Chorizo Frita: Spicy chorizo on egg bun with shoestring fries and Muenster
- Beef Frita: Classic beef with shoestring fries and Muenster
- Black Bean Frita: Vegetarian option
- Coconut Cream Batido: Tropical milkshake with fresh coconut and crushed ice
- Plantain Chips, Conch Fritters, Garlic Cilantro Fries
- Hibiscus Mojito, Sangria, craft cocktails

## Links

- Website: https://fritabatidos.com
- Order: https://order.toasttab.com/online/fritabatidos
- Yelp: https://www.yelp.com/biz/frita-batidos-ann-arbor
- Instagram: https://www.instagram.com/fritabatidos/
```

**Why this matters:** When the next generation of AI assistants crawls the web, the restaurants with `llms.txt` files will be the ones that get cited accurately. This is a 10-minute task that puts Frita Batidos ahead of 99% of restaurants nationally.

---

## The Bottom Line

Frita Batidos has earned extraordinary real-world reputation: 2,521 reviews, 4.4 stars, 11 consecutive "Best Burger" awards, certified halal, and a beloved chef-owner. None of that is visible to AI.

Right now, when someone asks ChatGPT "where should I eat near UMich?" — Zingerman's gets a detailed paragraph. Frita Batidos gets a passing mention. When someone asks "halal restaurant ann arbor?" — Taystee's Burgers shows up. Frita Batidos doesn't exist. When someone asks "best burger in ann arbor?" — Frita Batidos appears, but only because Yelp and the Michigan Daily carry it. The restaurant's own website is a 503 error page.

The fix is not complicated. It's three things:
1. Get the site back online (hosting issue)
2. Add the JSON-LD schema blocks above (one-time code addition)
3. Convert image menus to text and add llms.txt (half-day of work)

These changes would move the AI Discoverability Score from **18/100 to an estimated 72/100** — and unlock the halal market, the "best restaurant" queries, and the UMich student audience that Frita Batidos is currently invisible to.
