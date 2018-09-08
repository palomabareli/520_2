#/usr/bin/python3

def sum(x = 2, y = 2):
    ''' The function result in the sum of two values '''
    return (x + y)

a = 21
b = 76  

print('The sum of {0} + {1} = {2}'.\
    format(str(a), str(b), str(sum(x = a, y = b))))