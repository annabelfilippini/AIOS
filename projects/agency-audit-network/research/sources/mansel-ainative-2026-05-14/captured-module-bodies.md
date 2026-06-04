# Mansel Scheffel — AIOS captured module bodies

Captured: 2026-05-14 via authenticated Playwright on `skool.com/ainative`

Source community: AI Transformation Academy (Mansel Scheffel)

**These are Mansel's verbatim module write-ups, captured from the lesson view.** Video content (the bulk of each lesson, typically 10-30 min) is NOT included — only the written description he attaches to each video.

---

## 2. AIOS Overview
_Course: The AIOS Model_

11:56

Full walkthrough of every component in the AI operating system and how they connect

CLAUDE.md as the system handbook — governs everything, evolves over time, loaded at session start

Context folder: your business identity, voice, ICP — NOT SOPs (those live in Notion/ClickUp)

Memory: from basic built-in memory to full RAG solutions — not everyone needs the same level

Skills, hooks, rules, MCP, databases, scheduling, agents — what each does and why it matters

The practical walkthrough will come in a separate video where you build alongside Claude Code






Resources
AIOS Overview Guide

---

## 6.5. Automating AIOS Onboarding
_Course: The AIOS Model_

9:45

This video walks you through onboarding your AI Operating System via an automated method. This is currently version one. Let me know if you run into any bugs along the way. 

There are three skills attached to this:

The Onboarding skill is the main automated builder that will build out your AI OS folder structure.

The Pod Mapping skill.

The Offer Builder skill.

 If you didn’t grab them earlier, they tie into the Onboarding skill to help you with other areas of context gathering for your business.

Resources
Onboarding Skill
Pod Mapping Skill
Offer Builder
Onboarding Guide

---

## 7.5. Operations & Scale
_Course: The AIOS Model_

13:42

Just because you built it doesn't mean it stays working — maintenance is critical

Silent failures: model updates, OAuth expiry, stale context, mystery edits by users or Claude

Backup strategy: cloud sync (Dropbox with version history) for non-technical clients, GitHub for technical ones

Always test your backups — quarterly restore to a fresh workspace to confirm everything works

Health check skill: runs scheduled checks on hooks, MCP, skills, memory, context freshness, costs

Four proactive levels: Reactive → Scheduled → Event-driven → Hybrid

Scaling via department pods — same model, distributed per role within a small business (accountancy example)

Plugin distribution makes scaling easy — each department gets their own tailored plugin

Resources
Health Check Skill
Operations Guide

---

## 11. AIOS Security
_Course: The AIOS Model_

20:52

This walkthrough covers AIOS security and basic best practices, and includes a skill that automates the entire process for you and guides you toward smarter decisions. 




Resources
Security Audit Skill
Example Report Output

---

## 12. Monitoring
_Course: The AIOS Model_

15:54

Unzip the installer and drag it into your claude project folder.

Get claude to walk you through installation

Install guide attached with FAQ

Resources
Command Center V2
Install Guide

---

## 16. AIOS Failover
_Course: The AIOS Model_

15:11
Resources
Guide + Prompt

---

## 1. The AI Operating System
_Course: The AIOS Model_

10:26

Why you need an AIOS — most solopreneurs spend 80% of time on backend ops and only 20% on growth. We're flipping that ratio.

The three core problems: fragmentation (tools everywhere), broken foundations (AI amplifies chaos), compound errors (more steps = more failures)

AI doesn't fix broken processes — it amplifies them. You need to fix foundations first, then layer AI on top.

The AIOS knows your business, remembers across sessions, runs your processes, enforces safety, connects to your tools, delegates intelligently, and works while you sleep.

This isn't a chatbot or a prompt pack - it's an operating system.

Grab the full AIOS package below along with a quick start HTML file for reference. 

Resources
AIOS Full
Quick Start Guide
Asset files

---

## 3. Mapping Your Business
_Course: The AIOS Model_

16:30

Understanding the four pods in your business is key to knowing where to start when selecting your skills. 

We can automate this process using the Pod Mapping skill, which is a walkthrough of the topics covered in this video and will then give you guidance around what sort of skills you should be building or acquiring. 

Resources
Pod Mapping Skill
Mapping guide

---

## 5. AIOS Context Mapping
_Course: The AIOS Model_

30:24

Your AI doesn't know your business. Every conversation starts from zero - it doesn't know your customers, your offer, your voice, or how your business actually runs.

That's not a model problem. It's a context problem. And it's the #1 reason most people's AI automations feel useless.

What you'll learn:

- The 5 types of context your AIOS needs (and which ones YOU need right now)

- Where each type should live — markdown files, databases, RAG, MCP, or your team's existing tools

- The difference between context (business bible) and state (operational data) — and why mixing them up causes chaos

- How to scale this to a team without overcomplicating it

---
Useful videos:
Databases - https://www.skool.com/cybercloudpremium/classroom/011bb796?md=3ffdc059333a4b18a697c26481f3f850

RAG - https://www.skool.com/cybercloudpremium/classroom/011bb796?md=9cee79ff1ddc4cefa05cd343c3358502

Resources
Context Layer Explained

---

## 7. System Design & Planning
_Course: The AIOS Model_

28:45

Think like an architect, not someone using a tool — your AIOS has real dependencies

Four domains: Dependencies & Redundancy, Integration Architecture, Memory & Data, Security & Data Flow

What happens when Claude goes down? Skills are human-readable SOPs — worst case, you do it manually. Better case: fallback to Codex/Gemini via hooks.

MCP can fail silently (returns 200 OK but fails behind the header) — monitor this

Three integration methods: MCP (easy but latency + token bloat), Python scripts (deterministic, no tokens), Webhooks (event-driven)

Always have at least one cloud copy of everything. Credentials in a password manager. Database backups to Supabase.

GDPR considerations with Apollo and lead gen — factor this in for clients

Resources
System Design Guide

---

## 14. AIOS Consulting Playbook
_Course: The AIOS Model_

21:48

This vid should give you the overview of what to do for your engagements. 

For a full practical deep dive into an audit you can check out the video linked in the resources below alongside the guide. 

More assets alongside that vid to make your audit faster.

Most importantly - adapt to your engagement. The guide is not static gospel, make sure you use it as a template but add your own layer of situational awareness and change things as you need to. 

Resources
AIOS Playbook
Audit Deep Dive

---

## Audit Deep Dive (linked from Consulting Playbook)
_Course: One-Person AI Transformation / Phase 1_

23:18
Step 1) Stop starting with AI roundtables → Start with process audits

Goal: Build AI strategy on objective data, not executive opinions and politics.

The problem with roundtables:

Executives vote on where to implement AI based on end goals they've seen elsewhere

Sales wants prospecting automated, marketing wants copywriting, ops wants workflows optimized

Sounds logical — but nobody admits their department has broken handoffs or 3-day delays

Politics and ego prevent honest assessment of what's actually broken

Result: You automate garbage processes and burn $500K+ on failed pilots

Action: Before ANY AI discussion, map the actual workflows:

Interview stakeholders separately (get their vision)

Interview ground-level workers separately (get reality)

Document the gap between what leadership thinks is happening vs. what's actually happening

Ask: "Where does your process break if volume doubles in 90 days?"

Step 2) Stop buying solutions first → Start mapping your 4 business engines

Goal: Understand WHERE breakage happens before deciding WHAT to automate.

Every business has 4 engines:

Acquisition: How you get customers

Delivery: How you fulfill for customers

Support: How you handle problems when they arise

Internal Ops: How you coordinate all the above (HR, legal, finance, IT)

Action: Map workflows across all 4 engines before touching AI:

Pick ONE department to start (don't Gestapo the whole company at once)

Sit with actual workers and walk through their process step-by-step

Ask: "What breaks when you hand this off to the next team?"

Identify where handoffs fail, where queues pile up, where humans bottleneck approvals

Step 3) Stop guessing at problems → Start tagging every workflow step

Goal: Turn qualitative pain into quantifiable data you can fix.

What to tag on EVERY step:

Systems used: What tools touch this step?

Inputs/Outputs: What goes in, what should come out?

Volume: How often does this happen?

Doing time: How long does the actual work take?

Wait/Queue time: How long sitting in someone's inbox or a system queue?

Error/Rework rate: What % gets kicked back for fixes?

SLA: Is there a service level agreement?

Data sensitivity: Compliance or security risk?

Controls: Who/what approves or signs off?

Tag each step with pain indicators:

⏱️ Time sink: Takes way longer than it should

⏳ Wait/Handoff: Sitting in queue or waiting on another team

⚠️ Quality risk: High error rate or inconsistent output

🔒 Compliance/Data risk: Could cost $500K+ if it breaks

Action: Create a process map with step cards for ONE workflow:

Pick the workflow leadership thinks is "fine" but workers complain about

Document every micro-step (don't let them skip "obvious" ones)

Add the 9 data points above to each step card

Mark pain indicators on every step that bleeds time, quality, or risk

Step 4) Stop jumping to AI → Start with QDOAA first

Goal: Fix what's broken WITHOUT AI before layering automation on top.

QDOAA Framework:

Question: Why does this step exist? Why are there 4 steps to create 1 output?

Delete: What steps serve no purpose and can be removed entirely?

Optimize: How can we make this better manually (better tools, better handoffs)?

Accelerate: How can we make it faster without adding people?

Automate: NOW — and only now — add AI to what's left

Why this order matters:

Most processes have legacy steps nobody's questioned in years

You can often cut 30-40% of steps without AI

Automating an efficient 3-step process is cheaper and more performant than automating a bloated 7-step mess

You get faster ROI because you're not paying for unnecessary automation

Action: Run ONE workflow through QDOAA:

List every step in the workflow

Question: Force yourself to justify why each step exists

Delete: Cross out steps that add no value (approvals nobody reads, redundant handoffs)

Optimize: Fix what remains (better templates, clearer handoffs, single source of truth)

Accelerate: Add simple tech that doesn't require AI (auto-save to cloud, Zapier triggers)

Automate: ONLY THEN consider where AI makes sense

Step 5) Stop treating all opportunities equally → Start with quick wins

Goal: Get ROI in <90 days to build momentum and prove the model works.

Priority Matrix:

Deprioritize: High effort, low impact (waste of time)

Nice to Have: Low effort, low impact (do these last if ever)

Quick Wins: Low effort, high impact (<90 days) ← START HERE

Big Swings: High effort, high impact (6+ months) ← Do these AFTER quick wins

Why quick wins first:

Proves the model works before you ask for bigger budget

Builds trust with the team (they see results fast)

Generates cash/time savings that fund the big swings

Prevents the "AI doesn't work" narrative from taking root

Action: Build your priority matrix from the workflow audit:

List every improvement opportunity you identified

Estimate effort (hours/cost to implement)

Estimate impact (time saved, errors reduced, revenue protected)

Plot on 2×2 matrix

Execute ALL quick wins within 90 days

Use those results to justify funding for big swings

Step 6) Stop selling "we'll save you time" → Start quantifying cost of inaction

Goal: Make doing nothing more expensive than hiring you.

ROI levers to stack (use 2-3 minimum):

Time saved → operational efficiency (hours back)

Error reduction → quality + compliance (risk avoided)

Throughput increase → capacity without hiring (headcount savings)

Conversion lift → revenue optimization (deals closed faster)

Risk avoidance → protect existing revenue (compliance fines, churn)

Example: Content marketing workflow

Current state: 5-6 hours per video, 4 videos/month

Automatable: 40% of that time

Content marketer salary: $4K/month

Hourly value of leadership time: $500/video

Implementation cost: $1,500

Time saved monthly: 9.6 hours

Money saved monthly: $800 (content marketer) + $2,000 (leadership time)

ROI: Pays for itself in <1 month, then $2,800/month ongoing savings

Action: Build a "Cost of Inaction" calculator for your audit:

Quantify current pain in dollars (wasted salary, lost revenue, compliance risk)

Calculate annual cost of doing nothing

Show implementation cost vs. monthly/annual savings

Include ALL ROI levers (time + quality + risk + throughput)

Make it painfully obvious: "This starts paying for itself in month one."

Step 7) Stop delivering audits as reports → Start selling implementation

Goal: Position the audit as Phase 1 of a multi-phase engagement, not a one-off deliverable.

The audit IS the sales process:

You've shown them objective data about what's broken

You've identified quick wins (<90 days) and big swings (6+ months)

You've quantified the cost of inaction

You've proven you understand their business better than they do

Natural progression:

Phase 1 (Audit): Map workflows, identify opportunities, calculate ROI → Deliverable: Strategic roadmap

Phase 2 (Implementation): Build the quick wins, architect the AI-enhanced workflows → Deliverable: Working systems

Phase 3 (Optimization): Train their team on the new tools, ensure adoption → Deliverable: Trained team + documentation

Phase 4 (Maintenance): Ongoing observability, monitoring, optimization as models/processes change → Deliverable: Monthly performance reports

Action: Package your audit as a productized offering:

Sell the audit for $X (covers your time to map, analyze, build roadmap)

Present the roadmap with clear phases (quick wins, big swings, ongoing)

Propose Phase 2 implementation based on the quick wins you identified

Show them the cost of NOT implementing (monthly bleeding from broken workflows)

Position yourself as the strategic partner who predicts failure points before they happen

Critical reminder: One department at a time. Don't storm the whole company like the Gestapo. Pick the department with the most obvious broken workflows, prove the model works, then expand from there.

Resources
Audit Notion Page
Ai Audit Markdown
Whiteboard SVG

---

## 1. Design Your USP & Market Research
_Course: One-Person AI Transformation / Phase 1_

9:11

---

## 2. How to Position Yourself
_Course: One-Person AI Transformation / Phase 1_

14:05
Step 1) Stop selling “automations”..start diagnosing constraints

Goal: move from “tech vendor” to “business strategist.”

Replace “What do you want to automate?” with:
“Where does your business model break at scale?”

Diagnose which constraint you’re dealing with:

Capacity problem: volume too high, team drowning

Knowledge problem: inconsistent answers, tribal knowledge

Process problem: bad handoffs, messy workflows, bottlenecks

Action: Write 3 discovery questions you’ll ask every prospect:

“Where are you hitting delays or backlog right now?”

“What breaks if volume doubles in 90 days?”

“Where do humans become the bottleneck (approvals, escalations, QA)?”

Step 2) Stop selling “time saved”.. sell growth capacity

Goal: executives don’t buy hours back; they buy throughput without headcount.

Use these ROI levers to frame value (stack multiple, don’t rely on one):

Time saved → operational efficiency

Error reduction → quality + compliance

Throughput increase → capacity without hiring

Conversion lift → revenue optimization

Risk avoidance → protect existing revenue

Action: For every lead, pick 2–3 ROI levers and write the “business impact statement”:

“This removes the constraint blocking your next growth phase.”

Not: “This saves you 20 hours a week.”

Step 3) Price like a consultant: severity > complexity

Goal: stop charging for build-time. Start charging for the cost of not fixing it.

Your pricing anchor becomes:
“What is this problem costing you monthly/annually right now?”

Frame your offer as certainty/insurance, not a project quote.

Action: Create a simple “Cost of Inaction” calculator for your client

Wasted salary / misallocated talent

Lost revenue from bottlenecks

Churn / retention loss from slow support

Compliance / risk exposure

Step 4) Niche by problem pattern, not just industry

Goal: build repeatable frameworks that work across markets.

Industry niche = “AI for dentists”

Constraint niche = “companies stuck at ~$2M because operations don’t scale” 

Action: Choose one constraint pattern you want to own:

Founder dependency / approvals bottleneck

Support scaling wall

Lead qualification waste

Ops handoff chaos (sales → delivery → support)
Then list 3 industries where it shows up.

Step 5) Reposition: advisor sets the agenda, vendor competes on price

Goal: become the person who predicts failure points before they happen.

Vendor: “I build AI solutions.”

Advisor: “Here’s what will break at $X revenue — and what we implement now.”

Action: Write your new positioning line (one sentence):

“I redesign how growing companies operate. AI is just one tool in the system.”

Step 6) Sell strategic thinking first (audit → then implementation)

Why: when they call you, they’re already sold on “AI.” They’re paying for correct design.

Action: Productize an audit (check the audit video + playbook for sellable framework):

Map workflows + handoffs

Identify constraints + failure points at scale

Pick the highest ROI levers

Output: a prioritized roadmap (what to fix first, what AI touches, what it shouldn’t)

Step 7) Make the cost of inaction painfully obvious

Goal: “doing nothing” must feel more expensive than hiring you.

Action: In every call, quantify 1 painful example:

“You’re paying a senior person to do admin-level work.”

“This bottleneck is forcing headcount growth to scale revenue.”

Then land the line:

“This starts paying for itself in month one because it stops the loss.”

---

## 3. Pricing Methodologies
_Course: One-Person AI Transformation / Phase 1_

29:09
Quick Action Guide: The 4 Pricing Models (and when to use each)
Step 1) Stop “picking a price” — pick a model

Your income ceiling is mostly determined by how you price, not how good you are.

The 4 models:

Time & Materials (T&M)

Productized Services

Retainers

Value-Based Pricing

Step 2) Model #1 — Time & Materials (T&M)
What it is

You sell time for money:

Hourly (more beginner-friendly, more transparent)

Day rate (traditional “high-value” consulting contracts)

Use it when

You need low-friction work fast (especially early)

You want testimonials and reps

You can command top market rates (T&M can beat value-based in some cases)

You can extend the engagement by finding more problems on-site (upsells)

Avoid it when

They have tight deadlines and you want to decouple time from money

You’re very fast and there’s no follow-on work (you finish early = you lose billing)

Senior execs demand outcomes only (“just automate X”)

Action checklist (T&M)

Decide: hourly vs daily

Find market range → aim high → negotiate down if needed (don’t start at the bottom)

Put scope creep guards in writing immediately

Build a habit: every 2–3 weeks, identify next constraint to extend/upsell

Step 3) Model stacking: T&M + “sell other people” (partnership leverage)

This is how you scale without permanent staff:

Keep your day rate

Add margin by placing 1–2 other consultants via partners/network

Action checklist

Build a “bench” list of 5–10 trusted contractors (DevOps, data, engineering, etc.)

Know your target margin per placement (per day or per month)

Bundle it: you lead + they deliver pieces

Step 4) Model #2 — Productized Services
What it is

Turn repeatable expertise into a standard offer with clear scope + fixed price.

Examples:

Audit delivered in 1 day

Repeatable implementation package

“Template + light customization” delivery

Use it when

You’ve solved the same problem 20+ times

You can standardize delivery with minimal unknowns

You want higher margins + less dependency on your time

You can attach support later (which becomes a retainer)

Avoid it when

The work requires heavy customization every time

The problem is too complex/variable to standardize

Enterprise insists on bespoke everything (unless your product is so valuable they accept it)

Action checklist (Productized)

Write the offer as: Inputs → Process → Outputs → Timeline

Hard-limit the scope and variables

Price it so delivery is profitable even on a “bad week”

Add a support option (light retainer) from day one

Step 5) Model #3 — Retainers
What it is

Fixed monthly fee for ongoing access to your brain:

Fractional CTO / advisor style

Or support/maintenance for what you built

Use it when

You want predictable income

You want deeper relationships and referrals

You have a proven track record (especially for fractional)

Avoid it when

There’s no ongoing value needed

You can’t show consistent wins (no proof)

You show up unprepared and waste their time (retainers punish you if you’re sloppy)

Action checklist (Retainers)

Choose format:

Support retainer (maintenance + upgrades + monitoring)

Advisory retainer (strategy + weekly/biweekly calls)

Define what “value per call” looks like (deliverables, decisions, next actions)

Cap your time (days/month or hours/week) so you don’t get buried

Step 6) Model #4 — Value-Based Pricing
What it is

You charge a percentage of measurable value created:

Typical: 10–20% of annual value

10% = conservative (less proof)

15% = standard

20% = premium (requires strong perceived value + proof)

Use it when

You have testimonials / proof of outcomes

You’re solving a clear, measurable, high-value problem

The project is implementation (not fuzzy discovery)

Avoid it when

The work is discovery and you don’t know what you’ll find

The client won’t share enough data to quantify outcomes

You can’t link your work to measurable business value

How to quantify value (use these buckets)

Cost savings (hosting, errors, fewer roles, less rework)

Revenue increase (speed, uptime, new capabilities, faster sales)

Risk mitigation (breach avoidance, compliance, reduced downtime)

Time savings x cost per hour x team size

Action checklist (Value-based)

Pick 1–2 value buckets you can actually measure

Estimate annual value conservatively

Set your % based on proof + market positioning

Anchor the price on years of experience + reduced risk, not delivery time

Step 7) Choosing the right model: the 3 universal rules
Rule 1 — Use maths

Ask: will value-based pay more than T&M for the same period? If not, can i sell enough value-based products, in the same time as the T&M to make more? 

Rule 2 — Use critical thinking

Ask: will taking a smaller deal now unlock a bigger deal later?

“Land and expand” logic (get in → upsell retainer / long-term contract)

Rule 3 — Use opportunity stacking

Ask: can you combine models?
Examples:

Day-rate discovery → value-based implementation

Productized audit → retainer support

T&M contract → placement margin on other consultants

Step 8) Beginner path vs experienced path (practical)
If you have no proof, no network, no clients

Your job is to get proof fast:

Low-paid / free / fast wins if needed

Upwork is viable but saturated → you must look premium fast

Once you have proof and options

Stop racing to the bottom (it destroys perception)

Push for the top of market rates on T&M

Start stacking: productized + retainer + select value-based

---

## 4. Using Value-based Pricing
_Course: One-Person AI Transformation / Phase 1_

16:49
The only rule:

Stop selling “an automation.” Sell “removing an expensive constraint.”
Everything below is just the mechanics.

0) The One-Page Flow (memorize this)

Lead with an Audit or Education (find where they bleed money)

Quantify pain using ROI levers (get real numbers)

Prioritize (what hits hardest + fastest)

Present value first (shows you are competent) 

Price as a % of value (10–20% baseline)

Close implementation (roadmap → build → maintain)

1) Your Pricing Power Checklist (before you quote anything)

Score each 0–2.

Proof (case studies, portfolio, audience, brand)

Pain urgency (problem costs money NOW)

Scarcity (few can solve fast + well)

Total 0–6 → % guidance

0–2: You’re weak. Start with a small fixed-fee audit + strong case study ask.

3–4: Standard. Quote 15% of annual value.

5–6: Premium. Quote 20%+ and add a maintenance retainer.

2) The 15-Min Discovery Script (full breakdown in the sales module)

You need numbers. No numbers = harder to define value-based pricing.

Ask these in order:

“Walk me through the process end-to-end. Where does it slow down or break?”

“How many people touch this weekly? What roles?”

“How many hours does each person spend on it weekly?”

“When it fails, what happens? Lost revenue? Refunds? Rework? Compliance risk?”

“How often does it fail per month?”

“If we fixed it, what improves: speed, accuracy, capacity, conversion, risk?”

“What would solving this be worth this year if it worked?”

3) The 5 ROI Levers (use this to quantify)

Pick 2–3 levers per opportunity. Stack them.

Lever 1 — Time saved

Annual value = (hrs saved/week) × (loaded $/hr) × 52
Price: 15–20% of annual time value.

Lever 2 — Error reduction

Annual value = (cost/error) × (errors/month) × (reduction %) × 12
Price: 10–20% of annual error cost prevented.

Lever 3 — Throughput / capacity without headcount

Annual value = avoided hires + avoided hiring costs (+ optional revenue unlocked)
Price: 20–25% of avoided hiring cost (year 1).

Lever 4 — Conversion lift (revenue lift)

Annual value = volume × conversion delta × avg deal value
Price: 5–10% of incremental annual revenue.

Lever 5 — Risk / cost avoidance (insurance model)

Annual value = probability × incident cost × risk reduction %
Price: fixed fee justified by exposure (often big numbers).

4) The ROI Stack Worksheet (see spreadsheet in assets)

Time saved: $_____
Errors prevented: $_____
Capacity unlocked / hires avoided: $_____
Conversion lift: $_____
Risk avoided: $_____

Total annual value created = $_____

Then pick a %:

Conservative: 10%

Standard: 15%

Premium: 20%

Implementation fee = (Annual value) × (Chosen %)

5) The Audit Offer (what you sell first)
What you call it

“AI Operations Audit + ROI Roadmap” (AI readiness is another good one)

What they get (deliverables)

Current-state process map (where time/money leaks)

ROI stack (levers + numbers + assumptions)

Prioritized roadmap (quick wins + bigger plays)

Implementation plan (phases, owners, timeline)

What you charge (from the transcript)

Typical: $5K–$15K

Bigger mid-market: higher (you know this)

If you have low proof: do the audit cheap/free only if you get a case study with numbers.

** Sales + discovery breakdown in the sales module

---

## 5. Choose Your Business Model
_Course: One-Person AI Transformation / Phase 1_

21:46
The core idea

The “who hosts this / who owns the keys / who maintains it” question is not technical.
It’s a business model decision that should already be decided before you demo anything.

Rule: Hosting flows from business logic — not the other way around.

1) The 3 Questions You Must Answer (before you sell anything)

If you can’t answer these, you’ll freeze on the call.

Am I selling a product or a service?

Do I want one-time cash or recurring revenue?

How much ongoing responsibility do I want?

Your answers determine:

delivery method

pricing structure

client positioning

how confident you sound

2) The 3 Delivery Models (pick one and commit)
Model 1 — Build & Bail (one-time handoff)

What it is: you build, document, hand over, and leave.

Use when:

workflow is stable/simple

you don’t want maintenance load

client has (or can develop) technical ownership

How it works (clean handoff rules):

client owns infra + pays hosting + pays API costs

you get temporary admin access during delivery

once done: access removed (security + boundaries)

Non-negotiables (or you’ll get blamed later):

build in their environment after MVP

no client data on your systems once shipped

documentation + Loom walkthrough + workshop training

include 30 days post-launch support (separate from maintenance)

Pricing lever:

base one-time fee + charge more if:

they lack technical staff

you’re training internal owner

you’re delivering strategy + architecture decisions

add-ons: docs package, training package, handoff workshop

Pros: high margin, low headaches, scales with templates
Cons: no recurring revenue, still risk of blame if adoption fails

Model 2 — Managed Service (you run everything)

What it is: you host + maintain + operate. They pay monthly.

Use when:

complex workflows need ongoing optimization

client wants results but zero technical ownership

you want predictable recurring revenue

you have proprietary tooling and want leverage

How it works:

your infrastructure, their access

dedicated client workspaces (no mixing—ever)

secure credential management:

encrypted storage

key rotation cadence (monthly/quarterly)

SLA + monitoring + clear scope

weekly performance reporting to prove value

Pricing structure:

setup/onboarding fee

monthly management fee (hosting + monitoring + basic maintenance)

change requests = additional build fees + retainer adjustment

Pros: recurring revenue + full quality control + lock-in
Cons: ongoing ops responsibility + stress + scope creep risk

Model 3 — Hybrid (client hosts, you maintain)

This is the money model.
What it is: client owns infra; you stay on as maintenance + optimization partner.

Use when:

client wants ownership but lacks expertise

workflows need regular updates

you want recurring revenue without running full managed ops

you want long-term consulting relationship + upsells

How it works (shared responsibility model):

they own n8n cloud/self-hosted (you guide choice)

you keep admin access for upgrades/fixes (contract-defined)

client pays hosting; you provide expertise

full handoff still happens (docs + Loom + training)

retainer defines:

monthly hours

what’s included (updates, fixes, priority support)

availability windows

what’s explicitly not included

Why it prints money:

you become embedded as “strategic consultant”

you hear problems across teams (sales/marketing/recruiting)

maintenance isn’t new builds → upsell path stays open

trust already exists, so selling follow-on work is easy

Main risk: shared responsibility conflicts
Solution: ruthless clarity in SOW + boundaries

3) The Script: How to Answer the Hosting Question (without sounding unsure)

Stop giving options like a waiter reading a menu. Pick your default model.

Default positioning (recommended):

“We use a hybrid model. You own the infrastructure and keys. We build it in your environment, then we stay on a maintenance retainer to keep it running, secure, and improving.”

If they push: “Can you host it?”

“Yes — but only as a managed service, which comes with a different fee because we’d be taking on uptime, security, monitoring, and operational responsibility.”

If they ask: “Who owns the API keys?”

“You do. Always. We’ll use secure credential storage and define rotation schedules, but ownership stays with you.”

If they ask: “Who pays the costs?”

“If you host: you pay hosting and usage directly.
If we host: costs are bundled into the monthly management fee, with usage thresholds defined up front.”

4) The Deliverable Checklist (so you don’t get blamed later)
For ANY model, these are mandatory:

Environment separation: dev/test vs prod

Credential discipline: no keys in random docs/screenshots

Handoff pack:

text-based playbook

Loom walkthrough (how it works + troubleshooting)

adoption workshop (users run it with you live)

Post-launch support window: 30 days minimum

If you skip adoption + handoff, you’re basically shipping a Ferrari with no steering wheel and hoping they’re grateful.

5) Pricing Logic (simple, usable)
Model 1 (Build & Bail)

one-time fee

upsell training + documentation + extended support

Model 2 (Managed Service)

setup fee + monthly management

change requests billed separately or via tier upgrades

Model 3 (Hybrid)

build fee + monthly retainer (defined hours + scope)

new builds always separate (keeps expansion revenue alive)

6) Your Action Plan (what to do next)

Pick ONE model as your default (hybrid if you can deliver it).

Write a 1-paragraph “delivery policy” you can say on every call.

Define your boundaries in plain English:

who owns infra

who owns keys

who pays what

what maintenance includes/excludes

---

## 7. Framework - Maintenance
_Course: One-Person AI Transformation / Phase 1_

23:33

AI Automation vs. Maintenance Income Model — Actionable Roadmap

Step 1) Stop selling one-time builds → Start selling ongoing insurance

Goal: Reposition from disposable contractor to mission-critical infrastructure.

Why AI systems inevitably break after delivery:

OpenAI updates models monthly → prompts fail, hallucinations increase

APIs change without warning → integrations break overnight

Compliance rules shift → systems become liability risks

Security gaps appear → data breaches = lawsuits

Performance degrades → systems get slower and more expensive over time

The client's hidden pain (they don't know they have these problems yet):

3am Slack alerts when automations break

Customer complaints about AI gone rogue.

Compliance audits flagging their AI system → fines

CFO asking why API costs doubled in 3 months

No one internal knows how to fix it

The brutal reality: Most clients don't discover these issues until it's too late.

Action: Change your sales positioning from day one:

Stop: "I build AI workflows for $2K-5K."

Start: "I'm an insurance policy against AI system failure. The build is Phase 1, ongoing maintenance is how you protect your investment."

In every initial discovery call, ask: "Who's responsible for monitoring this after I deliver it? What happens when the models update and your prompts break?"

Step 2) Stop selling shiny tools → Start selling peace of mind

Goal: Shift client psychology from "new system" to "guaranteed uptime forever."

What clients think they want vs. what they actually need:

Think they want: Shiny new AI system, build it and leave

Actually need: Someone to guarantee it works, evolves, and doesn't destroy their business

Why clients pay premium for maintenance:

Downtime costs more than the retainer (lost revenue, angry customers)

Compliance mistakes = $500K-$5M fines (one violation pays for 3+ years of retainers)

Leaders hate uncertainty → they want to know it's handled

Working AI = competitive advantage over competitors with broken AI

Value stack you're selling (not "maintenance," but strategic infrastructure):

Business continuity insurance → System won't fail

Risk mitigation → Compliance handled proactively

Cost optimization → API costs decrease over time via better models

Strategic evolution → Systems improve continuously, stay ahead

Executive reporting → Invisible work becomes visible ROI dashboards

Action: Reframe every maintenance proposal:

Never say: "I'll maintain your system for $X/month"

Always say: "For $X/month, you eliminate the risk of [compliance fine / customer backlash / system downtime] which costs you $Y annually. This is insurance, not overhead."

Step 3) Stop treating maintenance as an afterthought → Start with 5 productized pillars

Goal: Package maintenance as a tangible, high-value offering with clear ROI per pillar.

Pillar 1: System Health Monitoring & Alerting

Business value: Error reduction + risk avoidance

What you offer: 24/7 monitoring with predictive alerts BEFORE failure

ROI example: "Last month I prevented 3 system failures that would've cost $75K in lost sales. Retainer paid for itself 5x in one incident."

Client fear addressed: Finding out the AI broke from angry customers instead of proactively

Tools: Helicone (performance monitoring), Portkey (guardrails + prompts)

Pillar 2: Performance & Cost Optimization

Business value: Cost avoidance + throughput increase

What you offer: Continuous tuning for speed, cost efficiency, quality as models evolve

ROI example: "Reduced API cost by $8K/month while improving response speed 60% = $96K annual savings"

Client fear addressed: Runaway costs and slow systems destroying their product

Tools: Prompt Metheus (prompting IDE for optimization), Helicone

Pillar 3: Security & Compliance Management

Business value: Risk avoidance (primary lever for mid-market/enterprise)

What you offer: Proactive security audits + regulatory compliance monitoring

ROI example: "Avoided $500K GDPR fine by updating data handling before new regulations took effect"

Client fear addressed: Data breaches and regulatory violations = millions in fines

Tools: Organization-specific (bake security into the build from day 1)

Pillar 4: Future-Proofing & Strategic Updates

Business value: Conversion lift + competitive advantage

What you offer: Continuous capability upgrades as new models release

ROI example: "Upgraded to latest models → 15% better lead qualification → $200K quarterly revenue increase"

Client fear addressed: Falling behind competitors using newer AI

Tools: Domain-specific news feeds, Prompt Metheus, Portkey for model swapping

Pillar 5: User Adoption & Training Programs

Business value: Throughput increase + error reduction

What you offer: Ensuring humans actually USE the AI systems effectively

ROI example: "Increased team adoption from 30% to 85% = equivalent to hiring 2 additional staff without payroll costs"

Client fear addressed: Expensive systems sitting unused because team won't adopt

Tools: Your change management framework, Typeform (anonymous surveys for feedback)

Action: Build a pillar checklist for every client:

Audit their current system (or the one you just built)

Identify which pillars have the highest cost of inaction

Prioritize 2-3 pillars for immediate ROI, propose others for phase 2

Document case studies from each pillar to use in future sales

Step 4) Stop pricing on time → Start pricing on value with 5 proven levers

Goal: Charge based on catastrophe avoided, not hours worked.

The 5 value levers (stack 2-3 minimum per proposal):

Time Saved

Maintenance context: "I free up your team from firefighting broken AI so they focus on revenue activities"

ROI: 40 hours saved weekly = $100K annual productivity value

Error Reduction

Maintenance context: "Prevent AI mistakes before they reach customers"

ROI: Stopped 5 bad AI responses/month = $50K saved in customer recovery costs

Throughput Increase

Maintenance context: "Optimized systems process more with same resources"

ROI: Tuning increased processing from 100 to 250 requests daily = equivalent to hiring 2.5 FTEs

Conversion Lift

Maintenance context: "Better AI performance = better business results"

ROI: 2% improvement in AI-driven lead qualification = $500K additional annual revenue

Risk & Cost Avoidance

Maintenance context: "Insurance against catastrophic failure and compliance violations"

ROI: Avoiding ONE $500K compliance fine pays for 3 years of retainers

Action: For every maintenance proposal, calculate the cost of inaction:

Pick 2-3 levers most relevant to their business

Quantify annual cost if they do nothing (API bloat, compliance risk, lost deals, customer churn)

Show monthly retainer vs. annual savings

Make it painfully clear: "This pays for itself in month one by stopping the bleeding"

Step 5) Stop offering one price → Start with tiered retainers that anchor value

Goal: Use pricing psychology to land clients in mid/high tiers.

3-Tier Structure (adjust based on client size and your social proof):

Bronze: $8K/month

Monitoring + basic fixes + monthly reporting

What they get: Observability, executive dashboards, emergency fixes

Who picks this: Smaller clients or those testing the waters

Silver: $10K/month ← Target landing zone

Everything in Bronze PLUS optimization, training, quarterly reviews

What they get: Pillars 1, 2, 5 (monitoring, cost optimization, adoption programs)

Who picks this: Mid-market clients who see the gap between $8K and $10K is a no-brainer

Gold: $15K/month

Full strategic partnership: All 5 pillars + executive reporting + proactive evolution

What they get: You become mission-critical infrastructure, not a vendor

Who picks this: Enterprises and clients with high compliance/risk exposure

Pricing psychology:

Bronze looks "okay" → Silver adds massive value for +$2K → Gold is obvious for high-risk clients

You want 80% landing in Silver/Gold, not Bronze

If everyone picks Bronze, your offer is too good there or too weak in higher tiers

Action: Test tiered pricing with next 3 clients:

Present all 3 tiers in every proposal (never offer just one price)

Track which tier closes most often

Adjust value in each tier until 70-80% close on Silver or Gold

Use pillar mix to control perceived value (Bronze = 2 pillars, Silver = 3-4, Gold = all 5)

Step 6) Stop abandoning existing clients → Start transitioning them to retainers

Goal: Convert past one-time projects into recurring revenue (easiest money you'll make).

Why existing clients are low-hanging fruit:

They already trust you (you delivered once)

They're already experiencing the pain (systems degrading, models updating)

You understand their environment (built it yourself)

The transition script:

Map their future pain: "When I built your system 6 months ago, here's what you didn't know: [list 3-5 specific issues they'll face based on what you built]"

Show cost of inaction: "If OpenAI deprecates GPT-4 and you're not monitoring, your entire lead gen workflow breaks overnight. Last time that happened to a client, it cost them $40K in lost deals before they noticed."

Offer the new path: "Here's what I'd do if I were you: Bronze tier keeps you safe, Silver optimizes what we built, Gold makes you competitive long-term."

Action: Audit your past 5-10 clients and reach out this week:

Email subject: "Quick heads-up about [system you built] and upcoming changes"

Body: "Hey [name], I built your [X system] [Y months] ago. Since then, [specific model/API change] means [specific risk to their system]. Got 15 min to walk you through how to future-proof it?"

On the call: Use the 3-step script above → present tiered retainer

Goal: Convert 30-50% of past clients to at least Bronze tier

Step 7) Stop pitching maintenance in isolation → Start selling the full transformation journey

Goal: Position maintenance as Phase 4 of a multi-phase strategic partnership (maximum lifetime value).

The 4-Phase Model (for new prospects):

Phase 1: Audit / Strategic Roadmap ($10K-$70K depending on client size)

Map workflows, identify constraints, build prioritized roadmap

Deliverable: Strategic plan showing quick wins + big swings

Sets up: "Here's what to build and why"

Phase 2: Implementation ($15K-$100K+ depending on scope)

Build the AI-enhanced workflows based on Phase 1 roadmap

Deliverable: Working systems

Sets up: "Here's what we built for you"

Phase 3: Training & Adoption ($5K-$20K)

Train team on new tools, ensure adoption, document processes

Deliverable: Trained team + adoption metrics

Sets up: "Here's proof your team is using it"

Phase 4: Ongoing Maintenance ($8K-$15K/month ongoing)

All 5 pillars: monitoring, optimization, security, future-proofing, adoption

Deliverable: Monthly performance reports showing ROI

Sets up: Recurring revenue for life of the client relationship

The positioning shift:

Never say: "I build AI tools"

Always say: "I'm a strategic partner for your entire AI transformation. Most consultants deliver a report and leave. I audit, build, train, and maintain—so you actually get ROI."

Action: Update your service offering page and sales decks:

Show the 4-phase journey as a visual roadmap

Price each phase separately (transparency)

Highlight that Phase 4 is where they protect their investment

Include case study showing: "Client paid $40K for Phases 1-3, now pays $10K/month. After 12 months, saved $250K in avoided compliance fines and optimized API costs."

Critical reminder: The difference between $5K/month and $25K/month recurring isn't technical skill—it's understanding that clients don't want to deal with this stuff themselves. Half of them don't even know these problems exist yet. You're not doing "maintenance work." You're mission-critical infrastructure. That's a consulting premium, not a commodity service.

---

## AI Operating System
_Course: Blueprint Library_

AI Transformation Academy
17
99+
Community
Classroom
Calendar
Members
Map
Leaderboards
About
17
99+
Blueprint Library
0%
Ultimate AI Memory System
AI Operating System
GTM OS
Content OS
Playwright Automated Testing
App building - ATLAS v3
Ai News Monitor
Daily Brief
AI SEO / GEO
Frontend Website Builder
Gamma Slides
Proposal Generator
Call Digest
Meeting Prep
Context Audit
Slide Generator (handdrawn style)
AI Operating System

Whole course on this now in the classroom. This package contains every skill you will need for your AIOS. 

Follow course for details on how to customise and use it. 

Resources
AIOS Full

---

## Context Audit
_Course: Blueprint Library_

16:49
Resources
Context Audit

---

## Daily Brief
_Course: Blueprint Library_

AI Transformation Academy
17
99+
Community
Classroom
Calendar
Members
Map
Leaderboards
About
17
99+
Blueprint Library
0%
Ultimate AI Memory System
AI Operating System
GTM OS
Content OS
Playwright Automated Testing
App building - ATLAS v3
Ai News Monitor
Daily Brief
AI SEO / GEO
Frontend Website Builder
Gamma Slides
Proposal Generator
Call Digest
Meeting Prep
Context Audit
Slide Generator (handdrawn style)
Daily Brief

Synthesized daily intelligence briefing from all data sources — tasks (ClickUp), emails (Gmail), AI news (Supabase), competitors (Supabase), YouTube analytics. One read, 5 minutes, you know the state of your business. Delivers via Telegram with saved markdown report.

Resources
Daily Brief

---

## Proposal Generator
_Course: Blueprint Library_

AI Transformation Academy
17
99+
Community
Classroom
Calendar
Members
Map
Leaderboards
About
17
99+
Blueprint Library
0%
Ultimate AI Memory System
AI Operating System
GTM OS
Content OS
Playwright Automated Testing
App building - ATLAS v3
Ai News Monitor
Daily Brief
AI SEO / GEO
Frontend Website Builder
Gamma Slides
Proposal Generator
Call Digest
Meeting Prep
Context Audit
Slide Generator (handdrawn style)
Proposal Generator

The post-discovery-call wedge. Closes your Phase 1 audit engagement with a single-fee, fixed-scope, fixed-timeline proposal that doubles as the SOW.

Built for consultants who sell phased work - paid audit first, build engagement quoted after. If you sell one-shot builds or retainers, this is the wrong tool (but can still be adapted easily).

What it produces

A polished dark-themed HTML proposal you can paste into PandaDoc, DocuSign, Gamma, or Notion

An optional PDF (claude might need to instal a few plugins for you)

A JSON source file you can re-render with different data later

What's in the proposal

11 sections plus a cover page: situation recap (their pain, in their words), desired outcomes, deliverables list (8-12 audit artifacts), 4-phase engagement model with "you are here" on Phase 1, week-by-week breakdown, scope in/out, how-we-work cadence, single-fee investment with 50/50 payment terms, about-you paragraph, next steps, signature block.

When to use it

You ran a discovery call. The buyer said yes verbally. You need to send the proposal within an hour while it's still warm.

When NOT to use it

The buyer hasn't agreed yet. Proposals don't close calls do. Finish selling first.

---

** Tailor this to your brand/colours/writing style etc. You can also get it to output the proposal in Gamma or any of your own tools. 




Resources
Proposal Generator

---

## Call Digest
_Course: Blueprint Library_

AI Transformation Academy
17
99+
Community
Classroom
Calendar
Members
Map
Leaderboards
About
17
99+
Blueprint Library
0%
Ultimate AI Memory System
AI Operating System
GTM OS
Content OS
Playwright Automated Testing
App building - ATLAS v3
Ai News Monitor
Daily Brief
AI SEO / GEO
Frontend Website Builder
Gamma Slides
Proposal Generator
Call Digest
Meeting Prep
Context Audit
Slide Generator (handdrawn style)
Call Digest

Processes sales call transcripts (Fathom, Fireflies, or pasted text) into structured intelligence — pain points, objections, buying signals, deal qualification (MEDDIC/BANT), competitor mentions, coaching scorecard, risk flags, and follow-up email drafts.

Resources
Call Digest

---

## Meeting Prep
_Course: Blueprint Library_

AI Transformation Academy
17
99+
Community
Classroom
Calendar
Members
Map
Leaderboards
About
17
99+
Blueprint Library
0%
Ultimate AI Memory System
AI Operating System
GTM OS
Content OS
Playwright Automated Testing
App building - ATLAS v3
Ai News Monitor
Daily Brief
AI SEO / GEO
Frontend Website Builder
Gamma Slides
Proposal Generator
Call Digest
Meeting Prep
Context Audit
Slide Generator (handdrawn style)
Meeting Prep

Pre-meeting research briefs and talking points. Auto-detects sales prospects from the research-lead pipeline and generates CLOSER-structured battle cards with predicted objections, AAA responses, and customized call flow.

* Ties in with "research-lead" skill to do intelligence. 

Resources
Meeting Prep

---

## Ultimate AI Memory System
_Course: Blueprint Library_

27:54
Resources
Memory Script - run with ai.

---

## GTM OS
_Course: Blueprint Library_

Oops
Sorry, something went wrong or Skool is just having a hiccup. Please try again
BACK TO HOME

---

## 6. Multiuser AIOS Designs
_Course: The AIOS Model_

21:25

This video walks you through multiple users for your AI operating system and discusses context sharing across those AI operating systems.

The onboarding video (coming up next) has skills that will walk you through setting up solo or multi-user designs in an automated question-based walkthrough.

But understanding context is vital!

**TLDR:**
- Everyone has their own skills, rules, memory, and Claude.md.
- The only things that are shared globally are things that do not live in skills or things that are shared between the business, as in the diagram above. These are business processes that Claude picks up from time to time. They might live in a Dropbox folder, or in Notion or Obsidian. It is context shared on demand and suits any member of the business.

**Resources:** MultiUser Guide (module-06-multi-user.html — gated behind signed URL, not captured. Architecture diagram captured separately as `multiuser-architecture-diagram.png` in this folder.)

**Architecture diagram contents (from `multiuser-architecture-diagram.png`):**

Title: **Multi-User AIOS Architecture — Federated Personal, Shared Backbone**

Three zones:

**Personal (per-person, never shared)** — shown for both "Sarah's AIOS" and "John's AIOS":
- `.env` (API keys)
- `skills/` (personal)
- `rules/hooks/` (personal)
- `memory/` (personal)
- `CLAUDE.md` + reads Dropbox context
- Runs on **Sarah's MacBook / John's MacBook** — labeled **"Claude Code / Cowork"** (either works, per-person choice)

**Shared Business Context (Dropbox, ~2s sync)** — at `~/Dropbox/our-business/`:
- `my-voice.md`
- `my-icp.md`
- `my-business.md`
- `offer.md`
- `goals.md`

**Shared State (Cloud)** — yellow zone at bottom:
- **Supabase** — leads, tasks, pipeline
- **Airtable** — "if already using it"
- **pgvector** — team memory, optional

Color legend in diagram: Blue = Personal (never shared). Green = Shared Context (Dropbox). Yellow = Shared State (Cloud).

---

## 9. Cowork AIOS Setup Guide
_Course: The AIOS Model_

28:20

An AIOS guide for setting everything up inside Cowork. The same skills you use in the IDE apply here, including onboarding, pod mapping, offer creation, and more. Everything you need works the same in Cowork.

(Video-only module. No additional written body.)

---

## Supabase 101
_Course: Vibe Coding & Agentic Workflows (Level 5 — Web App Toolkit)_

16:27

(Video-only module. No additional written body captured.)

---

## Vercel 101
_Course: Vibe Coding & Agentic Workflows (Level 5 — Web App Toolkit)_

4:14

(Video-only module. No additional written body captured.)

---

