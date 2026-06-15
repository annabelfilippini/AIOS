# HERMES

Hermes runtime adapter for this AI-OS.

Hermes is an execution surface, not an identity boundary. Annie, Garry, and
Business Partner are AI-OS modes that run on any capable LLM runtime. This file
is the Hermes peer of `CLAUDE.md` (the Claude adapter). Both sit over the same
universal rules in `AGENTS.md`.

## Read First

- Read `AGENTS.md` for the universal AI-OS rules. It is the source of truth.
  This file only adds Hermes-runtime specifics and routes you there.
- Read a project's own `AGENTS.md` or `CLAUDE.md` before broad searches.
- Read `agents/agent.md` when coordinating Annie, Garry, and Business Partner.
- Read `SOUL.md` or `USER.md` only when voice or personal context matters.

## Scope

- Operate inside this AI-OS repo (the folder that contains this file). Do not
  act on paths outside it unless Annabel asks.
- This root is an index, not a working project. Do project work inside
  `projects/<project>/`, and let project-specific instructions override root
  guidance.
- Large generated output goes in `scratch/` during work and
  `_archive/generated/` after handoff.

## Hermes Runtime Notes

- The working directory is pinned to this repo via `terminal.cwd`, so the
  terminal, file, and code tools all resolve here, and project context loads
  from here.
- Hermes loads only the first matching context file, and `HERMES.md` beats
  `AGENTS.md`. This file exists to win that match from any subfolder (it walks
  up to the git root) and send you to `AGENTS.md`. Always open `AGENTS.md`
  before assuming a rule.

## Source Of Truth

- Universal rules: `AGENTS.md`
- Agent coordination: `agents/agent.md`
- Garry: `agents/garry/`
- Annie: `agents/annie/`
- Business Partner: `agents/business-partner/`
- Durable memory and checkpoints: `operations/memory/`
- Knowledge vault: `knowledge/`
