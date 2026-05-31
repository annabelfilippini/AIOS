# Opportunity Patterns

## Hand-Assembled Weekly Numbers

Signal: the operator opens multiple dashboards, spreadsheets, or exports to
understand the week.

Opportunity: create one weekly summary and a short operator brief.

Route:

- Annie drafts the summary shape.
- Garry judges whether this is valuable to the offer.
- Business Partner checks data access and implementation path.

## Human Router

Signal: requests, leads, tickets, or documents pile up and the operator forwards
them manually.

Opportunity: triage queue, routing rules, draft responses, and approval gates.

Keep human approval for anything external.

## Repetitive Specialist Drafting

Signal: expensive human time goes to recurring drafts, summaries, letters,
reports, briefs, or internal notes.

Opportunity: specialist drafter plus review workflow.

Good first artifact: draft-only output folder and approval checklist.

## Raw Document Pile

Signal: PDFs, docs, spreadsheets, transcripts, emails, screenshots, or exports
exist but are not consistently readable by agents.

Opportunity: raw drop zone, converted text folder, and summary process.

This is often the real first step before AI adds value.

## Unread Customer Voice

Signal: reviews, surveys, support tickets, call transcripts, comments, or
community messages exist but nobody mines them weekly.

Opportunity: theme clustering, quote extraction, and a customer voice brief.

Garry can help decide whether this becomes positioning, product, or retention
work.

## Existing Automation That Almost Works

Signal: a Zapier, Make, n8n, script, or app automation exists but does not quite
solve the business problem.

Opportunity: audit before rebuilding. Keep what works, add summaries or approval
gates where needed.

## Available CLI Or Tool Connection

Signal: a tool has a CLI or API path and the operator's work depends on it.

Opportunity: add a CLI connection in `AI-OS/cli-connections/` or a skill in
`AI-OS/skills/` only if it supports repeated work.

Do not add tools to look sophisticated. Add them when they make a workflow
repeatable.

## Sensitive Or Regulated Data

Signal: health, legal, finance, identity, customer private data, or account
permissions are involved.

Opportunity: define boundaries first. Automation comes after access rules,
approval gates, and verification.
