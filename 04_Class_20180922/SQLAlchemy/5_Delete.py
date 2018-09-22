#/usr/bin/python3
from sqlalchemy import delete
from core import user_table,engine

con = engine.connect()

delete_01 = delete(user_table).where(user_table.c.name=='paloma')

result = con.execute(delete_01)
print(result.rowcount)
