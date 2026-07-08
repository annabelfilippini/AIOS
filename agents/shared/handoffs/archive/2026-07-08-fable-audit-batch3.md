---
date: 2026-07-08
from: Fable 5 (audit session)
to: Opus (implementation)
project: ai-os
status: done
reviewer: Fable 5 checks the result when done
---

# Handoff: AI-OS audit batch 3 — skills README, checkpoint standard, refinement close-out

## Context

A full Fable 5 audit of skills, hooks, commands, and the memory layer ran on
2026-07-08. Batches 1 and 2 are already applied (see
`operations/memory/checkpoints/in-progress.md`, last two entries). This batch
is the remaining approved work. Keep diffs minimal. Do not refactor anything
beyond what is written here. Do not touch recall.mjs, settings.json, hooks, or
/begin — those are done.

Style rules for any prose you write: headings are plain noun phrases, never
sentences. No explanatory one-liner subtitles under headings. No em-dashes or
double hyphens in body text; use commas or periods.

## Task 1: create skills/README.md

Create `~/Documents/AI-OS/skills/README.md`. Target length 40 to 60 lines.
Two sections only.

### Section: Skill Map

Group the 20 existing skills exactly like this (verified by audit, do not
re-derive):

- Idea pipeline, in execution order: office-hours-lite → ceo-review-lite →
  decision-pipeline → review-claude-plan → implement-approved-plan →
  checkpoint. Note that plan-eng-review-lite, adversarial-review-lite,
  guardrails-lite, investigate-lite are review/guard sub-skills invoked from
  within that pipeline (the last two live only in
  `agents/business-partner/skills/`, symlinked into the Claude runtime).
- Client work: client-opportunity-map, client-website-refresh,
  client-proposal-pdf, webflow-rebuild-qa, small-business-shopify-redesign.
- Intelligence and scraping: skool-intelligence-digest,
  reddit-intelligence-digest, site-scraper-cli-builder.
- Content: instagram-carousel.
- Maintenance: markdown-lint-operating-docs.

One line per skill max: name plus when it fires. Pull the "when" from each
skill's existing frontmatter description; do not invent new wording.

### Section: Authoring Standard

Every new skill must pass this checklist before it lands. Reproduce it
verbatim:

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

Also state the duplication model in two sentences: top-level `skills/` is the
source of truth; copies under `agents/*/skills/` exist for agent scoping and
must stay byte-identical (the agent README files already document which moved).

## Task 2: checkpoint skill standard

Edit `~/Documents/AI-OS/skills/checkpoint/SKILL.md` (top-level copy) AND its
byte-identical copy `~/Documents/AI-OS/agents/garry/skills/checkpoint/SKILL.md`.
Both files must end up identical. Add two rules to the existing rules section,
matching its current formatting:

1. `project:` must be a single canonical kebab-case slug matching the folder
   name under `projects/` (e.g. `style-feed`, `wayloft`, `life-os`), or
   `ai-os` for system work. Never prose, never a description.
2. When a new checkpoint supersedes an older `in-progress` checkpoint for the
   same project, update the older file's `status:` to `superseded` in the same
   session.

Do not restructure the rest of the skill.

## Task 3: close out the May 25 refinement candidate

File: `operations/memory/refinement-candidates/2026-05-25-weekly-system-consolidation.md`

1. Apply its approved edit: in `~/Documents/AI-OS/USER.md`, replace the skill
   names `garry-office-hours-lite` with `office-hours-lite` and
   `garry-ceo-review-lite` with `ceo-review-lite`. If those strings are not
   present, report that and skip (do not guess substitutes).
2. Do NOT rotate any keys yourself. Instead check
   `projects/pickleball-portal/` wiki/docs for any note that the Beehiiv API
   key was rotated after 2026-07-05. Report YES or NO with the file you
   checked. This is a flag for Annabel, not work for you.
3. Move the refinement candidate file to `operations/memory/archive/` and set
   its frontmatter `status: processed`.

## Verification before reporting done

1. `node operations/memory/scripts/recall.mjs --cwd ~/Documents/AI-OS --query "checkpoint" --limit 2` runs without error.
2. `diff ~/Documents/AI-OS/skills/checkpoint/SKILL.md ~/Documents/AI-OS/agents/garry/skills/checkpoint/SKILL.md` returns empty.
3. README renders: no broken relative links, every skill named actually exists in `skills/` or `agents/business-partner/skills/`.
4. `refinement-candidates/` is empty; the file exists in `archive/` with `status: processed`.

## Report format

List: files touched, the Beehiiv rotation YES/NO finding, anything skipped and
why, verification output. Append one progress line to
`operations/memory/checkpoints/in-progress.md` dated 2026-07-08, marked
"batch 3 (Opus)".

## Known risks

- USER.md strings may already be updated; skip rule is in Task 3.
- checkpoint SKILL.md copies could have drifted since the audit (they were
  byte-identical on 2026-07-08); if they differ, stop and report instead of
  editing.
