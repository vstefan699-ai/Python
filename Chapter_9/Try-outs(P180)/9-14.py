# Import the 'sample' function, which picks multiple unique items from a list
from random import sample

# Define the 'pool' of possible outcomes (a mix of numbers and letters)
lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']

# Use sample(list, k) where k is the number of items to pick
# This ensures that once 'a' is picked, it can't be picked again in the same draw
winning_ticket = sample(lottery, 4)

print("--- THE LOTTERY DRAW ---")

# Display the winning combination stored in the winning_ticket list
print(f"Any ticket matching these 4 numbers/letters wins a prize: {winning_ticket}")