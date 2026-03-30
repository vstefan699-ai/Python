# 1. INITIALIZATION
# Create an empty list to store names in the computer's memory while the program runs.
guest_list = []
# A "flag" variable to control when the loop should stop.
active = True

print('Welcome to the Digital Guest Book')
print('(Type "quit" when finished)')

# 2. THE DATA COLLECTION LOOP
# This loop will keep running as long as 'active' remains True.
while active:
    # Prompt the user for their name.
    name = input('\nPlease enter your name: ').strip().title()

    # Check if the user wants to stop. 
    # .lower() ensures "Quit", "QUIT", or "quit" all work.
    if name.lower() == 'quit':
        active = False # This flips the flag and will end the loop on the next check.

    else:
        # If they didn't type quit, greet them and add their name to our list.
        print(f'Hello {name}, you have been added to the list!')
        guest_list.append(name)

# 3. FILE WRITING
# Define the name of the file we want to create/write to.
filename = 'guest_book.txt'

# Open the file in 'w' (write) mode.
# Using 'with' ensures the file is saved and closed properly automatically.
with open(filename, 'w') as file_object:
    # Loop through the list we built during the 'while' loop.
    for guest in guest_list:
        # Write each name followed by a newline character (\n).
        # Without \n, all names would be squashed together on one line.
        file_object.write(f"{guest}\n")

print(f"\nSuccess! All names have been saved to {filename}.")