---
date: 2026-04-27
time: 16:19
project: ai-os
status: complete
next-session: Review tomorrow morning's Annie email, then tune calendar/follow-up inputs and consulting outreach target workflow.
---

# Session: Annie onboarding, Google access, and morning brief upgrade

## What we worked on

- Established Annie as a first-class life-wide assistant under `agents/annie/`.
- Documented access model (what Annie can read vs do) + first SOPs (morning brief + consulting outreach).
- Confirmed the morning email sender runs via macOS `launchd` and verified a real SMTP send using Keychain credentials.
- Captured “don’t be repetitive” constraints (especially world news) for the morning brief.

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

## Next steps

- Check the next 7:00 AM scheduled email send after `launchd` runs naturally.
- Tune repetition filtering + section order after seeing a real morning brief.
- Decide whether to add Google Calendar read-in for the brief.
- Create the first approved consulting outreach target list + first batch.

## Context to preserve

- Annabel wants Annie to become a real assistant across her life, not just a consulting helper.
- Annabel wants useful morning emails, not repetitive news digests.
- News can be omitted when there is no meaningful update.
- Annie should help with consulting company outreach and may send emails to potential clients under the SOP.
- Preserve privacy and approval gates even though Annie has broad context.
