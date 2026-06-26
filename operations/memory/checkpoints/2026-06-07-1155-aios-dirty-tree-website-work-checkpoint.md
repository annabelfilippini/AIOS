---
date: 2026-06-07
time: 11:55
project: ai-os / projects-websites
status: in-progress
next-session: Inspect the large dirty tree before committing; preserve current Copenhagen/Freeride work and avoid blindly accepting the 1701 deletions.
---

# Session: AI-OS dirty tree and website work handoff

## What we worked on

- Saved a continuity checkpoint after the current AI-OS workspace ended up with a very large dirty tree on `main`.
- Current branch: `main`.
- Last committed state before this checkpoint: `56780ad checkpoint: Copenhagen short trip plan`.
- Current `git status` summary before writing this checkpoint:
  - `1701` deleted tracked files.
  - `2` modified tracked files.
  - `8` untracked paths.
- Modified tracked files visible:
  - `operations/README.md` adds `operations/hermes-vps/` as a Hermes VPS restart and tunnel runbook location.
  - `operations/annabel-press/usage/events.jsonl` logs recent skill and CLI usage through Copenhagen, Vital Health, Hermes, and Freeride work.
- Untracked active paths visible:
  - `operations/hermes-vps/`
  - `operations/memory/checkpoints/2026-06-06-1420-copenhagen-planner-editorial-redesign.md`
  - `operations/memory/checkpoints/2026-06-07-1058-freeride-tarifa-editorial-preview.md`
  - `operations/memory/checkpoints/2026-06-07-1140-design-taste-atlas-preferences.md`
  - `operations/memory/checkpoints/2026-06-07-1141-freeride-mix-match-two-page-direction.md`
  - `operations/memory/checkpoints/2026-06-07-1146-freeride-session-checkpoint.md`
  - `operations/memory/checkpoints/2026-06-07-1154-copenhagen-planner-redesign-checkpoint.md`
  - `projects/websites/`

## Decisions made

- Do not blindly commit or push the `1701` deletions. They may represent an intended cleanup, an ignored-folder transition, an iCloud/local availability issue, or an autosync side effect. They need review first.
- Treat `projects/websites/` as the active work area for the current Copenhagen planner and Freeride Tarifa static previews.
- Keep using checkpoints as the continuity layer for design iteration rather than trying to encode every decision in startup files.

## Open questions

- Are the large tracked deletions intentional cleanup of old tracked project folders, or accidental local removals that should be restored?
- Should `projects/*` be ignored and removed from Git tracking going forward, or should selected website projects stay tracked in the AI-OS repo?
- Should `operations/hermes-vps/` become the durable runbook source for Hermes restart/tunnel/process management?
- For Freeride: does the hybrid direction stand, with the earlier cinematic hero and calmer Santic-style rail content below?
- For Copenhagen: is the route-order sketch enough, or should the planner get a true embedded/live map?

## Next steps

- Run a focused dirty-tree review before any commit:
  - `git status --short`
  - `git diff --stat`
  - inspect top deleted folders before staging anything.
- Decide whether to restore, ignore/remove-from-tracking, or commit the large deletion set.
- Review `projects/websites/` visually before committing it.
- If preserving website work, commit it separately from repository cleanup/deletions.
- Re-run `operations/compound-engineering/lint-aios-system.sh` after deciding what to stage.

## Context to preserve

- Latest Freeride checkpoint: `operations/memory/checkpoints/2026-06-07-1146-freeride-session-checkpoint.md`.
- Latest Copenhagen checkpoint: `operations/memory/checkpoints/2026-06-07-1154-copenhagen-planner-redesign-checkpoint.md`.
- The user asked only to "checkpoint this"; do not infer approval to fix, restore, delete, or commit the dirty tree.

## System refinement candidates

- Add a simple "large dirty tree guard" script that summarizes deleted/modified/untracked counts and warns before autosync or manual commit when deletions exceed a threshold.
- Consider a clearer policy for `projects/*`: tracked selected projects vs ignored local project workspaces, so future autosync does not create confusing deletion waves.
