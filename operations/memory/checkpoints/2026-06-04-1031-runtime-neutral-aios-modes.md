---
date: 2026-06-04
time: 10:31 UTC
project: ai-os
status: checkpointed
next-session: Review newly available AI-OS project/knowledge folders from GitHub and build sharper standards for Garry and Business Partner.
---

# Session: Runtime-Neutral AI-OS Modes And GitHub Sync

## What we worked on

- Verified Hermes can see the AI-OS GitHub-backed workspace at `/root/AI-OS`.
- Confirmed root repo sync is active through `operations/git-sync/aios-autosync.sh`.
- Reframed AI-OS so Claude, Codex, Hermes, ChatGPT, local models, and future LLMs are interchangeable runtimes/engines rather than identity boundaries.
- Reframed Annie, Garry, and Business Partner as reusable operating modes/personas usable from any capable runtime.
- Clarified that top-level `skills/` and `cli-connections/` are global AI-OS capabilities, not owned by a specific LLM runtime.
- Strengthened Garry and Business Partner language so they are expected to be critical, rigorous, and high-standards rather than agreeable or rubber-stamp reviewers.
- Renamed shared templates from runtime-specific names to responsibility-based names.
- Captured Annabel's durable preference that Garry and Business Partner should push back and raise standards.

## Files and areas changed

- `AGENTS.md`
- `CLAUDE.md`
- `agents/agent.md`
- `agents/annie/README.md`
- `agents/garry/README.md`
- `agents/garry/context/operating-manual.md`
- `agents/business-partner/README.md`
- `agents/business-partner/context/operating-manual.md`
- `agents/shared/templates/strategy-to-implementation-plan.md`
- `agents/shared/templates/business-partner-plan-review.md`
- `agents/shared/templates/builder-qa-request.md`
- `agents/shared/templates/qa-review.md`
- Runtime-neutral wording updates across selected `skills/` and agent SOP/template docs.

## Commits / verification

- Committed and pushed runtime-neutral mode refactor:
  - `0278e11 docs(agents): make modes runtime-neutral`
- Later repo state observed at checkpoint time:
  - `7eafdf7 checkpoint: Hermes AI-OS GitHub sync`
- Verification completed during the session:
  - `npm ci` succeeded.
  - `npm run lint:md` passed with 0 errors.
  - `git diff --check` passed.
  - Push to `origin/main` succeeded.

## Decisions made

- LLM runtimes are engines/execution surfaces, not agent identities.
- Annie, Garry, and Business Partner are modes/personas that should travel across runtimes.
- Skills, standards, templates, and CLI connections should be globally usable across AI-OS unless a runtime physically lacks the tool.
- Garry owns strategic challenge, business judgment, planning, and uncomfortable questions.
- Business Partner owns quality/reality gating across code, research, design, apps, websites, copy, and client deliverables.
- Business Partner should review Garry's plans against actual repository/context before implementation.
- Critical feedback is part of the product: the system should help Annabel become sharper, not merely feel validated.

## Open loops

1. Review newly pushed project folders from GitHub once visible on the VPS.
2. Build a formal standards library for research quality, design quality, app quality, website quality, client-ready work, and Annabel's taste/preferences.
3. Create evidence/example libraries with good/bad examples and reference outputs.
4. Deduplicate overlapping guidance across `AGENTS.md`, `CLAUDE.md`, `README.md`, and `agents/agent.md`.
5. Document Hermes as a runtime in the AI-OS start-here map.
6. Consider hardening autosync away from direct `main` pushes toward a safer sync branch/manual merge flow.
7. Add a correction-capture loop so painful iterations become reusable standards, skills, examples, or SOP updates.

## Context to preserve

- AI-OS root on the VPS: `/root/AI-OS`.
- Root GitHub remote: `git@github-aios:annabelfilippini/AIOS.git`.
- Autosync cadence: every 5 minutes, direct push to `main`, actor `hermes`.
- User is pushing missing Mac-side AI-OS folders/projects to GitHub so Hermes can inspect them.
- User wants AI-OS to support one-shot professional-grade apps, websites, research, and business outputs.
- User's father's AI research/prompting process is a benchmark for research quality.

## System refinement candidates

- Add a root/nested repo sync runbook for AI-OS.
- Add a script to clone/pull root plus nested repos into the VPS workspace.
- Add a standards library under AI-OS for research/design/app/client-readiness bars.
- Add good/bad examples for Garry and Business Partner to calibrate taste and rigor.
