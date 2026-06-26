---
date: 2026-06-08
time: 12:10
project: vital-health-webflow-review
status: complete
next-session: If marquee blank-space reappears, capture browser + viewport width + URL bar + a clean (non-hovered) screenshot before changing anything else.
---

# Session: Vital Health reviews marquee ported to Vercel and tuned

## What we worked on

- Ported the new "In patients' words." marquee (real 5-star Google reviews, 68 cards with avatars and Google place-page links) from [home-review.html](projects/websites/vital-health-review/home-review.html) into the deployed [client-share/vital-health-preview-html/index.html](projects/websites/vital-health-review/client-share/vital-health-preview-html/index.html).
- Replaced both the old `.rev-feed-*` mock-cards CSS and the 4 placeholder cards with the new `.rev-marquee` / `.rev-card` block from home-review.
- Deployed to Vercel project `vital-health-deploy` → <https://vital-health-deploy.vercel.app> .
- User reported large blank space on the right of the marquee. Could not consistently reproduce in Playwright at 2000x900 (5–6 cards visible at every 500ms sample), but hardened the layout anyway.

## Decisions made

- Vital Health deploy folder is `client-share/vital-health-preview-html/` (Vercel project `vital-health-deploy`, alias `vital-health-deploy.vercel.app`). `home-review.html` is the heavy working source; the deploy folder has its own slimmer pages with non-`-review.html` link patterns and must not be naively overwritten.
- Marquee uses 3 identical `.rev-marquee-set` copies (204 cards on the track) with keyframe `translate3d(-33.333%, 0, 0)` so the loop wraps exactly on a set boundary regardless of viewport width.
- Animation duration: 150s desktop, 120s mobile (started at 240s/200s, briefly tried 90s/70s — too fast).
- Edge fade mask tightened to 1% (was 2.5%) so cards feel dense at the edges.
- Always `cd` into `client-share/vital-health-preview-html/` before running `vercel --prod --yes`. Once accidentally deployed from `projects/websites/vital-health-review/` and pushed a different project (`vital-health-review.vercel.app`) — recovered by redeploying from the right folder.

## Open questions

- Root cause of the user's original blank-space screenshot is still unconfirmed. Hypotheses: hover/focus-within paused the animation at a transient frame; reduced-motion was on; or a snap-back frame artifact in their browser. The 3-set buffer + slower clean wrap should mask all of these.
- Whether to remove the `:hover` / `:focus-within` pause behavior on `.rev-marquee-track` to prevent any future "frozen-mid-scroll" screenshots — user has not asked for this yet.
- Whether home-review.html should ever be the canonical source for the deployed homepage, or whether the deploy folder stays its own thing (currently the answer is: stay separate, port targeted changes).

## Next steps

- If the blank-space gap returns, capture a non-hovered screenshot with browser name and viewport width before changing anything.
- If/when other home-review.html changes need to ship, repeat the targeted-port pattern (CSS block + section block) rather than overwriting index.html — the nav links and structure differ between the two files.

## Context to preserve

- Vercel project: `vital-health-deploy` (orgId `team_40AJMIX770P6E3pe7neFseHD`, projectId `prj_FVn54Oemq5sCIi0AdexXNh7XF8Fe`). Config in `client-share/vital-health-preview-html/.vercel/project.json`.
- Marquee CSS bounds inside the deploy index.html: lines ~38–212 (rev-* styles), keyframe block, plus reviews `<section id="google-reviews">` from line ~394.
- Each `.rev-marquee-set` is ~27,472px wide at desktop card size (380px flex-basis + 24px gap). Track width with 3 sets ≈ 82,416px.
- Avatars come from `lh3.googleusercontent.com`; "View on Google →" links all point at `place_id:ChIJcUlyRoo5W4YR6DO73UlEgjg`.
- Sibling Vercel project `vital-health-hormone-carousel` also lives in this folder — do not confuse the two.

## System refinement candidates

- Worth a [[feedback-vercel-deploy-cwd]] memory: before `vercel --prod`, verify CWD by reading `.vercel/project.json` and the projectName; one wrong `cd` shipped the wrong project this session.
