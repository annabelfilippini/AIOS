# Client Opportunity Map Workflow

## 1. Classify The Request

Use one of:

- **Greenfield:** no organized AI/client folder exists yet.
- **Audit-existing:** the folder already has AI instructions, skills, scripts,
  data folders, outputs, or automation artifacts.
- **Discovery only:** Annabel wants to understand a client or business before
  proposing anything.
- **Build candidate:** there is likely technical work for Business Partner.

## 2. Audit Before Asking

If the target is a local folder, use the read-only audit script to avoid asking
about things already present.

Look for:

- agent instructions
- skills
- rules or operating docs
- data folders
- generated reports
- raw drop zones
- converted files
- existing audit logs
- scripts or automations

Do not edit the folder during this pass.

## 3. Ask Operator-Shaped Questions

Good questions:

- What do you sell, and how do you make money?
- What do you open every Monday morning?
- What do you copy from one place to another?
- What messages, reports, or documents repeat every week?
- What tool do you pay for but barely use?
- What decisions still require your approval?
- What would save you two hours this week?

Avoid questions like:

- What is the schema?
- What is the payload?
- What is the data format?
- What is the export cadence?

Derive those details from the tools and artifacts later.

## 4. Build The Map

Capture:

- business type
- money path
- tools
- recurring work
- repeated documents or messages
- existing automation
- data sources
- human approval gates
- sensitive boundaries
- top pain points

Use plain English labels. If a technical word is useful, translate it once.

## 5. Identify Opportunities

Sort opportunities into:

- data organization first
- weekly summaries or briefs
- drafting support
- routing or triage
- customer voice or feedback analysis
- CLI/tool connection
- custom integration
- governance or approval gate

Rank by:

- time saved
- money recovered
- risk reduced
- ease of implementation
- trust needed before automation

## 6. Route Specialists

Route to Garry when asking:

- Is this a good offer?
- Is this valuable enough to sell?
- What is the wedge?
- Which opportunity should be first?

Route to Business Partner when asking:

- Can we build this with current tools?
- Which repo or folder matters?
- What CLI/API/tooling is needed?
- What verification would prove it works?

## 7. Produce The Artifact

Default artifact:

`OPPORTUNITY-MAP.md`

Keep it short enough that Annabel can use it on a client call.
