#!/usr/bin/env node
// Build the free AI Starting Point Audit preview form in Tally via API.
// Source spec: research/templates/free-audit.md
//
// Create new form:
//   TALLY_TOKEN=tly-... node scripts/build-tally-free-audit.mjs
//
// Update existing form:
//   TALLY_TOKEN=tly-... TALLY_FREE_FORM_ID=abc123 node scripts/build-tally-free-audit.mjs

import { randomUUID } from 'crypto';

const TOKEN = process.env.TALLY_TOKEN;
if (!TOKEN) {
  console.error('Missing TALLY_TOKEN env var.');
  process.exit(1);
}

const FORM_ID = process.env.TALLY_FREE_FORM_ID || process.env.TALLY_FORM_ID || process.env.FORM_ID || '';
const API = 'https://api.tally.so';

const u = () => randomUUID();
const blocks = [];

const push = (b) => blocks.push(b);
const formTitle = (txt) => push({ uuid: u(), type: 'FORM_TITLE', groupUuid: u(), groupType: 'TEXT', payload: { html: txt, title: txt } });
const h1 = (txt) => push({ uuid: u(), type: 'HEADING_1', groupUuid: u(), groupType: 'HEADING_1', payload: { html: txt } });
const para = (txt) => push({ uuid: u(), type: 'TEXT', groupUuid: u(), groupType: 'TEXT', payload: { html: txt } });
const pageBreak = () => push({ uuid: u(), type: 'PAGE_BREAK', groupUuid: u(), groupType: 'PAGE_BREAK', payload: {} });
const title = (txt) => push({ uuid: u(), type: 'TITLE', groupUuid: u(), groupType: 'TITLE', payload: { html: txt } });

const shortText = (label, opts = {}) => {
  title(label);
  push({
    uuid: u(),
    type: 'INPUT_TEXT',
    groupUuid: u(),
    groupType: 'INPUT_TEXT',
    payload: { isRequired: !!opts.required, placeholder: opts.placeholder || '' }
  });
};

const email = (label, opts = {}) => {
  title(label);
  push({
    uuid: u(),
    type: 'INPUT_EMAIL',
    groupUuid: u(),
    groupType: 'INPUT_EMAIL',
    payload: { isRequired: opts.required !== false }
  });
};

const longText = (label, opts = {}) => {
  title(label);
  push({
    uuid: u(),
    type: 'TEXTAREA',
    groupUuid: u(),
    groupType: 'TEXTAREA',
    payload: { isRequired: !!opts.required, placeholder: opts.placeholder || '' }
  });
};

const dropdown = (label, options) => {
  title(label);
  const g = u();
  options.forEach((text, i) => push({
    uuid: u(),
    type: 'DROPDOWN_OPTION',
    groupUuid: g,
    groupType: 'DROPDOWN',
    payload: { index: i, text, isFirst: i === 0, isLast: i === options.length - 1 }
  }));
};

// =====================================================================
// FORM
// =====================================================================

formTitle('Free AI Starting Point Audit');
para('A short diagnostic for small business owners who want to see where AI actually belongs. It points you toward the most useful workflow to inspect first, without turning into a giant homework assignment.');

h1('First, where should this go?');
email('What email should I send your preview to?', { required: true });
shortText('Your name', { required: true, placeholder: 'Name' });
shortText('Business name', { required: true, placeholder: 'Company' });
pageBreak();

h1('The 8-question preview');
para('Keep this plain-English and specific. A good answer is usually a few sentences, not a strategy memo.');

shortText('1. What kind of business is this, and roughly how big is it?', {
  required: true,
  placeholder: 'e.g. home services, 8 employees, $1.2M revenue'
});

dropdown('2. Where do you feel the most operational pressure right now?', [
  'Acquisition — finding, qualifying, or signing customers',
  'Delivery — onboarding, fulfillment, client work, or service delivery',
  'Support — follow-up, customer questions, issue handling, retention',
  'Operations — admin, finance, scheduling, reporting, internal handoffs'
]);

longText('3. What is one workflow or process you wish worked better?', {
  required: true,
  placeholder: 'e.g. client onboarding, quoting, appointment follow-up, weekly reporting'
});

dropdown('4. What usually goes wrong in that workflow?', [
  'It takes too much time',
  'People wait on each other or handoffs get stuck',
  'Errors, rework, or missed details happen too often',
  'The data is scattered, incomplete, or hard to trust',
  'Customers can feel the friction',
  'There is compliance, privacy, or business risk'
]);

dropdown('5. How often does this workflow happen?', [
  'Many times per day',
  'A few times per week',
  'A few times per month',
  'Only occasionally, but it is high-stakes'
]);

shortText('6. Who touches this workflow?', {
  required: true,
  placeholder: 'e.g. owner, ops manager, sales rep, assistant, technician'
});

shortText('7. What tools or systems are involved?', {
  required: true,
  placeholder: 'e.g. Gmail, Shopify, QuickBooks, CRM, spreadsheets, paper forms'
});

dropdown('8. If this improved in the next 90 days, what would matter most?', [
  'Save owner or team time',
  'Respond faster to customers or leads',
  'Reduce mistakes or rework',
  'Create cleaner reporting or visibility',
  'Make the business easier to hand off or scale'
]);
pageBreak();

h1('What you will get back');
para("After you submit, I'll review your answers and send back a short starting-point readout: where AI may belong first, what kind of friction is showing up, and the next best step I'd recommend.");
para('The paid audit goes deeper: Step Cards, friction tagging, QDOAA cleanup, ROI, Quick Wins, success criteria, implementation constraints, and an agency-ready handoff.');

// --- POST ---
const body = { status: 'DRAFT', name: 'Free AI Starting Point Audit', blocks };
const method = FORM_ID ? 'PATCH' : 'POST';
const endpoint = FORM_ID ? `${API}/forms/${FORM_ID}` : `${API}/forms`;

console.log(`${FORM_ID ? 'Updating' : 'Building'} free audit form with ${blocks.length} blocks...`);
const res = await fetch(endpoint, {
  method,
  headers: { Authorization: `Bearer ${TOKEN}`, 'Content-Type': 'application/json' },
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
