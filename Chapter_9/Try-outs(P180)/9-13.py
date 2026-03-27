from random import randint

# The Die class acts as a blueprint for any multi-sided die
class Die:

    # The __init__ method sets the number of sides. 
    # It defaults to 6 if no number is provided.
    def __init__(self, sides=6):
        """Initialize the number of sides on the die."""
        self.sides = sides

    # This method handles the logic for a random roll
    def roll_die(self):
        """Generate a random number between 1 and the number of sides."""
        # randint(a, b) returns a random integer N such that a <= N <= b
        roll = randint(1, self.sides)
        print(f'Rolling a {self.sides}-sided die... Result: {roll}')

# Create a standard 6-sided die (uses the default value)
six_sided = Die()
print('\n10 Rolls of 6-sided die')
# The underscore (_) is a Python convention for a loop variable 
# that we don't actually need to use inside the loop.
for _ in range(10):
    six_sided.roll_die()

# Create a 10-sided die by passing an argument
ten_sided = Die(sides=10)
print('\n10 Rolls of 10-sided die')
for _ in range(10):
    ten_sided.roll_die()

# Create a 20-sided die
twenty_sided = Die(sides=20)
print('\n10 Rolls of 20-sided die')
for _ in range(10):
    twenty_sided.roll_die()