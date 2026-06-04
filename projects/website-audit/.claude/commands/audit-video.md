# /audit-video — Video Walkthrough + Drive Upload

Step 8 of the pipeline. Produce a script the prospect can be walked through verbally, then upload the recorded video to the prospect's Google Drive folder. The video is the hook — 80% of the selling happens here. Everything else (portal, email) is the follow-up.

**Usage:** `/audit-video <prospect-name>`

Two-phase: Phase A (Claude drafts script) runs immediately. Phase B (upload) runs after Annabel records locally and provides the file path.

## Good Example (Pepper Pong)

Drafted `prospects/pepper-pong/video-script.md` pulling three findings directly from `audit-client.md`: Schools not in nav (Quick Win #5), vocabulary mismatch ("portable paddle sport" vs "mini pickleball" — the Big Opportunity), and no announcement bar (Housekeeping). Structured in 4 beats (open / 3 findings on live site / redesign reveal / close) hitting 60–90 sec. Warm opener ("Hey Tom"), no salesy language, concrete pointer actions for each finding. After recording, uploaded `pepper-pong-walkthrough.mp4` to the Pepper Pong Drive folder (`parentId: 1TlE66LCe2geERbAlbOrmM-oc4yrPJSLu`) via `create_file`, logged `drive_file_id` + `share_url` to `prospects/pepper-pong/video-meta.json`. Annabel clicked share in Drive → sent to Tom.

## Bad Example

Drafted a generic 4-beat template without pulling specifics from the audit — produced a script that could be about any site ("your SEO could be improved, your conversions look like they could be higher"). Or: script was 3 minutes long with 6 findings — prospect bounces at 45 sec. Or: script was read-aloud formal language ("I have prepared for you a comprehensive analysis...") instead of conversational. Or: uploaded the video to the root of Drive instead of the prospect folder — orphaned asset, hard to find later. Or: tried to programmatically share from Claude — the Drive MCP has no share tool, this always fails. Share is a human step.

## Steps

### Phase A — Draft the script (Claude)

1. **Read `prospects/$NAME/audit-client.md`.** Pick **2–3 findings** that meet all three criteria:
   - **Visible on the live site** (can be pointed at with a cursor in 10 sec)
   - **Visible in the redesign mockup** (can be pointed at in the reveal)
   - **Specific enough to be surprising** (not "your SEO is weak" — something like "your Schools page isn't in the nav")

2. **Write the script** at `prospects/$NAME/video-script.md`. Required structure (4 beats, 60–90 sec):
   - **0:00–0:08 Open.** Name + warm hook addressed to the contact by first name. "Hey [name], I'm Annabel — made a quick walk-through of [business]. Three things I found, then I'll show you what a fix could look like."
   - **0:08–0:40 Findings on live site.** Each finding gets ~10 sec. Spoken as a short paragraph, not bullets. Each finding names the problem concretely, points to a specific element, and frames why it matters.
   - **0:40–1:15 Redesign reveal.** Switch tabs to `<prospect>-audit.vercel.app`. Walk through the same 2–3 areas fixed. One sentence per change: what changed, why. Keep the brand intact — never say "totally redesigned." Say "same personality, made discoverable."
   - **1:15–1:30 Close.** Soft CTA. "I pulled this together as a full audit and dashboard too — happy to share if it's useful. Either way, hope this helps."

3. **Include a "Tabs open before recording" checklist** at the top — live site tab + portal tab + incognito if admin UI would be visible.

4. **Include a "Do / Don't" block** near the bottom. Required items: don't read verbatim, don't apologize or hedge, don't go past 1:30, do keep cursor slow. If the script contains any non-English brand, chef, or place name (e.g. Michoacán, Oaxaca, Ji Hye), add a pronunciation guide line to the Do block — cultural specificity is the point, mispronunciation undercuts it.

5. **Include "After recording" instructions** — save as `<name>-walkthrough.mp4`, give Claude the local path, human shares from Drive.

6. **Hand off to Annabel.** Tell her the script is ready at `prospects/$NAME/video-script.md`. Pause — recording is her step.

### Phase B — Capture the Drive upload (Claude, after Annabel records)

**Default path: Annabel uploads via Drive web UI, Claude records the metadata.**

Why manual-upload-default: the Drive MCP `create_file` tool takes base64-encoded content as a single parameter. Even a modestly compressed 90-sec video (~3–10MB) produces a base64 payload (~4–14MB) that either blows tool-call size limits or eats enough context to destabilize the session. MCP upload only works for tiny files (≲1MB). Don't try it first — default to manual.

7. **Get the prospect's Drive folder id.** From the sheet's `drive_folder` column or from Annabel directly. Don't guess.

8. **Tell Annabel to upload manually.** Give her exact steps:
   - Open the prospect's Drive folder (link with folder id)
   - Drag the recorded `.mp4` into the folder
   - When it finishes, right-click the file → **Get link** → paste the URL back to you

9. **Parse the share URL.** It looks like `https://drive.google.com/file/d/<FILE_ID>/view?usp=sharing`. Extract the file id.

10. **Write `prospects/$NAME/video-meta.json`:**
    ```json
    {
      "drive_file_id": "<extracted FILE_ID>",
      "share_url": "https://drive.google.com/file/d/<FILE_ID>/view",
      "drive_folder_id": "<prospect-drive-folder-id>",
      "uploaded_at": "<ISO timestamp>",
      "local_path": "<path Annabel recorded to>",
      "uploaded_as": "<filename Annabel used in Drive>",
      "upload_method": "manual (Drive web UI)",
      "prospect": "<prospect-name>",
      "recipient": "<contact first name>"
    }
    ```

11. **Draft a Share message for Annabel.** The message Drive sends when she clicks Share → adds the recipient → "Notify people." Match the Adam-Matthews-inspired casual tone (see `/audit-outreach` tone reference). 1–2 sentences max:
    - Opens with what she did ("made a walk-through of…")
    - Names the count of findings and references the mockup
    - Gives a casual out / invitation to react ("lmk what you think!")
    - No title, no CTA, no money talk
    - If recipient is family/close contact (Dad, sibling, friend), loosen further — lowercase, playful sign-off. Ask Annabel which tone level she wants if ambiguous.

12. **Report back to Annabel.** Give her:
    - The Drive share URL (now in video-meta.json)
    - 2–3 message options for the Drive Share dialog (let her pick the tone)
    - Reminder: click **Share** on the file → add recipient email → paste the message → **Notify people** ON → Send
    - Reminder: update the master sheet (status → `sent`, paste `share_url` into `video_link`, fill `sent_date`)
    - If the recipient gets the companion email too, run `/audit-outreach` next (skip for family)

### Phase B — Fallback: MCP upload (only for tiny files)

Only use this path if the recorded file is **under ~1MB** (rare — 90-sec video is usually 5–10MB even compressed). Steps:

- Verify file size: `ls -la <path>` → must be ≤ 1MB
- Base64 encode: `base64 -i <path> -o /tmp/upload_b64.txt`
- Call `mcp__claude_ai_Google_Drive__create_file` with `parentId = <folder id>`, `mimeType = 'video/mp4'`, `content = <base64>`, `title = <prospect>-walkthrough.mp4`
- Use the response's file id to write `video-meta.json` as above

If the MCP call fails or stalls, fall back to manual. Don't retry with larger and larger payloads.

## Assumes

- **Expects:**
  - `prospects/$NAME/audit-client.md` from `/audit-analyze` (findings source)
  - `https://<name>-audit.vercel.app` live from `/audit-package` (portal the script references)
  - A Drive folder under `Website-Audits/` for this prospect (Annabel creates manually before Step 8)
  - The master sheet row at `status: audited` or `status: queued`
- **Produces:**
  - `prospects/$NAME/video-script.md` (Phase A)
  - Uploaded video in the prospect's Drive folder + `prospects/$NAME/video-meta.json` (Phase B)
- **Quality bar:**
  - Script hits 60–90 sec when read at natural pace (roughly 150–225 words for the spoken portions)
  - 2–3 findings, all pullable from `audit-client.md`, all visible on both live site and mockup
  - Warm opener using contact's first name — no "Dear [name]" formality
  - Reveal preserves brand ("same personality, made discoverable"), never claims a total overhaul
  - Video uploads to the correct prospect folder on the first try (parentId verified)

## Constraints

- **No programmatic sharing.** Drive MCP has no share/permission-grant tool. Sharing is always a human step (Annabel clicks share). Don't suggest otherwise.
- **No voice clones in v1.** ElevenLabs / synthetic narration deferred — fidelity isn't there for warm pitches. Annabel records herself.
- **Don't attach the video to the outreach email.** The Drive share *is* the outreach. Step 9 (email) is the optional short note that references the Drive share.
- **Never upload without asking for the folder id.** A wrongly-parented file is painful to move and breaks the mental model ("one folder per prospect").

## Known Failure Modes

- **Script too generic** → pulls from audit findings, not from the contact's specific site. Fix: re-read `audit-client.md` and use direct quotes / specific element names.
- **Script too long** → 2+ minutes loses the prospect. Hard cap at 90 sec spoken; trim findings before trimming the reveal.
- **Script too salesy** → apologetic or pitch-y language. Fix: cut every sentence that starts with "I'd love to," "I think you should," "my recommendation is." State what's wrong, show the fix, let the work speak.
- **Uploaded to Drive root** → breaks the one-folder-per-prospect pattern. Always pass `parentId`.
- **Large MP4 causes MCP timeout / context explosion** → don't use MCP for anything over ~1MB. Default to manual upload via Drive web UI. Base64 inflation is ~1.37×, so even a "small" 10MB video becomes a ~14MB tool-call payload that will blow through context before the call completes.
- **Claude tries to call a share tool** → the tool doesn't exist. Stop and hand back to Annabel.
- **Claude burns tokens base64-encoding a large file before realizing it can't pass the content** → check `ls -la <path>` FIRST. Over 1MB = manual path, no encoding attempt.
