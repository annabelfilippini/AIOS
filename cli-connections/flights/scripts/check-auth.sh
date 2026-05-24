#!/usr/bin/env bash
set -euo pipefail

# Flightscope needs no login. This reports engine + optional-cookie readiness
# (the price engine dependency, and the optional flightconnections cookie).
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
BIN="$ROOT/tools/flightscope/bin/flightscope"

"$BIN" doctor --json
