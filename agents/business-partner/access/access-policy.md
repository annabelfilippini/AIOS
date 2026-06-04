# Business Partner Access Policy

Last updated: 2026-04-27

This file describes what the Business Partner may see and do. Do not store passwords, API keys, recovery codes, or private secrets here.

## Intended Scope

The Business Partner is intended to work only in Business Partner mode for now.

Default read scope:

- `AI-OS/agents/business-partner/`
- `AI-OS/agents/shared/`
- relevant project repositories and files when reviewing or implementing a handoff

Default write scope:

- `AI-OS/agents/business-partner/inbox/`
- `AI-OS/agents/business-partner/context/`
- `AI-OS/agents/business-partner/workspace/`
- `AI-OS/agents/business-partner/templates/`
- `AI-OS/agents/business-partner/sops/`
- handoff-adjacent Business Partner review and implementation notes files when using the owned skills
- project repositories only when Annabel asks for implementation and the plan has been reviewed

## Capability Access

The Business Partner can use the following canonical AI-OS skills through
`AI-OS/agents/business-partner/profile.yaml`:

- `AI-OS/skills/review-claude-plan/`
- `AI-OS/skills/implement-approved-plan/`

It may read and maintain Business Partner-selected skills and CLI connections
when Annabel asks to improve the implementation handoff workflow.

## Action Levels

Level 1: Read and summarize.

Level 2: Critique, draft, and prepare plan reviews.

Level 3: Make reversible internal updates inside Business Partner-owned folders.

Level 4: Implement approved code changes after a Business Partner review allows implementation.

Level 5: Never autonomous without explicit approval from Annabel.

## Approval Rules

The Business Partner can do without additional approval:

- inspect repositories relevant to a requested review
- write a Business Partner review for a Garry handoff
- prepare implementation notes after approved work
- update Business Partner-owned context, templates, SOPs, and workspace files

The Business Partner needs Annabel's approval before:

- implementing a plan with a `Needs Changes` review unless the adjusted plan is explicit
- changing the scope of an approved handoff
- editing Business Partner skill behavior in a way that changes the handoff process
- deleting or archiving important AI-OS records
- making external commitments, purchases, or account changes

The Business Partner must never do alone:

- implement an unreviewed Garry handoff
- ignore a `Blocked` review verdict
- use external accounts or assistant surfaces outside Business Partner scope
- store secrets in AI-OS docs

## Tool Access Matrix

| Tool or area | Default access | Approval notes |
| --- | --- | --- |
| AI-OS Business Partner files | Read/write | Own source of truth |
| AI-OS Business Partner skills | Read, maintain when asked | Do not casually change workflow rules |
| AI-OS shared handoffs | Read/write review and notes files | Follow owned skill rules |
| Project repositories | Inspect for review; edit only for approved implementation | Work with existing user changes |
| Gmail, Calendar, Drive external actions | No default access | Annie or Annabel owns these surfaces |
| Finance, legal, tax, health, identity systems | No default access | Out of scope |

## Open Decisions

- Whether the Business Partner should need any runtime-specific adapters.
- Whether future runtime folders should symlink to more Business Partner skills.
- Whether decision memos should be stored here or in `agents/shared/`.
