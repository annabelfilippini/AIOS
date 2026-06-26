# Brand DNA Audit — build from the client's side, not your house style

Use this at the START of any client website build, before designing anything. The
failure mode it prevents: pouring the client's photos and copy into Annabel's
default lane (cream/serif/editorial) so the site is *her taste with their
content*, instead of *their brand*. A business with real personality, colors, and
people deserves a site that looks like THEM. This is the difference between a
generic-but-pretty site and one the client recognizes as their own.

The method: audit every channel the client already has, extract their real
identity, agree the one direction decision, then build from their tokens.

## 1. Audit every channel they already have

Pull from all of these (whatever exists). Each one answers a different question.

- **Their live site** — the single richest source. Scrape it with Firecrawl using
  the `branding` format, which extracts real design tokens (colors, fonts,
  component styles, border-radius, even a `personality` tone/energy read):

  ```
  firecrawl_scrape(url, formats: ["markdown","branding","links"], waitFor: 8000, onlyMainContent: false)
  ```

  `markdown` gives you their real voice and copy; `branding` gives you the actual
  hex colors, font families, and button shapes off their CSS. Also scrape their
  About / "our story" / team page for the founder story and real roster.

- **Their logo** — READ the image file (it is the strongest single signal). Note
  its colors, shape language (rounded vs sharp, splatter vs clean), and any motif
  (a mascot, an icon, playful punctuation). The logo usually tells you the lane in
  one look, and it often contradicts the default house aesthetic.

- **Instagram** — pull recent posts/reels with
  `gallery-dl --cookies-from-browser chrome` (Firecrawl can't reach instagram.com;
  see the global instagram-scraping note). Read the captions for voice and the
  photos for real art direction and the actual people.

- **Facebook / Google Business Profile** — more photos, reviews, hours, the human
  layer. Google reviews are real, quotable proof.

## 2. Extract the brand DNA (write it down)

Synthesize the audit into a short, concrete brand portrait. Capture:

- **Colors** — their real hex values (from the `branding` extract + logo), which is
  primary, which is the accent/pop. Honor these even if they are louder or
  brighter than the default lane.
- **Type** — their real typeface(s) and feel (geometric sans? serif? rounded?).
- **Shape language** — rounded/pills or sharp/editorial. Preserve brand assets;
  this is the sanctioned override of the global "sharp corners, no pills" default
  when the brand genuinely is rounded.
- **Voice** — quote their actual lines. Note the register (playful, mindful,
  premium, technical). This is what kills invented marketing copy.
- **Founders & people** — real names, the founder's real origin story in their
  words, the actual team. Never invent bios for identifiable people.
- **Personality / core tension** — name the one thing that makes them them. Often
  a *duality* (e.g. loud playful surface over a calm soulful core, or rugged
  product with a warm family business behind it). The best draft expresses that
  tension instead of flattening it.

Save this into the project's `content.md` (facts: team, story, real site/email,
tokens) and `design.md` (how the DNA drives the build).

## 3. Decide the ONE direction fork before building

The audit usually leaves one real judgment call about how to interpret the brand
(e.g. how loud vs how calm, which of two tensions leads). Ask Annabel that single
question (AskUserQuestion) with a recommended option, then build. Do not ask a
pile of questions, and do not silently pick the whole direction yourself on a big
build — this is the decision that defines the draft.

## 4. Build from their tokens, holding the Ship Gate

- Build a standalone draft in their real color/type/shape system. Keep any
  existing draft intact (e.g. `index-<lane>.html`) so directions can be compared.
- Use their real photos (theirs to use on their own redesign) and their real
  words. No stock.
- **Headings are plain noun titles, never sentences** — not even the client's own
  sentence (their sentences go in body, the hero lede, or a clear pull-quote).
  This is a repeated Annabel correction; see the Ship Gate item 1 and the
  no-invented-headings memory.
- Run the full Ship Gate (`projects/websites/design.md`) and verify in a real
  browser at desktop + mobile (Playwright): console clean, 0 broken images, no
  horizontal overflow, mobile nav works.

## 5. Deploy gotchas (Vercel static)

When pushing a pitch link to Vercel:

- **Ship only the used assets.** If a `.vercelignore` excludes heavy source image
  folders, copy the specific images the page actually references into a deployed
  folder and repoint them, so nothing 404s and the deploy stays lean.
- **The page you want at `/` must be the physical `index.html`.** Vercel serves
  index.html ahead of a `"/" -> "/index-foo.html"` rewrite, so rename rather than
  rely on the rewrite. Preserve the old version under another name.
- A `*.vercel.app` URL is fine for the WhatsApp/email pitch; a **custom domain**
  waits until the launch blockers clear (review permission, real prices, current
  contact details, legal/medical claims).

## Why this works

Starting from their identity makes the pitch land differently: you are not selling
the client your taste, you are showing them their own brand done at a higher
craft level. It also removes whole categories of rework (wrong colors, invented
copy, a lane that isn't them) before they happen.
