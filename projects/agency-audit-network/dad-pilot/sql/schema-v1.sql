-- ============================================================
-- AIOS Schema v1
-- Project: agency-audit-network / dad-pilot
-- Date: 2026-05-15
-- Run this in the Supabase SQL editor as a single transaction.
-- ============================================================
--
-- Principles enforced here:
--   1. Default-deny RLS on every table BEFORE any data lands.
--   2. Per-person JWT auth — no shared admin keys in Cowork.
--   3. `service_role` (god-mode) bypasses RLS automatically and lives
--      ONLY in server-side jobs (Render AIOS workers / ingest jobs / vault-sync).
--   4. Pending-by-default for operational calls. Founders approve.
--   5. Visibility scope is a column, not an afterthought.
--   6. Supabase is the operational company brain, not the authoritative
--      source of truth for canon, CRM, finance, HR, or customer records.
--   7. Information hygiene is first-class: low-risk stale operational
--      records may auto-archive; important conflicts are flagged for review.
--
-- After running this:
--   (a) Create Supabase Auth users for Tom and Josh in the dashboard.
--   (b) Fill in the seed data block at the bottom with their auth UUIDs.
--   (c) Run the test queries (section 6) signed in as each role.
-- ============================================================


-- ============================================================
-- 1. ENUMS
-- ============================================================

create type employee_role as enum (
  'founder',                -- Tom, Josh — all companies, approval rights
  'dri_marketing_sales',    -- Erica
  'dri_operations',         -- Peter (when added)
  'viewer'                  -- limited contractors (future)
);

create type call_status as enum (
  'pending',                -- awaiting founder review
  'approved',               -- visible per `visibility` column
  'private',                -- founder-only history, no employee sees it
  'rejected'                -- soft-discarded
);

create type visibility_scope as enum (
  'founder',                -- Tom + Josh only
  'team_marketing',         -- marketing/sales role + founders
  'team_ops',               -- ops role + founders
  'company'                 -- all employees scoped to this company
);

create type sensitivity_level as enum (
  'normal',
  'confidential',
  'private',
  'restricted'
);

create type lint_status as enum (
  'passed',
  'flagged',
  'auto_archived',
  'needs_review',
  'error'
);

create type cleanup_action_type as enum (
  'auto_archive',
  'flag_conflict',
  'propose_canon_update',
  'mark_reviewed',
  'restore'
);

create type canon_candidate_status as enum (
  'proposed',
  'accepted',
  'rejected',
  'deferred'
);


-- ============================================================
-- 2. TABLES
-- ============================================================

-- companies: AIH, CFS, Falcon, FSL
create table companies (
  id           uuid primary key default gen_random_uuid(),
  code         text not null unique,         -- 'aih', 'cfs', 'falcon', 'fsl'
  display_name text not null,
  is_pilot     boolean not null default false,
  created_at   timestamptz not null default now()
);


-- employees: bridges Supabase Auth users to roles and company scope
create table employees (
  id                uuid primary key default gen_random_uuid(),
  auth_user_id      uuid not null unique references auth.users(id) on delete cascade,
  display_name      text not null,
  role              employee_role not null,
  -- For founders: leave null (means "all companies").
  -- For DRIs / viewers: must reference a specific company.
  scoped_company_id uuid references companies(id) on delete restrict,
  created_at        timestamptz not null default now()
);

create index on employees(auth_user_id);
create index on employees(role);


-- canon_docs: synced from Tom's Obsidian vault by the vault-sync worker
create table canon_docs (
  id            uuid primary key default gen_random_uuid(),
  company_id    uuid not null references companies(id) on delete cascade,
  file_path     text not null,               -- 'canon/cfs/_normalized/voice.md'
  content       text not null,
  content_hash  text not null,               -- so worker can skip unchanged files
  visibility    visibility_scope not null,   -- 'company' or 'founder'
  sensitivity   sensitivity_level not null default 'normal',
  source_ref    text,
  last_linted_at timestamptz,
  updated_at    timestamptz not null default now(),
  unique (company_id, file_path)
);

create index on canon_docs(company_id);
create index on canon_docs(visibility);


-- calls: Granola Seat A transcripts ONLY. Seat B never reaches this table.
create table calls (
  id               uuid primary key default gen_random_uuid(),
  company_id       uuid not null references companies(id) on delete restrict,
  granola_call_id  text unique,
  recorded_by      uuid references employees(id) on delete set null,
  recorded_at      timestamptz not null,
  participants     text[] not null default '{}',
  transcript       text not null,
  summary          text,
  status           call_status not null default 'pending',
  visibility       visibility_scope,         -- set when status -> 'approved'
  sensitivity      sensitivity_level not null default 'confidential',
  source_ref       text,
  validation_status lint_status,
  archived_at      timestamptz,
  last_linted_at   timestamptz,
  reviewed_by      uuid references employees(id) on delete set null,
  reviewed_at      timestamptz,
  review_notes     text,
  created_at       timestamptz not null default now()
);

create index on calls(status);
create index on calls(company_id);
create index on calls(recorded_by);


-- drafts: email / LinkedIn / newsletter drafts produced by skills
create table drafts (
  id             uuid primary key default gen_random_uuid(),
  company_id     uuid not null references companies(id) on delete restrict,
  created_by     uuid not null references employees(id) on delete restrict,
  draft_type     text not null,              -- 'email_reply' | 'linkedin_post' | 'newsletter'
  subject        text,
  body           text not null,
  status         text not null default 'draft', -- 'draft' | 'sent' | 'discarded'
  visibility     visibility_scope not null default 'team_marketing',
  sensitivity    sensitivity_level not null default 'normal',
  source_ref     text,
  validation_status lint_status not null default 'needs_review',
  source_call_id uuid references calls(id) on delete set null,
  archived_at    timestamptz,
  last_linted_at timestamptz,
  created_at     timestamptz not null default now()
);

create index on drafts(created_by);
create index on drafts(status);


-- clients: lightweight CRM
create table clients (
  id            uuid primary key default gen_random_uuid(),
  company_id    uuid not null references companies(id) on delete restrict,
  display_name  text not null,
  primary_email text,
  stage         text,
  visibility    visibility_scope not null default 'company',
  sensitivity   sensitivity_level not null default 'normal',
  source_ref    text,
  archived_at   timestamptz,
  last_linted_at timestamptz,
  created_at    timestamptz not null default now()
);

create index on clients(company_id);


-- newsletters: Beehiiv drafts + post-send stats
create table newsletters (
  id                uuid primary key default gen_random_uuid(),
  company_id        uuid not null references companies(id) on delete restrict,
  draft_id          uuid references drafts(id) on delete set null,
  sent_at           timestamptz,
  open_rate         numeric,
  click_rate        numeric,
  unsubscribe_count integer,
  beehiiv_post_id   text unique,
  visibility        visibility_scope not null default 'company',
  sensitivity       sensitivity_level not null default 'normal',
  archived_at       timestamptz,
  last_linted_at    timestamptz,
  created_at        timestamptz not null default now()
);


-- skill_runs: audit log of every skill execution (cost, latency, who ran it)
create table skill_runs (
  id             uuid primary key default gen_random_uuid(),
  run_by         uuid not null references employees(id) on delete restrict,
  skill_name     text not null,
  input_summary  text,
  output_summary text,
  duration_ms    integer,
  cost_cents     integer,
  created_at     timestamptz not null default now()
);

create index on skill_runs(run_by);
create index on skill_runs(skill_name);


-- information_lint_runs: one row per scheduled lint pass
create table information_lint_runs (
  id              uuid primary key default gen_random_uuid(),
  run_by          uuid references employees(id) on delete set null,
  lint_name       text not null,              -- freshness-lint | conflict-lint | access-lint | etc.
  scope           text not null,              -- table/company/connector/workflow scope
  status          lint_status not null,
  checked_count   integer not null default 0,
  flagged_count   integer not null default 0,
  archived_count  integer not null default 0,
  notes           text,
  created_at      timestamptz not null default now()
);

create index on information_lint_runs(lint_name);
create index on information_lint_runs(created_at);


-- stale_items: low-risk stale rows found by freshness lint
create table stale_items (
  id              uuid primary key default gen_random_uuid(),
  company_id      uuid references companies(id) on delete cascade,
  table_name      text not null,
  record_id       uuid not null,
  reason          text not null,
  risk_level      sensitivity_level not null default 'normal',
  status          lint_status not null default 'flagged',
  lint_run_id     uuid references information_lint_runs(id) on delete set null,
  archived_by_run boolean not null default false,
  reviewed_by     uuid references employees(id) on delete set null,
  reviewed_at     timestamptz,
  created_at      timestamptz not null default now()
);

create index on stale_items(company_id);
create index on stale_items(status);
create index on stale_items(table_name, record_id);


-- conflict_flags: contradictions between Supabase, source systems, and vault/canon
create table conflict_flags (
  id              uuid primary key default gen_random_uuid(),
  company_id      uuid references companies(id) on delete cascade,
  conflict_type   text not null,              -- canon_vs_source | source_vs_source | access_scope | etc.
  subject         text not null,
  supabase_value  text,
  source_value    text,
  source_ref      text,
  status          lint_status not null default 'needs_review',
  lint_run_id     uuid references information_lint_runs(id) on delete set null,
  reviewed_by     uuid references employees(id) on delete set null,
  reviewed_at     timestamptz,
  resolution_notes text,
  created_at      timestamptz not null default now()
);

create index on conflict_flags(company_id);
create index on conflict_flags(status);


-- cleanup_actions: audit trail of every archive/restore/review/proposal
create table cleanup_actions (
  id              uuid primary key default gen_random_uuid(),
  company_id      uuid references companies(id) on delete cascade,
  action_type     cleanup_action_type not null,
  table_name      text not null,
  record_id       uuid not null,
  reason          text not null,
  performed_by    uuid references employees(id) on delete set null,
  performed_by_system boolean not null default false,
  lint_run_id     uuid references information_lint_runs(id) on delete set null,
  reversible      boolean not null default true,
  created_at      timestamptz not null default now()
);

create index on cleanup_actions(company_id);
create index on cleanup_actions(action_type);
create index on cleanup_actions(table_name, record_id);


-- canon_update_candidates: proposed only; workers never edit canon directly
create table canon_update_candidates (
  id              uuid primary key default gen_random_uuid(),
  company_id      uuid not null references companies(id) on delete cascade,
  source_table    text,
  source_record_id uuid,
  proposed_path   text,
  proposed_text   text not null,
  evidence_summary text not null,
  status          canon_candidate_status not null default 'proposed',
  proposed_by_run uuid references information_lint_runs(id) on delete set null,
  reviewed_by     uuid references employees(id) on delete set null,
  reviewed_at     timestamptz,
  review_notes    text,
  created_at      timestamptz not null default now()
);

create index on canon_update_candidates(company_id);
create index on canon_update_candidates(status);


-- ============================================================
-- 3. HELPER FUNCTIONS for RLS
-- ============================================================
-- All marked `security definer` + fixed `search_path` so they can read
-- the employees table without triggering RLS recursion.

create or replace function current_employee_role()
returns employee_role
language sql
stable
security definer
set search_path = public
as $$
  select role from employees where auth_user_id = auth.uid() limit 1;
$$;

create or replace function current_employee_id()
returns uuid
language sql
stable
security definer
set search_path = public
as $$
  select id from employees where auth_user_id = auth.uid() limit 1;
$$;

create or replace function current_company_scope()
returns uuid
language sql
stable
security definer
set search_path = public
as $$
  select scoped_company_id from employees where auth_user_id = auth.uid() limit 1;
$$;

-- True if current role is allowed to see rows with given visibility
create or replace function visibility_allowed(v visibility_scope)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select case current_employee_role()
    when 'founder'              then true
    when 'dri_marketing_sales'  then v in ('team_marketing', 'company')
    when 'dri_operations'       then v in ('team_ops', 'company')
    when 'viewer'               then v = 'company'
    else false
  end;
$$;

-- True if current role is allowed to see rows with given sensitivity.
-- `private` and `restricted` are owner/founder-only in v1.
create or replace function sensitivity_allowed(s sensitivity_level)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select case
    when current_employee_role() = 'founder' then true
    when s in ('normal', 'confidential') then true
    else false
  end;
$$;

-- True if current employee can access data for given company
create or replace function company_allowed(c uuid)
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select case current_employee_role()
    when 'founder' then true                          -- founders see all 4 companies
    else current_company_scope() = c                  -- everyone else: scoped to one
  end;
$$;


-- ============================================================
-- 4. ROW LEVEL SECURITY — default deny, then explicit allow
-- ============================================================
-- Enable RLS on every table. With no policies, the default is DENY for
-- all roles except `service_role` (which bypasses RLS — used by workers).

alter table companies   enable row level security;
alter table employees   enable row level security;
alter table canon_docs  enable row level security;
alter table calls       enable row level security;
alter table drafts      enable row level security;
alter table clients     enable row level security;
alter table newsletters enable row level security;
alter table skill_runs  enable row level security;
alter table information_lint_runs enable row level security;
alter table stale_items enable row level security;
alter table conflict_flags enable row level security;
alter table cleanup_actions enable row level security;
alter table canon_update_candidates enable row level security;


-- ---------- companies ----------

create policy companies_read on companies
  for select
  using (company_allowed(id));

create policy companies_write on companies
  for all
  using (current_employee_role() = 'founder')
  with check (current_employee_role() = 'founder');


-- ---------- employees ----------
-- Founders see all employees. Everyone else sees only themselves.

create policy employees_read on employees
  for select
  using (
    current_employee_role() = 'founder'
    or auth_user_id = auth.uid()
  );

create policy employees_write on employees
  for all
  using (current_employee_role() = 'founder')
  with check (current_employee_role() = 'founder');


-- ---------- canon_docs ----------
-- Read: scoped by company + visibility. No human writes — only vault-sync
-- worker (service_role) writes, and service_role bypasses RLS.

create policy canon_docs_read on canon_docs
  for select
  using (
    company_allowed(company_id)
    and visibility_allowed(visibility)
    and sensitivity_allowed(sensitivity)
  );


-- ---------- calls ----------
-- Founders see ALL calls (including pending — that's the review queue).
-- Everyone else: only approved + visibility-allowed.
-- Calls with status='private' are founder-only forever.

create policy calls_read on calls
  for select
  using (
    company_allowed(company_id)
    and (
      current_employee_role() = 'founder'
      or (status = 'approved' and visibility_allowed(visibility) and sensitivity_allowed(sensitivity))
    )
  );

-- Only founders update calls (approve / reject / set visibility).
create policy calls_update on calls
  for update
  using (current_employee_role() = 'founder')
  with check (current_employee_role() = 'founder');

-- Note: INSERT happens via the Render AIOS ingest worker using service_role.
-- No insert policy means no JWT user can insert directly.


-- ---------- drafts ----------
-- Each person sees their own drafts plus drafts at a visibility they're
-- allowed to see. Insert/update restricted to own rows.

create policy drafts_read on drafts
  for select
  using (
    company_allowed(company_id)
    and (
      current_employee_role() = 'founder'
      or created_by = current_employee_id()
      or (visibility_allowed(visibility) and sensitivity_allowed(sensitivity))
    )
  );

create policy drafts_insert_own on drafts
  for insert
  with check (created_by = current_employee_id());

create policy drafts_update_own on drafts
  for update
  using (created_by = current_employee_id())
  with check (created_by = current_employee_id());


-- ---------- clients ----------

create policy clients_read on clients
  for select
  using (
    company_allowed(company_id)
    and visibility_allowed(visibility)
    and sensitivity_allowed(sensitivity)
  );

create policy clients_write on clients
  for all
  using (
    company_allowed(company_id)
    and current_employee_role() in ('founder', 'dri_marketing_sales')
  )
  with check (
    company_allowed(company_id)
    and current_employee_role() in ('founder', 'dri_marketing_sales')
  );


-- ---------- newsletters ----------

create policy newsletters_read on newsletters
  for select
  using (
    company_allowed(company_id)
    and visibility_allowed(visibility)
    and sensitivity_allowed(sensitivity)
  );

create policy newsletters_write on newsletters
  for all
  using (
    company_allowed(company_id)
    and current_employee_role() in ('founder', 'dri_marketing_sales')
  )
  with check (
    company_allowed(company_id)
    and current_employee_role() in ('founder', 'dri_marketing_sales')
  );


-- ---------- skill_runs ----------
-- Founders see all (cost/usage monitoring). Others see only their own runs.

create policy skill_runs_read on skill_runs
  for select
  using (
    current_employee_role() = 'founder'
    or run_by = current_employee_id()
  );

create policy skill_runs_insert_own on skill_runs
  for insert
  with check (run_by = current_employee_id());


-- ---------- information_lint_runs ----------
-- Founders and build-ops/debug users inspect lint health. In v1, this is
-- founder-only for JWT users; service_role workers insert.

create policy information_lint_runs_read on information_lint_runs
  for select
  using (current_employee_role() = 'founder');


-- ---------- stale_items ----------
-- Founders see all stale findings. Employees see only normal/confidential
-- stale findings in their company scope, not private/restricted items.

create policy stale_items_read on stale_items
  for select
  using (
    current_employee_role() = 'founder'
    or (
      company_allowed(company_id)
      and sensitivity_allowed(risk_level)
      and risk_level in ('normal', 'confidential')
    )
  );

create policy stale_items_update_founder on stale_items
  for update
  using (current_employee_role() = 'founder')
  with check (current_employee_role() = 'founder');


-- ---------- conflict_flags ----------
-- Conflicts can imply sensitive business drift, so only founders see them.

create policy conflict_flags_read on conflict_flags
  for select
  using (current_employee_role() = 'founder');

create policy conflict_flags_update_founder on conflict_flags
  for update
  using (current_employee_role() = 'founder')
  with check (current_employee_role() = 'founder');


-- ---------- cleanup_actions ----------
-- Founders see the full cleanup audit trail. Employees do not see cleanup
-- history unless a later UI exposes employee-safe summaries.

create policy cleanup_actions_read on cleanup_actions
  for select
  using (current_employee_role() = 'founder');


-- ---------- canon_update_candidates ----------
-- Proposed only. Workers never write canon directly; founders review.

create policy canon_update_candidates_read on canon_update_candidates
  for select
  using (current_employee_role() = 'founder');

create policy canon_update_candidates_update_founder on canon_update_candidates
  for update
  using (current_employee_role() = 'founder')
  with check (current_employee_role() = 'founder');


-- ============================================================
-- 5. SEED DATA (run AFTER creating Auth users for Tom and Josh)
-- ============================================================
-- Steps:
--   (a) In Supabase Dashboard > Authentication > Users, invite Tom and Josh.
--   (b) Copy their `auth.users.id` UUIDs from the dashboard.
--   (c) Uncomment and run the inserts below with real UUIDs.

-- insert into companies (code, display_name, is_pilot) values
--   ('aih',    'AIH (Holding)', false),
--   ('cfs',    'CFS',           false),
--   ('falcon', 'Falcon',        false),
--   ('fsl',    'FSL',           true);      -- Erica-first pilot

-- insert into employees (auth_user_id, display_name, role) values
--   ('<tom_auth_uuid>',  'Tom',  'founder'),
--   ('<josh_auth_uuid>', 'Josh', 'founder');

-- When Erica is added:
-- insert into employees (auth_user_id, display_name, role, scoped_company_id)
-- values (
--   '<erica_auth_uuid>',
--   'Erica',
--   'dri_marketing_sales',
--   (select id from companies where code = 'fsl')
-- );


-- ============================================================
-- 6. TESTS — run AS EACH ROLE before going live
-- ============================================================
-- Sign in via the Supabase JS client with each user's credentials, then:
--
-- As Erica (dri_marketing_sales scoped to FSL):
--   select count(*) from calls where status = 'pending';
--     -> expected: 0  (even if pending rows exist)
--   select distinct company_id from calls;
--     -> expected: only FSL's company_id
--   select count(*) from canon_docs where visibility = 'founder';
--     -> expected: 0
--   select count(*) from canon_docs where sensitivity in ('private', 'restricted');
--     -> expected: 0
--   select count(*) from employees;
--     -> expected: 1  (herself only)
--
-- As Peter (dri_operations scoped to FSL), after Erica inserts a draft:
--   select count(*) from drafts where created_by = <erica's employee_id>
--                                 and visibility = 'team_marketing';
--     -> expected: 0  (he's not on the marketing team)
--
-- As Tom (founder):
--   select count(*) from calls;          -> expected: all rows
--   select count(*) from canon_docs;     -> expected: all rows
--   select count(*) from employees;      -> expected: all employees
--   select count(*) from information_lint_runs; -> expected: all lint runs
--   select count(*) from cleanup_actions;       -> expected: full cleanup audit
--   update calls set status = 'approved', visibility = 'company'
--     where id = <some_pending_call_id>;
--     -> expected: succeeds
--
-- As anonymous (no JWT, anon key only):
--   select count(*) from calls;          -> expected: 0
--   select count(*) from canon_docs;     -> expected: 0
--     (Default-deny since current_employee_role() returns null and no
--      policy matches.)
--
-- If ANY of these tests fails the expectation, do not load real data.
-- Fix the policy first.
