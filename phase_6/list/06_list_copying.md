# 🐍 Python Master Course

# 📦 Phase 6: Collections – Lists

## 📌 Topic 6: Copying Lists

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand how lists are copied in Python.
- [ ] Understand the difference between assignment and copying.
- [ ] Use the `copy()` method.
- [ ] Copy lists using slicing.
- [ ] Understand shallow copying.
- [ ] Understand deep copying.
- [ ] Understand copying of nested lists.
- [ ] Choose the correct copying technique.

---

# 📖 What is Copying a List?

Copying a list means creating another list that contains the elements of an existing list.

For example:

```python
original = [10, 20, 30]
```

We may want another list with the same elements:

```python
copy_list = [10, 20, 30]
```

However, there are different ways to copy a list in Python.

Some methods create a **new list**, while others only create another reference to the **same list**.

---

# 📌 1. Assignment Using `=`

The simplest way to assign a list to another variable is:

```python
original = [10, 20, 30]

copy_list = original
```

But this does **not create a new list**.

Both variables refer to the same list.

---

## Example

```python
original = [10, 20, 30]

copy_list = original

copy_list.append(40)

print(original)
print(copy_list)
```

Output:

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

Why did the original list change?

Because:

```python
copy_list = original
```

makes both variables refer to the same list.

---

# 🧠 Visual Representation

```text
original ───────┐
                ↓
          [10, 20, 30]
                ↑
                │
copy_list ──────┘
```

There is only **one list object**.

---

# 📌 Checking with `id()`

You can use `id()` to check whether two variables refer to the same object.

```python
original = [10, 20, 30]

copy_list = original

print(id(original))
print(id(copy_list))
```

The two IDs will be the same.

---

# 📌 2. Using the `copy()` Method

The `copy()` method creates a **new list** containing the elements of the original list.

### Syntax

```python
new_list = original_list.copy()
```

---

## Example

```python
original = [10, 20, 30]

copy_list = original.copy()

print(original)
print(copy_list)
```

Output:

```text
[10, 20, 30]
[10, 20, 30]
```

The values are the same, but the lists are separate objects.

---

# 📖 Modifying the Copied List

```python
original = [10, 20, 30]

copy_list = original.copy()

copy_list.append(40)

print("Original:", original)
print("Copy:", copy_list)
```

Output:

```text
Original: [10, 20, 30]
Copy: [10, 20, 30, 40]
```

The original list is unchanged.

---

# 🧠 Visual Representation

```text
original ─────→ [10, 20, 30]

copy_list ────→ [10, 20, 30]
```

There are two separate list objects.

---

# 📌 Checking the IDs

```python
original = [10, 20, 30]

copy_list = original.copy()

print(id(original))
print(id(copy_list))
```

The IDs will be different.

---

# 📌 3. Copying Using Slicing

Another way to copy a list is using slicing.

```python
original[:]
```

Example:

```python
original = [10, 20, 30]

copy_list = original[:]

print(copy_list)
```

Output:

```text
[10, 20, 30]
```

This creates a new list.

---

# 📖 Modifying a Sliced Copy

```python
original = [10, 20, 30]

copy_list = original[:]

copy_list.append(40)

print("Original:", original)
print("Copy:", copy_list)
```

Output:

```text
Original: [10, 20, 30]
Copy: [10, 20, 30, 40]
```

---

# 📊 Assignment vs Copying

| Method | New List Created? | Independent? |
|---|---:|---:|
| `new = original` | ❌ | ❌ |
| `new = original.copy()` | ✅ | ✅ |
| `new = original[:]` | ✅ | ✅ |

---

# 📌 4. Shallow Copy

The `copy()` method creates a **shallow copy**.

A shallow copy creates a new outer list, but if the list contains other mutable objects such as nested lists, those inner objects may still be shared.

---

## Simple Example

```python
original = [10, 20, 30]

copy_list = original.copy()

copy_list[0] = 100

print("Original:", original)
print("Copy:", copy_list)
```

Output:

```text
Original: [10, 20, 30]
Copy: [100, 20, 30]
```

The outer lists are independent.

---

# ⚠️ Shallow Copy with Nested Lists

Consider:

```python
original = [
    [10, 20],
    [30, 40]
]

copy_list = original.copy()
```

The outer list is copied, but the inner lists are still shared.

---

## Example

```python
original = [
    [10, 20],
    [30, 40]
]

copy_list = original.copy()

copy_list[0].append(50)

print("Original:", original)
print("Copy:", copy_list)
```

Output:

```text
Original: [[10, 20, 50], [30, 40]]
Copy: [[10, 20, 50], [30, 40]]
```

The original changed too.

Why?

Because the inner list:

```python
[10, 20]
```

is shared between both lists.

---

# 🧠 Shallow Copy Diagram

```text
original ─────→ Outer List
                   │
                   ├──→ [10, 20] ←── shared
                   │
                   └──→ [30, 40]

copy_list ────→ Outer List
                   │
                   ├──→ [10, 20] ←── shared
                   │
                   └──→ [30, 40]
```

The outer lists are different.

The nested lists can be the same objects.

---

# 📌 5. Deep Copy

A **deep copy** creates a completely independent copy of the list, including nested objects.

Python provides the `copy` module for this.

First import the module:

```python
import copy
```

Then use:

```python
copy.deepcopy()
```

---

# 📖 Deep Copy Example

```python
import copy

original = [
    [10, 20],
    [30, 40]
]

copy_list = copy.deepcopy(original)

copy_list[0].append(50)

print("Original:", original)
print("Copy:", copy_list)
```

Output:

```text
Original: [[10, 20], [30, 40]]
Copy: [[10, 20, 50], [30, 40]]
```

The original nested list remains unchanged.

---

# 🧠 Deep Copy Diagram

```text
original ─────→ Outer List
                   │
                   ├──→ [10, 20]
                   │
                   └──→ [30, 40]


copy_list ────→ Outer List
                   │
                   ├──→ [10, 20]
                   │
                   └──→ [30, 40]
```

All nested objects are independently copied.

---

# 📊 Shallow Copy vs Deep Copy

| Feature | Shallow Copy | Deep Copy |
|---|---|---|
| New outer list | ✅ | ✅ |
| Nested lists copied | ❌ | ✅ |
| Nested objects shared | Can be | ❌ |
| `copy()` | ✅ | ❌ |
| `deepcopy()` | ❌ | ✅ |
| Requires `import copy` | ❌ | ✅ |

---

# 📌 Different Ways to Copy a List

There are three common ways:

### Method 1: `copy()`

```python
new = original.copy()
```

### Method 2: Slicing

```python
new = original[:]
```

### Method 3: `deepcopy()`

```python
import copy

new = copy.deepcopy(original)
```

---

# 📊 Complete Comparison

```python
original = [[1, 2], [3, 4]]
```

### Assignment

```python
new = original
```

```text
Same outer list
Same nested lists
```

---

### Shallow Copy

```python
new = original.copy()
```

```text
New outer list
Same nested lists
```

---

### Slicing

```python
new = original[:]
```

```text
New outer list
Same nested lists
```

---

### Deep Copy

```python
import copy

new = copy.deepcopy(original)
```

```text
New outer list
New nested lists
```

---

# 🌍 Real-World Example 1: Student Records

Suppose we have:

```python
students = [
    ["Aisha", 85],
    ["Saniya", 92],
    ["Rohan", 78]
]
```

Create a shallow copy:

```python
backup = students.copy()
```

For a completely independent copy:

```python
import copy

backup = copy.deepcopy(students)
```

---

# 🌍 Real-World Example 2: Shopping Cart

```python
cart = [
    ["Laptop", 50000],
    ["Mouse", 1000],
    ["Keyboard", 2000]
]
```

Create a copy:

```python
cart_backup = cart.copy()
```

Or a deep copy:

```python
import copy

cart_backup = copy.deepcopy(cart)
```

---

# 🌍 Real-World Example 3: Game Board

```python
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
]
```

If you want to create an independent board:

```python
import copy

new_board = copy.deepcopy(board)
```

Now changing `new_board` will not change `board`.

---

# 📌 Copying a List with Slicing

Slicing can also copy a list:

```python
numbers = [10, 20, 30, 40, 50]

new_numbers = numbers[:]

print(new_numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 📌 Copying Only Part of a List

Remember that slicing can also select a portion.

```python
numbers = [10, 20, 30, 40, 50]

new_numbers = numbers[1:4]

print(new_numbers)
```

Output:

```text
[20, 30, 40]
```

This is not a complete copy; it creates a new list containing only the selected elements.

---

# 📌 Copying Using `list()`

Another way to create a shallow copy is:

```python
numbers = [10, 20, 30]

new_numbers = list(numbers)

print(new_numbers)
```

Output:

```text
[10, 20, 30]
```

This also creates a new outer list.

---

# 📊 Four Ways to Create a Shallow Copy

```python
original = [10, 20, 30]
```

### 1. `copy()`

```python
new = original.copy()
```

### 2. Slicing

```python
new = original[:]
```

### 3. `list()`

```python
new = list(original)
```

### 4. `copy.copy()`

```python
import copy

new = copy.copy(original)
```

All of these create a **shallow copy**.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Thinking `=` Creates a Copy

```python
a = [1, 2, 3]

b = a

b.append(4)

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

`b` is not an independent copy.

---

## ❌ Mistake 2: Thinking `copy()` Deep-Copies Nested Lists

```python
a = [[1, 2], [3, 4]]

b = a.copy()

b[0].append(5)

print(a)
```

Output:

```text
[[1, 2, 5], [3, 4]]
```

The nested list is shared.

---

## ❌ Mistake 3: Forgetting the `copy` Module

Incorrect:

```python
new = copy.deepcopy(original)
```

Correct:

```python
import copy

new = copy.deepcopy(original)
```

---

# 📌 Checking Object Identity

Use `is` to check whether two variables refer to the same object.

### Assignment

```python
a = [1, 2, 3]
b = a

print(a is b)
```

Output:

```text
True
```

---

### Copy

```python
a = [1, 2, 3]
b = a.copy()

print(a is b)
```

Output:

```text
False
```

The lists are separate objects.

---

# 📌 Comparing Contents

Two separate lists can contain the same values.

```python
a = [1, 2, 3]
b = a.copy()

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

Remember:

```text
==  → compares values
is  → compares object identity
```

---

# 🧠 Important Concept

This is one of the most important things to remember:

```python
a = [1, 2, 3]
b = a
```

means:

```text
a ───┐
     ↓
 [1, 2, 3]
     ↑
     │
b ───┘
```

But:

```python
a = [1, 2, 3]
b = a.copy()
```

means:

```text
a ───→ [1, 2, 3]

b ───→ [1, 2, 3]
```

Two separate objects.

---

# 🚀 Advanced Example

```python
import copy

original = [
    ["Laptop", 50000],
    ["Mouse", 1000]
]

backup = copy.deepcopy(original)

backup[0][1] = 45000

print("Original:", original)
print("Backup:", backup)
```

Output:

```text
Original: [['Laptop', 50000], ['Mouse', 1000]]
Backup: [['Laptop', 45000], ['Mouse', 1000]]
```

The original remains unchanged.

---

# 🏋️ Practice Programs

## Beginner

### 1. Assignment

```python
numbers = [10, 20, 30]

new_numbers = numbers

new_numbers.append(40)

print(numbers)
print(new_numbers)
```

Predict the output before running it.

---

### 2. `copy()`

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)
```

---

### 3. Slicing

```python
numbers = [10, 20, 30]

new_numbers = numbers[:]

new_numbers.append(40)

print(numbers)
print(new_numbers)
```

---

# 🏋️ Intermediate Practice

### 4. Compare IDs

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(id(numbers))
print(id(new_numbers))
```

---

### 5. Compare with `is`

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(numbers is new_numbers)
```

---

### 6. Compare with `==`

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

print(numbers == new_numbers)
print(numbers is new_numbers)
```

---

# 🚀 Advanced Practice

### 7. Shallow Copy

```python
numbers = [
    [10, 20],
    [30, 40]
]

new_numbers = numbers.copy()

new_numbers[0].append(50)

print(numbers)
print(new_numbers)
```

Predict the output.

---

### 8. Deep Copy

```python
import copy

numbers = [
    [10, 20],
    [30, 40]
]

new_numbers = copy.deepcopy(numbers)

new_numbers[0].append(50)

print(numbers)
print(new_numbers)
```

Compare this with the previous program.

---

# 🏆 Challenge

Create a program using:

```python
students = [
    ["Aisha", 85, 90],
    ["Saniya", 92, 88],
    ["Rohan", 78, 82]
]
```

Perform the following:

1. [x] Create an assignment reference.
2. [x] Create a shallow copy using `copy()`.
3. [x] Create a copy using slicing.
4. [x] Create a copy using `list()`.
5. [x] Create a deep copy.
6. [x] Modify the original list.
7. [x] Modify the shallow copy.
8. [x] Modify the deep copy.
9. [x] Observe which lists change.
10. [x] Compare their IDs.

---

# ❓ Interview Questions

- [x] What happens when one list is assigned to another using `=`?
- [x] Does `copy()` create a new list?
- [x] What is a shallow copy?
- [x] What is a deep copy?
- [x] What is the difference between `copy()` and `deepcopy()`?
- [x] How can you copy a list using slicing?
- [x] How can you copy a list using `list()`?
- [x] What is the difference between `==` and `is`?
- [x] Why can modifying a nested list affect a shallow copy?
- [x] When should you use `deepcopy()`?

---

# 📊 Quick Comparison

| Technique | New Outer List | New Nested Lists |
|---|---:|---:|
| `new = original` | ❌ | ❌ |
| `new = original.copy()` | ✅ | ❌ |
| `new = original[:]` | ✅ | ❌ |
| `new = list(original)` | ✅ | ❌ |
| `copy.copy(original)` | ✅ | ❌ |
| `copy.deepcopy(original)` | ✅ | ✅ |

---

# 🧠 Easy Way to Remember

```text
= 
↓
Same list


copy()
↓
New outer list


[:]
↓
New outer list


list()
↓
New outer list


deepcopy()
↓
New outer list + new nested objects
```

---

# 📚 Summary

### Assignment

```python
new = original
```

Both variables refer to the **same list**.

### `copy()`

```python
new = original.copy()
```

Creates a **shallow copy**.

### Slicing

```python
new = original[:]
```

Creates a **shallow copy**.

### `list()`

```python
new = list(original)
```

Creates a **shallow copy**.

### Deep Copy

```python
import copy

new = copy.deepcopy(original)
```

Creates a completely independent copy, including nested objects.

---

# 🎯 Topic Completion Checklist

- [x] I understand assignment using `=`.
- [x] I understand the `copy()` method.
- [x] I understand copying using slicing.
- [x] I understand copying using `list()`.
- [x] I understand shallow copying.
- [x] I understand deep copying.
- [x] I understand `copy.deepcopy()`.
- [x] I understand `==` vs `is`.
- [x] I can copy nested lists correctly.
- [x] I completed the practice programs.
- [x] I completed the challenge.

---

# 📚 Next Topic

➡️ **Phase 6 – Topic 7: List Comprehension**

Topics:

- Basic List Comprehension
- List Comprehension with Conditions
- `if-else` with List Comprehension
- Nested List Comprehension
- List Comprehension with Functions
- Real-World Examples
- Advanced List Comprehension