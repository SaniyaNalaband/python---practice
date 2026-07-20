# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Collections - Part 1:** What is a List?

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a list is.
- [ ] Know why lists are used.
- [ ] Identify the characteristics of a list.
- [ ] Understand real-world uses of lists.
- [ ] Create your first list.

---

# 📖 1. What is a List?

A **list** is a collection data type used to **store multiple values in a single variable**.

Instead of creating many variables:

```python
student1 = "Saniya"
student2 = "Rahul"
student3 = "Aisha"
student4 = "Kiran"
```

You can store them in one variable:

```python
students = ["Saniya", "Rahul", "Aisha", "Kiran"]
```

Now all student names are stored in a single list.

---

# 📖 2. Why Do We Use Lists?

Imagine a class has **100 students**.

Without a list:

```python
student1 = "A"
student2 = "B"
student3 = "C"
...
student100 = "Z"
```

This is difficult to manage.

With a list:

```python
students = [
    "A", "B", "C", "...", "Z"
]
```

One variable can hold many values.

---

# 📖 3. Characteristics of a List

Lists have the following properties:

### ✅ Ordered

Items keep their position.

```python
fruits = ["Apple", "Banana", "Mango"]
```

- Apple → Index 0
- Banana → Index 1
- Mango → Index 2

The order is preserved.

---

### ✅ Changeable (Mutable)

You can modify a list after creating it.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

Output:

```text
['Apple', 'Orange', 'Mango']
```

---

### ✅ Allows Duplicates

Lists can contain duplicate values.

```python
numbers = [10, 20, 20, 30, 30]

print(numbers)
```

Output:

```text
[10, 20, 20, 30, 30]
```

---

### ✅ Can Store Different Data Types

A single list can hold multiple data types.

```python
data = [
    "Saniya",
    20,
    8.92,
    True
]

print(data)
```

Output:

```text
['Saniya', 20, 8.92, True]
```

---

### ✅ Can Store Other Lists

Lists can contain other lists (nested lists).

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix)
```

Output:

```text
[[1, 2], [3, 4]]
```

---

# 📖 4. List Syntax

```python
list_name = [item1, item2, item3]
```

Example:

```python
colors = ["Red", "Green", "Blue"]
```

Lists are created using **square brackets `[]`**.

---

# 📖 5. Empty List

You can create an empty list.

```python
items = []

print(items)
```

Output:

```text
[]
```

---

# 📖 6. Real-World Examples

### Shopping Cart

```python
cart = [                                                 
    "Milk",
    "Bread",
    "Eggs"
]
```

---

### Student Marks

```python
marks = [
    95,
    88,
    76,
    91
]
```

---

### To-Do List

```python
tasks = [
    "Study Python",
    "Practice Coding",
    "Push to GitHub"
]
```

---

### AI/ML Dataset Row

```python
record = [
    25,
    "Male",
    72.5,
    True
]
```

---

# 📖 7. Memory Representation

```text
students
    │
    ▼
+-------------------------------+
| "Saniya" | "Rahul" | "Aisha" |
+-------------------------------+
    0          1         2
```

The variable `students` refers to a list object containing multiple elements.

---

# ⚠️ Common Mistakes

## ❌ Using Parentheses

```python
fruits = ("Apple", "Banana")
```

This creates a **tuple**, not a list.

Correct:

```python
fruits = ["Apple", "Banana"]
```

---

## ❌ Forgetting Commas

Wrong:

```python
numbers = [1 2 3]
```

Correct:

```python
numbers = [1, 2, 3]
```

---

# 💡 Best Practices

- Use meaningful variable names.

```python
students = []
```

Instead of:

```python
x = []
```

---

- Store similar kinds of data together when possible.

```python
marks = [90, 80, 70]
```

---

# 🧠 Memory Trick

```
List

↓

[]

↓

Ordered

↓

Mutable

↓

Duplicates Allowed
```

Remember this shortcut:

> **OMD**

- **O** → Ordered
- **M** → Mutable
- **D** → Duplicates Allowed

---

# ❓ Interview Questions

- [ ] What is a list?
- [ ] Which brackets are used to create a list?
- [ ] Are lists mutable?
- [ ] Can lists contain duplicate values?
- [ ] Can a list store different data types?

---

# 🏋️ Practice Programs

## Easy

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

---

```python
numbers = [10, 20, 30]

print(numbers)
```

---

## Medium

```python
data = ["Saniya", 20, 8.92, True]

print(data)
```

---

```python
empty = []

print(empty)
```

---

## Advanced

```python
student = [
    "Saniya",
    20,
    "AI ML",
    8.92,
    ["Python", "SQL", "Git"]
]

print(student)
```

---

# 🎯 Challenge

Create the following lists:

```python
cities
subjects
marks
languages
```

Print each list.

---

# 📝 Assignment

Complete the following:

- [x] Create a list of 5 fruits.
- [x] Create a list of 5 numbers.
- [x] Create a list with mixed data types.
- [x] Create an empty list.
- [x] Explain three characteristics of a list.

---

# 📚 Summary

You learned:

- What a list is.
- Why lists are used.
- List characteristics.
- List syntax.
- Empty lists.
- Real-world examples.

---

# 🎯 Topic Completion Checklist

- [x] I understand what a list is.
- [x] I know list syntax.
- [x] I know that lists are ordered.
- [x] I know that lists are mutable.
- [x] I know that lists allow duplicates.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **List – Part 2: Creating Lists**