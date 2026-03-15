# Create a glossary dictionary where keys are terms and values are definitions
words = {
    'Variable': 'A named "container" used to store data values',
    'String': 'A sequence of characters used for text, always wrapped in quotes',
    'List': 'A collection of items kept in a specific order inside square brackets',
    'Dictionary': 'A collection of key-value pairs used to connect pieces of data',
    'Function': 'A named block of code that performs a specific action when you call it'
}

# Use .items() to loop through the terms (keys) and definitions (values)
for key, value in words.items():
    # \n is a "newline" character used to add a line break for better readability
    print(f'{key}:\n{value}\n')