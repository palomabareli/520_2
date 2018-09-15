#/usr/bin/python3
import psycopg2

ip, database, user, password = \
    'localhost', 'projeto', 'admin', '4linux'

try:
    con = psycopg2.connect(
        'host={0} dbname={1} user={2} password={3}'.\
            format(ip, database, user, password)
    )

    cursor = con.cursor()    

    #cursor.execute('insert into alunos (nome) values (''kenji'');')
    #con.commit()

    cursor.execute('select * from alunos;')
    #print(cursor.fetchone()) #result in Tupla

    for x in cursor.fetchall():
        print(
            '''
            ID: {i.>10}
            Nome: {i.>10}: int
            '''.format(x[0], x[1])
        )

    cursor.close()
    con.close()

except Exception as ex:
    print('Error: {0}'.format(ex.message))