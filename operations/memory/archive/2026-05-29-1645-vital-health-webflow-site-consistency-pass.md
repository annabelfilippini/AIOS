---
date: 2026-05-29
time: 16:45
project: consulting / vital-health
status: ready-for-review
next-session: Publish to .webflow.io STAGING ONLY and review all 4 pages. Confirm /services loads the designed page (CMS "Services Template" collection also uses /services for items — normally coexists). Confirm Fraunces 200 weight is loaded in Site Settings.
---

# Session: Vital Health Webflow — All Pages Built + Consistency Pass

## Status: full 4-page site built; needs a staging publish to review

Pages: Home `/`, Services `/services`, About `/about`, Contact `/contact`.
Custom code (reveal + nav current-underline) and weight-200 render only on
PUBLISH. Publish target = **.webflow.io staging only** (no custom domain).

## Designer connection

Mostly reliable this session; idle drops when the Designer tab loses
foreground — re-foreground to restore. whtml/element/style/component/data-API
all work. Page creation works (Annabel upgraded Webflow plan).

## What exists / done

- **Home** — polished: display headings weight 200, 4 service-card SVG icons
  (.svc-icon), nav border removed, hero-h1 font typo fixed, scroll-reveal.
- **Services** `/services` — built prior session (svcpg-*/svc-block classes).
  Slug changed THIS session from "services-overview" → **"services"** so the
  nav link reaches it + current-underline works. (See routing note below.)
- **About** `/about` — built this session (ab-* classes). Feste section REMOVED;
  Julie Swett = "Owner & Practice Lead"; philosophy reframed past-tense; counts
  four→three; team-intro h2 reworded to "Owner-led, and the practitioners who
  see you through." Practitioners: Swett/Thigpen/Peña (monogram cutouts).
- **Contact** `/contact` — built this session (ct-* classes): hero, forest
  schedule card, details list, "West Austin" map band. Phone/email/portal in
  the details list converted from links to PLAIN ink text (Annabel: not
  clickable, match location/hours). Booking + Call CTA buttons in the schedule
  card left clickable (intentional).
- **Headings** — all display headings on Home/About/Contact at font-weight
  **200** (Fraunces Light). NEEDS Fraunces 200/ExtraLight loaded in Site
  Settings or falls back to 300. *-emph accents stay 400 forest; svc-h3 400.
- **Nav active underline** — removed static `nav-link-active` from Home link;
  underline now follows current page via `.nav-link.w--current` CSS (injected
  by the site script). Works on published pages where nav href matches path
  (`/`, `/services`, `/about`, `/contact`).
- **Scroll-reveal** — inline site script id **vhscrollreveal**, site-wide
  footer, now **v0.0.4**. Injects .vh-reveal/.vh-in + .nav-link.w--current CSS;
  IntersectionObserver (threshold 0.12, rootMargin -8%), 80ms stagger,
  prefers-reduced-motion safe. Covers Home + About(ab-*) + Contact(ct-*) +
  Services(svcpg-hero-inner/svcpg-jumpnav/svc-block) selectors.

## Routing note to verify on publish

Designed Services static page now owns `/services`. The auto-generated CMS
"Services Template" collection (id 6a15e7c7d027bc3276dff771) also reports
publishedPath `/services` (its items live at /services/[item]). These usually
coexist; CONFIRM on staging that `/services` serves the designed page. If
collision: rename that CMS collection's URL slug to free `/services`.

## Scripts API quirk

`update_registered_script` keeps 404ing. To change the reveal script: call
`register_inline_script` with a NEW version, then `set_site_scripts` to it.
Currently applied: v0.0.4.

## Key IDs

- Site 6a15e6f364922623e13946da
- Home 6a15e6f464922623e139470e | Services 6a15f430cbd0f7ef0469e27f
- About 6a19b8b56de372b248e55901 (body 6a19b8b56de372b248e55907)
- Contact 6a19bf5c98546d4f3a53d97a (body 6a19bf5c98546d4f3a53d980)
- Components: Site Nav 86e91719-83ad-954e-3c69-f8b0eb5e6999
  (links: Home "/", Services "/services", About "/about", Contact "/contact";
  Home link active class removed) ; Site Footer 012f5c9e-8f09-5be5-b1b2-9a28cb867f35
- Reveal script: vhscrollreveal v0.0.4, site footer
- Designer launch: <https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99>

## Remaining / next

1. Publish to .webflow.io staging; review all 4 pages.
2. Verify /services serves designed page (routing note above).
3. Confirm/add Fraunces 200 weight in Site Settings.
4. Possible future: Dr. Feste real photo no longer needed (section removed).
