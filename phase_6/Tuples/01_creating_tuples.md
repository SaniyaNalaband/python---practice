# 🐍 Python Master Course

# 📦 Phase 6: Collections – Tuples

## 📌 Topic 1: Creating Tuples

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand what a tuple is.
- [ ] Create tuples using parentheses `()`.
- [ ] Create tuples without parentheses.
- [ ] Create an empty tuple.
- [ ] Create a single-element tuple.
- [ ] Create tuples containing different data types.
- [ ] Create nested tuples.
- [ ] Create tuples using the `tuple()` constructor.
- [ ] Convert lists, strings, and ranges into tuples.
- [ ] Understand the difference between tuples and lists.
- [ ] Understand tuple immutability.

---

# 📖 What is a Tuple?

A **tuple** is an ordered collection of elements in Python.

Tuples are similar to lists, but the major difference is:

> **Tuples are immutable.**

This means that once a tuple is created, its elements cannot be changed, added, or removed.

### Example

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits)
```

Output:

```text
('Apple', 'Banana', 'Mango')
```

---

# 📌 Syntax of a Tuple

The general syntax is:

```python
tuple_name = (item1, item2, item3)
```

Example:

```python
numbers = (10, 20, 30)
```

Here:

```text
numbers
   ↓
(10, 20, 30)
```

is a tuple.

---

# 📌 1. Creating a Tuple Using Parentheses

The most common way to create a tuple is by using parentheses `()`.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers)
```

Output:

```text
(10, 20, 30, 40, 50)
```

---

# 📌 Example: Tuple of Strings

```python
languages = ("Python", "Java", "C", "JavaScript")

print(languages)
```

Output:

```text
('Python', 'Java', 'C', 'JavaScript')
```

---

# 📌 Example: Tuple of Floating-Point Numbers

```python
prices = (99.5, 149.99, 250.75)

print(prices)
```

Output:

```text
(99.5, 149.99, 250.75)
```

---

# 📌 Example: Tuple of Boolean Values

```python
values = (True, False, True, True)

print(values)
```

Output:

```text
(True, False, True, True)
```

---

# 📌 2. Tuple with Different Data Types

A tuple can contain different types of data.

```python
student = ("Saniya", 21, 85.5, True)

print(student)
```

Output:

```text
('Saniya', 21, 85.5, True)
```

The tuple contains:

```text
"Saniya" → str
21       → int
85.5     → float
True     → bool
```

---

# 📌 Example: Multiple Data Types

```python
data = (
    "Python",
    3,
    3.14,
    True,
    None
)

print(data)
```

Output:

```text
('Python', 3, 3.14, True, None)
```

---

# 📌 3. Empty Tuple

An empty tuple contains no elements.

### Syntax

```python
empty = ()
```

Example:

```python
empty = ()

print(empty)
print(type(empty))
```

Output:

```text
()
<class 'tuple'>
```

---

# 📌 Why Use an Empty Tuple?

An empty tuple can be useful when:

- You need a placeholder.
- A function needs to return no values initially.
- You want an immutable empty collection.

Example:

```python
data = ()

print(len(data))
```

Output:

```text
0
```

---

# 📌 4. Single-Element Tuple

Creating a tuple with only one element is slightly different.

### ❌ This is NOT a tuple

```python
number = (10)

print(type(number))
```

Output:

```text
<class 'int'>
```

Why?

Because parentheses alone do not create a tuple.

---

# ✅ Correct Single-Element Tuple

You need a comma:

```python
number = (10,)

print(number)
print(type(number))
```

Output:

```text
(10,)
<class 'tuple'>
```

---

# 🧠 Important Rule

Remember:

```python
(10)     # int
(10,)    # tuple
```

The **comma** is what makes it a single-element tuple.

---

# 📌 Single String Tuple

Incorrect:

```python
name = ("Python")

print(type(name))
```

Output:

```text
<class 'str'>
```

Correct:

```python
name = ("Python",)

print(type(name))
```

Output:

```text
<class 'tuple'>
```

---

# 📌 5. Creating Tuples Without Parentheses

Python allows you to create a tuple without explicitly using parentheses.

```python
numbers = 10, 20, 30

print(numbers)
print(type(numbers))
```

Output:

```text
(10, 20, 30)
<class 'tuple'>
```

The commas tell Python that this is a tuple.

---

# 📌 Example

```python
languages = "Python", "Java", "C"

print(languages)
```

Output:

```text
('Python', 'Java', 'C')
```

---

# 🧠 Parentheses vs Commas

These both create tuples:

```python
numbers = (10, 20, 30)
```

and:

```python
numbers = 10, 20, 30
```

The important part is the comma-separated values.

---

# 📌 6. Using the `tuple()` Constructor

Python provides the built-in `tuple()` function for creating tuples.

### Syntax

```python
tuple(iterable)
```

Example:

```python
numbers = tuple([10, 20, 30])

print(numbers)
```

Output:

```text
(10, 20, 30)
```

---

# 📌 Converting a List into a Tuple

```python
numbers_list = [10, 20, 30, 40]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
```

Output:

```text
(10, 20, 30, 40)
```

The original list remains a list:

```python
print(type(numbers_list))
```

Output:

```text
<class 'list'>
```

The converted object is a tuple:

```python
print(type(numbers_tuple))
```

Output:

```text
<class 'tuple'>
```

---

# 📌 7. Converting a String into a Tuple

A string is iterable, so it can be converted into a tuple.

```python
word = "Python"

letters = tuple(word)

print(letters)
```

Output:

```text
('P', 'y', 't', 'h', 'o', 'n')
```

Each character becomes an element of the tuple.

---

# 📌 Another String Example

```python
word = "HELLO"

letters = tuple(word)

print(letters)
```

Output:

```text
('H', 'E', 'L', 'L', 'O')
```

Notice that duplicate characters are allowed.

---

# 📌 8. Converting a Range into a Tuple

The `range()` function can also be converted into a tuple.

```python
numbers = tuple(range(1, 6))

print(numbers)
```

Output:

```text
(1, 2, 3, 4, 5)
```

---

# 📌 Example with Range

```python
numbers = tuple(range(10, 21, 2))

print(numbers)
```

Output:

```text
(10, 12, 14, 16, 18, 20)
```

---

# 📌 9. Creating a Nested Tuple

A tuple can contain another tuple.

This is called a **nested tuple**.

```python
data = (
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
)

print(data)
```

Output:

```text
(('Aisha', 85), ('Saniya', 92), ('Rohan', 78))
```

---

# 📌 Example: Nested Numbers

```python
numbers = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(numbers)
```

Output:

```text
((1, 2, 3), (4, 5, 6), (7, 8, 9))
```

This type of structure is useful for representing:

- Matrices
- Tables
- Coordinates
- Records
- Grouped data

---

# 📌 10. Tuple Containing a List

A tuple can contain mutable objects such as lists.

```python
data = (
    "Python",
    [10, 20, 30]
)

print(data)
```

Output:

```text
('Python', [10, 20, 30])
```

The tuple itself is immutable, but the list inside it is mutable.

---

# ⚠️ Important Example

```python
data = (
    "Python",
    [10, 20, 30]
)

data[1].append(40)

print(data)
```

Output:

```text
('Python', [10, 20, 30, 40])
```

The tuple's structure has not changed.

We modified the **list inside the tuple**.

---

# 📌 11. Tuple Containing Another Data Structure

A tuple can contain:

- Strings
- Integers
- Floats
- Booleans
- Lists
- Tuples
- Dictionaries
- Sets
- Other objects

Example:

```python
data = (
    "Python",
    3.14,
    [10, 20],
    {"name": "Aisha"},
    (1, 2),
)

print(data)
```

---

# 📌 12. Creating a Tuple from a Set

```python
numbers = {10, 20, 30}

numbers_tuple = tuple(numbers)

print(numbers_tuple)
```

Output may be:

```text
(10, 20, 30)
```

The exact order should not be relied upon because sets are unordered collections.

---

# 📌 13. Creating a Tuple from a Dictionary

When a dictionary is passed to `tuple()`, its keys are converted into tuple elements.

```python
student = {
    "name": "Aisha",
    "age": 21,
    "marks": 90
}

result = tuple(student)

print(result)
```

Output:

```text
('name', 'age', 'marks')
```

Only the dictionary keys are included.

---

# 📌 14. Creating a Tuple from Dictionary Items

If you want key-value pairs:

```python
student = {
    "name": "Aisha",
    "age": 21,
    "marks": 90
}

result = tuple(student.items())

print(result)
```

Output:

```text
(
    ('name', 'Aisha'),
    ('age', 21),
    ('marks', 90)
)
```

---

# 📌 15. Checking the Type of a Tuple

Use the `type()` function.

```python
numbers = (10, 20, 30)

print(type(numbers))
```

Output:

```text
<class 'tuple'>
```

---

# 📌 16. Finding the Length of a Tuple

Use the `len()` function.

```python
numbers = (10, 20, 30, 40, 50)

print(len(numbers))
```

Output:

```text
5
```

---

# 📌 17. Duplicate Values in Tuples

Tuples allow duplicate values.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers)
```

Output:

```text
(10, 20, 10, 30, 10)
```

Duplicates are completely valid.

---

# 📌 18. Creating a Tuple with `None`

```python
data = (10, None, 20)

print(data)
```

Output:

```text
(10, None, 20)
```

`None` is a valid tuple element.

---

# 📌 19. Creating a Tuple with Boolean Values

```python
status = (True, False, True)

print(status)
```

Output:

```text
(True, False, True)
```

---

# 📌 20. Creating a Tuple with Expressions

You can create tuple elements using expressions.

```python
a = 10
b = 20

numbers = (a, b, a + b)

print(numbers)
```

Output:

```text
(10, 20, 30)
```

---

# 📌 21. Creating Tuples from Variables

```python
name = "Saniya"
age = 21
marks = 90

student = (name, age, marks)

print(student)
```

Output:

```text
('Saniya', 21, 90)
```

---

# 📌 22. Tuple Assignment

Multiple values separated by commas automatically form a tuple.

```python
student = "Saniya", 21, 90

print(student)
```

Output:

```text
('Saniya', 21, 90)
```

This concept leads directly into **Tuple Packing**.

---

# 📌 Tuple Immutability

Tuples cannot be modified after creation.

Example:

```python
numbers = (10, 20, 30)
```

Trying to change an element:

```python
numbers[0] = 100
```

will produce an error:

```text
TypeError: 'tuple' object does not support item assignment
```

---

# ❌ You Cannot Change a Tuple Element

```python
numbers = (10, 20, 30)

numbers[1] = 200
```

This is not allowed.

---

# ❌ You Cannot Append to a Tuple

```python
numbers = (10, 20, 30)

numbers.append(40)
```

This produces:

```text
AttributeError
```

Tuples do not have an `append()` method.

---

# ❌ You Cannot Remove an Element

```python
numbers = (10, 20, 30)

numbers.remove(20)
```

This is not supported.

---

# 📊 List vs Tuple

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[]` | `()` |
| Ordered | ✅ | ✅ |
| Indexed | ✅ | ✅ |
| Mutable | ✅ | ❌ |
| Immutable | ❌ | ✅ |
| Allows duplicates | ✅ | ✅ |
| Supports slicing | ✅ | ✅ |
| `append()` | ✅ | ❌ |
| `remove()` | ✅ | ❌ |
| `pop()` | ✅ | ❌ |
| Generally smaller | ❌ | ✅ |
| Can be dictionary key | ❌ | ✅ if elements are hashable |

---

# 📊 Different Ways to Create Tuples

| Method | Example |
|---|---|
| Parentheses | `(1, 2, 3)` |
| Without parentheses | `1, 2, 3` |
| `tuple()` | `tuple([1, 2, 3])` |
| From string | `tuple("ABC")` |
| From range | `tuple(range(1, 5))` |
| From list | `tuple([10, 20])` |
| From set | `tuple({10, 20})` |
| From dictionary | `tuple({"a": 1, "b": 2})` |

---

# 🌍 Real-World Examples

## Example 1: Student Record

```python
student = (
    "Saniya",
    21,
    "BCA",
    89.5
)

print(student)
```

Output:

```text
('Saniya', 21, 'BCA', 89.5)
```

A tuple can be useful for storing a fixed record.

---

# 🌍 Example 2: Coordinates

```python
point = (10, 20)

print(point)
```

Output:

```text
(10, 20)
```

This can represent an `(x, y)` coordinate.

---

# 🌍 Example 3: RGB Color

```python
color = (255, 128, 0)

print(color)
```

Output:

```text
(255, 128, 0)
```

A tuple can represent a fixed RGB color value.

---

# 🌍 Example 4: Product Information

```python
product = (
    "Laptop",
    55000,
    "Electronics"
)

print(product)
```

Output:

```text
('Laptop', 55000, 'Electronics')
```

---

# 🌍 Example 5: Database Record

```python
employee = (
    101,
    "Aisha",
    "Developer",
    45000
)

print(employee)
```

Output:

```text
(101, 'Aisha', 'Developer', 45000)
```

A tuple is suitable when the record should remain fixed.

---

# 🌍 Example 6: Days of the Week

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print(days)
```

---

# 🧠 Important Rules to Remember

### Rule 1

Parentheses are commonly used:

```python
numbers = (1, 2, 3)
```

### Rule 2

Commas are what distinguish tuple items:

```python
numbers = 1, 2, 3
```

### Rule 3

A single-element tuple requires a comma:

```python
number = (10,)
```

### Rule 4

An empty tuple is:

```python
empty = ()
```

### Rule 5

Tuples are immutable:

```python
numbers = (1, 2, 3)
```

You cannot change:

```python
numbers[0]
```

---

# 🧪 Practice Programs

## Beginner Practice

### 1. Create a tuple of five numbers.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers)
```

---

### 2. Create a tuple of programming languages.

```python
languages = (
    "Python",
    "Java",
    "C",
    "JavaScript"
)

print(languages)
```

---

### 3. Create an empty tuple.

```python
empty = ()

print(empty)
```

---

### 4. Create a single-element tuple.

```python
number = (100,)

print(number)
```

---

### 5. Create a tuple containing different data types.

```python
data = (
    "Python",
    10,
    3.14,
    True,
    None
)

print(data)
```

---

# 🏋️ Intermediate Practice

### 6. Convert a list into a tuple.

```python
numbers = [10, 20, 30, 40]

result = tuple(numbers)

print(result)
```

---

### 7. Convert a string into a tuple.

```python
word = "Python"

result = tuple(word)

print(result)
```

---

### 8. Convert a range into a tuple.

```python
numbers = tuple(range(1, 11))

print(numbers)
```

---

### 9. Create a nested tuple.

```python
data = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(data)
```

---

### 10. Create a student record.

```python
student = (
    "Saniya",
    21,
    "BCA",
    90
)

print(student)
```

---

# 🚀 Advanced Practice

### 11. Create a tuple from a dictionary's keys.

```python
student = {
    "name": "Aisha",
    "age": 21,
    "marks": 90
}

result = tuple(student)

print(result)
```

---

### 12. Create a tuple from dictionary items.

```python
student = {
    "name": "Aisha",
    "age": 21,
    "marks": 90
}

result = tuple(student.items())

print(result)
```

---

### 13. Create a nested student record.

```python
students = (
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
)

print(students)
```

---

### 14. Create a tuple containing a list.

```python
data = (
    "Python",
    [10, 20, 30]
)

print(data)
```

---

# 🏆 Challenge

Create a tuple representing a product:

```text
Product Name
Product ID
Price
Category
Stock
```

For example:

```python
product = (
    "Laptop",
    101,
    55000,
    "Electronics",
    25
)

print(product)
```

Then:

- [x] Check its type.
- [x] Check its length.
- [x] Try changing one element.
- [x] Observe the error.
- [x] Create a single-element tuple.
- [x] Create an empty tuple.
- [x] Convert a list into a tuple.
- [x] Convert a string into a tuple.
- [x] Convert a range into a tuple.

---

# ❓ Interview Questions

- [x] What is a tuple?
- [x] How do you create a tuple?
- [x] Are parentheses mandatory for creating a tuple?
- [x] What makes a single-element tuple different?
- [x] Why is `(10)` not a tuple?
- [x] Why is `(10,)` a tuple?
- [x] Can a tuple contain different data types?
- [x] Can a tuple contain another tuple?
- [x] Can a tuple contain a list?
- [x] What does `tuple()` do?
- [x] How do you convert a list into a tuple?
- [x] How do you convert a string into a tuple?
- [x] How do you create an empty tuple?
- [x] Are tuples mutable or immutable?
- [x] What is the difference between a list and a tuple?

---

# 📝 Quick Revision

```python
# Normal tuple
numbers = (10, 20, 30)

# Without parentheses
numbers = 10, 20, 30

# Empty tuple
empty = ()

# Single-element tuple
single = (10,)

# Mixed data types
data = ("Python", 10, 3.14, True)

# Nested tuple
nested = ((1, 2), (3, 4))

# From list
numbers = tuple([1, 2, 3])

# From string
letters = tuple("Python")

# From range
numbers = tuple(range(1, 6))
```

---

# 🧠 Remember

```text
Tuple
  ↓
Ordered
  ↓
Indexed
  ↓
Allows duplicates
  ↓
Can contain different data types
  ↓
Immutable
```

### Most Important Point

```python
(10)      # int
(10,)     # tuple
```

**The comma is important for a single-element tuple.**

---

# 🎯 Topic Completion Checklist

- [x] I understand what a tuple is.
- [x] I can create tuples using `()`.
- [x] I can create tuples without parentheses.
- [x] I can create an empty tuple.
- [x] I can create a single-element tuple.
- [x] I understand why `(10)` is not a tuple.
- [x] I understand why `(10,)` is a tuple.
- [x] I can create tuples with multiple data types.
- [x] I can create nested tuples.
- [x] I can convert a list into a tuple.
- [x] I can convert a string into a tuple.
- [x] I can convert a range into a tuple.
- [x] I understand tuple immutability.
- [x] I completed the practice programs.
- [x] I completed the challenge.

---

# 🚀 Next Topic

## 📌 Topic 2: Tuple Packing

Next we will learn:

- [ ] What is Tuple Packing?
- [ ] How Python automatically packs values into a tuple.
- [ ] Packing multiple values.
- [ ] Packing different data types.
- [ ] Packing with variables.
- [ ] Real-world examples.
- [ ] Practice programs.
- [ ] Advanced examples.