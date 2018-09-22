from sqlalchemy import select
from core import user_table

#All selects: return a cursor

#select 1 = all
select_01 = select([user_table]) 
print([x for x in select_01.execute()])

#select 2 = where
select_02 = select([user_table]).where(user_table.c.name == 'paloma')
print([x for x in select([user_table]).execute()])