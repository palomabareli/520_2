from unittest import TestCase, main

def root(number):
    if isinstance(number, int):
        return number ** 0.5
    elif isinstance(number, str):
        if number.isnumeric():
            return int(number) ** 0.5   

class Root(TestCase):
    def teste_root(self):
        self.assertEqual(root(64), 8)    
        self.assertEqual(root(25), 5)    
        self.assertEqual(root('abcde'), 1)    


if __name__ == '__main__':
    main()