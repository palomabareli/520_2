#/usr/bin/python3

''' The class Dog '''
class Dog():
    ''' 
        This is method constructor. 
        Parameters:  
        self: the object of Class
        name: The name of Object 
        yearsOld: The years Old of Object 
        race: The race of Object
    '''
    def __init__(self, name, yearsOld, race):
        self.name = name
        self.yearsOld = yearsOld
        self.race = race

    '''
        This is method Bark.
        Parameters:  
        self: the object of Class       
    '''        
    def bark(self):
        print('auau')

    def __str__(self):
        return 'name: {0}, yearsOld: {1}, race: {2}'.format\
            (name, yearsOld, race)  

dog1 = Dog('Bilu', 2, 'Pitbul')
dog2 = Dog('Rex', 2, 'Poodle')

print('The name the dog is {0}'.format(dog1.name))

print('The dog is: ')
dog1.bark()

#print(dog1.__doc__())
print(dog1.__str__())