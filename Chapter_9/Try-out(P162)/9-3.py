# The Class defines what data a User has and what actions they can take
class User:

    # The constructor method initializes five unique pieces of data for every user
    def __init__(self, first_name, last_name, location, age, hobby):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.hobby = hobby

    # A method to display a formatted summary of the user's data
    def describe_user(self):
        """Display a summary of the user's information."""
        print(f'\nUser Profile: {self.first_name.title()} {self.last_name.title()}, age: {self.age}')
        print(f'Location: {self.location.title()}')
        print(f'Hobby: {self.hobby.title()}')

    # A method to print a personalized greeting
    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f'Hey {self.first_name.title()}. Welcome back to studying.')

# Creating three distinct 'User' instances (objects)
pete = User('Pete', 'Dow', 'Kathu', 22, 'welding')
john = User('John', 'Smurf', 'Upinton', 12, 'ice skating')
bob = User('Bob', 'Jaarsveld', 'Pretoria', 34, 'singing')

# Storing the objects in a list so we can handle them collectively
users = [pete, john, bob]

# The Power Move: Looping through the list of objects
# 'user' is a temporary variable that represents each object one by one
for user in users:
    user.greet_user()      # Calls the greet method for the current user in the loop
    user.describe_user()   # Calls the describe method for the current user