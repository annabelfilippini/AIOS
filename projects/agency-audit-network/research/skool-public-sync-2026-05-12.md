# Skool Public Sync Notes

Date: 2026-05-12

## Command

```bash
node operations/annabel-press/scripts/skool-press.mjs sync --public-only
```

## Result

Public-only sync succeeded for the currently configured Skool account.

## Configured Account

- Early AI-dopters / Mark Kashef
- URL: `https://www.skool.com/earlyaidopters`
- Public status: private paid community
- Public price signal: `$77/month`
- Public size signal: about `1.4k` members, about `80` online
- Public course/topic signals: Claude Code, AI Consulting Playbook, How to Sell AI Solutions, Done-for-you Claude Code, automation/systems themes

## Interpretation

This community looks relevant for agency partner sourcing because it is explicitly centered on AI consulting, selling AI solutions, Claude Code systems, and done-for-you implementations.

Public-only data is enough to confirm community relevance, but not enough to identify member-level agency partners. For partner candidates, the next pass needs either:

- Mansel's Skool community URL, plus public-only sync; or
- Annabel-approved authenticated sync for subscribed communities.

## Next Step

Add Mansel's Skool URL to `operations/annabel-press/skool/accounts.json`, then rerun public-only sync. If Annabel wants member-level candidate research, use an approved temporary session export and save only summarized candidate notes in `partners/`.

