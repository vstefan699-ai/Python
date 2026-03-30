# 1. IMPORT THE MODULE
# We must import 'json' to gain access to functions like dump() and load().
import json

# 2. GET USER INPUT
# .strip() removes any accidental spaces the user might type before or after the number.
number = input('What is your favorite number? ').strip()

# 3. DEFINE THE FILE NAME
# We use the .json extension so other programs (and humans) know what's inside.
filename = 'fav_number.json'

# 4. SAVE DATA USING JSON
# Open the file in 'w' (write) mode.
with open(filename, 'w') as f:
    # json.dump() takes two arguments:
    # 1. The data you want to save (number)
    # 2. The file object where it should be stored (f)
    json.dump(number, f)

print(f"I've memorized that {number} is your favorite.")

###########################################################################
########################### second one ####################################

# 1. IMPORT THE MODULE
# We need the json module again to "decode" the format from the file.
import json

# 2. POINT TO THE FILE
# Make sure this filename matches exactly what you used when saving!
filename = 'fav_number.json'

# 3. OPEN AND LOAD THE DATA
# Note: When we don't specify 'w' or 'a', Python defaults to 'r' (read mode).
with open(filename) as f:
    # json.load(f) reads the string from the file and converts it back
    # into a Python-friendly format (string, int, list, etc.).
    favorite_number = json.load(f)

# 4. USE THE DATA
# Now that 'favorite_number' is a variable in our script, we can print it.
print(f"I know your favorite number! It’s {favorite_number}.")