---
date: 2026-05-31
time: 20:45
project: vital-health-webflow-migration
status: in-progress
next-session: scaffold the `health-brand-intro-carousel` skill at `~/Documents/AI-OS/skills/health-brand-intro-carousel/` from the consolidated spec at `projects/00-social-content/claude/2026-05-31/vh-intro-carousel/health-brand-carousel-skill-spec.md`. Then re-run the pipeline through the skill on Vital Health to confirm parity, then test it on a second health brand.
---

# Session: Vital Health intro carousel v4 → v5 shipped + skill spec

## What we worked on

- Re-read v4 checkpoint (Annabel had added a substantial "Reusable patterns for a future `health-brand-intro-carousel` skill" section — what kept, what corrected, the arc, voice rules, cost, skill-name suggestion).
- Took v4 → v5 with four corrections:
  1. **Dropped chapter kickers** on slides 2/3/4 ("01 · Why Vital Health", "02 · On your first visit", "03 · How we measure"). They read as a brochure TOC for a 6-slide carousel.
  2. **Dropped pull-quote attribution** on slide 5 ("The house style of Vital Health"). Fake brand-book attribution. Quote stands on its own.
  3. **Varied display serif on 2 of 6 slides**: added Cormorant Garamond italic for slides 3 ("Ninety.") and 5 (pull quote). Slides 1/2/4/6 stay Fraunces. Brand still reads coherent; no two adjacent slides share the exact display face.
  4. **Removed two small-text-on-photo legibility failures**: the slide 3 bottom sub ("Not fifteen. Not twenty. Long enough to actually listen.") and the slide 1 top kicker ("A note from Vital Health"). Same failure mode, caught twice in this build.
- Source-of-truth edits all made in `_workdir/render_slides.py` (NOT just the rendered slide HTMLs) so re-renders don't reintroduce the problems.
- Added v4→v5 row to the "What Annabel CORRECTED" table in the v4 checkpoint, including the **TEXT-ON-PHOTO LEGIBILITY** generalized rule.
- Wrote consolidated skill spec at `projects/00-social-content/claude/2026-05-31/vh-intro-carousel/health-brand-carousel-skill-spec.md` — merges v4 reusable-patterns notes + v5 corrections into one buildable doc, recommends skill folder shape, lists what's templated vs hand-edited.

## Decisions made

- **Font variety rule**: vary the display serif on ~2 of 6 slides with a close cousin (Cormorant Garamond italic pairs with Fraunces). Keep the body sans (Inter) constant across the carousel. Don't swap brand chrome (logos, wordmark, color palette).
- **No fake attributions** on pull-quote slides. Attribute to the founder by name (if it's truly her voice), or drop the attribution entirely.
- **No chapter-kicker meta-labels** ("01 · Why X") on intro carousels. The oversized italic display word already gives each slide its identity.
- **Pre-ship legibility audit is mandatory**: any text <24px on a photographic background needs a solid-color plate, a veil/gradient, or a guaranteed dark region behind it. Default to deletion for secondary copy.
- The pipeline is mature enough to become a reusable skill named `health-brand-intro-carousel`. Spec doc shipped; scaffolding deferred to next session pending Annabel's blessing of the shape.

## Open questions

- **Skill shape green-light**: scaffold as a Claude skill at `~/Documents/AI-OS/skills/health-brand-intro-carousel/` with SKILL.md + parameterized `render_slides.py` + `plan-template.md` + an inputs YAML, or a leaner tool-script?
- Which second health brand do we test the skill on first to validate it generalizes? (Candidate: any peptide / health & wellness client Annabel has lined up.)
- Promote v5 6 slide HTMLs into `brand_context/templates/instagram-carousel/` as real `template.html` + `preview.png` + manifest entries with `status: ready`? (Open since v4; still open.)

## Next steps

1. Annabel reviews `~/Desktop/vh-intro-carousel-review.html` (v5) one final time.
2. Annabel reads `health-brand-carousel-skill-spec.md` and confirms (or amends) the recommended skill shape.
3. On approval: scaffold the skill at `~/Documents/AI-OS/skills/health-brand-intro-carousel/`, port the working `render_slides.py` into a brand-context-driven version, write SKILL.md.
4. Re-run Vital Health through the skill end-to-end to confirm output parity with the hand-built v5.
5. Test the skill on a second health/wellness brand to validate generalization.

## Context to preserve

- Final v5 state per slide:
  - Slide 1 (hero, full-bleed): "Medicine that *catches it* before it catches you." — Fraunces, no top kicker
  - Slide 2 (split right-photo): "Most emergencies are *preventable.*" — Fraunces, no kicker
  - Slide 3 (full-bleed): "*Ninety.* minutes to read your story before we write any of it." — **Cormorant Garamond italic**, no bottom sub
  - Slide 4 (split left-photo): "Your workup takes *weeks.* Not minutes." — Fraunces, no kicker
  - Slide 5 (full-bleed pull quote): "Care here reads more like *a relationship* than an appointment." — **Cormorant Garamond italic**, no attribution
  - Slide 6 (CTA): "*Free.* Thirty minutes. No cost. Just a fit conversation." — Fraunces
- Google Fonts import now includes Cormorant Garamond alongside Fraunces and Inter.
- Total API cost across all 5 versions ≈ $0.80 (no new image gens in v5 — text-only edits).
- Carousel folder: `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/`.
- Source of truth: `_workdir/render_slides.py` regenerates everything. `_workdir/build_review.py` builds `~/Desktop/vh-intro-carousel-review.html`.

## System refinement candidates

- **NEW: pre-ship legibility audit hook** — add a step to the carousel pipeline that flags any text element <24px sitting on a photo without a plate/veil/dark region. Could be a CSS-class linter or a manual checklist in the skill's pre-ship checklist.
- **NEW: font-variety check** — same skill should flag if all 6 slides use the same display face. Carousel feels templated when this happens.
- Carried from v4: `00-social-content` hard gate is correct in principle but expensive in practice when the template pool isn't built. Consider a "lightweight mode" that runs on hand-authored HTML.
- Carried from v4: `.env` `grep KEY=` is not proof a key is set — validate length/prefix. Already added to global CLAUDE.md.
