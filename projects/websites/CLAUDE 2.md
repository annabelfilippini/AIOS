# CLAUDE — Website Projects

How website work in `projects/websites/` is organized. Read this before building
or revising any site in this folder. It applies to every runtime (Claude, Codex,
or any capable LLM), not just Claude.

## Three design layers, read in this order every time

1. `projects/websites/design.md` (GLOBAL). Taste and standards true for every
   site: vibe lanes, hero/shape/type/color rules, photography and licensing,
   no weird phrases as headings, fact-checking, verification. Durable
   cross-project preferences.
2. `projects/websites/<project>/design.md` (BRAND). This one site's direction:
   its real colors, type, voice, art direction, page architecture, and a running
   iteration log of what Annabel approved, liked, or rejected.
3. `projects/websites/<project>/content.md` (FACTS). This one site's verified
   information: real services, prices, hours, names, claims, links. The source of
   truth that stops the build from inventing things.

design.md is how a site looks, feels, and sounds. content.md is what is true.

Split test for where something belongs: "Would this change between two different
clients?" If yes, it is project level (that project's design.md or content.md).
If no, it is global (the shared design.md).

## Start a new site

Copy `_template/` into `projects/websites/<project>/`, then fill in `design.md`
and `content.md` before building anything. Keep facts in content.md, not
scattered through the markup.

## While building

- Build from `content.md`. If a fact is not verified, mark it and confirm before
  it becomes live copy (see global design.md: Content and Verification).
- Follow the global photography and licensing rules for every image.
- Pick one vibe lane from the global design.md and stay in it.

## After building, keep the docs current

When you change a site, before you finish:

- Update that project's `design.md`: decisions made, what was liked or rejected,
  a dated iteration-log entry.
- Update that project's `content.md`: any fact that changed or was newly
  verified.
- If a preference proved true for every site, promote it to the global
  `design.md`.

A Stop hook (`~/.claude/hooks/update-design-docs.sh`) reminds you if site files
changed this session but these docs did not.

## Client work

The full process (intake, audit, preview, rebuild, proposal) lives in the
`client-website-refresh` skill. Use it for client engagements.
