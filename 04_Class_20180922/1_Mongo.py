#/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
from faker import Faker
from datetime import datetime 

try:
    client = MongoClient('127.0.0.1')
    db = client['4linux']

    #insert 1
    # db.aluno.insert({"_id":2, "nome":"aline bergamo",
    #                 "cursos": [{"nome":"Python Fundamentals",
    #                 "carga horaria":40},
    #                 {"nome":"Linux Fundamentals",
    #                 "carga horaria":40}]})  

    #update 1
    # db.aluno.update
    # (
    #     {"_id":1.0}, 
    #     {"$addToSet":
    #         {"instrutores":
    #             {'nome':'Mariana',
    #             'email':'mariana.albano@4linux.com.br'
    #             }
    #         }	
    #     }
    # )

    #update 2
    # db.aluno.update
    # (
    #     {
    #         "_id":2.0, 
    #         "instrutores.nome":"Mariana"
    #     },
    #     {
    #         "$set":
    #         {
    #             "instrutores.$.nome":"Mari"
    #         }
    #     }
    # )    

    #Class Faker
    # fake = Faker('pt-BR')

    # for y in range(2000):
    #     record = {'nome': fake.name()}
    #     db.aluno.insert(record)

    #option 1 = all lines   
    for x in db.aluno.find():
        print(x)    

    #option 2 = one line
    #pprint(db.aluno.find_one())

    #option 3
    #print(x for x in db.aluno.find())

except Exception as ex:
    print('Error: {0}'.format(ex))
    exit()