# Adelitas — Video Walkthrough Script

**Target:** 60–90 sec. Conversational, not read-aloud.
**Recipient:** Silvia Andaya (Owner / Executive Chef)

**Tabs open before recording:**
1. `adelitasco.com` (homepage — the "Broadway / Edgewater" location picker, scrolled to top)
2. `adelitasco.com/tequilas-family-mexican-restaurant` (the page where the Silvia + Michoacán story is currently buried)
3. `adelitas-audit.vercel.app` (portal landing page ready)
4. `adelitas-audit.vercel.app/homepage-redesign.html` (mockup, scrolled to top)

Optional: a second browser profile or incognito so no logged-in admin UI shows.

---

## 0:00 – 0:08 — Open

> "Hey Silvia, I'm Annabel — made a quick walk-through of Adelitas. Three things I found, then I'll show you what a fix could look like."

*[Start on `adelitasco.com`.]*

---

## 0:08 – 0:40 — Three findings on the live site

**Finding 1 — Your homepage isn't a homepage** *(stay on adelitasco.com, cursor the two location cards)*

> "When anyone lands on adelitasco.com — a customer, a food writer, Google itself — this is what they see. A location picker. No food, no chef, no La Adelita story, no reservation link. Every press mention and every backlink points here, and there's nothing for Google to rank or a customer to read."

**Finding 2 — Reservations are hiding** *(cursor the nav, then mime a dead end)*

> "People are actively searching 'adelitas denver reservations' — it's the fourth most-typed query after your name. Your OpenTable page exists, it's live right now, but it's not linked from the site anywhere. They have to leave your site and go find you on OpenTable. A lot of them won't."

**Finding 3 — Your chef is your brand and nobody knows her** *(switch tab to `/tequilas-family-mexican-restaurant`)*

> "Silvia, the Michoacán-lineage three-restaurant story — Adelitas, La Doña, Ni Tuyo — is the single strongest brand story I've seen on a Denver restaurant site. But it's buried inside an SEO URL nobody's going to type. Press doesn't read SEO pages, they read Chef pages. You don't have one."

---

## 0:40 – 1:15 — Redesign reveal

*[Switch tabs to `adelitas-audit.vercel.app/homepage-redesign.html`, scrolled to top.]*

> "Here's a quick mockup of what this could look like."

*[Point out, in order:]*

1. **Real homepage at `adelitasco.com`** — hero of the room, the La Adelita heritage in two sentences, menu preview, reservation CTAs for both Broadway and Edgewater. The location picker becomes a dropdown in the header where it belongs.
2. **Reservations button in the nav** — one click to OpenTable for either location, from every page on the site.
3. **A real chef section** — Silvia, Michoacán, the three-restaurant universe, cross-linked to La Doña and Ni Tuyo in the footer. Editorial, not SEO.

> "The brand stays yours — same La Adelita iconography, same warmth, same voice. I just lifted the story out of the back of the site and put it where people actually land."

---

## 1:15 – 1:30 — Close

*[Back on the portal landing page briefly.]*

> "I pulled this together as a full audit plus a growth dashboard too — happy to share if it's useful. Either way, hope this helps."

---

## Do / Don't

- **Do** record in one take if it feels natural. Re-record whole; don't edit.
- **Do** keep the mouse slow and deliberate — fast cursor movement reads frantic.
- **Do** pronounce "Michoacán" as *mee-cho-ah-KAHN* — the cultural specificity is the whole point.
- **Don't** read verbatim. Use the script as guardrails, not a teleprompter.
- **Don't** apologize or hedge ("sorry if this is...", "I'm no expert but...") — the work is the credibility.
- **Don't** mention the doorway-page / Google-policy risk in the video. It's in the written audit for a reason — too technical for a 90-sec hook and risks sounding alarmist.
- **Don't** go past 1:30 — if you hit 2:00 on the timer, re-record shorter.

## After recording

1. Save as `adelitas-walkthrough.mp4` (or `.mov`).
2. Tell Claude the local path and the Adelitas Drive folder id.
3. Claude will walk you through manual Drive upload (MCP can't handle files over ~1MB — video will be larger).
4. Paste the Drive share URL back to Claude → Claude writes `video-meta.json` + drafts 2–3 share-message options.
5. Click Share in Drive → add Silvia's email (`info@adelitasco.com`) → paste message → Notify people ON → Send.
6. Run `/audit-outreach adelitas` next — companion email draft is already at `outreach-draft.md` and ready to go.
