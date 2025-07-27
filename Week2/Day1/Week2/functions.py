# Functions

# A function is a reusable block of code that runs when you "call" it

#Syntax

def func_name():
    '''prints a string in the console'''
    print("I am a function")


func_name()

# create a function that prints "Hello there!", then call the function to see the output

def greeting():
    """This function prints a friendly greeting in english."""
    print("Hello there!")

greeting()

# Passing ARGUMENTS to the function 
def greetings_adv(language, name):
    '''prints a greeting to a name, in specified language'''
    if language == 'PT':
        print(f'Ola, {name} tudo bem?"')
    
    elif language == 'ES':
        print(f'Hola {name}, que tal?')

    else:
        print('Unknown language')

greetings_adv('ES', 'Javier')

# Keyword Arguments 
def greetings_adv(language, name):
    '''prints a greeting to a name, in specified language'''
    if language == 'PT':
        print(f'Ola, {name} tudo bem?"')
    
    elif language == 'ES':
        print(f'Hola {name}, que tal?')

    else:
        print('Unknown language')

greetings_adv(name = "Jesus", language = 'ES')

# Default Value Arguments 

def greetings_adv(language = 'EN', name = 'Ari'):
    '''prints a greeting to a name, in specified language'''
    if language == 'PT':
        print(f'Ola, {name} tudo bem?"')
    
    elif language == 'ES':
        print(f'Hola {name}, que tal?')
    
    elif language == 'EN':
        print(f'Hello {name}, how are you?')

    else:
        print('Unknown language')

greetings_adv()



# Returning value from a Function()
def calculation(num1, num2)->int:
    '''sums to input numbers'''
    result = num1 + num2
    return result 

def multiply(calc)-> int:
    '''takes a number and muliplies by 5'''
    result = calc * 5
    return result

calc = (calculation(5, 3))
print(multiply(calc))


def greetings_adv(language = 'EN', name = 'Ari')-> str:
    '''prints a greeting to a name, in specified language'''
    if language == 'PT':
        return(f'Ola, {name} tudo bem?"')
    
    elif language == 'ES':
        return(f'Hola {name}, que tal?')
    
    elif language == 'EN':
        return(f'Hello {name}, how are you?')

    else:
        return('Unknown language')

greetings_adv()

def country_info(country="Naboo")-> str:
    """Prints the capital of the given country. Defaults to Naboo."""
    if country == "Naboo":
        print("The capital of Naboo is Theed.")
    
    elif country == "USA":
        print("The capital of USA is Washington DC.")
    
    elif country == "Israel":
        print("The eternal capital of Israel is Jerusalem.")
    
    else:
        print("Sorry, I don't know the capital of", country)

print(country_info('Israel'))




# Global Scope

age = 25 

def current_age():
    print(age)
    my_age = 35
    my_age += 1

current_age()


def happy_birthday():
    global age 
    age += 1
    print(age)

happy_birthday()