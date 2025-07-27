students = ['Harry', 'Ron', 'Hermione']

# create a function called welcome() that says 'Name, welcome to 

def welcome():
    for name in students:
        print(f'{name}, welcome to Hogwarts')

welcome()

def get_house():
    for i, name in enumerate(students):
        students[i] = f'{name} - Gryffindor'

get_house()
print(students)