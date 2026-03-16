# Use an infinite loop to continuously ask for ages
while True:
    age_input = input("\nPlease enter your age (or 'quit' to exit): ")

    # Check for the exit command before trying to process the data
    if age_input.lower() == 'quit':
        print("Goodbye!")
        # 'break' exits the loop immediately
        break

    # Convert the string input into an integer to perform comparisons
    age = int(age_input)

    # Use if-elif-else chain to categorize the price based on age
    if age < 3:
        price = "free"
    elif age <= 12:
        price = "$10"
    else:
        price = "$15"

    # This print is now outside the if/elif/else block,
    # so it will run regardless of which price category was chosen
    print(f"Your ticket price is {price}.")