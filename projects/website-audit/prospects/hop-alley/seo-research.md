# Hop Alley — SEO Research

**Researched:** 2026-04-15
**Prospect:** Hop Alley (Denver, CO) — Tommy Lee, Chef/Owner
**Cuisine:** Regional Chinese with Sichuan leanings
**Accolades:** 2025 James Beard Semifinalist (Outstanding Wine & Beverage), 2025 Michelin Exceptional Cocktails Award, 2023/2024/2025 Michelin Bib Gourmand, 2020 James Beard Semifinalist (Best Chef Mountain Region), 2016 5280 #1 Denver/Boulder

**Raw artifacts:** `seo/autocomplete.json`, `seo/diy_atp.json`, `seo/trends_error.txt` (pytrends 429 + urllib3 lib bug — trend data not pulled this pass)

---

## Executive Summary

Hop Alley is a Michelin-Bib-Gourmand, James-Beard-semifinalist Chinese restaurant that shows up fine for branded searches but is **invisible on the three category queries that matter most**: "sichuan restaurant denver," "upscale chinese denver," and "michelin restaurants denver 2025." The site's own menu page exists but links to Canva PDFs that Google can't index, so every dish-level query (mapo tofu denver, vegan chinese denver, dan dan noodles denver) bypasses hopalleydenver.com entirely.

There's also one clean **untapped opportunity**: the Chef's Counter (Doug Rankin, ex-Bar Chelou) is a Chinese tasting-menu concept with almost zero competition in SERPs — the query "chinese tasting menu denver" has Hop Alley #1 already despite zero optimization, and there's no dedicated page to build on that.

**Three biggest SEO fixes:**
1. **Ship HTML menus** (replace Canva PDFs) — unlocks dish-level discovery across every menu variant (main, vegan, pescatarian, vegetarian, GF).
2. **Build a Chef's Counter page** at `/chefs-counter` with Rankin's bio + schema + reservations CTA — owns "chinese tasting menu denver" and competes for "chef's counter denver."
3. **Add `award` schema markup** (7 awards, 0 in structured data) — triggers Knowledge Panel + rich results for "michelin restaurants denver" / "bib gourmand denver," where Hop Alley is currently text-invisible.

---

## Keyword Scorecard

| # | Keyword | Type | Autocomplete depth | Hop Alley position | Top competitor | Gap diagnosis |
|---|---|---|---|---|---|---|
| 1 | hop alley | Branded | 10 (active) | **#1** | Yelp, Michelin Guide | Owned. Branded knowledge intact. |
| 2 | hop alley denver | Branded | 10 (active) | **#1** | Yelp, Michelin Guide, Tock | Owned. |
| 3 | chinese restaurant denver | Category | 10 (active) | **#4** | Bao Brewhouse, Imperial, MAKfam, TripAdvisor lists | Losing to aggregator pages + 1985-era Imperial. No H1 geo-modifier on Hop Alley. |
| 4 | sichuan restaurant denver | Category | 5 (modest) | **Not in top 10** | Szechuan Chinese Restaurant (Lakewood), Szechuan Tasty House, Yelp | **Vocabulary mismatch**: searchers type "szechuan," site says "Sichuan." Also Hop Alley homepage leads with "Chinese" not "Sichuan." |
| 5 | michelin restaurants denver 2025 | Category | 10 (active) | **Not in top 10** | Denverite, 9News, OpenTable, Visit Denver list articles (Wolf's Tailor, Kizaki, Margot surface) | Seven awards in text, **zero in schema**. Google can't parse the accolades into rich-result eligibility. |
| 6 | michelin bib gourmand denver | Category | 7 (modest) | Listed by Michelin Guide (**#1 result is the Guide index**) | The Ginger Pig, Tavernetta, MAKfam, Glo Noodle House | Hop Alley's own site doesn't surface for this — only the Michelin Guide entry does. Missing `Restaurant` schema with `starRating` + `award`. |
| 7 | best chinese food denver | Intent | 10 (active) | **#4** | Imperial, MAKfam, Bao Brewhouse, 5280 article | Present but not leading. Trusted third-party lists (5280, visitdenver blog) dominate top-3. |
| 8 | chef's counter denver | Intent | **2 (thin)** | Mentioned but buried | **Beckon** (Michelin-starred Duncan Holmes), Westword list, 5280, newdenizen article about Hop Alley's counter | **Biggest missed opportunity**: Rankin's story is written up by New Denizen + Westword, but Hop Alley has no dedicated URL, no schema, no booking CTA for the Chef's Counter. Beckon owns this query. |
| 9 | upscale chinese denver | Intent | 10 (active) | **Not in top 10** | Imperial, Fortune Wok to Table, Miya Moon, Q House | Hop Alley doesn't position itself as "upscale" or "fine dining" anywhere on the site. Missing the word entirely. |
| 10 | chinese tasting menu denver | Intent | **0 (none)** | **#1** | Effectively nobody | **Free win available**: zero competition, zero autocomplete volume means intent users searching this find Hop Alley by default. Build a page to cement it and capture long-tail ("denver chinese tasting menu," "hop alley chef's counter menu"). |

**Visibility summary:** 4 visible (#1-4 rank), 4 invisible (category queries where competitors dominate), 2 mixed (present but not leading).

---

## Vocabulary Mismatch — The Sichuan Problem

The site consistently says **"Sichuan"** (homepage hero, menu, press quotes). Google Autocomplete and live searcher behavior show:

- `sichuan restaurant denver` → 5 autocomplete suggestions, one of which is literally **"best szechuan restaurant in denver"** (spelling swap)
- Yelp/Westword/5280 all index the restaurant under **"Szechuan"** category pages
- DIY AnswerThePublic: seed `sichuan denver` returned **zero** expansions across 16 prefix combinations — the phrase barely exists as a search idiom
- Seed `chinese food denver` returned expansion on vegan, near-me, delivery, and reservation variants — this is where real search volume lives

**Fix:** Use "Sichuan (Szechuan)" once in hero copy, once in schema `servesCuisine` array, once in meta description. Doesn't compromise brand voice, captures the search variant.

---

## Untapped Markets (from DIY AnswerThePublic)

### 1. Direct-intent "hop alley" questions Hop Alley doesn't answer on-site
Autocomplete shows real searchers asking:

- **"is hop alley michelin star"** → they're Bib Gourmand, not starred. Site should have an Awards/Accolades section that clarifies. Currently bold text, no context.
- **"hop alley happy hour"** → no mention on site. Either add one or state "no happy hour" to capture the query (a common restaurant pattern).
- **"hop alley owner"** → Tommy Lee. No chef/owner bio page. High-intent people-searching users hit Instagram instead.
- **"hop alley tasting menu"** → this is the Chef's Counter. Nobody calls it a "tasting menu" on the site. Rewriting the section to use that terminology captures the query.
- **"hop alley hours"** → hours are on the site, but only in footer as schema `openingHours` (trailing comma malformed). Hours should be in HTML copy too, above the fold.
- **"hop alley reviews"** → reviews land on Yelp. Pull 3-4 press quotes (303 Magazine, 5280, Westword, Food & Wine) into a reviews section on-site.

### 2. Menu-variant queries the Canva PDFs lose
Autocomplete shows:

- "vegan chinese food denver" (exists — their vegan Canva menu is unindexable)
- "gluten free chinese denver" (exists — same problem)
- "chinese food denver delivery" (they deliver via Toast / Uber Eats / DoorDash — homepage Postmates CTA is broken, links to self)

Every one of these is a menu Hop Alley already has. None are indexable because all 5 menus are Canva PDFs. Converting to HTML = instant long-tail discovery for every ingredient/dish/dietary variant.

### 3. "does denver have michelin" awareness queries
DIY ATP seed `michelin denver`:

- "does denver have michelin star restaurants"
- "any michelin star restaurants in denver"
- "how many michelin star restaurants in colorado"

High-volume **awareness** queries. Hop Alley doesn't capture any of these because (a) they're Bib Gourmand not starred and (b) their schema hides their accolades entirely. A well-structured "Michelin Recognition" block on-site (with image, context, and Michelin Guide outbound link) feeds the snippet economy for this cluster.

---

## Competitor Analysis

| Competitor | Why they rank above Hop Alley | What Hop Alley can do |
|---|---|---|
| **Imperial Chinese** | 40-year brand, blog content ("Why Imperial is the best…"), "Best of Denver 13 years running" copy everywhere | Content isn't the moat here — Hop Alley beats them on actual accolades. It's discoverability: add blog/press page, make awards indexable. |
| **Bao Brewhouse** | Multi-concept site with indexed menu pages, stronger LoDo SEO | HTML menus close the gap. |
| **MAKfam** | Cleaner Michelin Guide integration + Denver Bib Gourmand coverage by press | MAKfam and Hop Alley are peers in the Bib Gourmand list — MAKfam just has better schema. |
| **Beckon** | Dominates "chef's counter denver" — Michelin-starred, dedicated site name, clean schema, reservation flow on-site | Can't beat a starred property on that query alone, but "chinese tasting menu denver" is uncontested. Own that instead. |
| **Szechuan Tasty House / Lakewood Szechuan** | Spelling variant + decade of Westword / Yelp presence | Adding "Szechuan" in one spot captures the searchers confused about the spelling. |

---

## Google Trends — not pulled this pass

pytrends 429'd on both attempts (known issue per skill). The installed `pytrends==4.9.2` also has a urllib3 compat bug (`method_whitelist` → `allowed_methods`). For this audit, SERP + autocomplete + DIY ATP is enough signal. **If trend data becomes critical before outreach, pull manually from trends.google.com for:**

- `hop alley` (CO should be #1 — branded)
- `chinese food denver` (expect seasonal dips, holiday bumps)
- `michelin bib gourmand denver` (expect 2025-09 guide release spike)

None of these are likely to change the recommendations below.

---

## Top 3 Recommendations

### 1. Build the Chef's Counter page — free win on zero-competition query
- URL: `/chefs-counter` (or `/chef-rankin`)
- Content: Rankin bio (Bar Chelou / José Andrés / Ludo Lefebvre lineage), photo, menu format explanation, booking CTA (Tock deep-link), press pull-quotes (New Denizen, Westword)
- Schema: `Restaurant` subtype with `chef` property, `menu` HasMenu pointing to the counter menu
- Target queries: "chinese tasting menu denver" (already #1, cement it), "chef's counter denver" (currently dominated by Beckon but Hop Alley can reach #2), "doug rankin denver"
- **Impact:** High. Low competition + high-intent conversion ($$$$ 6-seat dinner).

### 2. Ship HTML menus — unlock dish-level SEO
- Replace all 5 Canva PDF links with HTML pages: `/menu` (main), `/menu/vegan`, `/menu/pescatarian`, `/menu/vegetarian`, `/menu/gluten-free`
- Schema: `Menu` + nested `MenuSection` + `MenuItem` with `name`, `description`, `price`, `suitableForDiet` (e.g., `VeganDiet`, `GlutenFreeDiet`)
- Mobile-readable, accessible, indexable
- Target queries: "vegan chinese food denver," "gluten free chinese denver," "mapo tofu denver," "dan dan noodles denver" + every dish name
- **Impact:** Medium-high. Dish queries are lower volume individually but compound across a menu of ~40+ items.

### 3. Award schema + press section — unlock rich results for Michelin/JBF queries
- Restaurant schema with `award` array (7 awards), `starRating` analogue for Bib Gourmand (use `Rating` with `ratingValue`), `sameAs` including Michelin Guide URL, Instagram, Tock, Google Business
- Upgrade `@type` from `LocalBusiness` to `Restaurant` with `servesCuisine: ["Chinese", "Sichuan"]`, `priceRange: "$$$"`, `acceptsReservations: true`
- Add a visible Accolades section with Michelin + JBF + 5280 logos (link out to each source)
- Add meta description (currently empty) with awards + category + location: *"Michelin Bib Gourmand Chinese restaurant in Denver's RiNo. Sichuan-inspired menu, James Beard semifinalist chef Tommy Lee, and a 6-seat Chef's Counter from Doug Rankin."*
- Target queries: "michelin restaurants denver 2025," "michelin bib gourmand denver," "best chinese food denver," "upscale chinese denver"
- **Impact:** High. Seven awards with zero structured-data representation is the single biggest discoverability leak on the property.

---

## Honesty caveats

- **Search positions are as of 2026-04-15 WebSearch pulls.** SERPs fluctuate; Reddit and aggregator domains (TripAdvisor, Yelp, OpenTable) often move 1-3 positions per day.
- **Trend data gap.** pytrends 429 + lib bug prevented pulling interest-over-time. Recommendations don't depend on it, but if Tommy Lee asks about seasonality, pull manually before the call.
- **No manual keyword-volume enrichment.** Ubersuggest/SEMrush not queried — the recommendations lean on autocomplete depth as a volume proxy (10 suggestions = active, 0-2 = thin). For a $500 deliverable, confirm at least the top 3 fixes' target keywords in Google Keyword Planner before client sign-off.
- **Michelin Bib Gourmand vs. Star:** Hop Alley is Bib Gourmand, not a Michelin Star. Copy must not overstate — "Michelin-recognized" / "Bib Gourmand" are accurate; "Michelin-starred" is not.
