import json

filename = 'fav_number.json'

# 1. THE "TRY" BLOCK
# We attempt to perform the most optimistic action: reading existing data.
try:
    with open(filename) as f:
        # If the file exists, we load the data into 'favorite_number'.
        favorite_number = json.load(f)

# 2. THE "EXCEPT" BLOCK
# This code ONLY runs if the 'try' block triggers a FileNotFoundError.
except FileNotFoundError:
    # Since we don't have the number, we ask the user for it.
    favorite_number = input('What is your favorite number? ').strip()

    # Now we save it so the error won't happen next time the script runs.
    with open(filename, 'w') as f:
        json.dump(favorite_number, f) # Save the data!
        print("Thanks, I'll remember your number next time.")

# 3. THE "ELSE" BLOCK
# This code ONLY runs if the 'try' block succeeded (no errors occurred).
else: 
    print(f'I know your favorite number is {favorite_number}.')