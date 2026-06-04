# Hop Alley — Video Walkthrough Script

**Target:** 60–90 sec. Conversational, not read-aloud.
**Recipient:** Tommy Lee (Chef / Owner)

**Tabs open before recording:**
1. `hopalleydenver.com` (homepage — scrolled to the top, awards strip visible)
2. A Perplexity tab with the query **"best sichuan restaurant denver"** already searched. Screenshot or keep the result page live — the Wok Spicy recommendation is the proof.
3. `hopalleydenver.com/menus` (or whichever Canva PDF menu loads — the point is the PDF-in-browser shell)
4. `hop-alley-audit.vercel.app` (portal landing page ready)
5. `hop-alley-audit.vercel.app/homepage-redesign.html` (mockup, scrolled to top)

Optional: incognito / second profile so no logged-in Squarespace chrome shows.

---

## 0:00 – 0:08 — Open

> "Hey Tommy, I'm Annabel — pulled together a quick walk-through of Hop Alley. Three things that jumped out, then I'll show you what a fix could look like."

*[Start on `hopalleydenver.com`, top of page.]*

---

## 0:08 – 0:45 — Three findings on the live site

**Finding 1 — Your awards are invisible to Google and AI** *(hover over the awards strip, then switch to the Perplexity tab)*

> "Seven awards on your homepage — three Bib Gourmands in a row, James Beard semifinalist, Michelin Exceptional Cocktails. All sitting as bold body text. Google and Perplexity can't read them — they need structured data to parse it."

*[Switch to the Perplexity tab, cursor the Wok Spicy paragraph.]*

> "We asked Perplexity for the best Sichuan restaurant in Denver. The winner was Wok Spicy — a suburban spot in Englewood, no Michelin, no James Beard. Hop Alley was mentioned as an also-ran. Wok Spicy won because their homepage says 'authentic Sichuan' plainly. Yours doesn't. That's the whole thing."

**Finding 2 — Your menus are trapped in Canva PDFs** *(switch tabs to the menus page)*

> "Every menu — main, vegan, pescatarian, gluten-free — lives as a Canva PDF. Google can't index Canva. So every search for 'mapo tofu denver,' 'dan dan noodles denver,' 'vegan chinese denver' bypasses your site — even though you serve every one of those dishes. Converting these to real HTML pages unlocks a category of traffic you're currently handing to competitors."

**Finding 3 — Your Chef's Counter ranks #1 with no page to capitalize** *(back to the homepage, scroll to where Chef's Counter is briefly mentioned)*

> "We checked — Hop Alley ranks number one in Denver for 'chinese tasting menu.' Almost zero competition, because the category barely exists. But there's no dedicated page, no bio, no photos, no booking CTA. You're sitting on the highest-margin product on the menu and the site does nothing with it. That's a page, not a project."

---

## 0:45 – 1:15 — Redesign reveal

*[Switch tabs to `hop-alley-audit.vercel.app/homepage-redesign.html`, scrolled to top.]*

> "Here's a rough mockup of what the homepage could look like with those three things addressed."

*[Point out, in order:]*

1. **Clear category positioning in the hero** — "Regional Chinese, specializing in Sichuan" — plus the three-peat Bib Gourmand and Michelin Cocktails recognition, above the fold. Same voice, same confidence — just legible to search engines and to anyone who's never been.
2. **A real press wall** — Michelin, James Beard, 5280, Westword, the cocktails award — with logos, pull-quotes, outbound links. Reads like a Michelin-tier site should.
3. **Chef's Counter elevated** — its own section pointing to a dedicated page, with room for Tock deep-linking and the kind of photography the concept deserves.

> "The brand stays yours — same voice, same typography, same Hop Alley confidence. The audit has the technical appendix too — copy-pasteable schema blocks for the awards, an FAQ block, an `llms.txt` template. All one-paste fixes."

---

## 1:15 – 1:30 — Close

*[Back on the portal landing page briefly.]*

> "I pulled the full audit plus a growth dashboard alongside — happy to share if any of it's useful. Either way, hope it helps — 2026 Michelin drops this fall, and the schema fix is a 30-minute job."

---

## Do / Don't

- **Do** record in one take if it feels natural. Re-record whole; don't edit.
- **Do** keep the cursor slow — fast mouse reads frantic.
- **Do** land the Perplexity moment clearly. It's the smoking gun. Let the Wok Spicy paragraph breathe for a full beat before moving on.
- **Do** pronounce it *see-chwan* (Sichuan) — matches their brand voice. "Szechuan" only shows up in the written audit as a spelling-variant note.
- **Don't** read verbatim. Script is guardrails, not a teleprompter.
- **Don't** apologize or hedge ("sorry if this is…", "I'm no expert but…") — the work is the credibility.
- **Don't** mention Uncle Ramen in the video — `Copy of HOME` and the broken phone link are in the written audit for a reason. Flagging them on camera reads as a dunk on his sister concept.
- **Don't** name Doug Rankin unless his status at the counter is confirmed beforehand. Scratchpad flagged this as pending. Safer: "the six-seat Chef's Counter." Add the name in a second take if confirmed.
- **Don't** mention the Tock/Resy contradiction, the delivery self-loop, the two H1 tags, or the `openingHours` trailing comma. Written audit handles all of it.
- **Don't** go past 1:30. If you hit 2:00, re-record shorter — the Perplexity finding is doing all the work.

## After recording

1. Save as `hop-alley-walkthrough.mp4` (or `.mov`).
2. Tell Claude the local path and the Hop Alley Drive folder id.
3. Claude will walk you through manual Drive upload (MCP can't handle files over ~1MB — video will be larger).
4. Paste the Drive share URL back to Claude → Claude writes `video-meta.json` + drafts 2–3 share-message options.
5. Click Share in Drive → add Tommy's email → paste message → Notify people ON → Send.
6. Run `/audit-outreach hop-alley` next — companion email draft gets generated from the audit findings (not yet written as of this session).
