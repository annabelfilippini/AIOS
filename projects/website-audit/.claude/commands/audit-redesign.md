# /audit-redesign — Design Critique + Homepage Mockup

Build an HTML mockup that fixes specific audit findings while elevating — not erasing — the brand's identity. Audit drives what to fix. Reference sites teach execution, never identity.

**Usage:** `/audit-redesign <prospect-name>`

## Modes
- `/audit-redesign <name>` → interactive (default). Main session opens the file once at the end.
- `AUDIT_AUTOMATED=1 /audit-redesign <name>` → unattended. No `open` calls, no confirmations, file output only.
- `AUDIT_USE_STITCH=1 /audit-redesign <name>` → opt-in Stitch skeleton pass (Phase 2). Default OFF per Apr 16 2026 decision — Phase 3 builds directly from copy spec + design-library cues + audit + scrape. Re-enable only if no-Stitch quality tanks.

## Phase 0: Scope & Prereq Gate (required, output before anything else)

**Scope statement.** Output: (a) prospect name, (b) which audit findings are in scope, (c) what's explicitly out, (d) mode (interactive or automated), (e) Stitch (ON if `AUDIT_USE_STITCH=1`, else OFF — default). Do not proceed until user confirms in interactive mode.

**Prereq check — FAIL FAST if any missing.** Three prereqs must pass before Phase 1. Stop and tell the user to re-run `/audit-scrape` — do not paper over mid-redesign (Hop Alley v1 lesson).
1. `prospects/<name>/branding.json` — Stitch design system needs real brand tokens.
2. `prospects/<name>/facts/verified-facts.md` — canonical list of every fact allowed in the mockup.
3. **Reference signal — either of:**
   a. `prospects/<name>/reference/<brand>/` with scraped content (full case — preferred for fresh Stitch generation, ideally 2-3 for restaurants/local), OR
   b. `prospects/<name>/reference/reference-summary.md` with ≥1 ref block (breadcrumb case — acceptable for re-runs on shipped prospects where `/audit-cleanup` pruned the scrapes). Summary-only runs proceed with a WARN: Stitch generation loses photography cues; light iteration OK, fresh mockups should re-scrape.

If missing, output verbatim: "Stop — `/audit-scrape` did not produce [X]. Re-run `/audit-scrape <name> <url> --ref <ref-url>` before proceeding." Do NOT scrape inline.

## Phase 1: Brand DNA + Section Plan

1. Read `prospects/$NAME/audit.md`, `design-critique.md` (if exists), `scrape/screenshots/`, `branding.json`, `reference/`.
2. **Design library lookup.** Read `~/Documents/Claude/wiki/wiki/design-library.md`.
   - Identify vertical (restaurant / DTC / luxury / portfolio / personal-brand / editorial / dashboard / annabel).
   - Open that vertical's **Primary refs** (URLs + `raw/` files listed). For restaurants, include the inline redesign mapping if one exists (e.g., Hop Alley → Fat Cow / Atomix / Cosme).
   - If vertical status is GAP or PARTIAL, flag it explicitly — do NOT default to generic SaaS layouts.
   - Extract 3-5 execution cues (hero, type pair, social-proof, motion, palette discipline) + 2-3 anti-patterns to avoid.
   - Write them into `redesign-spec.md` under a `## Design Library References` header before the section inventory. This section is the execution guide for Phase B (and Phase 2 Stitch, while Stitch is still in the loop).
3. **Identify brand DNA.** List signature elements explicitly: color usage, typography, voice, hero treatment, social proof pattern, motion. These MUST survive the redesign. If the reference site dominates over brand DNA in the final mockup, start over.
4. **Section inventory as copy spec.** Every section maps to a specific audit finding (for internal context — do NOT render audit-tag pills on the final mockup, see Phase 3). Every verbatim string (customer quotes, headlines, step labels, names) wrapped in triple-backticks with comment `DO NOT REWRITE THIS — COPY EXACTLY`. Unfenced text gets paraphrased by Stitch.
5. **No fact in the spec that isn't in `verified-facts.md`.** Missing facts → softer non-specific language ("open daily" vs invented hours). No fabrication.
6. **Menu destination.** If the prospect has (or will have) a downloadable menu, every "Menu" / "See the menu" CTA in the spec targets `assets/<slug>-menu.pdf` with `target="_blank"`. Never point menu CTAs at an on-page photo grid — the grid is a teaser, the PDF is the menu.
7. **Founder / chef portraits.** If `verified-facts.md` or `scrape/` does NOT surface a real portrait photo of the named founder/chef, the spec calls for a **portrait placeholder** in that slot — never substitute a bar/interior/food shot. Placeholder copy names the person and flags "photo to be provided by client."

Save spec to `prospects/$NAME/redesign-spec.md`.

## Phase 2: Stitch Generation (opt-in, default OFF)

**Gate:** Run this phase ONLY when `AUDIT_USE_STITCH=1`. If unset or `0`, skip steps 5-10 entirely and proceed to Phase 3's no-Stitch branch. This is the default per Apr 16 2026 decision — design-library cues in `redesign-spec.md` replace Stitch as the visual anchor.

5. **Create project** via `mcp__stitch__create_project` with `title: "$NAME Audit Redesign"`. Save project ID.
6. **Create design system** via `mcp__stitch__create_design_system`:
   - `headlineFont`: closest in enum (Metropolis≈Gotham, DM Sans≈Proxima/Helvetica Now, Space Grotesk≈modern geometric, Newsreader≈editorial serif).
   - `bodyFont`: INTER unless `branding.json` says otherwise.
   - `customColor` + `override*Color`: from `branding.json`.
   - `roundness`: ROUND_FULL (pill), ROUND_EIGHT (standard), ROUND_TWELVE (soft cards).
   - `colorVariant`: VIBRANT (bold), NEUTRAL (editorial), TONAL_SPOT (muted).
   - `designMd`: brand personality + DO/DON'T + voice. Embed the "constitution."
7. **Generate screen** via `mcp__stitch__generate_screen_from_text` with `modelId: GEMINI_3_1_PRO`, `deviceType: DESKTOP`. Use the copy spec as the prompt.
8. **Async pattern** — the call times out client-side at ~2 min, server job continues. Do NOT retry (spawns duplicate). Poll via `mcp__stitch__get_project` (`updateTime` changes first) then `mcp__stitch__list_screens` (new screen appears after). Typical wait: 3-5 min. Work on other things while polling; never `sleep` as a blocking wait.
9. **Always follow first generation with cleanup edit** via `mcp__stitch__edit_screens`: `"Remove any duplicate headers or nav bars — the page should have exactly one nav above the hero."` Stitch stacks navs on iteration.
10. **Review screenshot.** Iterate via `edit_screens` (targeted, faster) or `generate_variants` with `creativeRange: REFINE` (subtle tweaks).

## Phase 3: Agent Assembles Final HTML (MANDATORY DELEGATION)

**Hard rule: Claude does NOT hand-edit layout HTML in the main session.** Hand-building a 1,200-line mockup burns hundreds of thousands of tokens — #1 usage sink in the pipeline. If you catch yourself running `Edit`/`Write` on `prospects/*/mockups/*.html` in the main session, stop and spawn the agent.

**Two branches depending on `AUDIT_USE_STITCH`:**

### Branch A — Stitch ran (`AUDIT_USE_STITCH=1`)

11A. Download Stitch HTML → `prospects/$NAME/stitch/homepage-stitch.html` and the screenshot.
12A. Download assets → `prospects/$NAME/mockups/assets/` (hero @ `width=1920`, press logos at `h_60` PNG, no hotlinking).

### Branch B — No Stitch (default)

11B. **No skeleton to port.** Phase B agent builds from `redesign-spec.md` (section inventory + design-library cues), `audit.md`, `facts/verified-facts.md`, `scrape/`, and `reference/reference-summary.md` (if present).
12B. **Asset sourcing by agent (not this phase):** agent collects imagery from, in priority order:
    a. Image URLs embedded in `prospects/$NAME/scrape/*.md` + `scrape/*-metadata.json` (prospect's own pages).
    b. The prospect's live site via direct URL fetch (when scrape markdown references remote CDN paths).
    c. `prospects/$NAME/reference/<brand>/` if full scrapes exist (rare after cleanup).
    All downloaded to `prospects/$NAME/mockups/assets/`. Never hotlink.

### Both branches

Verify each image before placing:
  - **Appetite / appeal test (restaurants + food verticals):** shortlist 3-4 candidates for hero + feature slots, pick the most visually appealing to a first-time visitor. "Real" is necessary but not sufficient. Muddled molcajetes, murky ceviches, plated ingredients that read as "shrimp + guac" to a stranger — skip in favor of clean signature shots (al pastor with pineapple, carne asada, queso fundido bubbling, street tacos). When in doubt, prefer a single hero dish over a group/composite plate.
  - Product/hero subject clearly visible (not secondary in group shot)
  - `sips -g pixelWidth -g pixelHeight` → native width ≥ rendered CSS width (~1400px full-width desktop)
  - Aspect ratio matches container (landscape strips, square/crop-safe for cards)
  - Missing image beats blurry/miscropped image
  - **Founder/chef portrait rule:** if no real portrait photo of the named person exists in scrape or assets, render a styled placeholder (dashed border, person's name, "Portrait to be provided by client" note). NEVER substitute an interior/bar/food shot into a portrait slot — the viewer will read it as mislabeled.

13. **Spawn Phase B agent** via `Agent` tool with `subagent_type: general-purpose`. Token budget: ≤200K tokens per agent run (no-Stitch runs estimate 200-300K; split if a single agent exceeds — homepage-then-dashboard, or section A then B).

### Phase B Agent Prompt Template

```
Rebuild homepage-redesign.html for <prospect>. Mode depends on AUDIT_USE_STITCH.

Mode:
- If AUDIT_USE_STITCH=1 AND prospects/<name>/stitch/homepage-stitch.html exists: port Stitch skeleton to final HTML.
- Else (default): build from scratch using the copy spec + design-library cues + audit + scrape. No skeleton to port.

Inputs:
- Copy spec (source of truth): prospects/<name>/redesign-spec.md
  (includes `## Design Library References` section with vertical-specific execution cues + anti-patterns)
- Verified facts: prospects/<name>/facts/verified-facts.md (nothing outside this enters the mockup)
- Audit findings: prospects/<name>/audit.md
- Branding: prospects/<name>/branding.json
- Scrape: prospects/<name>/scrape/ (source for asset URLs in no-Stitch mode; read *.md + *-metadata.json)
- Reference breadcrumb: prospects/<name>/reference/reference-summary.md (high-value pre-digested cues when full scrapes were pruned)
- Stitch skeleton (only if AUDIT_USE_STITCH=1): prospects/<name>/stitch/homepage-stitch.html
- v1 reference (if exists): prospects/<name>/mockups/v1-handbuilt/*.html OR v1-stitch/*.html
- Assets dir: prospects/<name>/mockups/assets/ (download everything here)

Required (Stitch mode):
- Every Stitch placeholder img (lh3.googleusercontent.com, gstatic.com/stitch) → assets/*
- Stitch font enum → brand's real font stack via @font-face or Google Fonts

Required (no-Stitch mode):
- Every section in redesign-spec.md becomes a real <section> in spec order
- Asset collection: parse scrape/*.md for image URLs (markdown image syntax + raw <img> tags), download to assets/, verify dimensions
- Design-library cues from redesign-spec.md drive hero pattern, type pair, social-proof treatment, motion, palette discipline — not a generic template
- Reference-summary.md takeaways (if present) override library URL-level cues for this prospect

Required (both modes):
- Every `DO NOT REWRITE:` fenced string appears verbatim (casing, punctuation, em-dashes)
- Static HTML → motion (marquee scroll, UGC autoplay, hover states) where brand warrants
- **NO audit-tag pills** on the final mockup. The deliverable is the redesigned site, not a diff view — clients don't need to see what changed, just the new experience. Audit findings drive the spec (what to fix) but never render as on-page annotations.
- **Menu CTAs link to the PDF**, not on-page anchors. Every "Menu" / "See the menu" href targets `assets/<slug>-menu.pdf` with `target="_blank" rel="noopener"`. If the client hasn't supplied the PDF yet, still use the path (file will 404 until they drop it — the structure is right). On-page dish grids are teasers/visual features, not menu replacements.
- **Founder/chef portrait placeholder** when no real photo exists (see Phase 3 image-verification rules above). Dashed border, person's name, "Portrait to be provided" note. Never a stand-in interior/bar shot.
- Responsive @media (max-width: 768px)
- NO fact appears in the mockup that isn't in verified-facts.md
- No emoji. SVG icons only.

Browser discipline (strict):
- Playwright calls MUST be headless. Never open a visible browser.
- Never run `open <file>` from inside the agent.

Output: prospects/<name>/mockups/homepage-redesign.html

After writing, spawn QA agent (subagent_type: bb-quality, or general-purpose) with the Phase 4 checklist below. Iterate until green. Do NOT return until QA is green.

Return ≤200-word summary: what was built + open issues + token count.
```

## Phase 4: QA Gate (MUST be green before Phase 5)

**QA is authoritative inside the Phase B agent.** The Phase B agent spawns a QA subagent, iterates the checklist below until green, and only then returns. The main session does NOT spawn a second independent QA agent by default.

If the Phase B agent returns "PASS-WITH-NOTES" or similar amber, the main session's job is a ~2-minute grep-based spot-check (banned strings, verbatim spec strings present, no hotlinks, no emojis) — not a full re-run of A1–G22. A second independent QA agent is only warranted when:
- Phase B returned amber and the main session's spot-check flags something Phase B missed, OR
- The user explicitly asks for a second opinion.

**Cost lesson (Miss Kim, Apr 19 2026):** spawning a full independent QA agent after the Phase B agent had already self-QA'd took 42 minutes to catch one casing fix. Trust the self-QA; verify with grep in the main session; escalate to a second agent only on real amber.

QA runs at 1440px AND 768px.

**A. Content integrity**
1. Every `DO NOT REWRITE:` fenced string appears byte-for-byte (em-dashes, casing, `¿?¡!`).
2. No fabricated facts. Grep for: `since 20XX`, phone numbers, addresses, prices (`$N`, `$NN`), testimonials. Cross-reference against verified-facts.md. Any miss = P0.
3. No Stitch placeholder URLs (`lh3.googleusercontent.com`, `gstatic.com/stitch`).
4. No emoji characters anywhere. SVG icons only.
5. Social icons are inline SVG (Instagram, Facebook, TikTok, YouTube) — not "IG/TK/FB" text, not emoji.

**B. No audit annotations**
6. Zero audit-tag pills on the final mockup (grep for `audit-pill`, `audit-row`, `Fix ·`, `New ·`, `Signature ·` — any hit is a P0). The deliverable is the redesigned experience, not a diff.
7. Zero "before/after" labels, "changed:" comments, or audit-finding callouts rendered in the DOM.
8. Menu CTAs (nav "Menu", hero "See the menu", menu-foot "See the full menu") all point to `assets/<slug>-menu.pdf`, never to an on-page anchor like `#menu`.

**C. Alignment to neighbors**
9. Announcement bar shares horizontal gutters with nav directly below (≤2px drift).
10. Hero/headlines/footer columns share consistent max-width container. No section silently full-bleed.
10a. Cite pixel x-coords from 1440w screenshot for each section's left/right gutters. CSS calc is not proof.

**D. Section proportions**
11. No single section >2x vertical space of neighbors (excluding hero).
12. Chef/founder portraits ≤35% of two-column width, aspect ~3:4.
13. Hero ≤100vh. No 2000px midpage sections without content justification.

**E. Image quality**
14. Every image loads (no 404s, no broken icons, no white boxes on colored bars).
15. Native pixel width ≥ rendered CSS width on every image.
16. Aspect-ratio match: landscape sources for full-width strips, crop-safe images in card grids.
16a. **Appeal check:** hero + feature images are a first-time visitor's most appetizing option from the shortlist. Muddled composites (sizzling molcajetes with mixed meats + green garnish reading as "shrimp + guac"), brown/smothered close-ups as hero, or images where the hero dish is secondary in the frame → P0.
16b. **Portrait-slot check:** founder/chef portrait slots either contain a real portrait of the named person OR the styled placeholder. A bar/interior/food shot in a portrait slot = P0 (viewer reads it as mislabeled).

**F. Structural**
17. Exactly ONE nav above hero. No stacking.
18. All sections from redesign-spec.md present in spec order.
19. Every primary CTA's href resolves (reservation CTAs → real OpenTable/Resy, menu CTAs → real menu, location CTAs → real maps).
20. Responsive at 768px: two-column stacks, card grids collapse, nav condenses to SVG hamburger.

**G. Motion**
21. Hover states on CTAs render.
22. Advertised motion (marquee, autoplay video, smooth scroll) actually works.

**Reporting:** pass/fail per check with line numbers or selectors. Partial failure ≠ pass. QA iterates until green.

## Phase 5: Present

23. **Interactive mode:** main session calls `open <abs-path>` exactly ONCE after Phase 4 is green. Do not re-open after iterative fixes unless the user asks.
24. **Automated mode (`AUDIT_AUTOMATED=1`):** skip `open` entirely. Wrapper surfaces results via files + deployed URL.

## Phase 6: Completion Gate (must pass to declare done)

- [ ] Phase 0 scope confirmed (interactive) or mode logged (automated)
- [ ] Prereq gate passed — branding.json + verified-facts.md + reference/ all present
- [ ] Copy spec exists at `redesign-spec.md` with every verbatim string fenced
- [ ] Phase B ran as an agent, not in main session
- [ ] Phase 4 checklist all green (A1–G22)
- [ ] Exactly one `open` call (interactive) or zero (automated)
- [ ] Mockup output exists at `prospects/<name>/mockups/homepage-redesign.html`
- [ ] All assets local at `prospects/<name>/mockups/assets/` (zero `lh3.googleusercontent.com`, zero hotlinks)

If any unchecked → output "REDESIGN INCOMPLETE" and list what's missing. Do not say "ready" or "shipped."

## Stitch Prompt Template (copy-spec format)

Every section gets a field list. Verbatim strings fenced.

```
=== SECTION N: [NAME] ===
Layout: [one-line visual description]
Eyebrow: `DO NOT REWRITE: "<exact text>"`
Headline: `DO NOT REWRITE: "<exact text>"`
Subhead: `DO NOT REWRITE: "<exact text>"` (or free description if paraphrase OK)
Body: <free description>
CTA: `DO NOT REWRITE: "<exact button text>"`
Audit finding (internal — do NOT render on mockup): "Audit #N — what this section fixes"
Image: <description>
```

Example — testimonial card:
```
=== SECTION: WHERE WILL YOU RALLY ===
3-card grid. Each card: photo top, content bottom.
Card 1:
  Label: `DO NOT REWRITE: "Girls Trips"`
  Quote: `DO NOT REWRITE: "I packed it in my suitcase on a girls trip. Once we started playing, it's all we wanted to do. Every night!"`
  Attribution: `DO NOT REWRITE: "— Wendy S."`
  Image: friends playing Pepper Pong on vacation
```

Fencing verbatim copy eliminated ~70% of Pepper Pong's iteration cycle.

## Do Not

- Do not hand-edit layout HTML in the main session. Agent-only. (One-line bug fixes that are obvious text-strip / text-substitute edits — e.g., removing a stray class, fixing a casing issue — are fine in the main session. "Hand-editing" here means authoring or restructuring layout.)
- Do not run `open` inside any subagent. Main session, once, at the end.
- Do not call Playwright without `headless: true` inside an agent.
- **Do not use `sips --cropOffset` in the main session to slice agent-produced screenshots.** It misbehaves on macOS and wastes a handful of tool calls. If you need a specific section of a screenshot, ask the producing agent to crop it and return the path — they have the page layout context.
- **Do not use `ScheduleWakeup` to poll a scrape that runs <5 min.** Foreground the Bash call, or if backgrounded, wait for the completion notification. Cache-miss overhead from multi-minute wakeups exceeds the scrape itself.
- **Do not use `TaskCreate` for phases this skill already names.** The skill phases (0, 1, 2, 3A/B, 4, 5, 6) are the tracker. A parallel task list duplicates structure without adding information.
- Do not paraphrase verbatim copy — fence it.
- Do not invent specifics (hours, prices, years, names). Verify or remove.
- Do not use emojis on mockups. SVG only.
- **Do not render audit-tag pills, "before/after" labels, or diff annotations on the mockup.** The deliverable is the new site, not a changelog.
- **Do not point menu CTAs at on-page anchors** (`#menu`). Menu = PDF, always.
- **Do not drop a bar/interior/food shot into a chef/founder portrait slot.** Use a styled placeholder when no real portrait exists.
- Do not pick the "most real" image when "most appetizing" disagrees — shortlist, choose appeal.
- Do not ship with `lh3.googleusercontent.com` URLs remaining.
- Do not let the reference site become the identity. Elevate, don't erase.
- Do not retry timed-out Stitch calls — poll instead.
- Do not return "pass" on partial QA failure.

## Known Failure Modes

- **Unfenced copy gets paraphrased** — fence every verbatim string.
- **Duplicate nav bars after `edit_screens`** — always follow with the cleanup edit.
- **No motion in Stitch output** — Phase B wires marquee/autoplay/hover.
- **Limited font enum** — Phase B swaps to real stack via `@font-face`.
- **Google CDN image URLs expire** — Phase B swaps every `<img>` src to local assets.
- **Reference site becomes identity** — if mockup looks more like reference than prospect, start over.
- **Hero image doesn't show product** — download multiple candidates, verify visually.
- **Emojis / text social icons** — SVG brand icons only.
- **Press logos render as white boxes** — wrong format, opaque bg, or corrupt file. Use `filter: brightness(0) invert(1)` for white-on-red.
- **Image aspect ratio vs. container** — `sips -g pixelWidth -g pixelHeight` before placing; native width ≥ rendered CSS width.
- **Bot walls on OpenTable/Google** — Yelp + prospect's own site + Step 2 press usually fills the gap.

## Assumes

- **Expects:** `prospects/$NAME/audit.md` from `/audit-analyze`, `branding.json` + `facts/verified-facts.md` + `reference/` from `/audit-scrape`, screenshots at `prospects/$NAME/scrape/screenshots/`, `~/Documents/Claude/wiki/wiki/design-library.md` (design reference index).
- **Produces:** `prospects/$NAME/redesign-spec.md` (with `## Design Library References`), `prospects/$NAME/mockups/homepage-redesign.html`, `prospects/$NAME/mockups/assets/`. If Stitch ran: also `prospects/$NAME/stitch/homepage-stitch.html`.
- **Quality bar:** A prospect should see their brand — elevated, not replaced. Every design change traces to a specific audit finding. No broken images. No fabricated facts. No emojis.
