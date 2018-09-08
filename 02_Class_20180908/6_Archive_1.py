#/usr/bin/python3

archiveName = 'listName.txt'

#Type 1
'''
 archive = open(archiveName, 'r')

 print(archive.read())

 archive.close()
'''

#Type 2
'''
with open(archiveName, 'r') as archive:
    #print(archive.read()) #separator = \n
    print(archive.readlines()) #list
    archive.close() 
'''   

#Type 3
'''
with open(archiveName, 'a') as archive:
    #print(archive.read())
    archive.write('\naline')
    archive.write('\nbergamo')
    archive.close() 
'''

#Type 4
listName = ['aline', 'firmino']
with open(archiveName, 'a') as archive:
    #archive.writelines(listName)
    for name in listName:
        archive.write('\n'+name)
