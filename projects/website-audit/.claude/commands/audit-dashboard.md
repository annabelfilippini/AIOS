# /audit-dashboard — Intelligence Dashboard Preview

Build an HTML mockup showing what ongoing site intelligence looks like for THIS specific business. This is the $1K-3K upsell pitch — a vision of continuous engagement, not a working product.

**Usage:** `/audit-dashboard <prospect-name>`

## Modes

When `AUDIT_AUTOMATED=1` is set in the environment, skip any interactive checkpoints — no user confirmations, no browser `open` calls, no manual review pauses. The skill runs end-to-end and reports via files only. Default (unset) = interactive mode, same behavior as today.

When `AUDIT_USE_STITCH=1`, run Phase A (Stitch generation). Default OFF per Apr 16 2026 decision — Phase B builds directly from `dashboard-spec.md` + audit + branding + design-library cues. Re-enable only if no-Stitch quality tanks.

## Good Example (Pepper Pong)

Created a Stitch project with an editorial design system (all-Inter, no white card boxes, ROUND_EIGHT, NEUTRAL color variant). Wrote a copy-spec Stitch prompt with every verbatim string fenced (keyword names, evidence lines, quick-wins, growth channel copy). Stitch produced an 80%-correct layout. A general-purpose agent then ported the Stitch skeleton to final HTML — swapping the broken Stitch trends chart for v1's working SVG, adding the AI scan hero animation with the real product image, porting v1's keyword pill + accent-bar layout. A bb-quality agent QA'd before return. Final: 767 lines, 0 broken images, trends dots land on the line, all 3 collapsible details work.

## Bad Example

Claude hand-built the dashboard in the main session — 1,174 lines, multiple sessions, ~300K tokens. Infeasible at scale.

Or: generic SaaS template — white card boxes, Montserrat headers, opportunity progress bars, 160x160 product thumbnail that looked like a favicon. **Both happened in v1.**

## Pipeline (MANDATORY AGENT DELEGATION)

**Phase A — Stitch generates editorial dashboard layout.** Opt-in only (`AUDIT_USE_STITCH=1`). Default OFF.
**Phase B — Agent assembles** the final HTML. If Phase A ran: port skeleton + v1 components. If Phase A skipped (default): build from `dashboard-spec.md` + audit + branding + design-library cues + v1 reference (if prior runs exist).

### CRITICAL RULES (enforced by hook in this project)

1. **Phase B MUST be delegated to an agent** via the `Agent` tool with `subagent_type: general-purpose`. Claude does NOT hand-edit dashboard HTML in the main session. This is the #1 usage sink — Pepper Pong's v1 dashboard cost ~300K tokens hand-built.
2. **The Phase B agent MUST spawn a QA agent** (`subagent_type: bb-quality`) before returning. QA validates: trends chart data points land on the line, scan animation actually animates (not static), every collapsible `<details>` works, no Google CDN URLs remain, all-Inter font stack verified.
3. **Human reviews only after agent QA passes.**

## Steps

### Setup

1. Read `prospects/$NAME/audit.md`, `seo-research.md`, and `branding.json` from upstream steps.
2. Read `prospects/$NAME/scrape/screenshots/` to understand the brand visually.
3. **Design library lookup.** Read `~/Documents/Claude/wiki/wiki/design-library.md`.
   - ALWAYS read the `## Dashboard / Analytics / Data UI` entry — these principles are validated (no white card boxes, all-Inter, plain-English evidence, collapsible details).
   - ALSO read the prospect's brand vertical (restaurant / DTC / luxury / editorial / personal-brand / etc.) — the dashboard should echo brand identity, not generic SaaS.
   - If the prospect's vertical is GAP or PARTIAL, flag it and do NOT default to a template. Each dashboard gets its own visual personality tied to the brand.
   - Extract 3-5 dashboard-discipline cues + 2-3 brand-vertical cues (palette accent, type choice, photography tone). Write them to `prospects/$NAME/dashboard-spec.md` under a `## Design Library References` header before Phase A.

### Phase A — Stitch generation (opt-in, default OFF)

**Gate:** Run steps 4-7 ONLY when `AUDIT_USE_STITCH=1`. If unset or `0`, skip to Phase B's no-Stitch branch.

4. **Create a separate Stitch project for the dashboard** via `mcp__stitch__create_project` with `title: "<Prospect> Intelligence Dashboard"`. Keep this separate from the homepage project — the design systems are different.
5. **Create the dashboard design system** via `mcp__stitch__create_design_system`. Dashboard-specific settings:
   - `headlineFont: INTER` (NOT Metropolis — dashboards are editorial, not bold brand)
   - `bodyFont: INTER`, `labelFont: INTER`
   - `roundness: ROUND_EIGHT` (subtle, not pill-round)
   - `colorVariant: NEUTRAL` (analytical, not vibrant)
   - `customColor` + overrides from `branding.json` — use the brand's coral/primary as the urgency accent, navy/secondary as the analytical accent, green for positive signals.
   - `designMd` MUST include: "NO WHITE CARD BOXES ON GRAY. Editorial layout. Plain-English evidence under every metric. Honest status — no fake greens. Left accent bars for priority, not full-tile backgrounds. Use `<details>` collapsibles for long explanations."

6. **Write the Stitch generation prompt using the copy-spec fenced format** (see `/audit-redesign` for the template). Every verbatim string — keyword names, evidence lines, quick-win action text, growth channel copy, chart annotations — MUST be fenced in triple-backticks with `DO NOT REWRITE`. Dashboard sections to generate:
   - Top preview ribbon ("PREVIEW — This is a vision of what ongoing site intelligence looks like for <prospect>")
   - Nav with wordmark ("<brand> intelligence")
   - AI scan hero: product image + findings panel (overall grade, category breakdown, key findings with accent bars)
   - Site Health: 4-tile grid with grades, no boxes, thin dividers
   - Keyword Rankings: branded pills + invisible list with 4px left accent bars
   - Search Interest: line chart with annotations (holiday spike, peak, current)
   - Content Pipeline: 6-week calendar mapped to invisible keywords
   - Quick Wins: 8-item honest checklist with effort estimates
   - Growth Channels: 3-card grid with collapsible `<details>`
   - CTA: ink-dark band, coral pill button

7. **Generate via `mcp__stitch__generate_screen_from_text`** with `modelId: GEMINI_3_1_PRO`. Call times out client-side after ~2min; generation continues server-side. Wait 3-5min, then `list_screens` — download the new screen's HTML and screenshot.

### Phase B — Agent ports to final dashboard

8. **MANDATORY: Spawn a general-purpose agent** with the prompt template below. Claude does NOT edit the dashboard HTML directly.

```
Rebuild dashboard-preview.html for <prospect>. Mode depends on AUDIT_USE_STITCH.

Mode:
- If AUDIT_USE_STITCH=1 AND prospects/<name>/stitch/dashboard-stitch.html exists: port Stitch skeleton to final HTML.
- Else (default): build from scratch using dashboard-spec.md + audit + branding + v1 reference (if prior runs exist). No skeleton to port.

Inputs:
- Design-library cues (source of truth for execution): prospects/<name>/dashboard-spec.md
  (includes `## Design Library References` with Dashboard-discipline + brand-vertical cues)
- Audit findings: prospects/<name>/audit.md
- SEO research: prospects/<name>/seo-research.md
- Branding: prospects/<name>/branding.json
- Scrape: prospects/<name>/scrape/ (source for asset URLs in no-Stitch mode)
- Stitch skeleton (only if AUDIT_USE_STITCH=1): prospects/<name>/stitch/dashboard-stitch.html
- v1 reference (if exists): prospects/<name>/mockups/v1-stitch/dashboard-preview.html OR v1-handbuilt/
- Assets dir: prospects/<name>/mockups/assets/ (download everything here)

V1-derived components (port into every dashboard, regardless of Stitch mode):
- Trends chart: use v1's SVG structure (data points must land on the line — Stitch and from-scratch both get this wrong without the v1 template).
- AI scan hero: v1's `.scan-line` (animated horizontal line), `.grid-overlay`, 4 `.corner-mark` brackets, `@keyframes scan` + `@keyframes gridPulse`. Port verbatim with the real product/interior image.
- Keyword layout: v1's `.kw-owned-grid` (branded pills with rank badges) + `.kw-invisible-list` (rows with 4px left accent bars and evidence lines).

Required (Stitch mode):
- Every Stitch placeholder `<img src="https://lh3.googleusercontent.com/...">` → assets/*

Required (no-Stitch mode):
- Dashboard-spec.md sections drive layout order. Design-library cues from spec drive palette accent, type, photography tone.
- Asset collection: parse scrape/*.md for image URLs, download to assets/, verify dimensions.

Required (both modes):
- Font stack: Inter-only verified (no Metropolis leakage)
- All collapsible `<details>` work on click
- Preview ribbon preserved verbatim
- Content + imagery: scraped interior/exterior > Yelp > stock. Never fabricate.
- Every client-facing string in plain owner-English. Translate jargon in-sentence or cut it.
- Policy Risk callout: omit for hospitality unless audit flagged a Google manual action.
- Responsive @media (max-width: 768px)
- No emoji. SVG icons only.

Output: prospects/<name>/mockups/dashboard-preview.html

After writing: spawn bb-quality agent to QA. Gate return on QA pass.
Return a ≤150-word summary + token count.
```

### QA (inside Phase B agent, runs before return)

9. QA agent validates:
   - Trends chart data points visually land on the line (verify via DOM — circle cx/cy match path coordinates)
   - Scan animation CSS is present and references `@keyframes scan`
   - All `<details>` elements functional
   - Every `<img src>` resolves to a real `assets/*` path — zero `lh3.googleusercontent.com` URLs
   - Fonts render as Inter (no fallback to system font)
   - 768px breakpoint works
   - Reads as the prospect: does it feel like THEIR brand energy, not generic tool?
   - Alignment: cite pixel x-coords from a 1440w screenshot for every section's gutters. CSS calc is not proof.
   - Scan-hero src resolves inside `scrape/screenshots/` or `mockups/assets/`, not Yelp/stock.
   - Every client string passes plain-English check — flag any undefined jargon (doorway/canonical/schema/crawler/SERP).
   - Policy Risk section absent for hospitality unless upstream audit flagged a Google manual action.

## Assumes

- **Expects:** `prospects/$NAME/audit.md`, `seo-research.md`, `branding.json`, product images at `prospects/$NAME/mockups/assets/`, `~/Documents/Claude/wiki/wiki/design-library.md` (design reference index).
- **Produces:** `prospects/$NAME/dashboard-spec.md` (design-library cues), `prospects/$NAME/stitch/dashboard-stitch.html` (skeleton), `prospects/$NAME/mockups/dashboard-preview.html` (final).
- **Quality bar:** A prospect should see THEIR brand in this dashboard. Data is specific, not templated. Honest status. Editorial, not SaaS.

## Dashboard Design Rules (these are sticky — learned from Pepper Pong walkthrough)

1. **No white card boxes on gray.** The single biggest thing that prevents "AI-generated" look. Editorial sections on white, thin horizontal dividers.
2. **All-Inter, all-weight.** No Montserrat, no geometric sans at heavy weight. h2 is Inter 600-700 at 20-24px, NOT oversized.
3. **Keyword presentation:** branded pills + invisible list with 4px left accent bars + evidence lines. No opportunity progress bars.
4. **Plain-English evidence under every metric.** "10 autocomplete suggestions for 'mini pickleball'" not "High search demand."
5. **AI scan hero:** real product photo OR pure dark canvas with ghost-wordmark placeholder, scan-line animation, grid overlay, 4 corner brackets. **NEVER use the prospect's own homepage screenshot as the scan-hero background** — webpage text inside the image visually collides with the findings panel text. Hierarchy: (a) real interior/food photo from client or clean scrape > (b) dark canvas + outlined ghost wordmark of the brand name > (c) pure-black canvas with just scan effects. Skip the homepage screenshot entirely.
6. **Honest status:** 0 of 8 quick wins = "0 of 8 done." Pipeline items all "planned" in gray. No fake green checkmarks.
7. **Chart annotations in white boxes** offset from the trend line — text overlapping lines is unreadable.
8. **Collapsible details for Growth Channels.** Card surface = icon + name + 1-line status + big metric. Details hidden in `<summary>Why this matters</summary>`.
9. **Scan-hero imagery prefers the prospect's own photography.** Site-scraped interior/exterior shots > Yelp food plates > bright fluorescent stock. Restaurants especially: dim editorial rooms over day-lit plates.
10. **Plain-English everywhere.** Every string a business owner reads — findings, labels, callouts, quick-wins — leads with what's broken and why it matters, not what the scanner measured. SEO jargon ("doorway pages", "canonical", "crawler access") either gets translated or stays out.
11. **Policy Risk section is severity-gated.** Omit for hospitality/restaurant prospects unless the upstream audit flagged a Google manual-action risk. When included, callout text must not duplicate Site Health + Quick Wins content.
12. **Letter grades (A/B/C/D/F with +/−), NOT numeric scores.** The scan-hero hero grade, the per-category breakdown rows, and the Site Health tiles all use letters. Numeric fractions (8/25, 65/100) look like academic test scores and are slow to read for a restaurant owner. Single-character grades in mono 18-48px with urgency color on failing grades (F/D magenta, C/B/A ink) read instantly and match editorial tone. The numeric score can appear ONCE, small, as supporting detail under the letter — never as the hero metric.
13. **Content Pipeline section is OPT-IN, not default.** Skip the 6-week editorial calendar unless the prospect has explicitly asked for a content strategy add-on. Prescribing 6 weeks of posts on a first-pass audit implies a commitment that the prospect hasn't agreed to. Leave the dashboard at: scan hero → Site Health → Keywords → Search Interest → Quick Wins → Growth Channels → CTA.
14. **Scan-visual must be width-capped, not full-bleed filled.** "Break to viewport left edge" ≠ "occupy the entire left column." Cap the scan-visual at ~420px width with `grid-template-columns: 420px 1fr;` + `padding-right: max(40px, calc((100vw - 1120px) / 2 + 40px));` on the grid, and `max-width: 394px; margin-left: auto;` on the findings panel. This gives editorial left-edge bleed while keeping at least 300-400px of breathing room between the visual's right edge and the panel's left edge at every breakpoint ≥1200px.

## Known Failure Modes

- **Stitch trends chart is broken.** Auto-generated dots don't land on the line — known Stitch limitation. Always port v1's SVG verbatim.
- **Opportunity progress bars.** Nobody intuitively reads "longer red bar = more search demand." Use colored accent indicators + plain-English evidence text.
- **Tiny product image.** 160x160 looks like a favicon. Hero product should be large and prominent.
- **Generic template.** Each prospect's dashboard needs its own personality. Phase 1 reads `wiki/wiki/design-library.md` — cues come from the prospect's brand vertical + the Dashboard entry, not the last prospect's look.
- **Hotlinked images.** Download everything to `mockups/assets/`. Dashboard must work offline.
