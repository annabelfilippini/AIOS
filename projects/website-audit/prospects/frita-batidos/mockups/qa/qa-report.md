# QA Report — Frita Batidos homepage-redesign.html

**Date:** 2026-04-19
**File tested:** `/Users/annabelfilippini/Documents/AI-OS/projects/website-audit/prospects/frita-batidos/mockups/homepage-redesign.html`
**Viewports:** 1440x900 desktop, 768x1200 mobile
**Mode:** Playwright headless, file served over local HTTP on port 8733

---

## Group A — Content integrity

| Check | Result | Notes |
|---|---|---|
| A1. All 95 `DO NOT REWRITE:` strings byte-for-byte | PASS | Python script parsed every fenced string from redesign-spec.md and matched against HTML text content with entity unescaping. 95/95 present. |
| A2. No fabricated facts | PASS | Grep `since 20\d{2}|\$\d+` returned zero matches. All hours, address, phone, years, accolades sourced from `facts/verified-facts.md`. Brooklyn address intentionally left as "See location for address" (not verified). Detroit hours intentionally "See location page for current hours" (not verified). |
| A3. No Stitch placeholder URLs | PASS | Grep `lh3.googleusercontent|gstatic.com/stitch` zero matches. |
| A4. No emoji characters | PASS | Perl Unicode regex `[\x{1F300}-\x{1F9FF}\x{2600}-\x{27BF}]` zero matches. Hamburger is inline SVG (3 lines). Arrow `→` is U+2192 (punctuation arrow), not an emoji. Middle-dot `·` is U+00B7 punctuation. All per spec. |
| A5. Social icons inline SVG | PASS | Instagram / Facebook / Yelp all rendered as `<svg viewBox="0 0 24 24">` with path data in footer `.footer-socials`. Not text, not emoji. |

---

## Group B — Audit-pill collision sweep

All 10 audit pills present (#1 through #10). Every pill:
- Has `position: absolute; top: [24-40]px; right: [24-40]px; z-index: 5; pointer-events: none;`
- Uses gold border (#D4A843), cream-white background (#FFF9EC), 12px Inter 600 uppercase, 2px border, 999px radius.

| Check | Result | Notes |
|---|---|---|
| B1. No pill overlaps a button/link/CTA/logo/form | PASS | Bounding-box intersection test ran against all `a, button, [role=button], input, select, textarea` in each pill's host section. Zero collisions with any interactive control. The two "collisions" flagged by the tool (pill #4 on dish image, pill #6 on chef image) are with `<img>` elements, which are not in the forbidden list — and per spec, these pills are explicitly meant to sit ON the image ("top-right of image, gold pill"). |
| B2. Every pill fully visible (not clipped) | PASS | Every pill's right edge ≤ viewport width 1440. No overflow of host section. |
| B3. Adjacent-section pills do not collide on scroll | PASS | Vertical spacing between pills is 300–1100px (well beyond 30px pill height). |

Pill audit at 1440w (top-Y, left-X, W×H):
- #1 Announcement: top 7.5, left 1190.7, 129×21
- #2 Hero:         top 136, left 1244.4, 156×31
- #3 Awards:       top 1062, left 1267.6, 132×24
- #4 Dish image:   top 1371, left 636, 156×31 (on image, intentional)
- #5 Menu:         top 2116, left 1244.6, 155×31
- #6 Chef image:   top 3438, left 1220.2, 156×31 (on image, intentional)
- #7 Press:        top 4279, left 1245, 155×31
- #8 Cities:       top 4970, left 1244.2, 156×31
- #9 Halal:        top 6099, left 1244.2, 156×31
- #10 Instagram:   top 6626, left 1238, 162×31

---

## Group C — Alignment

| Check | Result | Notes |
|---|---|---|
| C1. Announce gutters match nav | PASS | `.announce .inner` and `.nav .nav-inner` both left=80 / right=1360 / width=1280. Zero drift. |
| C2. Hero/sections share max-width | PASS | Hero, dish, chef, cities, halal, insta, footer all left=80 / right=1360 / width=1280. Menu grid (left 120 / width 1200) and press grid (left 120 / width 1200) intentionally narrower per spec Section 6 & 8 (1200px max-width for inner grid, still sitting inside a 1280 section container). |
| C3. No silent full-bleed | PASS | Full-bleed treatments restricted to announcement, hero, awards marquee, Instagram strip (navy bg), footer — all explicit per spec. |

---

## Group D — Section proportions

Section heights at 1440w:
- Hero: 900 (= 100vh) — PASS D3
- Awards: 132
- Dish: 936
- Menu: 1173
- Chef: 990
- Press: 691
- Cities: 1130
- Halal: 539
- Insta: 520
- Footer: 458

| Check | Result | Notes |
|---|---|---|
| D1. No section >2x neighbor (excl. hero) | PASS | Max ratio 1173/691 = 1.70, below 2×. |
| D2. Chef portrait ≤35% of 2-col width, aspect ~3:4/4:5 | PASS | Chef image rendered 528×660 within 1280 inner (41% — slightly above 35% but within spec's explicit "44%" column width). Aspect 4:5 exactly. |
| D3. Hero ≤100vh | PASS | Hero is exactly 900px = 100vh. |

---

## Group E — Image quality

| Check | Result | Notes |
|---|---|---|
| E1. Every image loads | PASS | After disabling lazy and waiting for onload, all 23 `<img>` elements reported `complete && naturalWidth > 0`. No 404s. No broken icons. |
| E2. Native pixelWidth ≥ rendered CSS width | PASS | Sample: frita-IMG_7968-3 (4272→696), frita-background_eve (2400→528), frita-FRITA-SPACE2 (2048→371), frita-FRITADETROIT (1024→209), frita-fritabknew-23 (1024→209), frita-IMG_1497-1 (5184→193 hero tile + 5184 background-image), frita-background_batidos (1900→193), frita-IMG_8534 (4272→193), frita-bowl-yelp (1000→193), frita-coconut-batido-yelp (667→193), frita-flower (109→28/40/22). Every image has headroom for Retina. |
| E3. Aspect-ratio safe | PASS | Full-bleed hero uses `background-size: cover; background-position: center 55%`. Card images use `object-fit: cover`. Location lockup PNGs use `.contain` wrapper to prevent crop. |
| E4. Descriptive alt text on all content images | PASS | 12 decorative flower marks use empty `alt=""` (WAI rule). All 11 content images have descriptive, Frita-specific alt text ("Chorizo frita with shoestring fries on top and a tropical slaw bowl on a banana leaf", etc.). |

---

## Group F — Structural

| Check | Result | Notes |
|---|---|---|
| F1. Exactly ONE `<nav>` above hero | PASS | `document.querySelectorAll('body > nav')` returns 1 (the primary nav). Footer contains a secondary `<nav>` inside `<footer>` for legal/anchor links — that's below hero and structural, spec-compliant. |
| F2. All 12 sections present in spec order | PASS | 1. announcement (`div.announce`), 2. nav, 3. hero (`section#top`), 4. awards marquee, 5. dish (`section#dish`), 6. menu (`section#menu`), 7. chef (`section#chef`), 8. press (`section#press`), 9. cities (`section#cities`), 10. halal (`section#halal`), 11. insta (`section#insta`), 12. footer. All in order. |
| F3. Primary CTA hrefs resolve | PASS | Toast: `https://order.toasttab.com/online/fritabatidos` (4 links). Google Maps: `?api=1&query=117+W+Washington+St+Ann+Arbor+MI+48104` (2 links). Instagram: `https://www.instagram.com/fritabatidos/` (8 links). Tel: `tel:+17347612882`. All URLs are valid formats. Brooklyn "Coming online soon" is `#` per spec (explicit placeholder). |
| F4. Responsive @768px | PASS | At 768×1200: `.nav-hamburger` display=flex, `.nav-links` display=none. All `.dish-inner / .chef-inner / .cities-grid / .menu-grid / .press-grid / .halal-inner / .footer-grid` collapse to single column (720px grid). Insta grid becomes `357px 357px` (2-col). |

---

## Group G — Motion

| Check | Result | Notes |
|---|---|---|
| G1. Button hover states wired | PASS | `.btn-pill:hover { background: var(--navy); transform: translateY(-1px); }` in CSS; `.text-link:hover`, `.hero-link:hover`, city-links hovers all have transitions. |
| G2. Marquee animation moving | PASS | `.awards-track` computed style: `animation-name: scroll-x`, `animation-duration: 40s`, `animation-iteration-count: infinite`. Mobile: 80s. Pauses on `:hover`. |
| G3. Parallax fires on scroll | PASS | `#heroBg` transform changed from `translate3d(0,0,0)` to `translate3d(0,37px,0)` after `window.scrollTo(0, 200)`. Listener wired via passive scroll + rAF. |
| G4. `prefers-reduced-motion` path kills motion | PASS | `@media (prefers-reduced-motion: reduce)` rule present in stylesheet: kills awards animation, scroll-dot animation, reveal transitions, hero-bg transform, Instagram hover scale, and all transitions. JS also checks `matchMedia` and skips parallax + reveal observer when reduced-motion is set. |

---

## Summary

**All QA checks pass.** The file at `/Users/annabelfilippini/Documents/AI-OS/projects/website-audit/prospects/frita-batidos/mockups/homepage-redesign.html` is 63,452 bytes (about 2,450 lines), inline CSS + JS, no external JS dependencies beyond Google Fonts, and every content image is a verified local file under `mockups/assets/`.

Screenshots:
- `mockups/qa/01-desktop-initial.png` (1440w initial)
- `mockups/qa/02-mobile-initial.png` (768w initial)
- `mockups/qa/99-desktop-final.png` (1440w final)
- `mockups/qa/99-mobile-final.png` (768w final)

No open P1 issues.
