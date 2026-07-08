# Skills

## Skill Map

### Idea pipeline (execution order)

1. `office-hours-lite` — YC-style office hours when Annabel wants to brainstorm, validate, troubleshoot, or decide whether an idea is worth pursuing.
2. `ceo-review-lite` — founder/CEO review when Annabel wants to think bigger, reduce scope, choose ambition level, or challenge a plan before handoff.
3. `decision-pipeline` — turn a business or product idea into a clear decision and implementation-ready handoff, after the customer, pain, scope, and next move are clear.
4. `review-claude-plan` — review a Garry handoff against the actual repository before implementation; assess feasibility, risks, scope, and fit.
5. `implement-approved-plan` — implement a handoff only after Business Partner has reviewed it against the repo; make code changes, run verification, write notes.
6. `checkpoint` — save Garry strategy session state (decisions, reasoning, open questions, next steps) for continuity.

Review and guard sub-skills invoked from within that pipeline: `plan-eng-review-lite` (engineering review of a plan), `adversarial-review-lite` (harshest useful critique before shipping), `guardrails-lite` (scope and safety boundaries), `investigate-lite` (root-cause before fixing). The last two live only in `agents/business-partner/skills/`, symlinked into the Claude runtime.

### Client work

- `client-opportunity-map` — audit a client or business folder, map tools and recurring work, produce a plain-English AI opportunity map.
- `client-website-refresh` — end-to-end website refresh: audit, capture dislikes, plan, preview, rebuild in Webflow, prepare a proposal.
- `client-proposal-pdf` — build concise branded client proposal PDFs from markdown using the Vital Health pattern.
- `webflow-rebuild-qa` — turn a static HTML or Vercel preview into a client-editable Webflow site with staging publish and mobile QA.
- `small-business-shopify-redesign` — draft-only Shopify redesign, QA, and documentation for small business themes.

### Intelligence and scraping

- `skool-intelligence-digest` — collect and summarize Skool community signals for Annabel Press.
- `reddit-intelligence-digest` — read and summarize Reddit posts and full comment trees on a topic via the reddit-cli mirror.
- `site-scraper-cli-builder` — build or review a read-only, site-specific scraper CLI and matching AI-OS skill for sites Annabel can access.

### Content

- `instagram-carousel` — build an Instagram carousel (intro, ad, educational, testimonial, list, story) for any brand.

### Maintenance

- `markdown-lint-operating-docs` — practical Markdown linting for AI-OS operating docs without noisy generated files.

## Authoring Standard

Every new skill must pass this checklist before it lands:

1. Frontmatter has `name` and `description`.
2. Description states WHEN to trigger, with concrete phrases, not what the skill is.
3. Body is numbered steps or a checklist an agent can execute, not prose.
4. Every referenced file, script, or path exists (test each one).
5. No hardcoded paths to directories that do not exist yet.
6. Project names appear only as pattern exemplars, never as hardcoded targets.
7. Guardrails section if the skill touches live sites, client data, credentials, or publishing.
8. Output section says exactly what the skill returns.
9. Skills shared across agents live in top-level `skills/`; agent-only skills live in `agents/<agent>/skills/` and get a symlink in `~/.claude/skills/`.
10. Reusable skills stay project-agnostic; project specifics go in that project's folder.

Duplication model: top-level `skills/` is the source of truth. Copies under `agents/*/skills/` exist for agent scoping and must stay byte-identical (the agent README files already document which moved).
