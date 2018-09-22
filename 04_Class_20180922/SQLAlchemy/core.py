#/usr/bin/python3
from sqlalchemy import (create_engine, MetaData, Column,
                            Table, Integer, 
                            String, DateTime)

from datetime import datetime

engine = create_engine('sqlite:///teste.db', echo = False)
metadata = MetaData(bind=engine)


user_table = Table('user',
                    metadata,
                    Column('id', Integer, primary_key= True),
                    Column('name', String(40), index= True),
                    Column('yearsOld', Integer, nullable= False),
                    Column('key', String),
                    Column('Created in', DateTime, default=datetime.now),
                    Column('Updated in', DateTime, 
                        default=datetime.now, onupdate=datetime.now)
            )

metadata.create_all(engine)