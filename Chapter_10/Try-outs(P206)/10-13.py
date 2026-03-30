import json

filename = 'user_profile.json'

try:
    # 1. ATTEMPT TO READ
    # Note: We use the default read mode here. 'w' would wipe the file!
    with open(filename) as f:
        # json.load() converts the JSON object back into a Python Dictionary.
        user_data = json.load(f)

except FileNotFoundError:
    # 2. HANDLE NEW USER (File doesn't exist)
    print("I don't know you yet. Let's create your profile.")

    # Collect multiple pieces of data
    username = input('What is your name? ').strip().title()
    age = input('How old are you? ').strip()
    goal = input('What is your current goal in life? ').strip()

    # Create a Dictionary to group this data together
    user_data = {
        'username': username,
        'age': age,
        'goal': goal
    }

    # Save the entire dictionary into the JSON file
    with open(filename, 'w') as f:
        json.dump(user_data, f)

    print('\nProfile saved!')

else:
    # 3. HANDLE RETURNING USER (No error occurred)
    # We access the data using the dictionary keys we defined earlier.
    print(f"\nWelcome back, {user_data['username']}!")
    print(f"Age: {user_data['age']}")
    print(f"Goal: {user_data['goal']}")
    print("\nI remember everything!")