# nuuly-cli

A small, **read-only** pull of your own Nuuly **rental history** + **closet**,
normalized to JSON the style-feed taste engine ("The Edit") can consume. Built in
the `reddit-cli` / `skool-pp-cli` mold (see `skills/site-scraper-cli-builder`).

Python 3 + `curl_cffi` (already a project dep — `serve.py` uses it for Aritzia).

## Why it exists / how it reads Nuuly

Nuuly has **no public API** and fronts the site with **DataDome** bot management,
so the cheap paths fail (anonymous fetch + datacenter IPs get a 403 challenge
page). The one path that works is **your own logged-in browser session** (an
authenticated cookie) replayed with a real Chrome TLS fingerprint via
`curl_cffi` — the same fingerprint trick that beats Aritzia's Cloudflare.

- **Rental history** has no clean JSON endpoint. The
  `/rent/account/rental-history` page **server-renders** your past boxes into a
  state blob (`box.recentOrder` + `box.orderHistory`); the CLI extracts and
  flattens it. DataDome occasionally serves a lighter challenge page, so the
  fetch **retries until the real authenticated page comes back**.
- **Closet** uses the clean `GET /api/closet/v2?pageNumber=N` (paginated).
- **Profile** uses `GET /api/profiles/me` (sizes / body type only — no address,
  phone, or payment is read or stored).

Every rental item is something you **actively chose into a box**, so a worn
rental is a *stronger* signal than a passive like. Each item carries the box's
order date, so recency weighting works downstream.

The session cookie lasts until Nuuly expires it. When it stops working
(`doctor` shows a read failure), re-capture it (below).

## One-time setup: capture your session

1. Log into Nuuly in your browser.
2. DevTools (right-click → **Inspect**) → **Network** tab → reload.
3. Click the top `www.nuuly.com/rent` document row → right-click →
   **Copy → Copy as cURL**.
4. Pipe it straight in (keeps the cookie on your machine, never in a chat):

   ```bash
   pbpaste | python3 ~/Documents/AI-OS/tools/nuuly-cli/nuuly-cli auth import -
   ```

5. Validate:

   ```bash
   python3 ~/Documents/AI-OS/tools/nuuly-cli/nuuly-cli doctor
   ```

   `profile_read: ok` + `rental_history_read: ok` + `closet_read: ok` means it
   works.

The cookie is stored in `~/.config/nuuly-cli/session.json` (chmod 600, outside
git) and never printed.

## Commands

```bash
nuuly-cli doctor                    # validate session + read paths
nuuly-cli agent-context             # machine-readable contract (commands, schema)
nuuly-cli auth import [-|file]      # store cookie from a Copy-as-cURL
nuuly-cli auth status               # session freshness

# fetch + normalize rental history + closet -> ~/.local/share/nuuly-cli/data.json
nuuly-cli pull
nuuly-cli pull --out projects/style-feed/data/nuuly.json   # also drop a project copy
nuuly-cli pull --rental-only        # skip the closet
nuuly-cli pull --closet-only        # skip rental history

# dump normalized items (JSON to stdout, meant to be piped)
nuuly-cli export rental             # past rentals only
nuuly-cli export closet             # saved closet only
nuuly-cli export all                # both
```

Global flags: `--json` (machine output), `--agent` (compact JSON).

## Item schema

```jsonc
{
  "id": "94682457",            // styleNumber (stable product id)
  "style_number": "94682457",
  "choice_id": "94682457_010", // style + colour
  "source": "nuuly-rental",    // or nuuly-closet
  "signal": "rented",          // rented (strong) | closet (interest)
  "brand": "Free People",
  "name": "Forevermore Long-Sleeve Top",
  "color": "WHITE",
  "size": "S",
  "msrp": 98,
  "class": "Tops",
  "is_vintage": null,
  "review_score": 85,
  "has_fit_review": false,
  "img": "https://s7d2.scene7.com/is/image/nu/94682457_010_b?wid=800&fmt=jpeg",
  "url": "https://www.nuuly.com/rent/products/forevermore-long-sleeve-top",
  "date": "2026-06-11",        // box order date (rental only) — for recency
  "order_id": "9593b8c1..."
}
```

scene7 images **hotlink fine** (no proxy needed, unlike Aritzia) and are forced
to sized JPEG for vision/colour reads.

## Privacy

Read-only: no renting, returning, reviewing, or account changes. Your cookie and
all pulled data stay local — `session.json` is chmod 600 outside git, and
`projects/style-feed/data/nuuly.json` is gitignored.
