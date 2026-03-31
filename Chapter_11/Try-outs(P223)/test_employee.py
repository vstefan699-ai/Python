import pytest
# We import the Class we want to test from your employee.py file
from employee import Employee

# 1. THE FIXTURE
# @pytest.fixture is a "decorator." It tells pytest that this function 
# is a resource that other tests can use.
@pytest.fixture
def employee_setup():
    """Create a fresh employee for every test."""
    # This object is created brand new every time a test starts.
    return Employee('eric', 'matthes', 65000)

# 2. USING THE FIXTURE
# Notice how 'employee_setup' is passed as an argument to the test functions.
# Pytest sees the name match and automatically plugs in the object from the fixture.
def test_give_default_raise(employee_setup):
    """Test that the default $5,000 raise works."""
    employee_setup.give_raise()
    assert employee_setup.salary == 70000

def test_give_custom_raise(employee_setup):
    """Test that a specific raise amount (e.g., $10,000) works."""
    employee_setup.give_raise(10000)
    assert employee_setup.salary == 75000