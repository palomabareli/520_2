#/usr/bin/python3

#print('(Enter) with your notes: ')

note1 = input('First note: ')
note2 = input('Second note: ')

try:
    average = (int(note1)+int(note2))/2

    if (average >= 7):
        print('Approved')
    if ((average >= 3) and (average < 7)):    
        print('Recovery')
    else:
        print('Didn''t aprove')
except Exception as ex:
    print(ex.message)


