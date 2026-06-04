# /session-email-draft

**When to use:** Right after a 1:1 client session. Turns Granola notes or a transcript into a client follow-up email. Replaces the current ChatGPT summarize → edit → email flow.

**How to use:**
1. Granola is running alongside FaceTime; the transcript is ready when the session ends.
2. Drag the Granola notes/transcript file into Cowork (or copy-paste the text).
3. Type `/session-email-draft` and the prompt below.
4. Edit the draft. Send.

---

## Prompt to paste

```
/session-email-draft

Granola notes or session transcript attached / pasted below.

Client first name (for salutation only — never used elsewhere):

[first name]

Anything specific you want named or held back from the email:

[optional — e.g. "don't mention the conversation about her sister, that was held space"]

Draft a follow-up email in my voice. This should feel like a thoughtful client email, not a clinical session note and not a generic coaching recap.

Before drafting, silently read for:
- the emotional thread of the session
- what the client is likely still carrying after the call
- what should be named back
- what should be held and left out

If the Granola notes are too thin, messy, or contradictory to draft safely, ask me for the missing context instead of guessing.

Use this exact structure:

1. SHORT WARM OPEN
   One or two sentences. Not "It was so great to see you!" — something that names the moment we landed in, not the appointment we kept.

2. THE THREAD
   In 2–4 sentences, name the through-line of what we worked on today.
   Use "you" and "we" — never "the client."
   Don't list everything we discussed. Pull the thread that mattered.

3. WHAT YOU SAID THAT'S WORTH SITTING WITH
   Pull 1–2 specific things the client said in their own words (paraphrased, not exact quotes unless the line was particularly hers) that are worth her returning to this week.
   Frame it as: "You said something like — [paraphrased line]. Sit with that."

4. THE INVITATION FOR THE WEEK
   One specific practice, question, or noticing for the week. Not "be gentle with yourself."
   Something concrete: "Notice the moment this week when you almost say yes and then catch yourself."

5. CLOSE
   One short line. My usual close is warm, brief, and unhurried. Sign as Marta. No emoji.

CRITICAL — read before drafting:
- Never quote vulnerable disclosures verbatim. Reference the theme, not the words.
- If anything in the transcript shouldn't be named back (something held in confidence by tone, not request), flag it before drafting.
- This is a private email between coach and client. Not marketing. Not coaching wisdom. The voice is the voice of the room we just left.
- Do not save anything from this transcript into content-memory.md. Client session material is not compounding memory.
- Length: 150–250 words. Anything longer reads as a deliverable, not a follow-up.

After the draft, give me TWO lines:
- "What I might be getting wrong:" — your honest read on what the email could miss.
- "What you might want to add:" — anything from the transcript I haven't included that you think matters.
```

---

## Notes on running this

- **Granola setup**: Granola listens to system audio with no bot in the call. It's the right fit for FaceTime sessions because Fathom/Otter both join calls as bots, which doesn't work on FaceTime and changes room energy. Granola is invisible.
- **The "what you might be getting wrong" line at the end is the safety net.** It catches when Cowork has flattened the conversation into generic coaching language.
- **If the email comes back generic on first try, paste back: "Reread the transcript. The specific thing she said about [X] is the email."** Cowork will revise sharper.
- **Confidentiality**: don't keep transcripts in the workspace longer than needed. Drop, draft, delete the upload. Cowork's per-conversation context is the right shape — don't pin transcripts to the workspace permanently.
