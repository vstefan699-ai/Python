# Function with required parameters
# These must be provided in order unless specifically named
def greeting(name, age):
    print(f'Good morning {name}, can you believe you are {age} years old this year')

# Calling the function with specific values (Arguments)
greeting('Pete', 18)
greeting('Jonny', 23)

#######################################################################################
print()

# Function with default values
# If you don't provide a name or age, Python uses 'Will' and 43 automatically
def greetings(name='Will', age=43):
    print(f'Hey {name}, are you really turning {age} this year?')

# Calling the function without arguments uses the defaults
greetings()

# Calling the function with keyword arguments overrides the defaults
greetings(name='Santa', age=29)