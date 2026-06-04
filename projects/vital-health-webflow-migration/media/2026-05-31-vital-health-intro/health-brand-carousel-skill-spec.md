# `health-brand-intro-carousel` — Skill Spec

**Source**: consolidated from the v4 reusable-patterns notes + v5 corrections session.
**Goal**: turn the hand-built Vital Health intro carousel pipeline into a repeatable skill Annabel can run on any health / wellness / preventive-medicine brand and get a publish-ready 6-slide Instagram intro carousel.

This spec is the deliverable from the v5 session. It's the input for scaffolding the real skill at `~/Documents/AI-OS/skills/health-brand-intro-carousel/`.

---

## 1. What the skill does, in one sentence

> Given a brand context folder (with `voice-profile.md`, `positioning.md`, a website snapshot, and a visual-identity folder), generate a 6-slide Instagram carousel that introduces the brand: hero → why → first visit → diagnostics → philosophy → CTA. Output is 6 PNGs (1080×1350), a review HTML, and a `post.yaml`.

## 2. Inputs (the only things that change per brand)

Required:

- `brand_context_dir` — path to the brand's `brand_context/` folder containing:
  - `voice-profile.md` — how the brand sounds
  - `positioning.md` — the angle / promise
  - `snapshot/about.html` (or equivalent founder-story page) — real numbers, real story
  - `visual-identity/tokens.json` — colors, type scale, micro-rules
  - `visual-identity/logos/<brand>-mark.png` — small brand mark for CTA slide
- `brand_name` — e.g. "Vital Health"
- `primary_color`, `accent_color`, `cream_color`, `ink_color` — from tokens.json
- `cta_url` — e.g. "vitalhealthaustin.com"
- `cta_offer` — e.g. "Free 30-min call", "First consult on us"
- `founder_first_name` and `founder_credential` — e.g. "Dr. Swett", optional for pull-quote attribution

Optional:

- `display_serif_primary` — defaults to Fraunces
- `display_serif_secondary` — defaults to Cormorant Garamond (used on 2 of 6 slides)
- `body_sans` — defaults to Inter
- `output_dir` — defaults to `projects/00-social-content/claude/<date>/<slug>/`

## 3. The fixed arc (6 slides, in this order)

This arc is what made v3 onwards work. **Do not reorder, do not skip slides.** What changes per brand is the copy and the photo, not the structure.

| # | Role | Layout | What it says | Photo |
|---|---|---|---|---|
| 1 | **Hero** | Full-bleed photo + bottom-left headline + veil for legibility | Brand's preventive thesis in one line ("Medicine that catches it before it catches you.") | Person from behind, holding a warm drink at a window. Morning light. No face. |
| 2 | **Why / origin** | Split right-photo + left text block | Founder origin in one breath. Real number (years, patients, ER shifts). Display word = the contradiction the brand resolves ("preventable.") | Botanical still-life. Plants in window light. |
| 3 | **First visit** | Full-bleed photo + display word top-left | What makes their consult different. Specific minutes ("Ninety."). The display word IS the headline. | Top-down editorial still-life. Tea cup, paper card, brass pen, fresh herb. |
| 4 | **Diagnostics / measurement** | Split left-photo + right text block | What they test, how long it takes, how many people read it. Display word = the time scale ("weeks.") | Marble surface, amber glass vial, capsules, single leaf. |
| 5 | **Philosophy pull quote** | Full-bleed photo + opening quote glyph + literary italic quote | The brand's central line about relationship / care / philosophy. No attribution. | Wide outdoor landscape. Person walking away from camera, optionally with city/nature behind. Older patient ideal. |
| 6 | **CTA** | Full-bleed photo + centered cream typography + brand mark at base | Real low-friction first step. Display word = the offer ("Free."). NEVER "book your first consult." | Two hands meeting across a linen-draped table, hands only. Closing the loop visually with slide 1. |

## 4. What KEPT working across all 5 versions (defaults — bake into the skill)

| Pattern | Detail |
|---|---|
| Photographic vocabulary | Documentary still-life. Cream linen, growing plants, amber glass, marble, brass pen, natural window light. AI prompt ALWAYS includes "no faces, no readable text, no logos." |
| Aspect | 1080×1350 (4:5) Instagram carousel canvas |
| Composition pipeline | gpt-image-1 at 1024×1536 → embedded base64 into per-slide HTML → headless Chromium screenshot at 1080×1350. Text overlay is HTML, never baked into the AI image. |
| Brand chrome | Brand serif headlines, body sans (Inter), brand-token palette, ONE accent micro-rule per slide, brand mark on CTA slide only |
| Layout diversity rule | No two slides share a layout. Mix full-bleed, split-photo-left, split-photo-right, pull-quote, oversized-display. |
| Claude-namespaced output folder | `projects/00-social-content/claude/<date>/<slug>/` so Codex's parallel runs don't collide |

## 5. Failure modes to avoid (consolidated from all 5 versions)

### Photography vibe (v1 → v2)

- **Preventive-medicine brands = BRIGHT.** Morning light, growing plants, movement/outdoors, openness. Save intimate/moody stillness for chronic-care / hospice / therapy brands.
- **ONE motif per carousel.** If the brand has an intake form / supplement / device, show it on ONE slide, not as decoration on every slide. (Paper/card was on 4 slides in v1, killed to 1 slide in v2+.)

### Copy (v2 → v3)

- **NEVER draft from generic functional-medicine vocabulary.** Always read the brand's actual `snapshot/about.html`, `positioning.md`, and `voice-profile.md` BEFORE writing a single headline. Borrow founder story + real numbers + real CTA language verbatim.
- **Patient representation:** mix gender and age across the carousel. At least one older patient (50s+) is mandatory for preventive-medicine brands because the ICP skews older.

### Brand chrome duplication (v3 → v4)

- **Brand chrome ≠ duplicated identifier strings.** If a masthead says brand+city, the bottom slot is NOT "brand · city" again. URL alone, salute, or nothing.
- **Vary the architecture per slide:** oversized italic display words, asymmetric photo-left vs photo-right, pull-quote treatment, full-bleed alternating with split. Same chrome rhythm on every slide = templated and dead.

### Brochure-TOC kickers, fake attributions, font monotony, legibility (v4 → v5)

- **Drop chapter-kicker meta-labels** ("01 · Why X", "02 · On your first visit"). They make a 6-slide carousel feel like a TOC for a brochure. The display word carries the slide identity.
- **No fake pull-quote attributions.** "The house style of X" / "The X way" / etc. all read as brand-book filler. Either attribute to the founder by name (if it's truly her voice) or drop the attribution entirely.
- **Vary the display serif on 2 of 6 slides** with a close cousin (Cormorant Garamond italic pairs with Fraunces). Keep body sans constant. Otherwise the carousel reads as a template even when layouts vary.
- **TEXT-ON-PHOTO LEGIBILITY (caught twice in v5):** any text element <24px sitting on a photo without a solid plate, dark veil, or guaranteed dark region behind it WILL fail. Pre-ship checklist: audit every text element <24px. If it's on photo and has no plate/veil/dark region, give it one OR delete it. **Default to deletion for secondary copy.**

## 6. Voice rules (apply to every line of copy the skill generates)

- No em-dashes / en-dashes. Replace with periods or commas.
- No "miracle / cure / guaranteed / reverse / melt / biohack" claim language.
- Quiet confidence > hype. Short sentences. Plain words.
- Always end with a soft next step.
- "Whimsical" = italic accent words + asymmetric placement + display-word size variation, NOT hand-drawn or playful illustration.

## 7. Pre-ship checklist (skill MUST run this before declaring done)

The skill should run this as an automated audit step (or surface it as a manual checklist if automation isn't worth it):

- [ ] No two slides share the same layout (count: full-bleed, split-left, split-right, pull-quote, oversized-display — at least 3 distinct layouts across 6 slides)
- [ ] No two slides share the same display serif on identical layouts (run the alternate serif on at least 2 slides)
- [ ] Body sans is constant across all 6 slides
- [ ] Brand mark appears on slide 6 ONLY
- [ ] No "Austin · Brand · Year" style masthead appears twice (once or never)
- [ ] Every text element <24px sits on a solid color region, a veil, or a guaranteed dark region (NOT raw photo)
- [ ] No em-dashes or en-dashes in any copy
- [ ] No claim words (miracle / cure / guaranteed / reverse / melt / biohack)
- [ ] No "01 · X", "02 · Y" chapter-kicker labels
- [ ] No "the house style of X" or fake brand-book pull-quote attributions
- [ ] CTA slide uses real low-friction offer language (NOT "book your first consult")
- [ ] Photo prompts all include "no faces, no readable text, no logos"
- [ ] At least one older patient (50s+) represented across the carousel if the brand is preventive-medicine

## 8. Cost envelope (for skill quoting)

- ~$0.40 for 6 gpt-image-1 high-quality renders at 1024×1536
- ~$0.30 typical iteration cost across 2–3 photo regens
- Wall time: ~10–15 min per version once API key is set
- One-time setup (per project): venv + chromium ~3 min

## 9. Recommended skill folder shape

```
~/Documents/AI-OS/skills/health-brand-intro-carousel/
├── SKILL.md                     ← skill entrypoint (Claude reads this on trigger)
├── README.md                    ← human-facing overview
├── scripts/
│   ├── render_slides.py         ← parameterized port of v5 _workdir/render_slides.py
│   ├── generate_photos.py       ← wraps viz-image-gen with the 6 fixed prompts
│   ├── build_review.py          ← unchanged from v5
│   └── preship_audit.py         ← runs the checklist from §7
├── templates/
│   ├── slide-1-hero.html.tmpl
│   ├── slide-2-why.html.tmpl
│   ├── slide-3-first-visit.html.tmpl
│   ├── slide-4-diagnostics.html.tmpl
│   ├── slide-5-pull-quote.html.tmpl
│   └── slide-6-cta.html.tmpl
├── prompts/
│   └── photo-prompts.yaml       ← 6 base prompts with brand-substitutable fields
└── examples/
    └── vital-health/             ← copy of the v5 inputs + outputs as reference
```

### What's templated (changes per brand)

- All copy strings (display words, sub-lines, CTA offer)
- Color tokens (primary, accent, cream, ink, deep-forest, muted, line)
- Brand mark (PNG path)
- CTA URL
- Founder name (for optional pull-quote attribution)
- Photo prompts can be tuned (style suffix is brand-configurable, e.g. "warm forest-green palette" → "cool clinical-blue palette" for a different brand)

### What's hard-coded (the skill's opinion)

- The 6-slide arc and slide roles
- The layout assignments per slide
- The font pairing (primary serif + close-cousin secondary serif + Inter)
- The 2-of-6 alt-serif rule
- The legibility audit
- The voice rules
- The cost-saving choice of gpt-image-1 over flux/midjourney

## 10. Open questions before scaffolding

1. **Skill or tool?** A Claude skill (markdown SKILL.md + scripts) fits AI-OS conventions and is what Annabel triggers via `/health-brand-intro-carousel`. A tool (just a CLI script) is leaner but doesn't get the trigger-phrase ergonomics. **Recommendation: skill.**
2. **Single skill or chain?** This skill does photo gen + composite + review. We could split photo gen out as a sub-skill (`tool-carousel-photo-gen`) for reuse. **Recommendation: single skill for v1, refactor if a second skill needs the same photo pipeline.**
3. **Template the 6 photo prompts or let user write them?** v5 used hand-written prompts in `plan.md`. For Vital Health they worked. Generalizing them means parameterizing brand vocabulary (e.g. "forest-green" → primary color name). **Recommendation: parameterize the style suffix, keep the still-life subjects fixed (tea cup, brass pen, amber glass, marble, etc.) since they're brand-agnostic.**
4. **Should the skill enforce the arc, or allow slide-swapping?** Annabel may want to swap slide 5 (philosophy) for a slide about pricing, for instance. **Recommendation: enforce the arc for v1; add `--arc-overrides` flag if she needs flexibility later.**

## 11. Next action

**Annabel reads this spec, then green-lights (or amends) the recommended skill shape in §9 and the answers in §10.** Once approved, scaffolding the skill is a ~30 min job: port `render_slides.py` to the templated form, write SKILL.md, copy v5 as the `examples/vital-health/` reference, write `preship_audit.py`, smoke-test on Vital Health to confirm parity.
