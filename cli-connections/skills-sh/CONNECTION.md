---
name: skills-sh
display_name: skills.sh CLI
binary: npx skills
audience:
  - garry
  - business-partner
runtime:
  - claude
  - codex
visibility: private
related_skills: []
safe_commands:
  - npx skills list
  - npx skills show
approval_required:
  - npx skills add
  - npx skills remove
  - npx skills update
---

# skills.sh CLI Connection

Use this connection when inspecting, installing, or packaging skills through the
`skills.sh` ecosystem.

## Safe Uses

- List installed skills.
- Inspect a skill before install or update.
- Compare runtime skill state with canonical AI-OS skills.

## Requires Approval

- Installing third-party skills.
- Updating or removing skills.
- Publishing, packaging, or changing runtime skill directories.

## Verification

- Run `scripts/check-installed.sh` before assuming `npx skills` works.
- Set `DISABLE_TELEMETRY=1` when using `npx skills` unless Annabel chooses
  otherwise.

Do not store registry credentials, package tokens, or private repo credentials in
this folder.
