# Vital Health Webflow Build — In Progress

Started: 2026-05-26 (Annabel + Claude session)

Site: Vital Health (`6a15e6f364922623e13946da`)
Designer launch link: `https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99`

## Completed

- ✅ Design tokens (Base collection `collection-c6357a93-3689-4d6c-109f-554c923ef96c`):
  - 16 colors: cream, cream-2, paper, sand, stone, stone-2, sage, ink, ink-2, muted, forest, forest-2, forest-soft, gold, gold-soft, gold-dim
  - 2 font families: font-display (Fraunces), font-body (Inter)
- ✅ Base styles: wrap, eyebrow, btn-primary, btn-outline, link-arrow (bound to color/font variables)
- ✅ **Site Nav** component (`86e91719-83ad-954e-3c69-f8b0eb5e6999`, group: Layout) — fixed top nav with brand lockup, 4 links, Patient Portal CTA → Cerbo
- ✅ **Site Footer** component (`012f5c9e-8f09-5be5-b1b2-9a28cb867f35`, group: Layout) — forest BG, brand lockup, Explore/Services/Visit columns, copyright + "Hope and Healing" mantra
- ✅ **Home page complete** — all 6 content sections + Nav + Footer:
  - Hero (`dfe91478-4749-8c07-8acb-372f952b813d`)
  - Facts (`8e476e05-5fc9-5a29-0705-9d081b1195f6`)
  - Services grid (`84c0e81f-327c-8245-28af-e6e18c24d845`)
  - Philosophy (`bfb7ca9c-f75d-9bc1-d06d-1c7d32c5bf6f`)
  - Reviews (`5c064d71-6e5d-9659-5229-a6b1daf863be`)
  - Schedule CTA (`de2778e8-e3c0-8c5e-83d6-dec2ae0d5b98`)

- ✅ **Services page complete** (`/services-overview`, page `6a15f430cbd0f7ef0469e27f`) — Nav + hero + 4 service blocks (Peptide Therapy, Hormone Optimization, Medical Weight Loss, Wellness & Rejuvenation) + Schedule CTA + Footer.
  - Schedule CTA (`#schedule`): "Book a consultation" → Cerbo (`https://vitalhealth.md-hq.com`, new tab, rel=noopener); "Call (512) 559-4350" → tel link.
  - Note: the Schedule CTA insert appeared to time out on a Designer connection drop, but it actually landed — verified 2026-05-28.

## In Progress

- **Polish pass — BLOCKED on Designer connection.** Annabel reviewed Home + Services vs. the Vercel original and flagged 3 fixes (see below). Designer MCP `element_tool` times out after the first call, so native edits aren't reliable. Decision pending: custom code via Data API (reliable, code-only, needs publish) vs. native Designer edits. See checkpoint `2026-05-29-1725-vital-health-webflow-polish-blocked.md`.

### Review feedback to fix (from Vercel original)

1. **Headings too bold** — original display headings are Fraunces **Light (weight 300)**; accents (`.emph`) are 400. Set heading classes to 300. (Fonts confirmed added in Site Settings.)
2. **Service icons missing** — 4 Home service cards need their inline SVG icon above the title. Markup: `snapshot/index.html` lines 311-336. `.svc-icon` 52x52, color forest, stroke-width 1.3.
3. **No scroll-reveal** — replicate `.reveal` opacity/translateY + IntersectionObserver (CSS lines 44-50, JS lines 451-454 in snapshot). Annabel chose custom-code exact-match.

## Next

- Resolve the 3 polish fixes → About page → Contact page (create + build) → QA + publish

## Known polish items (do at end)

- ✅ Hero image (asset `6a15e762c2275bbc9df0cb25`) — proper Webflow Image element placed
- ✅ Nav brand logo (asset `6a15e761c2275bbc9df0caf7`) — proper Webflow Image element placed
- [ ] Footer brand-tag "INTEGRATIVE MEDICINE" wraps in narrow column — tighten letter-spacing or shorten
- [ ] Font setup: Annabel to add Fraunces + Inter in Site Settings → Fonts. See `docs/webflow-fonts-setup.md` for step-by-step.
- [ ] Hummingbird mark (asset `6a15e7613db23d2363961bd9`) — currently absent from footer brand lockup; original Vercel snapshot uses it as a CSS mask. Add as inline image to left of "Vital Health" in footer if desired.
- [ ] Feste portrait (asset `6a15e762dc3b4a8c69963ab8`) — for About page founder section
- [ ] Scroll-reveal animations from the snapshot (`.reveal` opacity/transform) and hero rise — Webflow Interactions, manual

## Follow-ups / TODO

- Add Fraunces + Inter to Webflow site fonts (Site Settings → Fonts → Add Google Font). Variables declare the family name but Webflow needs the font added to actually load it. Verify in Designer after first heading is placed.
- `.env` Webflow API token (`WEBFLOW_API_TOKEN`) is in project root — already git-ignored.
- Contact page does not exist yet; will be created during page build phase.
