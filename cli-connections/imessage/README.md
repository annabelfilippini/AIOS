# iMessage Bridge

Two-way local iMessage bridge for the AI-OS. Send messages via AppleScript and
read recent messages from the local Messages database. Everything runs locally
on this Mac — no third-party service, no network.

## Components

- `send.sh` — outbound. Sends an iMessage to a saved name or raw handle.
- `read.py` — inbound. Reads recent messages from `~/Library/Messages/chat.db`.
- `contacts.json` — friendly-name → handle map (e.g. `mom` → phone number).

## One-time setup (two macOS permissions)

These are TCC permissions; they cannot be granted from a script. Grant them to
**the app you launch Claude Code / your terminal from** (Terminal, iTerm, VS
Code, etc.).

1. **Full Disk Access** (needed by `read.py` to open `chat.db`)
   System Settings → Privacy & Security → Full Disk Access → add your terminal
   app → toggle on → fully quit and reopen the terminal.

2. **Automation → Messages** (needed by `send.sh` to control Messages)
   Granted via a prompt the first time `send.sh` runs. If you previously denied
   it: System Settings → Privacy & Security → Automation → your terminal →
   enable **Messages**.

## Usage

```bash
# Send (resolves "mom" via contacts.json, or pass a raw +phone / email)
./send.sh mom "Running 10 min late — see you soon!"
./send.sh +14155550123 "Hi"

# Read recent messages
./read.py                       # 20 most recent, all chats
./read.py --limit 50
./read.py --handle mom --limit 10
```

## Filling in contacts

Edit `contacts.json`. Phone numbers must be `+E.164` (e.g. `+14155550123`).
The `mom` entry ships as a `+1XXXXXXXXXX` placeholder — replace it with the
real number before sending.

## Notes & limitations

- `read.py` decodes message text from `attributedBody` heuristically (modern
  macOS stores text there when `text` is NULL). It handles typical plain-text
  messages; rich content / reactions / attachments show as `[no text / attachment]`.
- `send.sh` uses the classic Messages AppleScript (`buddy` of the iMessage
  service). Apple tightens this across macOS releases — verify with one real
  test send after granting Automation.
- This bridge reads your entire local message history once Full Disk Access is
  granted. Keep `contacts.json` and any exported output private.
