---
name: shopify
display_name: Shopify CLI
binary: shopify
audience:
  - business-partner
runtime:
  - codex
visibility: private
related_skills:
  - small-business-shopify-redesign
safe_commands:
  - shopify theme list
  - shopify theme dev
  - shopify theme check
approval_required:
  - shopify theme push
  - shopify app deploy
---

# Shopify CLI Connection

Use this connection for Annabel's Shopify theme and small-business redesign
workflows.

## Safe Uses

- Inspect available themes.
- Run draft theme development servers.
- Pull or check theme code when working in a known project folder.
- Verify theme issues before presenting owner-facing work.

## Requires Approval

- Pushing theme changes.
- Deploying app changes.
- Touching a live theme or production setting.
- Taking actions that could affect customer data, checkout, orders, products, or
  payments.

## Verification

- Run `scripts/check-installed.sh` before assuming the CLI is available.
- Run `scripts/check-auth.sh` before relying on account-specific commands.

Do not store Shopify tokens, store credentials, partner credentials, or customer
data in this folder.
