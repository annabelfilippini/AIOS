---
date: 2026-06-29
time: 10:45
project: stoop
status: in-progress
next-session: Finish A2P 10DLC Sole Proprietor registration via the **Twilio Console
  Direct SP wizard** (NOT the API — see why below). Annabel was on
  console.twilio.com/.../a2p-10dlc-overview; Twilio was acting up so we paused.
  Path is the guided wizard, fields pre-drafted (below). After she submits the Brand
  she replies to an OTP text on her cell within 24h. Then create the Sole-Proprietor
  Campaign on the existing "Stoop" Messaging Service (this is the only billable step,
  ~$2/mo). I can verify each Console step via the API as she clicks.
---

# Session: Stoop — Twilio A2P Sole-Proprietor registration attempted; API flow is the
wrong tool, Console wizard is the path

Picked up from the 2026-06-28 16:40 checkpoint (Batch 3 phone-OTP login verified). Goal
this session: register A2P 10DLC as a Sole Proprietor so real (non-whitelisted) numbers
can receive codes/texts. Annabel provided Twilio creds and brand info. We did NOT finish:
Twilio started acting up and she chose to pause. **No brand and no campaign exist yet;
no charges incurred.**

## Key finding (the important one): API Sole-Prop flow ≠ direct individual
- I followed Twilio's **ISV** Sole-Proprietor API walkthrough. Every field validated
  (name/email/address/phone all `passed`), but the Starter Customer Profile evaluation
  fails on the `primary_customer_profile` requirement: error 22216 "Primary customer
  profile is null" / 22217 "must be in approved or in-review state."
- Root cause: the ISV API flow assumes an **already-approved Primary *Business* Profile**
  to attach. A single direct account only has the auto-created stub profile (policy
  `RNffcb02a20420c81caf596ffc44f69712`), which doesn't qualify. Building a real Primary
  Business Profile via API requires **EIN + business website + authorized representative**
  (policy `RNdfbf3fae0e1107f8aded0e7cead80bf5`, type `customer_profile_business_information`)
  — exactly the legal-entity paperwork Sole Proprietor is meant to let you skip. So the
  API ISV flow fights itself for someone with no registered entity.
- Twilio's **Direct Sole Proprietor** registration is officially **Console-only** (no
  separate direct-flow API/policy SIDs documented). That is the supported path for
  Annabel's case (single account, no entity).
- Browser can't be driven for her: computer-use browser tier is **read-only** (can't
  type), and Playwright MCP launches a **fresh** browser with no Twilio login/session, so
  "drive her already-logged-in Chrome" / "CLI in with cookies" is not viable (also the
  Console uses CSRF + short-lived session tokens; cookie replay breaks). **Auth was never
  the blocker — her API keys work fine.** The blocker was the profile prerequisite.
- Workflow that DOES work: **she clicks the Console wizard, I verify each step via the
  API** (I can read brand/identity status + failure reasons in plain English).

## Account state (via API, end of session)
- Account `ACc06ecc…` active, Full (not trial). Auth token worked.
- **Brand registrations: 0.** No campaign on MS.
- Customer Profiles: only `BUab9f6dff539dbee63d463601f74cfcf4` ("My first Twilio account",
  twilio-approved, stub policy `RNffcb02…`).
- Trust Products: `BUd133f9b439fd230e2c220d2c7f7924cd` ("My first Twilio account",
  twilio-approved, policy `RN7a97559effdf62d00f4298208492a5ea`) — auto-created when she
  opened the A2P overview page ("account refreshed"). The draft starter/trust objects I
  created during the API attempt were cleaned up by Twilio. **Account is clean.**
- Messaging Service `MGd4166164b95b67e7188bd5ad1260a38b` "Stoop" with number
  +1 720 575 8753 (sid PNf2e66e…) still configured.

## Pre-drafted wizard fields (paste-ready for next session)
Console → Messaging → Regulatory Compliance → A2P 10DLC → Register → **Sole Proprietor**:
- Name **Annabel Filippini** · email **annabelflip1@gmail.com**
- Address **439 N Williams St, Denver, CO 80218, US**
- Mobile (OTP) **+1 303 859 3694** · Brand **Stoop** · Website **stoopmarkets.com**
- Vertical **Retail**
- Campaign use case **Sole Proprietor**
- Description: *Stoop is a hyperlocal neighborhood marketplace. We send one-time login
  verification codes when a user signs in, and transactional notifications to sellers when
  a neighbor reserves an item from their stand. No marketing.*
- Sample 1: `Your Stoop verification code is 123456. It expires in 10 minutes. Reply STOP to opt out.`
- Sample 2: `Stoop: A neighbor reserved an item from your stand. Open stoopmarkets.com to view and respond. Reply STOP to opt out.`
- Opt-in: *Users enter their mobile number in the Stoop web app at stoopmarkets.com to sign
  in or create an account. After entering their number and tapping "Send code," they
  consent to receive a login code and reservation notifications. Transactional only; no
  third-party sharing.*
- Opt-out **STOP** · Help **HELP**
- After Brand submit → **reply to the OTP text within 24h** (only she can do this).

## Scaling answer (asked + answered)
SP daily cap is low-thousands of segments/day — plenty for a Denver pilot (OTP logins +
reservation pings, handful of stands). Upgrade path if Stoop grows: migrate to a
**Standard / Low-Volume Standard brand** (needs an **EIN** → form an LLC or get a sole-prop
EIN); far higher throughput + multiple campaigns; keep the same number + Messaging Service,
just register the new brand/campaign and re-point. SP now is not a dead end.

## Product/architecture thread (explored, not built — Annabel is staying on SMS for now)
She floated dropping Twilio for reliability. Reframe given: separate **auth** (login OTP)
from **notifications** (bought/booked/reminders). Notifications never needed SMS — a
`notifications` table + Supabase realtime (in-app feed, not DMs/chat) covers it, web push
later. Auth could swap SMS→email magic link (Supabase native, no 10DLC). **Honey-stand flow
agreed:** Reserve (no in-app payment) → seller notified in Stoop → seller Confirms / marks
Ready with pickup hours → buyer notified "ready, stand open till X" → pay in person → mark
Picked up. Defer Stripe/payments in v1. **Decision: she's sticking with Twilio/SMS for now**,
so this stays as a backlog idea, not the active plan.

## Open items / next session options
1. **(Primary)** Finish the Console SP wizard (fields above) + reply to OTP, then create the
   campaign on MS "Stoop". I verify via API as she goes.
2. Optionally save the Twilio-flow learning to `projects/stoop/` (offered; a `## Stack`/SMS
   note so next session starts grounded). Not yet saved.
3. Draft objects already cleaned up by Twilio — nothing to delete.

## Context / secrets hygiene
- Twilio Account SID `ACc06ecc13543cab76ca98f7b0dad229a3`; auth token pasted in-session
  only (NOT in repo). **Rotate the auth token** after registration work is done.
- Supabase ref `pdovqkbejorncalnjqzv`; whitelisted test cell +1 303 859 3694 / fixed code
  123456 (valid through 2027) still short-circuits SMS so login stays testable pre-10DLC.
