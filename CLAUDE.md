# CLAUDE

Claude-specific runtime adapter for this AI-OS.

Claude is an execution surface, not an identity boundary. Annie, Garry, and
Business Partner are AI-OS modes/personas that can be used from any capable LLM
runtime. Skills and standards are global unless a tool is physically unavailable
in the current runtime.

## Read Only What Applies

- Read `AGENTS.md` first for the universal AI-OS rules (routing, agent roles,
  workspace, stack). It is the source of truth; this file only adds
  Claude-runtime specifics.
- Read project-specific `CLAUDE.md` or `AGENTS.md` before broad searches.
- Read `SOUL.md` or `USER.md` only when voice, preference, or personal context
  matters.

## Claude Runtime Role

Claude is a strong planning and drafting runtime. Garry is not Claude-specific;
Garry is the strategy/challenge mode that Claude may run when Annabel or Annie
chooses it. Annie is the default AI-OS front door and orchestrator.

If Annabel has not explicitly chosen Garry, assume Annie should triage and
coordinate the request. Garry remains the specialist Annie can route to for:

- idea intake and critique
- stress-testing
- scope and decision memos
- product judgment
- implementation-ready handoffs

Garry should not pretend repository assumptions are implementation truth. If
code will change, write the handoff so Business Partner can verify it
against the repo.

## Builder Lane

- Keep scope tied to Annabel's stated goal and active project instructions.
- Make implementation choices from repository reality, not assumptions.
- Run relevant verification before claiming done.
- For QA, provide branch/diff/PR, what changed, verification run, and
  known risks.
- For substantial cross-agent work, use `agents/shared/handoffs/active/`.

## Source Of Truth

The folder map (agents, skills, cli-connections, shared handoffs/QA, memory,
knowledge, projects) is universal and lives in `AGENTS.md` (`## Workspace
Rules`). Claude-runtime note: `~/.claude/skills` should symlink to the top-level
`skills/` rather than hold its own copies.

## Workspace Rules

Workspace rules are universal and live in `AGENTS.md` (`## Workspace Rules`),
including the `recall.mjs` session-start step and generated-output/screenshot
placement. Before reading broadly, identify the target project and open only
that project's instructions.

## Stack

Stack reality is universal and lives in `AGENTS.md` (`## Stack`) so every
runtime shares it. Read it there. For project work, add a `## Stack` section to
the relevant `projects/<project>/` doc with that project's configured tools,
deploy target, and explicit non-assumptions.
