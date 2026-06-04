# Annabel's Paid Audit Playbook — ARCHIVED

> **Archived 2026-05-14.** Superseded by `self-serve-audit.md` after Annabel pivoted to a self-serve, web-purchased, user-filled audit with a PDF output. Kept for reference (Mansel + Bo + Mark interview-led / consultative version). Do not edit. New work goes in `self-serve-audit.md`.

Status: v1 working draft — 2026-05-14
Spine: Mansel Scheffel's "Master AI Audit Playbook" (from his AIOS Consulting Playbook)
Layered in: Bo Sar's 6-layer Business Brain + DRI/AI-Founder org redesign + test harness + "audit as living document" framing
Layered in: Mark Kashef's Discovery → Autopsy → Pricing → Workshop-delivery sequence + audit-as-video paradigm + Chinese Menu pricing

This is the playbook for the paid engagement that Annabel will sell from her website. The free Quick Read (`templates/quick-read.md`) is the funnel; this is the product.

---

## 0. Positioning & Pre-Engagement

### Product name

Client-facing, the paid audit is the **AIOS Starting Point Audit**. The CTA on AnnabelFilippini.com is *"Find Your AI Operating System Starting Point."* Internal docs and conversations can keep saying "the audit" or "the paid audit" — this playbook itself is an internal artifact.

### What the AIOS Starting Point Audit actually is

A diagnostic engagement that ends with a co-signed 90-day implementation slate, a Cost-of-Inaction figure, a referral to a vetted implementation partner if the client wants build help, and a *living* business-brain document the client can update as their business evolves.

**It is not a PDF.** The audit lives in the client's workspace (Notion, Drive, ClickUp — whatever they actually use). They keep it. They update it. Annabel revisits it during the maintenance retainer if one is signed.

### Who it is for (and who to say no to)

Annabel's two ICPs:
1. **Owner-operators / small business owners** Annabel can reach through her network (Dad's circle, Cooldown-style product brands, professional-services teams of 1–10 people).
2. **Mid-market departments (50–500 staff)** where one functional leader (Sales / Ops / Marketing) controls the budget and the workflow being audited.

**Red flags — say no before scoping.** (From Mark Kashef's "Reading the Room & Red Flags" module — Module 3 of his AI Consulting Playbook.)

| Red flag | Why it kills the engagement |
|---|---|
| Owner has never personally used Claude / ChatGPT for more than a few minutes | Implementation will be mediocre because they can't evaluate the output. Bo calls this the "AI Founder gate." If they fail it, sell them a workshop, not an audit. |
| Owner pitches the AI use case in the discovery call | They've already decided. Audit is theatre. Either decline or change the deliverable to a build spec. |
| No named KPI is at risk this quarter | No urgency = no payment. |
| Tools / data aren't accessible (locked CRM, no API on their stack, no admin who can give us read-only access) | The Cost-of-Inaction math is unprovable. Walk away. |
| Owner can't name three people whose workflows we'll touch | The audit scope is fictional. |

### Engagement shape

| Phase | Time | Deliverable | Price band |
|---|---|---|---|
| **0. Qualification call** | 20 min free | Go / no-go, fee quoted | $0 |
| **1. AIOS Starting Point Audit** (this document) | 1–2 weeks | Living business-brain doc + 90-day slate + Money Slide + partner match | $1.5K — $15K (scaled by client size) |
| **2. Implementation referral** | — | Partner brief + warm intro | Referral fee from partner (10–20% of their build fee) |
| **3. Maintenance check-in** (optional) | Monthly | Doc updated, slate progress reviewed | $500 — $2K / mo |

Mansel prices Phase 1 (audit) at $10K–$70K for mid-market. For Annabel's ICP today the band is $1.5K (single-employee, small business) → $5K (small-business team of 5–10) → $10K+ (Cooldown-shape product brand or mid-market department). Anchor on the *Annual Value Created* number — Annabel charges 10–20% of that.

---

## 1. Run Rules (apply every engagement)

Interview pro-tips (Mansel's, preserved verbatim):

- **Listen more, talk less.** 80/20 — they do most of the talking.
- **Ask "why?" repeatedly.** When you uncover a pain point: "Why is it done that way?" "What happens if that step is missed?"
- **Record with permission.** Transcriber so you focus on the conversation.
- **Focus on problems, not solutions.** Don't pitch. Understand current reality first.

Sampling plan (mid-market, 100–500 staff):

- Stakeholders (dept heads / KPI owners): 1–2 per function (Sales, Marketing, Ops, Finance, HR, CS, IT).
- End-users (frontline doers): 2–3 per function — the people actually clicking the buttons.
- IT / data owners: 1–2. Finance / FP&A: 1–2.
- Process shadowing: 3–5 critical workflows — one per major function.

For small-business engagements (under 20 staff), scale down to: 1 stakeholder interview (the owner), 1–2 end-users, 1 shadowing session.

---

## 2. Phase 0 — The Six-Layer Business Brain Assessment (Bo)

Run this **before** interviews. It is the audit's diagnostic centerpiece and the document the client keeps.

Score each layer 0–5 on two axes: *how complete is the information* and *how accessible is it to an AI agent or a new employee*. Visualize as a radar chart on Page 1 of the audit.

| Layer | What we look for | Common gaps |
|---|---|---|
| **1. Identity** | Mission, products, ICP, brand voice, founder POV — written down somewhere stable | Lives in founder's head, never written |
| **2. Critical context** | Current quarter goals, active campaigns, current pricing, deals in flight | Last month's numbers in a Slack thread |
| **3. Working memory** | This week's sprint, in-progress deals, this week's content | Mental notes, untracked |
| **4. Episodic memory** | *Why* decisions were made — paused outbound, fired vendor, pivoted segment | Walks out the door with employees |
| **5. Long-term knowledge** | Playbooks, won / lost deal notes, case studies, customer interviews | Scattered across Drives |
| **6. Background decay** | Process that promotes frequently-cited info and decays stale info | Almost never exists |

**Why this matters.** Mansel's framework says "AI doesn't fix broken processes — it amplifies them." The reason most AI pilots fail isn't the model; it's that the model has no business context. The 6-layer brain is the artifact that fixes that. Every downstream automation we propose plugs into this brain. *If the brain is empty, the audit's first deliverable is filling it — there is no point automating before this is built.*

**How to score.**
- **0** — does not exist
- **1** — exists in someone's head only
- **2** — exists somewhere but no one knows where
- **3** — documented but not discoverable / not maintained
- **4** — documented, discoverable, occasionally updated
- **5** — documented, discoverable, automatically maintained, machine-readable

A typical small-business client scores 1–2 across the board. A mid-market client scores 3 on layers 1–2 and 0–1 on layers 3–6. The audit's first sentence is usually some version of "your business runs on episodic memory that walks out the door every time someone quits."

---

## 3. Phase 1 — Stakeholder Interviews (Leadership View 🚁)

(Mansel verbatim — these questions work; do not rewrite them.)

**Who:** C-level, VPs, Directors, Heads of department.
**Objective:** KPIs, bottlenecks, tech constraints, culture risk, $$$ impact.

### Original question set

**1) Role & Team Overview 👥**
- "Can you describe your role and your team's primary responsibilities?"
- "What are the main goals or KPIs your team is responsible for this quarter / year?"
- "Could you walk me through your team's structure? Who reports to whom?"

**2) Core Processes & Workflow ⚙️**
- "From a high level, what are the most critical processes your team manages?"
- "Where do you see the biggest bottlenecks or delays in your team's workflow?"
- "Which tasks seem to consume the most man-hours or resources?"

**3) Tools & Technology 💻**
- "What are the main software systems or tools your team relies on?"
- "What are your biggest frustrations with your current technology stack?"
- "Are there important processes that happen outside of your main software (spreadsheets, email, manual documents)?"

**4) Pain Points & Strategic Challenges 📍**
- "What are the biggest challenges your team is facing right now?"
- "If you had a magic wand, what is the one problem you would solve for your team overnight?"
- "What do you feel is preventing your team from being more efficient or effective?"

**5) Future Vision 🔮**
- "Where do you see the biggest opportunities for improvement in your department?"
- "How does your team generally respond to new technology? What would make a new tool successful versus likely to be resisted?"

**6) Cultural & Change Management**
- "How does your team generally respond to new initiatives or changes?"
- "What has been the biggest challenge in implementing new processes or technologies in the past?"

### Add-on questions (tie to dollars, adoption, and scope)

- **KPIs under pressure:** "Which KPIs are you most accountable for this quarter? What happens financially if you miss them?"
- **Cost of pain:** "Roughly how many people / hours are tied up in the top 2 bottlenecks?"
- **Risk lens:** "Any compliance, security, or customer risks tied to current processes?"
- **Change map:** "Who are your **champions**, who's **fearful**, who are the **skeptics** in this team?"
- **AI Founder gate (Bo):** "How often do you personally use Claude / ChatGPT in your own work?" Score the answer. If the leader is themselves below 5 hours of real use, flag implementation risk.

**Deliverable:** Stakeholder brief with KPIs, top 3 pains, culture map (champions / fearful / skeptics), initial $ assumptions.

---

## 4. Phase 2 — End-User Interviews (On-the-Ground Reality 👷)

(Mansel verbatim — same instruction.)

**Who:** SDRs, AMs, Analysts, Recruiters, AP clerks, CS agents, Coordinators.
**Objective:** Exact steps, time sinks, tool friction, adoption sentiment.

### Original question set

**1) Daily Role & Responsibilities 🗓️**
- "Can you walk me through a typical day or week in your role?"
- "What are the 1–3 most common tasks you perform every day?"
- "How much of your day is spent on your core responsibilities versus administrative or repetitive tasks?"

**2) Step-by-Step Process Deep Dive 🔬**
- "Could you walk me through the exact steps you take to complete [a specific, common task]?"
- "Which part of that process is the most manual or takes the most time?"
- "What information do you need to find or reference to complete this task, and where do you get it from?"

**3) Tools & Frustrations 😤**
- "What software do you spend most of your day working in?"
- "What do you find most frustrating about the tools you have to use?"
- "Is there any double-entry of data or copying-and-pasting you have to do between different systems?"

**4) Pain Points & Wishlist 📝**
- "What is the most boring or repetitive part of your job?"
- "If you had an assistant, what tasks would you give them immediately?"
- "How do you currently track your work or report on your progress?"

**5) Cultural & Change Management**
- "How do you feel about recent changes in your work processes or tools?"
- "What has been the biggest challenge in adapting to new processes or technologies?"

### Add-on questions (precision + adoption psychology)

- **Quality bar:** "How do you know you've done this task correctly? What does 'done well' mean?"
- **Time reallocation:** "If this task disappeared tomorrow, what higher-value work would you do instead?"
- **Safety:** "What would make you **actually** trust an AI assist here?"
- **Open-loop check (Bo):** "When you finish this task, who confirms it's done? Or does the work just disappear into someone else's inbox?" *Closed loops have confirmation. Open loops are where errors hide.*

**Deliverable:** Task maps with times, tool pain inventory, adoption blockers / enablers by persona (champion / fearful / skeptic).

---

## 5. Phase 3 — Sales / Business Dev Discovery Deep Dive

(Use when the audit scope includes sales — most paid audits will. Mansel's structure, preserved.)

**Objective:** Uncover revenue impact opportunities through process optimization, automation, workflow improvements.
**Time required:** 90–120 min with the sales leader.

### Section 1: Current performance baseline

*Get the numbers first — everything else builds on this.*

**Revenue & targets**
- "Tell me about the pressure you're under this quarter." *(Listen, then drill:)*
- "What's your specific revenue target?"
- "Which KPI keeps you up at night — the one that if it fails is game over?"

**Team structure**
- "Paint me a picture of your sales organization."
- "How many people total? Break that down for me."
- "Who owns what — prospecting, closing, renewals?"

**Current metrics**
- "Walk me through how your team is performing right now."
- "What's your current win rate?"
- "What's your average deal size?"
- "How many new opportunities are you creating monthly?"
- "How long does a typical deal take to close?"

**Impact validation**
- "If your win rate improved by 2 percent, what would that mean in dollars this quarter?"
- "What's your team's total weekly time investment? Hours per rep × team size?"

### Section 2: Process & workflow mapping

*Find where time and deals die.*

**High-level process**
- "Tell me about the last deal that took way longer than it should have. What happened?" *(Listen, then drill:)*
- "Walk me through your typical sales process from lead to close."
- "Where do deals typically get stuck or slow down?"

**Time wasters & inefficiencies**
- "Think about the last time you heard a rep complaining about their workload. What were they doing?" *(Listen, then drill:)*
- "What are the biggest time-wasters your reps face weekly?"
- "If I doubled your lead volume tomorrow, what would break first?"

**Bottlenecks & keystone moments**
- "Tell me about a time when a small mistake early in the process killed a big deal." *(Listen, then drill:)*
- "What's the make-or-break moment in your sales process — the keystone that holds everything together?"
- "Which handoffs between teams create the most problems?"

### Section 3: Tools & data quality

**Tech stack reality**
- "What tools are in your official stack?" (CRM, email sequences, data enrichment, calling, proposals)
- "Which tools do reps skip or work around? Why?"

**Shadow systems & workarounds**
- "Tell me about the last time you discovered a rep was tracking deals in a spreadsheet instead of the CRM." *(Listen, then drill:)*
- "Where do reps work outside your official systems?"
- "What drives them to create these workarounds?"

**Data quality disasters**
- "Walk me through the last time bad data cost you time or a deal." *(Listen, then drill:)*
- "What are your biggest data problems?" (wrong contacts, missing info, bad-fit leads, duplicates)
- "On a scale of 1–10, how often do reps discover bad data after they've spent time on it?"

### Section 4: Pain points & strategic priorities

**Biggest problems**
- "If you had to explain to your CEO why you might miss your number this quarter, what would you tell them?" *(Listen, then drill:)*
- "What are the 3 biggest obstacles to hitting your revenue target? Rank them."
- "Tell me about the last new tool or process rollout that failed. What killed it?"

**Cross-team friction**
- "Describe the last time a deal got delayed because of a handoff between teams." *(Listen, then drill:)*
- "Which team-to-team handoffs create the most rework / errors / delays?"
- "What typically gets dropped or delayed in these handoffs?"

**Cost of inaction**
- "If these problems persist for 90 more days, what happens to your business?"
- "What's the real cost — missed targets, lost deals, compliance issues?"

### Section 5: Opportunity prioritization

**Magic wand & keystone focus**
- "If you could wave a magic wand and fix one thing overnight, what would move your revenue number fastest?"
- "What's the keystone of your entire sales operation — the one thing that if it goes wrong, makes everything else irrelevant?"

**Growth levers**
- "Think about your biggest opportunity right now. Is it: more qualified leads at the top? Faster sales cycles? Higher close rates?"
- "Pick one and tell me why."

**Success metrics**
- "How would you know in 30 days that we're succeeding?"
- "What moves the needle first: cycle time, win rate, or qualified pipeline volume?"

### Section 6: Change management reality check

**Team dynamics**
- "Tell me about someone on your team who loves new tools versus someone who fights every change." *(Listen, then drill:)*
- "Who are your champions? Who resists? Who's on the fence?"
- "What makes the difference between these groups?"

**Past success patterns**
- "Think about a change that actually stuck with your team. What made it work?" *(Listen, then drill:)*
- "What would need to be true to get 80% of your reps using something new every week?"

### Section 7: Risk & compliance

**Critical failure points**
- "Tell me about your biggest 'oh shit' moment in the last 6 months." *(Listen, then drill:)*
- "What's your single biggest point of failure today?"
- "Any recent incidents that cost money or deals?"

**System dependencies**
- "If your CRM went down for 48 hours, walk me through what happens to your business."

### Section 8: Data access & next steps

**Validation & proof**
- "Let me reflect back what I heard: Your #1 priority is _____. Did I get that right?"
- "Who controls the data I need to validate this?"
- "When can we get read-only access to see the actual numbers?"

**Deep dive planning**
- "Who on your team should I interview next for detailed workflow mapping?"
- "Which reps would give me the most honest picture of day-to-day reality?"

---

## 6. Phase 4 — End-User Workflow Deep Dive

(Mansel verbatim — used to map a specific workflow with the people who execute it.)

**Objective:** Map detailed workflows to identify AI / automation opportunities through process analysis, error patterns, and manual task discovery.
**Time required:** 90–120 minutes.

### Section 1: Daily role & responsibilities

**Workflow overview**
- "Tell me about yesterday. Walk me through what you actually did vs. what you planned to do." *(Listen, then drill:)*
- "What are the 1–3 things you do most often each day?"
- "How much time goes to your main job vs. administrative stuff?"

**Volume & frequency**
- "Think about your busiest day last week. What made it crazy?" *(Listen, then drill:)*
- "How many times do you do your most common task daily / weekly?"
- "Does your workload change by season or other patterns?"

**Time reallocation**
- "If your most repetitive task disappeared tomorrow, what would you do with that time?"

### Section 2: Step-by-step process deep dive

**Process mapping**
- "Tell me about the last time you had to do [common task] and it took forever. What went wrong?" *(Listen, then drill:)*
- "Now walk me through the exact steps when it goes normally."
- "Which part takes the longest or feels most tedious?"
- "What information do you need to gather, and where do you get it?"

**Decision points & complexity**
- "Describe a time when you weren't sure what to do next in this process." *(Listen, then drill:)*
- "Where do you have to stop and think vs. just follow routine steps?"
- "What makes this task easy some days and hard others?"
- "How does the process change for different types of deals / customers / situations?"

**Quality & error patterns**
- "Tell me about the last mistake you caught before it became a problem." *(Listen, then drill:)*
- "How do you know you've done this correctly?"
- "When do errors typically happen?"
- "What do you do when you get bad or incomplete information?"

**Collaboration & dependencies**
- "Walk me through the last time you had to wait for someone else to do your job." *(Listen, then drill:)*
- "Who do you need to check with during this process?"
- "Where do you hand things off to other people?"

**Keystone moments**
- "Tell me about a time when one small mistake early on ruined a big opportunity." *(Listen, then drill:)*
- "What's the make-or-break step in your process — the one thing that if you get wrong, nothing else matters?"

### Section 3: Tools & system friction

**Primary tools & frustrations**
- "Describe the last time you got frustrated with your tools. What happened?" *(Listen, then drill:)*
- "What software do you live in all day?"
- "What drives you crazy about these tools?"

**Data movement & double work**
- "Walk me through the last time you had to copy the same information between different systems." *(Listen, then drill:)*
- "Where do you do double-entry or copy-paste work?"
- "What information do you look up over and over?"

**Workarounds & shadow systems**
- "Tell me about a shortcut you take that probably isn't official policy." *(Listen, then drill:)*
- "What do you do when the system doesn't work the way you need?"
- "Do you have any personal spreadsheets, notes, or tools to track things?"

### Section 4: Pain points & automation wishlist

**Manual work identification**
- "What did you do last week that made you think 'there has to be a better way to do this'?" *(Listen, then drill:)*
- "What's the most mind-numbing part of your job?"
- "If you had an assistant for one day, what would have them do?"

**Current tracking & reporting**
- "Tell me about the last report you had to create. How long did it take?" *(Listen, then drill:)*
- "How do you track your work and report progress?"
- "What reports do you create manually?"

**Ideal state visioning**
- "If you could eliminate one part of your job tomorrow, what would have the biggest impact?"
- "What would make you 20% more productive starting next week?"

### Section 5: Change management & AI readiness

**Past change experience**
- "Think about the last time they changed how you do something at work. How did that go?" *(Listen, then drill:)*
- "What made it successful or a disaster?"
- "How do you typically feel when they announce new processes or tools?"

**AI trust & safety concerns**
- "If I told you an AI could help with part of your job, what would be your first concern?" *(Listen, then drill:)*
- "What parts of your work would you never want automated? Why?"
- "How would you want to double-check that an AI did something right?"

**Adoption requirements**
- "Tell me about a tool you actually use every day vs. one you were supposed to use but don't." *(Listen, then drill:)*
- "What made the difference?"
- "How much time would you invest learning something new if it saved time later?"

### Section 6: Workflow observation setup

**Live demo planning**
- "Can you show me exactly how you do [specific task] right now?"
- "What would be a typical example we could walk through together?"
- "Any confidential stuff I shouldn't see, or can we use dummy data?"

**Documentation access**
- "Do you have any personal cheat sheets or templates I could look at?"
- "What resources do you reference most during your work?"

---

## 7. Phase 5 — Map the Process & Find Opportunities 🗺️

**Goal:** Visualize how work flows across the four pods and quantify friction.

### The four pods

Mansel calls them **pods**, not engines, in his most current Skool curriculum. Use *pods* in client-facing language — it's softer and less industrial.

1. **Acquisition Pod** — how they find and sign customers
    - Content creation → schedule → publish → repurpose
    - SDR research → sequence → call brief → CRM update
    - Lead capture → score → route → first touch
    - Webinar / LP signup → nurture → meeting set

2. **Delivery Pod** — how they deliver the product or service
    - Proposal → SOW → kickoff → delivery → sign-off
    - Project plan → sprint cadence → QA → handover
    - Milestone billing → invoice → collections

3. **Support Pod** — how they handle post-sale
    - Ticket intake → triage → draft reply → human approve → send
    - Bug report → priority → status comms → closure
    - QBR prep → insights pack → follow-ups

4. **Operations Pod** — how the back office runs
    - Hiring funnel: JD → sourcing → screen → schedule
    - Finance close: receipts → reconcile → report
    - Access management: request → approve → provision → audit
    - Knowledge base: add → tag → review → archive
    - Data hygiene: dedupe → enrich → validate

**Scope rule (Mansel):** Pick ONE pod. Don't audit all four at once. The whole-company audit is the implementation partner's job, not yours.

### How to map on the whiteboard

- **Shapes:**
    - Rectangle = task
    - Diamond = decision / approval / keystone
    - DB = data store
    - Terminator = start / end
- **Arrows show handoffs** (delays hide in handoffs)

### Step Card — attach one to every step (non-negotiable)

**Step Card template:**
- **Owner / Role:** who does it
- **Systems:** tools used
- **Inputs → Outputs:** what comes in / what leaves
- **Volume:** per day / week
- **Doing Time (AHT):** minutes spent actually working
- **Wait / Queue Time:** time waiting on others / systems
- **Error / Rework %:** and common causes
- **SLA:** target + breach rate
- **Data Sensitivity:** PII / Finance / HR / None
- **Controls:** approvals, dual control, exception rules
- **DRI today (Bo):** named human, or "none"
- **Open / Closed loop (Bo):** does the work get confirmed done, or does it disappear into someone's inbox?

> If you can't fill these, your map isn't audit-grade yet. Go back to interviews / observation.

### Friction tags — mark each step

- 🟡 **Time Sink** — repeated manual effort, high AHT or high frequency
- 🟠 **Wait / Handoff** — queue time > doing time
- 🔴 **Quality Risk** — error / rework %, SLA breaches
- 🟣 **Compliance / Data Risk** — sensitive data + weak controls
- 🔁 **Open Loop (Bo)** — no confirmation step; work hands off into a void
- 🟢 **Champion present** / ⚪ **Fearful** / ⚫ **Skeptical gatekeeper** (adoption psychology)

> Most ROI is in 🟠 waits and 🔴 rework loops, not just 🟡 manual tasks. And open loops 🔁 are where compounding errors hide — they're often the first thing to fix even before automating.

### When to apply each tag

**🟡 Time Sink (manual effort).** Ask:
- Does this step take **>15 minutes** of focused work per instance?
- Is the person doing it **overqualified** for the task (CEO ideating thumbnails)?
- Is it **repeated often** (daily / weekly)?

If yes to any → 🟡.

**🟠 Wait / Handoff.** Ask:
- Is the **wait time > doing time**? (2 hours editing, 24 hours waiting for upload / approval.)
- Does this step require **someone else's sign-off** before moving forward?
- Are there **frequent delays / queueing** here?

If yes to any → 🟠.

**🔴 Quality Risk.** Ask:
- Is **error / rework % > 10%**?
- Do **mistakes here break downstream work** (wrong data, missed publish deadline)?
- Is there **no formal checklist or QA** for this step?

If yes to any → 🔴.

**🟣 Compliance / Data Risk.** Ask:
- Does this step touch **sensitive data** (PII, Finance, HR, client contracts)?
- Are there **no clear controls** (approvals, RBAC, exception rules)?
- Could a **mistake here cause regulatory / legal risk**?

If yes to any → 🟣.

**🔁 Open Loop (Bo addition).** Ask:
- Does someone confirm this is done?
- Is there a measurable output someone signs off on?
- Or does the work just "go to" the next person without anyone checking it arrived?

If no confirmation → 🔁.

### Find the keystones

Run every workflow through the keystone checklist:

1. **"If this fails, does everything else collapse?"** *(YouTube content → thumbnail / CTR. Sales outreach → getting replies.)* — keystone.
2. **"What's the single biggest multiplier?"** Which step has 10× downstream leverage? *Keystones usually have multiplier effect, not linear value.*
3. **"Where's the first point of no return?"** *Proposal — if rejected, nothing downstream matters.* — choke point.
4. **"What's truly visible to the outside world?"** Thumbnails, first sales call, onboarding. External-facing steps are usually make-or-break.
5. **"What's the costliest to fix later?"** Bad CRM data poisons reports for months.

Mark keystones with ⭐. Keystones get **priority weighting** in the opportunity matrix — higher Impact score.

> **Bottom line.** Keystone = the domino that knocks down everything else. If it fails, you wasted the whole workflow. Find that one thing first before geeking out on optimization.

### QDOAA — fix what's broken **before** adding AI

The most important sequencing rule in the entire audit. Run every flagged step through these in order:

| Step | Prompt | Goal |
|---|---|---|
| **Q**uestion | What is the actual purpose? Who said this is necessary? What happens if we stop doing it? What are we assuming? | Identify bloated / legacy tasks. Cut "shoulds." |
| **D**elete | What contributes no measurable value? What can be removed with zero or minimal negative impact? What feels good but isn't necessary? | Remove clutter before optimizing noise. |
| **O**ptimize | If I had to do this with half the resources, how would I do it? What's the top 20% creating 80% of results? | Sharpen ROI. Streamline workflows. |
| **A**ccelerate | Where can we move faster without breaking quality? What can be done in parallel? | Apply force strategically. |
| **A**utomate | What can be delegated, templatized, automated? What SOPs save 10+ hours / month? | Build scalable systems — **only now**, once Q-D-O-A have been done. |

> "Automating an efficient 3-step process is cheaper and more performant than automating a bloated 7-step mess. You get faster ROI because you're not paying for unnecessary automation." — Mansel

Most processes have 30–40% of their steps cut by Q-D-O-A alone, before automation enters the picture.

---

## 8. Phase 6 — Build the Opportunity Matrix

**Goal:** Convert friction into a ranked, dollar-backed backlog.

### Turn every tag into a candidate solution

- 🟡 Time Sink → automate data entry; AI-assisted drafting / summarization; auto-enrich; routing
- 🟠 Wait / Handoff → auto-notifications; SLA-based routing; parallelization; self-serve portals
- 🔴 Quality Risk → validation rules; AI QA; duplicate detection; playbooks; checklists
- 🟣 Compliance Risk → on-prem RAG; PII redaction; RBAC; logging; retention policies
- 🔁 Open Loop → confirmation hooks; closed-loop status callbacks; SLA timers with escalation

### Score each candidate (1–5, brutal and consistent)

- **Impact** — revenue up / cost down / risk down (tie to KPI). 5 = moves 2+ KPIs hard.
- **Effort** — integration complexity, change scope, data wrangling. *Lower is better.*
- **Risk** — compliance, failure blast radius. *Lower is better.*
- **Adoption** — champions vs fearful vs skeptics. 5 = easy adoption.
- **Confidence** — interviews only = 2; observed + baseline data = 4–5.
- **Data Readiness** — 5 = clean, accessible, permissioned. Low = blockers.

### Scoring table

| Score | Impact | Effort | Risk | Adoption | Confidence | Data Readiness |
|---|---|---|---|---|---|---|
| **5** | Moves multiple KPIs: revenue ↑, cost ↓, risk ↓, major CX lift | Huge (multi-team, months of dev) | High: touches customers, money, compliance; failure = big damage | Easy: champions exist, obvious painkiller | Observed baseline + proof from tests | Clean, accessible, permissioned |
| **4** | Strong on at least 2 (e.g. cost ↓ + CX ↑) | High but doable (weeks of dev) | Medium-high: could cause customer impact | Some champions, little resistance | Observed data or clear precedent | Mostly clean, minor wrangling |
| **3** | Moderate (one KPI, modest gains) | Medium (moderate dev, API wiring) | Medium: slows things if it fails | Mixed enthusiasm, training required | Precedent exists, not tested here | Exists but siloed / messy |
| **2** | Small or indirect impact | Low (simple SOP, light tool change) | Low-medium | Hard: skeptical, adoption effort needed | Interviews only | Incomplete, permissions missing |
| **1** | No measurable impact | Trivial (one Zap, settings toggle) | Low: no consequence | Very hard: fearful, active resistance | Pure guesswork | No data, blocked, wrong format |

### Priority score formula

```
Priority = (Impact × Confidence) − (Effort + Risk + (6 − Adoption) + (6 − Data Readiness))
```

Higher = do sooner. Keystones get +2 Impact bonus.

### Plot on the 2×2

| | Low effort | High effort |
|---|---|---|
| **High impact** | **Quick Wins** (<90 days) ← START HERE | **Big Swings** (6+ months) — do these *after* quick wins |
| **Low impact** | Nice-to-have | Deprioritize |

> "Quick wins prove the model works before you ask for bigger budget. Builds trust. Generates cash / time savings that fund the big swings. Prevents the 'AI doesn't work' narrative from taking root." — Mansel

### Definition of Done + Kill / Pivot — for every candidate

- **DoD example:** "Reduce SDR research from 120 → 20 min; accuracy ≥ 95%; 70% adoption by week 4."
- **Kill / Pivot example:** "If AHT not down ≥ 40% by week 4 or accuracy < 90% → pause, fix prompts / datasets, or cut."

If a candidate doesn't have a DoD with a numeric threshold and a kill criterion, it's a wish list item, not an opportunity.

---

## 9. Phase 7 — Org-Chart Redesign per Opportunity (Bo)

For each of the top 3–5 candidates, assign three roles:

| Role | Definition | Who |
|---|---|---|
| **IC (Individual Contributor)** | The human who executes the part of the workflow that stays human (judgment calls, exceptions, customer interaction) | Existing employee, possibly retrained |
| **DRI (Directly Responsible Individual)** | Owns the outcome of this workflow end-to-end. Singular, named. | Manager or senior IC |
| **AI-Founder** | The person in the org who designs, tunes, and supervises the AI piece of this workflow. May be the owner / CEO in small businesses, or a dedicated AI ops role in mid-market. | Often the gap — most clients don't have one |

**Why this matters.** Bo's "AI-Founder gap" is a real-world failure mode: companies bolt AI tools onto a workflow but no one owns the AI piece. The model drifts, the prompts get stale, and adoption collapses 90 days in. The audit must surface this gap explicitly. If the org doesn't have an AI-Founder candidate, that's a hiring or training recommendation in the implementation phase — *not* a reason to skip the build.

---

## 10. Phase 8 — Test Harness Specification (Bo)

For the top 3 candidates flagged as automatable, draft test harness rules **before** the implementation partner starts building. This is what makes the audit *executable*.

A test harness rule answers: *how do we know the AI did this correctly?*

### Example — outbound email automation

| Rule | Why |
|---|---|
| Email must reference something specific from the lead's website | Generic emails get ignored; this is the quality bar |
| Tone must match the rep's voice (sample: 5 past emails) | Adoption depends on it sounding like them |
| Subject line under 60 characters | Mobile display |
| No more than 2 questions per email | Cognitive load |
| Must include a CTA pointing to one specific next step | Conversion |

### Example — support ticket draft reply

| Rule | Why |
|---|---|
| Reply must cite the relevant KB article ID | Auditability |
| If confidence < 80% on intent classification, escalate to human | Avoid bad replies |
| Reply length within 1.5× of historical mean for that ticket type | Format fit |
| No mention of pricing, refunds, or legal — always escalate those | Risk containment |

**The test harness becomes the spec.** When Annabel refers the build to an implementation partner, the test harness rules are the acceptance criteria. *This is the single biggest reason partner builds succeed: the audit handed them measurable rules, not vibes.*

---

## 11. Phase 9 — Validate the Solutions (Reality Check Workshop)

**Purpose.** Your opportunity matrix looks good on paper — but it's still **your perspective**. The client has hidden context you'll never see in interviews alone: politics, seasonality, unofficial approval steps, personalities. Goal: co-create the final prioritized list *with* the client, not for them.

### How to run it

**1. Set the stage (5 min).** Frame it as collaboration, not a pitch.
> "We've scored and ranked opportunities based on what we heard. This is our best hypothesis. Now we want to sanity-check it with your team's lived reality before locking the plan."

**2. Walk through the top 6–10 opportunities (30–40 min).** Share screen → Opportunity Matrix. For each: recap the friction → proposed solution → DoD + Kill / Pivot. Pause for discussion.

**3. Ask validation questions (the heart of it).**

- **Pain match:** "Which of these Quick Wins best matches the pain your team actually feels day to day?"
- **Hidden complexity:** "What hidden steps or approvals could make this harder than we've scored it?"
- **Adoption reality:** "Which of these would your team be excited to use vs quietly resist?"
- **Strategic alignment:** "Does this fit your 6–12 month strategy and budget owners?"
- **Premortem check:** "Imagine this failed in 60 days. Why would that happen?"

**4. Map adoption psychology (10 min).** Use the 🟢 / ⚪ / ⚫ tags. Call out: "Who would champion this? Who might block it?"

**5. Lock the 90-day slate (10 min).** Pick **2–3 Quick Wins** the team feels strongest about. Capture "what must be true first" for any Big Swings (data cleanup, API access, policy approval).
> "We're leaving here today with a 90-day slate you've co-signed. That's the work we'll ship first."

### Deliverables out of Phase 9

- Updated Opportunity Matrix (with client notes).
- Final 90-day slate: 2–3 Quick Wins, DoD + Kill / Pivot each.
- Prerequisites documented for Big Swings.
- Adoption map (champions, fearful, skeptics).
- Org-chart redesign per Quick Win (Phase 7).
- Test harness rules per Quick Win (Phase 8).

### Reminders

- **Don't defend your scores.** The point is to *update them*.
- **Write in their words.** If they reframe a Quick Win, edit it live.
- **Lock fewer, not more.** 2–3 wins in 90 days beats 10 maybes.
- **Always leave with commitment.** If the slate isn't agreed, the audit failed.

### The Call Autopsy (Mark)

After the validation workshop, run Mark Kashef's **Autopsy Protocol** internally before writing the final deliverable. (Module 5 of his AI Consulting Playbook.) Re-listen to the recorded call. For each major moment, tag:
- What landed? *(Use these phrases verbatim in the deliverable.)*
- What confused them? *(Rewrite that section.)*
- Where did they push back? *(Acknowledge it in the deliverable directly — don't paper over it.)*
- What did they reframe in their own words? *(That's the language to anchor the audit on.)*

The autopsy is what makes the final deliverable feel like it was written *for* this client, not pulled from a template. It is the difference between an audit and a real consulting product.

---

## 12. Phase 10 — Present the Findings (The 5-Part Flight Plan)

**Goal.** The audit's value isn't the document — it's the moment the client signs the 90-day slate. The presentation is where that happens.

### Mark's 5-part workshop framework (apply to the audit findings call)

This is Mark Kashef's pilot / airplane analogy (Module 14 of his playbook). Use it verbatim for the findings session.

**Part 1 — Sell the dream.** Open with the picture of what's true after this audit lands. Don't sell the audit; sell the future. "If we ship these three quick wins, your team gets ~840 hours back in Q1, your win rate moves from X to Y, and your CFO sees a $Z run-rate improvement that pays the engagement back in 90 days."

**Part 2 — Show the path.** Walk them through the journey of the next 90 days. Acknowledge their assumptions explicitly: *"I know you were thinking we'd start by ripping out the CRM. We're not. Here's why."* This is where Mansel's "scope and out-of-scope" slide goes.

**Part 3 — Announce the flight plan.** Like the pilot's announcement: where we're going, what to expect along the way, where the turbulence will be. *"In Week 3 there's going to be a moment where the team feels like nothing has changed. That's expected. Here's what we do."* Pre-warning the rough parts means the client doesn't panic when they hit them.

**Part 4 — In-flight service.** Drop the golden nuggets. The Opportunity Matrix, the Money Slide, the test harness specs. These are the moments the audit *earns its fee*. Plan them out — don't bury them in dense paragraphs.

**Part 5 — Land the plane.** Conclude with the explicit ask: approve the 90-day slate, assign DRIs, schedule the kickoff. *Do not* let the call end without a commitment. If the slate isn't agreed-to in this call, the audit failed and the implementation will not happen.

### Mansel's 5 non-negotiable slides

Inside the in-flight service window (Part 4), these are the slides that have to hit:

**Slide 1 — Scope & Objectives.**
- Scope (functions covered, interviews, observations, data sources)
- Objectives (top KPIs at risk / opportunity)
- Out of scope (call this out explicitly to prevent scope creep later)

**Slide 2 — Opportunity Matrix (the master visual).**
- 2×2: Impact (x) × Effort (y)
- Bubble size = annual dollar impact
- Color = adoption risk (green easy / amber medium / red hard)
- Label only the top 6–10; keep the rest faint

**Slide 3 — Roadmap Summary.**
- Phase 1 (0–90 days): 2–3 Quick Wins, each with owner, DoD, guardrails, metrics
- Phase 2 (90–180 days): enablers + selected Big Swings
- Gates: IT / Security / Legal checkpoints
- Instrumentation: weekly measurements (AHT, wait time, error rate, adoption %, SLA hit rate)

**Slide 4 — Opportunity Deep Dives.** *(1–3 slides, one per Quick Win.)*
- Current vs Future mini-diagram (5 boxes max)
- Baseline: volume / week, AHT, wait time, error / rework %, SLA breaches
- Future: target metrics + guardrails (RBAC, logging, PII redaction, retention)
- DoD: numeric target + timeframe
- Kill / Pivot criteria
- Owner + Timeline
- *Test harness rules (Bo)* — the spec the implementation partner inherits

**Slide 5 — The Money Slide.** *(See Section 13 for the calculator.)*

### Mansel's objection-handling cheat sheet

Have these in the speaker notes:

- **"This looks like job cuts."** → "No. We reallocate capacity to revenue and quality. Our message is 'empower people; cut waste.' Adoption collapses if this is framed as layoffs."
- **"Data risk?"** → "Guardrails: SSO / RBAC, prompt / response logging, PII redaction, retention policy, human-in-the-loop for outbound. We use approved vendors or run RAG on our infra."
- **"Why those first?"** → "Fastest payback, lowest risk, and they unlock the data / skills needed for the big swings."
- **"Why not build our own LLM?"** → "We don't need a jet engine; we need a plane with our logo. Use proven models, fine-tune or RAG where needed, deploy on our infra if data sensitivity demands it."
- **"What if adoption stalls?"** → "Champions drive early wins; fearful get pain removed; skeptics follow results. We measure weekly and adjust."

---

## 13. The Money Slide (ROI Calculator)

**Goal.** Put dollars on the table and make finance nod.

### The table

| Use case | Baseline hrs / wk | Time saved % | Hours saved / wk | Loaded $ / hr | **Annual cost saved** | Realloc % | Value / hr (rev) | **Annual revenue uplift** | **Annual total impact** | **One-time cost** | **Annual run-rate cost** | **Payback (months)** | **Confidence** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SDR research → AI assist | 10,000 | 83% | 8,300 | 60 | **$25,896,000** | 50% | 250 | **$1,037,500** | **$1,296,500** | $85,000 | $48,000 | **1.2** | High |
| Tier-1 support drafting | … | … | … | … | … | … | … | … | … | … | … | … | … |

> Confidence: **Low** (interviews only), **Med** (observed + baselines), **High** (pilot data).

### Calculator rules

**A) Direct cost savings**
1. **Hours saved / week** = Baseline hours / week × % time saved
2. **Annual cost saved** = Hours saved / week × Loaded $ / hr × 52

> Loaded $ / hr = (salary + benefits + taxes + overhead allocation) / 2080. Don't use bare salary.

**B) Revenue uplift (capacity redeployed)**
1. **Revenue hours unlocked** = Hours saved / week × Realloc %
2. **Annual revenue uplift** = Revenue hours unlocked × Value / hr × 52

> Value / hr: if 2 hours closes a $5,000 deal, value / hr = $2,500. Get this from historicals with Sales Ops / Finance.

**C) Net impact & payback**
- **Annual total impact** = Annual cost saved + Annual revenue uplift
- **Annual net** = Annual total impact − Annual run-rate cost
- **Payback (months)** = One-time cost / (Annual net / 12)

**D) Sensitivity & confidence (don't hand-wave)**
- One-liner under the table: *"Modeled at 70% adoption and 10% under-performance on savings; upside / downside bands ±20%."*

### The 5 ROI levers — stack at least 2–3

1. **Time saved** — operational efficiency (hours back)
2. **Error reduction** — quality + compliance (risk avoided)
3. **Throughput increase** — capacity without hiring (headcount savings)
4. **Conversion lift** — revenue optimization (deals closed faster)
5. **Risk avoidance** — protect existing revenue (compliance fines, churn)

### Worked example — content marketing (Mansel)

- Current: 5–6 hours per video × 4 videos / month
- Automatable: 40% of that time
- Content marketer salary: $4K / month
- Hourly value of leadership time: $500 / video
- Implementation cost: $1,500
- Monthly savings: $800 (marketer time) + $2,000 (leadership time) = $2,800
- ROI: pays for itself in <1 month, then $2,800 / month ongoing

### Speaker note for the Money Slide

> "This is conservative. Even without revenue uplift, the quick wins pay back in under 90 days. With 50% of saved time redeployed to selling / service, the upside is larger."

---

## 14. Pricing the Audit

### Mansel's pricing power checklist (score each 0–2)

| Factor | Score |
|---|---|
| Proof (case studies, portfolio, audience, brand) | 0–2 |
| Pain urgency (problem costs money NOW) | 0–2 |
| Scarcity (few can solve fast + well) | 0–2 |
| **Total** | **0–6** |

| Total | Approach |
|---|---|
| 0–2 | Small fixed-fee audit + strong case study ask |
| 3–4 | Quote 15% of annual value created |
| 5–6 | Quote 20%+ and add maintenance retainer |

### The 15-min discovery script (Mansel)

Use in order on the qualification call:

1. "Walk me through the process end-to-end. Where does it slow down or break?"
2. "How many people touch this weekly? What roles?"
3. "How many hours does each person spend on it weekly?"
4. "When it fails, what happens? Lost revenue? Refunds? Rework? Compliance risk?"
5. "How often does it fail per month?"
6. "If we fixed it, what improves: speed, accuracy, capacity, conversion, risk?"
7. "What would solving this be worth this year if it worked?"

### The ROI Stack Worksheet (the value-based pricing formula)

```
Time saved:                            $_____
Errors prevented:                      $_____
Capacity unlocked / hires avoided:     $_____
Conversion lift:                       $_____
Risk avoided:                          $_____
─────────────────────────────────────────────
Total annual value created:            $_____

Then pick %:
  Conservative: 10%
  Standard:     15%
  Premium:      20%

Audit fee = (Annual value) × (chosen %)
```

### Pricing models (Mansel's four)

1. **Time & Materials** — hourly or day rate. *Avoid for the audit unless the client demands it.*
2. **Productized Services** — fixed-fee, fixed-scope. *Default for small-business audits.*
3. **Retainers** — recurring (see Section 16). *For ongoing maintenance after the audit.*
4. **Value-Based Pricing** — % of value created. *Preferred for high-ticket audits where the ROI Stack number is real.*

### The Chinese Menu Technique (Mark Kashef)

Mark's pricing approach when the client wants options. Instead of one fee, offer three pre-built bundles:

| Tier | Includes | Use when |
|---|---|---|
| **Strategic** | Audit only — living doc, opportunity matrix, money slide, no implementation | Owner wants to do it themselves |
| **Architected** | Audit + test harness specs + partner referral + 30-day check-in | Owner wants vetted help to build |
| **Accompanied** | Audit + partner referral + 90-day weekly check-ins + maintenance starter | Owner wants accountability through the slate |

Anchor on Architected. Most clients pick it.

### Annabel's actual pricing bands (today)

| Client shape | Audit fee | Notes |
|---|---|---|
| Single employee / solo owner-operator | $1,500 | Audit one pod, deliver 5-page Quick Read + living doc |
| Small business (3–10 employees) | $3K – $5K | Single pod, full playbook |
| Product brand (Cooldown shape) | $5K – $10K | Two pods (Acquisition + Delivery), full playbook + video summary |
| Mid-market department | $10K – $30K | Full playbook, full Money Slide with sensitivity bands, partner-ready spec |

These are starting bands. The ROI Stack Worksheet is the real anchor — once Annabel has the annual value number, the % rule (10 / 15 / 20%) sets the true fee.

---

## 15. The Audit Deliverable Itself

### Format options

| Option | When to use | Effort |
|---|---|---|
| **Living document** (Notion / Drive / ClickUp) — default | Every paid audit | ~6–10 hrs |
| **Quick Read PDF** (5–7 pages) | Small business, single employee | ~2 hrs |
| **Personalized video audit** (5-min, voice-cloned) | High-trust prospects, viral marketing, paid demos | Set up once (~$20K of automation Mark gives away free, see Module 6 of his AI Consulting Playbook) — then ~5 min per audit |

### The video-audit option (Mark Kashef + Sydney Nichols)

Mark's community gives away a complete n8n workflow that auto-generates audit videos:

**Pipeline:** Lead form → Google Sheet → Perplexity (company research) → OpenAI (comparison against your audit framework) → Gamma API (slide generation with your branding) → 11Labs (voice clone reading the slides) → PDF.co (asset conversion) → CreatorKit (video assembly) → Google Drive.

**Demo claim:** "Delta Airlines audit generated in 5 minutes."

**Implication for Annabel.** Once the audit playbook in this document is mature, the Phase 0–6 outputs can be templatized into a Gamma slide template and the OpenAI prompt. A new prospect fills the qualification form, the n8n workflow runs in 5 minutes, and Annabel reviews/edits before sending. This is the productization moat — the audit document becomes a product, not a service.

**Build order:** Don't build the automation until Annabel has done 5+ audits manually and the playbook is stable. Mansel's "Don't automate a broken process" rule applies to the audit itself.

### The living-document structure (default — 8–12 pages in Notion)

| Page | Content | Source |
|---|---|---|
| 1 | **Cover page.** Plain-English summary (3 sentences max) + 6-layer brain radar chart + **AIOS-level recommendation** | Bo + Mansel + Annabel |
| 2 | Six-Layer Business Brain — current state, scored, with comments | Bo |
| 3 | Pod scope: which pod we audited, why, what's out of scope | Mansel |
| 4 | Tagged process map (with Step Cards) | Mansel + Bo open-loop tag |
| 5 | Opportunity Matrix (2×2 + scored backlog) | Mansel |
| 6 | Top 3 Quick Wins — each with DoD, Kill / Pivot, DRI, test harness | Mansel + Bo |
| 7 | 90-day Roadmap | Mansel |
| 8 | The Money Slide | Mansel |
| 9 | Partner referral (which implementation partner fits) — optional | Annabel |
| 10 | Maintenance recommendation — optional | Mansel |

### Page 1 — the AIOS-level recommendation

Every paid audit commits to exactly one of these four headline recommendations on the cover page. It frames the rest of the document and gives the client a single sentence to repeat to their team.

| Recommendation | When to give it | What follows in the audit |
|---|---|---|
| **Personal AIOS** | Solo founder / single employee carrying too much context. The bottleneck is one person's head. | The audit focuses on that person's workflows: writing, inbox, follow-up, research, reusable prompts and skills. |
| **Team AIOS** | Small team with shared workflows. The bottleneck is handoffs, repeated work, or knowledge stuck in one person's head. | The audit focuses on shared SOPs, lead intake, sales handoffs, support triage, delivery flow, role-based assistants. |
| **Company AIOS** | Larger SMB / multi-department. AI usage needs to become shared infrastructure with policies, dashboards, training. | The audit focuses on approved tools, company KB, department-level workflows, prompt / SOP libraries, training plan, measurement. |
| **Cleanup before automation** | Process is too broken to automate yet. QDOAA reveals 40%+ of steps shouldn't exist, or the 6-layer brain scores below 2 across the board. | The audit's 90-day slate is *process redesign*, not AI. Re-audit after cleanup ships. *Sometimes the most valuable deliverable.* |

This recommendation is Annabel's call after Phases 1–2 of the engagement. Page 2 onward then builds the case for it.

---

## 16. The Maintenance Retainer (Optional Add-on)

Mansel's recurring-revenue blueprint. Offer this as a separate sale *after* the implementation lands — not part of the audit fee.

### 5 productized pillars

| Pillar | Business value | What you offer | Tools |
|---|---|---|---|
| **1. System Health Monitoring & Alerting** | Error reduction + risk avoidance | 24 / 7 monitoring with predictive alerts before failure | Helicone, Portkey |
| **2. Performance & Cost Optimization** | Cost avoidance + throughput | Continuous tuning for speed, cost, quality as models evolve | Prompt Metheus, Helicone |
| **3. Security & Compliance Management** | Risk avoidance | Proactive security audits + regulatory compliance monitoring | Org-specific |
| **4. Future-Proofing & Strategic Updates** | Conversion lift + competitive advantage | Continuous capability upgrades as new models release | Domain feeds, Prompt Metheus, Portkey |
| **5. User Adoption & Training Programs** | Throughput + error reduction | Ensuring humans actually use the AI | Change management framework, Typeform |

### Retainer tiers (Mansel's pricing — adjust for Annabel's smaller-business ICP)

| Tier | Mansel's price | Annabel's price (today) | Includes | Who picks it |
|---|---|---|---|---|
| **Bronze** | $8K / mo | $500 / mo | Pillar 1 only, basic fixes, monthly reporting | Solo owners |
| **Silver** | $10K / mo | $1.5K / mo ← **target landing zone** | Pillars 1, 2, 5 | Small business |
| **Gold** | $15K / mo | $3K – $5K / mo | All 5 pillars + executive reporting | Product brands, mid-market depts |

> "You want 80% landing in Silver / Gold, not Bronze. If everyone picks Bronze, your offer is too good there or too weak in higher tiers." — Mansel

### Positioning language (Mansel verbatim)

> "Stop: 'I build AI workflows for $2K–5K.' Start: 'I'm an insurance policy against AI system failure. The build is Phase 1, ongoing maintenance is how you protect your investment.'"
>
> "Never say: 'I'll maintain your system for $X / month.' Always say: 'For $X / month, you eliminate the risk of [compliance fine / customer backlash / system downtime] which costs you $Y annually. This is insurance, not overhead.'"

---

## 17. Execution glue — bridge to implementation

Close the audit deck by showing how the 90-day wins move straight into implementation, training, and maintenance. Use Annabel's four-phase frame:

| Phase | Owner | Deliverable |
|---|---|---|
| 1. **AIOS Starting Point Audit** (this document) | Annabel | Living doc, Opportunity Matrix, Money Slide, partner brief |
| 2. **Implementation** | Vetted partner (Annabel refers) | Working systems against the DoDs and test harness rules |
| 3. **Training & Adoption** | Partner or Annabel | Trained team + adoption metrics |
| 4. **Ongoing Maintenance** | Annabel or partner | Monthly reports, dashboard, doc updates |

**Final slide — Next Steps:**

1. Approve the 90-day slate (A / B / C), owners, guardrails.
2. Legal / IT checkpoints scheduled.
3. Data access approved.
4. Kickoff booked; dashboards live by Week 2.
5. Weekly cadence: adoption %, AHT, wait, error, SLA.

---

## 18. Sourcing & attribution

- **Mansel Scheffel** — AIOS framework, pods, 7-step audit, Step Cards, QDOAA, friction tags, keystone selection, opportunity scoring formulas, Money Slide calculators, 4-phase engagement, maintenance pillars and tiers, pricing power checklist, ROI Stack Worksheet, the 15-min discovery script. Source: `research/sources/mansel-ainative-2026-05-14/` and Annabel's downloaded Knowledge Base (`/Users/annabelfilippini/Downloads/Knowledge Base-20260406084428 (2).md`).
- **Bo Sar** — Six-Layer Business Brain, IC / DRI / AI-Founder org redesign, open-loop / closed-loop tag, test harness specification, "audit as living document not PDF" framing. Source: `research/sources/bo-sar-*.md` and `research/sources/beau-bosar-aif-sop-2026-05-11.md`.
- **Mark Kashef** — Discovery → Autopsy sequencing, "Reading the Room & Red Flags" qualification, Chinese Menu pricing, audit-as-personalized-video deliverable (the $20K Audit Automation), 5-part workshop flight-plan structure (Sell the dream → Show the path → Announce flight plan → In-flight service → Land the plane), "AI Architect" positioning. Source: `research/sources/kashef-earlyaidopters-2026-05-14/acp-modules.md` (full ACP module bodies, authenticated 2026-05-14).

Where two sources agree, the convergence is the signal — don't rewrite. Where they disagree (audit-as-PDF vs audit-as-living-doc; mid-market pricing vs SMB pricing), Annabel's audience is closer to Bo's framing and Mark's smaller-business tier, with Mansel's depth where the engagement justifies it.
