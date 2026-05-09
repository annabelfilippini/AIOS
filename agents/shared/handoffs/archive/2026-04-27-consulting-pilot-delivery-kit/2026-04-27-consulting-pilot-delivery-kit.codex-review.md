# Codex Plan Review: Consulting Pilot Delivery Kit

## Verdict

Approved

## Codebase Reality Check

`projects/consulting/` is a documentation-first project, not an application repo. There is no local `AGENTS.md` or `CLAUDE.md` under the consulting project, so the root AI-OS instructions apply.

The project already contains the ingredients this plan depends on:

- `README.md` defines the consulting company thesis, first wedge, pilot strategy, adoption rules, and folder layout.
- `framework/engagement-playbook.md` defines the canonical pilot flow from pre-meeting research through 30-day review and case-study extraction.
- `prospects/marta-brummell/` contains discovery notes, a research brief, meeting prep, outreach, and a recommendation artifact.
- `MEMORY.md` explicitly says major decisions about offer structure, pilots, tooling, and direction should be logged.

There is no existing reusable pilot delivery kit. Creating one under `framework/` is consistent with the folder layout.

## Required Plan Changes

Keep the implementation as internal operating documentation. Do not create client-facing assets that imply access to Marta's voice samples, transcripts, tools, or credentials.

The Marta-specific plan should name the first workflow as an internal build plan, not a commitment already made to Marta. The existing notes support content/speaking leverage plus a recording/session-summary improvement, but they do not prove tool access, case-study permission, or final client approval.

Update `MEMORY.md` because standardizing a 30-day pilot delivery kit is an operating decision for the consulting company.

## Risks Found

- The plan could become overbuilt if it tries to cover every possible consulting engagement.
- Marta's work touches client session content and potentially vulnerable disclosures. The plan must keep human approval and privacy boundaries explicit.
- The current recommendation mentions Claude Cowork and Granola, but the repo does not contain implementation details or account access. Those should stay as proposed tools, not assumed installed systems.

## Adjusted Implementation Plan

1. Add `projects/consulting/framework/pilot-delivery-kit.md` as a concise reusable internal framework.
2. Add `projects/consulting/prospects/marta-brummell/30-day-pilot-implementation-plan.md` using existing Marta notes as the example.
3. Append a dated decision to `projects/consulting/MEMORY.md`.
4. Write implementation notes next to this handoff after the documentation changes.

## Verification Plan

- Re-read the created docs for consistency with `README.md` and `framework/engagement-playbook.md`.
- Confirm the docs avoid fake client facts, external commitments, and credential/tool access claims.
- Run a targeted file listing to confirm the expected files exist.

## Notes For Claude

The handoff was directionally correct. The important correction is posture: this is an internal delivery kit and example implementation plan, not a client promise or workspace build. Business Partner can implement the adjusted plan now.
