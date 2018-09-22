#/usr/bin/python3

def sum(x, y):
    return x + y

x = 3
y = 2

assert sum(x,y) == 5, 'The sum of {0} + {1} = {2}'.format(x, y, sum(x,y))    
assert sum(x,y) != 5, 'The sum of {0} + {1} = {2}'.format(x, y, sum(x,y)) 