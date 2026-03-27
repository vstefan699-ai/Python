# The asterisk (*) tells Python to collect an arbitrary number of arguments
# All provided toppings will be stored in a tuple called 'items'
def sandwich(*items):
    """Summarize the sandwich being ordered with any number of toppings."""
    print('\nGive me a sandwich with the following toppings:')
    
    # Since 'items' is a tuple, we can loop through it to print each topping
    for item in items:
        print(f'· {item}')

# Call the function with one argument
# Python packs 'roasted beef' into a tuple with one element
sandwich('roasted beef')

# Call the function with three arguments
# These are packed into a tuple: ('cheese', 'lettuce', 'tomato')
sandwich('cheese', 'lettuce', 'tomato')

# Call the function with another set of three arguments
sandwich('bacon', 'egg', 'hashbrown')