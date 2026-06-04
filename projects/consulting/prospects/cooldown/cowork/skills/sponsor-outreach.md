# /sponsor-outreach

**When to use:** Before sending a first-touch email to a brand. You already know which brand and why — or you have paste-ready input from `/sponsor-research`. This skill just writes the email.

**Owner:** Bailey (also usable by chapter leaders launching a new city — see Mode B)

**How to use:** Pick a mode. Fill in the few inputs. Get an email draft back. Always drafts, never sends. If the brand fit, contact path, or ask is unclear, run `/sponsor-research` first.

---

## Mode A — National / HQ outreach

For long-term partnerships, product seeding, collabs, season-long sponsorship.

```
/sponsor-outreach mode=national

Brand: [e.g., Element]
Contact (if known): [name + role, or blank]
What we want from them: [e.g., product seeding for chapter leaders / co-branded apparel / city activation / open-ended partnership convo]
Why they're a fit (one line): [e.g., "their hydration product is what our Tuesday runners actually drink" / "they just sponsored Bandit so they're warm to run-club partners"]
Anchor (optional): [city, event, or chapter to ground the pitch — e.g., "Denver Tuesday run" or "the Boulderthon"]

Output:
1. WHY US (3 short bullets) — anchored in real Cool Down assets (15+ chapters, weekly meetups, chapter leader network, the apparel line). Specific, not generic.
2. WHY [BRAND] IS A FIT (2 short bullets) — using the "why they're a fit" input + one more if obvious from public signal.
3. EMAIL DRAFT — sentence case (it's an email). Subject ≤50 chars. Body ≤120 words. Cool Down voice — warm, specific, no hype. One concrete ask (15-min call / yes-no on seeding / intro to right person). Sign as Bailey.
4. ONE LINE: "What I'd want to confirm before sending:"

Rules:
- Don't lead with sponsorship $ — lead with seeding, activation, or community access.
- No "obsessed," "level up," "synergy."
- Never invent campaigns, exec names, or numbers about the brand. If unsure, write "[verify]" inline.
- Italics for emphasis, not caps.
```

---

## Mode B — Chapter launch outreach

For when a chapter is launching and you're inviting recurring Cool Down sponsors or local sponsors to come activate.

**Recurring sponsors** (default list, edit as relationships change): Element, Berry's Bootcamp, Garmin, Ultra.

```
/sponsor-outreach mode=chapter-launch

Chapter / city: [e.g., "Ann Arbor — University of Michigan, our 2nd college-targeted club"]
Launch date: [e.g., "October 27"]
Sponsor: [brand + recurring or local — e.g., "Garmin (recurring)" or "Running Lab (local Ann Arbor)"]
Contact: [first name + role if known, or blank]
Ask: [show up / table / send product / send a rep / giveaway / open-ended]
Prior relationship: [e.g., "sponsored Boulder launch last year" or "first time"]

Output: just the email draft. Match this style:

   "Hi Nicholas! I hope you are well. We are launching our second college-targeted club in Ann Arbor for University of Michigan on October 27th and we were wondering if Garmin would like to be a part of our launch? We would love to have you out!
   Thanks so much!"

Rules:
- Sentence case. First-name greeting + exclamation, warm.
- One sentence: what we're launching (city + school + date + which # club if relevant).
- One sentence: the ask (be specific if input names a specific ask — table, product, rep).
- Optional: one sentence referencing prior relationship if there is one.
- Warm close ("Thanks so much!").
- ≤80 words. No hype. No "[verify]" tags unless contact name is guessed.
```

### Batch mode

For a chapter launch, draft all recurring-sponsor emails in one pass:

```
/sponsor-outreach mode=chapter-launch batch=true

Chapter / city: [...]
Launch date: [...]
Sponsors: Element, Berry's Bootcamp, Garmin, Ultra
Contacts (if known): [pairs, e.g., "Garmin: Nicholas (partnerships)"]

Vary the angle per sponsor — don't reuse the same sentence with the brand name swapped.
```

### Chapter-leader-facing variant

If a student is starting a new chapter and needs *local* sponsors (running stores, cafés, gyms in their city), use Mode B with `Sponsor: [local brand name]` and `Prior relationship: First time`. Same warm short style.

---

## Notes

- **You drive the "why."** This skill assumes you already know why you're reaching out. It doesn't research the brand for you — it writes the email.
- **Pair with `/sponsor-research` when the fit is unclear.** Research decides whether a prospect is worth the email and fills the draft-ready input.
- **Pair with `/sponsor-follow-up` after sending.** Log brand, contact, mode, date sent, follow-up date, next action, and status so nothing slips.
- **For repeat brands with no reply:** add `Previous attempt: [date], no reply` to the input — the skill will propose a different angle, not the same email reworded.

## What this saves

Bailey's sponsor outreach is est. 5-10 hrs/week steady, plus spiky bursts every chapter launch. Mode A turns a 60-90 min "draft from scratch" into a 2-min input + 30-sec draft. Mode B replaces "draft 4 nearly-identical launch emails by hand" every chapter opening. **Estimated savings: 3-5 hrs/week steady + ~2 hrs per launch.**
