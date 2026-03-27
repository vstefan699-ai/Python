# The 'Blueprint' for any restaurant
class Restaurant:

    # The constructor that assigns unique data to each new instance
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # A method that uses the specific data stored in 'self'
    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f'The name is: {self.restaurant_name.title()}')
        print(f'Their cuisine is: {self.cuisine_type}\n')

    def open_restaurant(self):
        """Indicate the restaurant is open."""
        print(f'{self.restaurant_name.title()} is now open!')

# Creating Instance #1: Stores 'Steers' and 'Fast Food'
take_aways = Restaurant('Steers', 'Fast Food')

# Creating Instance #2: Stores 'Ocean Basket' and 'Seafood'
seafood_supreme = Restaurant('Ocean Basket', 'Seafood')

# Creating Instance #3: Stores 'Panarottis' and 'Italian'
pizza_pasta = Restaurant('Panarottis', 'Italian')

# Calling the same method on three different objects
# Python knows which 'self' to use for each call
take_aways.describe_restaurant()
seafood_supreme.describe_restaurant()
pizza_pasta.describe_restaurant()