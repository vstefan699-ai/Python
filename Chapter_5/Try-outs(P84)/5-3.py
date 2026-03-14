# --- VERSION 1: THE PASSING TEST ---
# Set the alien color to green
alien_color = 'green'

# Check if the variable matches the string 'green'
# Since 'green' == 'green' is True, the code inside the block runs
if alien_color == 'green':
    print("Congratulations! You just earned 5 points for shooting the green alien!")

##################################################################################
print() # Print a blank line for visual separation

# --- VERSION 2: THE FAILING TEST ---
# Set the variable to a different color
alien_colors = 'red'

# Check if this new variable matches 'green'
# Since 'red' == 'green' is False, Python skips the indented code below
if alien_colors == 'green':
    # This print statement will not be visible in the output
    print("Congratulations! You just earned 5 points for shooting the green alien!")