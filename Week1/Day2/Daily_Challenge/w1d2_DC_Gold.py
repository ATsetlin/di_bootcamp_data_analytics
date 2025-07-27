# Week 1 Day 2 Daily Challeneg Gold 


from datetime import datetime
import calendar

# Ask for the user's birthdate
birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

# Parse the date
try:
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
except ValueError:
    print("Invalid format. Please enter as DD/MM/YYYY.")
    exit()

# Calculate age
today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
last_digit = age % 10

# Check if birth year is a leap year
is_leap = calendar.isleap(birthdate.year)

# Build the candles string
candles = "i" * last_digit if last_digit > 0 else " "

# Build the cake string
cake = f"""
       ___{candles}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

# Print 1 or 2 cakes based on leap year
print("\nYour birthday cake:")
print(cake if not is_leap else cake * 2)
