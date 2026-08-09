numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)



numbers = [10, 20, 30, 40]
numbers.sort()
print(numbers)



numbers = [50, 20, 40, 10, 30]
numbers.sort(reverse=True)
print(numbers)



fruits = ["Mango", "Apple", "Banana", "Orange"]
fruits.sort()
print(fruits)



fruits = ["Mango", "Apple", "Banana", "Orange"]
fruits.sort(reverse=True)
print(fruits)




names = ["apple", "Banana", "cherry", "Apple"]
names.sort()
print(names)



names = ["apple", "Banana", "cherry", "Apple"]
names.sort(key=str.lower)
print(names)



fruits = ["Apple", "Kiwi", "Watermelon", "Fig"]
fruits.sort(key=len)
print(fruits)



fruits = ["Apple", "Kiwi", "Watermelon", "Fig"]
fruits.sort(key=len,reverse=True)
print(fruits)



names = ["Saniya", "Priya", "Aman", "Neha"]
names.sort(reverse=True)
print(names)   






marks = [78, 92, 65, 88, 95]
marks.sort(reverse=True)
print(marks)



employees = [
    {"name": "Saniya", "salary": 45000},
    {"name": "Priya", "salary": 60000},
    {"name": "Aman", "salary": 40000},
    {"name": "Neha", "salary": 75000}
]
employees.sort(key=lambda employee: employee["salary"])
for employee in employees:
    print(employee)



numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)




fruits = ["Apple", "Banana", "Mango"]
fruits.reverse()
print(fruits)


numbers = [30, 10, 40, 20]
numbers.reverse()
print(numbers)



numbers = [50, 20, 40, 10, 30]
new_numbers = sorted(numbers)
print(new_numbers)




numbers = [50, 20, 40, 10, 30]
new_numbers = sorted(numbers)
print("Original:", numbers)
print("Sorted:", new_numbers)



students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]
students.sort(key=lambda student: student[1])
print(students)



students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]
students.sort(
    key=lambda student: student[1],
    reverse=True
)
print(students)