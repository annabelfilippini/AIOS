#!/usr/bin/env python3
"""Re-apply the AIOS "hide local provider from picker" patch to Hermes (VPS).

Hermes' model picker lists the loopback `local` (Ollama) provider as its own
group ("LIBRARY" in the Workspace app). Those entries duplicate the tuned
`local` / `local-fast` aliases, so we drop that provider row from the picker.
providers.local STAYS in config because it supplies the 64k context_length
override the aliases require (removing it breaks `local`/`local-fast`).

The patch edits hermes_cli/inventory.py:build_models_payload and is overwritten
by `hermes update`. Re-run this on the VPS after every update, then restart the
gateway so the running server picks it up:

    python3 /root/.hermes/aios-patches/hide-local-picker.py
    tmux kill-session -t hermes; cd /root/hermes-workspace && \
        tmux new-session -d -s hermes 'pnpm start:all'

Idempotent: safe to run repeatedly. Exits non-zero (without writing) if the
Hermes internals changed and the anchor is no longer found.
"""
import sys

TARGET = "/usr/local/lib/hermes-agent/hermes_cli/inventory.py"
MARK = "AIOS-PATCH hide-local-picker"


def main() -> int:
    try:
        src = open(TARGET).read()
    except OSError as e:
        print("cannot read %s: %s" % (TARGET, e), file=sys.stderr)
        return 1
    if MARK in src:
        print("already patched")
        return 0
    q = chr(34)
    needle = "    return {\n        " + q + "providers" + q + ": rows,"
    if needle not in src:
        print("ANCHOR NOT FOUND in %s — Hermes internals changed; patch NOT "
              "applied. Re-derive the patch by hand." % TARGET, file=sys.stderr)
        return 1
    sq = chr(39)
    inject = (
        "    # " + MARK + ": drop the loopback local provider from the picker.\n"
        "    # providers.local stays in config for the 64k context_length override\n"
        "    # the local/local-fast aliases need. Re-apply after a hermes update.\n"
        "    rows = [r for r in rows if str(r.get(" + sq + "slug" + sq + ")) != "
        + sq + "local" + sq + "]\n"
    )
    open(TARGET, "w").write(src.replace(needle, inject + needle, 1))
    print("patched %s" % TARGET)
    return 0


if __name__ == "__main__":
    sys.exit(main())
