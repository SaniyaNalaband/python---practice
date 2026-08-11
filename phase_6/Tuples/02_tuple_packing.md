# 🐍 Python Master Course

# 📦 Phase 6: Collections – Tuples

## 📌 Topic 2: Tuple Packing

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand Tuple Packing.
- [ ] Understand how Python automatically creates tuples.
- [ ] Pack multiple values into one tuple.
- [ ] Pack values without parentheses.
- [ ] Pack values of different data types.
- [ ] Pack variables into a tuple.
- [ ] Understand the relationship between packing and unpacking.
- [ ] Use Tuple Packing in real-world programs.
- [ ] Identify common mistakes with Tuple Packing.

---

# 📖 What is Tuple Packing?

**Tuple Packing** is the process of putting multiple values into a single tuple.

Python automatically groups multiple comma-separated values into a tuple.

### Example

```python
student = "Saniya", 21, 90

print(student)
```

Output:

```text
('Saniya', 21, 90)
```

Even though we did not explicitly use parentheses, Python created a tuple.

---

# 📌 Basic Syntax

```python
tuple_name = value1, value2, value3
```

Example:

```python
numbers = 10, 20, 30
```

Python packs these values into:

```text
(10, 20, 30)
```

---

# 🧠 How Tuple Packing Works

Consider:

```python
numbers = 10, 20, 30
```

Python sees:

```text
10 , 20 , 30
```

The commas separate the values.

Python packs them into:

```text
(10, 20, 30)
```

Therefore:

```python
print(type(numbers))
```

Output:

```text
<class 'tuple'>
```

---

# 📌 Tuple Packing with Parentheses

You can explicitly use parentheses:

```python
numbers = (10, 20, 30)
```

This is also Tuple Packing.

```python
print(numbers)
```

Output:

```text
(10, 20, 30)
```

---

# 📌 Packing Without Parentheses

Parentheses are not required in many situations.

```python
numbers = 10, 20, 30
```

Output:

```text
(10, 20, 30)
```

Both are valid:

```python
numbers1 = (10, 20, 30)

numbers2 = 10, 20, 30
```

---

# 📊 Compare Both

| Code | Result |
|---|---|
| `(10, 20, 30)` | Tuple |
| `10, 20, 30` | Tuple |
| `(10)` | Integer |
| `(10,)` | Tuple |

The comma is extremely important.

---

# 📌 Example 1: Packing Numbers

```python
numbers = 10, 20, 30, 40, 50

print(numbers)
print(type(numbers))
```

Output:

```text
(10, 20, 30, 40, 50)
<class 'tuple'>
```

---

# 📌 Example 2: Packing Strings

```python
languages = "Python", "Java", "C", "JavaScript"

print(languages)
```

Output:

```text
('Python', 'Java', 'C', 'JavaScript')
```

---

# 📌 Example 3: Packing Different Data Types

A tuple can contain different data types.

```python
data = "Python", 10, 3.14, True, None

print(data)
```

Output:

```text
('Python', 10, 3.14, True, None)
```

Python packs all these values into one tuple.

---

# 📌 Example 4: Packing Variables

You can pack variables into a tuple.

```python
name = "Saniya"
age = 21
marks = 90

student = name, age, marks

print(student)
```

Output:

```text
('Saniya', 21, 90)
```

Here:

```text
name
age
marks
 ↓
 ↓
 ↓
Single tuple
```

---

# 📌 Example 5: Packing Expressions

Expressions can also be packed.

```python
a = 10
b = 20

result = a, b, a + b

print(result)
```

Output:

```text
(10, 20, 30)
```

The expression:

```python
a + b
```

is evaluated first.

Then Python packs the results:

```text
(10, 20, 30)
```

---

# 📌 Example 6: Packing Boolean Values

```python
status = True, False, True

print(status)
```

Output:

```text
(True, False, True)
```

---

# 📌 Example 7: Packing Lists

A tuple can contain lists.

```python
data = [10, 20], [30, 40]

print(data)
```

Output:

```text
([10, 20], [30, 40])
```

The two lists are packed into a tuple.

---

# 📌 Example 8: Packing Nested Tuples

```python
data = (1, 2), (3, 4), (5, 6)

print(data)
```

Output:

```text
((1, 2), (3, 4), (5, 6))
```

This creates a tuple containing three tuples.

---

# 📌 Example 9: Packing Strings and Numbers

```python
product = "Laptop", 55000, "Electronics"

print(product)
```

Output:

```text
('Laptop', 55000, 'Electronics')
```

This can represent a fixed product record.

---

# 📌 Example 10: Packing Employee Information

```python
employee = 101, "Aisha", "Developer", 45000

print(employee)
```

Output:

```text
(101, 'Aisha', 'Developer', 45000)
```

---

# 📌 The Comma Creates the Tuple

This is one of the most important concepts.

Look at:

```python
value = (10)
```

This is an integer.

```python
print(type(value))
```

Output:

```text
<class 'int'>
```

But:

```python
value = (10,)
```

is a tuple.

```python
print(type(value))
```

Output:

```text
<class 'tuple'>
```

Therefore:

> **In tuple syntax, the comma is more important than the parentheses.**

---

# 📌 Single-Value Tuple Packing

A single value can be packed into a tuple using a comma.

```python
number = 10,

print(number)
print(type(number))
```

Output:

```text
(10,)
<class 'tuple'>
```

Parentheses are not necessary:

```python
number = 10,
```

is equivalent to:

```python
number = (10,)
```

---

# 📌 Multiple-Value Packing

```python
a = 10, 20, 30
```

is equivalent to:

```python
a = (10, 20, 30)
```

Python automatically packs the values.

---

# 🧠 Tuple Packing Diagram

```text
Individual Values
       ↓
  10 , 20 , 30
       ↓
   Tuple Packing
       ↓
 (10, 20, 30)
```

---

# 📌 Tuple Packing with User Input

Suppose we take three values:

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

person = name, age, city

print(person)
```

Example output:

```text
Enter name: Aisha
Enter age: 21
Enter city: Mysuru

('Aisha', 21, 'Mysuru')
```

The three values are packed into one tuple.

---

# 📌 Tuple Packing with Calculations

```python
length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

result = area, perimeter

print(result)
```

Output:

```text
(50, 30)
```

---

# 📌 Tuple Packing in Functions

A function can return multiple values separated by commas.

```python
def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference


result = calculate(20, 10)

print(result)
```

Output:

```text
(30, 10)
```

Python packs the returned values into a tuple.

---

# 🧠 What Happens Here?

This:

```python
return total, difference
```

creates a tuple:

```text
(total, difference)
```

So:

```python
result = calculate(20, 10)
```

gives:

```text
(30, 10)
```

---

# 📌 Multiple Values from a Function

```python
def student_details():
    name = "Saniya"
    age = 21
    marks = 90

    return name, age, marks


student = student_details()

print(student)
```

Output:

```text
('Saniya', 21, 90)
```

The three returned values are packed into a tuple.

---

# 📌 Tuple Packing with Different Objects

```python
data = (
    [1, 2, 3],
    {"name": "Aisha"},
    {10, 20},
    "Python"
)

print(data)
```

Here a tuple contains:

```text
List
Dictionary
Set
String
```

---

# 📌 Packing vs Creating a Tuple

These are essentially the same:

```python
numbers = (10, 20, 30)
```

and:

```python
numbers = 10, 20, 30
```

The second form demonstrates **Tuple Packing** more clearly because Python automatically groups the comma-separated values into a tuple.

---

# 🔄 Packing and Unpacking

Tuple Packing and Tuple Unpacking are opposite operations.

### Packing

Multiple values → One tuple

```text
10, 20, 30
     ↓
  Packing
     ↓
(10, 20, 30)
```

### Unpacking

One tuple → Multiple variables

```text
(10, 20, 30)
      ↓
   Unpacking
      ↓
a = 10
b = 20
c = 30
```

Example:

```python
numbers = 10, 20, 30

a, b, c = numbers

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

> **Tuple Unpacking is the next topic.**

---

# 🌍 Real-World Examples

## Example 1: Student Record

```python
name = "Aisha"
age = 21
course = "BCA"
marks = 88

student = name, age, course, marks

print(student)
```

Output:

```text
('Aisha', 21, 'BCA', 88)
```

---

# 🌍 Example 2: Product Record

```python
product_id = 101
product_name = "Laptop"
price = 55000
category = "Electronics"

product = product_id, product_name, price, category

print(product)
```

Output:

```text
(101, 'Laptop', 55000, 'Electronics')
```

---

# 🌍 Example 3: Coordinates

```python
x = 10
y = 20

point = x, y

print(point)
```

Output:

```text
(10, 20)
```

This represents a coordinate:

```text
(x, y)
```

---

# 🌍 Example 4: RGB Color

```python
red = 255
green = 128
blue = 0

color = red, green, blue

print(color)
```

Output:

```text
(255, 128, 0)
```

---

# 🌍 Example 5: Employee Record

```python
employee_id = 1001
name = "Riya"
department = "IT"
salary = 45000

employee = employee_id, name, department, salary

print(employee)
```

Output:

```text
(1001, 'Riya', 'IT', 45000)
```

---

# 🌍 Example 6: Date

```python
day = 11
month = 8
year = 2026

date = day, month, year

print(date)
```

Output:

```text
(11, 8, 2026)
```

---

# 📌 Tuple Packing with `enumerate()`

`enumerate()` produces pairs containing an index and value.

```python
names = ["Aisha", "Saniya", "Rohan"]

for item in enumerate(names):
    print(item)
```

Output:

```text
(0, 'Aisha')
(1, 'Saniya')
(2, 'Rohan')
```

Each pair is represented as a tuple.

---

# 📌 Tuple Packing with `zip()`

`zip()` groups values together into tuples.

```python
names = ["Aisha", "Saniya", "Rohan"]
marks = [85, 92, 78]

students = list(zip(names, marks))

print(students)
```

Output:

```text
[('Aisha', 85), ('Saniya', 92), ('Rohan', 78)]
```

Each pair:

```text
('Aisha', 85)
```

is a tuple.

---

# 🧠 Important Concepts

## 1. Commas

The comma separates tuple elements.

```python
numbers = 10, 20, 30
```

---

## 2. Parentheses

Parentheses are commonly used to make tuple structure clear.

```python
numbers = (10, 20, 30)
```

---

## 3. Single Element

A comma is required.

```python
number = (10,)
```

---

## 4. Multiple Values

Multiple comma-separated values are automatically packed.

```python
data = "Python", 10, True
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Forgetting the comma

```python
number = (10)
```

This is not a tuple.

Correct:

```python
number = (10,)
```

---

## ❌ Mistake 2: Thinking parentheses alone create a tuple

```python
value = ("Python")
```

This is a string.

Correct:

```python
value = ("Python",)
```

---

## ❌ Mistake 3: Forgetting commas

Incorrect:

```python
numbers = (10 20 30)
```

Correct:

```python
numbers = (10, 20, 30)
```

---

# 📊 Tuple Packing Summary

| Code | Result |
|---|---|
| `x = 10, 20, 30` | Tuple |
| `x = (10, 20, 30)` | Tuple |
| `x = (10)` | Integer |
| `x = (10,)` | Tuple |
| `x = "Python", 10` | Tuple |
| `x = ("Python", 10)` | Tuple |
| `x = 10,` | Single-element tuple |

---

# 🏋️ Practice Programs

## Beginner

### 1. Pack five numbers

```python
numbers = 10, 20, 30, 40, 50

print(numbers)
```

---

### 2. Pack programming languages

```python
languages = "Python", "Java", "C", "C++"

print(languages)
```

---

### 3. Pack different data types

```python
data = "Python", 10, 3.14, True

print(data)
```

---

### 4. Create a single-element tuple

```python
number = 100,

print(number)
```

---

### 5. Pack variables

```python
name = "Aisha"
age = 21
marks = 90

student = name, age, marks

print(student)
```

---

# 🏋️ Intermediate Practice

### 6. Pack product information

```python
product_id = 101
name = "Keyboard"
price = 1200

product = product_id, name, price

print(product)
```

---

### 7. Pack coordinate values

```python
x = 50
y = 100

point = x, y

print(point)
```

---

### 8. Pack calculated values

```python
a = 20
b = 10

result = a + b, a - b, a * b

print(result)
```

Expected output:

```text
(30, 10, 200)
```

---

### 9. Pack function results

```python
def calculate(a, b):
    return a + b, a * b


result = calculate(5, 4)

print(result)
```

Expected output:

```text
(9, 20)
```

---

### 10. Pack student details

```python
name = "Aisha"
age = 21
course = "BCA"
marks = 92

student = name, age, course, marks

print(student)
```

---

# 🚀 Advanced Practice

## Challenge 1: Employee Record

Create an employee tuple by packing:

```text
Employee ID
Name
Department
Salary
Experience
```

Example:

```python
employee_id = 1001
name = "Aisha"
department = "IT"
salary = 45000
experience = 2

employee = employee_id, name, department, salary, experience

print(employee)
```

---

## Challenge 2: Calculate and Pack

Create a program that takes two numbers and packs:

```text
Sum
Difference
Product
Division
```

Example:

```python
a = 20
b = 5

result = (
    a + b,
    a - b,
    a * b,
    a / b
)

print(result)
```

Output:

```text
(25, 15, 100, 4.0)
```

---

## Challenge 3: Function with Multiple Results

Create a function that returns:

```text
Total
Average
Highest
Lowest
```

Example:

```python
def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest


result = calculate_marks([80, 90, 75, 95])

print(result)
```

Output:

```text
(340, 85.0, 95, 75)
```

The returned values are packed into a tuple.

---

# 🧠 Key Difference

### Tuple Packing

```python
student = "Aisha", 21, 90
```

Multiple values become:

```text
('Aisha', 21, 90)
```

### Tuple Unpacking

```python
student = ("Aisha", 21, 90)

name, age, marks = student
```

One tuple becomes:

```text
name  → Aisha
age   → 21
marks → 90
```

---

# 🎯 Topic Completion Checklist

- [x] I understand Tuple Packing.
- [x] I know that comma-separated values can form a tuple.
- [x] I can pack numbers into a tuple.
- [x] I can pack strings into a tuple.
- [x] I can pack different data types.
- [x] I can pack variables.
- [x] I understand the importance of the comma.
- [x] I understand single-element tuple packing.
- [x] I can pack calculated values.
- [x] I can return multiple values from a function.
- [x] I understand how `zip()` produces tuples.
- [x] I understand how `enumerate()` produces tuples.
- [x] I understand the difference between packing and unpacking.
- [x] I completed the practice programs.
- [x] I completed the challenges.

---

# 📝 Quick Revision

```python
# Tuple packing
numbers = 10, 20, 30

# Explicit tuple packing
numbers = (10, 20, 30)

# Single-element tuple
number = 10,

# Mixed values
data = "Python", 10, 3.14, True

# Packing variables
name = "Aisha"
age = 21
marks = 90

student = name, age, marks

# Function returning multiple values
def calculate(a, b):
    return a + b, a - b

result = calculate(20, 10)
```

---

# 🧠 Remember This

```text
Multiple Values
      ↓
  Comma-Separated
      ↓
Tuple Packing
      ↓
    One Tuple
```

Example:

```python
10, 20, 30
```

becomes:

```python
(10, 20, 30)
```

### ⭐ Most Important Rule

```python
(10)      # int
(10,)     # tuple
```

> **The comma is what makes a single value a tuple.**

---

# 🚀 Next Topic

## 📌 Topic 3: Tuple Unpacking

In the next topic, we will learn:

- [ ] What is Tuple Unpacking?
- [ ] Basic tuple unpacking.
- [ ] Unpacking into multiple variables.
- [ ] Unpacking with different data types.
- [ ] Extended unpacking using `*`.
- [ ] Unpacking nested tuples.
- [ ] Swapping variables using tuple unpacking.
- [ ] Unpacking function results.
- [ ] Real-world examples.
- [ ] Practice programs.
- [ ] Advanced examples.