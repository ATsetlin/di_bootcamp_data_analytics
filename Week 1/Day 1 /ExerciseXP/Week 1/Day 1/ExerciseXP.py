# Exercise 1
print("Hello World\n" * 4)

# Exercise 2

ex2 = 99 ** 3 * 8 

print(ex2)

#exercise 3

# True, True, False, False, True 

# 5 < 3
# 3 == 3
# 3 == "3"
# # "3" > 3
# "Hello" == "hello"

# Exercise 4

computer_brand = "Really Old Macbook Air"

print("I have a " + computer_brand + " computer")

# Exercise 5

name = "Ari"
age = str(35)
shoe_size = str(45)
info = "Hello, my name is " + name + ". \nI am " + age + ". \nI wear " + shoe_size + " sized shoes."

print(info)

a = 10
b = 5

if a > b:
    print("Hello World")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


my_name = "Aryeh"
user_name = input("What's your name? ")

if user_name.strip().lower() == my_name.lower():
    print("Whoa! We have the same name. Are you my long-lost twin?")
else:
    print(f"{user_name}? That's a nice name... but mine's cooler!")


height = int(input("Enter your height in centimeters: "))

if height > 145:
    print("You're tall enough to ride! Enjoy the thrill!")
else:
    print("Sorry, you need to grow a bit more to ride. Eat your veggies!")

