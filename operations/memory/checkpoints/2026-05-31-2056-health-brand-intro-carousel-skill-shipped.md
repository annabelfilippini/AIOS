---
date: 2026-05-31
time: 20:56
project: vital-health-webflow-migration
status: shipped
next-session: test `health-brand-intro-carousel` skill on a second health/wellness brand (any peptide or wellness client Annabel has lined up) to validate generalization. Open question still: promote v5 slide HTMLs into `brand_context/templates/instagram-carousel/` as `status: ready` template entries so `00-social-content` orchestrator can use them.
---

# Session: health-brand-intro-carousel skill shipped + smoke-tested

## What we worked on

- Took the v5 Vital Health hand-built carousel pipeline and turned it into a reusable Claude skill at `~/Documents/AI-OS/skills/health-brand-intro-carousel/`.
- Built the full skill: `SKILL.md` (216 lines, full operating manual + lessons), `README.md` (quickstart + lineage), 4 scripts (`render_slides.py`, `generate_photos.py`, `build_review.py`, `preship_audit.py`), `prompts/photo-prompts.yaml` (6 base prompts with brand-substitutable style suffix), `examples/vital-health/inputs.yaml` (the v5 reference config as the template for new brands).
- Wrote the spec doc first at `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/health-brand-carousel-skill-spec.md` to align on shape before scaffolding.
- Codified every failure mode from v1→v5 into `SKILL.md` §6 as a 4-row table: `What we shipped | What Annabel said | The rule | How to avoid`. Quotes Annabel's actual feedback verbatim so future operators see the lived correction.
- Built `scripts/preship_audit.py` to auto-enforce 11 of those rules: layout diversity, font variety, body sans constant, brand mark slide 6 only, no duplicated masthead, no small-text-on-photo (the v5 legibility bug caught twice), no em/en dashes, no claim words, no chapter kickers, no fake attributions, real CTA language.
- Smoke-tested by running the new skill's pipeline against the existing v5 raw photos at `examples/vital-health/_smoke/`. Result: all 6 PNGs **byte-identical** to v5 manual build (`delta=+0 bytes` per slide). All 11 pre-ship audit checks pass.

## Decisions made

- **Skill, not tool.** Lives in AI-OS skill convention at `~/Documents/AI-OS/skills/health-brand-intro-carousel/`. Trigger phrases include "intro carousel for [brand]", "instagram intro post for [brand]", "preventive medicine carousel", etc.
- **Single skill v1**, not split into photo-gen sub-skill. Refactor only if a second skill ever needs the same photo pipeline.
- **6-slide arc is the default**, but skill accepts 3–8. For <6, drop priority is: slide 4 (diagnostics) → slide 5 (pull quote) → slide 3 (first visit). Slides 1, 2, 6 are non-negotiable. For >6, additional slide pool: testimonial, pricing/insurance, FAQ, before/after, team intro. Skill prompts the user when not 6.
- **Hard-coded opinions** (not user-tunable in v1): the 6-slide arc, layout assignments, font pairing rule (primary serif + 2-of-6 alt serif + Inter body), the legibility audit, the voice rules, the gpt-image-1 model choice.
- **Templated inputs** (per-brand): all copy strings, all color tokens, brand mark path, CTA URL, founder name, photo style suffix vocabulary.
- All "what went well / what didn't" lessons live INSIDE the skill (`SKILL.md` §5 + §6), not in a separate doc. Skill itself is the durable artifact; future operators read it on every run.

## Open questions

- **Second-brand validation**: which health/wellness brand do we run the skill on first to prove it generalizes beyond Vital Health?
- **Template pool promotion** (carried from v4): promote the v5 slide HTMLs into `brand_context/templates/instagram-carousel/` as real `template.html` + `preview.png` + `status: ready` manifest entries? Would let `00-social-content` orchestrator drive Vital Health posts too.
- Should `preship_audit.py` be wired as a pre-commit hook in the skill, or stay a manual `python preship_audit.py inputs.yaml` step? Manual is fine for v1.

## Next steps

1. Pick a second health/wellness brand. Run skill end-to-end. Document any failure modes that didn't surface in the Vital Health build, add a v5→v6 row to `SKILL.md` §6 if needed.
2. (Optional, separate task) Promote v5 slide HTMLs into `brand_context/templates/instagram-carousel/` template pool.
3. If the skill works cleanly on brand #2, consider hardening: making `render_slides.py` extract its inline HTML/CSS into `templates/slide-N.html.tmpl` files for easier per-brand customization (deferred from v1 — current inline templating is fine until a brand needs deep layout edits).

## Context to preserve

- **Skill location**: `~/Documents/AI-OS/skills/health-brand-intro-carousel/`
- **Reference example**: `examples/vital-health/inputs.yaml` (the v5 config). Copy + edit for any new brand.
- **Smoke test artifacts** (parity proof): `examples/vital-health/_smoke/` contains the run that confirmed byte-identical output to v5. Safe to delete if disk space matters; otherwise leave as the parity reference.
- **v5 working folder still intact** at `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/` — DO NOT DELETE. It's the smoke-test reference.
- **Cost envelope** baked into SKILL.md: ~$0.50–$1.00 per carousel ($0.40 first-pass + ~$0.30 typical iteration), 10–15 min wall time once inputs.yaml is filled out.
- **Build_review.py overwrote** `~/Desktop/vh-intro-carousel-review.html` with the smoke-test version — byte-identical content, just generated via the skill path instead of v5 manual scripts. No content loss.
- **PyYAML installed** into v5 venv at `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/_workdir/venv/`. New brand projects will need the same — skill scripts will need PyYAML in any project venv.

## Lineage chain (full conversation trail)

1. `2026-05-31-1829-vital-health-scrapes-carousel-pilot-paused.md` — pivot moment, Codex pilot paused
2. `2026-05-31-1854-vital-health-instagram-ad-brief.md` — creative brief intent
3. `2026-05-31-2015-vital-health-intro-carousel-v4-shipped.md` — v4 shipped + Annabel added the "Reusable patterns" section that became the skill spec foundation
4. `2026-05-31-2045-vital-health-intro-carousel-v5-shipped.md` — v5 shipped (kickers + attribution + font variety + legibility); skill spec written
5. **This checkpoint** — skill scaffolded, smoke-tested, parity confirmed; ready for second-brand validation

## System refinement candidates

- **NEW: skill-spec → skill scaffold flow worked well**. The pattern of (a) writing a consolidated spec doc with explicit recommendations + open questions, (b) getting user green-light on the open questions, (c) batching the scaffold across 2–3 messages with checkpoint between, kept this from blowing up. Worth codifying as a meta-pattern for any future "turn this hand-built pipeline into a skill" job.
- **NEW: byte-level parity smoke test** as the final acceptance check. When porting a working hand-built pipeline to a parameterized form, the parity smoke test (run the new pipeline against the old inputs, diff PNG sizes) is the cheapest proof of correctness. Worth defaulting to this pattern.
- Carried from v5: `00-social-content` hard gate is correct in principle but expensive when template pool isn't built. Now partially resolved — `health-brand-intro-carousel` skill is the "lightweight mode" for this format. Other formats (LinkedIn carousel, Twitter thread, etc.) still need their own template pool or skill.
- Carried from v4: `.env` `grep KEY=` is not proof a key is set — already in global CLAUDE.md.
