# city_functions.py

def get_city_country(city, country, population=''):
    """Generate a neatly formatted city and country name."""
    
    # 1. CHECK FOR OPTIONAL DATA
    # If 'population' was provided (it's not an empty string), 
    # we format the long version.
    if population:
        output = f"{city.title()}, {country.title()} - population {population}"
    
    # 2. THE FALLBACK
    # If 'population' is empty, we just show the city and country.
    else:
        output = f"{city.title()}, {country.title()}"
        
    return output

# --- How to call this function ---

# Scenario A: With population
# Result: "Kuruman, South Africa - population 53000"
print(get_city_country('kuruman', 'south africa', '53000'))

# Scenario B: Without population
# Result: "London, United Kingdom"
print(get_city_country('london', 'united kingdom'))