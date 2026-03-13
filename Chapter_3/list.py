# Creating a list of car brands
cars = ['toyota', 'honda', 'ford', 'chevrolet']

# Accessing the first element using index position 0
first_car = cars[0]  

# Using f-string to insert the list item into a sentence
message = f"My first car was a {first_car.title()}."

# Printing the message
print(message)  
######################################################
# Starting with a list of motorcycles
motorcycles = ['honda', 'yamaha', 'suzuki']

# Modifying an element (change 'yamaha' to 'ducati')
motorcycles[1] = 'ducati'
print(f"Modified list: {motorcycles}")

# Adding an element to the end of the list using append()
motorcycles.append('kawasaki')
print(f"List after appending 'kawasaki': {motorcycles}")

# Inserting an element at the beginning of the list using insert()
motorcycles.insert(0, 'harley-davidson')
print(f"List after inserting 'harley-davidson' at the beginning: {motorcycles}")

# Removing an element by index using del
del motorcycles[2]
print(f"List after removing element at index 2: {motorcycles}")

# Using pop() to remove and return the last item
popped_motorcycle = motorcycles.pop()
print(f"List after popping the last element: {motorcycles}")
print(f"Popped motorcycle: {popped_motorcycle}")

# Using pop() to remove an item from a specific position
first_motorcycle = motorcycles.pop(0)
print(f"List after popping the first element: {motorcycles}")
print(f"Popped first motorcycle: {first_motorcycle}")

# Removing an item by value using remove()
motorcycles.remove('ducati')
print(f"List after removing 'ducati': {motorcycles}")

# Attempting to remove an item by value that doesn't exist raises an error
# motorcycles.remove('harley')  # Uncommenting this would raise a ValueError

# Final list
print(f"Final list of motorcycles: {motorcycles}")
