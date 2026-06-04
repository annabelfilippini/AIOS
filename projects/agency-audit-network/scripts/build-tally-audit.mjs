#!/usr/bin/env node
// Build the AIOS Starting Point Audit form in Tally via API.
// Source spec: research/templates/self-serve-audit.md
//
// Create new form:
//   TALLY_TOKEN=tly-... node scripts/build-tally-audit.mjs
//
// Update existing form:
//   TALLY_TOKEN=tly-... TALLY_FORM_ID=rjJo05 node scripts/build-tally-audit.mjs
//
// Block schema notes (reverse-engineered, undocumented):
// - TITLE / TEXT / HEADING_N / PAGE_BREAK: groupType matches type, html in payload.
// - Inputs (INPUT_TEXT, INPUT_EMAIL, TEXTAREA, LINEAR_SCALE, FILE_UPLOAD): own groupUuid,
//   groupType matches type, payload accepts isRequired + type-specific fields.
// - Option blocks (MULTIPLE_CHOICE_OPTION, DROPDOWN_OPTION, CHECKBOX): shared groupUuid
//   across all options in one question; groupType is the plural form
//   (MULTIPLE_CHOICE / DROPDOWN / CHECKBOXES); every option needs explicit
//   `isFirst` + `isLast` booleans in payload.
// - LINEAR_SCALE cannot be the first input block in the form; precede it with a
//   regular input (email capture handles this for us).

import { randomUUID } from 'crypto';

const TOKEN = process.env.TALLY_TOKEN;
if (!TOKEN) { console.error('Missing TALLY_TOKEN env var.'); process.exit(1); }
const FORM_ID = process.env.TALLY_FORM_ID || process.env.FORM_ID || '';

const API = 'https://api.tally.so';
const u = () => randomUUID();
const blocks = [];

// --- helpers ---
const push = (b) => blocks.push(b);
const formTitle = (txt) => push({ uuid: u(), type: 'FORM_TITLE', groupUuid: u(), groupType: 'TEXT', payload: { html: txt, title: txt } });
const h1 = (txt) => push({ uuid: u(), type: 'HEADING_1', groupUuid: u(), groupType: 'HEADING_1', payload: { html: txt } });
const h2 = (txt) => push({ uuid: u(), type: 'HEADING_2', groupUuid: u(), groupType: 'HEADING_2', payload: { html: txt } });
const h3 = (txt) => push({ uuid: u(), type: 'HEADING_3', groupUuid: u(), groupType: 'HEADING_3', payload: { html: txt } });
const para = (txt) => push({ uuid: u(), type: 'TEXT', groupUuid: u(), groupType: 'TEXT', payload: { html: txt } });
const pageBreak = () => push({ uuid: u(), type: 'PAGE_BREAK', groupUuid: u(), groupType: 'PAGE_BREAK', payload: {} });
const title = (txt) => push({ uuid: u(), type: 'TITLE', groupUuid: u(), groupType: 'TITLE', payload: { html: txt } });

const shortText = (label, opts = {}) => {
  title(label);
  push({ uuid: u(), type: 'INPUT_TEXT', groupUuid: u(), groupType: 'INPUT_TEXT', payload: { isRequired: !!opts.required, placeholder: opts.placeholder || '' } });
};
const email = (label, opts = {}) => {
  title(label);
  push({ uuid: u(), type: 'INPUT_EMAIL', groupUuid: u(), groupType: 'INPUT_EMAIL', payload: { isRequired: opts.required !== false } });
};
const longText = (label, opts = {}) => {
  title(label);
  push({ uuid: u(), type: 'TEXTAREA', groupUuid: u(), groupType: 'TEXTAREA', payload: { isRequired: !!opts.required, placeholder: opts.placeholder || '' } });
};
const scale = (label, start = 0, end = 5) => {
  title(label);
  push({ uuid: u(), type: 'LINEAR_SCALE', groupUuid: u(), groupType: 'LINEAR_SCALE', payload: { isRequired: false, start, end } });
};
const fileUpload = (label) => {
  title(label);
  push({ uuid: u(), type: 'FILE_UPLOAD', groupUuid: u(), groupType: 'FILE_UPLOAD', payload: { isRequired: false } });
};
const dropdown = (label, options) => {
  title(label);
  const g = u();
  options.forEach((text, i) => push({
    uuid: u(), type: 'DROPDOWN_OPTION', groupUuid: g, groupType: 'DROPDOWN',
    payload: { index: i, text, isFirst: i === 0, isLast: i === options.length - 1 }
  }));
};
const radio = (label, options) => {
  title(label);
  const g = u();
  options.forEach((text, i) => push({
    uuid: u(), type: 'MULTIPLE_CHOICE_OPTION', groupUuid: g, groupType: 'MULTIPLE_CHOICE',
    payload: { index: i, text, isFirst: i === 0, isLast: i === options.length - 1 }
  }));
};
const checkboxes = (label, options) => {
  title(label);
  const g = u();
  options.forEach((text, i) => push({
    uuid: u(), type: 'CHECKBOX', groupUuid: g, groupType: 'CHECKBOXES',
    payload: { index: i, text, isFirst: i === 0, isLast: i === options.length - 1 }
  }));
};

// =====================================================================
// FORM
// =====================================================================

formTitle('AIOS Starting Point Audit');
para("A guided diagnostic that turns the messy reality of your business into a structured brief an AI agency can act on. ~60–90 minutes. You can save and resume. You'll get a PDF you can hand to an agency.");

// --- Section 1: Intro + identification ---
h1('First, a little about you');
para("This tells us who's filling out the audit and where to send the PDF.");
email('What email should we send your PDF to?', { required: true });
shortText("What's your business name?", { required: true, placeholder: 'Your company' });
shortText('Industry and rough size (employees / revenue)?', { placeholder: 'e.g. landscaping, 3 employees, $400K rev' });
pageBreak();

// --- Section 2: 6-Layer Brain ---
h1('Section 1 of 13 — Your business at a glance');
para("Score your business across 6 layers of knowledge. AI doesn't fix broken processes — it amplifies them. This score tells us whether you should automate now, or write things down first.");
para("Scoring guide: 0 = does not exist · 1 = in someone's head only · 2 = somewhere but no one knows where · 3 = documented but not maintained · 4 = documented and occasionally updated · 5 = documented, discoverable, automatically maintained.");
scale('1. Identity — mission, products, ICP, brand voice, founder POV written down somewhere stable');
scale("2. Critical context — this quarter's goals, active campaigns, current pricing, deals in flight");
scale("3. Working memory — this week's sprint, in-progress deals, this week's content");
scale("4. Episodic memory — WHY decisions were made (paused outbound, fired vendor, pivoted segment)");
scale('5. Long-term knowledge — playbooks, won/lost notes, case studies, customer interviews');
scale('6. Background decay — a process that promotes current info and decays stale info');
pageBreak();

// --- Section 3: Pick engine ---
h1('Section 2 of 13 — Pick your engine');
para("Don't audit your whole business. Pick ONE engine. The audit goes deep on one workflow inside it.");
para("Acquisition: how you find and sign customers. Delivery: how you deliver the product/service. Support: how you handle post-sale. Internal: how the back office runs (hiring, finance, KB, data hygiene).");
dropdown('Which engine do you want to audit?', ['Acquisition', 'Delivery', 'Support', 'Internal']);
shortText('What specific workflow inside that engine do you want to map?', { required: true, placeholder: 'e.g. SDR outreach, client kickoff, support triage' });
pageBreak();

// --- Section 4: Leadership view ---
h1('Section 3 of 13 — Your role and your team (leadership view)');
para("Answer as the person who owns the KPI. If you're the owner-operator, you answer for yourself. Short answers are fine — bullet points work.");
longText("What's your role, and what's your team responsible for?");
longText('What are the main KPIs your team owns this quarter or this year?');
longText('Who owns the workflow you picked, and who is accountable if it improves or breaks?');
longText('Where are the biggest bottlenecks, delays, or expensive handoffs in this workflow?');
longText('Which tasks consume the most hours, dollars, or leadership attention?');
longText('What are the main tools your team relies on, and where do people work outside the official system?');
longText('If you could fix one workflow in the next 90 days, what would move the business most? Why?');
longText('What prevents the team from being more efficient or effective today?');
longText('Which KPI is most at risk if this workflow stays the same? What happens financially if you miss?');
longText('Roughly how many people / hours are tied up in your top 2 bottlenecks?');
longText('Any compliance, security, or customer risks tied to current processes?');
longText('Who would champion a new tool, who would resist, and who needs to sign off? Name roles or people if you can.');
pageBreak();

// --- Section 5: On-the-ground view ---
h1('Section 4 of 13 — Your daily work (on-the-ground view)');
para("Now switch perspectives. Answer as the person who DOES the work. If your employee does it, fill it out AS them — or better, have them answer this section.");
longText('Walk through a typical day or week in this role. What are the 1–3 most common tasks?');
longText('How much of the day goes to the core job vs. administrative or repetitive tasks?');
longText('Walk through the workflow you picked at a high level. Which part is most manual or takes longest?');
longText('What information has to be gathered, where does it come from, and what gets created at the end?');
longText('What software is the doer in all day? Where is there double-entry, copy-paste, or tool frustration?');
longText('How is work currently tracked and reported on?');
longText("How do you know you've done this task correctly? What does \"done well\" mean?");
longText('If the most repetitive part disappeared tomorrow, what higher-value work would replace it?');
longText('What would make you actually TRUST an AI assist here?');
longText('When you finish this task, who confirms it\'s done? Or does the work just disappear into someone else\'s inbox?');
pageBreak();

// --- Section 6: Deep dive (both branches inline) ---
h1('Section 5 of 13 — Deep dive');
para('Answer only the branch that matches the engine you picked earlier. If you picked Acquisition, answer 5A. If you picked Delivery, Support, or Internal, answer 5B.');

h2('5A. Sales Discovery (skip if you didn\'t pick Acquisition)');
longText('What pressure are you under this quarter? What\'s your specific revenue target?');
longText('Which KPI keeps you up at night — the one that if it fails is game over?');
longText('Paint a picture of your sales org: team size, roles, and who owns prospecting, closing, renewals.');
longText('Current win rate, average deal size, new opportunities per month, typical close cycle, and weekly team hours.');
longText("If win rate, qualified pipeline, or cycle time improved slightly, what's that worth this quarter?");
longText("Last deal that took way longer than it should have — what happened?");
longText('Where do deals typically get stuck or slow down?');
longText('If lead volume doubled tomorrow, what would break first?');
longText('Make-or-break moment in your sales process — the keystone.');
longText('Which team-to-team handoffs create the most problems?');
longText("Official tools in your stack — CRM, email sequences, enrichment, calling, proposals?");
longText('Which tools do reps skip or work around, and where does bad data cost time or deals?');
longText("Biggest data problems? (Wrong contacts, missing info, bad-fit leads, duplicates.) How often do they show up?");
longText('3 biggest obstacles to hitting revenue target — rank them.');
longText('Biggest opportunity: more qualified leads at top, faster cycles, or higher close rates? Pick one and explain.');
longText('How would you know in 30 days you\'re succeeding?');
longText('Who are your champions, resisters, and fence-sitters? What made the last successful change stick?');
longText('Biggest serious incident or near-miss in the last 6 months. Single biggest point of failure today.');
longText('If your CRM went down for 48 hours, walk through what happens.');

h2("5B. End-User Workflow Deep Dive (skip if you DID pick Acquisition)");
longText("Walk through yesterday — what was actually done vs. what was planned?");
longText('How many times is the most common task done daily / weekly? What makes the busiest day hard?');
longText("If your most repetitive task disappeared, what would replace it?");
longText('Last time the workflow you picked took forever — what went wrong?');
longText("Walk through the exact steps when it goes normally. Which part takes longest?");
longText('Where do you have to stop and think, make a judgment call, or ask someone what to do next?');
longText("How does the process change for different deals/customers/situations?");
longText("When do errors typically happen, and how are mistakes caught before they become a problem?");
longText('What do you do with bad, incomplete, or conflicting information?');
longText('Last time you had to wait for someone else to do your job. Where do you hand off?');
longText("Make-or-break step in the process.");
longText("Where do tools, double-entry, copy-paste, or unofficial shortcuts create friction?");
longText("If you had an assistant for one day, what would they do?");
longText('What reports, updates, or status notes do you create manually?');
longText("What would make you 20% more productive starting next week?");
longText("If AI could help with part of your job, what would be your FIRST concern?");
longText('What parts of your work would you NEVER want automated? Why?');
fileUpload('OPTIONAL: Loom recording of yourself doing the task end-to-end (upload here)');
pageBreak();

// --- Section 7: Step Cards ---
h1('Section 6 of 13 — Turn the workflow into Step Cards');
para('You already described the workflow in plain English. Now break it into individual steps so an agency can estimate, quote, and build without re-interviewing you.');
para('Most workflows have 5–15 steps. If you have more than 20, you may be mapping more than one workflow.');
para('For each step, use this format: Step #, Step name, Owner/role, Tool(s), Input, Output, Volume, Doing time, Wait time, Common errors, Risk/sensitivity, Who confirms it is done, Friction tag.');
longText('Create your Step Cards here. Repeat the format for each step in order.');
fileUpload('OPTIONAL: Upload a spreadsheet, screenshot, Loom, or existing process doc that shows the workflow');
pageBreak();

// --- Section 8: Find your keystone ---
h1('Section 7 of 13 — Find your keystone');
para('A keystone is the step where if it fails, NOTHING else matters. Most workflows have one. Use the two prompts below to find yours.');
longText("Which step is the keystone: the one where failure collapses the workflow, loses the customer, or creates the costliest cleanup later?");
longText("Why is that step the keystone? Mention multiplier effect, point of no return, customer visibility, or downstream cleanup cost.");
shortText("Mark your KEYSTONE step here:", { placeholder: 'e.g. step #4 — proposal sent' });
pageBreak();

// --- Section 9: QDOAA ---
h1('Section 8 of 13 — Run QDOAA on your tagged steps');
para('Use the Step Cards from Section 6. For each step you tagged with friction — especially your keystone — run QDOAA before deciding what to automate.');
para('Q-D-O-A-A: Question (purpose?), Delete (zero-value?), Optimize (half the resources?), Accelerate (parallel?), Automate (only NOW).');
longText("Q — What's the actual purpose of each friction-tagged Step Card? What happens if you stop doing it?");
longText('D — What contributes no measurable value? What can be removed with zero negative impact?');
longText('O — If you had half the resources, how would you do this? What\'s the 20% creating 80% of results?');
longText('A — Where can you move faster without breaking quality? What can run in parallel?');
longText("A — What can be delegated, templatized, automated? Only NOW, once Q-D-O-A are done.");
pageBreak();

// --- Section 10: Score opportunities ---
h1('Section 9 of 13 — Score your opportunities');
para('Every tag is a candidate fix. Score 1–5 on six dimensions: Impact, Effort (lower better), Risk (lower better), Adoption, Confidence, Data Readiness. Priority = (Impact × Confidence) − (Effort + Risk + (6−Adoption) + (6−Data Readiness)). Keystones get +2 Impact.');
longText('List your top 3–5 candidate fixes (one per line) with rough scores. Or just describe them in plain English — the agency will help score in their scoping call.');
pageBreak();

// --- Section 11: ROI ---
h1('Section 10 of 13 — ROI + Cost of Inaction');
para('Put dollars on your top fixes. This anchors the agency quote and shows what doing nothing may keep costing you.');
para('Hours saved/wk = baseline × % saved. Annual cost saved = hours × loaded $/hr × 52. Loaded $/hr = (salary + benefits + taxes + overhead) / 2080. Annual revenue uplift = hours unlocked × value/hr × 52. Payback (months) = one-time cost / (annual net / 12).');
longText('Fix 1: name, baseline hours/wk, % time saved, loaded $/hr, annual cost saved estimate, revenue uplift estimate, one-time cost.');
longText('Fix 2: same fields.');
longText('Optional Fix 3: same fields, only if there is a third clear candidate.');
fileUpload('OPTIONAL: Upload any spreadsheet or notes you already use to estimate savings, revenue impact, team hours, or ROI.');
pageBreak();

// --- Section 12: Quick Wins ---
h1('Section 11 of 13 — Quick Wins (what you\'d build first)');
para("Pick 2–3 fixes from the top of your scored list. For each, fill the card below. This is what the agency will quote and build against.");

h2('Quick Win #1');
shortText('Fix name', { placeholder: 'e.g. AI-drafted outbound emails' });
shortText('Step(s) it touches', { placeholder: 'e.g. step #2, #3 from your map' });
longText('Current vs. Future (one sentence each)');
shortText('Internal owner — who owns the outcome of this fix inside your business?');
longText('Success criteria — what specific numbers would prove this fix worked, by when, and what result would mean it needs to be changed or stopped? Example: "Email drafting time drops from 8 minutes to 90 seconds by week 4, quality stays at 95%+, and if adoption is under 30%, the workflow needs to change."');
longText('Acceptance rules — 3–5 specific rules the agency build MUST hit.');

h2('Quick Win #2');
shortText('Fix name', { placeholder: 'Quick Win #2' });
shortText('Step(s) it touches');
longText('Current vs. Future');
shortText('Internal owner');
longText('Success criteria — what specific numbers would prove this fix worked, by when, and what result would mean it needs to be changed or stopped?');
longText('Acceptance rules');

h2('Quick Win #3 (optional)');
longText('Optional third Quick Win: fix name, step(s), DRI, Definition of Done, and acceptance rules.');
pageBreak();

// --- Section 13: Handoff Brief constraints ---
h1('Section 12 of 13 — Constraints the agency should know');
longText('Data access — what systems are reachable, what isn\'t, who can grant access');
longText('Risk / compliance — any data sensitivities, regulatory constraints, customer NDAs in play');
longText("Adoption reality — who'll champion this, who'll resist (pulled from your earlier change-map answer)");
shortText('Rough budget for Phase 1 build (optional)', { placeholder: 'e.g. $5K–$15K' });
checkboxes('What you want from the agency (pick any):', [
  'Build the 2–3 Quick Wins above',
  'Build + train the team to operate it',
  'Build + train + ongoing maintenance',
  'Strategy and architecture review only (no build)'
]);
pageBreak();

// --- Section 14: One last question ---
h1("Section 13 of 13 — One last question");
para("You've got a PDF. The PDF works whether you find an agency on your own or have one brought to you.");
radio('Do you want help finding an agency?', [
  'Yes — help me find an agency. (Annabel will personally vet your brief and intro 2–3 vetted agencies that fit your shape. Free to you. Annabel earns a referral fee from the agency, never from you.)',
  "No — I'll find one myself. My PDF is ready."
]);
para('If you picked Yes, we\'ll be in touch within 2 business days. If you picked No, your PDF is in your email and you\'re done — good luck.');

// --- POST ---
const body = { status: 'DRAFT', name: 'AIOS Starting Point Audit', blocks };
const method = FORM_ID ? 'PATCH' : 'POST';
const endpoint = FORM_ID ? `${API}/forms/${FORM_ID}` : `${API}/forms`;

console.log(`${FORM_ID ? 'Updating' : 'Building'} form with ${blocks.length} blocks...`);
const res = await fetch(endpoint, {
  method,
  headers: { 'Authorization': `Bearer ${TOKEN}`, 'Content-Type': 'application/json' },
  body: JSON.stringify(body)
});

const json = await res.json();
const expectedStatus = FORM_ID ? 200 : 201;
if (res.status !== expectedStatus) {
  console.error('FAILED', res.status, JSON.stringify(json, null, 2).slice(0, 2000));
  process.exit(1);
}

console.log('SUCCESS');
const id = json.id || FORM_ID;
console.log(`Form ID: ${id}`);
console.log(`Edit URL: https://tally.so/forms/${id}/edit`);
console.log(`Live URL (once published): https://tally.so/r/${id}`);
