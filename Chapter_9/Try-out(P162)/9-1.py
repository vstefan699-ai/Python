# A Class is a blueprint. By convention, class names start with a Capital letter.
class Restaurant:

    # The __init__ method runs automatically when you create a new 'instance'.
    # 'self' refers to the specific object being created (The Braai Master).
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        # These are called 'attributes'—variables that belong to the class.
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # A function inside a class is called a 'method'.
    def describe_restaurant(self):
        """Print the restaurant details."""
        print(f'The name is: {self.restaurant_name.title()}')
        print(f'Their cuisine is: {self.cuisine_type}')

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f'{self.restaurant_name.title()} is now open!')

# Creating an 'instance' (an object) of the Restaurant class.
my_restaurant = Restaurant('The Braai Master', 'South African')

# Accessing attributes directly using 'dot notation'
print(f'Name: {my_restaurant.restaurant_name}')
print(f'Cuisine: {my_restaurant.cuisine_type}')

# Calling methods (actions) that the class can perform
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()