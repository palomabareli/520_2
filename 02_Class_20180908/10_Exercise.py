#/usr/bin/python3

archiveNameRead = 'listName.txt'
archiveNameWrite = 'listNameExercise.txt'

def archiveNumerator(archiveName, list):
    with (open(archiveName, 'w')) as archiveWrite:
        for count,itemList in enumerate(list):
            archiveWrite.write(('{0} - '+itemList).format(count+1))

        archiveWrite.close

with (open(archiveNameRead, 'r')) as archiveRead:    
    nameList = archiveRead.readlines()
    archiveRead.close

archiveNumerator(archiveNameWrite, nameList)