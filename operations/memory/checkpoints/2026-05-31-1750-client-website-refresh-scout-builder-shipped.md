---
date: 2026-05-31
time: 17:50
project: client-website-refresh
status: in-progress
next-session: Build Batch 2 — stages/03-diff-auditor.md, stages/04-polish.md, three gate scripts. Then test the full pipeline on a non-clinical site.
---

# Session: client-website-refresh harness — Scout + Builder shipped, Revero v2 validates

## What we worked on

Restructured the `client-website-refresh` skill from a single quality-prose doc into a staged pipeline of subagent files with FAIL rules, modeled on Annabel's "modern kitchen renovation" principle. Codex's prior generic HTML output on Revero was the diagnostic that drove the redesign. Ran Scout + Builder live on Revero through two iterations (v1, v2) to validate the rules.

## Decisions made

- **Architecture**: 4 stages — Scout → Builder → Diff Auditor → Polish. Gates between stages (file-existence shell scripts or LLM verification subagents).
- **Runtime**: Claude Code runs the pipeline. Stages = Agent tool calls. Gates = Bash scripts.
- **Core principle**: "Same kitchen, renovated." Brand DNA (identity-bearing assets, vibe, voice register) carries over. Renovation lives in typography, spacing rhythm, image cropping, layout, mobile, scroll feel.
- **Latitude system**: 3 levels — `minor-refresh` / `redirect` / `full-redo`. Vital Health was full-redo with hummingbird DNA preserved; Revero ran at `redirect`.
- **Vibe is a closed list of 11 words** — calm, warm, clinical, bold, editorial, technical, local, premium, holistic, playful, restrained. No invented vibes.
- **Identity-bearing assets capped at 5, now include shapes/gradients** (not just images) — the Revero cyan scoop was the proof.
- **20 FAIL rules in Builder** — phrased as "FAIL IF" with mechanical conditions, not advice. Specific bans: pill buttons, box-shadow, bold in body, em/en-dash punctuation, single-font walls, uniform section padding, uniform section widths, 5-up trust strips, 4-up icon grids, destructive scroll-reveal, hero < 70vh desktop.
- **Scroll-reveal must be additive, not subtractive** — default `opacity: 1`, hide only when `html.js` class is set by the script itself. Catches the failure mode where JS doesn't run and the page is blank.

## Open questions

- Should the Diff Auditor (Stage 3) be an LLM subagent or a static `verify.sh` script, or both? Probably both — mechanical gate runs first, LLM Auditor catches semantic issues.
- Section/asset-once enforcement: should "each identity-bearing asset appears at most once at its named source_prominence" be a FAIL rule or an Auditor finding? Leaning Auditor.
- Does the title tag count as "visible copy" for the no-dash rule? Edge case; should be clarified.
- How portable are these rules outside clinical/health sites? Need to test on a non-clinical site (local service business, ecommerce) before generalizing.

## Next steps

1. Write `stages/03-diff-auditor.md` — LLM subagent that scores the preview against a fixed checklist (headline word delta, hero prominence, asset reuse count, banned-pattern check, section count, etc).
2. Write `stages/04-polish.md` — runs only on Auditor failures, fixes specific findings without rebuilding.
3. Write `gates/gate-01-snapshot-ready.sh`, `gate-02-preview-ready.sh`, `gate-03-audit-passed.sh`.
4. Update top-level SKILL.md to route through the 4 stages with the gates.
5. Update `references/workflow.md` Step 5 to point at the new pipeline.
6. Replace `references/html-preview-quality.md` content with a pointer to `stages/02-builder.md` (or delete).
7. Build `references/good-bad-examples.md` with annotated Vital Health (good) + Revero v0 (bad) + Revero v2 (good) screenshots.
8. Test on a non-clinical site to validate portability.

## Context to preserve

- Skill source of truth: `~/Documents/AI-OS/skills/client-website-refresh/`
- Files added this session: `stages/01-scout.md`, `stages/02-builder.md`, `references/brand-snapshot-template.md`.
- Test project: `~/Documents/AI-OS/projects/revero-website-refresh/`
- Revero artifacts preserved for comparison:
  - `mockups/homepage-preview-v0-codex-bad.html` (pre-harness failure)
  - `mockups/homepage-preview-v1.html` (first run, had destructive scroll-reveal, no scoop, short hero, over-deduped testimonials)
  - `mockups/homepage-preview.html` = v2 (current, passes all 20 rules)
  - `mockups/revero-preview-v0-desktop.png`, `revero-preview-v1-desktop.png`, `revero-preview-v2-desktop.png` + mobile variants
  - `audit/brand-snapshot.md` (Scout output, now includes asset_6 cyan scoop)
- v2 validates: cyan scoop preserved as identity-bearing, verbatim hero, three named testimonials (Kevin/Rob/Kiska), no trust strip, no pill buttons, no stock illustrations, JS-gated additive scroll-reveal, two-font stack, varying section widths/padding.
- Annabel's taste rules captured in builder FAIL list: rectangular buttons over pill, sharp corners matching everywhere, no shadows, full-bleed images, mixed fonts, thin weights, accent color on key headline noun only, scroll reveal as life signal.

## System refinement candidates

- Clarify rule 14 scope (visible copy + `<title>` + `<meta description>`).
- Add rule: "each identity-bearing asset appears at most once at its named source_prominence" (caught in v2: collage reused in Smart Clinic section).
- Tighten rule 2/4 wording: "buttons and structural cards" vs "decorative background shapes" — the scoop's 50% radius is intentional, not a violation.
- Vital Health home should become the canonical "good" reference image inside `references/good-bad-examples.md`.
