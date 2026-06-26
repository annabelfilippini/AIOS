---
date: 2026-06-19
time: 08:40
project: tools / wp-push  (freeride-tarifa client integration)
status: in-progress
next-session: wp-push CLI is built + locally verified (help, clean config-missing error, image discovery/rewrite on real tarifa.html). NOT yet run against the live site - needs the client's WordPress Application Password (admin login "likely" per Annabel, not in hand). When credentials arrive: drop them in tools/wp-push/wp-push.toml, run `python3 wp_push.py ping`, then a `--dry-run` publish, then a draft publish. Also pending (offered, awaiting Annabel's go): extract the venue-guide section from projects/websites/freeride-tarifa/tarifa.html into a standalone section-tarifa-guide.html so the pipeline is ready to fire. Client must also confirm REST API / Application Passwords aren't blocked by a security plugin.
---

# Session: wp-push CLI built for Freeride WordPress integration

## The question Annabel asked

Client wants Annabel to take pieces of the static Freeride build (the
Eat/Drink/Party venue-guide grid is the obvious portable one) and integrate
them into the client's existing live site freeridetarifa.com. Annabel wanted to
know if it's possible and wanted a CLI/MCP so she does NOT edit code herself
(so she can say no to a client if hand-coding were required).

## Key finding: the two are different stacks

- Annabel's work = hand-coded static HTML/CSS, 5 pages, live as a feedback
  preview at freeride-tarifa.vercel.app (`projects/websites/freeride-tarifa/`).
- Live freeridetarifa.com = **WordPress**, built with **WPBakery Page Builder**,
  plus WPML (multilingual), WP Rocket caching, RocketCDN. Confirmed from the
  site's own generator meta tags via Firecrawl.
- So integration = a translation step into WordPress, not a file copy.
- No WordPress MCP exists in the registry (checked). No Webflow-MCP-like visual
  editor for WP/WPBakery. WordPress DOES have a REST API + Application
  Passwords, which is what the CLI uses.

## Decision (Annabel chose via AskUserQuestion)

Path = **Build the wp-push CLI**. Access = **admin login likely**.

## What was built: tools/wp-push/

- `wp_push.py` - Python 3.11+ CLI, only dep is `requests`. Commands:
  - `ping` - verify creds + page-edit capability
  - `publish --html <section> --base-dir <dir> --slug <slug>` - scans the HTML
    for referenced local images, uploads them to the WP media library (caches
    in wp-push-manifest.json to skip re-uploads), rewrites img/background-image
    paths to the live media URLs, then creates/updates a dedicated page.
    DRAFT by default; `--publish` to go live; `--dry-run`, `--out`,
    `--reupload`, `--force`.
  - `page-get --slug --out` - back up a page's raw content before overwriting.
- `config.example.toml`, `requirements.txt`, `.gitignore` (ignores
  wp-push.toml + manifest - they hold a credential), `README.md`.

## Safety designed in (so Annabel can promise the client)

- Pages publish as DRAFT by default.
- The CLI stamps a hidden marker (`<!-- managed-by:wp-push -->`) into pages it
  creates and REFUSES to overwrite any page lacking that marker unless
  `--force`. So it cannot clobber an existing WPBakery layout.
- It deliberately does NOT surgically edit existing WPBakery pages (shortcode
  soup). Embedding the section INSIDE an existing page is the one path that
  still needs a manual wp-admin paste; the tool owns standalone pages only.
- Integration model: publishes a standalone page (e.g.
  freeridetarifa.com/tarifa-eat-drink) that renders inside the client theme
  (keeps header/footer/branding); client adds it to the nav menu.

## Verified locally (no creds needed)

- `--help` works; `ping` with no config errors cleanly with guidance.
- Unit-tested find_local_images + rewrite_html on real tarifa.html-style markup:
  correctly grabs local agua.jpg / free-your-mind.webp / balneario.jpg
  (incl. a background-image url()), correctly ignores external Google review
  hrefs and the RocketCDN logo. 24 venue images exist in
  projects/websites/freeride-tarifa/assets/web/venues/.

## Open / next

1. Get the client's WordPress Application Password (Users -> Profile ->
   Application Passwords). Confirm REST API not blocked by a security plugin.
2. Extract venue-guide section from tarifa.html -> section-tarifa-guide.html
   (offered, awaiting Annabel's go).
3. First live run: ping -> dry-run -> draft -> review -> publish.
4. Post-publish manual steps: clear WP Rocket cache; WPML translation is
   separate.
