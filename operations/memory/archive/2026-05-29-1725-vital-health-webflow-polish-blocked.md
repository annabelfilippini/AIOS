---
date: 2026-05-29
time: 17:25
project: consulting / vital-health
status: blocked
next-session: Decide the fix approach (custom code via Data API vs native Designer edits) for the three Home-page polish items, then apply. Designer MCP connection is the blocker.
---

# Session: Vital Health Webflow — Polish Pass Blocked on Designer Connection

## State of the build

- ✅ **Home page** — content complete (design system, Nav, Footer, all 6 sections).
- ✅ **Services page** (`/services-overview`) — content complete (Nav, hero, 4 service
  blocks, Schedule CTA wired to Cerbo, Footer). The Schedule CTA that earlier
  "timed out" was verified to have actually landed.
- ❌ **About page** — not started.
- ❌ **Contact page** — not started.

## Annabel's review feedback (3 fixes needed before continuing)

After reviewing Home + Services against the Vercel original
(`https://vital-health-deploy.vercel.app/`), three gaps:

1. **Headings too bold.** Original display headings are **Fraunces Light (font-weight 300)**
   — hero H1 and every section H2 (Facts, Services, Philosophy, Reviews, Schedule).
   Only the green accent words (`.emph`) are weight 400. Body is Inter 400. Webflow
   headings are rendering heavier (~400+). Fonts were added in Site Settings with
   weights 300/400/500 (Fraunces) and 300/400/500/600 (Inter) — confirmed by Annabel.
   Fix = set heading classes to weight 300.
2. **Service icons missing.** The 4 Home service cards (Peptide, Hormone, Weight Loss,
   Wellness) each have an inline SVG icon above the title in the original; not built in
   Webflow. Exact SVG markup captured in `snapshot/index.html` lines 311-336.
   `.svc-icon` = 52x52, color var(--forest), svg stroke-width 1.3.
3. **No scroll-reveal.** Original fades+slides elements in on scroll: `.reveal`
   (opacity 0→1, translateY 28px→0) flipped to `.reveal.in` via IntersectionObserver
   (threshold 0.12, rootMargin '0px 0px -8% 0px'), staggered delays reveal-d-1..4
   (.08/.16/.24/.32s). CSS at `snapshot/index.html` lines 44-50; JS at lines 451-454.
   Annabel chose the **custom-code (exact-match)** approach for this one.

## The blocker

The Webflow **Designer** MCP connection is unreliable: light page-tool calls
(`de_page_tool` get_current_page / get_current_mode) succeed, but `element_tool`
queries succeed only on the FIRST call after the app loads, then time out on every
subsequent call. This has held across two sessions. Root cause looks like the
embedded Designer app stalling/idling; the linked Webflow FAQ URL 404s. Chrome
Memory Saver was suspected; turning it off did not resolve it.

Implication: native click-to-edit changes (real heading styles via style_tool,
real icon elements) are not reliably doable right now.

## Decision pending (asked, Annabel dismissed — pick up here)

Proposed pivot: do all three fixes via the **Data API** (`data_scripts_tool`,
token-based, reliable — independent of the flaky Designer connection) by registering
inline custom code applied site-wide (footer). Tradeoffs:

- ✅ Reliable, fast, fixes all three at once.
- ⚠️ Renders only on the **published** site (would publish to the free `.webflow.io`
  staging URL to review) — not in the Designer canvas.
- ⚠️ Lives as code, so not Designer-editable by the client. Against the
  "client edits everything in Designer" goal, but fonts/icons/animations are
  normal polish to keep as code.
- Note: inline scripts are capped at **2000 chars each** — the 4 SVGs + CSS + JS
  will need splitting across ~2 registered scripts.

Options offered: (A) custom code all three via Data API [recommended];
(B) keep trying native Designer edits (slow/flaky); (C) font fix native, rest as code.
Annabel dismissed the question — awaiting her direction next session.

## Context to preserve

- Webflow site ID: `6a15e6f364922623e13946da`.
- Designer launch link (must open + run the MCP App in the Apps panel, keep tab
  foregrounded): `https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99`
- Home page id `6a15e6f464922623e139470e`; Services page id `6a15f430cbd0f7ef0469e27f`.
- Source of truth for visual direction: `snapshot/` (index.html, services.html,
  about.html, contact.html) and the live Vercel preview.
- Open tasks tracked: #1 heading weight 300, #2 service icons, #3 scroll-reveal.

## System refinement candidates

- The Webflow **Designer** MCP connection is the recurring failure mode for this
  project (timeouts + idle drops). For Webflow builds, prefer the **Data API**
  tools (sites/pages/CMS/assets/scripts) for anything scriptable, and batch
  Designer element/style work into the smallest possible bursts right after the
  app loads. Consider documenting this in a reusable "Webflow rebuild" playbook.
