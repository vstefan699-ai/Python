# --- SCENARIO 1: Alien is green ---
alien_color = 'green'

# Check color and assign points accordingly
if alien_color == 'green':
    print('You earned 5 points') # Triggered because color is green
elif alien_color == 'yellow':
    print('You earned 10 points')
elif alien_color == 'red':
    print('You earned 15 points')
else:
    print("No points earned for this color.")

##########################################################################

# --- SCENARIO 2: Alien is yellow ---
alien_color = 'yellow'

if alien_color == 'green':
    print('You earned 5 points')
elif alien_color == 'yellow':
    print('You earned 10 points') # Triggered because color is yellow
elif alien_color == 'red':
    print('You earned 15 points')
else:
    print("No points earned for this color.")

###########################################################################

# --- SCENARIO 3: Alien is red ---
alien_color = 'red'

if alien_color == 'green':
    print('You earned 5 points')
elif alien_color == 'yellow':
    print('You earned 10 points')
elif alien_color == 'red':
    print('You earned 15 points') # Triggered because color is red
else:
    print("No points earned for this color.")

############################################################################

# --- SCENARIO 4: Alien is pink (unlisted color) ---
alien_color = 'pink'

if alien_color == 'green':
    print('You earned 5 points')
elif alien_color == 'yellow':
    print('You earned 10 points')
elif alien_color == 'red':
    print('You earned 15 points')
else:
    # Triggered because the color is not in the list of recognized colors
    print("No points earned for this color.")