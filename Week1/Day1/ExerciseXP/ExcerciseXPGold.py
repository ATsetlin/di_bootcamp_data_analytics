# Print the following output in one line of code:

# Hello world
# Hello world
# Hello world
# Hello world
# I love python
# I love python
# I love python
# I love python

print(("Hello world\n" * 4 + "I love python\n" * 4).strip())

# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

month = int(input("Enter a month number (1 to 12): "))

if 3 <= month <= 5:
    print("It's Spring!")
elif 6 <= month <= 8:
    print("It's Summer!")
elif 9 <= month <= 11:
    print("It's Autumn!")
elif month == 12 or month == 1 or month == 2:
    print("It's Winter!")
else:
    print("That's not a valid month number. Please enter a number from 1 to 12.")

