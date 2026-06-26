---
date: 2026-06-23
time: 09:55
project: websites / addict-kiteschool-tarifa
status: DONE — brand-true homepage built from Addict's real identity (NOT the FyM lane), verified at desktop + mobile, console clean, opened in browser for Annabel's review. content.md + design.md filled from real sources. Not yet approved or deployed.
next-session: Get Annabel's reaction. If approved, build inner pages (Courses, Stay, Tarifa, Team, Contact) in the same system, then resolve the confirm-before-launch list (exact studio address, recheck 2026 prices + TripAdvisor count, photo permission, Eleveight sponsor status).
---

# Session: Addict Kite School — brand-true homepage

## Where the prior session died

The earlier session (transcript 93a7c80c) gathered all assets (brand logo/
favicon/banner, 6 curated site photos, full IG pull) and verified facts, then
**crashed on an API connection error at the exact moment before writing the docs
and building**. content.md + design.md were still blank templates; no HTML.

## Annabel's instruction this session

Build it, but do NOT default to the FreeYourMind pattern. Understand Addict's
real business and vibe first, then build from THAT. (This is the brand-true
method from the FyM pivot, applied again.)

## What I studied (real sources, before building)

- Scraped `addictkiteschool.com/en/` home + `/our-courses/prices/` + `/about/team/`.
- Read the logo + all 6 curated site photos.
- Read FyM's design.md to deliberately differentiate.

Addict's real identity: kitesurf school on **Los Lances Beach, Tarifa**, 10+
years, **Romain** (owner/instructor) + **Marine** (booking/co-owner) + 7
instructors, FR/EN/ES. **IKO/FAV** certified, **OLK** recommended, **366
TripAdvisor reviews / 99% 5-star**. Three lesson formats (Group 80€ /
Semi-private 120€ / Private 132€, pre-book -10%), rental, accommodation
(2 studios, Kite House "Akiteness", apartments, wellness), kids from ~8.
Brand colors from the logo (orange kitesurfer in a gray head, blue dashed ring):
**orange + ocean blue + graphite**. Voice: playful, friendly, "become ADDICT",
"a true kite family".

## The lane decision (≠ FreeYourMind)

FyM = warm espresso/sand + sunset coral + Fraunces serif, romantic/holistic.
**Addict = bright outdoor-action editorial**: cool, sporty, graphic. Bold
grotesque (Archivo display + Hanken Grotesk body + Space Mono figures), orange =
action, blue = ocean/structure, graphite ink, cool off-white (NOT cream). Bright
turquoise photography leads. Documented the separation in design.md so it can't
drift back into FyM.

## What got built

`projects/websites/addict-kiteschool-tarifa/index.html` — single homepage, inline
CSS, local assets. Flow: hero (full-bleed rider, "Kitesurfing in TARIFA", proof
strip 366/99%/OLK) → kite family (10+/7/3 stats + Romain pull-quote) → Courses
(3-card decision, middle highlighted, mono prices, includes-strip) → Why Tarifa
(blue ocean overlay, 3 facts) → Reviews (score strip + 3 real TripAdvisor quotes)
→ Stay (4 items) → Pre-book CTA over the orange-kite photo → dark footer.

content.md + design.md fully filled from the scraped facts (with [verified] /
[recheck] / [unconfirmed] tags and a confirm-before-launch list).

## Craft notes (ship gate held)

- Killed all sentence/tagline headings + trailing periods (hero, who, spot,
  book). "Become addict" energy lives in the hero lede / body, never in an h1/h2.
- Fixed two responsive bugs found in browser: mobile menu had no base
  `display:none` (showed as stray text on desktop); footer 3-col grid + hero h1
  overflowed on mobile. Both fixed, re-verified, no horizontal overflow at 375px.

## Preview

Local: `addict-tarifa` server, port **8857** (added to .claude/launch.json).
`open http://localhost:8857/index.html`.
