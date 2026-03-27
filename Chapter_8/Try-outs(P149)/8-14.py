# The **car_info parameter acts as a 'catch-all' for any extra 
# keyword arguments provided (like color or Farm_Rigged).
def car_make(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""

    # Add the required manufacturer and model to the dictionary 
    # using specific keys.
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    
    # Return the dictionary back to the caller
    return car_info

# Call the function with two required strings and two extra keyword arguments
# 'Isuzu' and 'D-Max' are required; the others are optional.
car_profile = car_make('Isuzu', 'D-Max', color='Blue', Farm_Rigged=True)

# Iterate through the dictionary to display the car's specifications
# .items() gives us access to both the attribute (key) and the detail (value)
for key, value in car_profile.items():
    # .replace('_', ' ') changes 'Farm_Rigged' to 'Farm Rigged' for cleaner output
    # .title() capitalizes each word
    print(f'{key.replace("_", " ").title()}: {value}')