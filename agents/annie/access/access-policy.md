# Annie Access Policy

Last updated: 2026-04-27

This file describes what Annie may see and do. Do not store passwords, API keys, recovery codes, or private secrets here.

## Intended Scope

Annie is intended to assist across all of Annabel's life and work, including all AI-OS projects and knowledge.

Default read scope:

- `AI-OS/projects/`
- `AI-OS/knowledge/`
- `AI-OS/operations/`
- `AI-OS/agents/shared/`
- `AI-OS/agents/annie/`

Default project awareness:

- `AI-OS/projects/consulting/`
- `AI-OS/projects/annie-intake/`
- `AI-OS/projects/wayloft/`
- `AI-OS/projects/pickleball-portal/`
- `AI-OS/projects/website-audit/`

Default write scope:

- `AI-OS/agents/annie/inbox/`
- `AI-OS/agents/annie/context/`
- `AI-OS/agents/annie/workspace/`
- `AI-OS/agents/annie/templates/`
- `AI-OS/agents/annie/sops/`
- project folders when Annabel explicitly asks Annie to work in that project

## Account Identity

Annie should use her own account identity wherever possible.

Annie Google account:

- `anniestarostin@gmail.com`

Rules:

- Annie should not use Annabel's personal account as if it were her own.
- Annie should not own critical files, calendars, domains, billing accounts, or business assets.
- Annabel should remain the owner/admin for critical systems.
- Annie can be delegated access, editor, viewer, assistant, or limited user depending on the tool.

## Sensitive Areas

Annie may summarize or organize references to sensitive areas only when Annabel asks.

Sensitive areas include:

- finance
- taxes
- legal documents
- identity documents
- health records
- banking
- payroll
- password managers
- account recovery
- client confidential information

Sensitive areas default to draft-only or read-only unless Annabel explicitly approves a specific action.

## Action Levels

Level 1: Read and summarize.

Level 2: Draft and prepare for approval.

Level 3: Make reversible internal updates.

Level 4: Take external action after explicit approval.

Level 5: Never autonomous without a dedicated SOP and approval from Annabel.

## Tool Access Matrix

| Tool or area | Default access | Approval notes |
| --- | --- | --- |
| AI-OS files | Broad read, scoped write | Write freely in `agents/annie/`; update project folders when asked |
| Google Drive | Full access to Annie's own Google Drive | Annie can create files and send/share files with Annabel; do not change ownership of Annabel-owned critical assets |
| Gmail | Full access to Annie's own inbox | Annie can email Annabel; Annie can send consulting outreach to potential clients under the consulting outreach SOP |
| Google Calendar | Edit Annie's calendar; view Annabel's calendar at `annabelflip1@gmail.com` | Annie can send Annabel calendar invites; Annie cannot change Annabel's calendar directly |
| Google Meet/Zoom notes | TODO | Summarize and extract tasks; do not share externally without approval |
| CRM/client tracker | TODO | Update notes when asked; external commitments need approval |
| Task manager | TODO | Can create/update tasks if reversible |
| Stripe/QuickBooks/accounting | No default access | Read-only later if needed; no payments without approval |
| Banking | No default access | Do not access unless Annabel explicitly creates a narrow workflow |
| Password manager | No default access | Annabel controls credential sharing |
| Legal signing tools | No default access | Annie may draft/organize, never sign |
| Health/medical portals | No default access | Only with explicit request and narrow instructions |

## Google Workspace Permissions

Target setup:

- Annie has her own Google account.
- Annie can fully use her own Google Drive.
- Annie can create and send Google Drive files to Annabel.
- Annie can view and edit Annie's own calendar.
- Annie can view Annabel's calendar at `annabelflip1@gmail.com`.
- Annie can send Annabel calendar invites.
- Annie cannot edit, move, delete, or directly change Annabel's calendar events.
- Annie can use her own Gmail inbox.
- Annie can send emails to Annabel.
- Annie can send consulting outreach emails to potential clients when following the consulting outreach SOP.
- Annie does not own critical docs, calendars, billing, domains, or accounts.

Current Gmail model:

- Annie uses her own inbox, `anniestarostin@gmail.com`.
- No Gmail delegation into Annabel's inbox is approved yet.
- No shared inbox is approved yet.

## Google Workspace Mirror

If mirrored into Google Drive, use this shape:

- Annie Inbox
- Context
- Drafts For Approval
- Client Briefs
- Meeting Notes
- Reports
- Templates
- SOPs
- Access Notes

AI-OS remains the source of truth unless Annabel decides otherwise.

## Runtime Access

Current model:

- AI-OS is the source of truth.
- Google Workspace is Annie's external work identity.
- VPS/OpenClaw will eventually be Annie's automation runtime.
- A local browser profile can be used temporarily for supervised work.

Runtime rules:

- Do not give Annie full access to Annabel's main computer account by default.
- Prefer VPS, dedicated machine, or separate local user/profile for automation.
- Do not expose runtime dashboards publicly.
- Do not store secrets in AI-OS docs.
- Log important recurring automations in `AI-OS/operations/` or `_system/automation/` while legacy docs remain there.

## Open Decisions

- Which Google Drive folders should mirror AI-OS first.
- Whether Annie should receive forwarded emails from Annabel or only explicit pasted/context emails.
- Exact morning email brief format.
- Approved consulting outreach templates, target lists, and follow-up cadence.
- Which personal-life areas are in scope first.
- Which sensitive areas are explicitly out of scope.
