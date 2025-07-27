# Week 1 Day 2 Exercise XP 


# Exercise 1 

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.


my_fav_numbers = {7, 14, 21}
print("My favorite numbers:", my_fav_numbers)

my_fav_numbers.add(28)
my_fav_numbers.add(35)
print("After adding two numbers:", my_fav_numbers)

my_fav_numbers.remove(35)
print("After removing the last added number (35):", my_fav_numbers)

friend_fav_numbers = {3, 14, 30}
print("Friend's favorite numbers:", friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)

# Exercise 2

my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)

print(new_tuple)


# Exercise 3


basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")

basket.remove("Blueberries")

basket.append("Kiwi")

basket.insert(0, "Apples")

apples_count = basket.count("Apples")
print("Apples appears", apples_count, "times.")

basket.clear()

print("Final basket:", basket)

# Exercise 4

sequence = []

num = 1.5
while num <= 5:
    sequence.append(num)
    num += 0.5

print(sequence)

# Exercise 5

for num in range(1,21):
    print(num)

numbers = list(range(1, 21))

for index in range(len(numbers)):
    if index % 2 == 0:
        print(numbers[index])

# Exercise 6 

my_name = "Aryeh"

while True:
    user_input = input("Enter your name: ")
    
    if user_input == my_name:
        print("That's my name too! Stopping the loop.")
        break
    else:
        print("That's not my name. Try again.")



# Exercise 7 


fav_fruits_input = input("Enter your favorite fruits (separated by spaces): ")

favorite_fruits = fav_fruits_input.split()

chosen_fruit = input("Enter the name of a fruit: ")

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# Exercise 8 

toppings = []
base_price = 10.0
topping_price = 2.5

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * topping_price)

print("\n--- Pizza Order Summary ---")
print("Toppings:", ", ".join(toppings) if toppings else "None")
print(f"Total price: ${total_price:.2f}")


# Exercise 9 

total_cost = 0
num_people = int(input("How many people want to buy a movie ticket? "))
all_ages = []

for i in range(1, num_people + 1):
    age = int(input(f"Enter the age of person {i}: "))
    all_ages.append(age)

    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print(f"\nTotal ticket cost: ${total_cost}")

restricted_attendees = [age for age in all_ages if 16 <= age <= 21]

print("\n--- Restricted Movie Access ---")
if restricted_attendees:
    print("Allowed attendees (ages 16–21):", restricted_attendees)
else:
    print("No one in the group is allowed to watch the restricted movie.")

# Exercise 10

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

print("Sorry, we're out of Pastrami.\n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\n--- Finished Sandwiches ---")
print(finished_sandwiches)
