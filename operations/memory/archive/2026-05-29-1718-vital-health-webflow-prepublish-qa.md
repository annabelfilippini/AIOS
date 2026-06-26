---
date: 2026-05-29
time: 17:18
project: consulting / vital-health
status: qa-pass-done-blockers-remain
next-session: Resolve 3 client-input blockers before any custom-domain publish — real testimonials (Home still placeholders), mobile nav menu (no hamburger), medical-claim accuracy on Services. Optional: footer compact hours via component edit; client "what's editable" note.
---

# Session: Vital Health Webflow — Pre-Publish QA Pass

## What this session did

Full QA of all 4 pages before publishing. Published to **staging only**
(`vital-health-9bf311.webflow.io`; no custom domain — `customDomains: []`,
`fullSiteCompiledAt` was null before this). Reviewed desktop (1440) + mobile
(390) via Playwright. Screenshots in `projects/.../docs/qa-*.png`.

## Edits applied + verified live on staging

- Home Facts: "4 / Dedicated practitioners — one MD, two NPs, one founding
  advisor." → **"3 / Dedicated practitioners — one MD, two NPs."** (matches
  About). Verified count=3, no "founding advisor".
- Home hero CTA "Schedule a consultation": link `/contact` →
  **`https://vitalhealth.md-hq.com`**, new tab, `rel="noopener noreferrer"`
  (matches other Book buttons). Verified href+target+rel.
- Contact page hours: `8:00am – 5:00pm` → **`8am – 5pm`** (Home already matched).
- SEO: Home got title "Vital Health Integrative Medicine — Austin, TX" +
  description (was empty); About description "four practitioners" → "three".
  (Both via Data API `update_page_settings`.) Verified tab title.

## Verified GOOD (no action needed)

- `/services` serves the **designed** page, not the CMS "Services Template"
  collision — routing concern from prior checkpoint is a non-issue.
- All anchors resolve: `#peptide/#hormone/#weight/#wellness/#schedule`.
- Scroll-reveal works on real scroll (25/25 elements vh-in). Hiding CSS is
  **JS-injected** = progressive-enhancement safe (content visible if JS fails).
  `prefers-reduced-motion` handled. No console errors, no horizontal overflow.
- Editability: all body copy, images, bios, stats, contact details are native
  Designer elements (client-editable). Only code = 1 site script `vhscrollreveal`
  (footer) handling animation + nav underline.

## BLOCKERS before custom-domain publish

1. **Placeholder testimonials** — Home reviews section still 3x "[Patient
   testimonial — drop in a real quote...]". Left as-is per Annabel — she will
   input real quotes AFTER meeting the client. MUST replace or hide before live.
2. **Medical-claim accuracy (Services)** — Annabel to verify with the practice
   clinician at the client meeting. Specific claims to confirm/source:
   - semaglutide "18% bodyweight in 6–8 weeks" (real STEP trials ~15% over ~68 wks)
   - exosome "96% stem cell at birth → 7% by 80"
   - "Testosterone in women can decline by as much as 50% between ages 20 and 50"
   Option offered: soften to non-numeric defensible phrasing if client can't source.

## RESOLVED this session (was blocker #2)

- **Mobile nav menu** — BUILT. Added inline script **VHMobileNav v0.0.2**
  (site footer, alongside vhscrollreveal). Injects a hamburger toggle for
  `max-width:991px`: hides the in-bar `.nav-portal`, drops `.nav-links` into an
  absolute dropdown panel (solid #F5EFE0 + blur), clones the Patient Portal link
  into the menu (`.nav-portal-m`), animates hamburger→X, closes on link click.
  Verified on staging at 390px: 5 items, opaque panel, no overflow. Nav LINKS
  remain Designer-editable; new links auto-appear in the mobile menu.
  Note: Webflow caches the published HTML's script URL — cache-bust (?cb=) to
  see a newly-published script version immediately.

## Smaller leftovers

- Footer compact hours `Mon – Fri · 8a – 5p` NOT standardized — lives inside the
  Site Footer component (012f5c9e-...); component-internal text isn't reachable
  via page-element query_elements. Needs component-edit mode (or 5-sec Editor
  fix). Other two hour instances now consistent.
- Footer "Privacy · HIPAA" are plain text linking nowhere (no policy pages).
- Hours day-name still mixed (Monday–Friday vs Mon–Fri) — acceptable by context.

## Designer MCP connection (recurring)

Still flaky: light page-tool calls (switch_page, get_current_page,
get_current_mode) reliable; `element_tool` works for ~2-3 calls then times out,
recovers on retry when Designer tab is foregrounded. element_tool edits used
this session: set_text, set_settings(static_link), add_or_update_attribute,
query_elements — all eventually succeeded with retries. Data API (pages/sites/
scripts) is the reliable path.

## Key IDs (unchanged from prior)

- Site 6a15e6f364922623e13946da | Home 6a15e6f464922623e139470e |
  Services 6a15f430cbd0f7ef0469e27f | About 6a19b8b56de372b248e55901 |
  Contact 6a19bf5c98546d4f3a53d97a
- Home hero link element: dfe91478-4749-8c07-8acb-372f952b8137
- Site Footer component: 012f5c9e-8f09-5be5-b1b2-9a28cb867f35
- Reveal script: vhscrollreveal v0.0.4, site footer
- Designer launch: <https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99>
