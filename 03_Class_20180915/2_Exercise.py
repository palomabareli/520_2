#/usr/bin/python3

directoryName = '/home/developer/520_2/02_Class_20180908/'
archiveNameRead = 'listName.txt'


def readArchive(archive):
    '''This is method for read the archive'''
    with open(archive, 'r') as arch:
        return arch.readlines().__len__()

def writeArchive(archive, content):
    '''This is method for write the archive'''
    try:
        with open(archive, 'a') as arch:
            return arch.writelines(content)
    except Exception as ex:
        print('Error: {0}'.format(ex.message))

def countLinesArchive(archive):
    '''This is method forto  count the line of archive'''
    return len(readArchive(archive))

readFirst = readArchive(directoryName+archiveNameRead)
print(readFirst)

writeFirst = writeArchive(directoryName+archiveNameRead,\
    {'andrea','kawata'})
print(writeFirst)

countArchive = countLinesArchive(directoryName+archiveNameRead)
print(countArchive)