# Consulting

AI operating systems for expert-led businesses.

> **Reminder:** Every time we make a big decision (positioning, pricing, pilots, target market, offer structure, tooling, partnerships, naming), update [`MEMORY.md`](./MEMORY.md) with the decision and the reasoning.

This company helps small businesses capture the knowledge, judgment, standards, and workflows that make them excellent, then turn that knowledge into AI-assisted systems their team can actually use.

The core belief: **automate tasks, not judgment.** AI should remove repetitive prep work so humans have more attention for the moments that require care, trust, taste, and discernment.

The practical goal is to help owners spend more time working **on** the company, not **in** the company. The business should not depend on the owner personally handling every mundane task, repeated explanation, follow-up, draft, and operational detail.

## Company thesis

Expert-led businesses lose value when their knowledge stays trapped in one person's head.

A dentist, dermatologist, therapist, nutritionist, consultant, or practice owner has built years of tacit judgment: how they communicate, how they handle edge cases, what "good" looks like, when to escalate, what details matter, and how they want clients or patients to feel.

The opportunity is to preserve that knowledge over time and make it transferable.

This is not "AI automation for local businesses." It is knowledge capture plus workflow implementation:

- Capture the owner's expertise, voice, standards, and operating principles
- Convert existing onboarding guides, SOPs, templates, and training docs into AI-ready context
- Build role-specific skills that help the team move faster
- Keep humans in the loop for work that requires judgment, trust, or approval
- Deliver outputs inside tools the business already uses

## The first wedge

### AI-ready onboarding conversion

If an onboarding guide can train a new employee, it can also onboard AI.

Many businesses already have the raw material: onboarding docs, SOPs, email templates, intake scripts, service standards, FAQs, policies, and examples of good work. The consulting offer is to turn those materials into a practical AI operating layer.

Inputs:

- onboarding guides
- SOPs and training docs
- scripts, templates, and FAQs
- sample client/patient communications
- examples of excellent work
- current tools and workflow map

Outputs:

- company context file: services, standards, voice, rules, and priorities
- expert knowledge map: judgment, preferences, escalation rules, and edge cases
- role or workflow skills for the team
- human-review rules: what AI may draft, what needs approval, what it must never do
- documentation gap report: what a new employee or AI assistant could not infer
- one live workflow implemented inside their existing tools

## Value propositions

### For the expert owner

"You have built a way of thinking that works. We help preserve it, document it, and make it usable by your team so the business becomes less dependent on you personally."

This matters for owners who want to hire, train, scale, step back, sell, or simply stop being the only person who knows how the business should operate.

It also gives owners time back for company-level work: improving the service, developing the team, building relationships, creating new offers, and making decisions that only the owner can make.

### For the team

"AI handles the repetitive prep work so your team can spend more attention on the human parts of the job."

Skills should help staff draft, summarize, prepare, route, triage, and retrieve knowledge faster. They should not replace the moments that require care, discretion, or professional judgment.

## Operating model

Inspired by the AIOS model:

- **Shared business context:** the company's services, standards, offers, voice, policies, and operating principles
- **Expert memory:** the owner's judgment, preferences, edge cases, and examples of good work
- **Team skills:** repeatable workflows for front desk, operations, marketing, sales, client/patient follow-up, and internal support
- **Rules and guardrails:** what AI can do, what needs human approval, what is off-limits
- **Shared state:** lightweight storage for approved knowledge, SOPs, workflow outputs, metrics, and implementation notes
- **Personal context:** role-specific preferences and workflows for individual team members

Tooling should be chosen pragmatically. Claude Cowork can be the more user-friendly client-facing layer. Codex can be the internal engineering bench for building reusable templates, scripts, audits, and implementation assets. Supabase or another database can support shared state when needed, but client data should not be centralized before there is a clear reason and a safe governance model.

## What to build first

Free 45-minute audit -> one free workflow built in 7 days -> 30-day review -> case study or paid continuation.

Anchor: "Going rate is $150/hr or $2-5k per implementation. Doing it free right now to build case studies."

The first build should be narrow, adopted, and measurable. No dashboards unless the client already lives in one.

Examples:

- inquiry follow-up drafts
- client/patient FAQ assistant
- intake summary for human review
- onboarding guide converted into staff-facing skills
- internal SOP assistant
- content or newsletter drafting workflow
- review/testimonial routing
- referral partner outreach prep
- meeting or call recap workflow

## Pilot strategy

Three pilots only. Finish all three, document before/after metrics, and extract case studies before taking on anyone new.

Current targets:

- Cherry Creek Nutrition (Suzanne)
- Marta Brummell
- one co-selected pilot

Every pilot needs:

- one named workflow
- one measurable before/after
- one reusable template or skill pattern
- one 30-day review call scheduled during the initial engagement
- explicit case-study permission if the project works

## 45-minute meeting structure

- 5 min: rapport + "what does a great outcome look like for you?"
- 15 min: walk through the current workflow from trigger to output
- 10 min: review onboarding docs, SOPs, templates, or examples of good work
- 10 min: screen-share their tools and watch for friction
- 5 min: rank 1-3 opportunities by value, reliability, and adoption likelihood

Deliverable: same-day written recap with the agreed workflow, what is needed from them, the 7-day build plan, and the 30-day review date.

## Who to target

Best fit:

- expert-led local businesses
- 5-50 employees
- owner has strong taste, judgment, or professional standards
- business has onboarding docs, SOPs, templates, or repeated workflows
- team is busy but willing to adopt help inside existing tools
- there is a clear operational bottleneck or knowledge-transfer problem

Promising categories:

- dentists
- dermatologists
- therapists and wellness practices
- nutritionists
- consultants and coaches
- boutique professional services
- accountants, lawyers, and financial advisors where compliance boundaries are clear

Be careful with:

- healthcare or regulated finance workflows involving sensitive records, diagnosis, treatment, or regulated advice
- clients with no documentation and no willingness to let you observe work
- technical founders who already want to build it themselves
- solo operators with no budget or no repeated workflow
- large organizations with heavy IT approval processes

## Adoption rules

- Build inside existing tools whenever possible
- Hide the plumbing from the client
- Prefer drafts, summaries, routing, and preparation over full automation
- Add review gates before anything external is sent
- Do not automate broken processes
- Do not create a workflow that requires the client to remember a new dashboard
- Document ownership, credentials, prompts, and rules in client-owned spaces

## Folder layout

- `prospects/<name>/` - per-client research, outreach, meeting prep, notes, and deliverables
- `framework/` - reusable templates, playbooks, and skill patterns
- `ai-site-audit/` - website/audit experiments and public-facing assets
