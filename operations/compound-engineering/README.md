# Compound Engineering

Compound engineering means each useful session should improve the system that
does future work, not only complete the immediate task.

## Loop

1. Do the work.
2. Verify the work.
3. Ask what should be easier next time.
4. Capture one reusable improvement if it is worth keeping.
5. Keep the improvement small enough that future agents will actually use it.

## What Counts

- A new or updated skill for recurring behavior.
- A better template, SOP, or checklist.
- A shorter startup instruction that prevents repeated context bloat.
- A project-specific `AGENTS.md` or `CLAUDE.md` rule.
- A durable checkpoint or refinement candidate.
- A lint/test/config improvement that makes verification repeatable.

## What Does Not Count

- Saving memory just because something happened.
- Adding process that no future session will read.
- Duplicating the same rule across many files.
- Updating `SOUL.md`, `USER.md`, `AGENTS.md`, or `CLAUDE.md` casually.
- Turning every small task into a system redesign.

## Capture Rule

At the end of meaningful work, ask:

- Did we repeat a pattern?
- Did we discover a failure mode?
- Did we create a prompt, command, checklist, lint rule, or template worth
  reusing?
- Would the next session be faster, safer, or clearer if this were captured?

If yes, capture the smallest reusable artifact. If no, leave a checkpoint only
when future context would otherwise be lost.

## Where To Put Improvements

- Agent behavior: `agents/<agent>/context/` or `agents/agent.md`
- Recurring workflow skill: `skills/<skill-name>/`
- CLI/tool connection: `cli-connections/<connection-name>/`
- Agent capability access: `agents/<agent>/profile.yaml`
- Agent-specific SOP: `agents/<agent>/sops/`
- Cross-agent artifact: `agents/shared/`
- Project rule: `projects/<project>/AGENTS.md` or `projects/<project>/CLAUDE.md`
- Memory candidate: `operations/memory/refinement-candidates/`
- Session checkpoint: `operations/memory/checkpoints/`

Prefer the most specific location that future agents will naturally read.

## Skill Creation Rule

Create durable skills in AI-OS first:

- Skills: `skills/<skill-name>/`
- CLI/tool connections: `cli-connections/<connection-name>/`

Declare which agents can use a skill or CLI connection in
`agents/<agent>/profile.yaml`. Legacy `agents/*/skills/` folders may remain
during migration, but new durable capabilities should route through the
top-level capability libraries.

Runtime folders such as `~/.claude/skills` and `~/.codex/skills` should point
back to AI-OS. Use `check-runtime-skill-drift.sh` to catch accidental
runtime-only skills.

When a canonical skill or CLI connection is materially used, log the usage in
Annabel Press:

```bash
operations/annabel-press/scripts/log-capability-use.mjs skill <skill-id> --agent <agent> --note "<short note>"
```

Do not log discovery, browsing, or mere availability.

## Approval Boundary

Agents may propose compound improvements freely.

Agents should edit core identity or root startup files only when the improvement
is durable, broadly useful, and Annabel has asked for it or clearly approved the
direction.
