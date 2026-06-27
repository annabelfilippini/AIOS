# Stoop

A Nextdoor for kid sellers. "The market that never packs up."

## What it is
A neighborhood marketplace that aggregates local kid sellers. Kids list what
they make, neighbors browse and buy, **local pickup only**. Sparked by a one-day
kids' farmers market: that market solves demand + local trust for an afternoon,
but a kid (e.g. one selling backyard honey) has no way to keep selling after it
packs up. The magic is the *block of stalls*, not any one stall — aggregation is
the value. A storefront builder (Shopify-for-9-year-olds) lives inside it as a
feature, not the product.

## Locked decisions
- **Users vs buyers:** kids are the stars/users (post + check sales); parents +
  neighbors are the buyers. Kid-facing joy on a parent rail.
- **Local pickup only** — the product, not a limitation. Kills the trust problem
  and the legal problem at once (no shipping = no FDA, no interstate food rules,
  no stranger fraud).
- **Payments:** a minor can't hold Stripe/PayPal, so **a parent is the account
  holder behind every stand**. COPPA mostly sidestepped (sellers are minors,
  parents hold accounts).
- **Legal read (general):** kids selling their own stuff is broadly legal
  (self-employment, not child labor). Honey is best-case cottage food.

## Open question
**Cold-start is double-empty** — need kid-sellers AND neighbor-buyers on the same
few blocks at once. Working GTM hypothesis: be the digital tail of a real one-day
kids' market that already gathered the roster + trust in an afternoon.

## NEXT (not yet picked)
- Builder flow — the 4-5 questions a kid answers to go from nothing to their page
- Parent view — the approve-orders / see-the-money screen (the load-bearing rail)
- Name + vibe options — "Stoop" chosen; still want a calmer dial-back visual
- GTM — the real-market tail hypothesis

## Stack
- No framework, no backend. `preview.html` is a single self-contained HTML file.
- Design is in a deliberate **craft-fair lane** (rounded corners, bunting, tilt)
  because the audience is ~8-year-olds — the one place the house no-rounded rule
  is intentionally broken. Fonts: Fredoka (display) + Nunito (body) + Caveat
  (marker). Dial-back path if too sugary: keep warm paper + chunky type, drop
  bunting/tilt, calm the brights.
- Non-assumptions: no Stripe/Supabase/hosting set up yet. Concept/preview stage.

## Files
- `preview.html` — current two-view concept (the market + a kid's stand)
- `shots/` — rendered screenshots
- `references/` — pasted inspiration / source images
