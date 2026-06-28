-- Stoop backend schema. Paste into Supabase → SQL Editor → Run.
-- Two tables, one public view, RLS-by-owner, one order RPC.
-- Identity = Supabase Auth (phone OTP). A seller owns their stands via the
-- `owner` column (= auth.uid()); RLS lets them touch only their own rows.
-- Buyers are account-free: they read the public feed and place orders via submit_order.
-- ponytail: photos stored inline as data-URL text. Move to Supabase Storage if rows get heavy.

-- ---------- tables ----------
create table if not exists stands (
  id          uuid primary key default gen_random_uuid(),
  owner       uuid references auth.users(id) on delete set null,  -- logged-in seller; null = demo seed
  created_at  timestamptz not null default now(),
  kind        text not null default 'service' check (kind in ('service','product')),
  hood        text not null,
  name        text,
  age         text,
  title       text,
  price       text,
  unit        text,
  dur         text,          -- service only
  loc         text,          -- service only
  bring       text,          -- service only
  description text,          -- product only
  phone       text,          -- parent contact; SERVER-SIDE only, excluded from public view
  theme       text default 'pink',
  photo       text,          -- hero image (data URL)
  about       text[]  default '{}',
  photos      text[]  default '{}',   -- product gallery
  avail       jsonb   default '{}'    -- date (YYYY-MM-DD) -> [times]
);

create table if not exists orders (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  stand_id    uuid not null references stands(id) on delete cascade,
  what        text not null,     -- slot label (service) or product title
  kid         text,              -- optional "for <kid>"
  contact     text not null,     -- buyer's phone/email
  note        text
);
create index if not exists orders_stand_idx on orders (stand_id, created_at desc);

-- ---------- public feed view (no phone) ----------
create or replace view public_stands as
  select id, created_at, kind, hood, name, age, title, price, unit,
         dur, loc, bring, description, theme, photo, about, photos, avail, owner
  from stands;
grant select on public_stands to anon, authenticated;

-- ---------- RLS ----------
alter table stands enable row level security;
alter table orders enable row level security;

-- Owners get direct, row-scoped access to the base table (feed reads use the view;
-- the owner reads their own full row only to prefill the edit form).
grant select, insert, update, delete on stands to authenticated;
create policy stands_owner_sel on stands for select to authenticated using (owner = auth.uid());
create policy stands_owner_ins on stands for insert to authenticated with check (owner = auth.uid());
create policy stands_owner_upd on stands for update to authenticated using (owner = auth.uid()) with check (owner = auth.uid());
create policy stands_owner_del on stands for delete to authenticated using (owner = auth.uid());

-- orders: no direct access; anon places one through submit_order below.
revoke all on orders from anon, authenticated;

-- ---------- order RPC (security definer = runs as owner, bypasses RLS) ----------
-- Buyers (anon) place an order without ever reading the stand's phone.
create or replace function submit_order(p_stand uuid, p_what text, p_kid text, p_contact text, p_note text)
returns uuid
language plpgsql security definer set search_path = public as $$
declare new_id uuid;
begin
  insert into orders (stand_id, what, kid, contact, note)
  values (p_stand, p_what, nullif(p_kid,''), p_contact, nullif(p_note,''))
  returning id into new_id;
  return new_id;
end $$;
grant execute on function submit_order(uuid, text, text, text, text) to anon, authenticated;
