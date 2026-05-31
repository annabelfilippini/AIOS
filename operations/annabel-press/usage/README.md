# Annabel Press Usage Ledger

`events.jsonl` records local, private capability-use events.

This is not automatic runtime telemetry. Agents should log a row only when they
materially use a canonical skill or CLI connection for Annabel's work.

Use:

```bash
operations/annabel-press/scripts/log-capability-use.mjs skill client-opportunity-map --agent annie --note "Mapped a med spa opportunity."
operations/annabel-press/scripts/log-capability-use.mjs cli shopify --agent business-partner --note "Checked draft theme status."
```

Each row is JSONL so it can be appended safely and summarized by Annabel Press.
