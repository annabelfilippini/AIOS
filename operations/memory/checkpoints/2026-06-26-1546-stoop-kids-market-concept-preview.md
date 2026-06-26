---
date: 2026-06-26 15:46
project: stoop
status: in-progress
type: checkpoint
slug: stoop-kids-market-concept-preview
---

# Stoop — neighborhood kid market concept + first visual preview

## The idea
Sparked by a one-day kids' farmers market. The wedge: that market already solved
demand + local trust for an afternoon, but a kid (e.g. one selling backyard
honey) has no way to keep selling after it packs up. Stoop = "the market that
never packs up." A **Nextdoor for kid sellers**: verified by neighborhood, kids
list what they make, neighbors browse and buy, **local pickup only**.

Two products hide in here; we landed on #2 with #1 as a feature inside it:
1. a storefront builder (Shopify-for-9-year-olds), and
2. a neighborhood marketplace that aggregates all the local kids. The magic was
   the *block of stalls*, not any one stall, so aggregation is the real value.

## Decisions made this session
- **Customer attention:** kids are the stars/users (they post + check sales);
  parents + neighbors are the buyers. Kid-facing joy riding on a parent rail.
- **Fulfillment: local pickup only.** This is the product, not a limitation — it
  kills the trust problem AND the legal problem at once (no shipping = no FDA, no
  interstate food rules, no stranger fraud).
- **Legal read (general, not yet state-specific):** kids selling their own stuff
  is broadly legal (self-employment, not child labor). Honey is the *best* case —
  most-exempt cottage food in the US. The real blocker is payments: a minor can't
  hold Stripe/PayPal, so **a parent is the account holder behind every stand**.
  COPPA is mostly sidestepped because sellers are minors and parents hold accounts.

## What was built
- `projects/kids-market/preview.html` — single self-contained HTML, two views:
  1. **The market** — verified "Maple Grove · 14 kid stands" header, bunting,
     feed of taped-flyer cards (Theo's honey, Maddie's lacrosse lessons = the
     cousin, friendship bracelets, Cookie Twins, car wash, birdhouses, lemonade,
     dog walking), name+age, chunky price, pickup tag, ♥ save, category filter
     chips, black "Build my stand" band.
  2. **A kid's stand** — the auto-generated mini-site (the website-builder idea):
     Theo's Honey hero, "About my bees" in kid voice, order box, gallery. Same
     builder makes the cousin's lacrosse page.
- **Parent rail made visible, not hidden:** order button = "I want a jar" with
  "Orders go to Theo's mom" beneath; click spells out the model.
- **Illustration-led, no photos** (fictional kids — fake-people photos banned by
  design rules anyway; doodles solve licensing + childlike-excitement at once).
- Copy on Desktop: `~/Desktop/stoop-preview.html`. Screenshots:
  `projects/kids-market/shot-market.png`, `shot-stand.png`. Verified both views
  render clean in browser (served on :8731, now stopped).

## Design note
Deliberately pushed Annabel's house cream/editorial language into a **craft-fair
lane** (rounded corners, bunting, marker underline, tilted cards) because the
audience is ~8-year-olds. This is the one place the sharp-corner / no-rounded
rule was intentionally broken. Fonts: Fredoka (display) + Nunito (body) + Caveat
(marker). Dial-back path if too sugary for the approving parents: keep warm paper
+ chunky type, drop bunting/tilt, calm the brights.

## NEXT (pick one)
- **Builder flow** — sketch the 4–5 questions a kid answers to go from nothing to
  the honey page.
- **Parent view** — the approve-orders / see-the-money screen (the load-bearing
  rail).
- **Name + vibe options** — "Stoop" is a placeholder; show 3 directions side by
  side; also a calmer "dial-back" visual vs the current sugary one.
- Open question not yet tackled: **cold-start is double-empty** (need kid-sellers
  AND neighbor-buyers in the same few blocks). Proposed GTM: be the digital tail
  of a real kids' market that already gathered the roster + trust in one afternoon.

No code committed (concept/preview only). Working files live in
`projects/kids-market/` (new folder, not a `projects/websites/` site).
