# Initial list of family members
invites = ['Dad', 'Mother', 'Grandma B', 'Grandpa', 'Grandma A', 'Sister']

# Announce the update to the group
print("Great news everyone! I found a bigger dinner table, so more friends are joining us!")

# Replace 'Sister' (at index 5) with 'Uncle A'
invites[5] = 'Uncle A'

# Use insert(0, ...) to add 'Uncle B' to the very beginning of the list
invites.insert(0, 'Uncle B')

# Use insert(5, ...) to add 'Aunt A' into the middle of the list at index 5
# Note: When you insert, everyone after index 5 shifts one spot to the right
invites.insert(5, 'Aunt A')

# Use append(...) to add 'Aunt B' to the very end of the list
invites.append('Aunt B')

# Print a header for the output using \n for a new line to keep it tidy
print("\n--- Final Invitation List ---")

# Start the loop to print each personalized invitation
for name in invites:
    # Use an f-string to inject the current name into the message
    print(f"Hey {name}, join us for a braai at my place!")