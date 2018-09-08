#/usr/bin/python3

try:
    language = input('What is the best language of programation?: ')

    if (language.lower().strip() == 'python'):
        print('The language is the best!!!')
    else:
        raise ValueError('The language is wrong!!!')
except Exception as ex:
    #print('Error in the aplication: {0}'.\
    #    format(ex.message))
    raise