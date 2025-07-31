# Week 1 Day 3 Exercise 

# Exercise 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))

print(result)


# Exercise 2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name.title()} (age {age}): ${price}")
    total_cost += price

print(f"\nTotal ticket cost: ${total_cost}")

# Bonus 

family = {}
add_more = "yes"

# Input loop
while add_more.lower() == "yes":
    name = input("Enter family member's name: ")
    age = int(input(f"Enter {name}'s age: "))
    family[name] = age
    add_more = input("Add another family member? (yes/no): ")

# Ticket pricing
total_cost = 0
print("\n--- Ticket Breakdown ---")

for name, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    
    print(f"{name.title()} (age {age}): ${price}")
    total_cost += price

print(f"\nTotal ticket cost: ${total_cost}")

# Exercise 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Change number of stores to 2
brand["number_stores"] = 2

# Describe Zara’s clients
print("Zara's clients include:", ", ".join(brand["type_of_clothes"]))

# Add country_creation key
brand["country_creation"] = "Spain"

# Check and update international_competitors
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Delete creation_date key
brand.pop("creation_date", None)

# Print last international competitor
print("Last international competitor:", brand["international_competitors"][-1])

# Print major colors in the US
print("Major colors in the US:", brand["major_color"]["US"])

# Print number of keys in dictionary
print("Number of keys in brand dictionary:", len(brand))

# Print all keys
print("All keys in brand dictionary:", list(brand.keys()))

# Bonus

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10_000
}

# Merge dictionaries (Python 3.9+ style)
brand.update(more_on_zara)

# Print final merged result
print("\nFinal merged dictionary:")
print(brand)


# Exercise 4

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

char_to_index = {name: index for index, name in enumerate(users)}
print("Characters to Indices:", char_to_index)

sorted_users = sorted(users)
sorted_char_to_index = {name: index for index, name in enumerate(sorted_users)}
print("Alphabetically Sorted Characters to Indices:", sorted_char_to_index)

