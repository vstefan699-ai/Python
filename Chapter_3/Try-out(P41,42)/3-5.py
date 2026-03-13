# Create the initial list of family members to invite
invites = ['Dad', 'Mother', 'Grandma', 'Grandpa', 'Grandma', 'Sister']

# Identify the person who can't attend by their position (Index 5 is the last person)
cant_make_it = invites[5]
print(f"Unfortunately, {cant_make_it} can't make it to the braai.")

# Update the list by replacing 'Sister' (at index 5) with 'Uncle'
invites[5] = 'Uncle'

# Loop through the updated 'invites' list one name at a time
for name in invites:
    # Print a personalized message for every person currently in the list
    print(f"Hey {name}, join us for a braai at my place!")