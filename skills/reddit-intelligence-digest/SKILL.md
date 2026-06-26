---
name: reddit-intelligence-digest
description: Read and summarize Reddit discussions (posts + full comment trees) on a topic, using the read-only reddit-cli authenticated mirror. Use when Annabel wants to know what people on Reddit actually say about a place, product, or question, especially when the answer is buried in comments, and wants cited results rather than guesses.
audience:
  - annie
  - business-partner
runtime:
  - claude
  - codex
visibility: private
related_connections:
  - reddit-cli
---

# Reddit Intelligence Digest

Use this when the task is "what are people on Reddit actually saying about X" and
the useful detail lives in the **comments** (recommendations, local knowledge,
gotchas), not just post titles. Backed by the read-only `reddit-cli` connection.

## When to use

- Researching a place, gear, product, or open question via real user discussion.
- Discovering things people mention that you didn't already know to look for
  (e.g. kite spots named only in comment threads).
- Any time you'd otherwise guess at Reddit sentiment — read and cite instead.

Not for posting, voting, messaging, or anything that writes to Reddit. This is
read-only.

## First steps

1. `reddit-cli doctor --json` — confirm the session is valid. If it fails with a
   cookie/expiry error, the human re-captures the session (see the CLI README);
   do not try to work around the auth.
2. `reddit-cli agent-context` — current commands and auth model.

## Workflow

1. **Sync** the relevant subreddits, bounded. Search mode finds topical threads;
   listing mode mirrors a sub.
   - `reddit-cli sync -r <subs> -q "<query>" --limit 30 --time all`
   - Keep it bounded. Default `--limit 30`, `--time all` for topic discovery;
     narrow `--time` / use `--since` for "what's new lately" monitoring.
2. **Search** the mirror and read the hits:
   - `reddit-cli find "<query>" --json` (add `--kind comment` for comment-only,
     `-r <sub>` to scope).
3. **Synthesize** with citations. Every claim should point to a thread or comment
   URL from the results. Prefer quoting the commenter's own words for specifics
   (spot names, prices, conditions).
4. For bulk/domain processing, `reddit-cli export -r <subs> --json` gives posts
   with their comments as a stable JSON contract (this is how kite-wind-watch
   mines spot names).

## Output principles

- Lead with the answer, then the evidence. Group by theme, not by thread.
- Quote sparingly and attribute with a link. Note when something is one person's
  opinion vs. a repeated consensus (count how many threads/comments say it).
- Flag staleness: a 4-year-old comment about a venue may be out of date.

## Private-data handling

- Never print or commit the session cookie, the cURL blob, or the raw SQLite DB.
  Those are secrets / local-only (see the connection).
- Summaries and cited public-post quotes are fine to share. Do not assemble
  dossiers on individual Redditors or infer sensitive personal traits — that
  violates Reddit's policy and Annabel's safety rules.
- Keep volume polite and bounded; this rides Annabel's personal session.
