def root(number):
    if isinstance(number, int):
        return number ** 0.5
    elif isinstance(number, str):
        if number.isnumeric():
            return int(number) ** 0.5       
    

assert root(8) == 64, 'The root square of {0} is {1}'.\
                    format(8, root(8))    
assert root('5') == 25, 'The root square of {0} is {1}'.\
                    format('5', root('5'))    
assert root(3) == 9, 'The root square of {0} is {1}'.\
                    format(9, root(964))    
