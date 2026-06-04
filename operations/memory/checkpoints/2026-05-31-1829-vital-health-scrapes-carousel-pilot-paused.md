---
date: 2026-05-31
time: 18:29
project: vital-health-webflow-migration
status: paused
next-session: Resume by gathering Annabel's inspo posts, desired ad/content topics, and carousel goals before generating more Vital Health content.
---

# Session: Vital Health Scrapes Carousel Pilot Paused

## What we worked on

- Annabel considered installing Simon/Scrapes `@scrapes/skill-systems` to help create Instagram content for Vital Health.
- Codex inspected the npm package and confirmed the relevant system is `00-social-content`, not the entire bundle.
- Annabel installed `00-social-content` into `projects/vital-health-webflow-migration`.
- Codex verified the install created 1 system, 18 skills, 3 agents, `brand_context/`, and `projects/`, plus a global Claude update-check hook.
- Codex then moved too quickly and created a dry-run Vital Health Instagram carousel before Annabel had supplied inspo posts or decided what the ads/content should talk about.

## Decisions made

- Keep the `00-social-content` install for now.
- Treat the generated carousel as a **pilot artifact only**, not as the actual creative brief or approved direction.
- Use Scrapes/Claude for pipeline structure and repeatable folders, but use Codex/Annabel for visual judgment and image direction.
- Keep publishing off; `ZERNIO_API_KEY` should remain blank for now.
- Vital Health content must stay medically restrained: no cure/guarantee/reversal/outcome-promise language.

## Open questions

- What specific Instagram/ad topics should Vital Health post about first?
- Is the goal organic content, ads, weekly automation, service education, patient trust-building, or all of these?
- What inspo posts/carousels does Annabel want the style to follow?
- Should the output look close to the Vital Health website, or borrow more heavily from the inspo posts?
- Should generated visuals use only existing Vital Health assets, generated clinical still-lifes, or a mix?

## Next steps

1. Ask Annabel for inspo posts/screenshots/links before making more content.
2. Ask what the first 3-5 carousel/ad topics should be.
3. Convert her inspo into a small creative brief: palette, composition, typography, image treatment, content rhythm.
4. Decide whether to run the native Claude `/00-social-content` pipeline or use the installed folder structure manually with Codex-rendered images.
5. Only then generate a new carousel draft.

## Context to preserve

- Installed Scrapes path: `/Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration/.claude/skills/00-social-content`
- Vital Health brand context was seeded by Codex at `/Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration/brand_context/`.
- Pilot output lives at `/Users/annabelfilippini/Documents/AI-OS/projects/vital-health-webflow-migration/projects/00-social-content/2026-05-31/vital-health-different-kind-of-care/`.
- The pilot includes `index.html`, `caption.md`, `post.yaml`, `slide-1.png` through `slide-5.png`, and `carousel-contact-sheet.png`.
- `brand_context/templates/instagram-carousel/manifest.json` was marked `pilot`, not `ready`, so Claude should not mistake it for a completed native Scrapes template pool.

## System refinement candidates

- When Annabel asks whether a tool/pipeline could be useful, Codex should first evaluate and ask for creative inputs before prototyping visible output.
- For social/content generation, require a lightweight brief before generation: objective, audience, topic, inspo references, brand constraints, and approval boundary.
