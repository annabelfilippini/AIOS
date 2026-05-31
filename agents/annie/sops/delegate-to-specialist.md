# Delegate To Specialist

## Trigger

Use this SOP when Annabel brings work to Annie that may need Garry, Business
Partner, or both.

Annabel should not have to choose the agent. Annie chooses the route.

## Inputs

- Annabel's request.
- Relevant AI-OS project, document, repo, inbox, or calendar context.
- Current agent profiles:
  - `agents/annie/profile.yaml`
  - `agents/garry/profile.yaml`
  - `agents/business-partner/profile.yaml`

## Routing

Handle directly when the work is:

- assistant operations
- inbox, calendar, docs, briefs, drafts, follow-ups
- project organization
- low-risk internal updates
- synthesis across existing context

Delegate to Garry when the work is:

- business idea critique
- customer, market, wedge, or positioning judgment
- product scope
- decision-making before implementation
- Claude-to-Codex handoff preparation

Delegate to Business Partner when the work is:

- repository inspection
- implementation judgment
- debugging
- QA review
- verification
- code changes after a reviewed or clearly amended plan

Coordinate both when the work has a strategy-to-build path:

1. Ask Garry to clarify the idea, scope, and handoff.
2. Ask Business Partner to review the handoff against the repo.
3. Return one synthesized recommendation to Annabel.

## Procedure

1. Restate the request in plain language.
2. Decide whether Annie can handle it directly or should delegate.
3. If delegating, prepare the smallest useful brief for the specialist:
   - request
   - goal
   - known context
   - files or project paths
   - constraints and approval boundaries
   - exact output needed
4. Preserve specialist boundaries:
   - Garry should not claim repo truth.
   - Business Partner should not invent product strategy.
   - Annie should not pretend to be either specialist.
5. Synthesize the result for Annabel:
   - answer first
   - specialist recommendation
   - tradeoffs or blockers
   - next action
6. Ask Annabel only when a decision is irreversible, external, expensive,
   sensitive, or genuinely ambiguous.
7. Log any canonical skill or CLI connection that was materially used:
   `operations/annabel-press/scripts/log-capability-use.mjs <skill|cli> <id> --agent annie --note "<short note>"`.

Do not log mere browsing, availability checks, or profile access.

## Output

Annie's user-facing response should be one coherent update, not a transcript of
specialist chatter.

Use this shape:

```text
I routed this as: <Annie / Garry / Business Partner / both>.

Recommendation: <one clear next move>.

Why: <short reasoning>.

Next action: <what Annie can do, what needs approval, or what the specialist should do next>.
```

## Approval Requirement

No approval is needed to route, draft, summarize, or prepare internal handoffs.

Approval is required before:

- external communication
- spending money
- scheduling or moving meetings
- changing account settings
- deleting or archiving important records
- merging, deploying, publishing, or pushing production changes
- making legal, tax, financial, health, or contractual commitments

## Final Artifact Location

- Light routing notes can stay in the conversation.
- Durable cross-agent handoffs go in `agents/shared/handoffs/active/`.
- Durable QA reviews go in `agents/shared/qa/active/`.
- Annie-owned drafts or briefs go in `agents/annie/workspace/`.
