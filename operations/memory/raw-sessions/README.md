# Raw Sessions

This folder is for raw or semi-raw session captures that may be useful later but
should not be read at startup.

Use this layer sparingly:

- Store raw captures only when a checkpoint would lose important evidence.
- Do not put secrets, API keys, cookies, private keys, or full auth headers here.
- Promote durable lessons into `checkpoints/` or `refinement-candidates/`.
- Archive or delete raw captures during weekly consolidation.

Recall order stays:

1. Active project docs
2. Startup recall brief
3. Surfaced checkpoints and refinement candidates
4. Raw sessions only on demand
