-- Seed the demo stands as real rows so every visitor's feed has content.
-- Idempotent: clears the three demo stands first (matched by a marker in phone),
-- so re-running won't duplicate. ponytail: phone='seed' tags demo rows.
delete from stands where phone = 'seed-demo';

-- Delaney — lacrosse lessons (service), Country Club. Availability = Tue/Thu/Sat
-- over the next 4 weeks, computed at seed time so the calendar isn't empty.
insert into stands (kind, hood, name, age, title, price, unit, dur, loc, bring, phone, theme, photo, about, avail)
values (
  'service','country-club','Delaney','14',$$Delaney's Lacrosse Lessons$$,'$30','lesson','1 hour','Cheesman Park','Bring your own stick',
  'seed-demo','pink','delaney.jpg',
  ARRAY[
    $$Hey!! I'm Delaney, I'm 14 and I go to Kent. I play attack for Concept and I seriously love it so much. I teach all levels, so it doesn't matter if you've literally never held a stick. I just really want to help kids get better and have fun doing it!$$,
    $$I can teach any position too, not just attack, so we can work on whatever you want to get better at. I'm usually at Cheesman Park but if somewhere else is easier for you that totally works. Just bring your own stick and we're good to go!$$
  ],
  coalesce((
    select jsonb_object_agg(to_char(d,'YYYY-MM-DD'),
      case extract(dow from d)
        when 6 then '["9:00 am","10:00 am","11:00 am"]'::jsonb
        else '["4:00 pm","5:00 pm","6:00 pm"]'::jsonb
      end)
    from generate_series(current_date, current_date + 27, interval '1 day') d
    where extract(dow from d) in (2,4,6)
  ), '{}'::jsonb)
);

-- Mateo — backyard honey (product), Country Club.
insert into stands (kind, hood, name, title, price, unit, description, phone, theme, about)
values ('product','country-club','Mateo','Backyard Honey','$7','jar',
  'Raw honey from our backyard hives, bottled by the jar. Local pickup in Country Club.',
  'seed-demo','sun',
  ARRAY[$$Hi I'm Mateo! My family keeps bees in our backyard and I bottle the honey. It's really good on toast.$$]);

-- Priya — friendship bracelets (product), Country Club.
insert into stands (kind, hood, name, title, price, unit, description, phone, theme, about)
values ('product','country-club','Priya','Friendship Bracelets','$4','bracelet',
  'Handmade friendship bracelets, made to order in any colors you want. Local pickup.',
  'seed-demo','purple',
  ARRAY[$$I'm Priya and I make friendship bracelets! Tell me your favorite colors and I'll make one just for you.$$]);

select name, kind, hood, (select count(*) from jsonb_object_keys(avail)) as avail_days
from stands where phone='seed-demo' order by name;
