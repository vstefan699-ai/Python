# Store the name with extra whitespace characters
# \t adds a tab and \n adds a new line
name = '\t stefan \n'

# Print the name with the whitespace included
print(name)

# Print the name with whitespace removed from the left side
print(name.lstrip())

# Print the name with whitespace removed from the right side
print(name.rstrip())

# Print the name with whitespace removed from both sides
print(name.strip())