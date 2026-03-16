# Create the prompt string; \n adds a new line for better readability
prompt = "\nPlease enter a pizza topping you'd like to add:"
prompt += "\n(Enter 'quit' when you are finished) "

# Use an infinite loop (while True) to keep asking for toppings
# until the user explicitly tells the program to stop
while True:
    # Capture the user's input
    topping = input(prompt)
    
    # Check if the user wants to quit; .lower() ensures it works
    # even if the user types 'QUIT' or 'Quit'
    if topping.lower() == 'quit':
        print("Okay, finishing your order!")
        # 'break' immediately stops the loop and moves the code 
        # to the next line outside the loop
        break 
    else:
        # If the user didn't type quit, acknowledge the topping
        print(f"I'll add {topping} to your pizza.")