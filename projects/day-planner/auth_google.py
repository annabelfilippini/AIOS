#!/usr/bin/env python3
"""
One-time Google authorization for The Day.

Reuses your existing Desktop OAuth client (~/.config/gws/client_secret.json) to
get a token covering two things, saved to token.json next to this script:
  • Google Calendar read + write (calendar.events: list, create, delete)
  • Gmail read-only (gmail.readonly) — so the Emails column can show the threads
    you still need to reply to. Read-only: The Day can never send, delete, or
    change your mail; it only reads which messages are unread/starred.

Run once (and again any time the scopes below change — adding Gmail is one such
change, so re-run this after updating):
    python3 auth_google.py
A browser opens — pick your account and click Allow. (If you see "Google hasn't
verified this app", that's expected for your own project: Advanced → Continue.)
Make sure BOTH the "make changes to events" and the "read your email" permissions
stay checked, so deleting/dragging-in to-dos AND the Emails column both work.

serve.py then reads token.json, pulls your calendar + pressing emails live, and
writes your calendar edits back. token.json is gitignored — it stays on this
machine only.
"""
import os, pathlib
from google_auth_oauthlib.flow import InstalledAppFlow

ROOT = pathlib.Path(__file__).resolve().parent
CLIENT_SECRET = os.path.expanduser("~/.config/gws/client_secret.json")
TOKEN = ROOT / "token.json"
# calendar.events = read + create + delete events (no access to settings/ACLs).
# gmail.readonly  = read message metadata/labels/bodies (cannot modify).
# gmail.send      = send mail as you, so you can reply to a thread from The Day.
#                   send-only: it cannot read more than readonly already does,
#                   and cannot delete or change existing mail.
SCOPES = ["https://www.googleapis.com/auth/calendar.events",
          "https://www.googleapis.com/auth/gmail.readonly",
          "https://www.googleapis.com/auth/gmail.send"]


def main():
    if not os.path.exists(CLIENT_SECRET):
        raise SystemExit(f"client secret not found at {CLIENT_SECRET}")
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
    creds = flow.run_local_server(port=0, prompt="consent")
    TOKEN.write_text(creds.to_json())
    print(f"\n  Authorized. Token saved to {TOKEN}")
    print("  Close the browser tab, then reload The Day — your calendar is live.\n")


if __name__ == "__main__":
    main()
