# Scrape Data — Culantro Peruvian Eatery

**Scraped:** 2026-04-21
**Mode:** Full audit run (not redesign-only) — homepage + 3 references × 2 pages + 5 facts sources
**Total Firecrawl calls:** 12

## Prospect scrape

- **URL:** https://www.culantroperu.com/
- **Homepage markdown:** 1,444 chars (very thin — essentially a photo gallery site)
- **Homepage screenshot:** `scrape/screenshots/homepage-desktop-full.png` (744KB) + mobile (255KB)
- **Branding:** extracted — see `branding.json`
- **Sibling pages:** not scraped. Homepage is the entire site surface — everything else links out (Square for Ferndale menu, PDF for Ann Arbor menu, Instagram for photos, Square storefronts per location). No `/about`, `/menu`, `/reservations` pages exist.

## What's on the current homepage

1. Flame-lit rotisserie chicken hero image (pollo a la brasa)
2. Ornate yellow/orange "Culantro Peruvian Eatery" logo centered
3. Two black buttons: "Ferndale" | "Ann Arbor" — both linked to per-location external flows
4. Photo gallery of build-out, murals, staff, storefronts (Ann Arbor before/after, signage, door art, manager portrait, Facebook placard, hand-painted walls, rotisserie oven)
5. Instagram CTA ("Share your photos of Culantro with the world")
6. Tiny footer with IG + FB icons

## What the current homepage is missing

- Actual menu content (one PDF link + one external Square link, per location — both mentioned but never previewed)
- Hours (present nowhere on the homepage)
- Addresses (present nowhere — users must click through to external Square/menu to find)
- Phone numbers (not listed anywhere in scraped site)
- Reservations CTA (Ferndale takes reservations per Yelp, but homepage doesn't surface it)
- Any founder/owner/story copy (only visual — build-out gallery tells the story implicitly)
- Structured data (no JSON-LD, no OG tags beyond a stale logo.jpg)
- Reviews / social proof (2,895 FB likes + 303 Yelp reviews Ferndale — invisible on site)
- Signature dish names (pollo a la brasa is the visual hero but never named)
- Mobile-considered layout (mobile screenshot shows the desktop carousel compressed poorly)

## References scraped

See `reference/reference-summary.md` for design takeaways per ref.

| Brand | Pages | Notes |
|---|---|---|
| Cutler & Co | homepage (2874 chars), menu (2590 chars) | Editorial gold standard. Homepage screenshot failed (no URL returned by Firecrawl) — menu screenshot captured. |
| Mission Ceviche | homepage (7830 chars), locations (5343 chars) | Two-location picker pattern — exact IA Culantro needs. |
| Gjelina | homepage (7327 chars), locations (117 chars stub) | Multi-location hub with warm cream background + red accent — bridges Cutler restraint to warm color. Locations page returned a stub. |

## Facts sources scraped

| Source | Chars | Status |
|---|---|---|
| Yelp Ferndale | 43,769 | ✓ full — 4.2★, 303 reviews, hours, menu prices, owner profile, review bodies |
| Yelp Ann Arbor | 45,033 | ✓ full — 3.7★, 65 reviews, hours, address (223 N Main St Kerrytown), reviews |
| Google Ferndale | 30,991 | ✓ partial — SERP + TripAdvisor + Facebook snippets; no full knowledge panel data |
| Google Ann Arbor | 29,544 | ✓ partial |
| OpenTable Ferndale | 12,985 | ✓ content returned (not bot-walled for once) |

Consolidated into `facts/verified-facts.md`.

## Completion gate

- [x] `branding.json` exists, non-empty colors + fonts
- [x] `facts/verified-facts.md` exists with Identity + Hours + 6 review quotes (each cited)
- [x] `facts/` has 5 raw source files
- [x] `reference/` has 3 subdirs (cutler-and-co, mission-ceviche, gjelina)
- [x] `reference/reference-summary.md` exists with per-ref blocks + synthesis
- [x] `scrape/screenshots/` has homepage desktop-full + mobile
- [x] This file (`scrape-data.md`) written
- [x] Leakage audit — all prospect assets under `prospects/culantro/`

**Scrape complete. Ready for `/audit-redesign`.**
