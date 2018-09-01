#/usr/bin/python3

list_number = range(101)

for number in list_number:
    if (number%2==0):
        print('The number {0} is pair'.format(number))
    else:
        print('The number {0} is odd'.format(number))