# Import 'sample' to pick multiple unique items from a list without replacement
from random import sample

# The 'pool' contains all possible balls that can be drawn (numbers and letters)
lottery_pool = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']

# This is the specific combination we are hoping to match
my_ticket = ['1', '5', 'a', 'e']

# Initialize variables to store the current draw, count attempts, and control the loop
winning_ticket = []
iterations = 0
active = True

print("Simulation started... pulling tickets.")

# The 'while' loop continues until 'active' is set to False (when we win)
while active:
    iterations += 1
    
    # Randomly select 4 unique items from the pool for this specific draw
    winning_ticket = sample(lottery_pool, 4)
    
    # Compare tickets using set(). Sets ignore the order of items, so 
    # ['1', 'a'] will match ['a', '1']. This is how real lotteries work!
    if set(winning_ticket) == set(my_ticket):
        active = False  # Exit the loop because we found a match
    
    # Safety break: stop the script if it runs over 1 million times to prevent infinite loops
    if iterations > 1_000_000:
        print("Giving up! Too many tries.")
        break

# Final report showing the winning draw and how many attempts were made
print(f"\n--- RESULTS ---")
print(f"Your ticket: {my_ticket}")
print(f"Last draw:   {winning_ticket}")
print(f"It took {iterations} iterations to win!")