# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 20: `zip()`

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what `zip()` is.
* [ ] Understand why `zip()` is useful.
* [ ] Understand the syntax of `zip()`.
* [ ] Combine two sequences using `zip()`.
* [ ] Combine multiple sequences using `zip()`.
* [ ] Iterate over zipped data using a `for` loop.
* [ ] Understand how `zip()` handles sequences of different lengths.
* [ ] Convert `zip()` objects into lists.
* [ ] Convert `zip()` objects into tuples.
* [ ] Create dictionaries using `zip()`.
* [ ] Use `zip()` with `dict()`.
* [ ] Unzip data using `zip(*)`.
* [ ] Use `zip()` with lists.
* [ ] Use `zip()` with tuples.
* [ ] Use `zip()` with strings.
* [ ] Use `zip()` with loops and conditions.
* [ ] Use `zip()` with `enumerate()`.
* [ ] Use `zip()` with dictionary methods.
* [ ] Use `zip()` in real-world applications.
* [ ] Avoid common mistakes when using `zip()`.
* [ ] Solve advanced problems using `zip()`.

---

# 📖 1. What is `zip()`?

`zip()` is a built-in Python function used to combine elements from two or more iterables.

It takes the first element from each iterable and combines them together.

Then it takes the second element from each iterable and combines them together.

Example:

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

result = zip(names, ages)

print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21), ('Riya', 19)]
```

Here:

```text
names → first iterable
ages  → second iterable
zip() → combines corresponding elements
```

---

# 🧠 2. Why Do We Use `zip()`?

Suppose you have two related lists:

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]
```

You may want to process them together.

Without `zip()`:

```python
for i in range(len(students)):
    print(students[i], marks[i])
```

With `zip()`:

```python
for student, mark in zip(students, marks):
    print(student, mark)
```

Output:

```text
Asha 90
Neha 85
Riya 88
```

`zip()` makes the code cleaner and easier to understand.

---

# 📚 3. Syntax of `zip()`

The general syntax is:

```python
zip(iterable1, iterable2, iterable3, ...)
```

Example:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

result = zip(names, marks)

print(list(result))
```

The important point is:

```text
zip()
 ↓
Combines corresponding elements
```

---

# 🔗 4. Combining Two Lists

You can combine two lists using `zip()`.

```python
names = ["Asha", "Neha", "Riya"]
courses = ["BCA", "BBA", "BCom"]

combined = zip(names, courses)

print(list(combined))
```

Output:

```text
[('Asha', 'BCA'), ('Neha', 'BBA'), ('Riya', 'BCom')]
```

The first elements are combined:

```text
Asha + BCA
```

The second elements are combined:

```text
Neha + BBA
```

The third elements are combined:

```text
Riya + BCom
```

---

# 🧩 5. Understanding the Pairing

Consider:

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]
```

When using:

```python
zip(names, ages)
```

Python pairs them like this:

```text
Asha  → 20
Neha  → 21
Riya  → 19
```

The resulting structure is:

```text
('Asha', 20)
('Neha', 21)
('Riya', 19)
```

Each pair is a tuple.

---

# 🔄 6. Using `zip()` with a `for` Loop

One of the most common uses of `zip()` is inside a `for` loop.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for name, mark in zip(names, marks):
    print(name, ":", mark)
```

Output:

```text
Asha : 90
Neha : 85
Riya : 88
```

Here:

```text
name → receives an element from names
mark → receives the corresponding element from marks
```

---

# 🧠 7. `zip()` Returns a Zip Object

When you directly print `zip()`, you do not normally see the combined values.

```python
names = ["Asha", "Neha"]
ages = [20, 21]

result = zip(names, ages)

print(result)
```

Typical output:

```text
<zip object at 0x...>
```

This is because `zip()` returns a **zip object**.

To see its contents, convert it to a list:

```python
print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21)]
```

---

# 📋 8. Converting `zip()` to a List

You can convert a zip object into a list.

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

result = zip(names, ages)

data = list(result)

print(data)
```

Output:

```text
[('Asha', 20), ('Neha', 21), ('Riya', 19)]
```

The structure becomes:

```text
list
 ↓
tuples
 ↓
(key-like value pairs)
```

---

# 🔢 9. Converting `zip()` to a Tuple

You can also convert the result into a tuple.

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

result = zip(names, ages)

data = tuple(result)

print(data)
```

Output:

```text
(('Asha', 20), ('Neha', 21), ('Riya', 19))
```

---

# 📏 10. `zip()` with Equal-Length Iterables

When all iterables have the same length, every element gets paired.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

print(list(zip(names, marks)))
```

Output:

```text
[('Asha', 90), ('Neha', 85), ('Riya', 88)]
```

There are three elements in each iterable, so there are three pairs.

---

# ⚠️ 11. `zip()` with Different-Length Iterables

If the iterables have different lengths, normal `zip()` stops when the **shortest iterable** is exhausted.

Example:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85]

print(list(zip(names, marks)))
```

Output:

```text
[('Asha', 90), ('Neha', 85)]
```

The `"Riya"` element is not included.

Remember:

```text
zip()
 ↓
Stops at the shortest iterable
```

---

# 🧠 12. Understanding the Shortest Iterable Rule

Consider:

```python
a = [1, 2, 3, 4]
b = ["A", "B"]
```

Using:

```python
zip(a, b)
```

produces:

```text
(1, 'A')
(2, 'B')
```

The remaining elements:

```text
3
4
```

are ignored because `b` has no more elements.

---

# 🔗 13. Combining Three Lists

`zip()` can combine more than two iterables.

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]
courses = ["BCA", "BBA", "BCom"]

result = zip(names, ages, courses)

print(list(result))
```

Output:

```text
[
    ('Asha', 20, 'BCA'),
    ('Neha', 21, 'BBA'),
    ('Riya', 19, 'BCom')
]
```

Each tuple contains three values.

---

# 🔢 14. Combining Multiple Lists

You can use several iterables with `zip()`.

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 85, 88]
sql_marks = [85, 80, 90]
git_marks = [88, 82, 86]

data = zip(students, python_marks, sql_marks, git_marks)

for student, python, sql, git in data:
    print(student, python, sql, git)
```

Output:

```text
Asha 90 85 88
Neha 85 80 82
Riya 88 90 86
```

---

# 🧩 15. `zip()` with Strings

Strings are iterable, so they can also be used with `zip()`.

```python
letters = "ABC"
numbers = "123"

print(list(zip(letters, numbers)))
```

Output:

```text
[('A', '1'), ('B', '2'), ('C', '3')]
```

Each character is treated as an individual element.

---

# 🔁 16. `zip()` with Tuples

`zip()` works with tuples too.

```python
names = ("Asha", "Neha", "Riya")
ages = (20, 21, 19)

result = zip(names, ages)

print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21), ('Riya', 19)]
```

`zip()` works with many iterable types, not only lists.

---

# 🏗️ 17. Creating a Dictionary Using `zip()`

One of the most useful applications of `zip()` is creating dictionaries.

Suppose:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]
```

You can create a dictionary:

```python
marks_dict = dict(zip(names, marks))

print(marks_dict)
```

Output:

```text
{'Asha': 90, 'Neha': 85, 'Riya': 88}
```

Here:

```text
names → keys
marks → values
```

---

# 🔑 18. `dict()` + `zip()`

The pattern:

```python
dict(zip(keys, values))
```

is extremely useful.

Example:

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

result = dict(zip(subjects, marks))

print(result)
```

Output:

```text
{'Python': 90, 'SQL': 85, 'Git': 88}
```

Remember:

```text
zip()
 ↓
Creates pairs

dict()
 ↓
Converts pairs into a dictionary
```

---

# 🧠 19. Using `zip()` to Combine Two Lists into a Dictionary

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [55000, 800, 1500]

product_prices = dict(zip(products, prices))

print(product_prices)
```

Output:

```text
{'Laptop': 55000, 'Mouse': 800, 'Keyboard': 1500}
```

This is a very common real-world pattern.

---

# 🔄 20. Looping Through a Dictionary Created with `zip()`

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

result = dict(zip(subjects, marks))

for subject, mark in result.items():
    print(subject, ":", mark)
```

Output:

```text
Python : 90
SQL : 85
Git : 88
```

Here `zip()` and `items()` work together.

---

# 🧩 21. Using `zip()` with Conditions

You can combine `zip()` with `if`.

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 65, 88]

for student, mark in zip(students, marks):
    if mark >= 80:
        print(student, ":", mark)
```

Output:

```text
Asha : 90
Riya : 88
```

This allows you to process related data while applying conditions.

---

# 🔢 22. Calculating Totals Using `zip()`

Suppose students have marks in two subjects.

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 80, 85]
sql_marks = [85, 75, 90]

for student, python, sql in zip(students, python_marks, sql_marks):
    total = python + sql
    print(student, ":", total)
```

Output:

```text
Asha : 175
Neha : 155
Riya : 175
```

---

# 📊 23. Calculating Averages Using `zip()`

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 80, 85]
sql_marks = [85, 75, 90]

for student, python, sql in zip(students, python_marks, sql_marks):
    average = (python + sql) / 2
    print(student, ":", average)
```

Output:

```text
Asha : 87.5
Neha : 77.5
Riya : 87.5
```

---

# 🔍 24. Finding the Highest Value Using `zip()`

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 85, 95]

highest = 0
top_student = ""

for student, mark in zip(students, marks):
    if mark > highest:
        highest = mark
        top_student = student

print("Top Student:", top_student)
print("Marks:", highest)
```

Output:

```text
Top Student: Riya
Marks: 95
```

---

# 🔄 25. Using `zip()` with `enumerate()`

You can combine `enumerate()` and `zip()`.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for index, (name, mark) in enumerate(zip(names, marks)):
    print(index, name, mark)
```

Output:

```text
0 Asha 90
1 Neha 85
2 Riya 88
```

Here:

```text
zip()
 ↓
creates pairs

enumerate()
 ↓
adds indexes
```

---

# 🧠 26. Starting `enumerate()` from 1

You can start the index from `1`.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for number, (name, mark) in enumerate(zip(names, marks), start=1):
    print(number, name, mark)
```

Output:

```text
1 Asha 90
2 Neha 85
3 Riya 88
```

This is useful for displaying numbered records.

---

# 🔓 27. Unzipping Data

`zip()` can also be used to reverse the pairing process.

Suppose:

```python
data = [
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
]
```

You can unzip it using:

```python
names, marks = zip(*data)

print(names)
print(marks)
```

Output:

```text
('Asha', 'Neha', 'Riya')
(90, 85, 88)
```

The `*` operator unpacks the pairs.

---

# 🧠 28. Understanding `zip(*)`

Consider:

```python
data = [
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
]
```

Using:

```python
zip(*data)
```

is conceptually like:

```python
zip(
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
)
```

The result separates the first values from the second values.

Therefore:

```text
First column  → names
Second column → marks
```

---

# 🔄 29. Recreating Original Lists After Unzipping

```python
data = [
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
]

names, marks = zip(*data)

names = list(names)
marks = list(marks)

print(names)
print(marks)
```

Output:

```text
['Asha', 'Neha', 'Riya']
[90, 85, 88]
```

---

# 🧩 30. Using `zip()` with Dictionary Keys

You can combine dictionary keys with another iterable.

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

values = ["Asha", 20, "BCA"]

for key, value in zip(student.keys(), values):
    print(key, ":", value)
```

Output:

```text
name : Asha
age : 20
course : BCA
```

---

# 🔗 31. Using `zip()` with Dictionary Values

You can also combine two sets of values.

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

for subject, mark in zip(subjects, marks):
    print(subject, "→", mark)
```

Output:

```text
Python → 90
SQL → 85
Git → 88
```

This is one of the most common uses of `zip()`.

---

# 🏗️ 32. Creating Employee Records Using `zip()`

```python
fields = ["id", "name", "department", "salary"]
values = [101, "Neha", "Development", 45000]

employee = dict(zip(fields, values))

print(employee)
```

Output:

```text
{
    'id': 101,
    'name': 'Neha',
    'department': 'Development',
    'salary': 45000
}
```

This is useful when data is received separately.

---

# 🛒 33. Real-World Example: Shopping Cart

Suppose product names and prices are stored separately.

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [55000, 800, 1500]

cart = dict(zip(products, prices))

total = 0

for price in cart.values():
    total += price

print("Cart:", cart)
print("Total:", total)
```

Output:

```text
Cart: {'Laptop': 55000, 'Mouse': 800, 'Keyboard': 1500}
Total: 57300
```

---

# 🎓 34. Real-World Example: Student Marks

```python
subjects = ["Python", "SQL", "Git", "HTML"]
marks = [90, 85, 80, 88]

student_marks = dict(zip(subjects, marks))

for subject, mark in student_marks.items():
    print(subject, ":", mark)
```

Output:

```text
Python : 90
SQL : 85
Git : 80
HTML : 88
```

---

# 👨‍💼 35. Real-World Example: Employee Information

```python
fields = [
    "employee_id",
    "name",
    "department",
    "salary"
]

values = [
    101,
    "Neha",
    "Development",
    45000
]

employee = dict(zip(fields, values))

print(employee)
```

Output:

```text
{
    'employee_id': 101,
    'name': 'Neha',
    'department': 'Development',
    'salary': 45000
}
```

---

# 📦 36. Real-World Example: Product Inventory

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [5, 15, 10, 7]

inventory = dict(zip(products, stock))

for product, quantity in inventory.items():
    if quantity < 10:
        print(product, "needs restocking")
```

Output:

```text
Laptop needs restocking
Monitor needs restocking
```

---

# 💰 37. Real-World Example: Product Prices

```python
products = ["Laptop", "Phone", "Tablet"]
prices = [55000, 30000, 20000]

for product, price in zip(products, prices):
    if price > 25000:
        print(product, ":", price)
```

Output:

```text
Laptop : 55000
Phone : 30000
```

---

# 🌍 38. Real-World Example: City Temperatures

```python
cities = ["Bengaluru", "Mumbai", "Delhi"]
temperatures = [26, 30, 34]

for city, temperature in zip(cities, temperatures):
    print(city, ":", temperature, "°C")
```

Output:

```text
Bengaluru : 26 °C
Mumbai : 30 °C
Delhi : 34 °C
```

---

# 🔢 39. Real-World Example: Student Result Processing

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 65, 82]

for student, mark in zip(students, marks):
    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    else:
        result = "Needs Improvement"

    print(student, ":", result)
```

Output:

```text
Asha : Excellent
Neha : Good
Riya : Excellent
```

---

# ⚠️ 40. Common Mistake: Printing the Zip Object

Wrong assumption:

```python
names = ["Asha", "Neha"]
ages = [20, 21]

result = zip(names, ages)

print(result)
```

Output will look similar to:

```text
<zip object at 0x...>
```

This does not mean `zip()` failed.

Correct:

```python
print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21)]
```

---

# ⚠️ 41. Common Mistake: Reusing an Exhausted Zip Object

A zip object is an iterator.

Example:

```python
names = ["Asha", "Neha"]
ages = [20, 21]

result = zip(names, ages)

print(list(result))
print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21)]
[]
```

Why?

Because the zip object has already been consumed.

Remember:

```text
First use
   ↓
Data available

Second use
   ↓
Zip object already exhausted
```

If you need the data multiple times, store it:

```python
result = list(zip(names, ages))

print(result)
print(result)
```

---

# ⚠️ 42. Common Mistake: Different Lengths

Consider:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85]

print(list(zip(names, marks)))
```

Output:

```text
[('Asha', 90), ('Neha', 85)]
```

`Riya` is not included.

Remember:

```text
zip()
 ↓
Stops at shortest iterable
```

---

# 🧠 43. `zip()` vs `range(len())`

Traditional approach:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for i in range(len(names)):
    print(names[i], marks[i])
```

Using `zip()`:

```python
for name, mark in zip(names, marks):
    print(name, mark)
```

The second approach is generally cleaner when you simply need corresponding elements.

---

# ⚖️ 44. `zip()` vs Manual Indexing

| Approach                | Purpose                           |
| ----------------------- | --------------------------------- |
| `range(len())`          | Work with indexes                 |
| `zip()`                 | Work with corresponding values    |
| `enumerate()`           | Work with index + value           |
| `zip()` + `enumerate()` | Work with index + multiple values |

Example:

```python
for name, mark in zip(names, marks):
    print(name, mark)
```

is easier to read than manually accessing:

```python
names[i]
marks[i]
```

---

# 🧩 45. Using `zip()` with List Comprehension

You can use `zip()` inside a list comprehension.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

result = [name + " : " + str(mark)
          for name, mark in zip(names, marks)]

print(result)
```

Output:

```text
['Asha : 90', 'Neha : 85', 'Riya : 88']
```

---

# 🔥 46. Advanced Example: Filtering with List Comprehension

```python
names = ["Asha", "Neha", "Riya", "Diya"]
marks = [90, 65, 88, 72]

result = [
    (name, mark)
    for name, mark in zip(names, marks)
    if mark >= 80
]

print(result)
```

Output:

```text
[('Asha', 90), ('Riya', 88)]
```

---

# 🏆 47. Advanced Example: Creating a Dictionary with a Condition

```python
subjects = ["Python", "SQL", "Git", "HTML"]
marks = [90, 65, 88, 72]

result = {
    subject: mark
    for subject, mark in zip(subjects, marks)
    if mark >= 80
}

print(result)
```

Output:

```text
{'Python': 90, 'Git': 88}
```

This combines:

```text
zip()
+
dictionary comprehension
+
condition
```

---

# 📊 48. Advanced Example: Comparing Two Lists

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 82, 90]

for student, old, new in zip(students, old_marks, new_marks):
    difference = new - old
    print(student, ":", difference)
```

Output:

```text
Asha : 10
Neha : 2
Riya : 5
```

This can be useful for comparing performance.

---

# 🧠 49. Advanced Example: Finding Improved Students

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 78, 90]

for student, old, new in zip(students, old_marks, new_marks):
    if new > old:
        print(student, "improved")
```

Output:

```text
Asha improved
Riya improved
```

---

# 💻 50. Practice Programs

## 🟢 Easy

### Program 1: Combine Two Lists

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

print(list(zip(names, ages)))
```

---

### Program 2: Display Two Lists Together

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

for subject, mark in zip(subjects, marks):
    print(subject, mark)
```

---

### Program 3: Convert `zip()` to a List

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [55000, 800, 1500]

result = zip(products, prices)

print(list(result))
```

---

### Program 4: Combine Three Lists

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]
courses = ["BCA", "BBA", "BCom"]

for name, age, course in zip(names, ages, courses):
    print(name, age, course)
```

---

# 🟡 Medium

### Program 5: Create a Dictionary Using `zip()`

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

result = dict(zip(subjects, marks))

print(result)
```

---

### Program 6: Calculate Total Marks

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 80, 85]
sql_marks = [85, 75, 90]

for student, python, sql in zip(students, python_marks, sql_marks):
    total = python + sql
    print(student, ":", total)
```

---

### Program 7: Display Passing Students

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 55, 82]

for student, mark in zip(students, marks):
    if mark >= 60:
        print(student, ":", mark)
```

---

### Program 8: Create an Employee Dictionary

```python
fields = ["id", "name", "department", "salary"]
values = [101, "Neha", "Development", 45000]

employee = dict(zip(fields, values))

print(employee)
```

---

# 🔴 Advanced

## Program 9: Compare Old and New Marks

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 78, 90]

for student, old, new in zip(students, old_marks, new_marks):
    difference = new - old
    print(student, ":", difference)
```

Output:

```text
Asha : 10
Neha : -2
Riya : 5
```

---

## Program 10: Find Students Who Improved

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 78, 90]

for student, old, new in zip(students, old_marks, new_marks):
    if new > old:
        print(student, "improved")
```

Output:

```text
Asha improved
Riya improved
```

---

## Program 11: Product Inventory

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [5, 15, 10, 7]

inventory = dict(zip(products, stock))

for product, quantity in inventory.items():
    if quantity < 10:
        print(product, "needs restocking")
```

Output:

```text
Laptop needs restocking
Monitor needs restocking
```

---

## Program 12: Student Result Processing

```python
students = ["Asha", "Neha", "Riya"]
marks = [92, 68, 81]

for student, mark in zip(students, marks):
    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    else:
        result = "Needs Improvement"

    print(student, ":", result)
```

---

# 🏆 51. Challenge

Create three lists:

```text
students
Python marks
SQL marks
```

Example:

```python
students = ["Asha", "Neha", "Riya", "Diya"]

python_marks = [90, 75, 88, 65]

sql_marks = [85, 80, 92, 70]
```

Then:

1. Use `zip()` to combine the student names and marks.
2. Display every student's Python and SQL marks.
3. Calculate the total marks for each student.
4. Calculate the average marks.
5. Display only students whose average is greater than or equal to `80`.
6. Find the student with the highest total.
7. Create a dictionary containing student names and total marks.
8. Display the final dictionary.

Try solving the challenge without copying a solution.

---

# 🧪 52. Mini Project: Student Performance System

Create a student performance system using `zip()`.

Use:

```python
students = ["Asha", "Neha", "Riya", "Diya"]

python_marks = [90, 75, 88, 65]

sql_marks = [85, 80, 92, 70]

git_marks = [88, 78, 85, 72]
```

Perform the following operations:

* Combine all student information using `zip()`.
* Display each student's marks.
* Calculate total marks.
* Calculate average marks.
* Determine whether the student passed or failed.
* Display students whose average is greater than or equal to `80`.
* Find the highest-scoring student.
* Create a dictionary containing student names and their total marks.
* Display the final dictionary.

### Your Goal

Build a complete student performance program using:

```text
zip()
for loop
if / elif / else
dict()
dictionary methods
```

---

# 🎤 53. Interview Questions

* [ ] What is `zip()` in Python?
* [ ] Why is `zip()` used?
* [ ] What is the syntax of `zip()`?
* [ ] What does `zip()` return?
* [ ] How do you convert a zip object into a list?
* [ ] How do you convert a zip object into a tuple?
* [ ] Can `zip()` combine more than two iterables?
* [ ] What happens when iterables have different lengths?
* [ ] Which iterable determines the length of the result?
* [ ] Can `zip()` work with strings?
* [ ] Can `zip()` work with tuples?
* [ ] How can you create a dictionary using `zip()`?
* [ ] What is the purpose of `dict(zip(keys, values))`?
* [ ] How do you loop through a `zip()` object?
* [ ] Can `zip()` be used with conditions?
* [ ] Can `zip()` be used with `enumerate()`?
* [ ] What does `zip(*)` do?
* [ ] What does the `*` operator do when used with `zip()`?
* [ ] What happens when a zip object is used a second time?
* [ ] Is `zip()` lazy or does it immediately create a list?
* [ ] What is the difference between `zip()` and manual indexing?
* [ ] How can `zip()` be used in real-world applications?
* [ ] How can `zip()` be combined with dictionary comprehension?

---

# 📝 54. Assignment

Complete the following programs.

### Task 1

Create two lists:

```text
names
ages
```

Use `zip()` to combine them.

---

### Task 2

Create two lists containing subjects and marks.

Use `zip()` to display every subject and its marks.

---

### Task 3

Create two lists and convert their zipped result into a list.

---

### Task 4

Create three lists containing:

```text
student names
ages
courses
```

Use `zip()` to display all three values.

---

### Task 5

Create two lists:

```text
products
prices
```

Use:

```python
dict(zip(products, prices))
```

to create a product-price dictionary.

---

### Task 6

Create student names and marks.

Use `zip()` and an `if` statement to display students whose marks are greater than `80`.

---

### Task 7

Create two lists containing old marks and new marks.

Use `zip()` to find students whose marks have improved.

---

### Task 8

Create a list of tuples and use:

```python
zip(*data)
```

to unzip the data.

---

### Task 9

Use `zip()` with `enumerate()` to display:

```text
1. Student
2. Student
3. Student
```

along with their marks.

---

### Task 10

Use `zip()` to create a dictionary containing five programming skills and their levels.

Example:

```text
Python → Advanced
SQL → Intermediate
Git → Intermediate
HTML → Advanced
CSS → Beginner
```

---

### Task 11

Create a real-world program that uses at least three iterables with `zip()`.

---

### Task 12

Create a program that uses:

```text
zip()
for
if
dict()
```

to process and display selected records.

---

# 🧠 55. Memory Tricks

Remember:

```text
zip()
 ↓
Combine corresponding values
```

---

Remember the basic pattern:

```text
list1       list2
 ↓            ↓
A            10
B            20
C            30
 ↓            ↓
     zip()
       ↓
(A, 10)
(B, 20)
(C, 30)
```

---

Remember creating a dictionary:

```text
keys
 ↓
zip()
 ↑
values
 ↓
dict()
 ↓
dictionary
```

Pattern:

```python
dict(zip(keys, values))
```

---

Remember unzipping:

```text
pairs
 ↓
zip(*pairs)
 ↓
separate values
```

---

Remember the length rule:

```text
Different lengths
       ↓
zip()
       ↓
Stops at shortest iterable
```

---

Remember:

```text
zip()       → Combine
list(zip()) → Convert to list
dict(zip()) → Create dictionary
zip(*)      → Unzip
```

---

# 📌 56. Important Rules to Remember

```text
1. zip() is a built-in Python function.

2. zip() combines corresponding elements from iterables.

3. zip() can accept two or more iterables.

4. zip() returns a zip object.

5. The zip object is an iterator.

6. Convert a zip object to a list using list().

7. Convert a zip object to a tuple using tuple().

8. zip() stops when the shortest iterable is exhausted.

9. zip() can work with lists, tuples, strings, and other iterables.

10. Each result from zip() is represented as a tuple.

11. zip() is commonly used with for loops.

12. dict(zip(keys, values)) can create a dictionary.

13. zip() can be combined with conditions.

14. zip() can be combined with enumerate().

15. zip(*) can be used to unzip data.

16. A zip object is consumed after iteration.

17. Store list(zip(...)) if the data needs to be reused.

18. zip() is useful for processing related data together.

19. zip() can simplify code that would otherwise use indexes.

20. zip() is commonly used in real-world data processing.
```

---

# 📊 57. `zip()` Structure

```text
                         zip()
                           │
                           ↓
                  Combine Iterables
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       List 1            List 2           List 3
          │                │                │
          ↓                ↓                ↓
          A               10              X
          B               20              Y
          C               30              Z
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                       zip(...)
                           │
                           ↓
                 ┌─────────────────┐
                 │  (A,10,X)       │
                 │  (B,20,Y)       │
                 │  (C,30,Z)       │
                 └─────────────────┘
                           │
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
        list(zip())    dict(zip())     zip(*data)
            ↓              ↓              ↓
          List         Dictionary        Unzip
```

---

# 📚 58. Complete `zip()` Cheat Sheet

### Combine Two Lists

```python
zip(names, marks)
```

### Convert to List

```python
list(zip(names, marks))
```

### Convert to Tuple

```python
tuple(zip(names, marks))
```

### Combine Three Lists

```python
zip(names, ages, courses)
```

### Loop Through Zipped Data

```python
for name, mark in zip(names, marks):
    print(name, mark)
```

### Create Dictionary

```python
dict(zip(subjects, marks))
```

### Use with Condition

```python
for name, mark in zip(names, marks):
    if mark >= 80:
        print(name)
```

### Use with `enumerate()`

```python
for index, (name, mark) in enumerate(zip(names, marks)):
    print(index, name, mark)
```

### Unzip Data

```python
names, marks = zip(*data)
```

### Convert Unzipped Data to Lists

```python
names, marks = zip(*data)

names = list(names)
marks = list(marks)
```

### Dictionary Comprehension with `zip()`

```python
result = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}
```

---

# 🏆 59. `zip()` Mastery

```text
                         zip()
                           │
                           ↓
                  Combine Iterables
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
    Two Lists          Multiple Lists       Strings/Tuples
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ↓
                       zip object
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
           list()        dict()        tuple()
             │             │             │
             ↓             ↓             ↓
           List       Dictionary       Tuple
                           │
                           ↓
                       Processing
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
             for          if       enumerate()
              │            │            │
              └────────────┼────────────┘
                           ↓
                      Real-World Data
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
    Students            Products            Employees
```

---

# 📚 60. Summary

In this lesson, you learned:

* What `zip()` is.
* Why `zip()` is useful.
* How to use the `zip()` function.
* The syntax of `zip()`.
* How to combine two iterables.
* How to combine multiple iterables.
* How to use `zip()` with lists.
* How to use `zip()` with tuples.
* How to use `zip()` with strings.
* How to iterate through a zip object.
* How to convert a zip object into a list.
* How to convert a zip object into a tuple.
* How `zip()` handles different-length iterables.
* Why `zip()` stops at the shortest iterable.
* How to create dictionaries using `dict(zip())`.
* How to use `zip()` with dictionary methods.
* How to use `zip()` with conditions.
* How to use `zip()` with `enumerate()`.
* How to calculate totals using `zip()`.
* How to calculate averages using `zip()`.
* How to compare two sets of data.
* How to find improved values using `zip()`.
* How to unzip data using `zip(*)`.
* How to use `zip()` with list comprehensions.
* How to use `zip()` with dictionary comprehensions.
* How to use `zip()` in real-world programs.
* Common mistakes when using `zip()`.
* How zip objects behave as iterators.
* How to solve advanced problems using `zip()`.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `zip()` is.
* [ ] I understand why `zip()` is useful.
* [ ] I know the syntax of `zip()`.
* [ ] I can combine two lists using `zip()`.
* [ ] I can combine multiple lists using `zip()`.
* [ ] I can use `zip()` with a `for` loop.
* [ ] I understand the zip object.
* [ ] I can convert a zip object into a list.
* [ ] I can convert a zip object into a tuple.
* [ ] I understand what happens when iterables have different lengths.
* [ ] I understand the shortest iterable rule.
* [ ] I can use `zip()` with strings.
* [ ] I can use `zip()` with tuples.
* [ ] I can create dictionaries using `dict(zip())`.
* [ ] I can use `zip()` with conditions.
* [ ] I can use `zip()` with `enumerate()`.
* [ ] I can calculate totals using `zip()`.
* [ ] I can calculate averages using `zip()`.
* [ ] I can compare two lists using `zip()`.
* [ ] I understand `zip(*)`.
* [ ] I can unzip data.
* [ ] I can use `zip()` with list comprehensions.
* [ ] I can use `zip()` with dictionary comprehensions.
* [ ] I understand that zip objects are iterators.
* [ ] I understand that zip objects can be exhausted.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the mini project.
* [ ] I completed the assignment.
* [ ] I can use `zip()` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Advanced Function Concepts**

In the next topic, you will learn:

* Function arguments in depth.
* Positional arguments.
* Keyword arguments.
* Default arguments.
* Variable-length arguments.
* `*args`.
* `**kwargs`.
* Argument unpacking.
* Positional-only parameters.
* Keyword-only parameters.
* Combining different parameter types.
* Function return values.
* Multiple return values.
* Nested functions.
* Scope of variables.
* Local and global variables.
* `global` keyword.
* `nonlocal` keyword.
* Functions as objects.
* Passing functions as arguments.
* Returning functions.
* Higher-order functions.
* Practical real-world examples.
* Common mistakes.
* Advanced function techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"The `zip()` function turns separate pieces of related data into one powerful stream of information."** 🐍📚
# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 20: `zip()`

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what `zip()` is.
* [ ] Understand why `zip()` is useful.
* [ ] Understand the syntax of `zip()`.
* [ ] Combine two sequences using `zip()`.
* [ ] Combine multiple sequences using `zip()`.
* [ ] Iterate over zipped data using a `for` loop.
* [ ] Understand how `zip()` handles sequences of different lengths.
* [ ] Convert `zip()` objects into lists.
* [ ] Convert `zip()` objects into tuples.
* [ ] Create dictionaries using `zip()`.
* [ ] Use `zip()` with `dict()`.
* [ ] Unzip data using `zip(*)`.
* [ ] Use `zip()` with lists.
* [ ] Use `zip()` with tuples.
* [ ] Use `zip()` with strings.
* [ ] Use `zip()` with loops and conditions.
* [ ] Use `zip()` with `enumerate()`.
* [ ] Use `zip()` with dictionary methods.
* [ ] Use `zip()` in real-world applications.
* [ ] Avoid common mistakes when using `zip()`.
* [ ] Solve advanced problems using `zip()`.

---

# 📖 1. What is `zip()`?

`zip()` is a built-in Python function used to combine elements from two or more iterables.

It takes the first element from each iterable and combines them together.

Then it takes the second element from each iterable and combines them together.

Example:

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

result = zip(names, ages)

print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21), ('Riya', 19)]
```

Here:

```text
names → first iterable
ages  → second iterable
zip() → combines corresponding elements
```

---

# 🧠 2. Why Do We Use `zip()`?

Suppose you have two related lists:

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]
```

You may want to process them together.

Without `zip()`:

```python
for i in range(len(students)):
    print(students[i], marks[i])
```

With `zip()`:

```python
for student, mark in zip(students, marks):
    print(student, mark)
```

Output:

```text
Asha 90
Neha 85
Riya 88
```

`zip()` makes the code cleaner and easier to understand.

---

# 📚 3. Syntax of `zip()`

The general syntax is:

```python
zip(iterable1, iterable2, iterable3, ...)
```

Example:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

result = zip(names, marks)

print(list(result))
```

The important point is:

```text
zip()
 ↓
Combines corresponding elements
```

---

# 🔗 4. Combining Two Lists

You can combine two lists using `zip()`.

```python
names = ["Asha", "Neha", "Riya"]
courses = ["BCA", "BBA", "BCom"]

combined = zip(names, courses)

print(list(combined))
```

Output:

```text
[('Asha', 'BCA'), ('Neha', 'BBA'), ('Riya', 'BCom')]
```

The first elements are combined:

```text
Asha + BCA
```

The second elements are combined:

```text
Neha + BBA
```

The third elements are combined:

```text
Riya + BCom
```

---

# 🧩 5. Understanding the Pairing

Consider:

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]
```

When using:

```python
zip(names, ages)
```

Python pairs them like this:

```text
Asha  → 20
Neha  → 21
Riya  → 19
```

The resulting structure is:

```text
('Asha', 20)
('Neha', 21)
('Riya', 19)
```

Each pair is a tuple.

---

# 🔄 6. Using `zip()` with a `for` Loop

One of the most common uses of `zip()` is inside a `for` loop.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for name, mark in zip(names, marks):
    print(name, ":", mark)
```

Output:

```text
Asha : 90
Neha : 85
Riya : 88
```

Here:

```text
name → receives an element from names
mark → receives the corresponding element from marks
```

---

# 🧠 7. `zip()` Returns a Zip Object

When you directly print `zip()`, you do not normally see the combined values.

```python
names = ["Asha", "Neha"]
ages = [20, 21]

result = zip(names, ages)

print(result)
```

Typical output:

```text
<zip object at 0x...>
```

This is because `zip()` returns a **zip object**.

To see its contents, convert it to a list:

```python
print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21)]
```

---

# 📋 8. Converting `zip()` to a List

You can convert a zip object into a list.

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

result = zip(names, ages)

data = list(result)

print(data)
```

Output:

```text
[('Asha', 20), ('Neha', 21), ('Riya', 19)]
```

The structure becomes:

```text
list
 ↓
tuples
 ↓
(key-like value pairs)
```

---

# 🔢 9. Converting `zip()` to a Tuple

You can also convert the result into a tuple.

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

result = zip(names, ages)

data = tuple(result)

print(data)
```

Output:

```text
(('Asha', 20), ('Neha', 21), ('Riya', 19))
```

---

# 📏 10. `zip()` with Equal-Length Iterables

When all iterables have the same length, every element gets paired.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

print(list(zip(names, marks)))
```

Output:

```text
[('Asha', 90), ('Neha', 85), ('Riya', 88)]
```

There are three elements in each iterable, so there are three pairs.

---

# ⚠️ 11. `zip()` with Different-Length Iterables

If the iterables have different lengths, normal `zip()` stops when the **shortest iterable** is exhausted.

Example:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85]

print(list(zip(names, marks)))
```

Output:

```text
[('Asha', 90), ('Neha', 85)]
```

The `"Riya"` element is not included.

Remember:

```text
zip()
 ↓
Stops at the shortest iterable
```

---

# 🧠 12. Understanding the Shortest Iterable Rule

Consider:

```python
a = [1, 2, 3, 4]
b = ["A", "B"]
```

Using:

```python
zip(a, b)
```

produces:

```text
(1, 'A')
(2, 'B')
```

The remaining elements:

```text
3
4
```

are ignored because `b` has no more elements.

---

# 🔗 13. Combining Three Lists

`zip()` can combine more than two iterables.

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]
courses = ["BCA", "BBA", "BCom"]

result = zip(names, ages, courses)

print(list(result))
```

Output:

```text
[
    ('Asha', 20, 'BCA'),
    ('Neha', 21, 'BBA'),
    ('Riya', 19, 'BCom')
]
```

Each tuple contains three values.

---

# 🔢 14. Combining Multiple Lists

You can use several iterables with `zip()`.

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 85, 88]
sql_marks = [85, 80, 90]
git_marks = [88, 82, 86]

data = zip(students, python_marks, sql_marks, git_marks)

for student, python, sql, git in data:
    print(student, python, sql, git)
```

Output:

```text
Asha 90 85 88
Neha 85 80 82
Riya 88 90 86
```

---

# 🧩 15. `zip()` with Strings

Strings are iterable, so they can also be used with `zip()`.

```python
letters = "ABC"
numbers = "123"

print(list(zip(letters, numbers)))
```

Output:

```text
[('A', '1'), ('B', '2'), ('C', '3')]
```

Each character is treated as an individual element.

---

# 🔁 16. `zip()` with Tuples

`zip()` works with tuples too.

```python
names = ("Asha", "Neha", "Riya")
ages = (20, 21, 19)

result = zip(names, ages)

print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21), ('Riya', 19)]
```

`zip()` works with many iterable types, not only lists.

---

# 🏗️ 17. Creating a Dictionary Using `zip()`

One of the most useful applications of `zip()` is creating dictionaries.

Suppose:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]
```

You can create a dictionary:

```python
marks_dict = dict(zip(names, marks))

print(marks_dict)
```

Output:

```text
{'Asha': 90, 'Neha': 85, 'Riya': 88}
```

Here:

```text
names → keys
marks → values
```

---

# 🔑 18. `dict()` + `zip()`

The pattern:

```python
dict(zip(keys, values))
```

is extremely useful.

Example:

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

result = dict(zip(subjects, marks))

print(result)
```

Output:

```text
{'Python': 90, 'SQL': 85, 'Git': 88}
```

Remember:

```text
zip()
 ↓
Creates pairs

dict()
 ↓
Converts pairs into a dictionary
```

---

# 🧠 19. Using `zip()` to Combine Two Lists into a Dictionary

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [55000, 800, 1500]

product_prices = dict(zip(products, prices))

print(product_prices)
```

Output:

```text
{'Laptop': 55000, 'Mouse': 800, 'Keyboard': 1500}
```

This is a very common real-world pattern.

---

# 🔄 20. Looping Through a Dictionary Created with `zip()`

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

result = dict(zip(subjects, marks))

for subject, mark in result.items():
    print(subject, ":", mark)
```

Output:

```text
Python : 90
SQL : 85
Git : 88
```

Here `zip()` and `items()` work together.

---

# 🧩 21. Using `zip()` with Conditions

You can combine `zip()` with `if`.

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 65, 88]

for student, mark in zip(students, marks):
    if mark >= 80:
        print(student, ":", mark)
```

Output:

```text
Asha : 90
Riya : 88
```

This allows you to process related data while applying conditions.

---

# 🔢 22. Calculating Totals Using `zip()`

Suppose students have marks in two subjects.

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 80, 85]
sql_marks = [85, 75, 90]

for student, python, sql in zip(students, python_marks, sql_marks):
    total = python + sql
    print(student, ":", total)
```

Output:

```text
Asha : 175
Neha : 155
Riya : 175
```

---

# 📊 23. Calculating Averages Using `zip()`

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 80, 85]
sql_marks = [85, 75, 90]

for student, python, sql in zip(students, python_marks, sql_marks):
    average = (python + sql) / 2
    print(student, ":", average)
```

Output:

```text
Asha : 87.5
Neha : 77.5
Riya : 87.5
```

---

# 🔍 24. Finding the Highest Value Using `zip()`

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 85, 95]

highest = 0
top_student = ""

for student, mark in zip(students, marks):
    if mark > highest:
        highest = mark
        top_student = student

print("Top Student:", top_student)
print("Marks:", highest)
```

Output:

```text
Top Student: Riya
Marks: 95
```

---

# 🔄 25. Using `zip()` with `enumerate()`

You can combine `enumerate()` and `zip()`.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for index, (name, mark) in enumerate(zip(names, marks)):
    print(index, name, mark)
```

Output:

```text
0 Asha 90
1 Neha 85
2 Riya 88
```

Here:

```text
zip()
 ↓
creates pairs

enumerate()
 ↓
adds indexes
```

---

# 🧠 26. Starting `enumerate()` from 1

You can start the index from `1`.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for number, (name, mark) in enumerate(zip(names, marks), start=1):
    print(number, name, mark)
```

Output:

```text
1 Asha 90
2 Neha 85
3 Riya 88
```

This is useful for displaying numbered records.

---

# 🔓 27. Unzipping Data

`zip()` can also be used to reverse the pairing process.

Suppose:

```python
data = [
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
]
```

You can unzip it using:

```python
names, marks = zip(*data)

print(names)
print(marks)
```

Output:

```text
('Asha', 'Neha', 'Riya')
(90, 85, 88)
```

The `*` operator unpacks the pairs.

---

# 🧠 28. Understanding `zip(*)`

Consider:

```python
data = [
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
]
```

Using:

```python
zip(*data)
```

is conceptually like:

```python
zip(
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
)
```

The result separates the first values from the second values.

Therefore:

```text
First column  → names
Second column → marks
```

---

# 🔄 29. Recreating Original Lists After Unzipping

```python
data = [
    ("Asha", 90),
    ("Neha", 85),
    ("Riya", 88)
]

names, marks = zip(*data)

names = list(names)
marks = list(marks)

print(names)
print(marks)
```

Output:

```text
['Asha', 'Neha', 'Riya']
[90, 85, 88]
```

---

# 🧩 30. Using `zip()` with Dictionary Keys

You can combine dictionary keys with another iterable.

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

values = ["Asha", 20, "BCA"]

for key, value in zip(student.keys(), values):
    print(key, ":", value)
```

Output:

```text
name : Asha
age : 20
course : BCA
```

---

# 🔗 31. Using `zip()` with Dictionary Values

You can also combine two sets of values.

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

for subject, mark in zip(subjects, marks):
    print(subject, "→", mark)
```

Output:

```text
Python → 90
SQL → 85
Git → 88
```

This is one of the most common uses of `zip()`.

---

# 🏗️ 32. Creating Employee Records Using `zip()`

```python
fields = ["id", "name", "department", "salary"]
values = [101, "Neha", "Development", 45000]

employee = dict(zip(fields, values))

print(employee)
```

Output:

```text
{
    'id': 101,
    'name': 'Neha',
    'department': 'Development',
    'salary': 45000
}
```

This is useful when data is received separately.

---

# 🛒 33. Real-World Example: Shopping Cart

Suppose product names and prices are stored separately.

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [55000, 800, 1500]

cart = dict(zip(products, prices))

total = 0

for price in cart.values():
    total += price

print("Cart:", cart)
print("Total:", total)
```

Output:

```text
Cart: {'Laptop': 55000, 'Mouse': 800, 'Keyboard': 1500}
Total: 57300
```

---

# 🎓 34. Real-World Example: Student Marks

```python
subjects = ["Python", "SQL", "Git", "HTML"]
marks = [90, 85, 80, 88]

student_marks = dict(zip(subjects, marks))

for subject, mark in student_marks.items():
    print(subject, ":", mark)
```

Output:

```text
Python : 90
SQL : 85
Git : 80
HTML : 88
```

---

# 👨‍💼 35. Real-World Example: Employee Information

```python
fields = [
    "employee_id",
    "name",
    "department",
    "salary"
]

values = [
    101,
    "Neha",
    "Development",
    45000
]

employee = dict(zip(fields, values))

print(employee)
```

Output:

```text
{
    'employee_id': 101,
    'name': 'Neha',
    'department': 'Development',
    'salary': 45000
}
```

---

# 📦 36. Real-World Example: Product Inventory

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [5, 15, 10, 7]

inventory = dict(zip(products, stock))

for product, quantity in inventory.items():
    if quantity < 10:
        print(product, "needs restocking")
```

Output:

```text
Laptop needs restocking
Monitor needs restocking
```

---

# 💰 37. Real-World Example: Product Prices

```python
products = ["Laptop", "Phone", "Tablet"]
prices = [55000, 30000, 20000]

for product, price in zip(products, prices):
    if price > 25000:
        print(product, ":", price)
```

Output:

```text
Laptop : 55000
Phone : 30000
```

---

# 🌍 38. Real-World Example: City Temperatures

```python
cities = ["Bengaluru", "Mumbai", "Delhi"]
temperatures = [26, 30, 34]

for city, temperature in zip(cities, temperatures):
    print(city, ":", temperature, "°C")
```

Output:

```text
Bengaluru : 26 °C
Mumbai : 30 °C
Delhi : 34 °C
```

---

# 🔢 39. Real-World Example: Student Result Processing

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 65, 82]

for student, mark in zip(students, marks):
    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    else:
        result = "Needs Improvement"

    print(student, ":", result)
```

Output:

```text
Asha : Excellent
Neha : Good
Riya : Excellent
```

---

# ⚠️ 40. Common Mistake: Printing the Zip Object

Wrong assumption:

```python
names = ["Asha", "Neha"]
ages = [20, 21]

result = zip(names, ages)

print(result)
```

Output will look similar to:

```text
<zip object at 0x...>
```

This does not mean `zip()` failed.

Correct:

```python
print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21)]
```

---

# ⚠️ 41. Common Mistake: Reusing an Exhausted Zip Object

A zip object is an iterator.

Example:

```python
names = ["Asha", "Neha"]
ages = [20, 21]

result = zip(names, ages)

print(list(result))
print(list(result))
```

Output:

```text
[('Asha', 20), ('Neha', 21)]
[]
```

Why?

Because the zip object has already been consumed.

Remember:

```text
First use
   ↓
Data available

Second use
   ↓
Zip object already exhausted
```

If you need the data multiple times, store it:

```python
result = list(zip(names, ages))

print(result)
print(result)
```

---

# ⚠️ 42. Common Mistake: Different Lengths

Consider:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85]

print(list(zip(names, marks)))
```

Output:

```text
[('Asha', 90), ('Neha', 85)]
```

`Riya` is not included.

Remember:

```text
zip()
 ↓
Stops at shortest iterable
```

---

# 🧠 43. `zip()` vs `range(len())`

Traditional approach:

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

for i in range(len(names)):
    print(names[i], marks[i])
```

Using `zip()`:

```python
for name, mark in zip(names, marks):
    print(name, mark)
```

The second approach is generally cleaner when you simply need corresponding elements.

---

# ⚖️ 44. `zip()` vs Manual Indexing

| Approach                | Purpose                           |
| ----------------------- | --------------------------------- |
| `range(len())`          | Work with indexes                 |
| `zip()`                 | Work with corresponding values    |
| `enumerate()`           | Work with index + value           |
| `zip()` + `enumerate()` | Work with index + multiple values |

Example:

```python
for name, mark in zip(names, marks):
    print(name, mark)
```

is easier to read than manually accessing:

```python
names[i]
marks[i]
```

---

# 🧩 45. Using `zip()` with List Comprehension

You can use `zip()` inside a list comprehension.

```python
names = ["Asha", "Neha", "Riya"]
marks = [90, 85, 88]

result = [name + " : " + str(mark)
          for name, mark in zip(names, marks)]

print(result)
```

Output:

```text
['Asha : 90', 'Neha : 85', 'Riya : 88']
```

---

# 🔥 46. Advanced Example: Filtering with List Comprehension

```python
names = ["Asha", "Neha", "Riya", "Diya"]
marks = [90, 65, 88, 72]

result = [
    (name, mark)
    for name, mark in zip(names, marks)
    if mark >= 80
]

print(result)
```

Output:

```text
[('Asha', 90), ('Riya', 88)]
```

---

# 🏆 47. Advanced Example: Creating a Dictionary with a Condition

```python
subjects = ["Python", "SQL", "Git", "HTML"]
marks = [90, 65, 88, 72]

result = {
    subject: mark
    for subject, mark in zip(subjects, marks)
    if mark >= 80
}

print(result)
```

Output:

```text
{'Python': 90, 'Git': 88}
```

This combines:

```text
zip()
+
dictionary comprehension
+
condition
```

---

# 📊 48. Advanced Example: Comparing Two Lists

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 82, 90]

for student, old, new in zip(students, old_marks, new_marks):
    difference = new - old
    print(student, ":", difference)
```

Output:

```text
Asha : 10
Neha : 2
Riya : 5
```

This can be useful for comparing performance.

---

# 🧠 49. Advanced Example: Finding Improved Students

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 78, 90]

for student, old, new in zip(students, old_marks, new_marks):
    if new > old:
        print(student, "improved")
```

Output:

```text
Asha improved
Riya improved
```

---

# 💻 50. Practice Programs

## 🟢 Easy

### Program 1: Combine Two Lists

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]

print(list(zip(names, ages)))
```

---

### Program 2: Display Two Lists Together

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

for subject, mark in zip(subjects, marks):
    print(subject, mark)
```

---

### Program 3: Convert `zip()` to a List

```python
products = ["Laptop", "Mouse", "Keyboard"]
prices = [55000, 800, 1500]

result = zip(products, prices)

print(list(result))
```

---

### Program 4: Combine Three Lists

```python
names = ["Asha", "Neha", "Riya"]
ages = [20, 21, 19]
courses = ["BCA", "BBA", "BCom"]

for name, age, course in zip(names, ages, courses):
    print(name, age, course)
```

---

# 🟡 Medium

### Program 5: Create a Dictionary Using `zip()`

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 88]

result = dict(zip(subjects, marks))

print(result)
```

---

### Program 6: Calculate Total Marks

```python
students = ["Asha", "Neha", "Riya"]
python_marks = [90, 80, 85]
sql_marks = [85, 75, 90]

for student, python, sql in zip(students, python_marks, sql_marks):
    total = python + sql
    print(student, ":", total)
```

---

### Program 7: Display Passing Students

```python
students = ["Asha", "Neha", "Riya"]
marks = [90, 55, 82]

for student, mark in zip(students, marks):
    if mark >= 60:
        print(student, ":", mark)
```

---

### Program 8: Create an Employee Dictionary

```python
fields = ["id", "name", "department", "salary"]
values = [101, "Neha", "Development", 45000]

employee = dict(zip(fields, values))

print(employee)
```

---

# 🔴 Advanced

## Program 9: Compare Old and New Marks

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 78, 90]

for student, old, new in zip(students, old_marks, new_marks):
    difference = new - old
    print(student, ":", difference)
```

Output:

```text
Asha : 10
Neha : -2
Riya : 5
```

---

## Program 10: Find Students Who Improved

```python
students = ["Asha", "Neha", "Riya"]
old_marks = [75, 80, 85]
new_marks = [85, 78, 90]

for student, old, new in zip(students, old_marks, new_marks):
    if new > old:
        print(student, "improved")
```

Output:

```text
Asha improved
Riya improved
```

---

## Program 11: Product Inventory

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [5, 15, 10, 7]

inventory = dict(zip(products, stock))

for product, quantity in inventory.items():
    if quantity < 10:
        print(product, "needs restocking")
```

Output:

```text
Laptop needs restocking
Monitor needs restocking
```

---

## Program 12: Student Result Processing

```python
students = ["Asha", "Neha", "Riya"]
marks = [92, 68, 81]

for student, mark in zip(students, marks):
    if mark >= 80:
        result = "Excellent"
    elif mark >= 60:
        result = "Good"
    else:
        result = "Needs Improvement"

    print(student, ":", result)
```

---

# 🏆 51. Challenge

Create three lists:

```text
students
Python marks
SQL marks
```

Example:

```python
students = ["Asha", "Neha", "Riya", "Diya"]

python_marks = [90, 75, 88, 65]

sql_marks = [85, 80, 92, 70]
```

Then:

1. Use `zip()` to combine the student names and marks.
2. Display every student's Python and SQL marks.
3. Calculate the total marks for each student.
4. Calculate the average marks.
5. Display only students whose average is greater than or equal to `80`.
6. Find the student with the highest total.
7. Create a dictionary containing student names and total marks.
8. Display the final dictionary.

Try solving the challenge without copying a solution.

---

# 🧪 52. Mini Project: Student Performance System

Create a student performance system using `zip()`.

Use:

```python
students = ["Asha", "Neha", "Riya", "Diya"]

python_marks = [90, 75, 88, 65]

sql_marks = [85, 80, 92, 70]

git_marks = [88, 78, 85, 72]
```

Perform the following operations:

* Combine all student information using `zip()`.
* Display each student's marks.
* Calculate total marks.
* Calculate average marks.
* Determine whether the student passed or failed.
* Display students whose average is greater than or equal to `80`.
* Find the highest-scoring student.
* Create a dictionary containing student names and their total marks.
* Display the final dictionary.

### Your Goal

Build a complete student performance program using:

```text
zip()
for loop
if / elif / else
dict()
dictionary methods
```

---

# 🎤 53. Interview Questions

* [ ] What is `zip()` in Python?
* [ ] Why is `zip()` used?
* [ ] What is the syntax of `zip()`?
* [ ] What does `zip()` return?
* [ ] How do you convert a zip object into a list?
* [ ] How do you convert a zip object into a tuple?
* [ ] Can `zip()` combine more than two iterables?
* [ ] What happens when iterables have different lengths?
* [ ] Which iterable determines the length of the result?
* [ ] Can `zip()` work with strings?
* [ ] Can `zip()` work with tuples?
* [ ] How can you create a dictionary using `zip()`?
* [ ] What is the purpose of `dict(zip(keys, values))`?
* [ ] How do you loop through a `zip()` object?
* [ ] Can `zip()` be used with conditions?
* [ ] Can `zip()` be used with `enumerate()`?
* [ ] What does `zip(*)` do?
* [ ] What does the `*` operator do when used with `zip()`?
* [ ] What happens when a zip object is used a second time?
* [ ] Is `zip()` lazy or does it immediately create a list?
* [ ] What is the difference between `zip()` and manual indexing?
* [ ] How can `zip()` be used in real-world applications?
* [ ] How can `zip()` be combined with dictionary comprehension?

---

# 📝 54. Assignment

Complete the following programs.

### Task 1

Create two lists:

```text
names
ages
```

Use `zip()` to combine them.

---

### Task 2

Create two lists containing subjects and marks.

Use `zip()` to display every subject and its marks.

---

### Task 3

Create two lists and convert their zipped result into a list.

---

### Task 4

Create three lists containing:

```text
student names
ages
courses
```

Use `zip()` to display all three values.

---

### Task 5

Create two lists:

```text
products
prices
```

Use:

```python
dict(zip(products, prices))
```

to create a product-price dictionary.

---

### Task 6

Create student names and marks.

Use `zip()` and an `if` statement to display students whose marks are greater than `80`.

---

### Task 7

Create two lists containing old marks and new marks.

Use `zip()` to find students whose marks have improved.

---

### Task 8

Create a list of tuples and use:

```python
zip(*data)
```

to unzip the data.

---

### Task 9

Use `zip()` with `enumerate()` to display:

```text
1. Student
2. Student
3. Student
```

along with their marks.

---

### Task 10

Use `zip()` to create a dictionary containing five programming skills and their levels.

Example:

```text
Python → Advanced
SQL → Intermediate
Git → Intermediate
HTML → Advanced
CSS → Beginner
```

---

### Task 11

Create a real-world program that uses at least three iterables with `zip()`.

---

### Task 12

Create a program that uses:

```text
zip()
for
if
dict()
```

to process and display selected records.

---

# 🧠 55. Memory Tricks

Remember:

```text
zip()
 ↓
Combine corresponding values
```

---

Remember the basic pattern:

```text
list1       list2
 ↓            ↓
A            10
B            20
C            30
 ↓            ↓
     zip()
       ↓
(A, 10)
(B, 20)
(C, 30)
```

---

Remember creating a dictionary:

```text
keys
 ↓
zip()
 ↑
values
 ↓
dict()
 ↓
dictionary
```

Pattern:

```python
dict(zip(keys, values))
```

---

Remember unzipping:

```text
pairs
 ↓
zip(*pairs)
 ↓
separate values
```

---

Remember the length rule:

```text
Different lengths
       ↓
zip()
       ↓
Stops at shortest iterable
```

---

Remember:

```text
zip()       → Combine
list(zip()) → Convert to list
dict(zip()) → Create dictionary
zip(*)      → Unzip
```

---

# 📌 56. Important Rules to Remember

```text
1. zip() is a built-in Python function.

2. zip() combines corresponding elements from iterables.

3. zip() can accept two or more iterables.

4. zip() returns a zip object.

5. The zip object is an iterator.

6. Convert a zip object to a list using list().

7. Convert a zip object to a tuple using tuple().

8. zip() stops when the shortest iterable is exhausted.

9. zip() can work with lists, tuples, strings, and other iterables.

10. Each result from zip() is represented as a tuple.

11. zip() is commonly used with for loops.

12. dict(zip(keys, values)) can create a dictionary.

13. zip() can be combined with conditions.

14. zip() can be combined with enumerate().

15. zip(*) can be used to unzip data.

16. A zip object is consumed after iteration.

17. Store list(zip(...)) if the data needs to be reused.

18. zip() is useful for processing related data together.

19. zip() can simplify code that would otherwise use indexes.

20. zip() is commonly used in real-world data processing.
```

---

# 📊 57. `zip()` Structure

```text
                         zip()
                           │
                           ↓
                  Combine Iterables
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       List 1            List 2           List 3
          │                │                │
          ↓                ↓                ↓
          A               10              X
          B               20              Y
          C               30              Z
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                       zip(...)
                           │
                           ↓
                 ┌─────────────────┐
                 │  (A,10,X)       │
                 │  (B,20,Y)       │
                 │  (C,30,Z)       │
                 └─────────────────┘
                           │
            ┌──────────────┼──────────────┐
            ↓              ↓              ↓
        list(zip())    dict(zip())     zip(*data)
            ↓              ↓              ↓
          List         Dictionary        Unzip
```

---

# 📚 58. Complete `zip()` Cheat Sheet

### Combine Two Lists

```python
zip(names, marks)
```

### Convert to List

```python
list(zip(names, marks))
```

### Convert to Tuple

```python
tuple(zip(names, marks))
```

### Combine Three Lists

```python
zip(names, ages, courses)
```

### Loop Through Zipped Data

```python
for name, mark in zip(names, marks):
    print(name, mark)
```

### Create Dictionary

```python
dict(zip(subjects, marks))
```

### Use with Condition

```python
for name, mark in zip(names, marks):
    if mark >= 80:
        print(name)
```

### Use with `enumerate()`

```python
for index, (name, mark) in enumerate(zip(names, marks)):
    print(index, name, mark)
```

### Unzip Data

```python
names, marks = zip(*data)
```

### Convert Unzipped Data to Lists

```python
names, marks = zip(*data)

names = list(names)
marks = list(marks)
```

### Dictionary Comprehension with `zip()`

```python
result = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}
```

---

# 🏆 59. `zip()` Mastery

```text
                         zip()
                           │
                           ↓
                  Combine Iterables
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
    Two Lists          Multiple Lists       Strings/Tuples
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ↓
                       zip object
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
           list()        dict()        tuple()
             │             │             │
             ↓             ↓             ↓
           List       Dictionary       Tuple
                           │
                           ↓
                       Processing
                           │
              ┌────────────┼────────────┐
              ↓            ↓            ↓
             for          if       enumerate()
              │            │            │
              └────────────┼────────────┘
                           ↓
                      Real-World Data
                           │
       ┌───────────────────┼───────────────────┐
       ↓                   ↓                   ↓
    Students            Products            Employees
```

---

# 📚 60. Summary

In this lesson, you learned:

* What `zip()` is.
* Why `zip()` is useful.
* How to use the `zip()` function.
* The syntax of `zip()`.
* How to combine two iterables.
* How to combine multiple iterables.
* How to use `zip()` with lists.
* How to use `zip()` with tuples.
* How to use `zip()` with strings.
* How to iterate through a zip object.
* How to convert a zip object into a list.
* How to convert a zip object into a tuple.
* How `zip()` handles different-length iterables.
* Why `zip()` stops at the shortest iterable.
* How to create dictionaries using `dict(zip())`.
* How to use `zip()` with dictionary methods.
* How to use `zip()` with conditions.
* How to use `zip()` with `enumerate()`.
* How to calculate totals using `zip()`.
* How to calculate averages using `zip()`.
* How to compare two sets of data.
* How to find improved values using `zip()`.
* How to unzip data using `zip(*)`.
* How to use `zip()` with list comprehensions.
* How to use `zip()` with dictionary comprehensions.
* How to use `zip()` in real-world programs.
* Common mistakes when using `zip()`.
* How zip objects behave as iterators.
* How to solve advanced problems using `zip()`.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `zip()` is.
* [ ] I understand why `zip()` is useful.
* [ ] I know the syntax of `zip()`.
* [ ] I can combine two lists using `zip()`.
* [ ] I can combine multiple lists using `zip()`.
* [ ] I can use `zip()` with a `for` loop.
* [ ] I understand the zip object.
* [ ] I can convert a zip object into a list.
* [ ] I can convert a zip object into a tuple.
* [ ] I understand what happens when iterables have different lengths.
* [ ] I understand the shortest iterable rule.
* [ ] I can use `zip()` with strings.
* [ ] I can use `zip()` with tuples.
* [ ] I can create dictionaries using `dict(zip())`.
* [ ] I can use `zip()` with conditions.
* [ ] I can use `zip()` with `enumerate()`.
* [ ] I can calculate totals using `zip()`.
* [ ] I can calculate averages using `zip()`.
* [ ] I can compare two lists using `zip()`.
* [ ] I understand `zip(*)`.
* [ ] I can unzip data.
* [ ] I can use `zip()` with list comprehensions.
* [ ] I can use `zip()` with dictionary comprehensions.
* [ ] I understand that zip objects are iterators.
* [ ] I understand that zip objects can be exhausted.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the mini project.
* [ ] I completed the assignment.
* [ ] I can use `zip()` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Advanced Function Concepts**

In the next topic, you will learn:

* Function arguments in depth.
* Positional arguments.
* Keyword arguments.
* Default arguments.
* Variable-length arguments.
* `*args`.
* `**kwargs`.
* Argument unpacking.
* Positional-only parameters.
* Keyword-only parameters.
* Combining different parameter types.
* Function return values.
* Multiple return values.
* Nested functions.
* Scope of variables.
* Local and global variables.
* `global` keyword.
* `nonlocal` keyword.
* Functions as objects.
* Passing functions as arguments.
* Returning functions.
* Higher-order functions.
* Practical real-world examples.
* Common mistakes.
* Advanced function techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"The `zip()` function turns separate pieces of related data into one powerful stream of information."** 🐍📚
