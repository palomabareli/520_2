#/usr/bin/python3

#from 5_Exercise import Account, Saving


person1 = Account(holder='Paloma', number=123456, balance=3000)

person1.deposit(2000)
person1.drawOut(50)

person1.transfer(1500, \
    Account(holder='Kenji', number=78910, balance=5000))

person2 = Saving(holder='Julia', number=741258, balance=10000)    