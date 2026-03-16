#1. Use a conditional test in the while statement to stop the loop.

# Initialize age_input with an empty string so the 'while' condition
# is True the first time, allowing the loop to start.
age_input = ''

# The loop condition is checked at the start of every iteration.
# It will keep running as long as the user hasn't typed 'quit'.
while age_input != 'quit':
    # Prompt the user and convert their input to lowercase 
    # to make the check against 'quit' case-insensitive.
    age_input = input("\nPlease enter your age (or 'quit' to exit): ").lower()

    # We must check the condition again inside the loop because, if the user
    # types 'quit', we need to skip the math logic to avoid a crash.
    if age_input != 'quit':
        # Convert the string input (e.g., '10') into an integer (10)
        age = int(age_input)

        # Logic to determine ticket price based on age brackets
        if age < 3:
            price = "free"
        elif age <= 12:
            price = "$10"
        else:
            price = "$15"

        # Print the final price for the user
        print(f"Your ticket price is {price}.")
    else:
        # This part runs only if age_input is equal to 'quit'
        print("Goodbye!")

################################################################################
################################################################################

#2.Use an active variable to control how long the loop runs.

# Initialize a flag variable called 'active' to True;
# this acts as the "master switch" for our while loop.
active = True

# The loop evaluates the 'active' variable at the start of every cycle.
# If 'active' is False, the loop stops immediately.
while active:
    age_input = input("\nPlease enter your age (or 'quit' to exit): ")

    # Check for the exit command before processing any data.
    # .lower() ensures that 'Quit', 'QUIT', or 'quit' are all treated the same.
    if age_input.lower() == 'quit':
        print("Goodbye!")
        # Setting active to False is the mechanism that signals
        # the loop to stop after the current iteration finishes.
        active = False
    else:
        # Convert the string input (from the user) into an integer
        # so we can perform numeric comparisons.
        age = int(age_input)

        # Logic to determine ticket price based on age brackets.
        if age < 3:
            price = "free"
        elif age <= 12:
            price = "$10"
        else:
            price = "$15"

        # Display the result to the user.
        print(f"Your ticket price is {price}.")

##################################################################################
##################################################################################

#3.Use a break statement to exit the loop when the user enters a 'quit' value.

# We use 'while True' to create an infinite loop that continues
# until we explicitly tell it to stop using a 'break' statement.
while True:
    age_input = input("\nPlease enter your age (or 'quit' to exit): ")

    # The 'break' statement is our "emergency exit."
    # We check for the 'quit' value first so we don't accidentally
    # try to convert the word "quit" into a number, which would crash the program.
    if age_input.lower() == 'quit':
        print("Goodbye!")
        # 'break' immediately jumps the program flow out of the while loop,
        # stopping the loop entirely.
        break

    # Convert the user's string input into an integer for numerical comparison.
    # If the user types something that isn't a number, this line will raise a ValueError.
    age = int(age_input)

    # Use an if-elif-else chain to determine the price bracket.
    if age < 3:
        price = "free"
    elif age <= 12:
        price = "$10"
    else:
        price = "$15"

    # Because this print is outside the if/elif/else block, it runs 
    # for every valid age entered before the loop starts again.
    print(f"Your ticket price is {price}.")