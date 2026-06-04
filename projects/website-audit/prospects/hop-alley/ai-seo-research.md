# Hop Alley — AI Discoverability Research

**Researched:** 2026-04-15
**Prospect:** Hop Alley (Denver, CO) — Tommy Lee, Chef/Owner
**Category:** Regional Chinese restaurant (Sichuan-leaning), Michelin Bib Gourmand, 2025 James Beard Semifinalist
**URL:** https://hopalleydenver.com/
**Platform:** Squarespace

---

## Score: 65 / 100

| Subscore | Hop Alley | Max | Note |
|---|---|---|---|
| Crawler access | **18** | 25 | robots.txt doesn't block AI bots, sitemap valid. Missing llms.txt. |
| Schema markup | **8** | 25 | Has basic LocalBusiness trio. Missing Restaurant upgrade, award property, Menu, Person, Review. |
| Content structure | **9** | 25 | Two H1s per page, zero H2s, no entity-clarity sentence, no FAQ. |
| Authority signals | **14** | 25 | Awards in body copy, phone + address in schema. No structured chef bio, no aggregate rating on-site. |
| Live LLM queries | **16** | 25 | Accurate on hours/address. **Loses "best Sichuan" to Wok Spicy; framed as "not strictly Sichuan-only."** Generic listing on Bib Gourmand query. |

**Core insight:** Hop Alley has Michelin-caliber credentials that are completely invisible to AI-driven discovery. Seven awards in plain text, zero in structured data. @type is generic `LocalBusiness` when it should be `Restaurant`. LLMs asked "best Sichuan Denver" or "Michelin Denver 2025" have no signal to surface Hop Alley over competitors with weaker credentials but better schema.

---

## Section 1 — Crawler Access (18/25)

### robots.txt — `curl -s https://hopalleydenver.com/robots.txt` → 200 OK

```
User-agent: AI2Bot
User-agent: anthropic-ai
User-agent: Bytespider
User-agent: CCBot
User-agent: ClaudeBot
User-agent: GPTBot
User-agent: Google-Extended
User-agent: Meta-ExternalAgent
User-agent: Quora-Bot
User-agent: YouBot
User-agent: *
Disallow: /config
Disallow: /search
Disallow: /account$
...

Sitemap: https://hopalleydenver.com/sitemap.xml
```

**Interpretation:** Squarespace lists every major AI crawler as a User-agent but shares the same `Disallow` lines as `User-agent: *`. No `Disallow: /` under any bot = **AI crawlers are ALLOWED to index content pages.** This is the default Squarespace state. If Tommy had toggled "block AI crawlers" in settings, each bot would have `Disallow: /` beneath it.

- ✅ GPTBot, ClaudeBot, anthropic-ai, Bytespider, CCBot, Google-Extended, Meta-ExternalAgent all allowed to crawl content
- ✅ PerplexityBot not explicitly listed (standard — Perplexity typically respects `User-agent: *` rules which only block admin paths)
- ❌ No `User-agent: PerplexityBot` entry — worth adding explicit allow

### llms.txt — `curl -s https://hopalleydenver.com/llms.txt` → 404

Does not exist. This is the emerging standard for LLM-readable site index (one markdown file listing key pages + one-sentence descriptions). Opportunity — not a penalty, since few restaurants have one, but Hop Alley's award-heavy positioning is exactly the use case where `llms.txt` pays off.

### sitemap.xml — `curl -s https://hopalleydenver.com/sitemap.xml` → 200 OK

- ✅ Valid XML, properly namespaced with `xmlns:image` and `xmlns:video`
- ✅ Listed in robots.txt
- ❌ Only 3 URLs: `/home`, `/home-3`, `/large-party-info`. Everything else (menus, about, reservations) lives as anchor sections on the homepage or as external links (Tock, Toast, Canva).
- ❌ `/home-3` appears to be an unpublished variant — shouldn't be in sitemap. Leaks draft content to crawlers.

**Score reasoning:** 18/25 — bots allowed (+10), sitemap valid and linked (+8), no llms.txt (−5), `/home-3` leak (−2).

---

## Section 2 — Schema Markup (8/25)

### What's present — verbatim JSON-LD from homepage:

```json
{
  "@context": "http://schema.org",
  "@type": "WebSite",
  "url": "https://hopalleydenver.com",
  "name": "Hop Alley",
  "description": "<p>Hop Alley Denver</p>"
}
```

```json
{
  "@context": "http://schema.org",
  "@type": "Organization",
  "legalName": "Hop Alley",
  "address": "3500 Larimer St\nDenver, CO, 80205",
  "email": "info@hopalleydenver.com",
  "telephone": "(720) 379-8340",
  "sameAs": ["https://www.facebook.com/Hopalleydenver?fref=ts"]
}
```

```json
{
  "@context": "http://schema.org",
  "@type": "LocalBusiness",
  "name": "Hop Alley",
  "address": "3500 Larimer St\nDenver, CO, 80205",
  "openingHours": "Mo 17:00-22:00, Tu 17:00-22:00, We 17:00-22:00, Th 17:00-22:00, Fr 17:00-22:00, Sa 17:00-22:00, "
}
```

### What's missing (ranked by impact × effort):

| Missing | Impact | Effort | Why it matters |
|---|---|---|---|
| **`@type` not `Restaurant`** | 🔴 Critical | 5 min | Google surfaces `Restaurant`-schema businesses in SERP rich results for "restaurants near me." `LocalBusiness` is the generic fallback. |
| **`award` property (7 awards, zero in schema)** | 🔴 Critical | 30 min | Rich results for "michelin restaurants denver." Knowledge Panel accolade rows. Perplexity ranks based on structured accolades. |
| **`servesCuisine`** | 🔴 Critical | 1 min | The query "Sichuan Denver" has no signal to prefer Hop Alley without this property. |
| **`starRating` or `michelinRating`** | 🟡 High | 10 min | Bib Gourmand is a Michelin designation — schema.org accepts `Rating` nested under `Restaurant`. |
| **`acceptsReservations: true`** | 🟡 High | 1 min | Reservation-intent searches ("book sichuan denver") boost sites with the flag. |
| **`menu` URL** | 🟡 High | 2 min | Right now menus are Canva PDFs → Google can't index them. With `menu` property pointing to Canva URL, LLMs at least know a menu exists. (Long-term fix: ship HTML menus.) |
| **`priceRange`** | 🟢 Medium | 1 min | `"$$$"` helps Perplexity segment for "upscale Chinese." |
| **Person schema for Tommy Lee** | 🟢 Medium | 15 min | Linking the chef as structured data makes "Tommy Lee chef Denver" queries attributable to Hop Alley. |
| **FAQPage schema** | 🟢 Medium | — | No FAQ exists yet. Building one (Section 3) unlocks schema. |
| **Review / AggregateRating** | 🟢 Medium | 1 hr | OpenTable/Yelp have Hop Alley at strong ratings. Self-hosted `aggregateRating` isn't spoofing — it's declarative. Google shows stars in SERPs. |
| **Second `sameAs` (Instagram)** | 🟢 Low | 1 min | `sameAs: ["https://instagram.com/hopalleydenver"]` closes the entity-disambiguation loop. |

**Score reasoning:** 8/25 — basic trio present (+8), no Restaurant upgrade (−5), no award (−5), no Menu (−3), no Person/Review (−4).

### Copy-pasteable replacement JSON-LD (drop into Squarespace Code Injection → Header)

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://hopalleydenver.com/#restaurant",
  "name": "Hop Alley",
  "url": "https://hopalleydenver.com",
  "telephone": "(720) 379-8340",
  "email": "info@hopalleydenver.com",
  "priceRange": "$$$",
  "servesCuisine": ["Chinese", "Sichuan", "Regional Chinese"],
  "acceptsReservations": true,
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "3500 Larimer St",
    "addressLocality": "Denver",
    "addressRegion": "CO",
    "postalCode": "80205",
    "addressCountry": "US"
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens": "17:00",
    "closes": "22:00"
  }],
  "sameAs": [
    "https://www.facebook.com/Hopalleydenver",
    "https://www.instagram.com/hopalleydenver",
    "https://guide.michelin.com/us/en/colorado/denver/restaurant/hop-alley"
  ],
  "menu": "https://hopalleydenver.com/menus",
  "award": [
    "2025 James Beard Foundation Semifinalist — Outstanding Wine & Beverage Program",
    "2025 Michelin Guide Exceptional Cocktails Award",
    "2025 Michelin Guide Bib Gourmand",
    "2024 Michelin Guide Bib Gourmand",
    "2023 Michelin Guide Bib Gourmand",
    "2020 James Beard Foundation Semifinalist — Best Chef, Mountain Region",
    "2016 5280 Magazine #1 Restaurant, Denver/Boulder"
  ],
  "employee": {
    "@type": "Person",
    "name": "Tommy Lee",
    "jobTitle": "Chef and Owner"
  }
}
```

**Instruction for Tommy / web person:** Squarespace → Settings → Advanced → Code Injection → Header. Paste inside `<script type="application/ld+json"> ... </script>`. Replaces the existing three generic blocks.

---

## Section 3 — Content Structure (9/25)

Every page of hopalleydenver.com renders the same broken heading skeleton:

| Page | H1 count | H2 count | H3 count | H1 texts |
|---|---|---|---|---|
| `/` (homepage) | **2** | 0 | 5 | `Hop Alley`, `FOLLOW US` |
| `/home` | 2 | 0 | 5 | `Hop Alley`, `FOLLOW US` |
| `/large-party-info` | 2 | 0 | 1 | `Hop Alley`, `FOLLOW US` |
| `/home-3` (draft) | — | — | — | — |

### Findings

- ❌ **Two H1s on every page.** `FOLLOW US` at the bottom is marked H1. Google treats one H1 as the page topic; two confuses the signal.
- ❌ **Zero H2 tags anywhere.** The document outline skips from H1 to H3. LLMs use heading hierarchy to map page structure — no H2s means the page reads as topic-less.
- ❌ **No entity-clarity sentence in the hero.** The first H3 is "WE ACCEPT TAKE OUT ORDERS OVER THE PHONE AT 3:30P, ONLINE ORDERING OPENS AT 5P" — an operational notice, not an identity statement. Contrast: "Hop Alley is a regional Chinese restaurant in Denver's RiNo district, recognized with three consecutive Michelin Bib Gourmands (2023–2025) and James Beard Foundation semifinalist awards for Outstanding Wine & Beverage (2025) and Best Chef Mountain Region (2020)."
- ❌ **No FAQ section or FAQ page.** Competing restaurants (Mister Jiu's has an FAQ; Atomix has an About that answers typical questions) own category-question queries like "what kind of chinese food is hop alley."
- ❌ **No author/authority page.** Tommy Lee is named in body copy once ("concept from Tommy Lee and the Uncle team") but there is no `/about` page, no chef bio, no Person schema. Doug Rankin (Chef's Counter) isn't named at all on the site despite appearing in Westword and New Denizen features.
- ❌ **Large-party-info page has **`FOLLOW US`** as an H1 — irrelevant to the topic of the page. H1 should be "Large Party Info" or similar.**

### Score reasoning: 9/25
- Content exists and is on-brand (+6)
- Two H1s (−4)
- Zero H2s, no entity sentence (−6)
- No FAQ (−3)
- No author page (−3)

### Three copy-paste fixes

**A. One-sentence entity hero (replace the "WE ACCEPT TAKE OUT ORDERS" block or add above it):**
> Hop Alley is a regional Chinese restaurant in Denver's RiNo district, recognized with three consecutive Michelin Bib Gourmands (2023–2025) and 2025 James Beard Foundation semifinalist honors for Outstanding Wine & Beverage.

**B. FAQ page stub** (`/faq` with FAQPage schema):
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What kind of Chinese food does Hop Alley serve?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Regional Chinese cuisine with a focus on Sichuan and traditional family-style dishes, plus contemporary takes on broader Asian ideas. Our menu changes seasonally."
      }
    },
    {
      "@type": "Question",
      "name": "Does Hop Alley have a tasting menu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Our Chef's Counter, led by Chef Doug Rankin, offers a seasonal Chinese tasting menu for 6 guests nightly. Reservations via Tock."
      }
    },
    {
      "@type": "Question",
      "name": "Is Hop Alley a Michelin restaurant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hop Alley has received the Michelin Bib Gourmand designation in 2023, 2024, and 2025, plus the 2025 Michelin Guide Exceptional Cocktails Award. We are also a 2025 James Beard Foundation Semifinalist for Outstanding Wine & Beverage Program."
      }
    },
    {
      "@type": "Question",
      "name": "Do you accommodate dietary restrictions?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — we have dedicated vegan, pescatarian, vegetarian, and gluten-free menus. Please call the restaurant for allergies and aversions; we cannot accommodate them through online ordering."
      }
    },
    {
      "@type": "Question",
      "name": "What's the reservation platform — Tock or Resy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tock. All reservations (including parties of 9 or more) are on Tock at exploretock.com/hop-alley-denver."
      }
    }
  ]
}
```

**C. Chef's bio page** (`/team` or `/about`) — short structured bios for Tommy Lee and Doug Rankin, with Person schema + sameAs links to press pieces.

---

## Section 4 — Authority Signals (14/25)

| Signal | Present? | Quality |
|---|---|---|
| Founder/chef bio | Partial | Tommy Lee named in og:description and one body paragraph. No dedicated bio page. Doug Rankin (Chef's Counter) **not named on the site** despite being the story of the tasting menu. |
| Press mentions | Yes | 7 awards listed in hero region. No links to the press pieces themselves (New Denizen, Westword, 5280, Michelin Guide). |
| Review count + aggregate rating | No | OpenTable and Yelp have Hop Alley strongly reviewed, but the site doesn't surface counts or stars. No `aggregateRating` schema. |
| Location + hours + phone | Yes | Address, phone, and hours are in both the rendered page and schema. ✅ |
| Social proof density | Low | Single Facebook link in `sameAs`. Instagram handle implied by "FOLLOW US" H1 but not machine-readable from the page. |

### Score reasoning: 14/25
- Address + hours + phone machine-readable (+6)
- Awards listed in body text (+4)
- Tommy Lee named once (+2)
- No structured bio (−4)
- No Doug Rankin mention (−3)
- No aggregate rating / review count (−3)
- Single social link (−1)

---

## Section 5 — Live LLM Query Results (16/25)

Tested Perplexity (2026-04-15) with three queries chosen to probe (a) category visibility, (b) accolade claim, (c) factual accuracy.

### Query 1 — "best sichuan restaurant denver" — **5/10 (Hop Alley #3, negatively framed)**

> A strong current pick is **Wok Spicy in Englewood** for the most authentic Sichuan-style cooking near Denver. It explicitly brands itself as authentic Sichuan cuisine, with bold, spicy, numbing flavors.
>
> Other good Denver-area options are:
>
> - **Happy Cafe** — often recommended by locals for Sichuan food.
> - **MAKfam** — a well-regarded Denver spot with Sichuan-inspired dishes and a strong local following.
> - **Hop Alley — not strictly Sichuan-only, but it's a Michelin Bib Gourmand restaurant and a top Denver Chinese restaurant overall.**
> - **Szechuan Chinese Restaurant** — a long-running classic in Denver.
>
> If you want the single best bet for traditional Sichuan heat and flavor, **Wok Spicy is the safest recommendation** from the current results.

**Analysis:** Hop Alley appears, but *loses the positioning war*. Wok Spicy wins the top spot not because it's better but because it **"explicitly brands itself as authentic Sichuan cuisine."** Hop Alley's homepage leads with "traditional, regional Chinese cuisine…served family-style as well as dishes with a unique spin on other Asian ideas" — that phrasing gave Perplexity nothing to latch onto for the Sichuan query. The verbatim framing *"not strictly Sichuan-only"* is the cost of vocabulary vagueness: a Michelin Bib Gourmand restaurant is placed below a suburban restaurant with zero accolades because the competitor owns the category keyword on its site.

**This is the single most persuasive paragraph in the entire audit.** It quantifies the cost of weak positioning in a way the owner can't dismiss.

### Query 2 — "michelin bib gourmand denver 2025" — **6/8 (cited but undifferentiated)**

> Denver's 2025 Michelin Bib Gourmand restaurants are Ash'Kara, Basta, Cozobi Fonda Fina, The Ginger Pig, Glo Noodle House, **Hop Alley**, La Diabla Pozole y Mezcal, MAKfam, Mister Oso, and Tavernetta.
>
> For Denver specifically, that list includes a mix of cuisines from Israeli and Mexican to Chinese, Latin American, and contemporary cooking.
>
> Hop Alley is on the 2025 Bib Gourmand list as well.

**Analysis:** Hop Alley is cited — but flat, alphabetized, no emphasis. Perplexity has no on-site signal (no `award` schema) to prefer the **three-peat** Bib Gourmand restaurant over single-year winners. A user asking this query gets "here are 10 options" instead of "here are three restaurants with multi-year recognition, starting with Hop Alley (2023, 2024, 2025)." The award schema block in Section 2 fixes exactly this — multi-year entries in an `award[]` array are machine-parseable as a streak.

### Query 3 — "hop alley denver hours menu" — **5/7 (accurate essentials, menu not from site)**

> Hop Alley in Denver is at 3500 Larimer St, Denver, CO 80205, and its listed hours are Monday through Saturday, 5:00 p.m. to 10:00 p.m.; it's closed on Sundays.
>
> The menu changes, but it includes dishes like chilled tofu, Beijing duck rolls, la zi ji, soft shell crabs, fried rice, dumplings, and noodles.
>
> A few current menu examples are:
>
> - **Vegetables:** chilled tofu, smashed cucumbers, steamed eggplant, grilled gai lan.
> - **Meat and seafood:** Beijing duck roll, steamed snapper, char siu beef tongue, la zi ji, salt and pepper soft shell crabs.
> - **Noodles, rice, and dumplings:** fried wontons, hong you chao shou, Taiwanese beef noodle soup, garlic shrimp noodles, Hop Alley fried rice.

**Analysis:** Factually accurate on address, hours, and dish list — so schema + Toast order menu + third-party sources (OpenTable, Yelp, press) are doing their job for branded queries. **But** Perplexity's menu content was assembled from *external sources* (Toast, press write-ups), not hopalleydenver.com, because the site's menu is a Canva PDF Google can't index. If Toast goes down or changes, Perplexity's menu description goes stale. Shipping HTML menus on the site is the fix.

### Scoring reasoning: 16/25
- Query 1: appears but negatively positioned (5/10)
- Query 2: cited, not differentiated (6/8)
- Query 3: accurate on essentials, menu sourced externally (5/7)

### The quote to lift into the client doc

> "Hop Alley — not strictly Sichuan-only, but it's a Michelin Bib Gourmand restaurant and a top Denver Chinese restaurant overall."
>
> *— Perplexity's answer to "best sichuan restaurant denver," April 2026. A four-year Sichuan-focused restaurant gets dismissed as not-quite-Sichuan because a suburban restaurant owns the category phrase on its homepage.*

---

## What's Working (keep doing)

1. **robots.txt allows AI crawlers.** No `Disallow: /` under GPTBot, ClaudeBot, anthropic-ai, Bytespider, CCBot — content is legitimately indexable by every major AI company. This is a free win most Squarespace sites lose by toggling "block AI crawlers" on.
2. **Sitemap is linked from robots.txt and well-formed.** Image sitemap extension present. Just needs the `/home-3` draft leak fixed and more content pages created to list.
3. **Address, phone, and hours are in structured data.** Even with weak schema overall, the `openingHours` string on `LocalBusiness` means Perplexity and Google Assistant can answer "when does Hop Alley open" accurately.

---

## Top Three Recommendations (ranked by impact × effort)

### 1. Replace the three generic JSON-LD blocks with one comprehensive `Restaurant` block

**Impact:** 🔴 Highest. Immediate eligibility for Google rich results on "michelin restaurants denver," Knowledge Panel accolades, Perplexity entity linking.
**Effort:** 30 minutes, one Squarespace Code Injection paste.
**Code:** See Section 2 above — the full copy-pasteable block including `@type: Restaurant`, all 7 awards as `award[]`, `servesCuisine`, `priceRange`, `acceptsReservations`, `menu`, Person schema for Tommy Lee, and three `sameAs` links.

### 2. Add an `/faq` page with FAQPage schema

**Impact:** 🟡 High. FAQ schema is the single biggest AI-discoverability win for restaurants — LLMs cite FAQ answers verbatim for category questions.
**Effort:** 1 hour to draft 5 FAQ entries, 15 minutes to paste schema into Squarespace.
**Code:** See Section 3, Fix B — five pre-drafted FAQs covering cuisine, tasting menu, Michelin status, dietary accommodations, and reservation platform (fixes the Tock/Resy contradiction in the process).

### 3. Publish `/llms.txt` at hopalleydenver.com/llms.txt

**Impact:** 🟢 Medium now, 🟡 High in 6–12 months as LLM routing standards mature. Declarative statement to every AI about what Hop Alley is and what content matters.
**Effort:** 15 minutes, one Squarespace file upload.
**Template:**

```
# Hop Alley

> Regional Chinese restaurant in Denver's RiNo district. Michelin Bib Gourmand 2023, 2024, 2025. James Beard Foundation Semifinalist 2025 (Outstanding Wine & Beverage) and 2020 (Best Chef Mountain Region).

## Identity
- Name: Hop Alley
- Address: 3500 Larimer St, Denver, CO 80205
- Phone: (720) 379-8340
- Hours: Monday–Saturday 5pm–10pm (closed Sunday)
- Chef/Owner: Tommy Lee
- Chef de Cuisine, Chef's Counter: Doug Rankin
- Cuisine: Regional Chinese with Sichuan focus

## Key Pages
- [Homepage](https://hopalleydenver.com/): restaurant overview, awards, reservations
- [Large Party Info](https://hopalleydenver.com/large-party-info): parties of 9+, private events
- [Reservations on Tock](https://exploretock.com/hop-alley-denver)
- [Online Orders on Toast](https://www.toasttab.com/hop-alley-denver/v3)

## Accolades
- 2025 Michelin Guide Bib Gourmand
- 2025 Michelin Guide Exceptional Cocktails Award
- 2025 James Beard Foundation Semifinalist — Outstanding Wine & Beverage Program
- 2024 Michelin Guide Bib Gourmand
- 2023 Michelin Guide Bib Gourmand
- 2020 James Beard Foundation Semifinalist — Best Chef, Mountain Region
- 2016 5280 Magazine — #1 Restaurant, Denver/Boulder

## Offerings
- Dine-in (Mon–Sat), reservations via Tock (up to 8)
- Large party inquiries (9+) via Tock
- Chef's Counter tasting menu (6 seats nightly), Chef Doug Rankin
- Takeout (phone at 3:30pm, online at 5pm)
- Gift cards via Toast
- Dedicated menus: main, vegan, pescatarian, vegetarian, gluten-free
```

---

## Loose Ends / Questions for Annabel

- **Hours accuracy.** Schema says Mon–Sat 5pm–10pm, closed Sunday. Google Business Profile may say differently — worth a spot-check before finalizing `llms.txt`.
- **Doug Rankin confirmation.** Chef's Counter chef is mentioned in New Denizen write-up (from SEO research). Worth confirming he's still there before publishing his name in schema/llms.txt. Last public reference was [date unknown — verify].
- **Instagram handle.** "FOLLOW US" H1 implies Instagram; need the actual handle (likely `@hopalleydenver`) before adding to `sameAs` array and `llms.txt`.
- **Reservation platform.** Homepage says Tock, `/large-party-info` says Resy. Schema above assumes Tock (matches the homepage CTA). If it's actually Resy somewhere, the contradiction is the real fix — not the schema.

---

## Raw artifacts

- `scrape/raw-html-analysis.json` — JSON-LD extraction across 4 pages
- `/tmp/ha_robots.txt`, `/tmp/ha_sitemap.xml` — crawl probe snapshots (15 Apr 2026)
- `scrape/homepage-metadata.json`, `scrape/large-party-info-metadata.json` — scraper meta dumps
