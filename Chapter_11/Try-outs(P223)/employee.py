# 1. THE CLASS DEFINITION
# A class is like a template or a cookie cutter. 
# It defines what an 'Employee' is and what they can do.
class Employee:
    
    # 2. THE CONSTRUCTOR (__init__)
    # This special method runs automatically every time you create a new employee.
    # 'self' refers to the specific individual employee being created.
    def __init__(self, first, last, salary):
        """Initialize the employee's attributes."""
        # We store the data in 'attributes' (variables that belong to the object).
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    # 3. THE METHOD (give_raise)
    # A method is a function that belongs to the class.
    # By setting 'amount=5000', we provide a default raise value.
    def give_raise(self, amount=5000):
        """Add a raise to the employee's total salary."""
        # This updates the specific employee's salary attribute.
        self.salary += amount