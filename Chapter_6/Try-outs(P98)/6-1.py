# Create a dictionary to store details about a person
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'Cape Town'
}

# Use the .items() method to retrieve both the key and the value in each loop iteration
for key, value in person.items():
    # .replace('_', ' ') changes underscores to spaces
    # .title() makes the first letter of each word uppercase
    # This cleans up the key so it displays nicely as a label
    print(f"{key.replace('_', ' ').title()}: {value}")