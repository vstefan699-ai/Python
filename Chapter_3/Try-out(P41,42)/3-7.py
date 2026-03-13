# Create the initial list of family members
invites = ['Dad', 'Mother', 'Grandma B', 'Grandpa', 'Grandma A', 'Sister']

# Print a notification about the smaller table size
print("I'm so sorry, everyone! The big table won't arrive in time, so I can only host two guests.")

# Use a 'while' loop to keep removing guests until only 2 are left
# len(invites) checks the current number of items in the list every time the loop repeats
while len(invites) > 2:
    # pop() removes the last person from the list and stores their name in 'removed_guest'
    removed_guest = invites.pop()
    # Print a personalized apology message to the person who was just removed
    print(f"Sorry {removed_guest}, there's just no room at the smaller table.")

# After the loop finishes, print the final confirmed guests
print("\n--- The Final Two ---")
for person in invites:
    # This loop only runs for the names remaining in the 'invites' list
    print(f"{person}, you're still on the list! See you at the braai.")

# Clear the list completely by deleting the remaining two items
# Since 'del' shifts the list, we delete the item at index 0 twice
del invites[0]
del invites[0]

# Print the final state of the list to confirm it is empty []
print("\nFinal list check:", invites)