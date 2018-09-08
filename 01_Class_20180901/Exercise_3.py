#/usr/bin/python3

'''

Calcular a soma das diagonais da matriz

[0][1][2]
[3][4][5]
[6][7][8]
'''


lineNumber = 4   #não inclusivo    
columnNumber = 4 #não inclusivo  

#matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrix = [[0, 0, 1, 2], [2, 2, 3, 4], [4, 4, 5, 6], [6, 6, 7, 8]]

sumFisrtDiagonal, sumSecondDiagonal = 0, 0
auxColumn, auxLine = 0, 0

for line in range(lineNumber):
    for column in range(columnNumber):
        print('line = {0}, column = {1}, matrix[{0}][{1}] = {2}'.\
              format(line,column,matrix[line][column]))

for line in range(lineNumber):
    for column in range(columnNumber):
        
        if (line == column):
            sumFisrtDiagonal += int(matrix[line][column])
            #print(matrix[line][column])   
   		
sumSecondDiagonal = sumFisrtDiagonal
		
print('First diagonal: {0}'.format(str(sumFisrtDiagonal)))
print('Second diagonal: {0}'.format(str(sumSecondDiagonal)))