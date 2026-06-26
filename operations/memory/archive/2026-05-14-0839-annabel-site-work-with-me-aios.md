---
date: 2026-05-14
time: 08:39
project: agency-audit-network
status: active draft
next-session: Continue refining AnnabelFilippini.com Work With Me page copy and audit flow; wire the free audit and payment/contact actions when links/forms are chosen.
---

# Session: Annabel Site — Work With Me AIOS Page

## What We Worked On

Created and refined a separate Work With Me tab/page for Annabel's site draft at:

- `projects/agency-audit-network/site-draft/work-with-me.html`
- Previewed at `http://localhost:4173/work-with-me.html`
- User currently opened it directly via `file:///Users/annabelfilippini/Documents/AI-OS/projects/agency-audit-network/site-draft/work-with-me.html`

Home page teaser cards in `projects/agency-audit-network/site-draft/index.html` were also wired to the new Work With Me page.

## Direction Locked In

The Work With Me page should focus on **AIOS / AI Operating System** positioning, inspired by Mansel Scheffel's Skool framework notes in the agency audit project.

Core message:

> Build your AI operating system.

Supporting idea:

> One system that understands how your business runs, improves over time, supports your team, and creates automation where it helps.

Annabel wants direct, simple language. Avoid wordy contrast phrases like:

- "not a pile of tools"
- "Most small businesses do not need..."
- "The goal is not to recommend random AI tools..."
- extra filler words like "actually"

## Current Page Structure

1. **Hero**
   - Work With Me
   - Build your AI operating system.
   - One-system explanation.

2. **Top free-audit card**
   - "Find your AIOS starting point."
   - Short free audit explanation.
   - First multiple-choice question now lives inside this card:
     - For me
     - For my team
     - For my company
     - Cleanup first
   - CTA: "Start the audit"

3. **Next Step section**
   - "Ready to map your AIOS?"
   - Should explain the path:
     - short, free audit
     - longer paid audit
     - agency transfer/handoff if implementation support is needed
   - The duplicate "Start with one question" block was removed from this section and moved into the top free-audit card.

4. **Paid audit and agency cards**
   - Business owners: book/pay for the AIOS Starting Point Audit
   - Agencies: contact Annabel to join the implementation network
   - Payment and contact links are placeholders until Annabel chooses Stripe/checkout/contact form/email.

5. **Process section**
   - "The audit maps the system your business can grow into."
   - Current four-part explanation:
     - Context
     - Pods
     - Architecture
     - Iteration

## Copy Preferences Captured

- Keep copy punchy and easy to scan.
- Make "Map the starting point" / "Start the audit" feel like the start of the actual free audit, likely multiple-choice or quiz-style.
- The free audit should be short and engaging.
- The paid audit should be the longer, thorough AIOS map.
- Agency transfer happens after the audit when implementation support is needed.
- Emphasize:
  - one evolving AI operating system
  - business context
  - four pods
  - queryable system for agents and team members
  - iteration over time
  - automation only where it helps

## Files Touched This Thread

- `projects/agency-audit-network/site-draft/index.html`
- `projects/agency-audit-network/site-draft/work-with-me.html`
- `projects/agency-audit-network/site-draft/assets/` generated from the original bundled HTML export

Original source file in Downloads was not edited:

- `/Users/annabelfilippini/Downloads/Annabel Filippini (1).html`

## Next Moves

1. Tighten "Ready to map your AIOS?" section so it clearly says:
   - free audit first
   - paid audit second
   - agency handoff third
2. Decide actual free audit format:
   - inline multiple-choice quiz
   - form
   - Typeform/Tally/Google Form
   - custom static page flow
3. Choose payment/contact destinations:
   - Stripe checkout/payment link for paid audit
   - email/contact form for agencies
4. Eventually rebuild/export back into whatever final site format Annabel wants to publish.
