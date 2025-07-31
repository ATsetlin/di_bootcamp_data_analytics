# Week 1 Day 3 Dily Challenge 

# Challenge 1

# Step 1: Ask the user for a word
word = input("Enter a word: ")

# Step 2: Initialize an empty dictionary
letter_indices = {}

# Step 3: Loop through each character with its index
for index, char in enumerate(word):
    if char in letter_indices:
        letter_indices[char].append(index)
    else:
        letter_indices[char] = [index]

# Step 4: Print the result
print(letter_indices)

# Challenge 2

# Sample Data (you can change these)
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet = "$300"

# Step 1: Clean wallet value
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# Step 2: Initialize an empty list for affordable items
affordable_items = []

# Step 3: Loop through items and clean prices
for item, price in items_purchase.items():
    # Remove $ and commas from price
    clean_price = int(price.replace("$", "").replace(",", ""))
    
    # Step 4: Check if item can be afforded
    if clean_price <= wallet_amount:
        affordable_items.append(item)

# Step 5: Sort list alphabetically or print "Nothing"
if not affordable_items:
    print("Nothing")
else:
    print(sorted(affordable_items))

