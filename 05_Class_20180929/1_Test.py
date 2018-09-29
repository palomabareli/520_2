from unittest import TestCase, main

def isOdd(number):
    response = False

    if isinstance(number, int):
        if (number % 2 != 0):
            response = True
    elif isinstance(number, str):
        if number.isnumeric():
            if (number % 2 != 0):
                response = True
    return False

class Root(TestCase):
    def teste_root(self):
        self.assertEqual(isOdd(10), False)    
        self.assertEqual(isOdd(15), True)    
        self.assertEqual(isOdd('abcde'), False)    


if __name__ == '__main__':
    main()