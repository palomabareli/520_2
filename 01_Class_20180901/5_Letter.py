#/usr/bin/python3

letters = []

for x in range(97, 123):
    letters.append(chr(x))

while letters:
    print(letters.pop())

print (letters)    

