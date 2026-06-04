# Closed Loops in the AIOS Pilot — Erica's Granola → Email → LinkedIn Flow

**Date:** 2026-05-14
**Purpose:** Ground the loop concept before the dad conversation. Companion to `plan-v1-2026-05-14.md`.

---

## Bo's definition (verbatim, the anchor)

> **Open loop:** Make decision → execute → maybe check results. No systematic feedback. Most businesses run this way.
> **Closed loop:** Thermostat. Continuously monitors output, adjusts process to meet goal.

The thermostat is the right mental model. A thermostat doesn't just turn the heat on. It **measures the room temperature**, **compares to the target**, and **adjusts**. Without all three steps, it's a heater, not a thermostat.

Most "AI workflows" are heaters. We're building thermostats.

---

## The three nested loops in your system

This is the key insight: there isn't ONE loop. There are three, nested inside each other like Russian dolls. Each operates on a different time scale.

```
                ┌─────────────────────────────────────────────┐
                │  LOOP 3: BRAND-LEVEL (months)               │
                │   Voice / ICP / Offer files evolve          │
                │   ┌─────────────────────────────────────┐   │
                │   │  LOOP 2: WORKFLOW-LEVEL (weeks)     │   │
                │   │   Email + LinkedIn patterns improve │   │
                │   │   ┌─────────────────────────────┐   │   │
                │   │   │ LOOP 1: SKILL-LEVEL (days)  │   │   │
                │   │   │   Each draft → outcome       │   │   │
                │   │   │   measured per send         │   │   │
                │   │   └─────────────────────────────┘   │   │
                │   └─────────────────────────────────────┘   │
                └─────────────────────────────────────────────┘
```

---

## LOOP 1: Skill-level (the inner loop, days)

**Question this loop answers:** *Did this specific draft work?*

### The Granola → Email piece, step by step

| Step | What happens | Where the data lives |
|---|---|---|
| 1 | Erica has a call with a prospect. Granola records. | Granola local + cloud |
| 2 | Cloudflare worker (running every 3 min) polls Granola API, finds new transcript. | — |
| 3 | Worker writes the transcript to Supabase `calls` table, status: `ingested`. | `calls` table |
| 4 | Worker triggers the email-writer skill (or Cowork's filewatcher does — same outcome). | — |
| 5 | Skill reads: the transcript + Erica's voice file + the prospect's history (if any prior calls exist in Supabase). | Dropbox + Supabase |
| 6 | Skill drafts the follow-up email per the **test harness rubric** (80–120 words, names a specific outcome from the call, one CTA, Erica's signature). | — |
| 7 | Skill writes the draft to Erica's Gmail drafts folder. Logs the draft text + which transcript it came from in Supabase `drafts` table. | `drafts` table |
| 8 | Erica opens her drafts, reviews. **Three possible feedback signals:** sends as-is, edits then sends, deletes without sending. | — |
| 9 | A Cloudflare worker watches Gmail's "Sent" folder for emails matching draft IDs. Logs the **final sent version** to Supabase. | `sent_emails` table |
| 10 | **The thermostat moment:** worker computes the diff between the draft and what Erica actually sent. Writes `edit_distance` and `kept_or_replaced` flags to Supabase. | `sent_emails` table |
| 11 | A few days later: did the prospect reply? Gmail-pulling cron job updates `reply_received: bool` and `reply_sentiment: pos/neg/neutral` on that email row. | `sent_emails` table |
| 12 | Did the deal advance? If you're using a CRM, the stage change writes back too. (For v1 without a CRM: Erica manually tags `outcome: meeting_booked / no_response / declined` in Supabase via a slash command in Cowork.) | `clients` table |

**What "closed" means here:** the email writer skill, before drafting the NEXT email to a similar prospect, reads:
- Last 5 drafts Erica heavily edited (what did she change?) → adjust style
- Last 5 emails that got replies → what was different about them?
- Last 5 emails that got *no* response → what to avoid

That's the thermostat for the skill itself.

### The Granola → LinkedIn piece

The LinkedIn loop is similar but with a different feedback source:

| Step | What happens |
|---|---|
| 1 | Erica triggers `/draft linkedin from this week` in Cowork (or a weekly cron) |
| 2 | Skill reads: last 7 days of Granola transcripts in Supabase, identifies recurring themes (objection patterns, success stories, frequently asked questions) |
| 3 | Picks a theme. Drafts a post per the LinkedIn test harness (hook in line 1, story in middle, lesson/CTA at end, Erica's voice file) |
| 4 | Writes draft to a `linkedin_drafts` table + an email/notification |
| 5 | Erica edits + posts to LinkedIn |
| 6 | **Feedback signal:** a LinkedIn cron job (or manual entry via Cowork: `/log linkedin <url> impressions=1200 reactions=45`) writes engagement data back to Supabase |
| 7 | **Closed:** the LinkedIn skill, before drafting the NEXT post, reads the top-engagement posts from the last 60 days. Pattern-matches what works (post structure, length, themes, hooks). |

---

## LOOP 2: Workflow-level (the middle loop, weeks)

**Question this loop answers:** *Are our patterns getting better?*

This loop runs every 2–4 weeks, partially automated, partially Erica-driven.

A **scheduled cron job in Cloudflare** runs a "pattern recap" skill weekly. It pulls from Supabase:

- Of last 20 follow-up emails sent, what % got replies? (Compare to previous 20.)
- Of the prospects who replied, which objections came up most? (Top 3.)
- Of the LinkedIn posts published, which themes correlated with highest engagement?
- Of the calls recorded, what topics came up that we *don't yet have* email templates / LinkedIn angles for?

Output: a weekly **"Erica brief"** — separate from the morning Daily Brief — that shows trends.

**The thermostat moment here is human-in-the-loop:**
- Erica reads the recap, picks the top 2 patterns worth changing
- She updates the relevant skill's instructions (e.g., "always address the pricing objection in the second paragraph if the prospect mentioned cost on the call")
- Or she promotes a recurring theme into a new dedicated skill (e.g., now there's a `/draft pricing-objection-response` skill because that question came up 8 times in 3 weeks)

This is what Bo means by *"team members are no longer the people who execute every task. They define the standards. AI iterates against those standards."* Erica isn't writing emails. She's writing the rules that the email-writer follows, and tightening those rules every week.

---

## LOOP 3: Brand-level (the outer loop, months)

**Question this loop answers:** *Is the company's voice / ICP / offer becoming sharper?*

Every month or so, a "voice audit" skill runs. It pulls from Supabase:

- The **language clients actually use** in transcripts (their words for what you do)
- The **language Erica uses successfully** (in emails that got replies, in LinkedIn posts that got traction)
- Gaps between what's written in `my-voice.md` and what's *actually working*

Output: a proposed diff to the Dropbox markdown files (`my-voice.md`, `my-icp.md`, `my-business.md`).

**Critical:** the system doesn't auto-edit these files. Mansel's principle: the system *proposes*, the human *approves*. Annabel (or dad, or Erica) reviews the proposed diff and accepts/rejects.

When the diff gets accepted, **every skill in the system gets sharper immediately**, because every skill reads from these files at runtime.

This is the compounding effect. Month 1, the voice file is your best guess. Month 6, it's been refined by evidence from real client interactions. Every future hire who plugs into the company brain inherits this refined voice, *not* the day-1 guess.

---

## Where the data actually flows (Supabase schema, concrete)

```
clients
  id, name, company, first_touch_date, current_stage, primary_concerns[]

calls
  id, client_id, employee_id, transcript_text, granola_id, status,
  themes[], objections[], next_steps[], ingested_at

drafts
  id, call_id, skill_name (email|linkedin|newsletter), draft_text,
  test_harness_pass: bool, created_at

sent_emails
  id, draft_id, sent_text, edit_distance, recipient,
  reply_received, reply_sentiment, deal_outcome

linkedin_posts
  id, draft_id, posted_url, impressions, reactions, comments,
  shares, theme_tag

skill_runs
  id, skill_name, inputs_summary, output_id, latency_ms,
  tokens_used, cost_usd (← Bo's "silent failure" detection)

voice_evidence
  id, source (call|email|linkedin), excerpt, signal_type
  (← what's actually working — feeds Loop 3)
```

This schema is what makes the loops *possible*. Without it, the data is scattered (Granola has transcripts, Gmail has emails, LinkedIn has posts) and the AI can't see across them. **Supabase is the brain because it's the only place where all signals live in one queryable shape.**

---

## What's automated vs. what Erica/you approve

| Action | Who does it |
|---|---|
| Pull transcript from Granola | Cloudflare (automatic) |
| Write transcript to Supabase | Cloudflare (automatic) |
| Draft follow-up email | Email skill (automatic) |
| **Send the email** | **Erica** (always — never auto-sent) |
| Log sent email + diff vs. draft | Cloudflare (automatic) |
| Check for replies | Cloudflare cron (automatic) |
| Tag deal outcome | Erica (slash command) |
| Weekly pattern recap | Cloudflare cron (automatic) |
| **Update skill instructions** | **Erica** (after reading recap) |
| Monthly voice audit | Cloudflare cron (automatic) |
| **Update Dropbox voice/ICP/offer files** | **Annabel + Dad** (after reviewing diff) |

The pattern: **measurement is automated, judgment is human.** Bo's "you cannot outsource your conviction" applied to data — the system serves you measurements, you make the calls.

---

## What compounds (the dad pitch)

Month 1: Erica saves ~2 hours/day. Drafts are decent but generic-feeling.

Month 3: Drafts are noticeably in your voice. Reply rates are measurably up because the email writer learned which openings work for your prospects.

Month 6: New hire arrives. They install the same Cowork plug-in and on day 1, their AI knows your voice, your top 10 objections, the 3 LinkedIn themes that consistently work, the language your best clients use. They are functionally month-3 productive on their first day. **That's the compounding asset.**

Month 12: Three employees on the system. The voice file has been refined 4–5 times. The system has logged 800+ calls, 2000+ emails, 100+ LinkedIn posts. The pattern recap surfaces things you'd never notice manually — e.g., "calls from referrals close 3x faster when the first email references the mutual connection by name in the subject line." That insight came from data, not intuition.

---

## What could turn a closed loop back into an open one (the warnings)

1. **Skill instructions never get updated.** The weekly pattern recap fires but Erica doesn't read it or doesn't change anything. Now the system measures but doesn't adjust. Mitigation: make updating skill instructions part of Erica's Friday routine.
2. **The voice file never gets the diff applied.** The monthly audit proposes changes but no one approves them. Mitigation: a 15-min monthly review with you (dad) and Annabel.
3. **Outcomes don't get tagged.** Erica forgets to mark `meeting_booked` or `no_response`. The system can't learn what worked. Mitigation: a daily 1-minute review where Cowork asks "tag yesterday's emails" (chat-driven, low friction).
4. **Bo's "silent failures."** OAuth tokens expire. Granola API changes. Models drift. The data stops flowing but no one notices for weeks. Mitigation: the weekly recap email shows volume — if calls-ingested drops to zero, you see it immediately.

---

## The one-sentence dad pitch for loops

> *"Every call Erica has, every email she sends, every LinkedIn post she publishes, every reply she gets — all of it flows into one database. The AI uses that database to draft the next thing better than the last thing. The voice your company speaks in gets sharper every month, and when you hire someone new, they inherit that sharpened voice on day one instead of taking six months to absorb it."*

That's a closed loop. That's the compounding asset. That's why we're building it this way and not as one-off ChatGPT prompts.

If dad asks "but how is this different from ChatGPT?" — the answer is **feedback flows back**. ChatGPT generates and forgets. Our system generates, measures the outcome, and adjusts. That's the thermostat vs. the heater.
