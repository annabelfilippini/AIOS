---
date: 2026-06-13
time: 21:46
project: websites / freeride-tarifa
status: in-progress
next-session: Promoted "Where to stay" from a section on tarifa.html into its own top-level page stay.html with a nav tab. Nav order is now Freeride / Lessons / Rent gear / Tarifa / Stay on all five pages (Annabel chose Tarifa then Stay). stay.html = split hero (oldtown.jpg) + the same 4 verified .venue cards (Hurricane, La Residencia, Hostal Africa, Surfers Residence) + an honest "more ways to stay" line linking Freeride's apartments + beach-houses category pages (no fabricated data) + stay CTA on grab.jpg. #stay removed from tarifa.html (now flows after-kite -> CTA). OPEN: (1) optionally build apartments + beach-houses into full cards (needs scraped photos + verified one-line descriptions; they are categories, not single rated properties). (2) Optional tarifa->stay teaser link. (3) Still carried: Shopping section, map OSM-vs-Google, Oleg/Leah unconfirmed names, photo clearance + verify hotel Google review counts before any live launch. Preview: launch name resolves to "freeride" on port 8792 (project launch.json says freeride-static/8791, auto-bumps). Server serves the freeride-tarifa folder as root (so URLs are /stay.html, NOT /projects/...). Cache-bust with ?v=.
---

# Session: Freeride "Stay" promoted to its own page + tab

## What we worked on

Annabel asked to read the most recent freeride checkpoint (the 16:40 "Where to
stay" hotels section) and act on its KEY NEXT: make Hotels/Stay its own top-level
tab rather than a section on the Tarifa page.

## What shipped

- **New `stay.html`** standalone top-level page (purpose-built CSS, not a clone of
  tarifa's full stylesheet):
  - Split hero (white text panel + image). Kicker "Kite & sleep", h1 "Where to
    stay" (STAY in green), copy, two CTAs: green "Plan your stay on WhatsApp" +
    dark "See lesson packages" (-> lessons.html, ties stay into the lesson+stay
    funnel).
  - Hero image `assets/web/oldtown.jpg` (the owned old-town street where the kite
    houses/hostels are). Chosen specifically so the hero is NOT one of the four
    card images (design.md: no reused imagery within a page).
  - Section "Beds a few minutes from the beach" with the same four verified
    `.venue` cards (photo + Google rating chip + vibe chip + one-liner + "See the
    place"): Hurricane Hotel 4.5 Beachfront, Hotel La Residencia 4.7 Spa hotel,
    Hostal Africa 4.5 Old town, Surfers Residence 4.8 Coliving. Each links to
    Freeride's own property page.
  - Honest "more ways to stay" line under the cards linking Freeride's apartments
    (/tarifa-holiday-rentals/) and beach houses & bungalows
    (/tarifa-holiday-beach-houses/) category pages, with NO fabricated ratings or
    photos.
  - Stay-specific dark CTA on `grab.jpg`: "Tell us your dates, we will sort the
    room."
- **Stay nav tab added to all five pages.** Final order (Annabel's call):
  Freeride / Lessons / Rent gear / Tarifa / **Stay**. Correct is-active per page.
- **Removed `#stay` from tarifa.html.** Moved, not duplicated. Tarifa now flows
  after-kite guide -> CTA. Verified `#stay` no longer present.
- **Docs updated:** design.md iteration log (new 2026-06-13 entry + final nav-order
  decision) and content.md ("Where to stay" now points to stay.html + the honest
  category-link note).

## Decisions (this session)

- Stay is a real top-level page/tab, matching the Santic-style "top-level pages for
  real user choices" rule and the "Learn, ride, stay, and belong" positioning.
- Nav order Tarifa then Stay (Stay last) — Annabel chose this over the initial
  "Stay before Tarifa" attempt.
- Apartments + beach houses surfaced as honest links only this pass (categories,
  not single rated properties); full cards deferred pending verified photos/copy.
- Fixed the broken "Every one minutes from the beach" guide-sub from the old
  section (new page uses a clean section title).

## Verified

- Page loads (200), title/h1 correct, all 7 images load, 0 console errors.
- Nav order + active state correct on all 5 pages (DOM-checked each).
- Hero + nav rendered (desktop screenshot); 4 cards + honest links rendered
  (tablet 2-col screenshot). Responsive 2-col at <=860, 1-col at <=520.
- tarifa.html has no `#stay`; sections flow top -> band -> spots -> after -> cta.

## Gotchas (carried + confirmed)

- **Preview server roots at the freeride-tarifa folder**, so the URL is
  `http://localhost:8792/stay.html` (NOT /projects/websites/freeride-tarifa/...).
  preview_list reports cwd as the AI-OS root, which is misleading — probe with a
  HEAD fetch if unsure.
- **preview_resize corrupts the scroll/screenshot surface** (confirmed again):
  after a custom resize, scroll clamped and a scrolled screenshot rendered the
  fixed header at the bottom over empty space. The FIRST screenshot right after a
  resize (still at the top) worked; scrolled ones glitched. Fix: stop + start for a
  fresh native viewport. Native viewport here is ~707px (tablet layout, tabs
  hidden), so to screenshot the desktop nav you must resize to ~1280 and shoot the
  hero immediately, before scrolling.
- python http.server stale cache: always cache-bust with ?v=.

## Still open (carried)

- Apartments + beach-houses as full cards (needs scraped photos + verified copy).
- Optional tarifa -> stay teaser/cross-link.
- Shopping section (deferred since 06-11).
- Map: keyless OpenStreetMap shipped; Annabel may still want the exact Google look.
- Homepage "Oleg" / "Leah" still [unconfirmed] (no-invented-people rule).
- Before live launch: photo clearance; verify hotel Google review counts if counts
  are wanted on the cards.
