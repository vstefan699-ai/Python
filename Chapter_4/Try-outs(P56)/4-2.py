# Create a list of animals
animals = ['horse', 'donkey', 'zebra']

# First loop: Simply print each animal name
for animal in animals:
    print(animal)

# Print an empty line for readability
print()

# Second loop: Print a personalized sentence for each animal
# We use an f-string to insert the animal name into the message
for animal in animals:
    print(f'I would like to own a {animal} or 10.')  

# Print another empty line
print()

# Final statement outside the loops (this only runs once)
print('They all look very simular.')