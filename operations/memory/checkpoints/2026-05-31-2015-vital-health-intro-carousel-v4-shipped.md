---
date: 2026-05-31
time: 20:15
project: vital-health-webflow-migration
status: in-progress
next-session: review v4 carousel in browser; decide whether to promote the 6 hand-authored HTML slides into the real instagram-carousel template pool, or iterate copy/imagery further.
---

# Session: Vital Health intro carousel v1 → v4 shipped

## What we worked on

- Merged 5 inspo refs (Oura, Function, Bloom, Solawave, Plunge) into `brand_context/visual-identity/` via `mkt-visual-identity` Update mode. Added 8 carousel-role moves to `moves.md`, 3 new avoids to `tokens.json`, 6-role rhythm to `identity.md`. Merge log at `brand_context/visual-identity/_analysis/2026-05-31-inspo-merge.md`. Locked fields untouched.
- Attempted `00-social-content` orchestrator. Phase 1 hard gate failed: `brand_context/templates/instagram-carousel/manifest.json` has 4 stub entries (all `status: pilot`), zero `template.html` files, no `composition-primitives.json`.
- Pivoted: hand-authored 6 self-contained HTML slide templates + generated 6 photos via `gpt-image-1` (`viz-image-gen/scripts/generate_image_gpt.py`). Composited via headless Chromium. Output namespaced under `projects/00-social-content/claude/2026-05-31/vh-intro-carousel/` to stay separate from Codex runs.
- Iterated v1 → v4 across the session:
  - **v1**: golden-hour moody, hands+notebook hero/signoff, paper on 4 slides
  - **v2**: brighter preventive vibe, people (back-only) on slides 1+5+6, paper only on slide 3, no notebook
  - **v3**: rewrote all 6 copy lines from `snapshot/about.html` (Julie's ER → prevention origin, 90-min visits, four-sets-of-eyes, free 30-min call); replaced slide 5 woman with older man patient
  - **v4**: rewrote 6 slide HTMLs for individual treatment — dropped duplicate masthead on slides 1+6, varied sizes/placements, magazine "01/02/03" kickers with italic gold numerals, oversized italic Fraunces display words ("preventable.", "Ninety.", "weeks.", "Free."), slide 5 redone as pull-quote with attribution

## Decisions made

- Pivot off `00-social-content` orchestrator (template pool was stub-only); use direct image gen + hand-authored composite instead.
- Use Claude-namespaced subfolder under `projects/00-social-content/claude/` to keep Codex's parallel work isolated.
- Story copy ALWAYS pulls from the website's actual language (`snapshot/about.html` + `brand_context/positioning.md` + `voice-profile.md`), not generic functional-medicine talk.
- Whimsy = italic Fraunces accent words + numbered chapter kickers + asymmetric placement, NOT hand-drawn.
- Lifestyle photos: no faces (back-only or wide). Mix women and one older man (in slide 5).
- Paper/card motif: ONE slide only (slide 3, the intake/first-consult slide).
- Slide 5 was upgraded from generic "A plan you can actually follow" to the brand's house line "Care here reads more like a relationship than an appointment."

## Open questions

- **Promote the 6 v4 slide HTMLs into `brand_context/templates/instagram-carousel/` as real `template.html` + `preview.png` + manifest entries with `status: ready`?** That would let future posts flow through the real `00-social-content` orchestrator instead of bespoke renders.
- Does Annabel want a second variant of any slide before locking? (Already saw v2-woman backup of slide 5 at `raw/v1-archive/s5-plan-v2-woman.png`.)
- Should the carousel be A/B tested as an ad, or just posted organic first?

## Next steps

1. Annabel reviews `~/Desktop/vh-intro-carousel-review.html` (v4).
2. On approval: promote HTMLs to template pool, write `instagram-carousel/manifest.json` entries with `status: ready`, copy `images/slide-N.png` → `preview.png`.
3. Decide publish target: organic IG, Meta ad, or both.
4. Run Codex's parallel attempt next session for comparison if Annabel wants.

## Context to preserve

- `.env` was broken (smashed line + empty placeholders); fixed so API calls work when `--api-key` is passed explicitly.
- venv lives at `projects/00-social-content/claude/2026-05-31/vh-intro-carousel/_workdir/venv`; earlier iterations archived under `raw/` + `images/v1-archive/` + `slides/v1-archive/`.

## System refinement candidates

- `.env` rule was added to `~/.claude/CLAUDE.md` (validate key length/prefix; don’t trust `KEY=` stubs; watch for smashed lines breaking dotenv parsing).
- Consider adding a “lightweight mode” to `00-social-content` so hand-authored HTML can run when template pool is empty (explicit user opt-in).

## Reusable patterns for a future `health-brand-intro-carousel` skill

- Preventive brands = bright. One motif only. No faces, no readable text, no logos.
- Copy must anchor to the real founder story (`snapshot/about.html` + positioning + voice). Mix gender + age; include at least one older patient (50s+).
- Every slide must feel individually composed (no duplicated chrome or repeated header/subheader pattern).
- Drop “01/02/03” chapter-kicker TOCs and fake pull-quote attributions (“house style of …”).
- Enforce text legibility and vary display serif on ~2 of 6 slides (close cousin); keep body sans constant.

### The arc that landed (v3 onwards) — generalizable to any preventive health brand

1. **Hero**: brand's preventive thesis in one line ("Medicine that catches it before it catches you.")
2. **The why**: founder origin story — what they saw that they couldn't unsee. Real number / years / lived experience.
3. **First visit**: what makes their consult different — specific minutes, what they actually do
4. **Measurement / diagnostics**: what they test, how long it takes, how many people read it
5. **The brand's central line**: a quote-style line about the relationship / philosophy ("Care here reads more like a relationship than an appointment")
6. **CTA**: real low-friction first step (free 30-min call, NOT "book your first consult")

### Voice rules (extracted from `voice-profile.md` and Annabel's reactions)

- No em-dashes / en-dashes (Annabel's global rule — replace with periods or commas)
- No "miracle / cure / guaranteed / reverse / melt / biohack" claim language
- Quiet confidence > hype. Short sentences. Plain words.
- Always end with a soft next step
- "Whimsical" = italic Fraunces accent words + numbered chapters + asymmetric placement, NOT hand-drawn or playful illustration

### Cost envelope (for skill quoting)

- (Omitted here; keep cost notes in the skill doc if needed.)

### Skill name suggestion

`health-brand-intro-carousel` — takes a brand_context folder + a website snapshot URL, runs the arc above with all corrections pre-applied. Inputs: brand name, primary color, founder story file (or URL), CTA type. Outputs: 6 slide PNGs + review HTML + post.yaml.
