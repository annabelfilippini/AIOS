# Consulting Pilot Delivery Kit

## Decision

Verdict: Build now
Reason: The consulting project already has a clear thesis, a pilot strategy, Marta-specific discovery notes, and a reusable engagement playbook. The missing piece is a concrete delivery kit that turns the strategy into repeatable pilot execution.
Tradeoff: This should stay as a lightweight operating artifact, not a polished product, dashboard, or client-facing sales deck.

## Goal

Create a reusable pilot delivery kit for Annabel's consulting company, using the Marta Brummell pilot as the first concrete example.

The kit should help Annabel move from "good strategic notes" to "I know exactly what to build, what to ask for, what to hand off, and how to review success after 30 days."

## Desired Behavior

Inside `projects/consulting/`, Annabel should have:

- a reusable framework artifact for running a 30-day consulting pilot
- a Marta-specific implementation plan that converts existing notes into a delivery path
- a memory entry recording the operating decision if this changes the consulting workflow

The output should be useful at 11pm: concise, concrete, and easy to follow without rereading every source note.

## User / Buyer

Primary user: Annabel, as the operator of the consulting company.

End client example: Marta Brummell, a warm pilot prospect who already uses AI and needs a sharper content/speaking thought partner plus a practical session recording workflow improvement.

## Pain Or Opportunity

The consulting company has strong positioning and enough discovery context, but pilot execution could still sprawl:

- the engagement playbook is canonical but broad
- Marta's notes are rich but distributed across prep, research, meeting notes, and recommendations
- the first few pilots need a consistent delivery rhythm so they generate case studies instead of becoming bespoke one-offs

## Stress Test

Strong signals:

- `projects/consulting/README.md` defines the wedge: AI-ready onboarding and practical AI operating layers for expert-led businesses.
- `projects/consulting/framework/engagement-playbook.md` defines a 45-minute discovery call, 7-day build, handoff, 30-day review, and case-study extraction.
- Marta's prospect folder already contains post-discovery notes and a recommended 30-day content/speaking leverage system.

Weak spots:

- Do not pretend the consulting offer is more validated than it is. The current strategy says three pilots only before expanding.
- Do not create a dashboard or complex new system.
- Do not create fake client-owned assets, transcripts, prompts, or credentials.
- Do not touch sensitive client material beyond what already exists in local notes.

## Smallest Useful Scope

1. Add a reusable `framework/pilot-delivery-kit.md`.
2. Add a Marta-specific `prospects/marta-brummell/30-day-pilot-implementation-plan.md`.
3. Update `MEMORY.md` if Codex confirms this is a meaningful operating decision.

## Non-Goals

- No external emails.
- No calendar invites.
- No Claude Cowork workspace creation.
- No generated client prompts pretending to be trained on private voice samples.
- No Squarespace, Circle, Granola, or account setup.
- No changes to website mockups or audit HTML.

## Acceptance Criteria

- The reusable framework makes the pilot sequence explicit from intake through 30-day review.
- The Marta plan references existing local context and identifies the first buildable workflow.
- The Marta plan includes what Annabel needs from Marta, what not to build, and how success should be measured.
- The implementation stays inside `projects/consulting/` and shared handoff artifacts.
- Any significant consulting operating decision is logged in `projects/consulting/MEMORY.md`.

## Risks And Assumptions

- Assumption: Annabel wants this as an internal operating artifact, not a client-facing proposal.
- Assumption: Marta remains the best example because there is already discovery context.
- Risk: The kit becomes process-heavy and slows Annabel down.
- Risk: The Marta plan overreaches into coaching/session data privacy without explicit client permission.
- Risk: "content/speaking thought partner" becomes too abstract unless tied to one concrete first workflow.

## Questions For Codex To Verify

- Does `projects/consulting/` already have a template or delivery kit that should be extended instead of creating a new one?
- Do Marta's existing notes support a 30-day pilot implementation plan, or is more discovery needed first?
- Does `MEMORY.md` require an update for this workflow decision?
- Are there project-specific instructions under `projects/consulting/` that override the root AI-OS guidance?

## Codex Handoff

Codex should inspect the relevant repo/files before implementing. Treat this plan as directional, not binding. If the codebase suggests a smaller or safer path, amend the plan before coding.
