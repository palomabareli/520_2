from pymongo import MongoClient, DESCENDING
import time

try:
    client =  MongoClient()
    db = client['chat']
except Exception as ex:
    print('Error in the aplication: {0}'.format(ex.message))
    exit()


def insert(name, message):
    date = {
        'name': name,
        'message': message,
        'time' : time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.chat.insert(date)

def select():
    last = [x for x in db.chat.find().sort("_id", DESCENDING)]    
    
    while True:
        date = [x for x in db.chat.find().sort("_id", DESCENDING)]    

        if (date != last):
            last = date

            print('[{0}] {1} : {2}'.format(
                date[0]['time'],
                date[0]['name'],
                date[0]['message'],
                ))

        time.sleep(2)