# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 4 (Part 6): Other Useful List Operations**

**Functions Covered:**

- ✅ `len()`
- ✅ `max()`
- ✅ `min()`
- ✅ `sum()`
- ✅ `any()`
- ✅ `all()`

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Find the number of elements in a list.
- [ ] Find the largest value.
- [ ] Find the smallest value.
- [ ] Calculate the total of numerical values.
- [ ] Check whether at least one element is `True`.
- [ ] Check whether all elements are `True`.
- [ ] Use these functions in real-world programs.

---

# 📌 1. `len()`

## 📖 What is `len()`?

The `len()` function returns the **number of elements** in a list.

### Syntax

```python
len(list_name)
```

---

## Example 1

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

There are four elements.

---

## Example 2

```python
fruits = ["Apple", "Banana", "Mango"]

count = len(fruits)

print("Number of fruits:", count)
```

Output:

```text
Number of fruits: 3
```

---

## Example 3: Empty List

```python
numbers = []

print(len(numbers))
```

Output:

```text
0
```

---

# 🌍 Real-World Example

```python
students = ["Aisha", "Saniya", "Rohan", "Karan"]

print("Total Students:", len(students))
```

Output:

```text
Total Students: 4
```

---

# 📌 2. `max()`

## 📖 What is `max()`?

The `max()` function returns the **largest element** from a list.

### Syntax

```python
max(list_name)
```

---

## Example 1

```python
numbers = [10, 50, 30, 90, 20]

print(max(numbers))
```

Output:

```text
90
```

---

## Example 2: Marks

```python
marks = [75, 88, 92, 64, 81]

highest = max(marks)

print("Highest Marks:", highest)
```

Output:

```text
Highest Marks: 92
```

---

## Example 3: Strings

`max()` can also compare strings.

```python
names = ["Apple", "Banana", "Mango"]

print(max(names))
```

The result is based on Python's string comparison rules.

---

# ⚠️ Empty List

Using `max()` on an empty list causes an error.

```python
numbers = []

print(max(numbers))
```

Output:

```text
ValueError: max() arg is an empty sequence
```

You can check first:

```python
if numbers:
    print(max(numbers))
else:
    print("List is empty")
```

---

# 📌 3. `min()`

## 📖 What is `min()`?

The `min()` function returns the **smallest element** from a list.

### Syntax

```python
min(list_name)
```

---

## Example 1

```python
numbers = [10, 50, 30, 90, 20]

print(min(numbers))
```

Output:

```text
10
```

---

## Example 2: Marks

```python
marks = [75, 88, 92, 64, 81]

lowest = min(marks)

print("Lowest Marks:", lowest)
```

Output:

```text
Lowest Marks: 64
```

---

# 🌍 Real-World Example

```python
temperatures = [32, 35, 29, 31, 36]

print("Lowest Temperature:", min(temperatures))
```

Output:

```text
Lowest Temperature: 29
```

---

# 📌 4. `sum()`

## 📖 What is `sum()`?

The `sum()` function calculates the **total of numerical values** in a list.

### Syntax

```python
sum(list_name)
```

---

## Example 1

```python
numbers = [10, 20, 30, 40]

print(sum(numbers))
```

Output:

```text
100
```

---

## Example 2: Student Marks

```python
marks = [80, 75, 90, 85]

total = sum(marks)

print("Total Marks:", total)
```

Output:

```text
Total Marks: 330
```

---

# 📖 Calculating Average

`sum()` and `len()` can be combined to calculate an average.

```python
marks = [80, 75, 90, 85]

average = sum(marks) / len(marks)

print("Average:", average)
```

Output:

```text
Average: 82.5
```

---

# 📌 5. `any()`

## 📖 What is `any()`?

The `any()` function returns:

```text
True
```

if **at least one element** in the iterable is truthy.

Otherwise it returns:

```text
False
```

### Syntax

```python
any(list_name)
```

---

# 📖 Example 1

```python
values = [False, False, True, False]

print(any(values))
```

Output:

```text
True
```

Because at least one value is `True`.

---

# 📖 Example 2

```python
values = [False, False, False]

print(any(values))
```

Output:

```text
False
```

There are no truthy values.

---

# 🧠 Truthy and Falsy Values

Python considers values such as:

```python
0
False
None
""
[]
```

as **falsy**.

Most non-zero numbers and non-empty objects are **truthy**.

Example:

```python
values = [0, 0, 5, 0]

print(any(values))
```

Output:

```text
True
```

Because `5` is truthy.

---

# 🌍 Real-World Example

Suppose we have login attempts:

```python
login_status = [False, False, True, False]

if any(login_status):
    print("At least one login was successful")
```

Output:

```text
At least one login was successful
```

---

# 📌 6. `all()`

## 📖 What is `all()`?

The `all()` function returns:

```text
True
```

only when **all elements** are truthy.

### Syntax

```python
all(list_name)
```

---

# 📖 Example 1

```python
values = [True, True, True]

print(all(values))
```

Output:

```text
True
```

---

# 📖 Example 2

```python
values = [True, True, False]

print(all(values))
```

Output:

```text
False
```

Because one element is `False`.

---

# 🌍 Real-World Example

```python
payments = [True, True, True, True]

if all(payments):
    print("All payments completed")
```

Output:

```text
All payments completed
```

---

# 🔥 `any()` vs `all()`

This is extremely important.

### `any()`

Means:

> **At least one**

```python
values = [False, False, True]

print(any(values))
```

Output:

```text
True
```

---

### `all()`

Means:

> **Every one**

```python
values = [True, True, True]

print(all(values))
```

Output:

```text
True
```

---

# 📊 Comparison Table

| Function | Purpose | Example Result |
|---|---|---|
| `len()` | Number of elements | `4` |
| `max()` | Largest value | `90` |
| `min()` | Smallest value | `10` |
| `sum()` | Total | `150` |
| `any()` | At least one truthy | `True` |
| `all()` | Every value truthy | `True` |

---

# 📊 Example Using Multiple Functions

```python
marks = [80, 75, 90, 85, 95]

print("Number of Students:", len(marks))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))
```

Output:

```text
Number of Students: 5
Highest Marks: 95
Lowest Marks: 75
Total Marks: 425
Average Marks: 85.0
```

---

# 🌍 Real-World Example: Exam Results

```python
marks = [85, 76, 92, 68, 90]

total = sum(marks)
highest = max(marks)
lowest = min(marks)
average = total / len(marks)

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
```

---

# 🌍 Real-World Example: Attendance

Suppose:

```python
attendance = [True, True, False, True]
```

Check if at least one student is present:

```python
if any(attendance):
    print("At least one student is present")
```

Check whether everyone is present:

```python
if all(attendance):
    print("Everyone is present")
else:
    print("Some students are absent")
```

Output:

```text
At least one student is present
Some students are absent
```

---

# 📖 Combining `any()` with Conditions

You can use `any()` with a generator expression.

```python
marks = [45, 55, 32, 70]

if any(mark < 35 for mark in marks):
    print("At least one student failed")
```

Output:

```text
At least one student failed
```

---

# 📖 Combining `all()` with Conditions

```python
marks = [45, 55, 72, 70]

if all(mark >= 35 for mark in marks):
    print("Everyone passed")
else:
    print("Someone failed")
```

Output:

```text
Everyone passed
```

---

# 📌 Important: `all([])` and `any([])`

Python has a special behavior for an empty iterable.

```python
print(any([]))
```

Output:

```text
False
```

But:

```python
print(all([]))
```

Output:

```text
True
```

This may look strange at first, but it follows Python's definition of `all()` and `any()`.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Using `sum()` on Strings

```python
names = ["Aisha", "Rohan"]

print(sum(names))
```

This causes a `TypeError`.

`sum()` is intended for numerical values.

---

## ❌ Mistake 2: Using `max()` on an Empty List

```python
numbers = []

print(max(numbers))
```

This causes:

```text
ValueError
```

---

## ❌ Mistake 3: Confusing `any()` and `all()`

```python
values = [True, True, False]

print(any(values))
```

Output:

```text
True
```

But:

```python
print(all(values))
```

Output:

```text
False
```

Remember:

```text
any() → at least one
all() → every one
```

---

# 💡 Best Practices

Use:

```python
len()
```

when you need the number of elements.

Use:

```python
max()
```

when you need the largest value.

Use:

```python
min()
```

when you need the smallest value.

Use:

```python
sum()
```

when you need the total.

Use:

```python
any()
```

when one or more elements being true is enough.

Use:

```python
all()
```

when every element must be true.

---

# 🚀 Advanced Example

Check whether all students passed:

```python
marks = [45, 67, 82, 91, 56]

passed = all(mark >= 35 for mark in marks)

print(passed)
```

Output:

```text
True
```

---

# 🚀 Advanced Example

Check whether anyone failed:

```python
marks = [45, 67, 32, 91, 56]

failed = any(mark < 35 for mark in marks)

print(failed)
```

Output:

```text
True
```

---

# 🏋️ Practice Programs

## Easy

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
```

---

```python
numbers = [10, 50, 30, 90, 20]

print(max(numbers))
```

---

```python
numbers = [10, 50, 30, 90, 20]

print(min(numbers))
```

---

```python
numbers = [10, 20, 30]

print(sum(numbers))
```

---

## Medium

```python
marks = [80, 75, 90, 65, 85]

print("Total:", sum(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))
```

---

```python
attendance = [True, True, False, True]

print("Anyone Present:", any(attendance))
print("Everyone Present:", all(attendance))
```

---

## Advanced

```python
marks = [45, 67, 89, 72, 91]

if all(mark >= 35 for mark in marks):
    print("All students passed")
else:
    print("At least one student failed")
```

---

```python
marks = [45, 67, 32, 72, 91]

if any(mark < 35 for mark in marks):
    print("At least one student failed")
else:
    print("Everyone passed")
```

---

# 🎯 Challenge

Write programs to:

1. Find the number of elements in a list.
2. Find the highest number.
3. Find the lowest number.
4. Calculate the total.
5. Calculate the average.
6. Check whether at least one number is greater than `100`.
7. Check whether all numbers are positive.
8. Check whether at least one student failed.
9. Check whether all students passed.
10. Create a program using all six functions.

---

# 📝 Assignment

- [x] Practice `len()`.
- [x] Practice `max()`.
- [x] Practice `min()`.
- [x] Practice `sum()`.
- [x] Practice `any()`.
- [x] Practice `all()`.
- [x] Combine `sum()` and `len()` to calculate an average.
- [x] Use `any()` with a condition.
- [x] Use `all()` with a condition.
- [x] Create one real-world program using these functions.

---

# 📚 Summary

| Function | Remember It As |
|---|---|
| `len()` | **How many?** |
| `max()` | **Largest?** |
| `min()` | **Smallest?** |
| `sum()` | **Total?** |
| `any()` | **At least one?** |
| `all()` | **Everyone?** |

### Easy Memory Trick

```text
len() → COUNT
max() → BIGGEST
min() → SMALLEST
sum() → TOTAL
any() → ONE OR MORE
all() → EVERY ONE
```

---

# 🎯 Topic Completion Checklist

- [x] I understand `len()`.
- [x] I understand `max()`.
- [x] I understand `min()`.
- [x] I understand `sum()`.
- [x] I understand `any()`.
- [x] I understand `all()`.
- [x] I know the difference between `any()` and `all()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 5: Nested Lists**

- Creating Nested Lists
- Accessing Nested List Elements
- Nested List Indexing
- Modifying Nested Lists
- Nested List Traversal
- Nested Lists with Loops