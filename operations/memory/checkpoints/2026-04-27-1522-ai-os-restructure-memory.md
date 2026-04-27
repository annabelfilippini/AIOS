---
date: 2026-04-27
time: 15:22
project: ai-os
status: complete
next-session: Test /decision-pipeline on one real idea, then run Codex review on the handoff.
---

# Session: AI-OS agent split, knowledge migration, and memory map

## What we worked on

- Split Claude and Codex roles: Claude owns planning/decision-making; Codex owns repo reality, implementation, and verification.
- Retired old overlapping Claude/Codex skills from active runtime folders and kept backups in `AI-OS/agents/runtime-backups/`.
- Created active Claude skill/command setup: `begin`, `checkpoint`, `decision-pipeline`.
- Created active Codex skills: `review-claude-plan`, `implement-approved-plan`.
- Made `AI-OS/agents` the source of truth and replaced runtime installs with symlinks.
- Migrated the Obsidian/Git vault from `AI-OS/wiki` to `AI-OS/knowledge`; left `AI-OS/wiki` as a compatibility symlink.
- Created and refined `SOUL.md`, `USER.md`, `AGENTS.md`, and `CLAUDE.md`.
- Added `references/` folders to active skills and set the rule that `good-bad-examples.md` should be based on real usage.
- Created `AI-OS/operations/memory/` with `checkpoints/`, `refinement-candidates/`, `archive/`, and `tmp/`.
- Updated the Sunday `Weekly System Consolidation` automation to consolidate candidates and clean memory.

## Decisions made

- Use `SOUL.md` for agent voice/taste, `USER.md` for Annabel's working model, `AGENTS.md` for universal operating rules, and `CLAUDE.md` as a thin Claude adapter.
- Keep `AI-OS/agents` canonical; `~/.claude` and `~/.codex` should be runtime symlinks only.
- Keep memory lean: checkpoint after meaningful sessions, then let Sunday consolidation propose permanent updates and clean stale notes.
- Do not auto-edit core identity files from checkpoints; checkpoints capture candidates.
- Do not invent good/bad skill examples before real runs.

## Open questions

- The `knowledge` Git repo still has a pre-existing unresolved `index.md` conflict and many dirty/deleted/untracked files. This session preserved that state but did not resolve it.
- Need to verify whether any external scripts still hardcode `AI-OS/wiki`; compatibility symlink should keep them working for now.
- Need to test the Claude-to-Codex handoff loop with a real idea.

## Next steps

- Run `/decision-pipeline` in Claude on one real idea and inspect the handoff quality.
- Run Codex `review-claude-plan` on that handoff and see whether the review format is useful.
- If the loop feels good, add real examples to the relevant skill `references/good-bad-examples.md`.
- Later: clean or resolve the `knowledge` repo conflict deliberately, not as a side effect of agent-system work.

## Context to preserve

- Annabel wants fewer overlapping tools and a clearer mental model.
- She wants real refinement mechanisms, not vague promises.
- She prefers reversible migrations, visible paper trails, and conservative deletion.
- The active memory home is now `AI-OS/operations/memory/checkpoints/`.
- `~/.claude/scratchpad/` is now runtime scratch, not the main durable memory path.

## System refinement candidates

- `USER.md`: Add more lived examples after testing `decision-pipeline`; current file is stronger but still mostly inferred from memory and this session.
- `SOUL.md`: Consider adding explicit "do not impersonate Annabel unless drafting requested" examples after first real outreach/content-draft run.
- `checkpoint` skill: After one or two real uses, add good/bad checkpoint examples to `references/good-bad-examples.md`.
- `AGENTS.md`: If Codex repeatedly misses the handoff protocol, make the Claude/Codex split more forceful.
