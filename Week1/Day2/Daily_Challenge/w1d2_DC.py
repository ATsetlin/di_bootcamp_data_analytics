# Week 1 Day 2 Daily Challenge 

# Challenege 1 

number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = [number * i for i in range(1, length + 1)]

print("Output:", multiples)


# Challenge 2 


user_input = input("Enter a word or phrase: ")

if user_input:
    result = user_input[0]

    for char in user_input[1:]:
        if char != result[-1]:
            result += char
else:
    result = ""

print("Modified string:", result)
