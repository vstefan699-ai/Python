# Create a list of multiples of 3 from 3 to 30.
# range(start, stop, step)
# Start at 3, stop at 31 (to ensure 30 is included), and use a step of 3.
multiples_of_three = list(range(3, 31, 3))

# Iterate through the list and print each multiple.
for number in multiples_of_three:
    print(number)