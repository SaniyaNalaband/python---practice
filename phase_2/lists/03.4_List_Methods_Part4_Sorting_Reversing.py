'''1. `sort()`
Sorts the original list in **ascending order**.'''

numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)


fruits = ["Mango", "Apple", "Banana"]
fruits.sort()
print(fruits)

numbers = [40, 10, 30, 20]
numbers.sort(reverse=True)
print(numbers)

names = ["saniya", "Rahul", "aisha", "Kiran"]
names.sort(key=str.lower)
print(names)

words = ["Python", "AI", "Machine", "ML"]
words.sort(key=len)
print(words)


marks = [75, 90, 85, 60]
marks.sort()
print(marks)

scores = [95, 88, 99, 70]
scores.sort(reverse=True)
print(scores)


students = [
    ("Rahul", 85),
    ("Saniya", 95),
    ("Aisha", 90)
]

students.sort(key=lambda x: x[1])
print(students)

'''2. `reverse()`
Reverses the current order of the list.'''

numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

numbers = [30, 10, 40, 20]
numbers.reverse()
print(numbers)


'''3. `sorted()`
`sorted()` is a **built-in function**, not a list method.
It returns a **new sorted list** without changing the original.
'''

numbers = [30, 10, 40, 20]
new_list = sorted(numbers)
print(new_list)
print(numbers)


numbers = [30, 10, 40, 20]
print(sorted(numbers, reverse=True))

