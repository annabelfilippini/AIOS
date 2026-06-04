# /audit-outreach — Short Follow-Up Email to Accompany the Drive Share

Step 9 of the pipeline. Draft a 3-sentence email that references the Drive-shared video and offers the portal as the "more if you want it" next step. The email is NOT the hook — the video is. This email is the optional companion note, sent the same day as the Drive share.

**Usage:** `/audit-outreach <prospect-name>`

One-phase: Claude drafts, Annabel reviews, Annabel sends. No programmatic sending.

## Good Example (Pepper Pong — hypothetical)

Drafted `prospects/pepper-pong/outreach-draft.md`: 3 subject line options, one tight body (greeting → one sentence on the video → one sentence on the portal → one-sentence close), sign-off with first name only. Total body reads aloud in ~8 seconds. Substance pulled from the existing `video-script.md` ("three things I found") and `audit-package` output (`pepper-pong-audit.vercel.app`). Never mentions money, never says "complimentary" or "portfolio," never hedges. Top of the file flags it as hypothetical since Tom is Annabel's dad and the Drive share alone is sufficient — the artifact exists to validate the pattern for prospect #2+.

## Tone Reference — Adam Matthews (real cold-share received Apr 14)

A stranger doing this same play sent Tom (Pepper Pong) a Drive share with exactly one sentence of companion text:

> Hi there, I just sent you an email with a video and figured I'd drop it here as well, in case it's easier to watch 🙂

Full breakdown saved at `prospects/_reference/adam-matthews-cold-share.md`. What to carry into every draft:

- **"In case it's easier…" framing** — give the recipient an out. Opposite of "please watch this."
- **Acknowledge the parallel channel casually.** If the video is in Drive AND email, say so in one phrase ("figured I'd drop it here as well"). Reduces friction.
- **One emoji at the end is fine** — warms cold contact without reading corporate. Don't stack them; one max, and only if it matches Annabel's voice in that specific send.
- **Open with what you did, not who you are.** No "I'm Annabel, I build…" preamble. The work speaks.
- **No CTA.** The video is the CTA. Email points at it.

## Bad Example

Wrote a 300-word "I've been working with AI tools and used your site as a case study..." email that repeats findings the video just covered. Or: led with a CTA ("I'd love to hop on a call") before the soft offer. Or: included a signature block with title, phone, LinkedIn — reads transactional. Or: used "Dear [Name]" or "I hope this email finds you well." Or: mentioned price / deliverables / scope — the video established value, the email should not re-pitch. Or: sent this email *before* the Drive share landed — the email becomes confusing ("what video?"). Or: forgot to personalize the subject line and sent "Site audit for [Business]" — reads like spam.

## Steps

1. **Read the prospect's `video-script.md`.** Pull: contact's first name, number of findings, the tone the video closes on. The email's voice should match the video's voice.

2. **Read the prospect's sheet row** (or ask Annabel) for:
   - `contact_name` → greeting
   - `url` → domain (strip protocol, strip trailing slash)
   - `channel` → if "text" or "DM", skip this skill; email is the only channel that needs this artifact

3. **Confirm the portal is live.** The body links to `https://<prospect-slug>-audit.vercel.app`. If `/audit-package` hasn't run yet, stop — the portal link is non-negotiable. If it's live, verify it loads.

4. **Write `prospects/$NAME/outreach-draft.md`** with this structure:
   - **Status block** at top — channel, timing ("same day as Drive share"), any special context (e.g., "hypothetical — Tom is Dad").
   - **3 subject line options** — conversational, no "audit" word, under 50 characters. Annabel picks the one that sounds like something she'd say out loud.
   - **Body** in a blockquote, 3 sentences + sign-off. Voice should read casual and low-pressure (see Adam Matthews reference above):
     1. Video reference: "Just shared a short walk-through of `<domain>` over Google Drive — figured I'd drop a note here too in case it's easier. [N] things I found that could help [one-phrase benefit], plus a quick mockup of what the fix could look like."
     2. Portal offer: "If anything in the video sticks, I also put the full audit and a growth dashboard here: `<portal-url>`"
     3. Soft close: "No pressure either way — hope it's useful 🙂" *(emoji optional, one max, only if it matches the specific send)*
     - Sign-off: `— Annabel` (first name only, no block).
   - **"What to personalize per prospect"** — list the fields (name, domain, N findings, portal URL, subject line).
   - **Send checklist** — Drive share sent first, portal loads on mobile, name spelled right, domain correct, reads in under 10 sec.
   - **Notes block** — preserve the "why so short" reasoning so future edits don't balloon it.

5. **Hand off to Annabel.** Tell her the draft is at `prospects/$NAME/outreach-draft.md`. Remind her:
   - Send the Drive share first (or in the same minute).
   - Update master sheet: status → `sent`, fill `sent_date` with today's date.

## Assumes

- **Expects:**
  - `prospects/$NAME/video-script.md` from `/audit-video` (voice + findings count reference)
  - `https://<prospect-slug>-audit.vercel.app` live from `/audit-package`
  - The prospect has an email address in the master sheet (`channel: email`)
- **Produces:**
  - `prospects/$NAME/outreach-draft.md` — ready to copy/paste into Gmail
- **Quality bar:**
  - Body reads aloud in under 10 seconds (≈ 45–60 words)
  - No money talk, no "complimentary," no "portfolio," no self-justification
  - Sign-off is first name only
  - Portal URL is the real live URL, not a placeholder
  - Subject line options all feel like something Annabel would say, not marketing copy

## Constraints

- **Never send.** Annabel sends every email. No SMTP, no Gmail API.
- **Never longer than 3 sentences in the body.** The video is the pitch. Email is context. Length creep is the #1 failure mode.
- **Never mention money, scope, or deliverables.** The value question is resolved by the video. Introducing price here kills the frame.
- **Never use "audit" in the subject line.** Reads transactional. "Walk-through," "a few ideas," "short video" all work better.
- **Skip entirely if channel is text/DM.** Those get a one-line iMessage, not a drafted email. If Annabel wants a text draft, she'll ask separately.

## Known Failure Modes

- **Too long.** Draft blooms to 5–7 sentences as "just one more thing to add" sneaks in. Fix: re-read BUILD-PLAN Step 9 ("2–3 sentences max"). Cut anything the video already said.
- **Repeats findings.** Email summarizes the three findings instead of pointing to the video. Fix: trust the video. Email says "three things I found" and links to the portal for depth.
- **Sales hedge.** "I'd love to," "if you'd be open to," "just wanted to reach out" — apologetic language undercuts the work. Fix: state what was sent, offer the portal, close. No hedges.
- **Wrong timing.** Email arrives before the Drive share — prospect opens to "what video?" Fix: Drive share first, email same minute or within the hour.
- **Formal sign-off.** "Best regards, Annabel Filippini | University of Michigan | annabelf@umich.edu" — reads transactional. Fix: `— Annabel` only.
- **Over-personalization-theater.** Mentioning something the prospect mentioned in a podcast 4 years ago reads like LinkedIn spam. Fix: the personalization is the audit itself. Don't stack.

## Relationship to Step 10

Step 10 is "delivery & tracking" — no skill, just sheet status progression. After this skill produces the draft and Annabel sends, she flips the sheet row to `status: sent` and fills `sent_date`. That's Step 10. Nothing else to automate at current volume.
