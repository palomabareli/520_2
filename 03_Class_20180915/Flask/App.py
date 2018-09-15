#/usr/bin/python3

from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Word</h1>'

@app.route('/login')
def login():
    return jsonify({'message':'My firt api REST', 
        'date': datetime.now()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)