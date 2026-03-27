# Define the function with default values for both parameters
# size defaults to 'Large' and message defaults to 'I Love Python'
def make_shirt(size='Large', message='I Love Python'):
    """Print a summary of the shirt being ordered."""
    print(f"\nMaking a {size} shirt with the message: '{message}'")

# Call the function with no arguments
# Since nothing is passed, it uses both defaults: 'Large' and 'I Love Python'
make_shirt()

# Call the function with one positional argument
# 'Medium' is assigned to 'size', but 'message' stays as the default 'I Love Python'
make_shirt('Medium')

# Call the function with two positional arguments
# This overrides both defaults with the specific values provided
make_shirt('Small', 'I Love Code College')