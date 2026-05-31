---
date: 2026-05-31
time: 10:20
project: ai-os / website-refresh-skills
status: complete
next-session: Use `client-website-refresh` as the front door for the next client website refresh, then route Webflow QA through `webflow-rebuild-qa` and proposal PDFs through `client-proposal-pdf`.
---

# Session: Client Website Refresh Skill Harness

## What we worked on

Created a reusable AI-OS skill harness from the Vital Health website process and
the older website-audit pipeline so Annabel can repeat the process for future
client sites with fewer repeated corrections.

## Skills created

- `skills/client-website-refresh/`
  - End-to-end harness for intake, client dislikes, audit, Garry scope, HTML
    preview, Business Partner QA, editable-platform build, proposal, and
    checkpointing.
  - References include the full workflow, client question bank, and good/bad
    examples from Vital Health.
- `skills/webflow-rebuild-qa/`
  - Webflow rebuild and QA skill for translating static/Vercel previews into
    editable Webflow sites.
  - Captures staging-only publish, Designer flakiness, Data API reliability,
    editability rules, mobile QA, placeholders, and live blockers.
- `skills/client-proposal-pdf/`
  - Branded proposal PDF skill for phases, rates, honest ranges, hosting costs,
    blockers, and next steps.
  - Includes `scripts/build_proposal_pdf.py`, a markdown to styled HTML to
    Chrome PDF renderer.

## Routing updates

- Added the new skills to:
  - `agents/annie/profile.yaml`
  - `agents/garry/profile.yaml`
  - `agents/business-partner/profile.yaml`
- Updated `projects/website-audit/CLAUDE.md` to point new high-touch client
  refresh work at the canonical skills while preserving the older
  `.claude/commands/audit-*` pipeline as source material.

## Vital Health lessons preserved

- Keep existing portals/vendor tools unless replacement is explicitly scoped.
- Position mixed public-site/backend work accurately, for example public website
  plus workflow coordination, not a simple brochure-site redesign.
- Use Webflow when the client needs editable public content.
- Treat Vercel/static HTML as a preview unless the client wants custom code.
- Publish to staging first and block live launch on testimonials, headshots,
  sensitive claims, links, and client approval.
- Preserve Annabel's copy mechanics: no dashes as punctuation, current-status
  people language, no redundant clauses, plainest accurate phrasing.
- Proposal PDFs should be short, phased, rate-clear, and honest about discovery.

## Verification

- `quick_validate.py` passed for all three new skills.
- `build_proposal_pdf.py --help` passed.
- `python3 -m py_compile skills/client-proposal-pdf/scripts/build_proposal_pdf.py`
  passed.
- Smoke-rendered the Vital Health proposal markdown to
  `/private/tmp/vital-health-proposal-skill-smoke.pdf` with headless Chrome
  outside the sandbox after sandboxed Chrome aborted.

## Open notes

- The agent profile files appear untracked in the current git status, but they
  existed locally and were updated because profile routing is the right place
  for recurring behavior.
- Future improvements can add a Webflow "what the client can edit" note template
  after the next real client build validates the wording.
