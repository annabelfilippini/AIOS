# Hop Alley — Internal Audit

**Audited:** 2026-04-15
**Prospect:** Hop Alley (Denver, CO) — Tommy Lee, Chef/Owner
**URL:** https://hopalleydenver.com/
**Platform:** Squarespace
**Contact:** info@hopalleydenver.com, reservations@hopalleydenver.com, (720) 379-8340

## Summary

Hop Alley is a three-peat Michelin Bib Gourmand restaurant (2023–2025), 2025 James Beard semifinalist for Outstanding Wine & Beverage, 2020 JBF Mountain Region semifinalist, and 2025 Michelin Exceptional Cocktails awardee. None of those credentials are machine-readable. The site's `@type` is generic `LocalBusiness`, not `Restaurant`. Seven awards exist as bold body copy with zero `award` schema. Menus are Canva PDFs Google can't index. The headline data point: **Perplexity, asked "best sichuan restaurant denver," places Hop Alley below Wok Spicy of Englewood with the framing "not strictly Sichuan-only"** — a Michelin-caliber restaurant losing category-claim to a suburb restaurant with zero accolades because the competitor owns the vocabulary on its homepage.

The core issue is **discovery, not conversion.** Branded traffic that lands on hopalleydenver.com converts fine (Tock, Toast, phone). The leak is upstream: category queries, AI-driven recommendations, and dish-level search. The fix is structured (schema), architectural (HTML menus), and narrative (chef/concept stories).

**Critical cross-find:** Uncle Ramen (Tommy Lee's sister concept) ships with `<h1>Copy of HOME</h1>` in production. This audit speaks to both properties.

---

## Technical Health

### Working
- Squarespace foundation is clean (valid markup, responsive layout, HTTPS enforced)
- OG tags and Twitter Card tags populated for social shares
- `openingHours` machine-readable (schema-parseable for Google Assistant / Perplexity)
- robots.txt and sitemap.xml both present, linked to each other, and allow every major AI crawler (GPTBot, ClaudeBot, anthropic-ai, Bytespider, CCBot, Google-Extended)

### Issues

| # | Finding | Severity | Effort |
|---|---|---|---|
| T1 | **Two H1s per page** (`Hop Alley` + `FOLLOW US`), zero H2s, skips straight to H3 | 🟠 High | 30 min |
| T2 | **Homepage meta description is empty.** Title tag fine. SERP previews fall back to scraped text | 🔴 Critical | 5 min |
| T3 | **Broken delivery CTA** — `[delivery via UberEats, postmates & doordash]` links to hopalleydenver.com itself (self-link). Postmates absorbed by Uber in 2020. | 🟠 High | 15 min |
| T4 | **Stale Instagram embed** — 4 hand-picked posts, all from May 2022, shown to 2026 visitors | 🟡 Medium | 15 min (embed live feed or remove) |
| T5 | **No analytics of any kind** — no GA4, no GTM, no Meta Pixel, no Squarespace Analytics surfaced | 🟠 High | 1 hr |
| T6 | **`/home-3` leaked in sitemap.xml** — appears to be an unpublished variant, exposes draft content to crawlers | 🟡 Medium | 5 min |
| T7 | **`openingHours` trailing comma** (`... Sa 17:00-22:00, `) — malformed string | 🟢 Low | 2 min |
| T8 | **Copy typos** — `RESERVATIONS VIA TOCk`, inconsistent Bar Chelou / "Petit Chelou" capitalization | 🟢 Low | 15 min |
| T9 | **4 of 12 homepage images have `alt=""`.** Food photography with empty alt = lost search relevance + a11y fail | 🟡 Medium | 30 min |
| T10 | **No `lang` attribute on `<html>`, no skip-nav, no ARIA landmarks** (Squarespace default) | 🟢 Low | 15 min |

---

## SEO

### Working
- **Branded dominance:** "hop alley" and "hop alley denver" both rank #1
- **`chinese tasting menu denver` ranks #1** with zero competition (free win — just needs a landing page to cement)
- "best chinese food denver" at #4 (present, not leading)
- "chinese restaurant denver" at #4

### Keyword Visibility Table

| # | Keyword | Intent | Autocomplete | Position | Root cause |
|---|---|---|---|---|---|
| 1 | hop alley | Branded | Active | #1 | Owned |
| 2 | hop alley denver | Branded | Active | #1 | Owned |
| 3 | chinese restaurant denver | Category | Active | #4 | No geo-modifier in H1, aggregator pages dominate |
| 4 | sichuan restaurant denver | Category | Modest | Not in top 10 | Vocabulary: site says "Chinese" not "Sichuan" |
| 5 | michelin restaurants denver 2025 | Category | Active | Not in top 10 | 7 awards in text, 0 in schema |
| 6 | michelin bib gourmand denver | Category | Modest | Michelin Guide cites (Hop Alley itself absent) | No `award` schema |
| 7 | best chinese food denver | Intent | Active | #4 | 5280/VisitDenver lists lead |
| 8 | chef's counter denver | Intent | Thin | Buried | No dedicated page; Beckon owns it |
| 9 | upscale chinese denver | Intent | Active | Not in top 10 | Word "upscale" never used on site |
| 10 | chinese tasting menu denver | Intent | Zero | #1 | Free win — no landing page to cement |

### Issues

| # | Finding | Severity | Effort |
|---|---|---|---|
| S1 | **Canva PDF menus (×5) unindexable.** Every dish-level query (mapo tofu, dan dan noodles, vegan chinese, gluten free chinese — all 40+ menu items) bypasses hopalleydenver.com entirely | 🔴 Critical | 4–6 hrs (HTML menu build + schema) |
| S2 | **Vocabulary mismatch: "Sichuan" on site, "Szechuan" in searcher behavior.** Autocomplete for `sichuan restaurant denver` suggests `best szechuan restaurant in denver` as #1 — a spelling fork users actively search | 🟠 High | 15 min (add "Sichuan (Szechuan)" in hero + schema + meta) |
| S3 | **No `/about`, no `/chef`, no press page.** Tommy Lee is mentioned once on homepage. Doug Rankin (Chef's Counter) isn't named anywhere on the site despite Westword/New Denizen features | 🟠 High | 2–3 hrs |
| S4 | **Chef's Counter (Doug Rankin) buried mid-homepage** — no dedicated URL, no schema, no hero card, no photo. "Chinese tasting menu denver" = #1 uncontested, no page to cement | 🟠 High | 2 hrs |
| S5 | **Autocomplete queries unanswered on-site:** `hop alley michelin star` (no — Bib Gourmand), `hop alley happy hour` (no info), `hop alley owner` (Tommy Lee, no bio), `hop alley tasting menu` (Chef's Counter, not labeled that way), `hop alley reviews` (off-site only) | 🟡 Medium | 1 hr |
| S6 | **"Michelin Bib Gourmand" never uses that exact phrase on-site.** Copy says "Michelin Bib Gourmand" in the awards list but no Michelin Guide outbound link | 🟡 Medium | 30 min |
| S7 | **pytrends 429 blocked trend data this pass.** Recommendations don't depend on it; pull manually if seasonality comes up | 🟢 Low | — |

---

## AI Discoverability — **Score: 65/100**

Four-subscore summary:

| Subscore | Score | Max |
|---|---|---|
| Crawler access | 18 | 25 |
| Schema markup | 8 | 25 |
| Content structure | 9 | 25 |
| Authority signals | 14 | 25 |
| Live LLM queries | 16 | 25 |

Full data in `ai-seo-research.md`. Key findings below.

### Verbatim Perplexity (2026-04-15)

**Query: "best sichuan restaurant denver"**
> A strong current pick is Wok Spicy in Englewood for the most authentic Sichuan-style cooking near Denver. It explicitly brands itself as authentic Sichuan cuisine… Hop Alley — not strictly Sichuan-only, but it's a Michelin Bib Gourmand restaurant and a top Denver Chinese restaurant overall… If you want the single best bet for traditional Sichuan heat and flavor, Wok Spicy is the safest recommendation.

**Query: "michelin bib gourmand denver 2025"**
> Denver's 2025 Michelin Bib Gourmand restaurants are Ash'Kara, Basta, Cozobi Fonda Fina, The Ginger Pig, Glo Noodle House, Hop Alley, La Diabla Pozole y Mezcal, MAKfam, Mister Oso, and Tavernetta.

(Cited but alphabetical — no emphasis on three-peat streak.)

**Query: "hop alley denver hours menu"**
> Hop Alley in Denver is at 3500 Larimer St, Denver, CO 80205… Monday through Saturday, 5:00 p.m. to 10:00 p.m.; it's closed on Sundays… chilled tofu, Beijing duck rolls, la zi ji, soft shell crabs…

(Accurate on essentials — but menu content came from Toast / press, not Hop Alley's site.)

### Issues

| # | Finding | Severity | Effort |
|---|---|---|---|
| A1 | **`@type: LocalBusiness` instead of `Restaurant`.** Missing `servesCuisine`, `priceRange`, `acceptsReservations`, `menu`, `starRating` | 🔴 Critical | 30 min |
| A2 | **Zero `award` schema for 7 accolades.** James Beard × 2, Michelin Bib × 3, Michelin Cocktails × 1, 5280 #1 × 1 — all invisible to Knowledge Panel and rich results | 🔴 Critical | 30 min |
| A3 | **No `Person` schema for Tommy Lee or Doug Rankin.** "Tommy Lee chef Denver" queries unlinkable to Hop Alley | 🟠 High | 1 hr |
| A4 | **No FAQ page + no FAQPage schema.** FAQ is the single biggest AI-citation win for restaurants; Perplexity and Claude quote FAQ answers verbatim | 🟠 High | 1 hr |
| A5 | **No `llms.txt`.** Declarative LLM-readable site index absent. Template drafted in `ai-seo-research.md` | 🟡 Medium | 15 min |
| A6 | **`sameAs` only Facebook (with obsolete `?fref=ts`).** No Instagram, Michelin Guide, OpenTable, Google Business | 🟡 Medium | 5 min |
| A7 | **No `Review` / `AggregateRating` schema.** Yelp/OpenTable have strong ratings; declaring them first-party enables star snippets in SERPs | 🟢 Medium | 1 hr |

Copy-pasteable JSON-LD for A1–A3 + A6 lives in `ai-seo-research.md` Section 2.

---

## Accessibility

### Working
- HTTPS, responsive, keyboard focus ring present (Squarespace default)
- `openingHours` machine-readable
- No `aria-label` abuse or hidden-by-default content patterns detected

### Issues

| # | Finding | Severity | Effort |
|---|---|---|---|
| AX1 | **Canva PDF menus are inaccessible** — screen readers cannot read the image-text content. Affects 5 menus covering every dietary restriction | 🟠 High | Fixed by S1 (HTML menus) |
| AX2 | **Empty `alt=""` on 4 of 12 homepage images** (food photography) | 🟡 Medium | 30 min |
| AX3 | **Missing `lang` attribute on `<html>` root** | 🟢 Low | 5 min |

Not audited this pass: color contrast ratios (need Lighthouse run), form labels on contact/reservation, focus order full trace.

---

## Content & UX

### Working
- **Brand voice is coherent** — "WE ACCEPT TAKE OUT ORDERS OVER THE PHONE AT 3:30P" reads as an intentionally punchy, unfiltered house voice
- **Awards copy is confident** (bold, prominent placement above the fold)
- **Photography exists and is good quality** (food + interiors from the image sitemap)
- **Large-party info page** does its job — clear 9+ capacity rules, set menu pricing, pre-purchase explanation

### Issues

| # | Finding | Severity | Effort |
|---|---|---|---|
| C1 | **Reservation platform contradiction: homepage says Tock, `/large-party-info` says Resy.** One is wrong. Trust-killer for a Michelin property | 🔴 Critical | 10 min |
| C2 | **No entity-clarity sentence in hero.** First H3 is an operational notice. No "Hop Alley is a [what] in [where]" | 🟠 High | 30 min |
| C3 | **Chef's Counter ($$$$ per-seat tasting, 6 seats nightly) buried mid-page.** Tommy's highest-margin product, no dedicated URL, no hero card, no Rankin bio | 🟠 High | Covered by S4 |
| C4 | **Dual-channel takeout UX needs three paragraphs to explain** — phone at 3:30, online at 5, no allergies online. Should be one button + one sentence | 🟠 High | 1 hr |
| C5 | **No press/review section, no press logos.** Michelin, JBF, 5280 mentioned as text only — no Michelin Guide outbound link, no logo wall, no reviewer pull-quotes (303 Magazine, Westword, Food & Wine, Denver Post) | 🟠 High | 2 hrs |
| C6 | **H1 "Hop Alley" carries no value prop or modifier** — no "Denver's three-peat Michelin Bib Gourmand Chinese kitchen" framing | 🟡 Medium | 10 min |
| C7 | **Gift cards story split and undersold.** One sentence, no visual. Gift cards drive 5–15% of restaurant revenue Nov–Dec at Michelin-tier properties | 🟡 Medium | 2 hrs |
| C8 | **Tock/Toast pages carry zero Hop Alley brand presence beyond logo.** Full context-switch every external click | 🟡 Medium | Medium (Tock custom theme, Toast storefront styling) |

---

## Uncle Ramen (Companion Property)

Tommy Lee's sister concept on uncleramen.com. Audited as a companion because Tommy owns both — findings surface in the client doc as a second-property signal that operational hygiene is an unresolved pattern.

| # | Finding | Severity | Effort |
|---|---|---|---|
| U1 | **`<h1>Copy of HOME</h1>`** shipped to production | 🔴 Critical | 2 min |
| U2 | **Broken phone link in markup** — `[303.433.326](tel:3034333263) 3` — trailing `3` outside anchor. Dead `tel:` link | 🔴 Critical | 2 min |
| U3 | **Stale "STARTING APRIL 8TH, RESERVATIONS WILL BE AVAILABLE THROUGH OPENTABLE" announcement** + visible typo "EXITING RESERVATIONS" (meant "EXISTING") | 🟠 High | 5 min |
| U4 | **Three inconsistent names** — "Uncle," "Uncle Ramen," "Uncle Restaurant" — across title, H1, legalName, body | 🟡 Medium | 30 min |
| U5 | **Platform split** — Hop Alley on Tock, Uncle Ramen on OpenTable. Two customer bases, no cross-promotion | 🟡 Medium | Decision |

---

## AI Opportunities (Hop Alley-specific)

| Opportunity | Impact | Effort | Connects to |
|---|---|---|---|
| **FAQ page + FAQPage schema** — 5 questions drafted in `ai-seo-research.md` answer the top autocomplete variants (Michelin star?, tasting menu?, hours?, dietary?, platform?) | 🔴 High | 1–2 hrs | A4, S5, C1 (FAQ resolves Tock/Resy confusion) |
| **`llms.txt` with awards + pages + chef names** | 🟡 Medium now, 🟠 High in 12 mo | 15 min | A5 |
| **Restaurant + Menu + MenuItem schema on HTML menus** — `suitableForDiet: VeganDiet` etc. Unlocks long-tail dish queries | 🟠 High | Included in S1 | S1, A1 |
| **Award schema block** — all 7 accolades, year by year | 🔴 Critical | 30 min | A2 |
| **Doug Rankin + Tommy Lee Person schema on an About/Team page** | 🟡 Medium | 1 hr | A3, S3 |
| **AggregateRating schema pulled from OpenTable + Google** — enables star snippets in Google | 🟡 Medium | 1 hr | A7 |

---

## Priority Action List

### This week (6–8 hrs, $0 software cost)
1. **Replace all three JSON-LD blocks with the `Restaurant` block from `ai-seo-research.md` Section 2.** Single Squarespace Code Injection paste. Immediately unlocks Knowledge Panel, Michelin-query rich results, Sichuan category claim.
2. **Add meta description** to homepage (draft: "Michelin Bib Gourmand Chinese restaurant in Denver's RiNo. Regional Sichuan cuisine, three-time Bib Gourmand (2023–2025), James Beard semifinalist for Outstanding Wine & Beverage. Reservations via Tock.")
3. **Fix the Tock/Resy contradiction** on `/large-party-info`. Both pages should say Tock.
4. **Fix H1 structure.** One H1 per page, demote "FOLLOW US" to H2, demote operational notices from H3 to paragraph-class text with a visible-but-semantic style.
5. **Fix broken delivery CTA self-link** + drop Postmates.
6. **Uncle Ramen: fix "Copy of HOME" and the broken phone link.** Two-minute fixes on a second-property crisis.
7. **Publish `/llms.txt`** using the template in `ai-seo-research.md` Section 5.

### This month (12–16 hrs)
8. **Ship HTML menus** (5 variants: main, vegan, pescatarian, vegetarian, gluten-free) with `Menu` schema. Replaces Canva PDFs.
9. **Build `/chefs-counter` page** with Doug Rankin bio + Person schema + tasting-menu terminology + Tock deep-link CTA. Owns "chinese tasting menu denver" (already #1) + "chef's counter denver" (currently #2 after Beckon).
10. **Build `/about` or `/team`** with Tommy Lee bio + Person schema + accolades timeline.
11. **Install GA4 + Meta Pixel** (or Squarespace Analytics minimum). Baseline conversion data before further changes.
12. **Build FAQ page** using schema from `ai-seo-research.md` Section 3 Fix B.
13. **Press/accolades section** with logos + Michelin Guide outbound link + reviewer pull-quotes.

### This quarter (20+ hrs)
14. **Simplify takeout UX** (one button, one sentence, drop the cutoff-time explanation from the hero).
15. **Refresh Instagram embed** to live feed or remove entirely.
16. **Gift cards** storytelling + seasonal hero block (Nov–Dec).
17. **Custom Tock theme / Toast storefront styling** to carry brand across external touchpoints.
18. **Uncle Ramen: full entity-reconciliation pass** (pick one name, rebuild schema, fix stale announcement, reconsider OpenTable-vs-Tock strategic choice).

---

## Sources

- `scrape-data.md` — 20 findings, 5 Uncle Ramen findings, external touchpoints, reference site analysis
- `seo-research.md` — 10-keyword scorecard, vocabulary mismatch, 3 top recommendations
- `ai-seo-research.md` — 65/100 score, four subscores, verbatim Perplexity, copy-pasteable schema
- `scrape/raw-html-analysis.json` — meta, schema, heading, alt data for 4 pages
- `scrape/screenshots/` — 9 screenshots
- `reference/mister-jius/`, `reference/atomix/` — Michelin analogue reference sites
- `companion/uncle-ramen/` — sister concept scrape
