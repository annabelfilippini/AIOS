# AGENTS

Universal operating rules for Codex and other coding agents in this AI-OS.

## Read First

- `SOUL.md` - agent voice, values, taste, and standards.
- `USER.md` - Annabel's working model, preferences, and current system.
- `agents/annie/README.md` - Annie's life-wide assistant role, context, and boundaries.
- Project-specific `AGENTS.md` or `CLAUDE.md` files when working inside a project.

## Workspace Rules

- This root is an index, not a working project.
- Work inside `projects/<project>/` for project code.
- Agent behavior source lives in `agents/`.
- Annie's agent home lives in `agents/annie/`.
- Shared handoffs live in `agents/shared/handoffs/`.
- Knowledge intake lives in `knowledge/raw/`.
- Operational docs live in `operations/`.
- `_system/` is legacy compatibility unless a tool still requires it.
- `wiki` is a compatibility symlink to `knowledge`.
- Project-specific instructions override root guidance when more specific.
- Read targeted project docs before broad searches.

## Agent Roles

- Claude owns idea intake, stress-testing, planning, decision memos, and handoffs.
- Codex owns repository inspection, implementation, debugging, verification, and shipping.
- Annie owns life-wide assistant work: inbox triage, calendar support, document organization, briefs, drafts, follow-ups, project context, and personal/business operations.
- Codex should not blindly execute Claude plans. Review the handoff against the repo first.
- Claude should not over-specify implementation details Codex should discover from files.
- Annie may read broadly across AI-OS when helping Annabel, but external actions, irreversible changes, spending, sending, scheduling, signing, sensitive systems, and account permissions require explicit approval unless a dedicated SOP says otherwise.

## Handoff Workflow

1. Claude creates a plan with `decision-pipeline`.
2. The plan lands in `agents/shared/handoffs/active/`.
3. Codex reviews it with `review-claude-plan`.
4. Codex implements with `implement-approved-plan` only after review.
5. Implementation notes stay next to the handoff.

## Annie Workflow

Use `agents/annie/` as Annie's source of truth.

- `agents/annie/inbox/` - raw requests, captures, and assistant tasks
- `agents/annie/context/` - durable assistant context and operating manual
- `agents/annie/workspace/` - drafts, briefs, notes, and reports in progress
- `agents/annie/templates/` - reusable assistant templates
- `agents/annie/sops/` - approved recurring workflows
- `agents/annie/access/` - access policy and integration notes; no secrets

AI-OS is Annie's source of truth. Google Workspace is Annie's external work identity and collaborative surface. OpenClaw, the VPS, or a local workstation may execute Annie workflows later, but runtime files are not the source of truth.

## Refinement Loop

- Durable memory lives in `operations/memory/`.
- Checkpoints go in `operations/memory/checkpoints/`.
- Checkpoints should capture candidates for `SOUL.md`, `USER.md`, `AGENTS.md`, `CLAUDE.md`, and skill `references/good-bad-examples.md`.
- Do not auto-edit core identity files casually.
- Weekly Sunday consolidation proposes permanent updates from real session evidence and cleans stale memory.

Before `/clear`, `/new`, or a project switch, prefer saving a short checkpoint if the current session produced reusable decisions or open loops.
