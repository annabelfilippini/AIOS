---
date: 2026-06-20
time: 19:58
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: BLOCKED ON ONE DECISION FROM ANNABEL — how to weight a worn Nuuly rental vs a normal feed like. I offered 3 options (rental ~1.5-2x a like + closet = normal like [recommended]; rental = a like; brand/style-signal only); she DISMISSED the question to decide later. Do not build integration until she picks. THEN: integrate Nuuly into the taste engine (build_feed.py). `tools/nuuly-cli` is BUILT + verified (70 rental items, 123 closet items pulling clean to projects/style-feed/data/nuuly.json). Feed nuuly-rental items per chosen weight, nuuly-closet as lighter interest. Also decide how to dedupe Nuuly items against existing store-scraped items (match on brand+name? styleNumber is Nuuly-only), and add a recency lever using the rental `date`. Open: should heavily-rented brands (Free People, Anthropologie, Pilcro, CAARA, AGOLDE, MOTHER) auto-boost in build_feed feedback_adjust, or only inform vision-attribute taste? Also still open from prior: add activewear store (Workout only ~6), undergarments source, email purchase signal via Gmail MCP.
---

# Session: The Edit — "My List" shortlist fix (#2) + Nuuly CLI built

## #2 DONE + verified — "My List" is a real buy shortlist, not all-time likes
Problem: My List dumped all ~292 historical likes (a feed again). Root cause: the
heart did double duty as taste signal AND buy list.
Fix (quickchoose.html): **decoupled the heart from taste.** New local-only buy
list `theedit:cart:v1` (localStorage, NOT pushed to /feedback):
- My List starts EMPTY even though 292 taste-likes still power ranking.
- ♥ on a card = add to buy list (and quietly teaches taste underneath).
- ♥ on a filled card = remove from list; taste signal stays.
- ✕ pass = teaches dislike + removes from list.
- My List: per-item ✕ (cart-only) + new **Clear list** button.
- Card heart-filled state + header count now reflect CART, not state.liked.
Verified in browser (:8801 /quickchoose.html): clean boot liked=292 / cart=0;
add/remove/clear/pass all green; 0 console errors.
NOTE the sandbox/browser clock is a DAY AHEAD (today()=2026-06-21). My test clicks
wrote stray likes to feedback.json; cleaned them out — disk restored to verified
**292 liked / 284 disliked**, no stray keys (the Abercrombie pant re-affirm was
kept, its bumped ts removed).

## Nuuly CLI BUILT + verified — `tools/nuuly-cli/nuuly-cli`
Mirrors reddit-cli / skool-pp-cli pattern. Python3 + curl_cffi.
- **Transport reality:** Nuuly has NO public API and uses **DataDome** bot
  management. Beaten by curl_cffi impersonate=**chrome120** + FULL browser
  headers + her cookie. Minimal-header requests get a 403 challenge; the page
  also intermittently serves a lighter challenge page, so fetch_page **retries
  until the real authenticated page (>1MB, contains styleNumber) returns.**
- **Rental history = SSR state blob, not an API.** `/rent/account/rental-history`
  server-renders past boxes into a double-JSON-encoded `<script>` =
  `state.box.recentOrder` + `state.box.orderHistory` (11 past boxes + current).
  extract_state() decodes twice; parse_rental_history() flattens + dedupes
  (recentOrder repeats orderHistory[0]) → **70 unique rental items, Aug 2025 →
  Jun 2026.** Top brands: Free People 12, Anthropologie 11, Pilcro 7, CAARA 5,
  AGOLDE 5, MOTHER 3, Citizens of Humanity, Reformation.
- **Closet = clean API:** `GET /api/closet/v2?pageNumber=N` (paginated, 123 saved
  items). **Profile:** `GET /api/profiles/me` (sizes/body type only — NO
  address/phone/payment read or stored).
- **Auth:** cookie carries `x_nuuly_auth_token` (JWT, sub=her id, no exp claim).
  Stored ~/.config/nuuly-cli/session.json (chmod 600). Re-capture via
  `pbpaste | nuuly-cli auth import -`.
- **Images:** scene7 (`s7d2.scene7.com/is/image/nu/<style>_<color>_b`) HOTLINK
  fine, no proxy needed (unlike Aritzia). CLI appends `?wid=800&fmt=jpeg`
  (forced jpeg dodges the AVIF-can't-decode issue build_feed hit on Aritzia).
- **Commands:** doctor / agent-context / auth import|status / pull
  [--out PATH --rental-only --closet-only] / export [all|rental|closet].
- **Verified:** `doctor` → profile/rental/closet all ok; `pull --out
  projects/style-feed/data/nuuly.json` → 70 rental + 123 closet + profile
  Annabel. Normalized item has brand/name/color/size/msrp/class/img/url/date/
  signal/order_id.

## Privacy
projects/style-feed/.gitignore added: feedback.json, feedback.bak.json,
nuuly.json, style-overrides.json, style-profile.md all gitignored. Cookie outside
repo. Nothing personal was committed (all data/ files were already untracked).

## Files
- projects/style-feed/quickchoose.html (cart layer)
- tools/nuuly-cli/nuuly-cli + README.md (new)
- projects/style-feed/.gitignore (new)
- projects/style-feed/data/nuuly.json (gitignored pull output)
