#/usr/bin/python3

guestList = ['Paloma', 'Julia', 'Kenji']

try:
    guestIdInput = \
        int(input('Enter with the number of guest: '))

except Exception as ex:
    print('Error in the aplication: {0}'.\
        format(ex.message))
else:
    try:
        print('The guest is found, the name is {0}'.\
            format(guestList[guestIdInput]))
    except Exception as ex:
        print('The guest is not found. \
            The list of guest contains {0} people'.\
            format(len(guestList)))