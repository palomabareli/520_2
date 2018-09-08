#/usr/bin/python3

nameList = ['paloma', 'bareli', 'ribeiro']

search = input ('Enter your name: ')

for name in nameList:
    if (search.lower().strip() == name):
        print('Found')
        break
else:
    print('Not found')        