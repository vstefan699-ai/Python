# ============================================================
# Listing 6.1
# Working with Dictionaries and Lists in Python
# ============================================================


# ------------------------------------------------------------
# A LIST OF DICTIONARIES
# Each dictionary represents a car with its details
# ------------------------------------------------------------

cars = [
    {'make': 'Toyota', 'model': 'Corolla', 'color': 'blue'},   # Car 1
    {'make': 'Honda', 'model': 'Civic', 'color': 'red'},      # Car 2
    {'make': 'Ford', 'model': 'Mustang', 'color': 'black'}    # Car 3
]

# Loop through the list of dictionaries
# Each iteration assigns one dictionary to the variable 'car'
for car in cars:
    # Access values using dictionary keys and print formatted output
    print(f"Car: {car['make']} {car['model']}, Color: {car['color']}")


# ============================================================
# A LIST IN A DICTIONARY
# The dictionary contains a list as one of its values
# ============================================================

garage = {
    'colors': ['blue', 'red', 'black', 'white', 'green'],  # List stored inside a dictionary
    'location': 'San Francisco'                            # String value
}

# Print the garage location
print(f"Garage Location: {garage['location']}")

# Print a heading before listing colors
print("Available Colors for Cars:")

# Loop through the list stored under the 'colors' key
for color in garage['colors']:
    print(f"- {color}")


# ============================================================
# A DICTIONARY IN A DICTIONARY
# Nested dictionaries to store user information
# ============================================================

users = {
    'jdoe': {   # Username as the key
        'first_name': 'John',
        'last_name': 'Doe',
        'location': 'New York'
    },
    'jsmith': { # Another user
        'first_name': 'Jane',
        'last_name': 'Smith',
        'location': 'Los Angeles'
    }
}

# Loop through the outer dictionary
# 'username' holds the key, 'user_info' holds the inner dictionary
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    
    # Combine first and last name from the inner dictionary
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    
    # Retrieve the user's location
    location = user_info['location']
    
    # Display formatted user information
    print(f"Full Name: {full_name}")
    print(f"Location: {location}")
