# Create a dictionary to store favorite numbers with names as keys
person = {
    'Jane': 5,
    'John': 9,
    'Donald': 23
}

# The .items() method returns a view of the dictionary's (key, value) pairs
# We loop through these pairs, assigning the name to 'key' and the number to 'value'
for key, value in person.items():
    # Print the name and the corresponding number
    print(f'{key} {value}')