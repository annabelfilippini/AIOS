# CFS LinkedIn Post Skill — Closed-Loop Demo

**Date:** 2026-05-14
**Audience:** Dad (Tom) — walks through how one AI skill actually works, end-to-end, using Charter Flight Support as the live example.
**Companion to:** `plan-v1-2026-05-14.md` and `loops-explained-2026-05-14.md`

This is not a separate idea. It is one of the four skills in the plan (the LinkedIn writer, week 4) built out in full so you can see what "closed loop" looks like in practice. Read it as: *this is what Erica's LinkedIn workflow becomes.*

---

## The one-paragraph version

A normal AI writing tool generates a post and forgets. This skill is different in three ways: (1) it reads CFS's documented voice before drafting, (2) it reads CFS's last 90 days of high-engagement LinkedIn posts so the next post pattern-matches what already works for your audience, and (3) after Erica posts, the system logs the engagement and feeds that back in. The voice gets sharper. The posts get sharper. The next hire inherits all of it. That's the thermostat.

---

## The closed loop, illustrated for LinkedIn

```
  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  ERICA TYPES: /draft linkedin about NBAA shuttle seats         │
  │                            │                                   │
  │                            ▼                                   │
  │              ┌─────────────────────────┐                       │
  │              │ SKILL READS (inputs):   │                       │
  │              │  - voice.md (community  │                       │
  │              │    register section)    │                       │
  │              │  - last 90 days of      │                       │
  │              │    CFS LinkedIn posts   │                       │
  │              │    ranked by engagement │                       │
  │              │  - this week's Granola  │                       │
  │              │    themes (optional)    │                       │
  │              └────────┬────────────────┘                       │
  │                       ▼                                        │
  │              ┌─────────────────────────┐                       │
  │              │ SKILL DRAFTS            │                       │
  │              │ Self-checks against     │                       │
  │              │ rubric. Revises if any  │                       │
  │              │ check fails.            │                       │
  │              └────────┬────────────────┘                       │
  │                       ▼                                        │
  │              ┌─────────────────────────┐                       │
  │              │ DRAFT lands in          │                       │
  │              │ linkedin_drafts table   │                       │
  │              │ + Erica's notifications │                       │
  │              └────────┬────────────────┘                       │
  │                       ▼                                        │
  │              ┌─────────────────────────┐                       │
  │              │ ERICA edits + posts     │  ← human in the loop  │
  │              └────────┬────────────────┘                       │
  │                       ▼                                        │
  │              ┌─────────────────────────┐                       │
  │              │ WEEK LATER: cron job    │                       │
  │              │ logs impressions,       │                       │
  │              │ reactions, comments,    │                       │
  │              │ shares → linkedin_posts │                       │
  │              └────────┬────────────────┘                       │
  │                       │                                        │
  │                       └──────────────┐                         │
  │                                      ▼                         │
  │                          Feeds the next /draft call            │
  │                          (closes the loop)                     │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘
```

The arrow at the bottom is what makes this not-ChatGPT. ChatGPT generates and forgets. This generates, measures, and adjusts.

---

## What the skill reads before drafting (the "context window")

### 1. CFS voice — community register

From `voice.md` (already drafted, 10KB, lives at `projects/consulting/prospects/charter-flight-support/voice.md`):

- **Tone:** warmer than the website, peer-to-peer, industry-insider without being cliquey.
- **Allowed phrases:** "stoked," "friends," "come find us," "hope to see you there."
- **Anchor every post in an aviation outcome.** Warmth without an operational reason is fluff.
- **Avoid:** "luxury redefined," "elevate," "white glove," "game-changing," "frictionless," and anything that frames CFS as insurance.
- **Load-bearing vocabulary:** AOG, mechanical, recovery, replacement aircraft, cost difference, broker, operator, Part 135, DNU list, client experience, continuity.

### 2. CFS's actual high-engagement LinkedIn examples (pool the skill reads from)

These are real CFS posts and post-shapes captured from public sources. In the live system, the skill pulls these from a Supabase table sorted by engagement. For the demo, here is the seed pool:

**Example A — event/community shape (Charter Connect):**
> "Great few days at Charter Connect. The best conversations were not abstract — they were about the real decisions brokers and operators have to make when a trip goes mechanical: protect the client, control the cost, and keep everyone moving."

**Example B — partner/platform shoutout (Tuvoli):**
> CFS announced availability on the Tuvoli platform — supplemental support for clients in the event of unforeseen mechanical AOG situations.

**Example C — event hosting offer (NBAA shuttle seats):**
> CFS offered free seats on light jets for CFS clients attending NBAA in Las Vegas, with 5 open seats available from Scottsdale on Monday mornings.

**Example D — team/culture (office dog Ace, holiday posts):**
> Light culture content — office dog Ace, team travel, seasonal messages. Tone is warm, peer, brief.

**Example E — data-backed insight (Josh Allen on Ironbird):**
> "Those six-figure recoveries happen. And most companies simply can't absorb that kind of loss." Paired with the published stat: ~10% average AOG disruption rate across charter flights, $4M in recovery payouts last year.

**Example F — financial-tension framing (Dan Harris, Ironbird):**
> "If there's a situation where you can depart on time but it's going to cost $30,000 more, or you can delay four hours and only spend a couple thousand more, most brokers are going to choose the cheaper option."

The skill pattern-matches across these: short, named moment, real aviation tension, no luxury language, ends with a practical implication or quiet invitation.

### 3. This week's Granola themes (optional input)

When `/draft linkedin from this week` is used, the skill scans the last 7 days of recorded calls for recurring themes (objections, success stories, FAQs that came up 3+ times) and proposes one as a post topic. This input is empty in the demo because Granola isn't wired yet — but the skill design accounts for it.

---

## The skill itself

Lives at `skills/cfs-linkedin-post/SKILL.md` once shipped. Contents below.

```markdown
---
name: cfs-linkedin-post
description: Draft a LinkedIn post in CFS voice for the community register. Reads voice file, recent high-engagement posts, and (optional) this-week Granola themes.
inputs:
  - topic (string, required)
  - register (community | thought_leadership, default: community)
  - length_target (short 60-90 words | medium 90-150 words, default: medium)
context_files:
  - projects/consulting/prospects/charter-flight-support/voice.md
context_queries:
  - supabase: SELECT post_text, impressions, reactions FROM linkedin_posts
    WHERE posted_at > now() - interval '90 days'
    ORDER BY (reactions::float / NULLIF(impressions, 0)) DESC LIMIT 10
  - supabase: SELECT theme_tag, count(*) FROM calls
    WHERE ingested_at > now() - interval '7 days'
    GROUP BY theme_tag ORDER BY count DESC LIMIT 5
---

# Prompt

You are drafting a LinkedIn post for Charter Flight Support (CFS).

Read the attached voice.md. Use the community register for default LinkedIn
posts; switch to thought leadership register only if the topic is a data
insight, industry tension, or educational post.

Read the 10 highest-engagement CFS posts from the last 90 days. Pattern-match
on structure, length, and theme — do not copy phrasing.

Read the top recurring themes from this week's Granola transcripts. If the
topic input is empty, propose three post directions from these themes.

Draft the post. Then run it through the rubric below. If any check fails,
revise and re-check. Do not output until all checks pass.

# Rubric (test harness — every check must pass)

1. Length: between 60 and 150 words (default), or 60-90 if length_target=short.
2. Register match: community by default (warm, peer-to-peer, allowed casual phrases). Thought leadership only when topic is data/insight.
3. Names a specific aviation moment: event, recovery, broker/operator situation, partner action, or concrete data point. No abstract aviation philosophy.
4. Vocabulary check: uses at least one load-bearing CFS term (AOG, mechanical, recovery, broker, operator, replacement aircraft, cost difference, Part 135).
5. Forbidden phrases not present: "luxury redefined," "elevate," "white glove," "game-changing," "frictionless," "unlock," "disrupt," "revolutionary," "never worry," "risk-free."
6. No insurance language: does not call CFS insurance, does not use "insured" or "guaranteed coverage."
7. No client/passenger safety claims, no operational control claims (no "we operate the aircraft").
8. Ends with a practical implication, a quiet invitation, or a partner/team acknowledgment. Not a hard CTA.
9. Reads peer-to-peer, not corporate. If "we are pleased to announce" or similar PR phrasing appears, fail.
10. If the topic touches pricing, AOG eligibility, reimbursement: surface the "support, not insurance" framing or hand off to a human-approved template.

# Output format

- The post (ready to paste into LinkedIn)
- 3 one-line variations of the opening hook
- Self-check report: which rubric checks were borderline and why
```

---

## Three sample drafts (generated by walking the skill manually)

These are what the skill produces. Each one has been run through the rubric in this document; the self-check report follows each draft.

### Draft 1 — NBAA shuttle seats (the actual recent CFS post angle)

**Topic input:** "NBAA Las Vegas — we have 5 open light jet seats from Scottsdale Monday morning, free for CFS clients."
**Register:** community
**Length target:** short

> NBAA week. We have five open seats on a light jet from Scottsdale to Las Vegas, Monday morning. Free for CFS clients heading to the convention.
>
> If you're flying in and the seat works for your schedule, send a note and we'll get you on the manifest. If we miss each other on the ride, come find us on the floor — happy to talk AOG recovery, broker-operator workflows, or just trade notes on how the season's been.
>
> Hope to see you out there.

*Self-check:* 84 words ✓ short range. Community register ✓ (allowed phrases "come find us," "hope to see you there"). Specific moment — NBAA + Monday flight ✓. Load-bearing vocab — "AOG recovery," "broker-operator workflows" ✓. No forbidden phrases ✓. No insurance language ✓. Quiet invitation ending ✓. Peer-to-peer ✓.

### Draft 2 — Charter Connect event recap (community)

**Topic input:** "Recap our time at Charter Connect — the conversations that mattered."
**Register:** community
**Length target:** medium

> Great few days at Charter Connect. No booth this year, just good conversations.
>
> The most useful ones weren't about features or pricing. They were about the actual decisions brokers and operators have to make when an aircraft goes mechanical: which replacement option protects the client experience, what the cost delta does to the trip economics, and how you keep your team focused on client communication while recovery logistics happen behind the scenes.
>
> Those decisions don't change much from year to year. The way teams prepare for them does. Thanks to everyone who made time to sit down with us — and to Goodwin for co-hosting an event that keeps getting the format right.

*Self-check:* 117 words ✓ medium range. Community register ✓ ("Great few days," "good conversations," partner shoutout). Specific moment — Charter Connect ✓. Load-bearing vocab — "mechanical," "replacement option," "client experience," "broker," "operator," "recovery logistics" ✓. No forbidden phrases ✓. Quiet ending — partner thank-you ✓. Peer-to-peer ✓.

### Draft 3 — The $30K delta tension (thought leadership)

**Topic input:** "The financial decision brokers actually face when an aircraft goes mechanical."
**Register:** thought leadership
**Length target:** medium

> A mechanical event isn't one decision. It's two stacked on top of each other.
>
> Decision one is operational: where's the recovery aircraft, what's its tail history, who's the operator, is it on the DNU list. Decision two is financial: what does the cost delta do to the trip — and to the relationship.
>
> When the on-time replacement costs $30,000 more, most brokers don't get to choose freely. The math forces a tradeoff between client experience and trip economics. That tradeoff is where a lot of broker-operator relationships quietly erode — not because anyone made the wrong call, but because someone had to absorb a loss that wasn't theirs to absorb.
>
> The recovery decision is operational. The cost decision is structural. They're worth separating.

*Self-check:* 130 words ✓ medium range. Thought leadership register ✓ (industry tension, no luxury phrasing, peer-to-peer not corporate). Specific framing — the $30K delta ✓ (mirrors Dan Harris on Ironbird). Load-bearing vocab — "mechanical," "recovery aircraft," "operator," "DNU list," "broker," "cost delta" ✓. No forbidden phrases ✓. No insurance language ✓. Ends with practical implication ✓.

---

## What gets logged after Erica posts (the feedback half of the loop)

A week after Erica publishes Draft 3, this row exists in Supabase:

```
linkedin_posts
  id: lp_0421
  draft_id: ld_0418
  posted_url: linkedin.com/posts/charter-flight-support_...
  posted_at: 2026-05-21
  impressions: 4,820
  reactions: 87
  comments: 14
  shares: 6
  theme_tag: "cost_delta_tension"
  engagement_rate: 1.80%
```

And this row in `voice_evidence`:

```
voice_evidence
  id: ve_0188
  source: linkedin
  excerpt: "The recovery decision is operational. The cost decision is structural."
  signal_type: high_engagement_phrase
  linked_post_id: lp_0421
```

The next time `/draft linkedin` runs, this post is in the top-10 read pool. The phrase "the recovery decision is operational" is in the voice_evidence table, available to be referenced in future drafts. Loop 3 (monthly voice audit) may eventually propose adding "decision separation" as a recurring CFS framing pattern in `voice.md` itself.

That's the thermostat. The room is warmer. The system measured it. The next draft adjusts.

---

## Heater vs thermostat — the week-4 vs week-6 diff

The plan ships LinkedIn in week 4. **The full closed loop above isn't all live in week 4.** Here's what is and isn't:

| Capability | Week 4 (heater) | Week 6+ (thermostat) |
|---|---|---|
| Reads voice.md | ✅ | ✅ |
| Rubric self-check | ✅ | ✅ |
| Reads past high-engagement posts | seed pool only (manual) | live Supabase query |
| Reads Granola themes | ❌ | ✅ |
| Drafts to `linkedin_drafts` table | ✅ | ✅ |
| Logs engagement to `linkedin_posts` | ❌ | ✅ |
| Writes to `voice_evidence` | ❌ | ✅ |
| Feeds next draft from real data | ❌ | ✅ |

This is on purpose. Week 4 produces real value (consistent on-voice drafts) immediately. Week 6 closes the loop once we've got 2-3 weeks of engagement data to feed back in. Trying to ship the full closed loop on day one would mean Erica gets nothing for 6 weeks.

The phrase to use with dad: **"we ship the heater first, then turn it into a thermostat once we have temperature readings."**

---

## What this proves for the broader system

If dad reads this and asks "OK, but how is this different from just using ChatGPT?" — the answer is in three places:

1. **The voice.md file.** ChatGPT doesn't have it. Your AI does, and it grows sharper every month from `voice_evidence` capture.
2. **The high-engagement read.** ChatGPT can't read your last 90 days of CFS posts ranked by reactions. Your AI can, because Supabase holds them.
3. **The logging.** ChatGPT never finds out if the post worked. Your AI knows next week's draft is being asked to beat 1.80% engagement, because that number is in the database.

Same architecture works for the email writer (rubric + past replies + reply outcomes), the newsletter (rubric + open rates + click-through), and any future skill. **LinkedIn is the easiest one to show first because the feedback signal is public and visible.** That's why this is a good demo.

---

## What dad should push back on

This document is built to be argued with. Likely pushback:

1. **"The week-6 logging is complicated. Can we live in week-4 forever?"** Maybe — but the compounding value lives in week 6+. The heater is useful. The thermostat is what makes Erica's setup transferable to the next hire.
2. **"Why pattern-match on engagement instead of just on what reads well?"** Because engagement is the only signal we have that the audience cares. Editorial judgment alone produces consistent voice but doesn't tell us if anyone is reading.
3. **"Are we tracking the wrong metric? Reactions ≠ deals."** Fair. The loop should eventually include downstream signal (did the post drive any inquiries, member sign-ups, or relevant comments). Week 8+ work.
4. **"Erica might not want her LinkedIn measured."** Bo's principle: the DRI owns the result, not the tasks. If Erica is DRI for lead pipeline + brand voice, then post engagement is one input to her result. The measurement isn't a performance review — it's tooling she uses to write better posts.

---

## Sources

- CFS voice.md and research (already in repo at `projects/consulting/prospects/charter-flight-support/`)
- [Private Jet Card Comparisons — "Changing how charter flight mechanical cancellations are handled" (March 2026)](https://privatejetcardcomparisons.com/2026/03/16/changing-how-charter-flight-mechanical-cancellations-are-handled/) — for Josh Allen, Erin Donnelly, and Dan Harris quotes plus published stats
- [Ironbird Podcast — Josh Allen on Charter Flight Support](https://flyironbird.com/private_jet_podcast/josh-allen-charter-flight-support)
- [CFS LinkedIn company page](https://www.linkedin.com/company/charter-flight-support) — Tuvoli, NBAA shuttle seats, Charter Connect, team/culture posts
- Bo Sar's closed-loop framework and Mansel Scheffel's federated architecture (captured in `agency-audit-network/research/sources/`)
