# --- BLOCK 1: Alien is green ---
alien_color = 'green'

# Check if the color is exactly 'green'
if alien_color == 'green':
    print('You just earned 5 points for shooting the alien')
# If the color is NOT 'green', this branch runs instead
elif alien_color != 'green':
    print('You just earned 10 points')

########################################################################

# --- BLOCK 2: Alien is red ---
alien_colors = 'red'

# Check if the variable matches 'green' (This will be False)
if alien_colors == 'green':
    print('You just earned 5 points for shooting the alien')
# Check if the variable is NOT 'green' (This will be True)
elif alien_colors != 'green':
    print('You just earned 10 points')