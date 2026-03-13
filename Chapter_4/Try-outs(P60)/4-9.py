# A list comprehension to generate the first 10 cubes in one line.
# This replaces the need to initialize an empty list and use a separate append loop.
# [expression for item in iterable]
cubes = [number**3 for number in range(1, 11)]

# Print the resulting list of cubed numbers to the console.
print(cubes)