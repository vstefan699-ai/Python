# test_cities.py

# 1. IMPORT THE FUNCTION
# We pull in the specific function we want to verify from your other file.
from city_functions import get_city_country

# 2. TEST CASE: BASIC FUNCTIONALITY
def test_city_country():
    """Verify that 'Santiago, Chile' formats correctly."""
    result = get_city_country('santiago', 'chile')
    
    # 'assert' checks if the following expression is True.
    # If it matches, the test passes silently.
    # If it fails, Python raises an AssertionError.
    assert result == 'Santiago, Chile'

# 3. TEST CASE: OPTIONAL PARAMETERS
def test_city_country_population():
    """Verify that population data is included correctly in the string."""
    result = get_city_country('santiago', 'chile', '5000000')
    
    # We are testing the specific string format including the population.
    assert result == 'Santiago, Chile - population 5000000'