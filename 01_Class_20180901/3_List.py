#/usr/bin/python3
list1 = ['a', 'b', 'c', 'd'], []

print('Type of list1: ', type(list1))

print('Last element of list1: ', list1[-1])
print('First element of list1: ', list1[0])

list2 = list1

print('list1:', list1)
print('list2:', list2)

#não é permitido alterar!
#list2

list2 = list1[:-1]
print('list1:', list1)
print('list2:', list2)
