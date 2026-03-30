import json

# 1. FUNCTION: RETRIEVE DATA
def get_stored_user():
    """Attempt to get stored user data from a JSON file."""
    filename = 'user_profile.json'
    try:
        with open(filename) as f:
            user_data = json.load(f)
    except FileNotFoundError:
        # If the file isn't there, return None so the program knows to ask for input
        return None
    else:
        # Return the dictionary containing the user's profile
        return user_data

# 2. FUNCTION: COLLECT NEW DATA
def get_new_user():
    """Prompt for new user info and save it to a JSON file."""
    username = input("What is your name? ").strip().title()
    age = input("How old are you? ").strip()
    # Great context—perfect for tracking specific progress!
    goal = input("What is your fitness goal? ").strip()
    
    user_data = {
        'username': username,
        'age': age,
        'goal': goal
    }
    
    filename = 'user_profile.json'
    with open(filename, 'w') as f:
        json.dump(user_data, f, indent=4) # Added indent for a cleaner file!
    return user_data

# 3. FUNCTION: MAIN LOGIC
def greet_user():
    """Greet the user by name, or create a new profile if they are new."""
    user_data = get_stored_user()
    
    if user_data:
        # Verify if the person running the script is the one in the file
        correct = input(f"Are you {user_data['username']}? (yes/no): ").strip().lower()
        
        if correct == 'yes':
            print(f"\nWelcome back, {user_data['username']}!")
            print(f"I remember your goal is: {user_data['goal']}")
        else:
            # If it's a different person, overwrite the old data with a new profile
            user_data = get_new_user()
            print(f"We'll remember you next time, {user_data['username']}!")
    else:
        # If no file exists at all, get new user data
        user_data = get_new_user()
        print(f"We'll remember you next time, {user_data['username']}!")

# 4. EXECUTION
# This single line kicks off the entire process.
greet_user()