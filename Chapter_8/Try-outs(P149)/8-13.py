# The **user_info parameter tells Python to create an empty dictionary 
# called 'user_info' and pack any extra keyword arguments into it.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    # Add the required first and last names to the dictionary 
    # using 'first_name' and 'last_name' as the keys.
    user_info['first_name'] = first
    user_info['last_name'] = last
    
    # Return the completed dictionary to the line where the function was called
    return user_info

# Call the function with two required strings and three 'extra' keyword arguments
# location, field, and likes are packed into the **user_info dictionary automatically
user_profile = build_profile('Stefan', 'Visser', 
                             location='Kuruman', 
                             field='Coding', 
                             likes='Isuzu')

# Use a loop to iterate through the dictionary's key-value pairs
# .items() allows access to both the key (e.g., 'Location') and the value ('Kuruman')
for key, value in user_profile.items():
    print(f'{key.replace("_", " ").title()}: {value}')