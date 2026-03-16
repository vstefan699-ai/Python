# Initialize the flag to 'True' to control the loop's lifecycle
active = True

# The loop continues to run as long as 'active' remains True
while active:
    # 1. Ask the user for input; input() always returns a string
    user_input = input("Enter a number between 1 and 10 (or 'quit' to exit): ")

    # 5. Check if user wants to quit; .lower() ensures 'Quit' or 'QUIT' also work
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        active = False # Setting the flag to False prevents the next loop iteration
        break          # 4. 'break' exits the entire loop immediately

    # 3. Use .isdigit() to check if the string contains only numbers before converting
    if not user_input.isdigit():
        print("That is not a number. Try again.")
        continue  # 'continue' stops the current cycle and skips to the start of the while loop

    # Convert the validated string input into an actual integer for comparison
    number = int(user_input)

    # 3. Check if the number is within the defined range (1-10)
    if number < 1 or number > 10:
        print("Number is out of range. Try again.")
        continue # 'continue' restarts the loop to ask for input again

    # 6. Logic to handle a specific exit condition (e.g., number 5 triggers an exit)
    if number == 5:
        print("You entered 5, exiting the loop.")
        active = False
        break          # Exits the loop structure entirely

    # If the input passed all checks (number is 1-10 and not 5), process the data
    print(f"You entered: {number}")