#/usr/bin/python3

archiveNameRead = 'listName.txt'
archiveNameWrite = 'listNameExercise.txt'

with (open(archiveNameRead, 'r')) as archiveRead:    
    nameList = archiveRead.readlines()
    archiveRead.close

with (open(archiveNameWrite, 'w')) as archiveWrite:
    for count,itemList in enumerate(nameList):
        archiveWrite.write(('{0} - '+itemList).format(count+1)) 