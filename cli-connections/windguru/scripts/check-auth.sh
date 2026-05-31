#!/usr/bin/env bash
set -euo pipefail

# Windguru needs no login, key, or cookie. This just runs doctor, which reports
# how many catalog spots carry a windguru_id and whether the wind path is ready.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
BIN="$ROOT/tools/flightscope/bin/flightscope"

"$BIN" doctor --json
