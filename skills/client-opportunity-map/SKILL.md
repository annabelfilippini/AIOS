---
name: client-opportunity-map
description: Annie-led workflow for auditing a client or business folder, mapping tools and recurring work, identifying practical AI opportunities, and producing a plain-English opportunity map that can route strategy to Garry and build feasibility to Business Partner.
audience:
  - annie
  - garry
  - business-partner
runtime:
  - codex
  - claude
visibility: private
related_cli_connections:
  - github
---

# Client Opportunity Map

Use when Annabel wants to turn messy client or business context into a practical
AI opportunity map.

Annie leads. Garry judges business value. Business Partner checks build reality.

## Steps

1. Identify the target business, client, project, or folder.
2. If auditing a local folder, run read-only: `scripts/audit-existing-folder.py <path>`.
3. Decide whether the work is greenfield or audit-existing.
4. Ask how work happens in real life. Do not ask schema-shaped questions.
5. Map tools, repeated work, manual handoffs, automations, bottlenecks, and approval boundaries.
6. Match opportunity patterns and rank the top 3-5.
7. Route business/offer judgment to Garry and technical feasibility to Business Partner.
8. Produce a concise `OPPORTUNITY-MAP.md` or conversation summary.

## References

- Read [workflow.md](references/workflow.md) for the full operating model.
- Read [question-bank.md](references/question-bank.md) for interview prompts.
- Read [opportunity-patterns.md](references/opportunity-patterns.md) for pattern matching.
- Read [artifact-template.md](references/artifact-template.md) when writing a durable map.

## Guardrails

- Do not request credentials or rewrite client files during intake.
- Treat regulated, financial, legal, health, identity, and customer data as sensitive.
- Keep human approval for external messages, production changes, payments, account settings, and legal commitments.
