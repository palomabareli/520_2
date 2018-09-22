#/usr/bin/python3
from sqlalchemy import update
from core import user_table,engine

con = engine.connect()

update_01 = update(user_table).where(user_table.c.name=='paloma') #where
update_01 = update_01.values(name='paloma') #set (update)
result = con.execute(update_01)
print(result.rowcount)

update_01 = update(user_table).where(user_table.c.name=='paloma') #where
update_01 = update_01.values(yearsOld=(user_table.c.yearsOld - 1)) #set (update)
result = con.execute(update_01)
print(result.rowcount)
