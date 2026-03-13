# Create an empty list to store the cube values
cubes = []

# Loop through numbers from 1 to 10
# The range(1, 11) ensures we process every integer from 1 up to 10
for number in range(1, 11):
    # Calculate the cube of the current number (n^3)
    # The '**' operator is Python's exponentiation operator
    cube = number ** 3
    # Use append() to add the result to the end of our list
    cubes.append(cube)

# Loop through our newly populated 'cubes' list and print each value
for cube in cubes:
    print(cube)