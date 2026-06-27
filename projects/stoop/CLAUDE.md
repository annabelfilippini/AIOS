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

## Shape (refined)
**Link-first, feed-second.** Every kid gets a personal, shareable profile page
(Linktree/Beacons pattern, not Etsy). The feed is where those pages collect — it
fills in *behind* the link, not before it. Growth loop: a kid shares their link →
people land on Stoop → some get curious → a few make their own page.

This dissolves the cold-start problem for launch: you don't need a full
neighborhood, you need one kid with a link.

## Hyperlocal is a hard rule, not a nice-to-have
Nextdoor's failure mode is loose geo — you get alerts from people nowhere near
you and it's just noise. Stoop must be **block/neighborhood-tight**: at signup we
verify which specific neighborhood someone is in, and the feed only ever shows
*your* blocks. Pickup-only naturally enforces this (you only buy from someone you
can walk/drive to). This is a **feed-era** decision — it does NOT bite v1 (a
single shared page works regardless of geo), but it's locked for when the feed
exists. Do not build broad-radius defaults.

## Open question
**Cold-start is double-empty** — need kid-sellers AND neighbor-buyers on the same
few blocks at once. Working GTM hypothesis: be the digital tail of a real one-day
kids' market that already gathered the roster + trust in an afternoon. The
link-first shape (above) is the practical answer for launch.

## NEXT (not yet picked)
- Builder flow — the 4-5 questions a kid answers to go from nothing to their page
- Parent view — the approve-orders / see-the-money screen (the load-bearing rail)
- Name + vibe options — "Stoop" chosen; still want a calmer dial-back visual
- GTM — the real-market tail hypothesis

## v1 = the cousin's lacrosse page
One page, built from ~5 questions (name + age, what you offer, price, when you're
available, one thing about you). Looks personal and pretty. Has a **visual,
interactive calendar** for her schedule/availability. "Request a lesson" button
that routes to her **parent** (email/text) — NOT an open DM inbox on a child's
profile. Shareable link. No feed yet, no other kids — prove the link first.

- **Payments off-platform in v1** — kid just shares Venmo, sorts pickup directly.
  Stoop touches no money → no Stripe, no parent-account, no COPPA payment knot.
- **AI page builder stays lazy in v1** — 5 questions + templates, no live model.
  The "rewrite in kid-voice / generate a theme" model layer is a later add.
- Service wedge (coaching) dodges cottage-food/inventory entirely.

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
