#/usr/bin/python3
from flask import Flask, jsonify
from datetime import datetime
from pymongo import MongoClient
import psycopg2
from json import dumps, loads
from bson import BSON

app = Flask(__name__)
# mongodb
client = MongoClient()
db = client['4linux']

# postgresql
con = psycopg2.connect(
    'host=127.0.0.1 dbname=aluno user=admin password=4linux')
cur = con.cursor()


@app.route('/postgresql')
def postgres():
    cur.execute("select * from user;")
    date = cur.fetchall()
    lista = []
    for x in date:
        aux = {"_id": x[0], "name": x[1], "yearsOld": x[2]}
        lista.append(aux)

    return jsonify(lista)


@app.route('/mongo')
def index():
    lista = []
    for x in db.user.find():
        lista.append(x)
    return jsonify(lista)


@app.route('/login')
def login():
    return jsonify({'mensagem': 'My first API Rest',
                    'data': datetime.now().strftime(
                        '%d-%b-%Y %H:%M:%S')})

@app.route('/teste')
def teste():
    return jsonify(dumps(loads([x for x in db.user.find()])))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)