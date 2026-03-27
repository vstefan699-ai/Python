# Define a function with one required parameter (name) and one default (country)
# The .title() method ensures the output looks like a proper noun (e.g., 'Gaborone')
def describe_city(name, country='Botswana'):
    """Display a simple sentence about a city and its country."""
    print(f'{name.title()} is in {country.title()}')

# Call with only the required argument
# Since no country is provided, it uses the default: 'Botswana'
describe_city('Gaborone')

# Call again with only the city name
# Again, this will output 'Francistown is in Botswana'
describe_city('Francistown')

# Call with both arguments to override the default
# This tells Python to ignore 'Botswana' and use 'South Africa' instead
describe_city('Cape Town', 'South Africa')