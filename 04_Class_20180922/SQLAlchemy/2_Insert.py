#/usr/bin/python3
from core import user_table, engine

con = engine.connect()
ins = user_table.insert()

new = ins.values(yearsOld= 30, name='paloma', key='tester') 

con.execute(new)

