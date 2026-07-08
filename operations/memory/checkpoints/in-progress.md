# In progress — The Edit consolidation (Life OS)

Session 2026-06-27. Collapsing 5 style surfaces -> ONE feed (The Edit) + ONE morning debrief.

## Done + verified
- Batch 1: ShopMy refresh (refresh_sources.py, merge-safe, 1383 pins), Pinterest scrape
  (refresh_pinterest.py, 28 real pins), daily cron (crontab 30 6, refresh_all.sh).
- Batch 2a: build_feed.py ingests Pinterest ("Inspiration" tab) + closet ("My Closet" tab)
  into feed.html. Both ♥/✕ -> feedback.json. Verified live.

## LIVE for review (leave running)
projects/style-feed/serve.py 8801 -> http://localhost:8801/feed.html
Restart: cd projects/style-feed && python3 serve.py 8801

## Next — paused for Annabel's feedback on the live feed
- 2b: one Morning Debrief = day-planner/morning.html canonical + the-edit.html card CSS;
  link from The Day's Morning pill AND The Edit (same link). Outfits use owned + aspirational.
- 2c: life-os/serve.py "The Edit" tab -> feed.html (was the-edit.html); retire lookbook.html,
  quickchoose.html, the-edit.html, pinterest-board/. Watch: serve.py cross-module banner
  keys off the-edit.html occasion cards (will need rework).

Full detail: 2026-06-27-1745-life-os-the-edit-one-feed-live.md
- 2026-07-08: Fable audit batch 1 done — retargeted guardrails/investigate skill symlinks, created agents/shared/handoffs/{active,archive}, pruned 46 old hook state markers, removed dead website-audit from /begin. Batch 2 (hook consolidation + READMEs) awaiting go-ahead.
- 2026-07-08: Fable audit batch 2 done — recall.mjs status-bonus age decay + crash-proof reads, BB stripped from Stop hooks and /begin, state-marker auto-prune added, insta hooks kept. Remaining: checkpoint-skill slug/close-out rules, skills README, refinement candidate from May 25.
- 2026-07-08 batch 3 (Opus): created skills/README.md (skill map + authoring standard), added slug/supersede rules to checkpoint SKILL.md (both copies byte-identical), applied USER.md skill renames (garry-office-hours-lite→office-hours-lite, garry-ceo-review-lite→ceo-review-lite), archived May 25 refinement candidate as status:processed. Beehiiv rotation-after-2026-07-05 check: NO (scratchpad.md only notes it needs rotation, account discontinued).
