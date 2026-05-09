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
- Recurring workflow: `agents/<agent>/skills/`
- Shared runtime skill: `agents/shared/skills/`
- Agent-specific SOP: `agents/<agent>/sops/`
- Cross-agent artifact: `agents/shared/`
- Project rule: `projects/<project>/AGENTS.md` or `projects/<project>/CLAUDE.md`
- Memory candidate: `operations/memory/refinement-candidates/`
- Session checkpoint: `operations/memory/checkpoints/`

Prefer the most specific location that future agents will naturally read.

## Skill Creation Rule

Create durable skills in AI-OS first:

- Claude/Garry only: `agents/garry/skills/`
- Codex/Business Partner only: `agents/business-partner/skills/`
- Claude and Codex: `agents/shared/skills/`

Runtime folders such as `~/.claude/skills` and `~/.codex/skills` should point
back to AI-OS. Use `check-runtime-skill-drift.sh` to catch accidental
runtime-only skills.

## Approval Boundary

Agents may propose compound improvements freely.

Agents should edit core identity or root startup files only when the improvement
is durable, broadly useful, and Annabel has asked for it or clearly approved the
direction.
