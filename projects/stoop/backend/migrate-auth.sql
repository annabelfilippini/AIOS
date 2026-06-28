-- Auth/ownership migration (Batch 1 of the login refactor).
-- Moves stands off the secret edit_token model onto Supabase Auth (phone) ownership.
-- Idempotent: safe to run more than once.

-- 1. Owner column -> a logged-in seller's auth user. Old seed rows stay owner=null
--    (still visible in the feed, just not editable by anyone — they're demo data).
alter table stands add column if not exists owner uuid references auth.users(id) on delete set null;

-- 2. Expose owner in the public feed so the client can mark "this stand is mine".
--    A uuid is not sensitive; phone is still excluded.
create or replace view public_stands as
  select id, created_at, kind, hood, name, age, title, price, unit,
         dur, loc, bring, description, theme, photo, about, photos, avail, owner
  from stands;
grant select on public_stands to anon, authenticated;

-- 3. Logged-in owners get direct, row-scoped access to the base table.
--    Feed reads still go through the view (no phone); the owner reads their own
--    full row (incl. phone) only to prefill the edit form.
grant select, insert, update, delete on stands to authenticated;

drop policy if exists stands_owner_sel on stands;
drop policy if exists stands_owner_ins on stands;
drop policy if exists stands_owner_upd on stands;
drop policy if exists stands_owner_del on stands;
create policy stands_owner_sel on stands for select to authenticated using (owner = auth.uid());
create policy stands_owner_ins on stands for insert to authenticated with check (owner = auth.uid());
create policy stands_owner_upd on stands for update to authenticated using (owner = auth.uid()) with check (owner = auth.uid());
create policy stands_owner_del on stands for delete to authenticated using (owner = auth.uid());

-- 4. Retire the token-based RPCs; ownership is now enforced by RLS + auth.uid().
--    Buyers still place orders through submit_order (unchanged, anon, security definer).
drop function if exists create_stand(jsonb);
drop function if exists update_stand(uuid, uuid, jsonb);
alter table stands drop column if exists edit_token;
