# Args & Kwargs
# ARGS = ARGUMENTS, TUPLES, SETS
# Keyword Arguments = Dictionary


students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    print(args)
    if args:
        for name in args:
            print(f'{name}, welcome!')
    else:
        print('You didn\'t pass a name')       

welcome('Ari', 'David', 'Stef')


def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = 'Ari', email = 'ari@ari.com', age = 35, is_online = True, pets = ['cat', 'dog'])