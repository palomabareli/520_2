#/usr/bin/python3

variable = 10

def scope():
    global variable
    variable = 5
    print(variable)


scope()    
print(variable)