#!/usr/bin/env python3
"""Read recent iMessages from the local Messages database.

Requires Full Disk Access for the terminal/app running this script
(System Settings > Privacy & Security > Full Disk Access), otherwise
chat.db cannot be opened.

Usage:
  ./read.py                      # 20 most recent messages, all chats
  ./read.py --limit 50           # most recent 50
  ./read.py --handle +14155550123  # only this contact (name or handle)
  ./read.py --handle mom --limit 10
"""
import argparse
import json
import os
import sqlite3
import sys

DB = os.path.expanduser("~/Library/Messages/chat.db")
HERE = os.path.dirname(os.path.abspath(__file__))
CONTACTS = os.path.join(HERE, "contacts.json")

# Apple's epoch (2001-01-01) offset from Unix epoch, in seconds.
APPLE_EPOCH = 978307200


def resolve_handle(name_or_handle):
    """Map a friendly name from contacts.json to a handle; pass handles through."""
    if name_or_handle.startswith("+") or "@" in name_or_handle:
        return name_or_handle
    try:
        with open(CONTACTS) as f:
            return json.load(f).get(name_or_handle, name_or_handle)
    except FileNotFoundError:
        return name_or_handle


def decode_attributed_body(blob):
    """Best-effort plain-text extraction from the NSAttributedString blob that
    modern macOS stores in message.attributedBody when message.text is NULL.
    Heuristic — works for typical plain-text messages, not rich content."""
    if not blob:
        return None
    try:
        idx = blob.find(b"NSString")
        if idx == -1:
            return None
        s = blob[idx + len("NSString"):]
        plus = s.find(b"\x2b")  # length marker follows a '+' (0x2b)
        if plus == -1:
            return None
        s = s[plus + 1:]
        n = s[0]
        if n == 0x81:  # 2-byte little-endian length
            n = int.from_bytes(s[1:3], "little")
            text = s[3:3 + n]
        else:
            text = s[1:1 + n]
        return text.decode("utf-8", errors="replace")
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser(description="Read recent iMessages.")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--handle", default=None, help="name (from contacts.json) or raw handle")
    args = ap.parse_args()

    if not os.path.exists(DB):
        print(f"error: {DB} not found", file=sys.stderr)
        sys.exit(1)

    try:
        conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    except sqlite3.OperationalError as e:
        print(f"error: cannot open chat.db ({e}). Grant Full Disk Access to "
              "your terminal in System Settings > Privacy & Security.", file=sys.stderr)
        sys.exit(1)

    conn.row_factory = sqlite3.Row
    where, params = "", []
    if args.handle:
        where = "WHERE handle.id = ?"
        params.append(resolve_handle(args.handle))

    sql = f"""
        SELECT
          datetime(message.date/1000000000 + {APPLE_EPOCH}, 'unixepoch', 'localtime') AS ts,
          message.is_from_me AS from_me,
          handle.id AS handle,
          message.text AS text,
          message.attributedBody AS body
        FROM message
        LEFT JOIN handle ON message.handle_id = handle.ROWID
        {where}
        ORDER BY message.date DESC
        LIMIT ?
    """
    params.append(args.limit)

    try:
        rows = conn.execute(sql, params).fetchall()
    except sqlite3.OperationalError as e:
        print(f"error: query failed ({e})", file=sys.stderr)
        sys.exit(1)

    for r in reversed(rows):  # oldest-first for readability
        text = r["text"] or decode_attributed_body(r["body"]) or "[no text / attachment]"
        who = "me" if r["from_me"] else (r["handle"] or "unknown")
        print(f"[{r['ts']}] {who}: {text}")


if __name__ == "__main__":
    main()
