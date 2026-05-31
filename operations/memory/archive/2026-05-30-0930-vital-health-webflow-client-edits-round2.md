---
date: 2026-05-30
time: 09:30
project: consulting / vital-health
status: second client-edit round applied + published to staging; site QA-clean; ready to share staging link with client (Rob/Julie) for review
next-session: Still the same two content blockers before a LIVE custom-domain publish — (1) real testimonials on Home (3x placeholders), (2) medical-claim sign-off on Services. Founder story still routed to Julie via Rob's email. When client approves, point custom domain (vitalhealthim.com) and publish.
---

# Session: Vital Health Webflow — Final QA + Round 2 Client Edits

Supersedes `2026-05-29-1815-vital-health-webflow-touchups-email.md`.
Staging: `vital-health-9bf311.webflow.io` (subdomain only, `customDomains: []`).
Republished to staging ~4x this session. Staging link is PUBLIC (no login),
auto-updates on every publish, Webflow sets it no-index.

## Final QA pass (all 4 pages, curl + Playwright) — CLEAN
- All pages HTTP 200; 0 em-dashes; "Hope and Healing" gone; SEO titles +
  meta/OG/Twitter descriptions all set (titles use "|", no em-dash regression
  even though Designer page-settings still cache an em-dash title — live output
  is correct via Data API). 0 console errors. Scripts (vhscrollreveal +
  VHMobileNav) load on all pages.

## Round 2 edits applied + verified live
1. **About "care team" block → just "The Team".** Set h2.ab-team-h2 = "The Team"
   (was "The team that *stays with you*."); removed eyebrow span "The care team"
   (...6998b2) and the body paragraph (...6998b9) via element_tool remove_element.
2. **About: removed the jagged gold pulse SVG** above the team heading
   (ab-pulse, ...6998b0). Section is now `<div><h2>The Team</h2></div>`.
3. **About ab-team band made smaller.** padding-top/bottom 80px → 50px (band
   height 220 → 160px). text-align already center; heading stays centered.
4. **Contact info-row alignment fixed.** `.ct-fact` align-items start → **baseline**
   and `.ct-fact-lbl` padding-top 3px → **0** so Phone/Email/Location/Hours labels
   baseline-align with their values (were top-aligned/floating).
5. **Removed underlines on all 4 CTA buttons** (text-decoration: none): Contact
   `ct-cta-white`, `ct-cta-ghost`; About `ab-btn-primary`, `ab-btn-outline`.
   Outline/ghost buttons keep their box borders (those are button outlines, not
   underlines — left intact intentionally).
6. **Contact green "header box" (`.ct-info-card`) smaller + centered.** Added
   display:flex, flex-direction:column, align-items:center, text-align:center,
   align-self:flex-start (stops it stretching to the tall facts column, removing
   the empty green void). `.ct-cta-row` align-items flex-start → center so the
   two buttons center too.

## Still-standing blockers before LIVE (custom-domain) publish (unchanged)
- Real testimonials (Home still 3x "[Patient testimonial...]" placeholders).
  Fine for a client-REVIEW link; must replace/hide before patient-facing live.
- Medical-claim sign-off on Services (semaglutide 18%/6-8wk, exosome 96%→7%,
  testosterone ~50%) — needs clinician verification.
- Founder story (About) routed to Julie via Rob's email.

## Gotchas (reconfirmed this session)
- Designer style_tool/element_tool still times out ~every other large call;
  RETRY with the Webflow Designer tab foregrounded — the retry succeeds. Style
  updates are idempotent so re-running the whole batch on timeout is safe.
- Data API (data_sites publish, data_pages settings) never times out.
- Webflow caches published HTML/CSS + the CSS filename hash changes per publish;
  cache-bust (?cb=) and re-extract the .css URL when curl-verifying.
- Bash safety classifier (claude-opus-4-8) was intermittently down; read-only
  ops + Playwright browser_evaluate worked as a fallback for DOM/CSS inspection.

## Key IDs
- Site 6a15e6f364922623e13946da
- Home 6a15e6f464922623e139470e | Services 6a15f430cbd0f7ef0469e27f |
  About 6a19b8b56de372b248e55901 | Contact 6a19bf5c98546d4f3a53d97a
- About team heading h2.ab-team-h2: fb40ea1a-fc4f-34fd-74eb-46e97f6998b7
- Styles touched: ct-fact, ct-fact-lbl, ct-info-card, ct-cta-row, ct-cta-white,
  ct-cta-ghost, ab-team, ab-btn-primary, ab-btn-outline
- Designer launch: https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99

## QA screenshots (project root)
qa-final-home-desktop.png, qa-contact-facts.png, qa-contact-final.png,
qa-about-cta-final.png, qa-team-smaller-final.png (+ baseline/preview variants).
