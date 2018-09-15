#/usr/bin/python3

''' The class Account '''
class Account():
    ''' 
        This is method constructor. 
        Parameters:  
        self: the object of Class
        holder: The holder of Object 
        number: The number of Object 
        balance: The balance of Object 
    '''
    def __init__(self, holder, number, balance):
        self.holder = holder
        self.number = number
        self.balance = balance

    '''
        This is method drawOut.
        Parameters:  
        self: the object of Class  
        amount: the amount of Object 
        Account: then Class to transfer the other Account    
    '''        
    def drawOut(self, amount, Account):
        self.balance -= amount 
        Account.deposit(amount)

    '''
        This is method deposit.
        Parameters:  
        self: the object of Class 
        amount: the amount of Object           
    '''        
    def deposit(self, amount):
        self.balance += amount 

    '''
        This is method transfer.
        Parameters:  
        self: the object of Class     
        amount: the amount of Object             
    '''        
    def transfer(self, amount):
        self.drawOut(amount, Account)        

    def __str__(self):
        return 'holder: {0}, number: {1}, balance: {2}'.format\
            (holder, number, balance)  

''' The class Saving '''
class Saving(Account):
    '''
        This is method interestIncome.
        Parameters:  
        self: the object of Class 
    '''        
    def interestIncome(self):
        self.balance *= 1.05

    def __init__(self, holder, number, balance):
        super().__init__(holder, number, balance)
        self.balance *= 1.05

    def __str__(self):
        return 'holder: {0}, number: {1}, balance: {2}'.format\
            (holder, number, balance)