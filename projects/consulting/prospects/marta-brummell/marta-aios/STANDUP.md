# Marta Cowork Workspace — Stand-Up Guide

**For:** Annabel
**Goal:** Working Cowork workspace for Marta, demo-ready for the 12:30 Cool Down call.
**Time:** ~15 min if Cowork is already on your account; +5 min if you have to enable it.

---

## 0. Before you start

- Open: https://claude.ai/cowork (or claude.ai → Cowork in the left nav)
- Have these files open in Finder, ready to drag:
  - `cowork/instructions.md`
  - `cowork/context/voice.md`
  - `cowork/context/audience.md`
  - `cowork/context/offers.md`
  - `cowork/context/podcast-truths.md`
  - `cowork/context/content-memory.md`
  - `cowork/skills/speaking-prep.md`
  - `cowork/skills/podcast-pressure-test.md`
  - `cowork/skills/session-email-draft.md`

---

## 1. Create the workspace (2 min)

1. Click **+ New project** (or "New Cowork").
2. **Name:** `Marta — Practice & Speaking`
3. **Description (optional):** `Private podcast + speaking thought partner; session email drafter. Newsletter is Grace's lane — out of scope.`

---

## 2. Paste the system instructions (3 min)

1. Open `cowork/instructions.md` in a text editor.
2. Copy everything **below the `---` divider on line 5** (start at "You are Marta Brummell's…", end at the bottom of the file).
3. In Cowork → project settings → **Custom instructions** (or "System prompt") field → paste.
4. Save.

> **Don't paste the top header / "Paste this into…" line — that's the meta instruction, not the prompt itself.**

---

## 3. Upload context files (3 min)

In the workspace's **Files** / **Knowledge** panel, drag-upload all five:

- `voice.md`
- `audience.md`
- `offers.md`
- `podcast-truths.md`
- `content-memory.md`

**Heads up before the demo:** these files are honestly status-tagged (`v0.1`, `v0.2`, `v0.5`, `LISTEN-PASS` markers, `TODO`s). That's fine — for Cool Down it actually shows your methodology: you don't fake context, you mark what's known vs. what needs more discovery. If you'd rather not show the TODOs, upload `audience.md` *after* the call.

---

## 4. Register the three skills (5 min)

Cowork skills can be installed two ways depending on what your account shows. Try Path A first; fall back to Path B.

### Path A — Native skills (if your Cowork has a "Skills" tab)

For each of the three `.md` files in `cowork/skills/`:
1. Click **+ Add skill**.
2. **Name:** the filename without `.md` (e.g., `speaking-prep`).
3. **Trigger:** `/speaking-prep` (etc.)
4. **Body:** paste the `## Prompt to paste` block from the file (the fenced code block — don't include the surrounding markdown notes).
5. Save. Repeat for all three.

### Path B — Skills-as-files (if no Skills tab)

Drag-upload all three skill `.md` files into **Files** alongside the context files. Then add this to the bottom of your system instructions:

```
## Skills (callable by name)

When Marta types one of these, follow the format in the corresponding uploaded file exactly:
- /speaking-prep → speaking-prep.md
- /podcast-pressure-test → podcast-pressure-test.md
- /session-email-draft → session-email-draft.md
```

Either path works for the demo. Path A is cleaner-looking on screenshare.

---

## 5. Smoke test (3 min) — DO NOT use a real session

**Critical:** for the Cool Down demo, do **not** use a real Marta session transcript. Use the synthetic one below. (Real client material is confidential and the workspace's instructions explicitly say transcripts are one-shot.)

In a new chat, paste:

```
/session-email-draft

Session transcript attached / pasted below.

Client first name (for salutation only — never used elsewhere):
Jamie

Anything specific you want named or held back from the email:
Don't mention the work conversation about her boss — that was held space.

[SYNTHETIC TRANSCRIPT — DEMO USE ONLY]

Marta: How are you walking in today?
Jamie: Tired. I had this whole week where I kept saying yes to things and then resenting them by Thursday.
Marta: Tell me about the one that's still sitting with you.
Jamie: My mom called Sunday. She wanted me to fly out for her birthday. I said yes before I even thought about it. Then I spent three days angry about it.
Marta: What was the moment between the question and the yes?
Jamie: There wasn't one. That's the thing. It was reflex.
Marta: And if there had been a moment?
Jamie: I don't know. I think I would've said — let me check, let me think about it. Just that. Just a pause.
Marta: What does the pause feel like in your body when you imagine it?
Jamie: ...calmer. Like I have a chest again.
Marta: Stay there for a second. The "I have a chest again" — that's the practice.
Jamie: ...yeah.
Marta: What would change this week if you took one pause like that, before one yes?
Jamie: I'd be less furious by Friday probably. (laughs) That's a low bar but it's real.

[END SYNTHETIC TRANSCRIPT]

Draft a follow-up email in my voice. Use the structure in /session-email-draft.
```

**What to look for in the output:**

- ✅ Opens with a moment, not "great session today!"
- ✅ Pulls "I have a chest again" or the pause language as the thread
- ✅ One concrete invitation for the week (not "be gentle with yourself")
- ✅ 150–250 words
- ✅ Two final lines: "What I might be getting wrong" + "What you might want to add"
- ✅ Does NOT mention the held-back boss conversation
- ❌ If it sounds generic, paste back: *"Reread the transcript. The 'I have a chest again' line is the email."* It will revise sharper.

---

## 6. (Optional, 2 min) Test one more skill on screenshare

For the Cool Down demo, run one of these on the call so they see a second skill in action:

- `/podcast-pressure-test` with: *"Episode idea: how saying yes too fast is a body-level habit, not a willpower problem. Want to use Jamie's session moment as the spine."*
- `/speaking-prep` with: a 3-sentence outline of a fake parent talk.

Don't do both. Pick whichever matches the energy of the call.

---

## If something breaks

- **Skills don't trigger on `/`** → use Path B (skills-as-files in custom instructions). Restart the chat after editing.
- **Output sounds generic / breaks voice rules** → ask: *"Reread voice.md. Fix the lines that violate rules 1, 2, or 5."* (Reference rule numbers.)
- **Cowork can't find an uploaded file** → re-upload, then start a new chat (uploads sometimes don't propagate to existing chats).
- **You hit time pressure (it's past 11:30)** → ship what works, fall back to walking Cool Down through the `.md` files in the repo via screenshare. The artifacts are the credibility, the workspace is the polish.

---

## Demo flow for Cool Down (2 min on the call)

1. Open the workspace. Show the **Files** sidebar — `voice.md`, `audience.md`, `offers.md`, `podcast-truths.md`. Say: *"This is what I built for Marta — her voice, her audience, her offers, her podcast patterns. The system reads this every time."*
2. Open the **Skills** sidebar (or scroll instructions). Show the three slash commands. Say: *"Each of these is a workflow we identified in our 45-min audit. She calls them in the chatbox like a teammate."*
3. Run `/session-email-draft` with the synthetic transcript pre-staged. Watch the draft come back in her voice in ~30 seconds.
4. Pivot: *"That's what an AIOS for an expert-led business looks like. The interesting question is what the first few skills look like for you two."*

That's the bridge into your Cool Down skill drafts (task #4).
