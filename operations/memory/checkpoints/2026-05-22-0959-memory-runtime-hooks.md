---
date: 2026-05-22
time: 09:59
project: ai-os-memory
status: complete
next-session: In a fresh Claude and Codex session, confirm the SessionStart hook surfaces the AI-OS recall brief before broad searches.
---

# Session: Memory Runtime Hooks

## What we worked on

- Added `operations/memory/scripts/session-recall.sh` as the canonical startup memory hook.
- Wired the hook into both `~/.claude/settings.json` and `~/.codex/hooks.json` under `SessionStart`.
- Added `operations/memory/scripts/checkpoint-reminder.sh` and wired it into both runtime `Stop` hooks.

## Decisions made

- Use hooks to surface recall, not bigger startup files.
- If a session starts outside AI-OS, show a root `ai-os-memory` recall brief and tell the agent to rerun recall from the relevant leaf folder.
- If a session starts inside AI-OS, show a cwd-scoped recall brief immediately.
- Stop hook reminds only when AI-OS files changed recently and no recent checkpoint exists.

## Open questions

- Codex may ask to trust the updated hook command because `~/.codex/hooks.json` changed.

## Next steps

1. Start a fresh Codex session and verify the recall brief appears.
2. Start a fresh Claude session and verify the recall brief appears.
3. If the hook output feels too long, reduce `session-recall.sh` from `--limit 3` to `--limit 2`.

## Context to preserve

- `session-recall.sh` was verified from `/Users/annabelfilippini` and from `projects/wayloft`.
- `checkpoint-reminder.sh` was syntax-checked and run; it emitted nothing because a recent checkpoint exists.
