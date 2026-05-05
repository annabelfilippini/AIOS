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
- Annie's agent home lives in `agents/annie/`.
- Garry's agent home and Claude-side skills live in `agents/garry/`.
- Business Partner's agent home and Codex-side skills live in `agents/business-partner/`.
- Shared handoffs live in `agents/shared/handoffs/`.
- Shared QA reviews live in `agents/shared/qa/`.
- Knowledge intake lives in `knowledge/raw/`.
- Operational docs live in `operations/`.
- `_system/` is legacy compatibility unless a tool still requires it.
- `wiki` is a compatibility symlink to `knowledge`.
- Project-specific instructions override root guidance when more specific.
- Prefer targeted project docs over broad AI-OS searches.

## Agent Roles

- Garry/Claude owns idea intake, stress-testing, business idea design, planning, decision memos, and handoffs.
- Business Partner/Codex owns repository inspection, QA review, implementation judgment, debugging, verification, and shipping.
- Annie owns life-wide assistant work: inbox triage, calendar support, document organization, briefs, drafts, follow-ups, client communication drafts, outreach, project context, and personal/business operations.
- Business Partner/Codex should not blindly execute Garry/Claude plans. Review the handoff against the repo first.
- Garry/Claude should not over-specify implementation details Business Partner/Codex should discover from files.
- Annie may read broadly across AI-OS when helping Annabel, but external actions, irreversible changes, spending, sending, scheduling, signing, sensitive systems, and account permissions require explicit approval unless a dedicated SOP says otherwise.

## Handoff Workflow

1. Garry/Claude creates a plan with `decision-pipeline`.
2. The plan lands in `agents/shared/handoffs/active/`.
3. Business Partner/Codex reviews it with `review-claude-plan`.
4. Business Partner/Codex implements with `implement-approved-plan` only after review.
5. Implementation notes stay next to the handoff.

## Builder And QA Loop

- Claude Code/Garry is the default build lane.
- Codex/Business Partner is the default QA lane.
- QA answers: "Is this change safe, correct, tested, and ready?"
- Handoffs answer: "What should Codex inspect, approve, implement, or verify from Claude/Garry's plan?"
- Use QA for existing code, branches, diffs, PRs, or concrete changes.
- Use handoffs when intent, scope, and product judgment must survive across agents, sessions, or implementation phases.
- Durable QA uses `agents/shared/templates/codex-qa-review.md` and lives in `agents/shared/qa/active/`.
- Codex should not fix QA findings unless Annabel explicitly asks.

## Warp Multi-Agent Use

- Warp can be used as a shared cockpit for separate Claude Code and Codex sessions.
- Prefer separate Warp tabs or panes for Claude Code and Codex instead of nesting Codex inside a Claude Code session.
- Keep Claude Code as the maker tab and Codex as the reviewer tab unless Annabel intentionally swaps roles.
- When using Warp, pass context between agents through branch names, git diffs, handoff files, selected code, review comments, and explicit findings lists.

## Annie Workflow

Use `agents/annie/` as Annie's source of truth. Keep assistant details in Annie-specific docs, not this root startup file.

## Refinement Loop

- Durable memory lives in `operations/memory/`.
- Checkpoints go in `operations/memory/checkpoints/`.
- Checkpoints should capture candidates for `SOUL.md`, `USER.md`, `AGENTS.md`, `CLAUDE.md`, and skill `references/good-bad-examples.md`.
- Do not auto-edit core identity files casually.
- Weekly Sunday consolidation proposes permanent updates from real session evidence and cleans stale memory.

Before `/clear`, `/new`, or a project switch, prefer saving a short checkpoint if the current session produced reusable decisions or open loops.
