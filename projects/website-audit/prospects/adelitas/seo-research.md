# Adelitas + La Doña — SEO Keyword Research

**Researched:** 2026-04-14
**Tools:** WebSearch (SERPs), Google Autocomplete (`suggestqueries.google.com`), pytrends (interest_over_time + interest_by_region + DMA)
**Raw data:** `autocomplete.json`, `trends.json`

---

## TL;DR (top 3 findings)

1. **Adelitas is invisible for the search that matters 10x more than anything else.** "Mexican restaurant Denver" has a Denver-DMA interest score of 56 (vs. 14 for "best Mexican food Denver," 1 for "mezcal bar Denver," 0 for "Michoacán food Denver"). Adelitas does not appear on page 1 of this SERP. Casa Bonita, Tamayo, Los Chingones, Alma Fonda Fina, and **Ni Tuyo (Silvia Andaya's own third property)** are the names Google surfaces.
2. **The 17 doorway pages are a policy-violation AND they're working.** `/best-mexican-food-in-denver-colorado`, `/tequila-restaurant-in-denver`, `/mezcal-in-denver`, `/best-mexican-restaurant-in-denver` are actively ranking on multiple queries. Pruning without 301s destroys existing rank. Consolidation plan must be a redirect map, not a deletion.
3. **Chef Silvia Andaya's personal brand has zero search authority.** Google Autocomplete returns 0 suggestions for her name. Only one editorial mention (Shoutout Colorado) is indexed. This is the single highest-leverage untapped asset — Adelitas, La Doña, and Ni Tuyo all trace back to one chef with a Michoacán heritage story that's already written but buried on a doorway page.

---

## Keyword Scorecard

| # | Keyword | Intent | Denver DMA | Autocomplete depth | Adelitas rank | What ranks instead |
|---|---|---|---|---|---|---|
| 1 | Adelitas Denver | Branded | n/a | 10 (max) | Adelitas dominates | Yelp, OpenTable, /broadway, doorway page, adelitasco.com |
| 2 | La Doña mezcaleria Denver | Branded | n/a | 1 | **punycode URL ranks** | xn--ladoamezcaleria-1qb.com, Instagram, Yelp |
| 3 | Chef Silvia Andaya | Personal brand | n/a | **0** | Scattered across doorway pages | Shoutout Colorado interview (single editorial) |
| 4 | Mexican restaurant Denver | Category (high-vol) | **56** | 10 (max) | **Invisible on page 1** | Casa Bonita, Tamayo, Los Chingones, **Ni Tuyo**, Alma Fonda Fina |
| 5 | Michoacán food Denver | Unique positioning | 0 | 5 | Mentioned on Uncover Colorado + doorway #3 | Carnitas Estilo Michoacán, Patzcuaro's, La Adelita (Glendale) |
| 6 | Mezcal bar Denver | La Doña differentiator | 1 | 10 | /mezcal-in-denver doorway ~#6; La Doña punycode ranks | Mezcal (Colfax), **Malinche Audio Bar**, Mezcaleria Alma, Ni Tuyo |
| 7 | Family-owned Mexican restaurant Denver | Narrative-matched | n/a | 6 | Doorway ranks ~#4 | Chakas, El Sampa, Castañeda's; Adelitas missing from editorial "10 Family-Owned" roundup |
| 8 | Best Mexican food Denver | Intent (discovery) | 14 | 10 (max) | Doorway ranks ~#7 | Tripadvisor list, DoorDash blog, Los Chingones, Tamayo, Alma Fonda Fina |
| 9 | Mexican restaurant Denver reservations | Booking intent | n/a | 10 | **Invisible** | Tamayo (has online booking), Rio on Wazee, Alma Fonda Fina, Ni Tuyo |
| 10 | Tequila dinner Denver | Event intent | 29 (proxy: "tequila Denver") | 4 | Two doorways rank #2 and #3 | Tacos Tequila Whiskey, Casa Tequila, Federales |

**Quality-check call-outs:**
- Adelitas's OpenTable listing exists (`opentable.com/r/adelitas-cocina-y-cantina-denver`) — contradicts the Step 2 scrape finding "no reservation system detected." The booking integration is set up; it's just not linked from adelitasco.com or referenced in structured data. Step 4 audit should flag this.
- **Ni Tuyo is a third Andaya property** at nituyo.com — surfaced in SERPs for "mezcal bar Denver" and "Mexican restaurant Denver." Step 2 scrape did not capture it. Adelitas does not cross-link to Ni Tuyo from either site.

---

## Seasonality (12-mo interest_over_time, US)

| Term | Mean | Peak week | Signal |
|---|---|---|---|
| Mexican restaurant Denver | 71.8 | 2026-01-25 | **Post-holiday dining window.** January–February is when discovery-intent peaks. |
| Tequila Denver | 40.2 | 2025-05-18 | **Cinco de Mayo bump.** May is when tequila-intent ranking pays off. |
| Best Mexican food Denver | 6.9 | 2025-07-06 | **Summer-visitor window.** July is peak discovery for tourists. |
| Mezcal bar Denver | 0.0 | 2026-04-05 | Interest rising but negligible (peak value = 2). Positioning claim, not a search-volume channel. |
| Michoacán food Denver | 0.0 | — | Zero search volume in Denver metro. A differentiator claim, not a ranking target. |

**Implication:** the three calendar windows that matter are January (discovery), May (Cinco de Mayo tequila), and July (summer visitors). Any SEO work should land before those.

---

## Root-Cause Diagnoses

### Why Adelitas is invisible on "Mexican restaurant Denver" (the one search that matters)

- **Site says** "Authentic Mexican Restaurant Denver Colorado | Adelitas" on identical Broadway and Edgewater location pages with `LocalBusiness` JSON-LD. Same title on two self-canonical pages = Google picks one and suppresses the other; neither accumulates link equity. Meanwhile the root URL (`adelitasco.com/`) — the page every backlink lands on — has title `"Location Picker"` with no meta, no h1, no JSON-LD. Google's best candidate to rank on "Mexican restaurant Denver" is a thin chooser page with zero semantic content.
- **Searchers expect** a branded, locationally-anchored restaurant homepage with reviews, menu, and booking. Adelitas's homepage can't even identify itself.
- **Fix:** the root URL becomes a proper homepage with the location chooser in the nav, not the body. Broadway and Edgewater pages get differentiated content (different photos, different menu highlights, different review pulls) so they stop competing with each other for the same slot.

### Why Chef Silvia Andaya has zero search authority

- **Site says** her story only on `/tequilas-family-mexican-restaurant` — a doorway-branded URL with 6 h1 tags and a keyword-stuffed template. It reads as an SEO page, not an editorial one.
- **Searchers would type** "Silvia Andaya chef," "Adelitas owner," "Michoacán chef Denver" — and Google finds nothing authoritative. The one editorial piece (Shoutout Colorado) isn't reinforced by any owned content.
- **Fix:** Promote the chef story to a dedicated `/chef` or `/story` page with person-schema `JSON-LD`, editorial photography, press quotes. Cross-link from Adelitas, La Doña, and Ni Tuyo. This is the hub that unifies three properties into one brand universe.

### Why La Doña is effectively invisible

- **Site says** its canonical URL is the punycode `xn--ladoamezcaleria-1qb.com` (with tilde). The plain-ASCII domain users actually type (`ladonamezcaleria.com`) is not canonical. All backlink equity is flowing to a URL users can't type from memory. The JSON-LD `url` field is a **different** broken punycode (`xn--laoamezcaleria-1qb.com`, missing an "n") — a malformed domain that schema parsers reject.
- **Searchers expect** one consistent, typeable URL.
- **Fix:** commit to one canonical (recommend the plain-ASCII), 301 the other, correct the JSON-LD. This is a 30-minute engineering change with outsized SEO impact.

### Why the 17 doorway pages are a trap

- **Site says** each doorway targets one keyword ("best-mexican-food-in-denver-colorado", "mezcal-in-denver") with 5-6 h1 tags, 25K characters of keyword-stuffed narrative, 15 images with 12 empty alts, and the same `LocalBusiness` / `Organization` / `WebSite` JSON-LD verbatim. Google's doorway policy explicitly describes this pattern. Risk: manual action → site-wide demotion.
- **But:** these pages are currently Adelitas's entire ranking presence. Kill them without a plan and the restaurant goes dark for 3–6 months.
- **Fix:** consolidate into 3-4 legitimate content hubs — `/menu` (real, crawlable), `/tequilas-and-mezcal` (bar program story), `/our-story` (Silvia + Michoacán heritage), `/brunch` (separate brunch menu). 301-redirect each doorway to the closest consolidated hub. Preserves keyword coverage by merging it into fewer, higher-quality pages.

### Why "adelitas denver reservations" is unmet intent

- **Autocomplete suggests** `adelitas denver reservations` as the 4th most-typed extension of the branded query — real people are searching for this.
- **Site provides** no booking widget, no "Reservations" nav link, no `/reservations` page. OpenTable integration exists but is not discoverable from the site.
- **Fix:** surface the OpenTable link in the top-right nav, add `Reservation` schema, build a `/reservations` page that links to OpenTable for both Broadway and Edgewater.

### Why "Michoacán" is a claim, not a channel

- **Trends data:** "Michoacán food Denver" has a Denver-DMA interest score of 0. Nobody types this.
- **But:** it is the single strongest identity differentiator — no other Denver Mexican restaurant has Silvia's generational Michoacán lineage.
- **Fix:** Michoacán is a brand story for *owned* channels (homepage hero, editorial press, about page), not an SEO keyword target. Stop optimizing for it; start *narrating* it.

---

## Untapped Markets

### 1. Editorial roundups (the single biggest gap)

Adelitas is **missing from every third-party "best of Denver" list** surfaced in SERPs:
- Uncover Colorado "8 Best Mexican Restaurants"
- DoorDash "Best Mexican Food in Denver"
- Cozymeal "Top 21 Mexican Restaurants in Denver"
- Classpop "Best in 2025"
- "10 Family-Owned Mexican Restaurants In Colorado" (Every After in the Woods)

Their entire SEO presence is *their own doorway pages* + Yelp/OpenTable aggregators. Zero earned editorial. Westword has a bare location listing, not a feature.

**Opportunity:** a 6-week PR push — pitch Westword, 5280, Eater Denver, Uncover Colorado on the "one chef, three restaurants, one Michoacán lineage" angle. Editorial backlinks are worth more than 17 doorway pages combined.

### 2. "Denver Taco Tuesday" + delivery/order-online intent

Autocomplete for branded queries surfaces:
- `adelitas denver taco tuesday` (they're known for this per Yelp "raucous Taco Tuesdays")
- `adelitas denver delivery`
- `adelitas denver happy hour`
- `adelitas order online`

None of these have dedicated pages on the site. The product (Taco Tuesdays, happy hour, delivery) exists. The SEO surface for it does not.

### 3. Ni Tuyo as a hub linker

Ni Tuyo ranks on "Mexican restaurant Denver" where Adelitas doesn't. The Andaya family has three brands that **do not cross-link to each other** and therefore share no domain authority. A simple footer block on each property linking to the other two would lift all three.

### 4. Subcategory queries Malinche and Mezcaleria Alma are winning

"Mezcal listening bar Denver", "mezcal audio bar Denver", "best mezcal bar Denver" — these pull Malinche, Mezcaleria Alma, and the original Mezcal (Colfax). La Doña doesn't appear in autocomplete for any of them. La Doña has real mezcal depth (Oaxacan positioning, chef-led) but the site is a single Showit page with no crawlable content. A real `/mezcal-program` page with the list of spirits, the Oaxacan story, and the tasting-flight offer would start capturing this subcategory.

### 5. Brand-collision mitigation

Autocomplete for "Adelitas" is crowded with:
- "Las Adelitas" (other restaurants nationally)
- "La Adelita" (a Glendale, CO Mexican restaurant — same Michoacán claim)
- "Adelitas way" (a rock band)
- Liga MX Femenil soccer/basketball (Adelitas teams)

Branded SERPs for "Adelitas" in Denver are mostly clean, but unbranded "Adelita near me" gets mixed into these. **Owning "Adelitas Cocina y Cantina" and "Adelitas Denver" unambiguously matters.** Meta titles should always include "Cocina y Cantina" to disambiguate from La Adelita (Glendale) specifically. The Glendale restaurant is the single highest name-collision risk because they also claim Michoacán heritage.

---

## Top 3 Recommendations (for `/audit-analyze` to deepen)

### 1. Consolidate 17 doorway pages → 4 legitimate hubs with a 301 map. *Before pruning.*

- `/menu` — real HTML, linked from primary nav, searchable (Adelitas currently routes "Menus" to `/qr-code-menu`, an HTML-empty stub).
- `/our-story` — Silvia + Michoacán + La Adelita heritage; absorb the story currently buried at `/tequilas-family-mexican-restaurant`.
- `/tequilas-and-mezcal` — bar program, ~200 tequilas referenced, absorbs `/tequila-restaurant-in-denver`, `/mezcal-in-denver`, `/top-cocktail-bars-in-denver`.
- `/brunch` — absorbs `/best-brunch-in-denver-colorado`, `/best-mexican-breakfast-denver`, `/best-breakfast-burritos-denver`, `/denver-breakfast-burrito`.

301-redirect the remaining 13 doorway URLs to the closest hub. Preserve keyword coverage; eliminate policy-violation risk.

### 2. Fix the root URL and the canonical leaks. *30–60 minutes of engineering.*

- `adelitasco.com/` becomes a real homepage: hero, Silvia's story teaser, menu preview, reservation CTAs for both locations, Ni Tuyo + La Doña cross-links in footer.
- Location picker moves to header nav ("Broadway" / "Edgewater"), where it belongs.
- Broadway vs. Edgewater pages get differentiated content so they stop duplicate-competing.
- La Doña canonical switched to plain-ASCII `ladonamezcaleria.com`; punycode 301s in; JSON-LD `url` corrected.
- JSON-LD `name` fixed from "Adeli Tasco" → "Adelitas Cocina y Cantina" across every page carrying the schema.

### 3. Build the Chef Silvia Andaya editorial hub + push for one major press hit in the next 6 weeks.

- New `/chef` page with Person schema: full bio, Michoacán lineage, photo, press quotes, links to Adelitas/La Doña/Ni Tuyo.
- Pitch Westword, 5280, Eater Denver: "One chef, three Denver restaurants, one Michoacán lineage." The angle exists; the press story is un-pitched.
- Cross-link from all three restaurant sites. Unified brand universe = shared domain authority.

**Expected impact (qualitative):** recommendations 1+2 are 100% defensive (avoid Google penalty, fix broken plumbing). Recommendation 3 is the only offensive play, but it compounds — the chef hub becomes the asset every future piece of press, SEO, and social content points to.

---

## Handoff to `/audit-analyze` (Step 4)

Findings that the client-facing audit should lead with:
- The root URL is a placeholder (confirmed by SERP data — adelitasco.com itself doesn't rank for anything meaningful)
- Doorway pages must be consolidated, not deleted — show the 301 map
- OpenTable integration exists but isn't surfaced (one-line fix, high intent)
- Ni Tuyo is part of the family and should be cross-linked
- Chef Silvia's story is the marketing asset Adelitas is sitting on and not using

Findings to keep out of the *client* doc (they belong in the internal audit):
- The "Adeli Tasco" schema typo (embarrassing to surface; fix it silently)
- The punycode canonical leak on La Doña (same — technical, not narrative)
- The brand-collision risk with La Adelita Glendale (defensive framing only)
