'''1. `index()`
Returns the **index (position)** of the **first occurrence** of a value.'''

fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Banana"))

numbers = [10, 20, 30, 20, 40]
print(numbers.index(20))


numbers = [10, 20, 30, 20, 40]
print(numbers.index(20, 2))

'''2. `count()`
Returns the **number of times** a value appears.'''


numbers = [10, 20, 20, 30, 20]
print(numbers.count(20))

fruits = ["Apple", "Banana", "Apple"]
print(fruits.count("Apple"))