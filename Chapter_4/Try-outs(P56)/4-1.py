# Create a list of different pizza flavors
pizza = ['pepperoni', '3 cheeses', 'something meaty', 'bacon & avo']

# First loop: Simply print each flavor name
# The .title() method capitalizes the first letter of every word
for flavors in pizza:
    print(flavors.title())

# Print an empty line to separate the two sections of output
print()

# Second loop: Print a full sentence for each flavor
# We use an f-string to insert the flavor directly into the message
for flavors in pizza:
    print(f'I love a {flavors} pizza!')

# Print another empty line for better spacing
print()

# Final statement outside the loops
# The \n adds one more line break before the text runs
print("\nI really love pizza! It's the best meal after a long day of coding.")