#Using range() function
for number in range(5):
    print(number)

#Using range() with list()
even_numbers = list(range(0, 11, 2))
print(even_numbers)

#Square Root Example (Squares of Numbers)
squares = []
for number in range(1, 4):
    square = number ** 2
    squares.append(square)
print(squares)

#Using min(), max(), and sum()
numbers = [10, 20, 30, 40, 50]
print("Min:", min(numbers))  
print("Max:", max(numbers))  
print("Sum:", sum(numbers))  

#List Comprehensions
doubled_numbers = [number * 2 for number in range(1, 6)]
print(doubled_numbers)
#####################################################################################
# Original list of fruits
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Slicing a list: Get the first three fruits
sliced_fruits = fruits[:3]

# Looping through a slice: Print each fruit in the slice
print("First three fruits:")
for fruit in sliced_fruits:
    print(fruit)

# Copying a list: Make a copy of the entire list
copied_fruits = fruits[:]

# Modify the original list and show both lists
fruits.append('fig')

print("\nOriginal list after adding a fruit:")
print(fruits)

print("\nCopied list (unchanged):")
print(copied_fruits)
