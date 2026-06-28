-- Stoop backend schema. Paste into Supabase → SQL Editor → Run.
-- Two tables, one public view, three RPCs. The frontend talks to this with the
-- ANON key only — it can read the public feed and call the RPCs, nothing else.
-- ponytail: photos stored inline as data-URL text (matches current frontend).
-- Move to Supabase Storage if rows get heavy; the column type doesn't change.

-- ---------- tables ----------
create table if not exists stands (
  id          uuid primary key default gen_random_uuid(),
  edit_token  uuid not null default gen_random_uuid(),  -- secret; gates edits, never public
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
  description text,          -- product only (was profile.desc)
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

-- ---------- public feed view (no phone, no edit_token) ----------
create or replace view public_stands as
  select id, created_at, kind, hood, name, age, title, price, unit,
         dur, loc, bring, description, theme, photo, about, photos, avail
  from stands;

-- ---------- lock the tables; the anon role only gets the view + the RPCs ----------
alter table stands enable row level security;
alter table orders enable row level security;
-- (no policies created => no direct row access for anon; all writes go through RPCs)

revoke all on stands from anon, authenticated;
revoke all on orders from anon, authenticated;
grant select on public_stands to anon, authenticated;

-- ---------- RPCs (security definer = run as owner, bypass RLS) ----------

-- create a stand; returns its id + the secret edit_token (show once, save as the edit link)
create or replace function create_stand(p jsonb)
returns table (id uuid, edit_token uuid)
language plpgsql security definer set search_path = public as $$
begin
  return query
  insert into stands (kind, hood, name, age, title, price, unit, dur, loc, bring,
                      description, phone, theme, photo, about, photos, avail)
  values (
    coalesce(p->>'kind','service'), p->>'hood', p->>'name', p->>'age', p->>'title',
    p->>'price', p->>'unit', p->>'dur', p->>'loc', p->>'bring', p->>'description',
    p->>'phone', coalesce(p->>'theme','pink'), p->>'photo',
    coalesce((select array_agg(value::text) from jsonb_array_elements_text(p->'about')), '{}'),
    coalesce((select array_agg(value::text) from jsonb_array_elements_text(p->'photos')), '{}'),
    coalesce(p->'avail','{}'::jsonb)
  )
  returning stands.id, stands.edit_token;
end $$;

-- edit a stand; only succeeds if the edit_token matches. returns true on success.
create or replace function update_stand(p_id uuid, p_token uuid, p jsonb)
returns boolean
language plpgsql security definer set search_path = public as $$
declare hit int;
begin
  update stands set
    kind=coalesce(p->>'kind',kind), hood=coalesce(p->>'hood',hood),
    name=p->>'name', age=p->>'age', title=p->>'title', price=p->>'price', unit=p->>'unit',
    dur=p->>'dur', loc=p->>'loc', bring=p->>'bring', description=p->>'description',
    phone=p->>'phone', theme=coalesce(p->>'theme',theme), photo=p->>'photo',
    about=coalesce((select array_agg(value::text) from jsonb_array_elements_text(p->'about')), about),
    photos=coalesce((select array_agg(value::text) from jsonb_array_elements_text(p->'photos')), photos),
    avail=coalesce(p->'avail', avail)
  where id=p_id and edit_token=p_token;
  get diagnostics hit = row_count;
  return hit > 0;
end $$;

-- place an order; returns the order id. SMS send happens in the edge function (Batch C).
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

grant execute on function create_stand(jsonb)               to anon, authenticated;
grant execute on function update_stand(uuid, uuid, jsonb)   to anon, authenticated;
grant execute on function submit_order(uuid, text, text, text, text) to anon, authenticated;
