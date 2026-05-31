# Annabel Press

Annabel Press is the local index and dashboard for AI-OS capabilities.

It should work like a personalized Printing Press: one place to see the skills
Annabel has built, the CLI connections those skills can use, and which agents
are allowed to pull from each capability.

## Source Of Truth

The long-term source of truth should move toward:

```text
AI-OS/
  skills/              # canonical skills
  cli-connections/     # canonical CLI/tool connections
  agents/              # agent profiles and operating docs
  operations/
    annabel-press/     # dashboard, scanners, indexes, validation
```

Current agent-owned skill folders should not be deleted casually. Migrate them
carefully by moving or symlinking each skill into `AI-OS/skills/`, then updating
runtime symlinks after validation.

## Mental Model

- `AI-OS/skills/` holds reusable agent capabilities.
- `AI-OS/cli-connections/` holds reusable CLI/tool connection definitions.
- `AI-OS/agents/<agent>/profile.yaml` declares which skills and CLI connections
  an agent can use.
- `operations/annabel-press/` displays, validates, and connects those pieces.

This keeps skills from being confused with Garry-only, Business Partner-only,
Codex-only, Claude-only, or `skills.sh`-owned folders. A skill is canonical once;
profiles decide who uses it.

## Skill Standard

Each canonical skill should keep the existing Codex/Claude-compatible shape:

```text
skills/<skill-name>/
  SKILL.md
  references/
  scripts/
  assets/
```

`SKILL.md` should include concise frontmatter and body instructions. Annabel
Press may read additional metadata from frontmatter when present:

```yaml
---
name: small-business-shopify-redesign
description: Draft-only Shopify redesign workflow for small business sites.
audience:
  - garry
  - business-partner
runtime:
  - claude
  - codex
visibility: private
related_cli_connections:
  - shopify
  - github
---
```

Keep `SKILL.md` lean. Long examples, policy details, command notes, and domain
reference material should live in `references/`.

## CLI Connection Standard

CLI connections should mirror skills, but use `CONNECTION.md` as the entrypoint:

```text
cli-connections/<connection-name>/
  CONNECTION.md
  references/
    commands.md
    safety.md
  scripts/
    check-installed.sh
    check-auth.sh
```

`CONNECTION.md` frontmatter should describe the tool and its safety model:

```yaml
---
name: shopify
display_name: Shopify CLI
binary: shopify
audience:
  - business-partner
runtime:
  - codex
visibility: private
related_skills:
  - small-business-shopify-redesign
safe_commands:
  - shopify theme list
  - shopify theme dev
  - shopify theme check
approval_required:
  - shopify theme push
  - shopify app deploy
---
```

The body should explain:

- when to use the CLI
- how to check install/auth state
- commands that are safe to run
- commands that require explicit approval
- where docs and troubleshooting notes live
- what secrets, credentials, or private data must never be exposed

CLI connection folders should never store credentials, API keys, private keys,
tokens, or customer secrets.

## Agent Profiles

Agent profiles should declare access instead of owning duplicate skills:

```text
agents/
  garry/
    profile.yaml
  business-partner/
    profile.yaml
  annie/
    profile.yaml
```

Example:

```yaml
agent: business-partner
skills:
  - review-claude-plan
  - implement-approved-plan
  - small-business-shopify-redesign
cli_connections:
  - github
  - shopify
  - skills-sh
```

Profiles should stay short. Operating manuals and detailed behavioral docs can
remain inside each agent folder.

## Annabel Press Views

Initial dashboard tabs:

1. Skills
   - Reads `AI-OS/skills/`
   - Shows name, description, audience, runtime, visibility, related CLIs,
     references, scripts, assets, runtime install status, and local usage count.

2. CLI Connections
   - Reads `AI-OS/cli-connections/`
   - Shows binary, install status, auth check status, safe commands,
     approval-required commands, related skills, references, scripts, and local
     usage count.

Later tab:

1. Workflows
   - Combines skills and CLI connections into named operating bundles.
   - Example: `small-business-shopify-redesign` + `shopify` + `github`.

## Migration Plan

1. Create top-level `AI-OS/skills/` and `AI-OS/cli-connections/`.
2. Inventory current skills from `AI-OS/skills/`.
3. Remove or archive legacy `agents/*/skills/` copies only after verifying the
   top-level skill is complete.
4. Add metadata to each `SKILL.md` for audience, runtime, visibility, and
   related CLI connections.
5. Create the first personalized CLI connections:
   - `shopify`
   - `github`
   - `skills-sh`
6. Create agent `profile.yaml` files that select from canonical skills and CLI
   connections.
7. Update runtime symlinks in `~/.claude/skills` and `~/.codex/skills`.
8. Add Annabel Press scanners and validation scripts.
9. Build the local dashboard once the filesystem model is stable.

## Validation Rules

Annabel Press should eventually validate that:

- every skill has `SKILL.md`
- every CLI connection has `CONNECTION.md`
- required frontmatter exists
- referenced skills and CLI connections exist
- runtime symlinks point to canonical AI-OS folders
- scripts referenced by docs exist
- no credentials or private keys are committed into capability folders
- approval-required commands are clearly marked

## Usage Tracking

Annabel Press tracks local usage with `usage/events.jsonl`.

This is private local bookkeeping, not external telemetry. A row should be
logged only when an agent materially uses a canonical skill or CLI connection
for Annabel's work.

Use:

```bash
operations/annabel-press/scripts/log-capability-use.mjs skill client-opportunity-map --agent annie --note "Mapped a client opportunity."
operations/annabel-press/scripts/log-capability-use.mjs cli shopify --agent business-partner --note "Checked draft theme status."
```

Do not log mere discovery, browsing, availability, or profile access.

## First Build Slice

The first useful version should be filesystem-first:

```text
AI-OS/
  skills/
  cli-connections/
  agents/*/profile.yaml
  operations/annabel-press/scripts/
```

Do not clone external Printing Press repos for v1. Use them as conceptual
inspiration only. Annabel Press should stay personalized to Annabel's actual
AI-OS workflows, not become a generic catalog.
