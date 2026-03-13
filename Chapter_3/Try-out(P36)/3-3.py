# Create a list containing different models of bakkies
bakkies = ['Isuzu V-Cross', 'Isuzu Artic', 'Ford Raptor']

# Start a 'for' loop to iterate (loop) through the 'bakkies' list
# 'bakkie' is a temporary variable that represents one item at a time
for bakkie in bakkies:
    
    # Use an f-string to plug the current bakkie name into the sentence
    # This line runs once for every item in the list
    print(f"I would like to own a {bakkie}")