---
date: 2026-05-24
time: 17:40
project: cli-connections/imessage
status: complete
next-session: Build the standalone always-on relay + launchd keep-awake for phone-driven iMessage; fill remaining contacts.json handles.
---

# Session: iMessage Bridge Complete

## What we worked on

- Resumed in-progress work on a fully-local two-way iMessage bridge in
  `cli-connections/imessage/` (send.sh, read.py, contacts.json, README.md).
- Verified inbound: `read.py` reads `~/Library/Messages/chat.db` and decodes
  `attributedBody` (incl. reaction text). Full Disk Access already granted.
- Verified outbound: added `me -> +13038593694` to contacts.json and ran
  `./send.sh me "hi"`. Round trip confirmed via `read.py` (`me: hi`).
- Automation -> Messages permission already granted (send ran without prompt).

## Decisions made

- Bridge stays fully local: AppleScript out, sqlite read on chat.db in. No
  third-party service, no network.
- Test outbound by texting self (`me`) rather than messaging another person.
- Keep `me` in contacts.json as a permanent safe test target.

## Remote access (text from phone) — design decision

- HARD CONSTRAINT: iMessage has no cloud/server API. It can only be sent from a
  Mac or iPhone signed into the Apple ID. The send MUST run on this Mac; a VPS
  or cloud Claude cannot send iMessage and has no access to local chat.db.
- Telegram plugin (`~/.claude/channels/telegram/`) runs LOCALLY as a session-bound
  `bun server.ts` MCP process — it routes phone messages to a paired, *running*
  Claude Code session. No session = nothing receives. Phone chat ID 8519804405
  is already allowlisted (dmPolicy: allowlist).
- CHOSEN PATH: keep real iMessage from Annabel's own number; accept that the Mac
  must stay awake (not off). Use `caffeinate` to prevent sleep.
  - Temporary: run `caffeinate -s` in a SEPARATE terminal window (NOT via Claude,
    or it dies with the session). Keeps Mac awake while plugged in / lid open.
  - Permanent: a launchd agent that auto-runs caffeinate on login (to build).
  - caffeinate does NOT keep a closed-lid laptop on battery awake, and nothing
    works if the Mac is fully off — that combination is impossible for iMessage.
- Rejected: Twilio/cloud SMS (would work Mac-off but uses a different number,
  green-bubble SMS not iMessage, costs $). Off the table unless Mac-off becomes
  a hard requirement.

## Open questions

- Whether to wrap the bridge as a Claude skill / friendly command for routine use.
- Build the standalone always-on relay (launchd) so phone texts work without an
  open Claude session, vs. just keeping a dedicated session open.

## Next steps

1. Replace the `mom` placeholder (`+1XXXXXXXXXX`) and add any other real contacts.
2. Optional: thin skill or alias so Annie/Claude can send/read iMessage by name.
3. Note for portability: AppleScript `buddy of service` may break on future
   macOS releases — re-test a real send after major OS updates (README warns).

## Context to preserve

- Both macOS TCC permissions (Full Disk Access, Automation->Messages) are
  granted to the terminal launching Claude Code.
- contacts.json must use +E.164 handles. Keep it and any exported output private.
