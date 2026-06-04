# AIOS Audit Intake — Dad's 4-Company Entity

**Date:** 2026-05-14
**Audience:** Dad — what the audit does, what we need from you, what you get
**Companion to:** `plan-v1-2026-05-14.md` (the build plan that happens *after* this intake)
**Who edits the outputs:** You (comfortable in Obsidian), Josh (non-technical co-owner across all 4 companies), and every employee who comes later. The audit picks an editing surface that fits all three — see *Editing the canon after it's locked* below.

---

## The one-paragraph summary

Before we build anything for Erica, we need a clean picture of two things: (1) your current system — what's in your Obsidian vault, what tools and accounts already exist, what's missing — and (2) each of your four companies' voice, customer, offer, business shape, and goals. The audit produces both by **reading what you already have**, not by handing you a 50-question form. It scans your vault, your tools, your channels, and comes back with a normalized canon per company *plus* a target architecture, a setup checklist, and a pilot recommendation. Only the handful of things it genuinely can't infer get sent back to you as voice-memo questions. Total time from you: ~55 minutes across 3 days.

---

## How the audit runs (where the work happens)

The audit is a Claude Code skill that runs **on your laptop**. Your vault, your Gmail, your Granola transcripts, your LinkedIn — none of it leaves your machine. Tokens stay local, files stay in your vault.

Annabel is on a screenshare twice: once at setup (~20 min, to point the audit at the right places and catch anything weird while it kicks off) and once at review (~20 min, to walk the outputs together). Everything in between is autonomous on your end — the audit just runs.

You're the operator. She's the co-pilot. This is also how the product will work for everyone else later; you're the v0.

---

## What we need from you (total: ~55 minutes)

| Step | What you do | Time |
|---|---|---|
| 1 | Setup screenshare with Annabel — point audit at your vault, run OAuth (Gmail / Granola / LinkedIn), share four company URLs + existing tool accounts and plan tiers | ~20 min |
| 2 | Answer ~5 voice-memo questions per company (the only stuff the audit can't extract) — solo, on your time | ~15 min |
| 3 | Review screenshare with Annabel — skim the outputs together, mark anything wrong | ~20 min |

That's it. No form. No spreadsheet. No interviews. Two short calls and some voice memos.

---

## What the audit does autonomously (zero work from you)

**System scan** (across the whole entity):

- Walks your Obsidian vault — every note, every linked file, every folder. Indexes structure and content.
- Inventories the tool stack — what's already set up (Granola? Beehiiv? Anthropic Team?) and what plan tier each is on.
- Identifies what's missing for the target architecture (Supabase, Cloudflare Workers, Anthropic Team-plan seats, vault sync).
- Flags anything misconfigured (e.g. Granola on a tier that doesn't expose the transcript API).

**Per-company scan** (for each of CFS, Falcon, FSL, plus a lighter pass on AIH):

- Your vault notes / subfolders / tags belonging to that company. Every document, deck, PDF, brand guideline, proposal, case study. OCR on images.
- Your company website. Every page. Copy, offer language, headlines, About, services.
- Your company LinkedIn page. Posts, About, recent activity.
- Your personal LinkedIn (founder voice signal). Last 90 days of posts and comments.
- Your sent Gmail, filtered to outbound emails you wrote yourself. Voice samples.
- Your Granola transcripts if they exist. Sales calls, client calls — ICP language, objections, customer wording.
- Your newsletter archive if there is one. Tone samples.
- Public testimonials and case studies wherever they live.

For AIH (holding co) the scan is lighter — identity, structure, founder-level voice. No operational canon needed.

---

## What you get back

A package containing seven things:

1. **System inventory** — what you have today, what's missing, what's misconfigured. One page.
2. **Target architecture** — the layers diagram annotated for your specific stack (Obsidian vault + sync, Supabase, Cloudflare, Cowork on the Anthropic Team plan, Blotato, etc.).
3. **Per-company normalized canon** — for each company, a folder like this:

```
canon/cfs/_normalized/
  voice.md         ← how CFS talks
  icp.md           ← who CFS sells to
  offer.md         ← what CFS sells
  business.md      ← what CFS is
  goals.md         ← what CFS wants in 6-12 months (this one needs you)
  _gaps.md         ← what the audit couldn't find
  _evidence.md     ← quotes from your materials backing every claim
```

4. **Setup checklist** — exact accounts to create, plan tiers to pick, settings to configure, in what order, with monthly cost estimates. You work through it (Annabel on a call if you want); spend is your call.
5. **Co-owner + employee onboarding template** — the repeatable pattern for how Josh (next, as co-editor of the canon) and then each employee plug into the system. Means Josh's onboarding is hours, not weeks — and each hire after that is the same.
6. **Pilot recommendation** — which of the four companies goes first, with the reasoning.
7. **Build order** — the `plan-v1` sequence adjusted for your actual starting point.

---

## The intake flow, step by step

### Step 1: Setup screenshare (Day 1 AM, ~20 minutes)

You hop on a call with Annabel and together you:

1. **Point the audit at your Obsidian vault.** It's already on your laptop; the skill just needs the path. If your vault isn't synced anywhere yet, this is when we'd note that for the setup checklist (sync goes in later, not blocking for the audit).
2. **Run OAuth for Gmail, Granola, LinkedIn** — three one-click approvals in your browser. Tokens land in your machine's local store, not Annabel's.
3. **Drop in the four company URLs** — paste them into the skill prompt.
4. **List existing tool accounts** — quick read-out: *"I have Anthropic Team, Beehiiv on Scale, Granola personal, no Supabase, no Cloudflare."* The audit needs this to avoid recommending things you already pay for.
5. **Name anything you don't want scanned** — folders, channels, anything. Default is the whole vault; exclusions are respected.

At the end of the call, the audit is running. Annabel can hop off; you don't need to babysit it.

### Step 2: Scan & Normalize (Day 1 PM → Day 2, zero from you)

The audit runs on your laptop. It walks your vault, inventories your tools, scans your websites and channels, and writes:

- The system inventory + target architecture
- The four `_normalized/` canon drafts
- The setup checklist
- The employee onboarding template

Every extraction gets logged with a citation back to the source — so when you read it you can see *why* the audit decided your voice is "warm but technical" or your ICP is "ops leaders at 50-200 person services firms."

### Step 3: Gap questions (Day 2, ~15 minutes from you)

Per company, the audit comes back with the short list of things it genuinely cannot infer. Usually the same six categories:

1. **Goals for the next 6-12 months.** Revenue target? Hires? New product launch? *(Not in any document.)*
2. **Why this company exists separately.** What's the strategic reason CFS is CFS and not folded into Falcon? *(Sometimes inferable, cleaner to ask.)*
3. **ICP exclusions.** Who do you actively say no to, and why? *(Usually invisible in marketing materials.)*
4. **Top 3 objections** you hear that aren't already in transcripts. *(Skipped if Granola history is rich.)*
5. **What would be most valuable if Erica had it drafted for her tomorrow?** *(Forces a prioritization signal.)*
6. **Plan tiers and existing accounts** *(asked once, not per company)* — confirm what's paid for so the setup checklist doesn't double-spend.

You answer by **voice memo** — phone, Granola, whatever. 2-3 minutes per company. Audio gets transcribed and slotted into the right `_normalized/` files. **No typing required.**

### Step 4: Review screenshare (Day 3 AM, ~20 minutes)

You and Annabel jump back on a call. The audit's outputs are already sitting in your vault: system inventory, target architecture, four normalized canons, setup checklist, onboarding template. You walk them together. For anything wrong, you say so (in the moment, or via a voice memo right after — whichever is fastest). The audit updates and everything locks.

### Step 5: Deliverable + handoff to build (Day 3–4)

Locked canon files live in your Obsidian vault at `canon/<company>/_normalized/`. The setup checklist becomes your build queue — Annabel can co-pilot on a call as you work through it, or you run it solo and ping her when stuck. The `plan-v1` build sequence kicks off against the pilot company the audit recommended.

---

## Per-company expectations

### AIH (holding company)

Light scan. We extract your founder identity, the holding-co structure, anything brand-level that spans all four. No operational canon needed — there's no Erica equivalent doing AIH-specific work. **Expected gap question count: 1-2.**

### CFS

Full scan. Likely one of the two pilot candidates. **Expected gap questions: 3-5.**

### Falcon

Full scan. Other pilot candidate. Because CFS and Falcon are structurally similar but brand-distinct, whichever wins the pilot makes standing up the other one mostly a voice/brand swap, not a re-architecture. **Expected gap questions: 3-5.**

### FSL

Full scan. Most different from the other three, so the audit will probably flag it as "pilot later" — once the pattern is proven on a CFS-or-Falcon shape, FSL gets its own pass with adjustments. **Expected gap questions: 4-6.**

---

## Pilot recommendation logic

The audit ranks the four companies on three axes:

1. **Canon completeness.** How much material already exists in the vault and on public channels. More material = better day-1 drafts = less ramp time.
2. **Channel volume.** How much is happening in the channels we'd plug into (email, LinkedIn, sales calls, newsletter). The pilot proves itself fastest where there's already volume.
3. **Sales motion clarity.** Whether the offer, ICP, and pricing are sharp. Fuzzy offer = fuzzy drafts no matter how good the AI.

The company that ranks highest across all three wins the pilot. The audit shows you the ranking and the reasoning before locking it in — push back if your instinct says different.

---

## What the audit explicitly will not do

- **Will not modify your originals.** Everything it produces lives in new `_normalized/` subfolders or new top-level docs. Your vault notes are untouched and remain the source of record.
- **Will not auto-decide anything.** Pilot recommendation, gap fills, voice extractions, setup choices — all proposed, all reviewable, all your call.
- **Will not scan anything you flagged as excluded.** Default is the whole vault; tell us what to skip.
- **Will not store your raw materials anywhere outside the systems they already live in.** Extractions go into the `_normalized/` files inside your vault. The audit doesn't ship copies of your full vault to anyone.
- **Will not spin up paid services without your approval.** The setup checklist is a *plan*. Spend gets approved by you before anything is provisioned.

---

## Timeline

| Day | What happens | Your time |
|---|---|---|
| **Day 1 AM** | Setup screenshare with Annabel — point audit at vault, OAuth, URLs, account list | 20 min |
| **Day 1 PM → Day 2** | Audit runs on your laptop — scans, extracts, drafts inventory & checklist | 0 |
| **Day 2 PM** | Voice-memo gap questions per company (solo) | 15 min |
| **Day 3 AM** | Review screenshare with Annabel — walk outputs together, mark anything wrong | 20 min |
| **Day 3 PM** | Audit applies corrections, locks deliverables | 0 |
| **Day 4** | Final package locked in your vault + pilot company kicked off | 0 |

**Total time from you: ~55 minutes across 3 days, of which ~40 minutes is on screenshares with Annabel.**

---

## Editing the canon after it's locked

The normalized canon (`voice.md`, `icp.md`, `offer.md`, `business.md`, `goals.md`) lives in your Obsidian vault by default. You're fine in Obsidian. Josh isn't — and the employees coming after him probably won't be either. So the canon needs an editing surface that works for someone who doesn't live in markdown.

The audit will recommend one of three options and land the choice in the setup checklist:

1. **Guided Obsidian, simplified view.** Obsidian's Live Preview mode is close to WYSIWYG. Josh gets a vault with only the canon folder visible, no plugins, no folder maze. Cheapest, no new tools — but he still has to open Obsidian.
2. **Notion (or similar) as the front door.** Canon files mirrored into Notion; edits sync back to the vault. Most familiar surface for a non-technical editor. Adds one tool to the stack.
3. **Per-file shared docs (Google Docs / similar).** Each canon file is a shared doc; edits sync back. Simplest mental model, most fragile sync pipe.

The audit recommends one based on what Josh already uses day-to-day; you and Annabel land the final call on the review screenshare. Whichever wins is the same surface every future employee edits through — so this is one decision, not a repeated one.

---

## What happens after the audit

The build plan in `plan-v1-2026-05-14.md` takes over with the setup checklist as the to-do list. Week 1 stops being "draft the five canon files with you" because the audit will have already done that. Week 1 becomes "execute the checklist" — spin up Supabase, Cloudflare, Anthropic Team-plan seats (covers Cowork + Claude Code in one subscription), vault sync, and the editing surface Josh and future employees will use — and we get to the Daily Brief skill faster.

Once your system is running end-to-end, Josh is the first person to plug in. The onboarding template that gets him editing the canon is the same one that lands Erica and every hire after her — hours, not weeks, because the canon already exists, the architecture already exists, and the template tells you (with Annabel on a call if you want) exactly what to clone.

---

## What we still need to align on (before Day 1)

Three small decisions:

1. **Which scans are off the table.** Anything you don't want the audit reading — including specific vault folders. Default is the whole vault + all the channels listed above.
2. **Whether to scan personal LinkedIn / personal Gmail.** Useful for founder-voice signal. If you'd rather keep it out, we work from company channels only — slightly less voice precision, no big deal.
3. **Vault sync approach.** Obsidian Sync (~$8/user/mo, native) or cloud-folder sync (iCloud / Dropbox-as-sync / Syncthing — cheaper, slightly more setup). The audit will recommend based on what's already running on your laptops; this is just a heads-up that one of these is going in.

Once those three are answered, we can start Day 1.
