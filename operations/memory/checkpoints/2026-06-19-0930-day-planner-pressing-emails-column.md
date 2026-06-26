---
date: 2026-06-19
time: 09:30
project: day-planner ("The Day" — personal calendar + to-do tab)
status: shipped + verified (visual). The Day is now THREE columns — Pressing emails (left) · Calendar timeline (center) · to-do Inbox (right). Emails are read-only Gmail, filtered to "only what you'd reply to": STARRED always shows; UNREAD shows only if the sender isn't an automated no-reply/receipts/notifications/booking-style robot. Spam/Promotions/Social excluded by Gmail category. Cards match the calendar exactly — Cormorant sender names, Jost subjects/labels, cream cards, mail-icon chip (love-tinted when unread), Unread dot + gold Starred badge, date stamp; clicking a card opens that Gmail thread to reply. Verified at 1320x880: cols 300/730/290, 8 real cards (Dad's flights, apartment, rentals, kitesurf…), fonts correct, no console errors.
next-session: The launchd agent `com.annabel.theday` was ALREADY restarted onto the new serve.py (probe: `/api/emails`→200, 8 snapshot emails, needGmail:True, planner.html 200). So reloading her tab NOW shows the new 3-column layout immediately. LIVE email needs ONE remaining thing from Annabel: `python3 auth_google.py` (keep BOTH "make changes to events" AND "read your email" ticked), then reload — NO agent restart needed, `/api/emails` re-checks the token scopes each cycle and flips to live once the gmail scope is present. Until then she sees the SEED snapshot (data/emails.json, 8 real threads) + the "run auth_google.py" note. NOTE: 8802 is the launchd agent (anaconda python /opt/anaconda3/bin/python3, has google libs), NOT a manual terminal — restart via `launchctl bootout gui/$(id -u)/com.annabel.theday` then `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.annabel.theday.plist`. Filter is intentionally tunable: AUTOMATED_LOCALPARTS + AUTOMATED_DOMAINS lists at top of serve.py — if a junk sender slips in or a real one gets hidden, add/remove a word or domain. Open polish: (a) "Annie Morning Brief" from anniestarostin@gmail.com passes the human filter (personal gmail) though it's an automated brief — add a subject/sender skip if she wants it gone; (b) starred receipts she keeps as reference (flight confirmations, Function Health) will show as "pressing" because she said starred=pressing — revisit if too noisy; (c) no mark-as-read / archive from the page (read-only by design).
build: projects/day-planner/{planner.html, serve.py, auth_google.py, data/emails.json}.
  - auth_google.py: SCOPES now += gmail.readonly (read-only — can't send/modify mail).
  - serve.py: _creds() shared loader; _service() (calendar) + _gmail() (gmail). _has_gmail_scope(). fetch_pressing_emails() → messages.list q="in:inbox category:primary (is:unread OR is:starred)", per-thread dedupe, format=metadata (From/Subject/Date), filter via _looks_automated(email) [_parse_from splits "Name <addr>"]. GET /api/emails → _emails() (live cached 90s, writes data/emails.json fallback, sets needGmail when scope absent). Unit-tested _looks_automated on real senders — all pass.
  - planner.html: .app grid 300px/1fr/290px; new <aside class="mail"> left (icons mail+star added to lib, __I_mail__ token); .rail moved to RIGHT (border-right→border-left). JS: loadEmails()/renderEmails()/fmtMailDate()/esc(), MAIL state, #mailRefresh button, renderAll()+boot() now include emails. Card link → https://mail.google.com/mail/u/0/#all/<threadId>.
  - .claude/launch.json (AI-OS root): added "the-day" (python3 projects/day-planner/serve.py 8803 --no-open, autoPort:false) for preview.
---

# Session: The Day — added a Pressing-emails column (3-column layout)

## Ask
"Combine my emails with the planner on one page: pressing emails I need to
respond to on the left, calendar on the right, no spam, same font/titles as the
calendar." Chose: three columns (emails | calendar | to-dos). Pressing =
unread + starred.

## Key decision (data-driven)
Pulled her real inbox first. A literal unread+starred filter returns ~201
threads dominated by booking.com / KLM / Ryanair / YouTube / no-reply receipts —
NOT reply-worthy. So: STARRED always shows (she flagged it), UNREAD shows only
if the sender passes a human/no-reply test. The genuinely-pressing human threads
(Dad's flights, apartment w/ Sharabi Gil, kitesurf, rental apps) were almost all
already starred — which confirmed her instinct that starred matters most.

## Verify
Preview at 1320x880 against the seed snapshot: 3 cols (300/730/290), 8 real
cards, Cormorant sender + Jost subject confirmed by computed style, unread chip
= #b54b5a, card href opens the right Gmail thread, zero console errors. Live
endpoint + filter unit-tested in Python (all sender cases pass). Live Gmail in
the browser is pending her one-time re-auth (see next-session).
