# Week 1 Day 2 Exercise XP Gold

# Exercise 1

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend (modifies list1)
list1.extend(list2)
print("Concatenated list:", list1)


# Exercise 2

for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)


# Exercise 3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")

if user_name in names:
    print(f"{user_name} found at index {names.index(user_name)}")
else:
    print("Name not found.")


# Exercise 4

n1 = int(input("Input the 1st number: "))
n2 = int(input("Input the 2nd number: "))
n3 = int(input("Input the 3rd number: "))

print("The greatest number is:", max(n1, n2, n3))


# Exercise 5

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")


# Exercise 6

words = []
for i in range(7):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

letter = input("Enter a single character: ")

for word in words:
    if letter in word:
        print(f"'{letter}' found in '{word}' at index {word.index(letter)}")
    else:
        print(f"'{letter}' not found in '{word}'.")


# Exercise 7

numbers = list(range(1, 1_000_001))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))


# Exercise 8

user_input = input("Enter comma-separated numbers: ")
items = user_input.split(',')

print("List:", items)
print("Tuple:", tuple(items))


# Exercise 9

import random

wins = 0
losses = 0

while True:
    user_input = input("Guess a number from 1 to 9 (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    user_guess = int(user_input)
    if user_guess < 1 or user_guess > 9:
        print("Number out of range!")
        continue

    random_number = random.randint(1, 9)
    print(f"The correct number was: {random_number}")

    if user_guess == random_number:
        print("Winner! 🎉")
        wins += 1
    else:
        print("Better luck next time!")
        losses += 1

# Bonus 2: Results summary
print("\nGame Over!")
print(f"Total games won: {wins}")
print(f"Total games lost: {losses}")
