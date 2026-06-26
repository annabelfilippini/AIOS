# wp-push

Push a self-contained HTML section into a WordPress site over its REST API, so
nobody has to paste HTML or upload images by hand in wp-admin.

Built for the Freeride Tarifa job: take the venue-guide section from the static
build and publish it into the client's WordPress site
(`freeridetarifa.com`, WordPress + WPBakery + WP Rocket).

## What it does and does not do

- **Does:** uploads the images a section references to the site's media
  library, rewrites the image paths to the live URLs, and creates or updates a
  **dedicated WordPress page** holding that section. Draft by default.
- **Does not:** edit existing WPBakery / page-builder pages. Those store their
  layout as shortcodes, and writing into them over the API would wreck the
  layout. wp-push only owns pages it creates (it stamps a hidden marker and
  refuses to overwrite anything else). To put the section inside an existing
  page, that stays a manual paste in wp-admin.

So the integration model is: wp-push publishes a clean page (e.g.
`freeridetarifa.com/tarifa-eat-drink`), and the client adds it to their nav
menu. The page renders inside their theme, so it keeps the site's header,
footer, and branding.

## One precondition: an Application Password from the client

This needs an Administrator (or Editor) account on the client's WordPress, and
an **Application Password** for it. That is not the login password - it is a
separate, revocable token, so the client never shares their real password.

The client (or you, once you have a login) creates one in wp-admin:

> Users -> Profile -> scroll to **Application Passwords** -> name it `wp-push`
> -> Add New. WordPress shows a 24-character value with spaces, e.g.
> `abcd EFGH ijkl MNOP qrst UVWX`. Copy it (it is shown once). Revoke it from
> the same screen any time.

If the site has the REST API or Application Passwords disabled (some security
plugins do this), this approach is blocked and it falls back to a manual paste.
`ping` will tell you.

## Setup

```bash
cd tools/wp-push
python3 -m pip install -r requirements.txt
cp config.example.toml wp-push.toml
# edit wp-push.toml: site_url, username, app_password
```

`wp-push.toml` and the upload manifest are gitignored - they hold a credential
and site-specific state.

## Use

```bash
# 1. confirm the credentials work and the account can edit pages
python3 wp_push.py ping

# 2. dry run - see which images would upload and what page would change,
#    without sending anything
python3 wp_push.py publish \
  --html ../../projects/websites/freeride-tarifa/section-tarifa-guide.html \
  --base-dir ../../projects/websites/freeride-tarifa \
  --slug tarifa-eat-drink --dry-run

# 3. for real, as a DRAFT (safe - not public)
python3 wp_push.py publish \
  --html ../../projects/websites/freeride-tarifa/section-tarifa-guide.html \
  --base-dir ../../projects/websites/freeride-tarifa \
  --slug tarifa-eat-drink

# review the draft via the edit link it prints, then go live:
python3 wp_push.py publish ... --slug tarifa-eat-drink --publish
```

`--base-dir` is the folder the image paths in your HTML are relative to (the
project root, usually). Re-running is safe: already-uploaded images are cached
in `wp-push-manifest.json` and skipped.

### Back up before touching an existing page

```bash
python3 wp_push.py page-get --slug some-existing-page --out backup.html
```

## Notes / gotchas

- **WP Rocket cache.** After you `--publish`, the change may not show until the
  WP Rocket cache is cleared (one click in wp-admin). wp-push reminds you.
- **WPML (multilingual).** The site runs in several languages. wp-push
  publishes one page in one language; translating it is a separate step in
  WPML.
- **Theme styling.** The page renders inside the client's theme. The section
  carries its own inline CSS, but the theme's container width or fonts can
  still nudge it. Check the draft before publishing.
- **The `publish` input** is a standalone HTML section (your markup + inline
  `<style>`), not a whole page. Keep styles scoped/inline so they travel.
