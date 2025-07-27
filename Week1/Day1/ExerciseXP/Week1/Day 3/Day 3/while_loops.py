# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.


ticket_cost = 0
while age != 'done':
    age = int(input('Enter the age of the person or "done" to finish'))
    if age < 3:
        print("this age is FREE")
        pass
    elif age >=3 and age <=12:
        ticket_cost =+ 10
        print("This age is $10")
    else:
        ticket_cost =+15





