# Create an empty dictionary
student = {}

##############################################################
# Adding key-value pairs to the dictionary
student['name'] = 'Alice'
student['age'] = 20
student['major'] = 'Computer Science'
print(f"After adding data: {student}")

##############################################################
print()

# Updating existing values by assigning new data to the same keys
student['age'] = 21
student['major'] = 'Data Science'
print(f"After updating values: {student}")

##############################################################
print()

# Removing a key-value pair using the 'del' statement
del student['major']
print(f"After deleting major: {student}")

##############################################################
print()

# Using the .get() method to safely retrieve a value
# This returns the value if the key exists, or None if it doesn't
student_age = student.get('age')
print(f"Student age retrieved safely: {student_age}")

##############################################################
print()

# A direct use of .get() within a print statement
print(f"Age: {student.get('age')}")