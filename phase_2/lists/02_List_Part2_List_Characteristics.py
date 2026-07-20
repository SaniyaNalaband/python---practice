# ORDERED LIST

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# MUTABLE(CAN BE CHAGED)

colors = ["Red", "Blue", "Green"]
colors[1] = "Yellow"
print(colors)

# ALLOWS DUPLICATE VALUES

numbers = [10, 20, 10, 30, 20, 10]
print(numbers)


# CAN STORE DIFFERENT DATA TYPES 

data = [
    "Saniya",
    20,
    85.5,
    True,
    2 + 3j
]
print(data)

# CAN STORE ANOTHER LIST(NESTED LIST)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)


# DYNAMIC SIZE 

fruits = ["Apple", "Banana"]

print(fruits)
fruits.append("Mango")
print(fruits)
fruits.append("Orange")
print(fruits)

# SUPPORTS POSITIVE ANS NEGETIVE INDEXING 

cities = ["Mysuru", "Bengaluru", "Hubli", "Belagavi"]
print(cities[0])
print(cities[-1])
print(cities[-2])

# SUPPORTS SLICING

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:5])
print(numbers[:3])
print(numbers[::2])

# ALLOWS MEMBERSHIP TRAINING 

languages = ["Python", "Java", "SQL"]
print("Python" in languages)
print("C++" in languages)
print("Java" not in languages)

# ITERRABELE CAN BE USED IN LOOPS 

subjects = ["Python", "Java", "SQL", "HTML"]
for subject in subjects:
    print(subject)

