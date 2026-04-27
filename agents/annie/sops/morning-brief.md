# Morning Brief SOP

Last updated: 2026-04-27

## Purpose

Send Annabel a useful morning email that helps her start the day with clarity, priorities, and follow-through.

## Trigger

Daily morning automation.

## Sender

Annie may send this from:

- `anniestarostin@gmail.com`

The local delivery script now prefers `anniestarostin@gmail.com` through the `annie-briefing-gmail` Keychain item. Until that app password exists, it falls back to the legacy `annabelflip1@gmail.com` sender so the morning email does not silently stop.

## Recipient

Annabel.

TODO: Confirm preferred recipient email address.

## Inputs

- Annie's calendar
- Annabel's calendar view at `annabelflip1@gmail.com`
- Annie inbox items
- AI-OS project context
- recent Annie workspace reports
- explicit notes or tasks Annabel has given Annie

## Current Draft Format

Subject:

```text
Annie Morning Brief - Mon DD
```

Body:

```text
Good morning Annabel,

1. Command Center
- What changed since yesterday
- Repeated/no-new sections omitted
- Briefing sources included

2. Open Follow-Ups
- [Open todos or follow-through items]

3. Consulting Outreach
- [Active prospect folders]
- [Replies or follow-ups due once connected]

4. Briefing Details
- Only include genuinely new intelligence.
- Omit world news if there is nothing meaningfully new.
```

## Repetition Rules

Annie should not repeat news day to day just because the scan found another article about the same ongoing topic.

If the scan does not surface meaningful new world news, omit the world news section entirely.

The local email script filters repeated briefing items against the prior 7 days and omits raw sources from the email body. Source links remain in the underlying markdown files.

## Rules

- Keep the brief skimmable.
- Put urgent or time-sensitive items first.
- Do not include filler.
- Distinguish facts from assumptions.
- Do not invent calendar context, client facts, or commitments.
- If there is nothing important in a section, omit it.
- Include links only when they are useful.
- Prefer a shorter email over a repeated email.

## Output

- Email sent to Annabel.
- Optional copy saved in `agents/annie/workspace/reports/`.

## Approval

No approval required for sending the morning brief to Annabel.

Any external action recommended inside the brief still follows the access policy and relevant SOP.

## Format Iteration Notes

TODO: Refine with Annabel after reviewing the first few morning emails.
