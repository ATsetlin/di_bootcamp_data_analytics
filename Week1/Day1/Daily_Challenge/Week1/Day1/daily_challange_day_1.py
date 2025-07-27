import random

# Step 1: Ask for user input
user_string = input("Enter a string exactly 10 characters long: ")

# Step 2: Check the length
if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # Step 3: Print the first and last characters
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])

    # Step 4: Build the string character by character
    print("\nBuilding the string:")
    for i in range(1, len(user_string) + 1):
        print(user_string[:i])

    # Step 5 (Bonus): Jumble the string
    chars = list(user_string)
    random.shuffle(chars)
    jumbled = ''.join(chars)
    print("\nJumbled string:", jumbled)
