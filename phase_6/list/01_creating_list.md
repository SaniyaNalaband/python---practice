# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 1:** Creating Lists

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a list is.
- [ ] Create empty and non-empty lists.
- [ ] Store different data types in a list.
- [ ] Create nested lists.
- [ ] Create lists using the `list()` constructor.
- [ ] Understand list memory basics.

---

# 📖 What is a List?

A **list** is a built-in Python data structure used to store **multiple values in a single variable**.

Lists are:

- Ordered
- Mutable (can be changed)
- Allow duplicate values
- Can store different data types

---

# 🤔 Why Do We Need Lists?

Imagine storing marks of five students.

### Without a List

```python
mark1 = 85
mark2 = 90
mark3 = 78
mark4 = 95
mark5 = 88
```

This becomes difficult to manage.

---

### With a List

```python
marks = [85, 90, 78, 95, 88]
```

Now all marks are stored in a single variable.

---

# 📖 Syntax

```python
list_name = [item1, item2, item3]
```

Example

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

# 📖 Creating an Empty List

An empty list contains no elements.

```python
numbers = []

print(numbers)
```

Output

```text
[]
```

---

# 📖 Creating a List with Integers

```python
numbers = [10, 20, 30, 40, 50]

print(numbers)
```

Output

```text
[10, 20, 30, 40, 50]
```

---

# 📖 Creating a List with Strings

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits)
```

Output

```text
['Apple', 'Banana', 'Orange']
```

---

# 📖 Creating a List with Floats

```python
prices = [99.99, 120.50, 45.75]

print(prices)
```

Output

```text
[99.99, 120.5, 45.75]
```

---

# 📖 Creating a List with Boolean Values

```python
results = [True, False, True]

print(results)
```

Output

```text
[True, False, True]
```

---

# 📖 Creating a Mixed Data Type List

A list can store different data types together.

```python
student = ["Rahul", 21, 87.5, True]

print(student)
```

Output

```text
['Rahul', 21, 87.5, True]
```

---

# 📖 Creating a Nested List

A list can contain another list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
```

Output

```text
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

# 📖 Creating a List Using `list()`

The `list()` constructor converts an iterable into a list.

### From a String

```python
letters = list("Python")

print(letters)
```

Output

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

### From a Tuple

```python
numbers = list((10, 20, 30))

print(numbers)
```

Output

```text
[10, 20, 30]
```

---

### From a Range

```python
numbers = list(range(1, 6))

print(numbers)
```

Output

```text
[1, 2, 3, 4, 5]
```

---

# 📖 Creating Lists with Repeated Values

Using the `*` operator:

```python
zeros = [0] * 5

print(zeros)
```

Output

```text
[0, 0, 0, 0, 0]
```

---

# 📖 Length of a List

Use the `len()` function.

```python
fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))
```

Output

```text
3
```

---

# 📖 Checking the Data Type

```python
numbers = [1, 2, 3]

print(type(numbers))
```

Output

```text
<class 'list'>
```

---

# 📖 Memory Basics

Every list has its own memory address.

```python
numbers = [1, 2, 3]

print(id(numbers))
```

Output

```text
140368951532224
```

> The number will be different on every computer.

---

# 📊 Trace Table

Program

```python
colors = ["Red", "Green", "Blue"]

print(colors)
print(len(colors))
```

| Statement | Output |
|-----------|--------|
| `print(colors)` | `['Red', 'Green', 'Blue']` |
| `print(len(colors))` | `3` |

---

# 🌍 Real-World Examples

## Student Names

```python
students = ["Rahul", "Aisha", "Saniya", "Rohan"]

print(students)
```

---

## Shopping List

```python
shopping = ["Milk", "Bread", "Eggs", "Rice"]

print(shopping)
```

---

## Mobile Prices

```python
prices = [15999, 24999, 34999]

print(prices)
```

---

## Daily Temperatures

```python
temperatures = [29.5, 31.0, 30.2, 28.8]

print(temperatures)
```

---

## To-Do List

```python
tasks = [
    "Study Python",
    "Complete Assignment",
    "Exercise",
    "Read Book"
]

print(tasks)
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting Square Brackets

Incorrect

```python
numbers = 1, 2, 3
```

This creates a **tuple**, not a list.

Correct

```python
numbers = [1, 2, 3]
```

---

## ❌ Using Parentheses Instead of Square Brackets

Incorrect

```python
fruits = ("Apple", "Banana")
```

This creates a tuple.

Correct

```python
fruits = ["Apple", "Banana"]
```

---

## ❌ Forgetting Commas

Incorrect

```python
numbers = [10 20 30]
```

Output

```text
SyntaxError
```

Correct

```python
numbers = [10, 20, 30]
```

---

# 💡 Best Practices

- Use meaningful variable names like `students`, `marks`, or `prices`.
- Store related items in the same list.
- Keep formatting consistent for better readability.
- Use `list()` only when converting another iterable.

---

# 🚀 Pro Tips

Lists are widely used in:

- Student management systems
- Shopping cart applications
- Banking software
- Data analysis
- Machine learning
- Web development
- Game development

---

# ❓ Interview Questions

- [ ] What is a list in Python?
- [ ] How do you create an empty list?
- [ ] Can a list store different data types?
- [ ] What is the difference between `[]` and `list()`?
- [ ] How do you create a nested list?

---

# 🏋️ Practice Programs

## Easy

```python
colors = ["Red", "Green", "Blue"]

print(colors)
```

---

```python
numbers = [10, 20, 30, 40]

print(numbers)
```

---

## Medium

```python
student = ["Rahul", 20, 85.5, True]

print(student)
```

---

```python
letters = list("Python")

print(letters)
```

---

## Advanced

```python
matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(matrix)
```

---

```python
numbers = list(range(1, 11))

print(numbers)
```

---

# 🎯 Challenge

Write programs to:

1. Create a list of your five favorite movies.
2. Create a list of ten even numbers.
3. Create a nested list representing a 3×3 matrix.
4. Convert the string `"Programming"` into a list of characters.

---

# 📝 Assignment

- [x] Create an empty list.
- [x] Create a list of integers.
- [x] Create a list of strings.
- [x] Create a mixed data type list.
- [x] Create a nested list.
- [x] Create a list using `list()`.
- [x] Create a list using `range()`.
- [x] Print the length of each list.

---

# 📚 Summary

You learned:

- ✅ What a list is.
- ✅ How to create different types of lists.
- ✅ How to create empty, mixed, and nested lists.
- ✅ How to use the `list()` constructor.
- ✅ How to use `len()`, `type()`, and `id()` with lists.

### Key Points to Remember

- Lists are created using **square brackets `[]`**.
- Lists are **ordered** and **mutable**.
- Lists can contain **duplicate values**.
- Lists can store **multiple data types**.
- The `list()` function converts iterables into lists.

---

# 🎯 Topic Completion Checklist

- [x] I understand what a list is.
- [x] I can create different types of lists.
- [x] I can create nested lists.
- [x] I know how to use `list()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 2: List Indexing**