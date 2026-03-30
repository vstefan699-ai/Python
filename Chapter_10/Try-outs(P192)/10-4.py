# 1. Collect user input and store it in a variable called 'name'
# The input() function always returns data as a string.
name = input('Please enter your name: ')

# 2. Use the 'with' keyword to open (or create) a file.
# 'guest.txt' is the name of the file.
# 'w' stands for 'write mode'. 
# Note: 'w' will overwrite the file if it already exists or create it if it doesn't.
# 'file_object' is the temporary name (alias) we use to refer to the file in code.
with open('guest.txt', 'w') as file_object:
    
    # 3. Use the .write() method to save the contents of 'name' into the file.
    file_object.write(name)

# Outside the 'with' block, the file is automatically closed.
# This saves memory and prevents data corruption.