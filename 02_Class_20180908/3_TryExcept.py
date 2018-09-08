#/usr/bin/python3

from ErrorLog import LogException

try:
    count = int(input('Enter with count of notes: '))

    try:
        for x in range(count):            
            try:
                notes += int(input('{0}º note: '.format(x+1)))
            except ex as Exception:
                x -= 1
                #LogException.LogMessage(ex)
                print('Error in the aplication: {0}'.\
                    format(ex.message))

        average = notes/count        

        if (average >= 7):
            print('Approved')
        if ((average >= 3) and (average < 7)):    
            print('Recovery')
        else:
            print('Didn''t aprove')
    except Exception as ex:
        #LogException.LogMessage(ex)
        print('Error in the aplication: {0}'.\
            format(ex.message))


except ex as Exception:
    #LogException.LogMessage(ex)
    print('Error in the aplication: {0}'.\
        format(ex.message))