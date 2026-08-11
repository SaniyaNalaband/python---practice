# 🐍 Python Master Course

# 📦 Phase 6: Collections – Tuples

## 📌 Topic 3: Tuple Unpacking

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand Tuple Unpacking.
- [ ] Unpack tuple elements into variables.
- [ ] Understand how the number of variables must match the number of elements.
- [ ] Unpack tuples containing different data types.
- [ ] Unpack tuples without parentheses.
- [ ] Swap variables using tuple unpacking.
- [ ] Use extended unpacking with `*`.
- [ ] Unpack nested tuples.
- [ ] Unpack values returned from functions.
- [ ] Use unpacking in loops.
- [ ] Use tuple unpacking in real-world programs.
- [ ] Understand common unpacking errors.

---

# 📖 What is Tuple Unpacking?

**Tuple Unpacking** is the process of taking the individual values from a tuple and assigning them to separate variables.

### Example

```python
student = ("Aisha", 21, 90)

name, age, marks = student

print(name)
print(age)
print(marks)
```

Output:

```text
Aisha
21
90
```

Here:

```text
Tuple
("Aisha", 21, 90)
       ↓
   Unpacking
       ↓
name  → "Aisha"
age   → 21
marks → 90
```

---

# 📌 Basic Syntax

```python
variable1, variable2, variable3 = tuple
```

Example:

```python
numbers = (10, 20, 30)

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

---

# 🧠 How Tuple Unpacking Works

Suppose we have:

```python
numbers = (10, 20, 30)
```

Python matches each tuple element with a variable:

```text
10  → a
20  → b
30  → c
```

So:

```python
a, b, c = numbers
```

means:

```python
a = 10
b = 20
c = 30
```

---

# 📌 Example 1: Basic Unpacking

```python
numbers = (10, 20, 30)

x, y, z = numbers

print(x)
print(y)
print(z)
```

Output:

```text
10
20
30
```

---

# 📌 Example 2: String Tuple

```python
languages = ("Python", "Java", "C")

first, second, third = languages

print(first)
print(second)
print(third)
```

Output:

```text
Python
Java
C
```

---

# 📌 Example 3: Different Data Types

```python
student = ("Aisha", 21, 89.5, True)

name, age, marks, status = student

print(name)
print(age)
print(marks)
print(status)
```

Output:

```text
Aisha
21
89.5
True
```

Each variable receives the corresponding value.

---

# 📌 Example 4: Unpacking Without Parentheses

The tuple itself can be written without parentheses.

```python
student = "Aisha", 21, 90

name, age, marks = student

print(name)
print(age)
print(marks)
```

Output:

```text
Aisha
21
90
```

---

# 📌 Number of Variables Must Match

This is an important rule.

Consider:

```python
numbers = (10, 20, 30)
```

There are **3 elements**.

Therefore, we normally need **3 variables**:

```python
a, b, c = numbers
```

---

# ❌ Too Few Variables

```python
numbers = (10, 20, 30)

a, b = numbers
```

Output:

```text
ValueError: too many values to unpack
```

There are three values but only two variables.

---

# ❌ Too Many Variables

```python
numbers = (10, 20, 30)

a, b, c, d = numbers
```

Output:

```text
ValueError: not enough values to unpack
```

There are three values but four variables.

---

# 🧠 The Matching Rule

Normally:

```text
Number of values = Number of variables
```

Example:

```python
a, b, c = (10, 20, 30)
```

```text
3 values = 3 variables ✅
```

But:

```python
a, b = (10, 20, 30)
```

```text
2 variables ≠ 3 values ❌
```

---

# 📌 Example 5: Student Record

```python
student = (
    "Aisha",
    21,
    "BCA",
    92
)

name, age, course, marks = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)
```

Output:

```text
Name: Aisha
Age: 21
Course: BCA
Marks: 92
```

---

# 📌 Example 6: Product Information

```python
product = (
    101,
    "Laptop",
    55000,
    "Electronics"
)

product_id, name, price, category = product

print(product_id)
print(name)
print(price)
print(category)
```

Output:

```text
101
Laptop
55000
Electronics
```

---

# 📌 Example 7: Coordinates

```python
point = (10, 20)

x, y = point

print("X:", x)
print("Y:", y)
```

Output:

```text
X: 10
Y: 20
```

---

# 📌 Example 8: Date

```python
date = (11, 8, 2026)

day, month, year = date

print(day)
print(month)
print(year)
```

Output:

```text
11
8
2026
```

---

# 📌 Example 9: RGB Color

```python
color = (255, 128, 0)

red, green, blue = color

print("Red:", red)
print("Green:", green)
print("Blue:", blue)
```

Output:

```text
Red: 255
Green: 128
Blue: 0
```

---

# 📌 Example 10: Employee Record

```python
employee = (
    1001,
    "Riya",
    "Developer",
    45000
)

employee_id, name, role, salary = employee

print(employee_id)
print(name)
print(role)
print(salary)
```

---

# 🔄 Packing vs Unpacking

Tuple Packing and Tuple Unpacking are opposite processes.

## Tuple Packing

Multiple values → One tuple

```python
student = "Aisha", 21, 90
```

Result:

```text
("Aisha", 21, 90)
```

---

## Tuple Unpacking

One tuple → Multiple variables

```python
student = ("Aisha", 21, 90)

name, age, marks = student
```

Result:

```text
name  → Aisha
age   → 21
marks → 90
```

---

# 📊 Packing vs Unpacking

| Concept | Meaning | Example |
|---|---|---|
| Packing | Multiple values → tuple | `x = 10, 20, 30` |
| Unpacking | Tuple → multiple variables | `a, b, c = x` |

---

# 📌 Unpacking Directly

You do not always need to create the tuple first.

```python
name, age, marks = "Aisha", 21, 90

print(name)
print(age)
print(marks)
```

Output:

```text
Aisha
21
90
```

Python first packs the right side into a tuple and then unpacks it.

Conceptually:

```text
"Aisha", 21, 90
       ↓
    Packing
       ↓
("Aisha", 21, 90)
       ↓
   Unpacking
       ↓
name, age, marks
```

---

# 📌 Swapping Variables

One of the most useful applications of tuple unpacking is swapping values.

Suppose:

```python
a = 10
b = 20
```

We want:

```text
a → 20
b → 10
```

Python allows:

```python
a, b = b, a
```

Example:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

---

# 🧠 How Swapping Works

Before:

```text
a = 10
b = 20
```

Right side:

```python
b, a
```

becomes:

```text
(20, 10)
```

Then Python unpacks it:

```text
a = 20
b = 10
```

So:

```python
a, b = b, a
```

performs both packing and unpacking.

---

# 📌 Traditional Swapping vs Python Swapping

### Traditional approach

```python
a = 10
b = 20

temp = a
a = b
b = temp
```

### Python approach

```python
a = 10
b = 20

a, b = b, a
```

The Python approach is shorter and easier to read.

---

# 📌 Extended Unpacking Using `*`

What if we have more values than variables?

Example:

```python
numbers = (10, 20, 30, 40, 50)

a, *b = numbers

print(a)
print(b)
```

Output:

```text
10
[20, 30, 40, 50]
```

The `*` collects the remaining values into a list.

---

# 🧠 Understanding `*`

```python
a, *b = numbers
```

means:

```text
a → first value
b → remaining values
```

Therefore:

```text
a = 10

b = [20, 30, 40, 50]
```

Notice that the starred variable receives a **list**, not a tuple.

---

# 📌 Example: First and Remaining

```python
numbers = (10, 20, 30, 40, 50)

first, *remaining = numbers

print(first)
print(remaining)
```

Output:

```text
10
[20, 30, 40, 50]
```

---

# 📌 Last Value and Remaining Values

You can use `*` before the last variable.

```python
numbers = (10, 20, 30, 40, 50)

*remaining, last = numbers

print(remaining)
print(last)
```

Output:

```text
[10, 20, 30, 40]
50
```

---

# 📌 First, Middle, and Last

You can also use a starred variable in the middle.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
10
[20, 30, 40]
50
```

---

# 📊 Extended Unpacking Patterns

| Code | Result |
|---|---|
| `a, *b = values` | First + remaining |
| `*a, b = values` | Remaining + last |
| `a, *b, c = values` | First + middle + last |

---

# 📌 Example: Student Marks

```python
marks = (85, 90, 78, 92, 88)

first, *remaining = marks

print("First:", first)
print("Remaining:", remaining)
```

Output:

```text
First: 85
Remaining: [90, 78, 92, 88]
```

---

# 📌 Example: Separate First and Last

```python
marks = (85, 90, 78, 92, 88)

first, *middle, last = marks

print("First:", first)
print("Middle:", middle)
print("Last:", last)
```

Output:

```text
First: 85
Middle: [90, 78, 92]
Last: 88
```

---

# ⚠️ Important Rule for `*`

Only **one starred variable** can be used in a single unpacking assignment.

### ❌ Incorrect

```python
a, *b, *c = numbers
```

This produces a syntax error.

### ✅ Correct

```python
a, *b, c = numbers
```

---

# 📌 Nested Tuple Unpacking

Tuples can contain other tuples.

Example:

```python
student = (
    ("Aisha", 85),
    ("Saniya", 92)
)
```

We can unpack the nested structure.

```python
(first_name, first_marks), (second_name, second_marks) = student

print(first_name)
print(first_marks)

print(second_name)
print(second_marks)
```

Output:

```text
Aisha
85
Saniya
92
```

---

# 📌 Another Nested Example

```python
data = ((10, 20), (30, 40))

(a, b), (c, d) = data

print(a)
print(b)
print(c)
print(d)
```

Output:

```text
10
20
30
40
```

---

# 📌 Unpacking Function Results

Functions can return multiple values.

```python
def calculate(a, b):
    return a + b, a - b


result = calculate(20, 10)

print(result)
```

Output:

```text
(30, 10)
```

We can directly unpack the result:

```python
def calculate(a, b):
    return a + b, a - b


addition, subtraction = calculate(20, 10)

print(addition)
print(subtraction)
```

Output:

```text
30
10
```

---

# 📌 Function Returning Multiple Values

```python
def student_details():
    return "Aisha", 21, 90


name, age, marks = student_details()

print(name)
print(age)
print(marks)
```

Output:

```text
Aisha
21
90
```

---

# 📌 Unpacking in a `for` Loop

Tuple unpacking is commonly used with loops.

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]

for name, marks in students:
    print(name, marks)
```

Output:

```text
Aisha 85
Saniya 92
Rohan 78
```

Each tuple is automatically unpacked during every iteration.

---

# 🧠 How the Loop Works

First iteration:

```text
("Aisha", 85)
      ↓
name = "Aisha"
marks = 85
```

Second iteration:

```text
("Saniya", 92)
      ↓
name = "Saniya"
marks = 92
```

Third iteration:

```text
("Rohan", 78)
      ↓
name = "Rohan"
marks = 78
```

---

# 📌 Unpacking with `enumerate()`

```python
names = ["Aisha", "Saniya", "Rohan"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```text
0 Aisha
1 Saniya
2 Rohan
```

`enumerate()` produces tuples such as:

```text
(0, "Aisha")
(1, "Saniya")
(2, "Rohan")
```

These tuples are unpacked into:

```python
index, name
```

---

# 📌 Unpacking with `zip()`

```python
names = ["Aisha", "Saniya", "Rohan"]
marks = [85, 92, 78]

for name, mark in zip(names, marks):
    print(name, mark)
```

Output:

```text
Aisha 85
Saniya 92
Rohan 78
```

Each `zip()` result is a tuple:

```text
("Aisha", 85)
("Saniya", 92)
("Rohan", 78)
```

---

# 🌍 Real-World Example 1: Student Records

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]

for name, marks in students:
    print(f"{name} scored {marks}")
```

Output:

```text
Aisha scored 85
Saniya scored 92
Rohan scored 78
```

---

# 🌍 Real-World Example 2: Product Records

```python
products = [
    ("Laptop", 55000),
    ("Keyboard", 1200),
    ("Mouse", 800)
]

for product, price in products:
    print(f"{product}: ₹{price}")
```

Output:

```text
Laptop: ₹55000
Keyboard: ₹1200
Mouse: ₹800
```

---

# 🌍 Real-World Example 3: Coordinates

```python
points = [
    (10, 20),
    (30, 40),
    (50, 60)
]

for x, y in points:
    print("X =", x, "Y =", y)
```

Output:

```text
X = 10 Y = 20
X = 30 Y = 40
X = 50 Y = 60
```

---

# 🌍 Real-World Example 4: Employee Records

```python
employees = [
    (101, "Aisha", "Developer"),
    (102, "Saniya", "Designer"),
    (103, "Rohan", "Tester")
]

for employee_id, name, role in employees:
    print(employee_id, name, role)
```

Output:

```text
101 Aisha Developer
102 Saniya Designer
103 Rohan Tester
```

---

# 🌍 Real-World Example 5: Separating Date

```python
date = (11, 8, 2026)

day, month, year = date

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
```

Output:

```text
Day: 11
Month: 8
Year: 2026
```

---

# 📌 Ignoring Values with `_`

Sometimes you don't need every value.

You can use `_` for values you want to ignore.

```python
student = ("Aisha", 21, "BCA", 90)

name, _, course, _ = student

print(name)
print(course)
```

Output:

```text
Aisha
BCA
```

Here:

```text
_ → ignored value
```

---

# 📌 Example: Ignore the Middle Value

```python
data = (10, 20, 30)

first, _, last = data

print(first)
print(last)
```

Output:

```text
10
30
```

The value `20` is ignored.

---

# 📌 Using `*` to Ignore Multiple Values

```python
numbers = (10, 20, 30, 40, 50)

first, *_, last = numbers

print(first)
print(last)
```

Output:

```text
10
50
```

The middle values are collected into `_`.

---

# ⚠️ Common Errors

## ❌ Error 1: Too Many Variables

```python
numbers = (10, 20, 30)

a, b, c, d = numbers
```

Error:

```text
ValueError: not enough values to unpack
```

There are only three values but four variables.

---

# ❌ Error 2: Too Few Variables

```python
numbers = (10, 20, 30)

a, b = numbers
```

Error:

```text
ValueError: too many values to unpack
```

There are three values but only two variables.

---

# ❌ Error 3: Incorrect Nested Structure

```python
data = ((10, 20), (30, 40))

a, b, c, d = data
```

This does not correctly match the nested structure.

Correct:

```python
(a, b), (c, d) = data
```

---

# ❌ Error 4: Multiple Starred Variables

Incorrect:

```python
a, *b, *c = numbers
```

A single unpacking assignment can contain only one starred target.

---

# 📊 Normal vs Extended Unpacking

| Type | Example | Result |
|---|---|---|
| Normal | `a, b, c = (10, 20, 30)` | Each gets one value |
| First + remaining | `a, *b = values` | `a` gets first |
| Remaining + last | `*a, b = values` | `b` gets last |
| First + middle + last | `a, *b, c = values` | `a`, `b`, `c` split values |

---

# 🧠 Important Rules

### Rule 1: Match the number of values

```python
a, b, c = (10, 20, 30)
```

---

### Rule 2: Use `*` for variable-length unpacking

```python
a, *b = (10, 20, 30, 40)
```

---

### Rule 3: Only one `*` is allowed

```python
a, *b, c
```

✅

```python
a, *b, *c
```

❌

---

### Rule 4: `_` can represent an ignored value

```python
a, _, c = (10, 20, 30)
```

---

### Rule 5: Nested structures need matching unpacking

```python
(a, b), (c, d) = ((10, 20), (30, 40))
```

---

# 📊 Tuple Packing and Unpacking Together

```python
# Packing
student = "Aisha", 21, 90

# Unpacking
name, age, marks = student

print(name)
print(age)
print(marks)
```

Output:

```text
Aisha
21
90
```

The complete process:

```text
"Aisha", 21, 90
       ↓
    PACKING
       ↓
("Aisha", 21, 90)
       ↓
  UNPACKING
       ↓
name = "Aisha"
age = 21
marks = 90
```

---

# 🏋️ Practice Programs

## Beginner Practice

### 1. Unpack three numbers

```python
numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)
```

---

### 2. Unpack student details

```python
student = ("Aisha", 21, 90)

name, age, marks = student

print(name)
print(age)
print(marks)
```

---

### 3. Unpack coordinates

```python
point = (50, 100)

x, y = point

print(x)
print(y)
```

---

### 4. Unpack a date

```python
date = (11, 8, 2026)

day, month, year = date

print(day)
print(month)
print(year)
```

---

### 5. Swap two numbers

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

---

# 🏋️ Intermediate Practice

### 6. Use extended unpacking

```python
numbers = (10, 20, 30, 40, 50)

first, *remaining = numbers

print(first)
print(remaining)
```

---

### 7. Extract first and last

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

---

### 8. Ignore a value

```python
student = ("Aisha", 21, "BCA", 90)

name, _, course, _ = student

print(name)
print(course)
```

---

### 9. Unpack nested tuples

```python
data = ((10, 20), (30, 40))

(a, b), (c, d) = data

print(a)
print(b)
print(c)
print(d)
```

---

### 10. Unpack function result

```python
def calculate(a, b):
    return a + b, a * b


total, product = calculate(10, 5)

print(total)
print(product)
```

---

# 🚀 Advanced Practice

## Challenge 1: Student Records

Given:

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]
```

Use tuple unpacking to print:

```text
Aisha scored 85
Saniya scored 92
Rohan scored 78
```

---

## Challenge 2: Product Records

Given:

```python
products = [
    ("Laptop", 55000, 5),
    ("Keyboard", 1200, 10),
    ("Mouse", 800, 15)
]
```

Use tuple unpacking to print each product, price, and quantity.

---

## Challenge 3: First and Last

Given:

```python
numbers = (10, 20, 30, 40, 50, 60, 70)
```

Use extended unpacking to obtain:

```text
First: 10
Middle: [20, 30, 40, 50, 60]
Last: 70
```

---

## Challenge 4: Function Results

Create a function that returns:

```text
Total
Average
Highest
Lowest
```

Then unpack the returned tuple into four variables.

Example:

```python
def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest
```

Then unpack the result.

---

# ❓ Interview Questions

- [] What is Tuple Unpacking?
- [ ] How do you unpack a tuple?
- [ ] What happens if the number of variables does not match the number of tuple elements?
- [ ] What is extended unpacking?
- [ ] What does `*` do during unpacking?
- [ ] Can you use more than one `*` in one unpacking statement?
- [ ] What is the purpose of `_` in unpacking?
- [ ] How can you swap two variables using tuple unpacking?
- [ ] How can you unpack nested tuples?
- [ ] How can you unpack values returned by a function?
- [ ] How is tuple unpacking used in a `for` loop?
- [ ] How does `zip()` work with tuple unpacking?
- [ ] How does `enumerate()` work with tuple unpacking?
- [ ] What is the difference between packing and unpacking?

---

# 📝 Quick Revision

## Basic Unpacking

```python
numbers = (10, 20, 30)

a, b, c = numbers
```

---

## Swapping

```python
a, b = b, a
```

---

## First + Remaining

```python
first, *remaining = numbers
```

---

## Remaining + Last

```python
*remaining, last = numbers
```

---

## First + Middle + Last

```python
first, *middle, last = numbers
```

---

## Ignore Values

```python
a, _, c = numbers
```

---

## Nested Unpacking

```python
(a, b), (c, d) = ((10, 20), (30, 40))
```

---

## Function Unpacking

```python
total, average = calculate()
```

---

## Loop Unpacking

```python
for name, marks in students:
    print(name, marks)
```

---

# 🧠 Easy Memory Trick

Remember:

```text
PACKING
Multiple values
      ↓
   One tuple
```

Example:

```python
student = "Aisha", 21, 90
```

And:

```text
UNPACKING
One tuple
      ↓
Multiple variables
```

Example:

```python
name, age, marks = student
```

---

# 🎯 Topic Completion Checklist

- [x] I understand Tuple Unpacking.
- [x] I can unpack a tuple into variables.
- [x] I understand the matching rule.
- [x] I know what happens when the number of variables is incorrect.
- [x] I can unpack tuples containing different data types.
- [x] I can swap variables using tuple unpacking.
- [x] I understand extended unpacking.
- [x] I can use `*` to collect remaining values.
- [x] I can use `_` to ignore values.
- [x] I can unpack nested tuples.
- [x] I can unpack function return values.
- [x] I can unpack tuples inside loops.
- [x] I understand unpacking with `zip()`.
- [x] I understand unpacking with `enumerate()`.
- [x] I completed the practice programs.
- [x] I completed the challenges.

---

# 🎉 Tuple Topic Progress

So far, you have completed:

- [x] Creating Tuples
- [x] Tuple Packing
- [x] Tuple Unpacking
- [ ] Tuple Methods

---

# 🚀 Next Topic

## 📌 Topic 4: Tuple Methods

Next, we will learn the built-in methods available for tuples, including:

- [ ] `count()`
- [ ] `index()`
- [ ] How tuple methods work.
- [ ] Practical examples.
- [ ] Real-world examples.
- [ ] Common mistakes.
- [ ] Practice programs.
- [ ] Advanced examples.