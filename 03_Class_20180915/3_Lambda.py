#/usr/bin/python3

#perfectSquare(x):
print(list(map(lambda y: y ** 2, range(1,11))))

myName = ['Paloma', 'Bareli', 'Ribeiro']
print(list(map(lambda x: x.title()), myName))


'''
map(lambda x: x if condicao:
    pass
else:
    lambda y: y, sequencia)

verdade if condicao else falso    
'''