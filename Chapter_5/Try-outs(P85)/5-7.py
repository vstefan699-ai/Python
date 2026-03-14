# Create a list of three favorite fruits
favorite_fruits = ['Pineapple', 'Banana', 'Mango']

# Use the 'in' keyword to check if a specific item exists in the list
# If the expression is True, the code inside the block executes
if 'Pineapple' in favorite_fruits:
    print('I really like Pineapple')

if 'Banana' in favorite_fruits:
    print('I really like Banana')

if 'Mango' in favorite_fruits:
    print('I really like Mango')

# These checks will not trigger because 'strawberries' and 'kiwi' are not in the list
if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")

if 'kiwi' in favorite_fruits:
    print("You really like kiwi!")