# brand_context/

This folder holds your brand-level context that all skills can read:
voice profile, samples, ICP, positioning, design tokens.

It lives at the project root so any skill in any system can find it
by walking up the directory tree.

## Files Typically Here

  voice-profile.md     Tone, vocabulary, formatting rules
  samples.md           Verified writing samples used as templates
  icp.md               Ideal customer profile
  positioning.md       Differentiation and competitive frame
  design-tokens.md     Visual brand tokens (colors, fonts)

## How to Populate

Run `/mkt-brand-voice` in Claude Code. It walks you through a
playbook and writes the files here for you.

Created by @scrapes/skill-systems installer.
