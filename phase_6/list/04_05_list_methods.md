# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 4 (Part 5): Copying Lists**

**Topics Covered:**

- ✅ Assignment using `=`
- ✅ `copy()`
- ✅ Slicing `[:]`
- ✅ Shallow Copy
- ✅ Deep Copy

**Difficulty:** ⭐⭐ Intermediate → ⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand how list copying works.
- [ ] Understand the difference between assignment and copying.
- [ ] Use the `copy()` method.
- [ ] Copy a list using slicing.
- [ ] Understand shallow copying.
- [ ] Understand deep copying.
- [ ] Avoid unexpected changes to copied lists.

---

# 📖 Why Do We Need to Copy Lists?

Suppose we have:

```python
original = [10, 20, 30]
```

We want another list containing the same values.

We might try:

```python
copy_list = original
```

But this does **not actually create a separate list**.

This is one of the most important concepts when working with mutable objects in Python.

---

# 📌 Part 1: Assignment Using `=`

When you use:

```python
copy_list = original
```

both variables refer to the **same list object**.

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

Why did `original` change?

Because both variables refer to the **same list**.

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

There is only **one list** in memory.

---

# 📖 Checking with `id()`

```python
original = [10, 20, 30]

copy_list = original

print(id(original))
print(id(copy_list))
```

The IDs will be the same.

This confirms that both variables refer to the same object.

---

# 📌 Part 2: `copy()` Method

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

copy_list.append(40)

print(original)
print(copy_list)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

Now the lists are independent.

---

# 🧠 Visual Representation

```text
original ───────→ [10, 20, 30]

copy_list ──────→ [10, 20, 30, 40]
```

There are **two separate list objects**.

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

# 📌 Part 3: Copying Using Slicing

You can also create a copy using:

```python
original[:]
```

Example:

```python
original = [10, 20, 30]

copy_list = original[:]

copy_list.append(40)

print(original)
print(copy_list)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

This creates a new list.

---

# 📊 Three Common Techniques

| Technique | Creates New List? | Independent Outer List? |
|---|---:|---:|
| `copy_list = original` | ❌ | ❌ |
| `copy_list = original.copy()` | ✅ | ✅ |
| `copy_list = original[:]` | ✅ | ✅ |

---

# 📌 Part 4: Shallow Copy

The `copy()` method creates a **shallow copy**.

For a simple list containing immutable values, this usually behaves exactly as expected.

```python
original = [10, 20, 30]

copy_list = original.copy()

copy_list[0] = 100

print(original)
print(copy_list)
```

Output:

```text
[10, 20, 30]
[100, 20, 30]
```

The outer lists are separate.

---

# ⚠️ Shallow Copy with Nested Lists

Now consider:

```python
original = [
    [10, 20],
    [30, 40]
]

copy_list = original.copy()
```

The outer list is copied, but the **nested lists are still shared**.

---

## Example

```python
original = [
    [10, 20],
    [30, 40]
]

copy_list = original.copy()

copy_list[0].append(99)

print(original)
print(copy_list)
```

Output:

```text
[[10, 20, 99], [30, 40]]
[[10, 20, 99], [30, 40]]
```

Why?

Because the inner list `[10, 20]` is shared.

---

# 🧠 Shallow Copy Visualization

```text
              ┌───────────────┐
original ───→ │  outer list   │
              └───────┬───────┘
                      ↓
                   [10, 20] ←──── shared
                      ↑
              ┌───────┴───────┐
copy_list ──→ │  outer list   │
              └───────────────┘
```

The **outer lists are different**, but their nested objects can still be shared.

---

# 📌 Part 5: Deep Copy

A **deep copy** creates a completely independent copy, including nested objects.

Python provides the `copy` module for this.

```python
import copy
```

Then:

```python
copy.deepcopy()
```

---

# 📖 Example

```python
import copy

original = [
    [10, 20],
    [30, 40]
]

copy_list = copy.deepcopy(original)

copy_list[0].append(99)

print(original)
print(copy_list)
```

Output:

```text
[[10, 20], [30, 40]]
[[10, 20, 99], [30, 40]]
```

Now the nested lists are independent too.

---

# 🧠 Deep Copy Visualization

```text
original ───→ [ [10, 20], [30, 40] ]

copy_list ──→ [ [10, 20], [30, 40] ]

             ↑
       Completely separate
       nested objects
```

---

# 🔥 Shallow Copy vs Deep Copy

| Feature | Shallow Copy | Deep Copy |
|---|---|---|
| Outer list copied | ✅ | ✅ |
| Nested objects copied | ❌ | ✅ |
| Nested objects shared | Sometimes | ❌ |
| Method | `copy()` | `copy.deepcopy()` |
| Module required | ❌ | ✅ `copy` |

---

# 📊 Important Comparison

Consider:

```python
original = [
    [1, 2],
    [3, 4]
]
```

### Assignment

```python
new = original
```

➡️ Same outer list.

---

### Shallow Copy

```python
new = original.copy()
```

➡️ New outer list, shared nested lists.

---

### Slicing

```python
new = original[:]
```

➡️ New outer list, shared nested lists.

---

### Deep Copy

```python
import copy

new = copy.deepcopy(original)
```

➡️ New outer list and new nested lists.

---

# 📖 Example: Assignment

```python
original = [[1, 2], [3, 4]]

new = original

new[0].append(99)

print(original)
```

Output:

```text
[[1, 2, 99], [3, 4]]
```

---

# 📖 Example: Shallow Copy

```python
original = [[1, 2], [3, 4]]

new = original.copy()

new[0].append(99)

print(original)
```

Output:

```text
[[1, 2, 99], [3, 4]]
```

The nested list is shared.

---

# 📖 Example: Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

new = copy.deepcopy(original)

new[0].append(99)

print(original)
```

Output:

```text
[[1, 2], [3, 4]]
```

The original remains unchanged.

---

# 📌 Important: `copy()` vs `deepcopy()`

```python
original.copy()
```

creates a **shallow copy**.

```python
copy.deepcopy(original)
```

creates a **deep copy**.

---

# 🌍 Real-World Example: Student Records

Suppose we have:

```python
students = [
    ["Aisha", 85],
    ["Saniya", 92],
    ["Rohan", 78]
]
```

If we want a completely independent backup:

```python
import copy

backup = copy.deepcopy(students)
```

Now changes to `backup` won't affect the original nested records.

---

# 🌍 Real-World Example: Shopping Cart

```python
cart = [
    ["Laptop", 50000],
    ["Mouse", 1000]
]

backup_cart = cart.copy()
```

This creates a shallow copy.

For a completely independent nested cart:

```python
import copy

backup_cart = copy.deepcopy(cart)
```

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

## ❌ Mistake 2: Thinking `copy()` Deep-Copies Everything

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

## ❌ Mistake 3: Forgetting to Import `copy`

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

# 💡 Best Practices

### Use assignment when:

```python
new = original
```

You intentionally want both variables to refer to the **same list**.

### Use `copy()` when:

```python
new = original.copy()
```

You need a separate outer list.

### Use slicing when:

```python
new = original[:]
```

You want a quick shallow copy.

### Use `deepcopy()` when:

```python
new = copy.deepcopy(original)
```

You need completely independent nested objects.

---

# 📊 Quick Decision Guide

```text
Do I want another variable pointing to the same list?
                ↓
               YES
                ↓
         use: original


Do I need a separate list?
                ↓
               YES
                ↓
        Is it nested?
          ↙       ↘
        NO         YES
        ↓           ↓
   copy() / [:]   deepcopy()
```

---

# ❓ Interview Questions

- [ ] What happens when you assign one list to another using `=`?
- [ ] What does the `copy()` method do?
- [ ] What is a shallow copy?
- [ ] What is a deep copy?
- [ ] What is the difference between shallow and deep copying?
- [ ] How do you create a deep copy?
- [ ] Why can modifying a nested list affect a shallow copy?

---

# 🏋️ Practice Programs

## Easy

```python
numbers = [10, 20, 30]

new_numbers = numbers.copy()

new_numbers.append(40)

print(numbers)
print(new_numbers)
```

---

## Medium

```python
numbers = [10, 20, 30]

new_numbers = numbers[:]

new_numbers[0] = 100

print(numbers)
print(new_numbers)
```

---

## Assignment Practice

```python
numbers = [10, 20, 30]

new_numbers = numbers

new_numbers.append(40)

print("Original:", numbers)
print("New:", new_numbers)
```

Observe the output carefully.

---

## Advanced: Shallow Copy

```python
original = [
    [10, 20],
    [30, 40]
]

new = original.copy()

new[0].append(50)

print("Original:", original)
print("New:", new)
```

Predict the output before running the program.

---

## Advanced: Deep Copy

```python
import copy

original = [
    [10, 20],
    [30, 40]
]

new = copy.deepcopy(original)

new[0].append(50)

print("Original:", original)
print("New:", new)
```

Compare this result with the previous example.

---

# 🎯 Challenge

Write programs to:

1. Demonstrate why `=` does not create an independent copy.
2. Create a list copy using `copy()`.
3. Create a list copy using slicing.
4. Create a shallow copy of a nested list.
5. Create a deep copy of a nested list.
6. Modify the copied list and observe whether the original changes.

---

# 📝 Assignment

- [x] Demonstrate assignment using `=`.
- [x] Demonstrate `copy()`.
- [x] Demonstrate copying using `[:]`.
- [x] Demonstrate shallow copying with nested lists.
- [x] Demonstrate deep copying.
- [x] Compare `copy()` and `deepcopy()`.
- [x] Check object IDs using `id()`.
- [x] Explain why a shallow copy can still share nested objects.

---

# 📚 Summary

There are several ways to "copy" a list, but they don't all behave the same way.

### Assignment

```python
new = original
```

➡️ Both variables refer to the **same list**.

### `copy()`

```python
new = original.copy()
```

➡️ Creates a **shallow copy**.

### Slicing

```python
new = original[:]
```

➡️ Also creates a **shallow copy**.

### Deep Copy

```python
import copy

new = copy.deepcopy(original)
```

➡️ Creates a completely independent copy, including nested objects.

---

# 🧠 Easy Way to Remember

```text
= 
↓
Same object

copy()
↓
New outer list

[:]
↓
New outer list

deepcopy()
↓
Everything copied
```

---

# 🎯 Topic Completion Checklist

- [x] I understand assignment using `=`.
- [x] I understand `copy()`.
- [x] I understand slicing-based copying.
- [x] I understand shallow copy.
- [x] I understand deep copy.
- [x] I know when to use `copy()` and `deepcopy()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 4 (Part 6): Other Useful List Operations**

- `len()`
- `max()`
- `min()`
- `sum()`
- `any()`
- `all()`