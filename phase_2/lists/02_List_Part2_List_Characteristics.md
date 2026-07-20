# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Collections - List (Part 2):** List Characteristics

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand the characteristics of lists.
- [ ] Explain each characteristic with examples.
- [ ] Know why lists are the most commonly used collection.
- [ ] Answer interview questions about lists.

---

# 📖 What are List Characteristics?

List characteristics describe the **behavior and properties** of Python lists.

A Python list is:

1. Ordered
2. Mutable (Changeable)
3. Allows Duplicates
4. Can Store Different Data Types
5. Dynamic (Can Grow or Shrink)
6. Supports Indexing
7. Supports Slicing
8. Supports Nested Lists

---

# 1️⃣ Ordered

Lists maintain the order in which elements are added.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango']
```

The order is preserved.

Indexes:

```text
Apple  → 0
Banana → 1
Mango  → 2
```

---

# 2️⃣ Mutable (Changeable)

You can change elements after the list is created.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

Output:

```text
['Apple', 'Orange', 'Mango']
```

Unlike strings, lists are mutable.

---

# 3️⃣ Allows Duplicates

Lists allow duplicate values.

```python
numbers = [10, 20, 20, 30, 30]

print(numbers)
```

Output:

```text
[10, 20, 20, 30, 30]
```

Duplicates are preserved.

---

# 4️⃣ Can Store Different Data Types

A single list can contain different types of values.

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

# 5️⃣ Dynamic Size

Lists can grow or shrink while the program is running.

```python
numbers = [10, 20]

numbers.append(30)

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

```python
numbers.pop()

print(numbers)
```

Output:

```text
[10, 20]
```

No fixed size is required.

---

# 6️⃣ Supports Indexing

Each element has an index.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
```

Output:

```text
Apple
```

Negative indexing:

```python
print(fruits[-1])
```

Output:

```text
Mango
```

---

# 7️⃣ Supports Slicing

You can extract part of a list.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

---

# 8️⃣ Supports Nested Lists

Lists can contain other lists.

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

Access nested elements:

```python
print(matrix[0][1])
```

Output:

```text
2
```

---

# 🌍 Real-World Examples

## Shopping Cart

```python
cart = [
    "Milk",
    "Bread",
    "Eggs"
]
```

You can:

- Add products
- Remove products
- Change products

---

## Student Marks

```python
marks = [95, 88, 91]
```

Duplicates are allowed:

```python
marks = [95, 95, 91]
```

---

## Game Inventory

```python
inventory = [
    "Sword",
    "Shield",
    "Potion"
]
```

Players can add or remove items during gameplay.

---

# 📊 Summary Table

| Characteristic | Supported |
|---------------|-----------|
| Ordered | ✅ Yes |
| Mutable | ✅ Yes |
| Duplicates | ✅ Yes |
| Mixed Data Types | ✅ Yes |
| Dynamic Size | ✅ Yes |
| Indexing | ✅ Yes |
| Slicing | ✅ Yes |
| Nested Lists | ✅ Yes |

---

# ⚠️ Common Mistakes

## ❌ Thinking Lists Are Immutable

Wrong:

```python
fruits = ["Apple", "Banana"]

fruits[0] = "Orange"
```

Some beginners think this causes an error.

It works because lists are mutable.

---

## ❌ Confusing Lists with Sets

```python
numbers = [10, 20, 20]
```

Lists keep duplicates.

A set would automatically remove duplicate values.

---

# 💡 Best Practices

- Use lists when data may change.
- Use meaningful variable names.
- Group related items together.
- Use nested lists for table-like data.

---

# 🧠 Memory Trick

Remember:

```
OMDDISSN
```

- **O** → Ordered
- **M** → Mutable
- **D** → Duplicates Allowed
- **D** → Different Data Types
- **D** → Dynamic Size
- **I** → Indexing
- **S** → Slicing
- **N** → Nested Lists

---

# ❓ Interview Questions

- [ ] Are Python lists ordered?
- [ ] Are lists mutable?
- [ ] Can lists contain duplicate values?
- [ ] Can lists store different data types?
- [ ] Can lists grow or shrink?
- [ ] Do lists support indexing and slicing?

---

# 🏋️ Practice Programs

## Easy

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits)
```

---

```python
numbers = [10, 20, 20, 30]

print(numbers)
```

---

## Medium

```python
data = ["Saniya", 20, True, 8.92]

print(data)

data[1] = 21

print(data)
```

---

## Advanced

```python
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix)
print(matrix[2][1])
```

---

# 🎯 Challenge

Create:

```python
students = [
    "Saniya",
    "Rahul",
    "Aisha",
    "Rahul"
]
```

Then:

- Print the list.
- Change `"Rahul"` at index `1` to `"Arjun"`.
- Print the last element using negative indexing.
- Print the first three elements using slicing.

---

# 📝 Assignment

- [x] Create a list with duplicate values.
- [x] Modify one element in a list.
- [x] Create a mixed data type list.
- [x] Access an element using negative indexing.
- [x] Slice a list.
- [x] Create a nested list.

---

# 📚 Summary

A Python list is:

- Ordered
- Mutable
- Allows duplicates
- Can store mixed data types
- Dynamic in size
- Supports indexing
- Supports slicing
- Supports nested lists

---

# 🎯 Topic Completion Checklist

- [x] I understand all list characteristics.
- [x] I can explain each characteristic with an example.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **List – Part 3: Creating Lists (All Methods)**