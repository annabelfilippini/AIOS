#!/usr/bin/env bash
set -euo pipefail

# Resolve repo root from this script's location (cli-connections/windguru/scripts).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
BIN="$ROOT/tools/flightscope/bin/flightscope"

test -x "$BIN" || { echo "flightscope binary not executable at $BIN" >&2; exit 1; }
command -v python3 >/dev/null || { echo "python3 not found" >&2; exit 1; }
"$BIN" --version
