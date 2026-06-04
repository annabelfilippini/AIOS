# Adelitas Cocina y Cantina — Internal Audit Reference
**Site:** adelitasco.com + ladonamezcaleria.com | **Platform:** Showit (both) | **Date:** 2026-04-14
**Inputs:** scrape-data.md (7 core + 2 SEO samples + La Doña + 3 references), seo-research.md (10 keywords)

Core insight: **Good restaurant, broken plumbing.** Adelitas is invisible for the one search that matters (`Mexican restaurant Denver`, DMA 56), while its entire SEO surface is a 17-page doorway cluster that violates Google's doorway policy. The single strongest brand asset — Chef Silvia Andaya's Michoacán "La Adelita" heritage, shared across three properties (Adelitas, La Doña, Ni Tuyo) — is buried inside an SEO spam URL and invisible on the homepage. Every inbound backlink lands on a placeholder `<title>Location Picker</title>` page with no content.

Risk framing: recommendations 1–3 are defensive (prevent Google manual action, stop SEO equity leaks); recommendation 4 is the only offensive play but it compounds — it unifies three restaurants into one brand universe.

---

## Technical Health (D)

### Working
- HTTPS active on both properties
- Showit renders reliably; GTM + Mailchimp installed on Adelitas
- La Doña has working Instagram wall and contact form

### Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| `adelitasco.com/` root = `<title>Location Picker</title>`. No meta description, no h1, no JSON-LD, no OpenGraph. Every backlink to the domain lands on a content-free page. | Critical | Medium |
| `/broadway` and `/edgewater` are byte-for-byte duplicate templates (37,837 vs 37,838 chars — difference is street address). Both self-canonical → Google picks one and suppresses the other; neither accumulates link equity. | High | Medium |
| JSON-LD `name` = `"Adeli Tasco"` (space injected) across every page carrying schema. Google uses this for knowledge panels. Silent brand-identity failure. | High | Low |
| `/catering` raw HTML leaks `<h1>Success!</h1>` (form-success state rendering in static page) | Medium | Low |
| `/qr-code-menu` (the page linked from the "Menus" nav button) has 0 images, 0 h1s, 0 JSON-LD. Menu is opaque to Google and screen readers. | High | Medium |
| No robots.txt on either domain | Medium | Low |
| No reservation integration in raw HTML on either site (no Resy/Tock/OpenTable/SevenRooms embed) — despite OpenTable listing existing at `opentable.com/r/adelitas-cocina-y-cantina-denver` | High | Low |
| Adelitas mobile homepage screenshot is 2KB — likely blank or late-painting. Confirm via DevTools device mode. | High | Medium |
| La Doña canonical = `xn--ladoamezcaleria-1qb.com` (punycode tilde-domain). Users type plain-ASCII; all backlink equity flows to a URL nobody can type from memory. | Critical | Low |
| La Doña JSON-LD `url` = `xn--laoamezcaleria-1qb.com` — **different** broken punycode, missing an "n". Malformed domain; schema parser treats the site as unreachable. | Critical | Low |
| No sitemap.xml for La Doña (404) | Medium | Low |
| La Doña is a single-page Showit site — "menu" and "reservations" are on-page anchors, not crawlable pages. No menu as HTML, no booking flow. | High | High |
| Shared designer (bohemefox.com) on both properties — single vendor relationship to coordinate fixes through | Info | — |

---

## SEO (F)

### Working
- Adelitas dominates its own branded SERP (Yelp, OpenTable, /broadway, doorway pages all owned)
- Adelitas sitemap exists and lists 24 URLs
- LocalBusiness JSON-LD present on location/doorway pages (even if `name` is wrong)

### Keyword Visibility

| Keyword | Denver DMA | Position | Root Cause |
|---------|-----------|----------|------------|
| Adelitas Denver | — | Dominant | — |
| La Doña mezcaleria Denver | — | Punycode URL ranks | Canonical leak |
| Chef Silvia Andaya | — | Scattered across doorway pages | No editorial hub |
| **Mexican restaurant Denver** | **56** | **Invisible on page 1** | Root URL is placeholder; Broadway/Edgewater duplicate-compete |
| Michoacán food Denver | 0 | Mentioned on Uncover Colorado + doorway page | Zero search volume — brand claim, not channel |
| Mezcal bar Denver | 1 | /mezcal-in-denver doorway ~#6; La Doña punycode ranks | La Doña has no crawlable content |
| Family-owned Mexican restaurant Denver | — | Doorway ranks ~#4 | Missing from editorial "10 Family-Owned" roundup |
| Best Mexican food Denver | 14 | Doorway ranks ~#7 | No owned content; aggregators dominate |
| Mexican restaurant Denver reservations | — | **Invisible** | Booking integration exists but isn't linked |
| Tequila dinner Denver | 29 (proxy) | Two doorways rank #2 and #3 | Doorway dependency |

**Root cause:** All current SEO presence depends on a 17-page doorway cluster that Google's policy explicitly flags. Primary home (`adelitasco.com/`) has zero semantic content. OpenTable listing exists, not linked. Chef Silvia Andaya has zero search authority (0 autocomplete suggestions, 1 indexed editorial mention).

### Google Trends (12-mo, US)

| Term | Mean | Peak | Signal |
|---|---|---|---|
| Mexican restaurant Denver | 71.8 | 2026-01-25 | **Post-holiday dining window (Jan–Feb)** is peak discovery intent |
| Tequila Denver | 40.2 | 2025-05-18 | Cinco de Mayo bump — May ranking pays off |
| Best Mexican food Denver | 6.9 | 2025-07-06 | Summer-visitor window (July) |
| Mezcal bar Denver | 0.0 | 2026-04-05 | Rising but negligible — positioning, not volume |
| Michoacán food Denver | 0.0 | — | Zero DMA volume |

**Implication:** three calendar windows that matter — January (discovery), May (Cinco de Mayo tequila), July (tourists). Any SEO work must land before those windows to convert the traffic.

### Autocomplete Insights
- `adelitas denver` — 10 suggestions (max). 4th most common: `adelitas denver reservations`. Real unmet intent.
- `chef silvia andaya` — **0 suggestions**. Zero branded recognition in Google's index.
- `la doña mezcaleria denver` — 1 suggestion. La Doña's invisibility reaches even branded search.
- `silvia andaya` alone — no autocomplete coverage. Editorial hub absent.

### The 17 Doorway Pages

All 17 follow the same pattern: 5-6 h1 tags on one page, 15 images (12 with empty alt), 25K chars of keyword-stuffed narrative, identical WebSite/LocalBusiness/Organization JSON-LD verbatim across every URL. Google's doorway-page policy describes this pattern exactly.

| Finding | Severity | Effort |
|---------|----------|--------|
| 17 doorway URLs in sitemap — textbook policy violation | Critical | High |
| Cannot delete: several are actively ranking on `/best-mexican-food-in-denver-colorado`, `/tequila-restaurant-in-denver`, `/mezcal-in-denver`, `/best-mexican-restaurant-in-denver` | — | — |
| Must consolidate with 301 redirect map, not blanket delete | — | — |

**Consolidation target (recommended):** 4 legitimate hubs, 13 doorways 301'd in:

| Consolidated hub | Absorbs | Rationale |
|---|---|---|
| `/menu` (new, real HTML — replaces `/qr-code-menu` stub) | — (new canonical) | Menu is an owned nav item; must be crawlable |
| `/our-story` | `/tequilas-family-mexican-restaurant`, `/family-owned-mexican-denver` (if present) | Lift Silvia + Michoacán narrative to a proper editorial page |
| `/tequilas-and-mezcal` | `/tequila-restaurant-in-denver`, `/mezcal-in-denver`, `/top-cocktail-bars-in-denver`, `/best-margaritas-in-denver` | Bar-program hub with Adelitas tequila + La Doña mezcal cross-linked |
| `/brunch` | `/best-brunch-in-denver-colorado`, `/best-mexican-breakfast-denver`, `/best-breakfast-burritos-denver`, `/denver-breakfast-burrito` | Separate brunch menu is real product |
| `/` (homepage, rebuilt) | `/best-mexican-food-in-denver-colorado`, `/best-mexican-restaurant-in-denver`, `/best-authentic-tacos-in-denver`, `/best-food-and-drinks-in-denver`, `/best-happy-hour-denver`, `/brunch-restaurants-denver`, `/mexican-food-delivery-denver`, `/mexican-happy-hour-denver`, `/mexican-tacos-restaurant-denver` | Generic "best Denver X" terms consolidate onto a proper homepage |

### Other SEO Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| Adelitas absent from every indexed editorial "best of Denver" roundup (Uncover Colorado, DoorDash, Cozymeal, Classpop, Every After in the Woods). Zero earned editorial backlinks. | High | High |
| Ni Tuyo (third Andaya property) outranks Adelitas on "Mexican restaurant Denver". The three properties **do not cross-link** — sharing no domain authority. | High | Low |
| Name-collision risk with La Adelita (Glendale, CO Mexican restaurant claiming same Michoacán heritage). Meta titles must always include "Cocina y Cantina" to disambiguate. | Medium | Low |
| Subcategory queries ("mezcal listening bar Denver", "mezcal audio bar Denver") going to Malinche / Mezcaleria Alma. La Doña has real depth but no crawlable content. | Medium | High |

---

## Accessibility (C)

### Working
- Heading hierarchy on the `/tequilas-family-mexican-restaurant` page is dense but structured
- Broadway / Edgewater pages have proper h1, meta description, LocalBusiness schema
- La Doña uses alt text on several hero images

### Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| 17 doorway pages each have 15 images with 12 empty alts (= 204 missing alts on doorway cluster alone) | High | Medium |
| La Doña page has 64 images, 14 with empty alt — mostly gallery textures, but several are food/product shots | Medium | Low |
| Each doorway page has 5-6 h1 tags — violates heading hierarchy, confuses screen readers | Medium | Medium |
| `/qr-code-menu` has no h1, no alt text, no structured content — menu inaccessible to screen readers | High | Medium |
| Adelitas mobile homepage may not render (2KB screenshot) — if confirmed, blocks every mobile user from entering the site | Critical | Medium |
| No lang attribute verified on either domain's `<html>` tag | Low | Low |

---

## Content & UX (C)

### Working
- Broadway location photography is strong (dim, evening cantina atmosphere)
- Edgewater location photography differentiates (brighter, modern interior)
- "La Adelita" heritage narrative (woman-warrior / soldadera / Michoacán lineage) is fully written — just buried
- Brand voice on `/tequilas-family-mexican-restaurant`: "festive", "authentic", "family recipes from Michoacán" — consistent and grounded
- La Doña brand voice is more intimate and spirits-forward: "mezcal-centric cocktail bar in rustic digs behind Adelitas" — legitimate hidden-gem positioning
- Event page (`/event`) documents real programming: Sip & Savor tequila dinner with Chef Silvia + Adolfo Aguilar

### Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| Homepage is a location-picker placeholder — no brand narrative, no Chef Silvia presence, no reservation CTA, no menu preview, no photography of the actual food | Critical | High |
| Chef Silvia Andaya doesn't appear on the homepage, the "menus" page, or as her own editorial page. Personal brand is the highest-leverage untapped asset across all three properties. | High | Medium |
| "La Adelita" soldadera heritage story lives only on `/tequilas-family-mexican-restaurant` (a doorway-named URL) — the strongest differentiator is hidden in SEO spam | High | Medium |
| `/qr-code-menu` (menu entry point from nav) is an HTML-empty stub. No menu visible on-page. | High | Medium |
| Broadway and Edgewater pages identical — no differentiated photography, menu highlights, review pulls | Medium | Medium |
| Catering page leaks "Success!" form state into static render | Low | Low |
| OpenTable listing exists (`opentable.com/r/adelitas-cocina-y-cantina-denver`) but is invisible from the site. Autocomplete shows `adelitas denver reservations` is the 4th most-typed branded variant — unmet intent. | High | Low |
| No "Reservations" nav link on either property | High | Low |
| Ni Tuyo exists as a third Andaya property — not cross-linked from Adelitas or La Doña | High | Low |
| No press / editorial mention footer on any page. Shoutout Colorado interview exists but isn't referenced. | Medium | Low |
| No blog / journal content. Nothing to pitch to editorial. Nothing for Google to index as fresh. | Medium | High |

### Page-by-Page Notes

**Homepage (`/`):** `<title>Location Picker</title>`. 1 hero image, 2 location cards (Broadway / Edgewater). No h1. No h2. No menu preview. No Chef Silvia. No reservation CTA. No La Adelita narrative. No press. No footer cross-link to La Doña or Ni Tuyo. This page does not identify the business to a visitor or to Google.

**Broadway (`/broadway`) & Edgewater (`/edgewater`):** Identical templates. "Authentic Mexican Restaurant Denver Colorado | Adelitas" title on both. 33 images each, 6 scripts, same WebSite/LocalBusiness/Organization JSON-LD. The only difference is the physical address.

**/tequilas-family-mexican-restaurant:** De-facto About page. 6 h1s. Keyword-stuffed narrative wrapper, but the embedded content is genuinely good — Silvia's journey, Michoacán heritage, "La Adelita" heroine framing. This is the content the homepage should be using.

**/qr-code-menu:** Linked from the "Menus" header button. No images, no h1, no JSON-LD. Presumably a Showit gallery behind click interactions; doesn't render as crawlable HTML content.

**/event:** Sip & Savor tequila dinner promo (Silvia + Adolfo Aguilar). Real programming — this should be a recurring events hub, not a one-off page.

**/catering:** Thin. `<h1>Success!</h1>` leaking from form-success state rendering on page load.

**La Doña (single page):** Chef-led intro references Silvia. Address: 13 E Louisiana Ave, Denver ("behind Adelitas"). Hours, contact, mezcal-forward copy, IG wall, 4 testimonials. One link out to Adelitas. Canonical and JSON-LD URLs are both broken punycode. No menu as HTML, no booking flow.

---

## AI Opportunities

| Opportunity | Impact | Effort | Connection to Findings |
|-------------|--------|--------|------------------------|
| AI-drafted editorial pitches to Westword / 5280 / Eater Denver — angle: "one chef, three Denver restaurants, one Michoacán lineage" | High | Medium | Addresses zero-earned-editorial finding; Silvia's story un-pitched |
| Chef Silvia editorial page: AI-drafted bio, press-quote curation, cross-link copy to Adelitas/La Doña/Ni Tuyo | High | Low | Fixes personal-brand authority gap (0 autocomplete) |
| Reservation-intent content: `/reservations` page + meta + Reservation schema, AI-templated per location | High | Low | Captures `adelitas denver reservations` unmet intent (4th branded autocomplete) |
| Social proof curation: pull best Yelp/Google/press quotes, categorize by experience (Taco Tuesday, private events, mezcal flights), publish as a curated reviews hub | Medium | Medium | Yelp mentions "raucous Taco Tuesdays" — no owned content surfaces this |
| Menu as crawlable HTML: AI-transcribe current Showit menu images into structured HTML + Menu schema | High | Medium | `/qr-code-menu` is opaque to Google; menu schema enables rich results |
| Event-calendar scaffolding: Sip & Savor is one real event — AI can maintain a recurring event hub with schema markup | Medium | Medium | `/event` is a one-off; recurring programming has SEO value |

**Notable:** The three-property Andaya brand universe (Adelitas, La Doña, Ni Tuyo) is a content moat no competitor can replicate. Cross-linking + unified chef hub + one editorial hit compounds across all three sites' domain authority.

---

## Priority Action List (Deduplicated)

### This Week (< 1 hour each — engineering)
1. Switch La Doña canonical from `xn--ladoamezcaleria-1qb.com` to plain-ASCII `ladonamezcaleria.com`; 301 punycode → ASCII
2. Fix La Doña JSON-LD `url` field (currently malformed `xn--laoamezcaleria-1qb.com`, missing "n")
3. Fix JSON-LD `name` across every Adelitas page carrying schema: `"Adeli Tasco"` → `"Adelitas Cocina y Cantina"`
4. Add OpenTable link to Adelitas header nav ("Reservations" button → `opentable.com/r/adelitas-cocina-y-cantina-denver`)
5. Add robots.txt to both domains
6. Remove leaked `<h1>Success!</h1>` from `/catering` static render (Showit template fix)
7. Add Ni Tuyo + La Doña cross-links to Adelitas footer; Adelitas + Ni Tuyo to La Doña footer

### This Month (design + content work)
8. Rebuild `adelitasco.com/` as a real homepage — hero with Silvia, La Adelita narrative teaser, menu preview, reservations CTA, location nav affordance (Broadway / Edgewater), cross-links to La Doña + Ni Tuyo, press footer
9. Move location picker into header nav, not the root page body
10. Differentiate Broadway vs Edgewater pages — separate photography, menu highlights, reviews, neighborhood context
11. Build `/menu` as real HTML (structured sections, Menu schema), replace `/qr-code-menu` stub
12. Build `/our-story` — lift Silvia + Michoacán + La Adelita narrative from `/tequilas-family-mexican-restaurant` into a proper editorial page with Person schema
13. Build `/reservations` page — both locations, OpenTable CTAs, Reservation schema
14. Confirm Adelitas homepage mobile rendering (the 2KB screenshot needs manual DevTools verification — if blank, this is a P0 mobile-UX bug)

### This Quarter (SEO consolidation + press)
15. Execute 17-doorway → 4-hub 301 redirect map. Add new hubs *before* redirecting to preserve ranking continuity.
16. Build `/tequilas-and-mezcal` hub — bar program, ~200 tequilas, La Doña mezcal program cross-link
17. Build `/brunch` hub — separate brunch menu, breakfast program
18. Build `/chef` editorial page with Person schema (Silvia bio, press quotes, links to all three properties)
19. Build La Doña as a real multi-page site (at minimum: `/menu`, `/mezcal-program`, `/reservations`)
20. Editorial pitch campaign — Westword, 5280, Eater Denver, Uncover Colorado. Target: one major press hit before January 2027 dining-discovery window.
21. Event-program hub at `/events` (recurring: Sip & Savor, Taco Tuesday, happy hour, private dining)
22. Get Adelitas on "Best Mexican Restaurants in Denver" editorial roundups (currently absent from every one indexed)
23. Taco Tuesday page — autocomplete shows `adelitas denver taco tuesday` as real branded search; Yelp already references the product ("raucous Taco Tuesdays")

### Kept out of client doc (technical / defensive)
- "Adeli Tasco" schema typo — embarrassing to surface; fix silently
- Punycode canonical details on La Doña — technical, not narrative
- La Adelita (Glendale) brand-collision risk — defensive meta-title framing only, not a client-facing concern
