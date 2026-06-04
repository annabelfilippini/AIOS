# Cooldown Meeting Script — 45 min Zoom

**Goal:** Leave the call with (a) Bailey + Anya's actual workflow mapped in your notes, (b) one agreed-upon automation you'll build for free in the next 7 days, (c) an understanding of whether there's ongoing/paid work possible.

**Not the goal:** Closing a contract. Pitching a package. Showing off.

---

## Before the call (day-of)

- [ ] Have the audit URL open in a tab: https://cooldown-site-review.vercel.app
- [ ] Have Cooldown's IG, Strava (if exists), and their site open
- [ ] Notion/Google Doc open for live notes with a section per workflow
- [ ] Ask them at the top of the call if you can record — Fathom or Zoom native (use it yourself so you can skip note-taking and the transcript becomes the first sample of "meeting recap AI")
- [ ] Silence your phone. This matters.

---

## 0–3 min: Open

Keep it tight. Bailey already said yes.

> "Hey Bailey! [Anya — if there]. Thanks for making time. Quick framing before we dive in: the audit was mostly about the site, but the part I'm actually most excited about is the AI / workflow side — how you two run the business day to day. I want to understand your week, find the places AI can actually save time or make money, and leave today with one thing I can build for you this week for free. Cool if I record this so I don't have to take notes? I use a tool called Fathom — it'll actually end up being one of the things I'll probably recommend you use."

*That last line is the first soft pitch without being a pitch.*

---

## 3–20 min: Hypothesis walkthrough (the main event)

Don't ask open-ended "tell me about your workflow." You'll get generic answers. Instead, present your guesses and let them correct you.

> "I want to try something — I've been trying to guess what your weeks look like based on everything I can see publicly. Let me walk through what I *think* you spend time on, and you tell me where I'm wrong. Cool?"

### For Bailey
> "My guess is your biggest time sinks are:
> 1. Sponsor outreach — researching brands, writing personalized emails, tracking follow-ups. Is that 5ish hours a week? More?
> 2. Chapter leader recruitment — reviewing Typeform applications, onboarding calls, back-and-forth. Spiky, right?
> 3. Partnership and collab calls — plus the follow-up emails after.
> 4. Product launches — when there's a drop, you're the one coordinating copy, images, emails, IG.
> 5. Whatever Anya escalates from the inbox.
>
> What am I missing? What's the one you'd pay to stop doing?"

### For Anya (or Bailey speaking to Anya's work if Anya's not there)
> "For Anya — my guess is:
> 1. Social media across 15+ cities is the single biggest chunk. Posting, stories, collecting content from leaders. 10+ hours a week?
> 2. Checking in with chapter leaders about weekly runs.
> 3. Inbox — sizing, returns, meetup questions.
> 4. Newsletter drafting.
> 5. Keeping city pages updated.
>
> Does that match how you two split work? Where does she actually spend her time?"

### Listen for (write these down verbatim)
- Any workflow they describe that you didn't guess → new opportunity
- Any "ugh" / "I hate" / "takes forever" → top priority
- Any tool name they mention → update your stack hypothesis live
- Any number ("it takes me 3 hours every Monday...") → goldmine for ROI math in the follow-up

---

## 20–30 min: Day-in-the-life + tool tour

Pick the two workflows they flagged as most painful. Ask them to walk you through one concretely — ideally screen-shared.

> "Can you actually walk me through what sponsor outreach looks like for one prospect? From 'I want to reach out to Nike' to 'email sent.' Show me your screens if you can."

Watch for:
- Copy-paste between tools
- Data re-entered in multiple places
- Any task they do every X days that's basically the same template
- Tabs they have open (their real stack)
- Spreadsheets (automation gold — Sheets + Claude is easy)

Same drill for Anya's biggest pain (probably social content across cities).

---

## 30–40 min: Your ranked recommendations

**Do NOT dump all 7. Pick the 2-3 that match what they actually described.** Adjust on the fly. Here's the full bench to pull from:

### A. Social media content factory for 15+ chapters *(Anya, highest volume)*
- Custom Claude project or GPT trained on Cooldown's brand voice
- Input: photo + 2-sentence context from chapter leader
- Output: IG caption variants, story copy, 3 reel hooks
- Est. saves: 5-8 hrs/week
- Reliability: HIGH — nothing touches their live account, Anya still posts
- Lift: 1 day to build the custom prompt + playbook

### B. Sponsor outreach research + draft + follow-up tracker *(Bailey, highest $$)*
- Google Sheet or simple tool: paste a brand name → get a pre-filled research doc + personalized first draft
- Uses Claude or ChatGPT with a template
- Logs prospect + send date to a Sheet so follow-ups don't slip (nudges Bailey when it's time to circle back)
- Est. saves: 1-2 hrs per prospect, ~3-5 hrs/week
- Reliability: HIGH — always drafts, never sends. Bailey approves every one.
- Lift: 1-2 days to build

### C. Meeting recap + follow-up draft *(both, easiest install)*
- Fathom (free tier) records Zoom calls, auto-generates summary + action items + drafts a follow-up email
- Est. saves: 30 min per call
- Reliability: HIGH — mature tool
- Lift: 10 min to set up. **Good quick-win offer if they're decision-fatigued.**

### D. Chapter leader content collection *(Anya, removes chasing)*
- Typeform or WhatsApp bot: leaders submit weekly recap (photos + 3 questions) every Sunday
- Zapier sends into Airtable or Google Drive → Anya pulls from there instead of chasing
- Est. saves: 2-3 hrs/week of chasing + context-switching
- Reliability: HIGH
- Lift: 1 day to set up, but needs leader buy-in

### E. Inbox triage + draft responses *(both, but mostly Anya)*
- Gmail with an AI assistant that drafts replies for common questions (sizing, returns, meetup times)
- Anya approves before send → never auto-sends
- Est. saves: 3-5 hrs/week
- Reliability: MEDIUM — need careful prompt eng, tight domain
- Lift: 2-3 days

### F. Product description generator *(both, low volume but visible)*
- Template + Claude project that produces Kenny-Short-quality descriptions from structured inputs
- Fixes the inconsistency flagged in the audit
- Est. saves: 1-2 hrs per product
- Reliability: HIGH
- Lift: half a day

### G. Weekly newsletter draft *(Anya)*
- Claude project that takes this week's recaps + new product + sponsor spotlight → draft Mailchimp newsletter
- Est. saves: 2-3 hrs/week
- Reliability: HIGH
- Lift: half a day

---

## 40–45 min: Close + commitment

> "Here's what I'd suggest — pick one. Not three. I'd rather you actually use one thing than have a list you never touch. Based on what you just told me, the highest-leverage one is **[X]**. I can have a working version of that built and in your hands by **[date 5-7 days out]**, free. If it saves what I think it'll save, we talk about the next one. If it doesn't, you haven't lost anything.
>
> What do you think?"

### Then
- Agree on which one
- Confirm you'll send a follow-up email today/tomorrow with:
  - 1-page recap of what you heard
  - Top 3 ranked (the one we're building + next 2 on deck)
  - The scope + delivery date for the quick win
- Ask: "Anything I'd need from you to build this? [logins, sample data, examples of their best emails/captions, etc.]"

---

## Red flags to watch for (pause and adjust)

- **They want to talk about the website, not the workflow** → pivot. Say "happy to fix the quick wins from the audit too, but let me first understand the hours side — that's where the 10x is."
- **Bailey does all the talking, Anya's quiet** → directly ask Anya "what's the thing in your week you'd most want to get off your plate?" Anya is where the hours live.
- **They have a budget in mind** → don't quote yet. "Let me build the first thing free, we see if it actually delivers, and then we talk price when you have evidence. I don't want to quote before I know what's fair."
- **They say "we've tried AI tools and they didn't work"** → goldmine. Ask which ones and why they failed. You'll learn more in 5 min than from 2 hours of stalking.
- **They start listing 10 things they want** → "Love it. Let's pick one. Which one, if we got it right, would free up the most time?"

---

## One-liner if it goes sideways

If the call goes weird / you forget your script / someone derails: anchor back to:

> "What's the one thing in your week you wish you could stop doing?"

That question never fails.
