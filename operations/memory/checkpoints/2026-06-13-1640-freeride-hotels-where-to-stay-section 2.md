---
date: 2026-06-13
time: 16:40
project: websites / freeride-tarifa
status: in-progress
next-session: Built a "Where to stay in Tarifa" hotels section on tarifa.html (4 advertised properties as venue-pattern cards). KEY NEXT ASK FROM ANNABEL: Hotels should be its OWN TOP-LEVEL TAB/page (like Lessons, Rent), not a section inside the Tarifa page. Next session: promote the #stay block into a standalone hotels page + add the nav tab; consider also including Free Ride's Apartments and Beach Houses categories (the 2 generic ones skipped this pass). Other still-open: Shopping section (deferred since 06-11), map OSM-vs-Google decision, Oleg/Leah unconfirmed homepage names, photo clearance before any live launch. Preview: launch.json name "freeride-static" (port 8791, auto-bumps to 8792); cache-bust tarifa.html with ?v=.
---

# Session: Freeride Tarifa "Where to stay" hotels section

## What we worked on

Annabel opened the Freeride project to continue under the new 3-layer website
doc system (global design.md + per-project design.md + content.md). Picked up the
deferred "Hotels" ask from the 06-11 checkpoint and built it.

## What shipped (tarifa.html)

- New `#stay` section "Where to stay in Tarifa" (eyebrow "Kite & sleep"), placed
  after the eat/drink/party guide and before the CTA. Reuses the exact `.venue`
  card pattern (photo + Google rating chip + vibe chip + one-line desc), 4 cards
  in the default 4-col grid (2-col tablet, 1-col mobile). Verified: 4 cards, all
  images load, 0 console errors.
- Four properties Free Ride advertises (from /vacation-rentals-in-tarifa/):
  - Hurricane Hotel — ★4.5, Beachfront — /beach-hotel-tarifa/
  - Hotel La Residencia (La Residencia Puerto Hotel & Spa) — ★4.7, Spa hotel — /spa-hotel-in-tarifa/
  - Hostal Africa — ★4.5, Old town — /kite-hostel-tarifa/
  - Surfers Residence — ★4.8, Coliving — /tarifa-kite-house/
- Images: single hero photos pulled from Free Ride's own CDN (their marketing
  images), each showing the property's best pool/rooftop with the sea. In
  assets/web/venues/ as hotel-hurricane.jpg, hotel-residencia.jpg,
  hostal-africa.jpg, surfers-residence.jpg.
- Updated content.md ("Where to stay" section + source log) and design.md
  (dated iteration-log entry).

## Decisions (this session)

- **Cards link to Free Ride's own property pages, not Google reviews** ("See the
  place ↗"), to keep bookings in Free Ride's funnel; Google star stays as the
  trust badge. FLAGGED as easy to flip to Google-review links if Annabel wants
  strict consistency with the eat/drink cards. (She has not chosen yet.)
- **Review counts deliberately omitted.** Honest fallback (rating only + "See the
  place"), same as Silos 19 / Morena on this page.
- Used single gallery photos, not the og:image (which were multi-photo collages).

## KEY NEXT — Annabel's direction

- **Hotels should be its own TAB**, not a section on the Tarifa page. Next session:
  promote `#stay` into a standalone top-level page (matches design.md's
  Santic-style "top-level pages for real user choices" + Page Architecture). Add
  the nav tab across pages (Freeride / Lessons / Rent / Tarifa / + Stay). Decide
  whether to also surface Free Ride's Apartments (/tarifa-holiday-rentals/) and
  House & Bungalow (/tarifa-holiday-beach-houses/) categories, which were left out
  this pass because they are categories, not single rated properties.

## Gotchas (so we don't rediscover them)

- **Firecrawl can't read Google Maps review COUNTS reliably** — JSON extraction
  returned echoed/default garbage ("20" for the famous Hurricane, "1234" = my
  prompt's example, "0"). RATINGS were fine (place-verified, stable across two
  scrapes). So: trust firecrawl Maps for the star rating, never the count.
- **preview_resize corrupts the screenshot surface** — after a resize,
  preview_eval reports the right innerWidth but preview_screenshot returns blank
  white frames. Fix: stop + start the preview server (fresh native viewport),
  verify layout via DOM/preview_eval. (Proposed a global CLAUDE.md note for this;
  Annabel declined — leaving it here instead.)

## Still open (carried)

- Shopping section (deferred 06-11; needs better shop photos + fuller list).
- Map: shipped keyless OpenStreetMap; Annabel may still want the exact Google
  look (needs API key or static image).
- Homepage "Oleg" (instructor) / "Leah" (rider) still [unconfirmed] — confirm real
  or replace (no-invented-people rule).
- Before live client launch: photo clearance; verify Google review counts if
  counts are wanted on hotel cards.
