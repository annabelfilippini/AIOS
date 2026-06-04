---
date: 2026-06-01
time: 17:20
project: instagram-carousel-skill
status: in-progress
next-session: Run Batch 2 — relocate Vital Health v5 carousel artifacts from `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/` into `projects/vital-health-webflow-migration/media/2026-05-31-vital-health-intro/`, then copy the 6 final slide PNGs into `~/Documents/AI-OS/skills/instagram-carousel/inspiration/vital-health-intro-2026-05-31/` with a `note.md`. Then Batch 3 — install the two hooks (`listen-for-corrections.sh` UserPromptSubmit + `enforce-media-folder.sh` PreToolUse), write `scripts/save_correction.py`, smoke-test the loop.
---

# Session: instagram-carousel skill scaffolded (Batch 1 of 3)

## What we worked on

- Pivot from `health-brand-intro-carousel` (locked to health intros) to a global `instagram-carousel` skill that handles any IG carousel format (intro, ad, educational, testimonial, list, story). Option C from the scope discussion: brand-agnostic skill, health is just the strong reference until other niches accumulate.
- Slimmed folder structure to 4 top-level items: `inspiration/`, `references/`, `scripts/`, plus SKILL.md + README.md. Killed `templates/`, `examples/`, `prompts/`, `references/posts/` as overbuilt — `inspiration/` doubles as the case library (good external ads + Annabel's past good work), and `references/preferences.md` carries the lessons from anything she didn't like.
- Wrote SKILL.md in the shape Annabel asked: title + one-line description → divider → "How to use" → "What's in this skill" folder map.
- Ported every correction from v1→v5 Vital Health build (old SKILL.md §5+§6, v4 + v5 checkpoint tables, pipeline-log.md, inspo-notes synthesis) into structured `references/preferences.md` with categories: Typography, Photography, Copy, Layout/Composition, TEXT-ON-PHOTO LEGIBILITY (highest priority — caught twice), Voice, Don't do this, Working principles, Synthesis moves, Uncategorized. Every entry has date + rule + source + verbatim quote where captured + applies-to.
- Folded useful conventions from `00-social-content` into SKILL.md: image-source priority, real-logos rule, AI prompt vocabulary (documentary keywords, never cinematic/8k/masterpiece), humanizer placement, post.yaml/caption.md/pipeline-log.md output convention.
- Copied scripts unchanged (byte-identical) from the old health skill: render_slides.py, generate_photos.py, build_review.py, preship_audit.py, photo-prompts.yaml.
- Archived (not deleted) `~/Documents/AI-OS/skills/health-brand-intro-carousel/` → `_archive/skills/health-brand-intro-carousel-2026-05-31/`, and `projects/vital-health-webflow-migration/.claude/skills/00-social-content/` → `_archive/skills/00-social-content-2026-06-01/`.
- Moved `brand_context/visual-identity/_refs/inspo-notes.md` → `skills/instagram-carousel/inspiration/ad-analyses-health.md` (global, applies to any project). Left a stub at the old location pointing to the new path.

## Decisions made

- **Name**: `instagram-carousel` (global), not `health-brand-intro-carousel` (locked).
- **Two hooks, both pending in Batch 3**:
  - `listen-for-corrections.sh` (UserPromptSubmit): pattern-matches negative feedback ("I don't like…", "don't use…", "change the…", "make it less…", "too X", etc.). Calls `scripts/save_correction.py` to append a structured entry directly to `preferences.md` with keyword-based category inference. No pending-corrections middle step.
  - `enforce-media-folder.sh` (PreToolUse on Write/Edit/Bash): blocks .png/.html/.yaml/.jsonl writes outside `<project_root>/media/<date>-<slug>/`. If no project root detected, auto-creates `~/Documents/AI-OS/projects/<brand-slug>/media/<date>-<slug>/`.
- **Scripts stay** — they're proven plumbing, byte-parity tested against v5. Not reinventing inline each run.
- **00-social-content fully integrated, then archived.** Not left "sitting there." Useful rules baked into new SKILL.md.
- **inspo-notes globalized.** Annabel can use the 5 ad analyses for any health project, not just Vital Health.

## Open questions

- Trigger phrase list for `listen-for-corrections.sh` — current draft errs aggressive (false positives = deletable, false negatives = lost forever). Confirm/expand the list when Batch 3 installs the hook.
- Hook scoping: how does the listener know an instagram-carousel run is active vs Annabel complaining about something unrelated? Likely an env flag the SKILL.md sets when invoked, hook reads it.
- When to test on a second brand to validate generalization beyond Vital Health (carried open since v5 checkpoint).

## Next steps

1. **Batch 2** — Relocate Vital Health v5 artifacts:
   - Move `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/` contents → `projects/vital-health-webflow-migration/media/2026-05-31-vital-health-intro/` (the new media-folder convention).
   - Copy the 6 final slide PNGs to `~/Documents/AI-OS/skills/instagram-carousel/inspiration/vital-health-intro-2026-05-31/` with a `note.md` ("the v5 build — proven 6-slide intro arc; copy structure, not copy").
   - Verify `~/Desktop/vh-intro-carousel-review.html` still opens correctly OR regenerate from the new media path.
2. **Batch 3** — Install hooks + write save_correction.py:
   - Write `~/.claude/hooks/listen-for-corrections.sh` + register in `~/.claude/settings.json` (UserPromptSubmit).
   - Write `~/.claude/hooks/enforce-media-folder.sh` + register (PreToolUse on Write/Edit/Bash).
   - Write `~/Documents/AI-OS/skills/instagram-carousel/scripts/save_correction.py` with keyword category inference + structured append to preferences.md.
   - Smoke-test: fake correction phrase → verify it lands in preferences.md correctly. Fake out-of-place write → verify hook blocks.

## Context to preserve

- **New skill location**: `~/Documents/AI-OS/skills/instagram-carousel/`. 11 files seeded.
- **Archived skills**: `~/Documents/AI-OS/_archive/skills/{health-brand-intro-carousel-2026-05-31, 00-social-content-2026-06-01}/`. Don't delete — proven reference builds + orchestrator history.
- **Vital Health v5 source artifacts** still at `projects/vital-health-webflow-migration/projects/00-social-content/claude/2026-05-31/vh-intro-carousel/` — Batch 2 moves them; DO NOT delete before Batch 2 runs.
- **preferences.md** is the durable artifact. The hook in Batch 3 will keep it growing automatically.
- **Old inspo-notes path** has a stub pointer now: `brand_context/visual-identity/_refs/inspo-notes.md` → points to new global location. Safe; don't delete the stub.

## System refinement candidates

- The "scaffold a new skill from a hand-built pipeline" pattern (used twice now: v5 → health-brand-intro-carousel, then → instagram-carousel) is converging on a meta-pattern: (1) write SKILL.md in `title → how to use → folder map` shape, (2) seed a `references/preferences.md` with every correction mined from prior runs (verbatim quotes preserved), (3) keep scripts/ as proven plumbing, (4) install a correction-listener hook so the skill grows automatically. Worth codifying.
- Hook-driven preference accumulation is the leverage point — if it works for instagram-carousel, the same pattern fits any execution skill that learns from user feedback (linkedin-carousel, video-thumbnails, podcast-clips, etc.). Worth a generic `correction-listener-hook` skill.
- Carried from v5: byte-level parity smoke test as final acceptance check. Apply to Batch 3 smoke-test (run new pipeline against vital-health v5 inputs, expect byte-identical PNGs).
