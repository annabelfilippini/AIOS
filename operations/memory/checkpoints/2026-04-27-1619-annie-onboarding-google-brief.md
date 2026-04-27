---
date: 2026-04-27
time: 16:19
project: ai-os
status: complete
next-session: Review tomorrow morning's Annie email, then tune calendar/follow-up inputs and consulting outreach target workflow.
---

# Session: Annie onboarding, Google access, and morning brief upgrade

## What we worked on

- Created Annie as a first-class life-wide assistant agent under `AI-OS/agents/annie/`.
- Updated core AI-OS docs so Annie is recognized alongside Claude and Codex.
- Reviewed historical source repos:
  - `https://github.com/annabelfilippini/life-os`
  - `https://github.com/annabelfilippini/Personal-Canon`
- Incorporated durable personal canon and old Life OS lessons into current AI-OS context without treating stale details as current truth.
- Filled in Annie's Google account and access model.
- Created first Annie SOPs for morning brief and consulting outreach.
- Inspected the existing Annie morning email automation and confirmed it runs through Mac `launchd`, not Mac cron.
- Updated the morning email sender/format/repetition behavior.
- Added Annie's Gmail app password to macOS Keychain and verified a real SMTP send.

## Files changed or created

- `AI-OS/agents/annie/README.md`
- `AI-OS/agents/annie/context/operating-manual.md`
- `AI-OS/agents/annie/context/personal-canon-summary.md`
- `AI-OS/agents/annie/access/access-policy.md`
- `AI-OS/agents/annie/sops/morning-brief.md`
- `AI-OS/agents/annie/sops/consulting-outreach.md`
- `AI-OS/agents/README.md`
- `AI-OS/AGENTS.md`
- `AI-OS/USER.md`
- `AI-OS/SOUL.md`
- `AI-OS/CLAUDE.md`
- `AI-OS/README.md`
- `AI-OS/_system/automation/annie-morning-brief.md`
- `AI-OS/projects/annie-intake/scripts/email-briefing.py`
- `AI-OS/operations/memory/refinement-candidates/2026-04-27-life-os-personal-canon-import.md`

## Decisions made

- Annie belongs in `AI-OS/agents/annie/`, not inside only the consulting project, because she is intended to assist across all projects and personal/business operations.
- AI-OS is Annie's source of truth.
- Google Workspace is Annie's external work identity.
- VPS/OpenClaw is the execution/runtime layer once healthy.
- Annie may broadly read AI-OS context, but action permissions are narrower.
- Annie's Google account is `anniestarostin@gmail.com`.
- Annie can view and edit her own calendar.
- Annie can view Annabel's calendar at `annabelflip1@gmail.com`.
- Annie can send Annabel calendar invites, but cannot directly edit Annabel's calendar.
- Annie can use her own Gmail inbox and Google Drive.
- Annie can email Annabel.
- Annie can send consulting outreach to potential clients when following an approved SOP, approved positioning, and approved target list.
- Morning news should not repeat day to day. If there is no meaningfully new world news, Annie/OpenClaw should omit the world news section.

## Morning email automation state

Existing path:

```text
VPS/OpenClaw generates briefing markdown
GitHub/wiki-cache syncs locally
Mac launchd runs email-briefing.py at 7:00 AM
Gmail SMTP sends the email
```

LaunchAgent:

- `~/Library/LaunchAgents/com.annabel.annie.briefing-email.plist`

Script:

- `AI-OS/projects/annie-intake/scripts/email-briefing.py`

The updated script:

- Prefers sender `anniestarostin@gmail.com`.
- Uses Keychain service `annie-briefing-gmail`.
- Falls back to legacy sender `annabelflip1@gmail.com` with service `daily-briefing-gmail` if Annie's credential is missing.
- Changes the subject to `Annie Morning Brief - Mon DD`.
- Adds a command-center section.
- Adds open follow-ups from `outputs/todos.md`.
- Adds consulting outreach context from active consulting prospect folders.
- Filters repeated briefing items against the previous 7 days.
- Uses a more aggressive repeat filter for world news.
- Omits raw source lists from the email body.
- Supports `ANNIE_BRIEFING_DRY_RUN=1` to generate `scripts/logs/email-preview.html` without sending.

Verification:

- Dry run succeeded.
- Keychain item was verified outside the sandbox.
- Real send succeeded:
  - from: `anniestarostin@gmail.com`
  - to: `annabelflip1@gmail.com`

## Important caveats

- The `AI-OS/projects/annie-intake` repo already had unrelated local modifications before the morning email edits:
  - `DESIGN.md`
  - `README.md`
  - `scripts/wiki-pull.py`
  - untracked `wiki-cache/`
- Those pre-existing changes were not reverted.
- `AI-OS` root itself is not a git repo.
- The current morning email script does not yet read Google Calendar directly. It only notes that calendar access is documented.
- Consulting outreach in the morning email currently reports active prospect folders, not live inbox replies or a CRM state.

## Open questions

- Did the real Annie test email arrive visibly in Gmail, or did it land in spam/promotions/all-mail?
- Should the 7-day repetition window be shorter or longer?
- Should repeated world news be filtered by topic/entity more aggressively than the current title-based heuristic?
- What should count as a "new" world-news update worth including?
- Which Google Drive folders should mirror AI-OS first?
- Should Annie receive forwarded emails from Annabel, or only explicit pasted/context emails for now?
- What exact consulting outreach target list should Annie start with?
- Should Annie create a prospect tracker sheet/doc in her Google Drive?
- Which personal-life areas should Annie help manage first?

## Next steps

- Check tomorrow morning's 7:00 AM email after launchd sends it naturally.
- If it does not arrive, inspect:
  - `AI-OS/projects/annie-intake/scripts/logs/email-stdout.log`
  - `AI-OS/projects/annie-intake/scripts/logs/email-stderr.log`
  - today's dated log in `scripts/logs/`
- Tune the morning email format after seeing one live send.
- Add a calendar-reading integration or a manual calendar export step if calendar items should be included.
- Create an approved consulting outreach target list and first outreach batch for Annie.
- Consider adding an Annie `mistakes.md` or `lessons.md` once she starts operating regularly.

## Context to preserve

- Annabel wants Annie to become a real assistant across her life, not just a consulting helper.
- Annabel wants useful morning emails, not repetitive news digests.
- News can be omitted when there is no meaningful update.
- Annie should help with consulting company outreach and may send emails to potential clients under the SOP.
- Preserve privacy and approval gates even though Annie has broad context.
