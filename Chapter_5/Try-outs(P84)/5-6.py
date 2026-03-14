# Set the age to test
age = 23

# Check for the youngest category first
if age < 2:
    print('This person is a baby')

# Python only reaches this elif if the age is 2 or older
elif age < 4:
    print("This person is a toddler.")

# Only reached if age is 4 or older
elif age < 13:
    print("This person is a kid.")

# Only reached if age is 13 or older
elif age < 20:
    print("This person is a teenager.")

# Only reached if age is 20 or older
elif age < 65:
    print("This person is an adult.") # This executes because 23 is less than 65

# The catch-all for anyone 65 or older
else:
    print("This person is an elder.")