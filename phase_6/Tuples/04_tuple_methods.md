# 🐍 Python Master Course

# 📦 Phase 6: Collections – Tuples

## 📌 Topic 4: Tuple Methods

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand tuple methods.
- [ ] Understand why tuples have fewer methods than lists.
- [ ] Use the `count()` method.
- [ ] Use the `index()` method.
- [ ] Understand the syntax of both methods.
- [ ] Use tuple methods with numbers.
- [ ] Use tuple methods with strings.
- [ ] Use tuple methods with mixed data.
- [ ] Handle `index()` errors.
- [ ] Use tuple methods in real-world programs.
- [ ] Practice tuple methods with different examples.

---

# 📖 What are Tuple Methods?

A **tuple method** is a built-in operation that can be called on a tuple to perform a specific task.

Python tuples have only **two built-in methods**:

| Method | Purpose |
|---|---|
| `count()` | Counts how many times a value occurs |
| `index()` | Finds the position of the first occurrence of a value |

The two methods are:

```python
count()
index()
```

---

# 🧠 Why Does a Tuple Have Only Two Methods?

Tuples are **immutable**.

This means that after creating a tuple, we cannot directly change its elements.

For example, tuples do not have methods such as:

```python
append()
remove()
insert()
pop()
clear()
sort()
reverse()
```

These methods modify a collection.

Since tuples cannot be modified, Python provides only methods that **look at or search the tuple**.

The two main methods are:

```python
count()
index()
```

---

# 📊 Tuple Methods Overview

| Method | Description | Changes Tuple? |
|---|---|---|
| `count()` | Counts occurrences | ❌ No |
| `index()` | Finds position | ❌ No |

Both methods return information about the tuple without modifying it.

---

# 1️⃣ `count()` Method

## 📖 What is `count()`?

The `count()` method returns the number of times a specified value appears in a tuple.

### Syntax

```python
tuple.count(value)
```

---

# 📌 Example 1: Counting Numbers

```python
numbers = (10, 20, 10, 30, 10, 40)

result = numbers.count(10)

print(result)
```

Output:

```text
3
```

The value `10` appears three times.

---

# 📌 Example 2: Counting Another Number

```python
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(20))
```

Output:

```text
1
```

---

# 📌 Example 3: Value Not Present

```python
numbers = (10, 20, 30, 40)

print(numbers.count(100))
```

Output:

```text
0
```

If the value does not exist, `count()` returns:

```text
0
```

---

# 📌 Example 4: Counting Strings

```python
languages = (
    "Python",
    "Java",
    "Python",
    "C",
    "Python"
)

print(languages.count("Python"))
```

Output:

```text
3
```

---

# 📌 Example 5: Counting Names

```python
names = (
    "Aisha",
    "Saniya",
    "Aisha",
    "Riya",
    "Aisha"
)

print(names.count("Aisha"))
```

Output:

```text
3
```

---

# 📌 Example 6: Counting Boolean Values

```python
values = (True, False, True, True, False)

print(values.count(True))
```

Output:

```text
3
```

---

# 📌 Example 7: Counting Zero

```python
numbers = (0, 1, 0, 2, 0, 3)

print(numbers.count(0))
```

Output:

```text
3
```

---

# 📌 Example 8: Counting Duplicate Marks

```python
marks = (80, 90, 75, 90, 85, 90)

print(marks.count(90))
```

Output:

```text
3
```

This tells us that three students or records have the mark `90`.

---

# 📌 Example 9: Counting a Product

```python
products = (
    "Laptop",
    "Mouse",
    "Keyboard",
    "Mouse",
    "Mouse"
)

print(products.count("Mouse"))
```

Output:

```text
3
```

---

# 📌 Example 10: Counting Items in a Tuple

```python
items = (
    "Pen",
    "Book",
    "Pen",
    "Pencil",
    "Pen",
    "Book"
)

print("Pen:", items.count("Pen"))
print("Book:", items.count("Book"))
print("Pencil:", items.count("Pencil"))
```

Output:

```text
Pen: 3
Book: 2
Pencil: 1
```

---

# 🧠 How `count()` Works

Consider:

```python
numbers = (10, 20, 10, 30, 10)
```

When we write:

```python
numbers.count(10)
```

Python checks every element:

```text
10 → Match ✅
20 → No
10 → Match ✅
30 → No
10 → Match ✅
```

Total matches:

```text
3
```

Therefore:

```python
numbers.count(10)
```

returns:

```text
3
```

---

# 2️⃣ `index()` Method

## 📖 What is `index()`?

The `index()` method returns the **index position of the first occurrence** of a specified value.

### Syntax

```python
tuple.index(value)
```

---

# 📌 Example 1: Find a Number

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

Output:

```text
2
```

Remember that Python indexing starts from `0`.

```text
10 → index 0
20 → index 1
30 → index 2
40 → index 3
```

---

# 📌 Example 2: Find a String

```python
languages = ("Python", "Java", "C", "JavaScript")

print(languages.index("C"))
```

Output:

```text
2
```

---

# 📌 Example 3: Find a Name

```python
names = ("Aisha", "Saniya", "Riya", "Meera")

print(names.index("Riya"))
```

Output:

```text
2
```

---

# 📌 Example 4: Duplicate Values

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.index(10))
```

Output:

```text
0
```

There are multiple `10`s, but `index()` returns the position of the **first occurrence**.

---

# 🧠 Understanding First Occurrence

Consider:

```python
numbers = (10, 20, 10, 30, 10)
```

Indexes:

```text
Value:  10   20   10   30   10
Index:   0    1    2    3    4
```

When we use:

```python
numbers.index(10)
```

Python finds the first `10`:

```text
10
↑
index 0
```

Therefore:

```text
0
```

---

# 📌 Example 5: Value Not Present

```python
numbers = (10, 20, 30)

print(numbers.index(100))
```

This produces:

```text
ValueError: tuple.index(x): x not in tuple
```

Unlike `count()`, `index()` raises an error if the value is not found.

---

# ⚠️ Important Difference

### `count()`

If the value doesn't exist:

```python
numbers.count(100)
```

returns:

```text
0
```

### `index()`

If the value doesn't exist:

```python
numbers.index(100)
```

raises:

```text
ValueError
```

---

# 📊 `count()` vs `index()`

| Feature | `count()` | `index()` |
|---|---|---|
| Purpose | Counts occurrences | Finds position |
| Return | Number | Index |
| Duplicate values | Counts all | Finds first |
| Value absent | Returns `0` | Raises `ValueError` |
| Modifies tuple? | ❌ No | ❌ No |

---

# 📌 `index()` with Duplicate Strings

```python
languages = (
    "Python",
    "Java",
    "Python",
    "C",
    "Python"
)

print(languages.index("Python"))
```

Output:

```text
0
```

It returns the first occurrence.

---

# 📌 Using `index()` with Start Position

Python's `index()` method can accept a starting position.

### Syntax

```python
tuple.index(value, start)
```

Example:

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.index(10, 1))
```

Output:

```text
2
```

Why?

Python starts searching from index `1`:

```text
Index:  0   1   2   3   4
Value: 10  20  10  30  10
            ↑
         start here
```

The next `10` is at index `2`.

---

# 📌 `index()` with Start and Stop

You can also provide a starting and ending position.

### Syntax

```python
tuple.index(value, start, stop)
```

Example:

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.index(10, 1, 4))
```

Output:

```text
2
```

Python searches from index `1` up to, but not including, index `4`.

---

# 📊 `index()` Parameters

```python
tuple.index(value)
```

Search the entire tuple.

```python
tuple.index(value, start)
```

Search from `start`.

```python
tuple.index(value, start, stop)
```

Search from `start` to `stop`.

---

# 📌 Example: Finding a Repeated Value

```python
numbers = (10, 20, 10, 30, 10, 40)

first = numbers.index(10)

second = numbers.index(10, first + 1)

third = numbers.index(10, second + 1)

print(first)
print(second)
print(third)
```

Output:

```text
0
2
4
```

This finds the first, second, and third occurrences.

---

# 📌 Using `count()` and `index()` Together

```python
numbers = (10, 20, 10, 30, 10)

value = 10

print("Count:", numbers.count(value))
print("First position:", numbers.index(value))
```

Output:

```text
Count: 3
First position: 0
```

---

# 🌍 Real-World Example 1: Student Marks

```python
marks = (85, 90, 78, 90, 92)

print("Number of students with 90:", marks.count(90))
print("First student with 90 is at index:", marks.index(90))
```

Output:

```text
Number of students with 90: 2
First student with 90 is at index: 1
```

---

# 🌍 Real-World Example 2: Product Orders

```python
orders = (
    "Laptop",
    "Mouse",
    "Keyboard",
    "Mouse",
    "Monitor"
)

print("Mouse orders:", orders.count("Mouse"))
print("First Mouse order index:", orders.index("Mouse"))
```

Output:

```text
Mouse orders: 2
First Mouse order index: 1
```

---

# 🌍 Real-World Example 3: Attendance

```python
attendance = (
    "Present",
    "Absent",
    "Present",
    "Present",
    "Absent"
)

print("Present:", attendance.count("Present"))
print("Absent:", attendance.count("Absent"))
```

Output:

```text
Present: 3
Absent: 2
```

---

# 🌍 Real-World Example 4: Website Visits

```python
pages = (
    "Home",
    "Products",
    "Home",
    "Contact",
    "Home"
)

print("Home visits:", pages.count("Home"))
print("First Home visit:", pages.index("Home"))
```

Output:

```text
Home visits: 3
First Home visit: 0
```

---

# 🌍 Real-World Example 5: Exam Results

```python
results = (
    "Pass",
    "Fail",
    "Pass",
    "Pass",
    "Fail"
)

passed = results.count("Pass")
failed = results.count("Fail")

print("Passed:", passed)
print("Failed:", failed)
```

Output:

```text
Passed: 3
Failed: 2
```

---

# 📌 Tuple Methods Do Not Modify the Tuple

Consider:

```python
numbers = (10, 20, 10, 30)

numbers.count(10)

print(numbers)
```

Output:

```text
(10, 20, 10, 30)
```

The tuple remains unchanged.

Similarly:

```python
numbers.index(20)

print(numbers)
```

Output:

```text
(10, 20, 10, 30)
```

---

# 🧠 Why Can't We Use List Methods?

This works with a list:

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

But this does not work with a tuple:

```python
numbers = (10, 20, 30)

numbers.append(40)
```

Output:

```text
AttributeError: 'tuple' object has no attribute 'append'
```

The reason is:

> Tuples are immutable.

---

# 📊 List Methods vs Tuple Methods

| Operation | List | Tuple |
|---|---:|---:|
| `append()` | ✅ | ❌ |
| `extend()` | ✅ | ❌ |
| `insert()` | ✅ | ❌ |
| `remove()` | ✅ | ❌ |
| `pop()` | ✅ | ❌ |
| `clear()` | ✅ | ❌ |
| `sort()` | ✅ | ❌ |
| `reverse()` | ✅ | ❌ |
| `count()` | ✅ | ✅ |
| `index()` | ✅ | ✅ |

---

# 📌 Built-in Functions That Work with Tuples

Although tuples have only two methods, many Python **built-in functions** work with tuples.

For example:

```python
numbers = (10, 20, 30, 40)
```

### `len()`

```python
print(len(numbers))
```

Output:

```text
4
```

---

### `max()`

```python
print(max(numbers))
```

Output:

```text
40
```

---

### `min()`

```python
print(min(numbers))
```

Output:

```text
10
```

---

### `sum()`

```python
print(sum(numbers))
```

Output:

```text
100
```

---

# ⚠️ Methods vs Functions

Remember that:

```python
numbers.count(10)
```

is a **method**.

But:

```python
len(numbers)
```

is a **built-in function**.

Similarly:

```python
max(numbers)
min(numbers)
sum(numbers)
```

are functions.

---

# 📊 Tuple Operations

| Operation | Example |
|---|---|
| Count value | `numbers.count(10)` |
| Find position | `numbers.index(10)` |
| Length | `len(numbers)` |
| Largest | `max(numbers)` |
| Smallest | `min(numbers)` |
| Total | `sum(numbers)` |

---

# 🧠 Important Difference: Method vs Function

### Method

Called using the object:

```python
numbers.count(10)
```

### Function

Passed the object as an argument:

```python
len(numbers)
```

---

# 🏋️ Practice Programs

## Beginner

### 1. Count a number

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

---

### 2. Find a number

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

---

### 3. Count a name

```python
names = ("Aisha", "Saniya", "Aisha", "Riya")

print(names.count("Aisha"))
```

---

### 4. Find a language

```python
languages = ("Python", "Java", "C", "Python")

print(languages.index("Python"))
```

---

### 5. Count marks

```python
marks = (80, 90, 90, 75, 90)

print(marks.count(90))
```

---

# 🏋️ Intermediate Practice

### 6. Count multiple values

```python
numbers = (10, 20, 10, 30, 20, 10)

print("10:", numbers.count(10))
print("20:", numbers.count(20))
print("30:", numbers.count(30))
```

---

### 7. Find first occurrence

```python
numbers = (5, 10, 15, 10, 20)

position = numbers.index(10)

print(position)
```

---

### 8. Find second occurrence

```python
numbers = (5, 10, 15, 10, 20)

first = numbers.index(10)
second = numbers.index(10, first + 1)

print(second)
```

---

### 9. Count attendance

```python
attendance = (
    "Present",
    "Absent",
    "Present",
    "Present",
    "Absent"
)

print("Present:", attendance.count("Present"))
print("Absent:", attendance.count("Absent"))
```

---

### 10. Product search

```python
products = (
    "Laptop",
    "Mouse",
    "Keyboard",
    "Mouse",
    "Monitor"
)

print("Mouse count:", products.count("Mouse"))
print("First Mouse:", products.index("Mouse"))
```

---

# 🚀 Advanced Practice

## Challenge 1: Find Repeated Values

Given:

```python
numbers = (10, 20, 10, 30, 20, 10, 40)
```

Find:

- Number of `10`s.
- Number of `20`s.
- First position of `10`.
- First position of `20`.

---

## Challenge 2: Search a Student

Given:

```python
students = (
    "Aisha",
    "Saniya",
    "Riya",
    "Saniya",
    "Meera"
)
```

Find:

- How many times `"Saniya"` appears.
- The first index of `"Saniya"`.

---

## Challenge 3: Analyze Marks

Given:

```python
marks = (85, 90, 75, 90, 92, 90, 80)
```

Find:

- How many students scored `90`.
- The first position of `90`.
- Total marks using `sum()`.
- Highest mark using `max()`.
- Lowest mark using `min()`.

---

# ❓ Interview Questions

- [ ] How many methods does a tuple have?
- [ ] What does `count()` do?
- [ ] What does `index()` do?
- [ ] What does `count()` return if the value is absent?
- [ ] What happens when `index()` cannot find a value?
- [ ] Does `index()` return the first or last occurrence?
- [ ] Can `index()` accept a starting position?
- [ ] Can `index()` accept both start and stop positions?
- [ ] Why doesn't a tuple have `append()`?
- [ ] What is the difference between a method and a built-in function?
- [ ] Is `len()` a tuple method?
- [ ] Can `sum()` be used with a tuple?
- [ ] Why does a tuple have fewer methods than a list?

---

# 📝 Quick Revision

## `count()`

Counts how many times a value occurs.

```python
numbers = (10, 20, 10, 30)

print(numbers.count(10))
```

Output:

```text
2
```

---

## `index()`

Returns the position of the first occurrence.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output:

```text
1
```

---

## `index()` with Start

```python
numbers = (10, 20, 10, 30)

print(numbers.index(10, 1))
```

Output:

```text
2
```

---

## `index()` with Start and Stop

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.index(10, 1, 4))
```

Output:

```text
2
```

---

# 🧠 Easy Memory Trick

Remember:

```text
count() → HOW MANY?
index() → WHERE?
```

Example:

```python
numbers = (10, 20, 10, 30)

numbers.count(10)
```

asks:

```text
How many 10s?
```

Result:

```text
2
```

And:

```python
numbers.index(10)
```

asks:

```text
Where is the first 10?
```

Result:

```text
0
```

---

# 🎯 Topic Completion Checklist

- [x] I understand tuple methods.
- [x] I know that tuples have two main methods.
- [x] I understand `count()`.
- [x] I can count duplicate values.
- [x] I understand `index()`.
- [x] I can find the first occurrence of a value.
- [x] I understand `index()` with `start`.
- [x] I understand `index()` with `start` and `stop`.
- [x] I know the difference between `count()` and `index()`.
- [x] I understand why tuple modification methods don't exist.
- [x] I know the difference between methods and functions.
- [x] I can use `len()`, `max()`, `min()`, and `sum()` with tuples.
- [x] I completed the practice programs.
- [x] I completed the challenges.

---

# 🎉 Tuple Topic Completed

You have now completed all four tuple topics:

- [x] Creating Tuples
- [x] Tuple Packing
- [x] Tuple Unpacking
- [x] Tuple Methods

---

# 🚀 Next Collection Topic

The next collection in your Python learning sequence is:

## 📌 Sets

Topics will include:

- [ ] Creating Sets
- [ ] Set Methods
- [ ] Set Operations
- [ ] Frozen set