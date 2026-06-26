---
date: 2026-06-01
time: 17:04
project: vital-health-webflow-migration
status: failed-attempt
next-session: decide whether to extend `health-brand-intro-carousel` skill with a second arc (service-intro / paid-ad shape) and role-based layout types BEFORE attempting peptide carousel again, OR fork a sibling skill. The skill's current `render_slides.py` hard-codes the v5 brand-intro layouts and cannot produce format variety (packshot, explainer, mechanism diagram, protocol grid, testimonial, offer CTA) without engineering work.
---

# Session: Vital Health peptide therapy carousel — failed attempt

## What we worked on

Tried to build a 6-slide Instagram intro carousel for Vital Health's **peptide therapy** service, intended as the second-brand-validation case for the `health-brand-intro-carousel` skill (per the 2026-05-31-2056 checkpoint's open question).

Pipeline: confirmed audience (curious-but-uninformed, has heard "peptide" but doesn't know it), goal (educate / build authority), scope (broad intro), checked `snapshot/services.html` for what VH actually offers (BPC-157, CJC-1295, MOTS-c, Thymosin-α1, plus HGH / Cerebrolysin / LL-37 / Thymosin Beta-4).

Drafted v1 copy using skill defaults (italic-heavy editorial mold from v5). Annabel pushed back: "lean away from italic … hone in on switching things up and doing different things with ads … not always keep it so generic." Provided AG1 ($72 kit, Erica B testimonial, Sloane S testimonial), Ritual (Natalbiotic yellow packshot), and KLIK (comparison ad) as references, plus Simone Scrapes video on carousel variety within consistent brand chrome.

Synthesized refs into a redesigned 6-slide structure: packshot hero (Ritual) → icon-flow explainer (KLIK) → labeled mechanism diagram → AG1-style protocol grid → anonymized testimonial (no face) → offer CTA (AG1+Ritual). Annabel greenlit. Built slides 1–3 as bespoke HTMLs + a `review-batch1.html` (copied to Desktop).

Annabel correctly flagged: "you didn't use this skill for this i can tell."

I went bespoke because `render_slides.py` hard-codes the six v5 slide roles (`hero / why / first_visit / diagnostics / pull_quote / cta`) and there is no way to slot in alternate layouts (packshot, grid, testimonial-with-attribution-chip, etc.) without editing the skill's renderer. I read that as "skill can't do this, build around it" instead of "skill needs to be extended."

Annabel paused the build, asked for a failed-attempt checkpoint, and to delete the bespoke content.

## Decisions made (and reversed)

- **Reversed**: build bespoke, treat as "second-brand evidence" — Annabel correctly identified this defeats the skill's purpose. Bespoke means the skill learns nothing, and the next brand still starts from zero.
- **Carry forward**: peptide ad SHOULD have format variety per slide (packshot, explainer, mechanism, grid, testimonial, offer CTA). Not 6 italic-serif slides. The references (AG1 / Ritual / KLIK) and Simone Scrapes' thesis ("same fonts, accent colors, layout grids, but layouts vary") are the right north star.
- **Carry forward**: italic should appear at most once across the carousel, not 4-of-6 like v5.
- **New finding (architectural)**: the skill needs role-based layout types, not fixed slide positions. A `service-intro` arc needs to be able to say "slide 1 = packshot, slide 4 = protocol_grid, slide 5 = testimonial" via inputs.yaml. Currently impossible without script edits.

## Open questions

- **Extend the skill or fork it?** Option 1: add new slide-role types (`packshot`, `explainer`, `mechanism_diagram`, `protocol_grid`, `testimonial`, `offer_cta`) to `render_slides.py` + `photo-prompts.yaml`, let `inputs.yaml` map roles to slots. Option 2: fork a sibling skill `health-brand-service-carousel` for service-intro / paid-ad shape, leave `health-brand-intro-carousel` as the brand-intro-only skill. Option 1 is leaner but couples two arcs into one skill; option 2 is cleaner separation but duplicates the brand-context-reading scaffolding.
- **Should the testimonial role allow real photos** (with patient consent) or stay anonymized (no-face per skill's current photo rule)? VH may not have the source material either way — would need a real patient quote.
- **Slide count**: Simone Scrapes recommends 8–10 for the engagement sweet spot. The skill defaults to 6. Worth reconsidering as part of the extension work.
- **Per-brand visual identity consumption**: when extending the skill, should role layouts read MORE from `brand_context/visual-identity/moves.md` (e.g. "this brand uses sticker callouts" / "this brand uses serif quotes on plates") so the same role can render differently per brand?

## Next steps

1. Decide extend-vs-fork (the architectural question above) before any more peptide carousel work.
2. If extend: scope `render_slides.py` v2 — role-based dispatch, 6+ slide-role templates, inputs.yaml role-mapping schema. Write the spec doc first (matches the v5 → skill pattern that worked).
3. If fork: scaffold `health-brand-service-carousel` skill with the new role types from day one. Inherit brand-context reading scaffolding via shared helper or copy-with-attribution.
4. **Then** rerun the peptide carousel through whichever skill won — that's the actual second-brand validation, with real reuse evidence.

## Context to preserve

- **Brand context for VH peptide therapy is already gathered** (no rework needed next time):
  - VH peptide menu pulled from `snapshot/services.html`: BPC-157 (tissue repair), CJC-1295 (HGH support, sleep, recovery), MOTS-c (metabolism, endurance), Thymosin-α1 (immune regulation). Additional: HGH, Cerebrolysin (neuroplasticity), LL-37 (antimicrobial), Thymosin Beta-4 (wound healing).
  - VH site tagline for peptides: *"Targeting longevity, recovery, and vitality at the messenger level."*
  - VH framing: peptides are biologic messengers, work epigenetically, prescribed against labs/goals, never on assumption.
- **Reference set Annabel approved** (use again on next attempt):
  - Ritual Natalbiotic (packshot on saturated background)
  - AG1 $72 welcome kit (offer grid with struck-through prices)
  - AG1 Erica B + Sloane S (testimonial with plate quote + attribution chip)
  - KLIK camera (comparison ad with column structure)
  - Simone Scrapes video <https://youtu.be/REEzMNF54GY> — carousel-variety thesis
- **Voice direction from Annabel**: "lean away from italic" — at most one italic moment, not the v5 four-of-six pattern.
- **Slide 1 direction from Annabel**: lead with the WORD "peptides" as eye-catcher, not poetic abstraction. The Ritual packshot pattern fits this exactly.
- **Testimonial photo path chosen**: option (b) — anonymized (no face, hand on vial / hand at window). VH does not need to source real patient photos for this attempt.
- **Cost burned**: $0 — no photos generated this session, all work was HTML + planning.

## What was deleted (per Annabel's request)

All bespoke content created this session, removed at session end:

- `projects/00-social-content/claude/2026-06-01/vh-peptide-intro/` (entire folder: brief.md, slides 1-3 HTML, review-batch1.html)
- `~/Desktop/vh-peptide-intro-batch1.html`
- `~/Desktop/vh-peptide-intro-batch1-assets/` (entire folder)

No skill files were modified or created. The `health-brand-intro-carousel` skill is unchanged from its post-2026-05-31-2056-shipped state.

## Lineage chain

1. `2026-05-31-1829-vital-health-scrapes-carousel-pilot-paused.md` — Codex pilot paused
2. `2026-05-31-1854-vital-health-instagram-ad-brief.md` — creative brief intent
3. `2026-05-31-2015-vital-health-intro-carousel-v4-shipped.md` — v4 brand-intro shipped
4. `2026-05-31-2045-vital-health-intro-carousel-v5-shipped.md` — v5 brand-intro shipped + skill spec
5. `2026-05-31-2056-health-brand-intro-carousel-skill-shipped.md` — skill scaffolded + smoke-tested, open question "test on a second brand"
6. **This checkpoint** — first second-brand validation attempt FAILED at the architectural level (skill's renderer can't do format variety), build deleted, decision point identified

## System refinement candidates

- **NEW (architectural)**: the v5 → skill pipeline assumed every health brand would want the same brand-intro shape. False — the second use case (a SERVICE intro, not a BRAND intro) wants different layouts. Future skills that codify one hand-built reference should default to **role-based dispatch from day one**, not position-locked layouts. Even when v1 has only one arc, the renderer should be able to add arcs without re-architecting.
- **NEW (process)**: when the user describes the target as "switching things up and doing different things with ads," the right diagnostic is to **check the skill's flexibility surface BEFORE drafting copy or HTML**. If the skill can't produce the requested variety, the conversation should pivot to "extend the skill" not "build around the skill." This session inverted that order and burned a build.
- **NEW (feedback pattern)**: Annabel reliably catches "you didn't use the skill" within one batch. The cost of going bespoke is therefore at most one batch of work — but the better default is to never go bespoke in the first place if a skill exists for the format.
- Carried from v5: `00-social-content` hard gate is correct in principle, partially resolved by `health-brand-intro-carousel`, but the skill's flexibility limits (this session's finding) mean it still only covers one shape. Other shapes (service-intro, paid-ad, testimonial-led, FAQ-led) need their own arcs or skills.
- Carried from prior: `.env` `grep KEY=` is not proof a key is set (global rule, in `~/.claude/CLAUDE.md`). Not exercised this session because no photos were generated.
