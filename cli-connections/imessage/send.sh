#!/usr/bin/env bash
# Outbound iMessage via AppleScript. Resolves a friendly name from
# contacts.json, or accepts a raw handle (+E.164 phone or email).
#
# Usage:
#   ./send.sh mom "Running 10 min late, see you soon!"
#   ./send.sh +14155550123 "Hi"
#
# Requires: macOS Automation permission for the terminal to control Messages
# (granted on first run via a system prompt, or in System Settings >
# Privacy & Security > Automation).

set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
contacts="$here/contacts.json"

if [[ $# -lt 2 ]]; then
  echo "usage: $0 <name-or-handle> <message>" >&2
  exit 64
fi

name_or_handle="$1"
shift
message="$*"

# Resolve a friendly name to a handle via contacts.json. A handle is anything
# that looks like a phone (+digits) or email (@); otherwise treat as a name key.
handle="$name_or_handle"
if [[ "$name_or_handle" != +* && "$name_or_handle" != *@* ]]; then
  if [[ -f "$contacts" ]]; then
    resolved="$(python3 -c "import json,sys; d=json.load(open('$contacts')); print(d.get('$name_or_handle',''))")"
    if [[ -z "$resolved" ]]; then
      echo "error: '$name_or_handle' not found in contacts.json and is not a phone/email handle" >&2
      exit 1
    fi
    handle="$resolved"
  else
    echo "error: contacts.json missing and '$name_or_handle' is not a phone/email handle" >&2
    exit 1
  fi
fi

# Pass handle + message as AppleScript args (no string interpolation = no
# quoting/injection issues).
osascript - "$handle" "$message" <<'APPLESCRIPT'
on run {targetHandle, msgText}
  tell application "Messages"
    set svc to 1st service whose service type = iMessage
    set toBuddy to buddy targetHandle of svc
    send msgText to toBuddy
  end tell
end run
APPLESCRIPT

echo "sent to $handle"
