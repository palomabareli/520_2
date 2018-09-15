#/usr/bin/python3

def persons_args(*args):
    print(args)

def persons_kwargs(**kwargs):
    print(kwargs)

persons_args('Paloma', 'Bareli', 'Ribeiro')    

persons_kwargs(first = 'Paloma', second = 'Bareli', thrist = 'Ribeiro')    