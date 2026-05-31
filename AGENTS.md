# AGENTS

Universal operating rules for Codex and other coding agents in this AI-OS.

## Read Only What Applies

- Always read project-specific `AGENTS.md` or `CLAUDE.md` before broad searches.
- Read `agents/agent.md` only when coordinating Annie, Garry, and Business Partner.
- Read agent-specific READMEs only when that agent is involved.
- Read `SOUL.md` or `USER.md` only when voice, preference, or personal context matters.

## Workspace Rules

- This root is an index, not a working project.
- Work inside `projects/<project>/` for project code.
- Agent behavior source lives in `agents/`.
- Canonical skills live in `skills/`.
- Canonical CLI/tool connections live in `cli-connections/`.
- Annie's agent home lives in `agents/annie/`.
- Garry's agent home lives in `agents/garry/`.
- Business Partner's agent home lives in `agents/business-partner/`.
- Legacy agent-owned skill folders are not source of truth. New durable
  capabilities route through top-level `skills/` and `cli-connections/`.
- Shared handoffs live in `agents/shared/handoffs/`.
- Shared QA reviews live in `agents/shared/qa/`.
- Knowledge intake lives in `knowledge/raw/`.
- Operational docs live in `operations/`.
- `_system/` is legacy compatibility unless a tool still requires it.
- `wiki` is a compatibility symlink to `knowledge`.
- Project-specific instructions override root guidance when more specific.
- Prefer targeted project docs over broad AI-OS searches.

## Agent Roles

- Annie is the default front door and orchestrator. Annabel should be able to talk to Annie first; Annie routes to Garry or Business Partner when specialist work is needed and synthesizes the result.
- Garry/Claude owns idea intake, stress-testing, business idea design, planning, decision memos, and handoffs.
- Business Partner/Codex owns repository inspection, QA review, implementation judgment, debugging, verification, and shipping.
- Annie owns life-wide assistant work: inbox triage, calendar support, document organization, briefs, drafts, follow-ups, client communication drafts, outreach, project context, personal/business operations, specialist delegation, and synthesis.
- Business Partner/Codex should not blindly execute Garry/Claude plans. Review the handoff against the repo first.
- Garry/Claude should not over-specify implementation details Business Partner/Codex should discover from files.
- Annie may read broadly across AI-OS when helping Annabel, but external actions, irreversible changes, spending, sending, scheduling, signing, sensitive systems, and account permissions require explicit approval unless a dedicated SOP says otherwise.

## Handoff Workflow

1. Annabel brings the request to Annie by default.
2. Annie handles simple assistant/ops work directly or routes strategy to Garry.
3. Garry/Claude creates a plan with `decision-pipeline` when strategy should become implementation.
4. The plan lands in `agents/shared/handoffs/active/`.
5. Annie routes the handoff to Business Partner/Codex for `review-claude-plan`.
6. Business Partner/Codex implements with `implement-approved-plan` only after review.
7. Implementation notes stay next to the handoff, and Annie summarizes the outcome for Annabel.

## Builder And QA Loop

- Claude Code/Garry is the default build lane.
- Codex/Business Partner is the default QA lane.
- QA answers: "Is this change safe, correct, tested, and ready?"
- Handoffs answer: "What should Codex inspect, approve, implement, or verify from Claude/Garry's plan?"
- Use QA for existing code, branches, diffs, PRs, or concrete changes.
- Use handoffs when intent, scope, and product judgment must survive across agents, sessions, or implementation phases.
- Durable QA uses `agents/shared/templates/codex-qa-review.md` and lives in `agents/shared/qa/active/`.
- Codex should not fix QA findings unless Annabel explicitly asks.

## Compound Engineering

After meaningful work, apply the compound-engineering loop:

- Ask what should be easier, safer, or clearer next time.
- Capture the smallest reusable improvement in the most specific place.
- Prefer skills, templates, SOPs, project rules, lint/test config, checkpoints,
  or refinement candidates over bloating startup files.
- See `operations/compound-engineering/README.md`.

## Skill Source Of Truth

- Create durable skills inside AI-OS first, never directly in runtime folders.
- Use top-level `skills/` as the canonical AI-OS skills library.
- Use top-level `cli-connections/` as the canonical AI-OS CLI/tool connection library.
- Use `agents/<agent>/profile.yaml` to declare an agent's default/recommended
  skills and CLI connections. Claude and Codex runtimes may both access global
  top-level skills.
- Legacy `agents/*/skills/` folders are not source of truth. Keep durable
  skills in top-level `skills/`; remove or archive legacy copies only during a
  dedicated cleanup pass.
- Runtime folders like `~/.claude/skills` and `~/.codex/skills` should point
  to canonical AI-OS skills, preferably with symlinks.
- Annabel Press lives in `operations/annabel-press/` and indexes skills, CLI
  connections, profiles, and validation status.
- When an agent materially uses a canonical skill or CLI connection, log it with
  `operations/annabel-press/scripts/log-capability-use.mjs`. Do not log mere
  discovery, browsing, or availability.
- Run `operations/compound-engineering/check-runtime-skill-drift.sh` when a
  runtime-only skill may have been created by accident.

## Warp Multi-Agent Use

- Warp can be used as a shared cockpit for separate Claude Code and Codex sessions.
- Prefer separate Warp tabs or panes for Claude Code and Codex instead of nesting Codex inside a Claude Code session.
- Keep Claude Code as the maker tab and Codex as the reviewer tab unless Annabel intentionally swaps roles.
- When using Warp, pass context between agents through branch names, git diffs, handoff files, selected code, review comments, and explicit findings lists.

## Annie Workflow

Use `agents/annie/` as Annie's source of truth. Annie is the default routing layer for AI-OS requests unless Annabel explicitly chooses Garry or Business Partner. Keep assistant/orchestration details in Annie-specific docs, not this root startup file.

## Refinement Loop

- Durable memory lives in `operations/memory/`.
- Checkpoints go in `operations/memory/checkpoints/`.
- Checkpoints should capture candidates for `SOUL.md`, `USER.md`, `AGENTS.md`, `CLAUDE.md`, and skill `references/good-bad-examples.md`.
- At the start of an AI-OS session or project switch, run
  `node operations/memory/scripts/recall.mjs --cwd "$PWD" --query "<task>"`
  before broad memory searches. Read only the surfaced sources unless more depth
  is needed.
- Do not auto-edit core identity files casually.
- Weekly Sunday consolidation proposes permanent updates from real session evidence and cleans stale memory.

Before `/clear`, `/new`, or a project switch, prefer saving a short checkpoint if the current session produced reusable decisions or open loops.
