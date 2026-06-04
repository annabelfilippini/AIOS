# Marta AIOS — Internal Build Notes

**For:** Annabel (not Marta)
**What this is:** The internal scaffolding for Marta's Podcast & Speaking Thought Partner + Session Email Drafter, delivered via Claude Cowork. **Newsletter is explicitly out of scope** — Grace owns that end-to-end.

## Architecture choice

Mansel's AIOS pattern (CLAUDE.md kernel + context + memory + rules + skills + scheduling) — translated into Claude Cowork shape so Marta gets a real workspace with persistent context, file uploads, and skills in the chatbox. Cowork is a step up from ChatGPT Project: better critique writing, real file workspace, custom skills callable in chat.

See `recommendations.md` (one level up) for the layer mapping table — update it from "ChatGPT Project" to "Claude Cowork" when you re-share with Marta.

Why Cowork over ChatGPT Project:
- Sharper critique writing (the actual bottleneck for Marta — Grace already produces, she needs *editor*).
- Skills are callable in the chatbox like slash commands — closer to Mansel's AIOS feel without forcing her into a CLI.
- File workspace handles transcript uploads cleanly for the session→email pipeline.
- One subscription replaces the ChatGPT $20/mo (or runs in parallel during transition).

Why still not Claude Code / CLAUDE.md / crons:
- Cowork = browser. Claude Code = terminal. Marta is a browser user.
- Crons still violate the "no push notifications" rule. Calendar event + pull stays.

## Folder map

```
marta-aios/
├── README.md                    ← this file (internal)
└── cowork/                      ← what gets uploaded into Marta's Cowork workspace
    ├── instructions.md          ← paste into the workspace's system prompt / project instructions
    ├── context/                 ← upload as workspace files
    │   ├── voice.md             ← TODO: needs Marta's writing samples
    │   ├── audience.md          ← TODO: needs discovery follow-up worksheet
    │   ├── offers.md            ← drafted from research-brief
    │   ├── podcast-truths.md    ← TODO: needs 3-5 episode listen pass
    │   └── content-memory.md    ← compounding podcast/speaking memory; no client details
    └── skills/                  ← prompt library — Marta calls in the chatbox
        ├── speaking-prep.md
        ├── podcast-pressure-test.md
        └── session-email-draft.md   ← the recording→email pipeline
```

## Scope — what's in and what's out (updated 2026-04-26)

**In scope** (Cowork helps):
- Podcast — pressure-testing ideas before recording
- Speaking — prep for talks, parent nights, graduation speeches, podcast guest appearances
- 1:1 sessions — recording fix (Granola) + email draft after every session

**Out of scope** (Grace owns, hands off):
- Newsletter drafting (Grace writes Marta's newsletter end-to-end)
- Podcast audio editing
- Social media reels
- Circle membership content

If Marta tries to use Cowork for newsletter, the system instructions tell it to redirect her to one of the in-scope skills.

## The session recording → email pipeline

Marta runs sessions on FaceTime. Current workflow: records on something that cuts off every few minutes, summarizes with ChatGPT, edits, sends.

Proposed:
1. **Granola** runs alongside FaceTime — captures system audio, transcribes live, doesn't cut off, no bot in the call. (Fathom and Otter both require joining as a meeting bot, which is awkward on FaceTime. Granola is the right fit because it listens to system audio passively.)
2. After the session, Marta drags the Granola transcript into Cowork and types `/session-email-draft`.
3. The skill produces a follow-up email in her voice, framed around the moments that mattered, not a generic recap.
4. Marta edits and sends.

This replaces her current "record → ChatGPT summarize → edit → email" flow with a tighter "record → drop → draft → edit" flow. Same shape, fewer steps, no recording cutoff, sharper draft because the workspace knows her voice.

**Confidentiality flag:** session transcripts contain vulnerable client material. The skill must be written to never refer back to client-identifying details across chats, never store specifics in memory, and treat transcripts as one-shot. Build this into `instructions.md` and into the skill prompt itself.

## Build status

- [x] Recommendations doc (Marta-facing) — needs platform-rename pass before reshare
- [x] Internal README (this file)
- [x] Custom instructions (instructions.md)
- [x] Skill: speaking-prep.md
- [x] Skill: podcast-pressure-test.md
- [x] Skill: session-email-draft.md (the pipeline skill)
- [x] ~~Skill: newsletter-tension-check.md~~ — DELETED. Grace owns newsletter end-to-end (confirmed 2026-04-26). Out of scope.
- [x] Context: offers.md (built from research-brief, updated to mark newsletter as Grace's)
- [x] Context: voice.md v0.2 — re-grounded after newsletter scope change. Newsletter samples now flagged as Grace-filtered, not raw Marta. Trustworthy voice signal: podcast (LISTEN-PASS), session emails (need 2-3 de-identified samples), speaking drafts.
- [ ] Context: audience.md (need 30-min worksheet call with her)
- [x] Context: podcast-truths.md v0.5 — built from show-notes pattern read on 10 recent episodes. Tagged `LISTEN-PASS` where audio confirmation needed (spoken cadence, opening/closing signatures, Part 2 quality test).
- [x] Context: content-memory.md v0.1 — compounding memory for podcast/speaking threads; explicitly excludes client session details.
- [ ] One-page how-it-works for Marta (post-handoff doc)
- [ ] Loom script (under 3 min per playbook)
- [ ] Granola setup how-to (under 1 page, screenshots)

## Recording tool decision

Granola, not Fathom or Otter. Reasoning:
- **FaceTime compatibility.** Granola listens to system audio. No bot to invite. Fathom and Otter are built around Zoom/Meet/Teams calendar invites; FaceTime breaks that model.
- **No bot in the room.** Vulnerable client conversation — a third "participant" called "Otter Bot" changes the room energy. Granola is invisible.
- **Mac-native.** Marta is on Mac (confirmed via her stack). Granola is Mac-first.
- **Long sessions.** No cutoff issue.
- **Cost.** Free tier covers individual use. $18/mo Pro if she wants unlimited.

Backup if Granola breaks: Otter desktop app in "auto-record" mode — also captures system audio, slightly worse UI.

## Pull-not-push rationale (no crons)

Unchanged. Marta consolidated her week, protected weekends. Pushing morning briefings restores the noise she escaped. Single Mon 9am calendar event with `"Open Cowork → /weekly-content-review"` does the work without the maintenance burden.
