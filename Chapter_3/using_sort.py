#Sample list
cars = ['bmw', 'audi', 'toyota', 'subaru']

#Sorting the list permanently
cars.sort()
print("Sorted list(ascending):", cars)

#Sorting the list in reverse order
cars.sort(reverse=True)
print("Sorted list(descending):", cars)

#Using sorted() to display the list temporarily sorted
original_cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original list:", original_cars)
print("Sorted list temporarily:", sorted(original_cars))

#Showing that the original list remains unchanged
print("Original list after sorted() (unchanged):", original_cars)

#Reversing the order of the list
cars.reverse()
print("Reversed list:", cars)

#Finding the length of the list
print("Length of the list:", len(cars))
#####################################################
#Accesing a value that doesn't exist
motorcycles = ['honda', 'yamaha', 'suzuki']

#Trying to access an index that doesn't exist
print(motorcycles[3])