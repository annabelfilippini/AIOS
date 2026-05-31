---
date: 2026-05-29
time: 17:26
project: consulting / vital-health
status: qa-done-mobile-built-2-blockers-remain
next-session: Two client-input blockers gate a live (custom-domain) publish — (1) real testimonials on Home, (2) medical-claim sign-off on Services. Both are Annabel's after her client meeting. Optional leftovers below. Staging is current and reviewable.
---

# Session: Vital Health Webflow — Pre-Publish QA + Mobile Nav Built

Supersedes `2026-05-29-1718-vital-health-webflow-prepublish-qa.md`.

## Where the site is
Full QA done on all 4 pages (desktop 1440 + mobile 390) via Playwright.
Published to **staging only**: `vital-health-9bf311.webflow.io` (no custom
domain — `customDomains: []`). Visuals polished, content correct/concise,
mobile nav working, content editable in Designer. Screenshots:
`projects/vital-health-webflow-migration/docs/qa-*.png`.

## Edits applied + verified live this session
- Home Facts: "4 / one MD, two NPs, one founding advisor" → **"3 / one MD, two
  NPs"** (matches About). Verified.
- Home hero CTA "Schedule a consultation": → **patient portal**
  (`https://vitalhealth.md-hq.com`), new tab, `rel="noopener noreferrer"`.
  Verified href+target+rel.
- Contact hours: `8:00am – 5:00pm` → **`8am – 5pm`** (Home already matched).
- SEO: Home title "Vital Health Integrative Medicine — Austin, TX" + description
  added (was empty); About description "four"→"three". Verified tab title.
- **Mobile nav menu BUILT** — inline script **VHMobileNav v0.0.2** (site footer,
  with vhscrollreveal). Hamburger at `max-width:991px`; hides in-bar
  `.nav-portal`, drops `.nav-links` into an opaque absolute panel (#F5EFE0+blur),
  clones Patient Portal into menu (`.nav-portal-m`), hamburger→X, closes on link
  click. Verified at 390px: 5 items, opaque, no overflow. Nav links stay
  Designer-editable; new links auto-appear in the mobile menu.

## Verified GOOD (no action)
- `/services` serves the DESIGNED page, not the CMS "Services Template" collision.
- All anchors resolve: `#peptide/#hormone/#weight/#wellness/#schedule`.
- Scroll-reveal works (25/25); hiding CSS is JS-injected = progressive-enhancement
  safe (visible if JS fails); `prefers-reduced-motion` handled. No console errors.
- Editability: all body copy/images/bios/stats/contact details are native
  Designer elements. Only code = 2 polish scripts (vhscrollreveal, vhmobilenav).

## BLOCKERS before live (custom-domain) publish — Annabel, post client-meeting
1. **Real testimonials** — Home reviews still 3x placeholder "[Patient
   testimonial...]". Left as-is per Annabel; she inputs real quotes after the
   client meeting. Replace or hide before live.
2. **Medical-claim sign-off (Services)** — clinician to confirm/source:
   - semaglutide "18% bodyweight in 6–8 weeks" (real STEP ~15% over ~68 wks)
   - exosome "96% at birth → 7% by 80"
   - "testosterone in women can decline ~50% between ages 20 and 50"
   Offer: soften to non-numeric defensible phrasing if unsourceable.

## Smaller leftovers (optional)
- Footer compact hours `Mon – Fri · 8a – 5p` NOT standardized — lives in the Site
  Footer component (012f5c9e-...); component-internal text isn't reachable via
  page-element query_elements (needs component-edit mode or a 5-sec Editor fix).
- Footer "Privacy · HIPAA" are plain text linking nowhere (no policy pages).
- Offered but not yet written: a client "what you can edit in Webflow" note.

## Gotchas / operational notes
- Designer MCP `element_tool` still flaky: works ~2-3 calls then times out,
  recovers on retry with Designer tab foregrounded. Data API (pages/sites/
  scripts) is reliable. Used for edits: set_text, set_settings(static_link),
  add_or_update_attribute, query_elements.
- Webflow caches published HTML's script-src URL — after publishing a new script
  version, cache-bust (`?cb=`) to verify the new version loads.
- update_registered_script 404s; to change a script: register_inline_script with
  a NEW version, then add_site_script with that version.

## Key IDs
- Site 6a15e6f364922623e13946da | Home 6a15e6f464922623e139470e |
  Services 6a15f430cbd0f7ef0469e27f | About 6a19b8b56de372b248e55901 |
  Contact 6a19bf5c98546d4f3a53d97a
- Home hero link element: dfe91478-4749-8c07-8acb-372f952b8137
- Site Footer component: 012f5c9e-8f09-5be5-b1b2-9a28cb867f35
- Scripts (site footer): vhscrollreveal v0.0.4, vhmobilenav v0.0.2
- Designer launch: https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99
