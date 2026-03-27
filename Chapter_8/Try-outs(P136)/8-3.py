# Defines a function that accepts two parameters: size and message
def make_shirt(size, message):
    """Summarize the shirt to be fabricated."""
    print(f"\nMaking a {size} shirt with the message: '{message}'")

# Call the function using positional arguments
# 'Large' is assigned to 'size' and 'Code College' to 'message' based on their order
make_shirt('Large', 'Code College')

# Call the function using keyword arguments
# By naming the arguments, the order no longer matters; Python matches them by name
make_shirt(message='1000 Hours to mastery', size='Medium')