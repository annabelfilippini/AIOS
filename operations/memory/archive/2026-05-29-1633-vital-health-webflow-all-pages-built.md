---
date: 2026-05-29
time: 16:33
project: consulting / vital-health
status: ready-for-review
next-session: Publish to .webflow.io STAGING ONLY and review all 4 pages. Confirm Fraunces 200 weight is loaded in Site Settings (else headings fall back to 300). Optional copy tweak: About team-intro h2 still says "A founder, a lead..." — reword to owner-led if desired.
---

# Session: Vital Health Webflow — All Four Pages Built

## Status: all pages exist; needs a staging publish to review
Home (polished), Services (prior session), About (built + content-corrected),
Contact (built). Custom code (reveal) + weight-200 render only on PUBLISH.
Annabel's publish target = **.webflow.io staging only** (no custom domain push).

## Designer connection
Worked well this session with intermittent idle drops (every few min when the
Designer tab loses foreground). Re-foregrounding the tab restores it; whtml /
element / style / component calls all succeed. Page creation now works after
Annabel UPGRADED her Webflow plan + reloaded the Designer.

## Home polish — DONE
- Headings weight **200** (hero-h1, facts-h2, services-h2, phil-h2, rev-h2,
  sched-h2). NOTE: needs Fraunces 200/ExtraLight loaded in Site Settings or
  browser falls back to 300. svc-h3 stays 400; *-emph accents 400 forest.
- 4 service-card SVG icons added (.svc-icon, 52x52 forest stroke 1.3).
- Scroll-reveal script (see below).
- Removed site-nav border-bottom; fixed hero-h1 "Fraunce"→"Fraunces" typo.

## About page — DONE (id 6a19b8b56de372b248e55901, /about)
Built with **ab-** namespaced classes. Nav cmpt + hero + philosophy (2-col) +
team intro + practitioners + schedule + footer cmpt.
CONTENT CORRECTIONS (Annabel: Feste no longer works there, Julie is owner):
- ❌→removed Dr. Feste's full practitioner section.
- Julie Swett role → **"Owner & Practice Lead"**.
- Philosophy P1 reframed to past-tense founding legacy (no "still advising").
- Counts fixed four→**three** in hero P, philosophy P4, team-intro P.
- Practitioners now: Swett (owner), Thigpen, Peña — monogram cutouts JS/KT/KP.
- OPEN: team-intro h2 still "A founder, a lead, and the practitioners..." —
  has an emph accent span, so edit the leading String node only to preserve it.

## Contact page — DONE (id 6a19bf5c98546d4f3a53d97a, /contact)
Built with **ct-** namespaced classes. Nav cmpt + hero ("Let's start the
conversation") + contact body (forest .ct-info-card schedule CTA + .ct-facts
details list: phone/email/location/hours/portal) + map band ("In the hills of
West Austin" + Get directions) + footer cmpt. No images needed.

## Scroll-reveal script
Inline script id **vhscrollreveal**, applied site-wide footer, now **v0.0.3**
(covers Home + About ab-* + Contact ct-* selectors). Injects .vh-reveal/.vh-in
+ IntersectionObserver (threshold 0.12, rootMargin -8%), 80ms stagger,
respects prefers-reduced-motion. Renders on PUBLISHED site only.
NOTE: update_registered_script API kept 404ing; had to register_inline_script
with a new version then set_site_scripts to it. Do that for future edits.

## Key IDs
- Site: 6a15e6f364922623e13946da
- Home 6a15e6f464922623e139470e | Services 6a15f430cbd0f7ef0469e27f
- About 6a19b8b56de372b248e55901 (body 6a19b8b56de372b248e55907)
- Contact 6a19bf5c98546d4f3a53d97a (body 6a19bf5c98546d4f3a53d980)
- Components: Site Nav 86e91719-83ad-954e-3c69-f8b0eb5e6999 ;
  Site Footer 012f5c9e-8f09-5be5-b1b2-9a28cb867f35
- Designer launch: https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99

## Remaining / next
1. Publish to .webflow.io staging, review all 4 pages.
2. Confirm/add Fraunces 200 weight in Site Settings.
3. Optional: About team-intro h2 reword.
4. Nav links: confirm About/Contact nav items point to /about and /contact
   (Site Nav is a shared component — should resolve once pages exist).
