````markdown
# 🐍 Python Master Course

# 📦 Phase 6: Collections – Sets

## 📌 Topic 1: Creating Sets

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand what a Set is.
- [ ] Create a Set using curly braces `{}`.
- [ ] Create a Set using the `set()` constructor.
- [ ] Understand that Sets are unordered.
- [ ] Understand that Sets do not allow duplicate values.
- [ ] Create Sets containing different data types.
- [ ] Create an empty Set correctly.
- [ ] Understand the difference between `{}` and `set()`.
- [ ] Convert other collections into Sets.
- [ ] Create Sets from strings, lists, tuples, and ranges.
- [ ] Understand Set mutability.
- [ ] Use Sets in real-world situations.
- [ ] Identify common mistakes when creating Sets.

---

# 📖 What is a Set?

A **Set** is a built-in Python collection used to store multiple values.

A Set has three important characteristics:

1. **Unordered**
2. **No duplicate elements**
3. **Mutable**

Example:

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

---

# 📌 Basic Syntax

A Set is commonly created using curly braces:

```python
set_name = {value1, value2, value3}
```

Example:

```python
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

Output:

```text
{'Apple', 'Banana', 'Mango'}
```

> The order in which Set elements are displayed should not be relied upon.

---

# 🧠 Characteristics of Sets

## 1. Sets are Unordered

Sets do not maintain elements based on a fixed positional order.

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

You should not assume that the elements will always be displayed in the same order.

---

## 2. Sets Do Not Allow Duplicates

Consider:

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

The duplicate values are automatically removed.

---

## 3. Sets Are Mutable

A Set can be changed after it has been created.

For example:

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

The Set itself can be modified.

---

# 📌 Creating a Set with Numbers

```python
numbers = {10, 20, 30, 40, 50}

print(numbers)
```

Output:

```text
{10, 20, 30, 40, 50}
```

---

# 📌 Creating a Set with Strings

```python
languages = {"Python", "Java", "C", "JavaScript"}

print(languages)
```

Output:

```text
{'Python', 'Java', 'C', 'JavaScript'}
```

---

# 📌 Creating a Set with Floats

```python
prices = {99.5, 149.99, 250.75}

print(prices)
```

---

# 📌 Creating a Set with Boolean Values

```python
values = {True, False}

print(values)
```

Output:

```text
{False, True}
```

---

# 📌 Creating a Mixed Set

A Set can contain different hashable data types.

```python
data = {10, "Python", 3.14, True}

print(data)
```

The Set contains:

```text
Integer
String
Float
Boolean
```

---

# ⚠️ Important: Mutable Objects Cannot Be Set Elements

A Set can contain immutable/hashable objects such as:

```python
10
"Python"
3.14
(1, 2)
```

But mutable objects such as lists cannot normally be elements of a Set.

### ❌ Incorrect

```python
data = {[1, 2], [3, 4]}
```

This produces:

```text
TypeError: unhashable type: 'list'
```

---

# 📌 Set with a Tuple

A tuple can be an element of a Set because tuples can be hashable when their contents are hashable.

```python
data = {(10, 20), (30, 40)}

print(data)
```

Output:

```text
{(10, 20), (30, 40)}
```

---

# 📌 Creating an Empty Set

This is a very important concept.

You might think:

```python
empty = {}
```

creates an empty Set.

But it does not.

```python
empty = {}

print(type(empty))
```

Output:

```text
<class 'dict'>
```

`{}` creates an empty **dictionary**.

---

# ✅ Correct Way to Create an Empty Set

Use:

```python
empty = set()

print(type(empty))
```

Output:

```text
<class 'set'>
```

---

# 📊 `{}` vs `set()`

| Code | Type |
|---|---|
| `{}` | Dictionary |
| `set()` | Empty Set |
| `{10, 20}` | Set |
| `{"Python", "Java"}` | Set |

---

# 📌 Creating a Set Using `set()`

Python provides the `set()` constructor.

Syntax:

```python
set(iterable)
```

Example:

```python
numbers = set([10, 20, 30])

print(numbers)
```

Output:

```text
{10, 20, 30}
```

---

# 📌 Creating a Set from a List

```python
numbers = [10, 20, 30, 20, 10]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output:

```text
{10, 20, 30}
```

The duplicate values are removed.

---

# 📌 Creating a Set from a Tuple

```python
numbers = (10, 20, 30, 20, 10)

unique_numbers = set(numbers)

print(unique_numbers)
```

Output:

```text
{10, 20, 30}
```

---

# 📌 Creating a Set from a String

A string is an iterable, so it can be passed to `set()`.

```python
letters = set("Python")

print(letters)
```

The Set contains the unique characters from the string.

For example:

```text
{'P', 'y', 't', 'h', 'o', 'n'}
```

The order is not guaranteed.

---

# 📌 Duplicate Characters

```python
letters = set("banana")

print(letters)
```

Output contains only unique characters:

```text
{'b', 'a', 'n'}
```

The repeated `a` and `n` characters are removed.

---

# 📌 Creating a Set from a Range

```python
numbers = set(range(1, 6))

print(numbers)
```

Output:

```text
{1, 2, 3, 4, 5}
```

---

# 📌 Creating a Set from User Input

Suppose the user enters:

```text
10 20 30 20 10
```

We can create a Set of unique values:

```python
values = input("Enter numbers: ").split()

numbers = set(values)

print(numbers)
```

Example output:

```text
{'10', '20', '30'}
```

Notice that the values are strings because `input()` returns strings.

---

# 📌 Converting Input to Integers

```python
values = input("Enter numbers: ").split()

numbers = {int(value) for value in values}

print(numbers)
```

If the input is:

```text
10 20 30 20 10
```

Output:

```text
{10, 20, 30}
```

---

# 🧠 Set Automatically Removes Duplicates

Consider:

```python
numbers = {10, 10, 20, 20, 30, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

Think of it as:

```text
Original values:
10 10 20 20 30 30

       ↓

Remove duplicates

       ↓

10 20 30

       ↓

Set

{10, 20, 30}
```

---

# 📌 Creating a Set from a List to Remove Duplicates

This is one of the most common uses of Sets.

```python
numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output:

```text
{10, 20, 30, 40}
```

---

# 🌍 Real-World Example 1: Unique Student Names

Suppose a registration system contains duplicate names:

```python
students = [
    "Aisha",
    "Saniya",
    "Aisha",
    "Riya",
    "Saniya"
]

unique_students = set(students)

print(unique_students)
```

The Set contains only unique names.

---

# 🌍 Real-World Example 2: Unique Products

```python
products = [
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse"
]

unique_products = set(products)

print(unique_products)
```

Output contains:

```text
Laptop
Mouse
Keyboard
```

---

# 🌍 Real-World Example 3: Unique Website Visitors

```python
visitors = [
    "user101",
    "user205",
    "user101",
    "user309",
    "user205"
]

unique_visitors = set(visitors)

print(unique_visitors)
```

The Set stores each visitor only once.

---

# 🌍 Real-World Example 4: Unique Courses

```python
courses = [
    "Python",
    "Java",
    "Python",
    "Machine Learning",
    "Java"
]

unique_courses = set(courses)

print(unique_courses)
```

---

# 🌍 Real-World Example 5: Unique Tags

```python
tags = [
    "python",
    "programming",
    "python",
    "coding",
    "programming"
]

unique_tags = set(tags)

print(unique_tags)
```

Output contains only unique tags.

---

# 📌 Set Length

Use the `len()` function to find the number of elements in a Set.

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

Output:

```text
4
```

---

# 📌 Length After Removing Duplicates

```python
numbers = {10, 20, 10, 30, 20, 40}

print(len(numbers))
```

Output:

```text
4
```

Although six values were written, only four unique values exist.

---

# 📌 Set with Duplicate Values

```python
numbers = {1, 1, 2, 2, 3, 3}

print(numbers)
print(len(numbers))
```

Output:

```text
{1, 2, 3}
3
```

---

# 📌 Set Does Not Use Indexing

Because Sets are unordered, you cannot access elements using indexes like:

```python
numbers = {10, 20, 30}

print(numbers[0])
```

This produces an error because Sets do not support positional indexing.

### ❌ Incorrect

```python
numbers[0]
```

### ✅ Correct approach

You can iterate through the Set:

```python
for number in numbers:
    print(number)
```

---

# 📌 Set and List Comparison

```python
numbers_list = [10, 20, 10, 30]
numbers_set = {10, 20, 10, 30}

print(numbers_list)
print(numbers_set)
```

Output:

```text
[10, 20, 10, 30]
{10, 20, 30}
```

The List keeps duplicates.

The Set removes duplicates.

---

# 📊 List vs Set

| Feature | List | Set |
|---|---|---|
| Ordered | Yes | No |
| Duplicates | Allowed | Not allowed |
| Mutable | Yes | Yes |
| Indexing | Yes | No |
| Slicing | Yes | No |
| Uses `[]` | Yes | No |
| Uses `{}` | No | Yes |
| Empty collection | `[]` | `set()` |

---

# 📌 Set with `set()`

The `set()` constructor accepts an iterable.

Examples:

```python
set([1, 2, 3])
```

```python
set((1, 2, 3))
```

```python
set("hello")
```

```python
set(range(5))
```

---

# 📊 Converting Collections to Sets

| Original | Code |
|---|---|
| List | `set([1, 2, 3])` |
| Tuple | `set((1, 2, 3))` |
| String | `set("hello")` |
| Range | `set(range(5))` |

---

# 📌 Set from a Dictionary

When a dictionary is passed to `set()`, its keys are used.

```python
student = {
    "name": "Aisha",
    "age": 21,
    "course": "BCA"
}

keys = set(student)

print(keys)
```

The Set contains the dictionary keys:

```text
{'name', 'age', 'course'}
```

---

# 📌 Set from Dictionary Keys

You can also explicitly use:

```python
student = {
    "name": "Aisha",
    "age": 21,
    "course": "BCA"
}

keys = set(student.keys())

print(keys)
```

---

# 📌 Set from Dictionary Values

```python
student = {
    "math": 90,
    "science": 85,
    "english": 90
}

values = set(student.values())

print(values)
```

Output:

```text
{90, 85}
```

The duplicate `90` is removed.

---

# 🧠 Important: Set Elements Must Be Hashable

Set elements must generally be **hashable**.

Examples of commonly hashable values:

```python
10
3.14
"Python"
True
(1, 2)
```

Examples that are not hashable:

```python
[1, 2]
{"a": 1}
```

Therefore:

```python
numbers = {[1, 2], [3, 4]}
```

is invalid.

---

# 📌 Set of Tuples

This works:

```python
points = {(10, 20), (30, 40), (50, 60)}

print(points)
```

Each tuple is hashable because its elements are hashable.

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Using `{}` for an Empty Set

```python
empty = {}
```

This creates a dictionary.

Correct:

```python
empty = set()
```

---

## ❌ Mistake 2: Trying to Use Indexing

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Sets do not support indexing.

---

## ❌ Mistake 3: Expecting Duplicates

```python
numbers = {10, 20, 10, 30}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

Duplicates are automatically removed.

---

## ❌ Mistake 4: Adding a List as an Element

```python
data = {[1, 2], [3, 4]}
```

This causes:

```text
TypeError: unhashable type: 'list'
```

---

## ❌ Mistake 5: Expecting a Fixed Display Order

Do not write programs that depend on a particular printed order of a Set.

For example:

```python
numbers = {30, 10, 20}

print(numbers)
```

The displayed order should not be treated as meaningful.

---

# 📌 Checking the Type

Use `type()`:

```python
numbers = {10, 20, 30}

print(type(numbers))
```

Output:

```text
<class 'set'>
```

---

# 📌 Set vs Frozenset

Python has two related collection types:

### Set

```python
numbers = {10, 20, 30}
```

A Set is mutable.

### Frozenset

```python
numbers = frozenset([10, 20, 30])
```

A Frozenset is immutable.

For now, focus on normal Sets.

---

# 🏋️ Practice Programs

## Beginner Practice

### 1. Create a Set of numbers

```python
numbers = {10, 20, 30, 40, 50}

print(numbers)
```

---

### 2. Create a Set of strings

```python
languages = {"Python", "Java", "C"}

print(languages)
```

---

### 3. Create a Set with duplicates

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Observe how duplicates are removed.

---

### 4. Create an empty Set

```python
numbers = set()

print(numbers)
print(type(numbers))
```

---

### 5. Convert a List to a Set

```python
numbers = [10, 20, 10, 30, 20]

unique_numbers = set(numbers)

print(unique_numbers)
```

---

# 🏋️ Intermediate Practice

### 6. Remove duplicate names

```python
names = [
    "Aisha",
    "Saniya",
    "Aisha",
    "Riya",
    "Saniya"
]

unique_names = set(names)

print(unique_names)
```

---

### 7. Create a Set from a String

```python
letters = set("programming")

print(letters)
```

---

### 8. Create a Set from a Tuple

```python
numbers = (10, 20, 30, 20, 10)

unique_numbers = set(numbers)

print(unique_numbers)
```

---

### 9. Create a Set from a Range

```python
numbers = set(range(1, 11))

print(numbers)
```

---

### 10. Count unique values

```python
numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = set(numbers)

print("Unique values:", unique_numbers)
print("Number of unique values:", len(unique_numbers))
```

---

# 🚀 Advanced Practice

## Challenge 1: Unique Student Names

Given:

```python
students = [
    "Aisha",
    "Saniya",
    "Riya",
    "Aisha",
    "Meera",
    "Saniya"
]
```

Create a Set containing only unique student names.

---

## Challenge 2: Unique Numbers

Given:

```python
numbers = [
    10, 20, 30, 10, 40,
    20, 50, 30, 60, 10
]
```

Create a Set and find the number of unique values.

---

## Challenge 3: Unique Characters

Given:

```python
word = "programming"
```

Create a Set containing the unique characters.

---

## Challenge 4: Unique Courses

Given:

```python
courses = [
    "Python",
    "Java",
    "Python",
    "Machine Learning",
    "Java",
    "Python"
]
```

Create a Set of unique courses.

---

## Challenge 5: User Input

Ask the user to enter several numbers separated by spaces.

Example:

```text
Enter numbers: 10 20 10 30 20 40
```

Create a Set containing only unique numbers.

---

# ❓ Interview Questions

- [ ] What is a Set in Python?
- [ ] How do you create a Set?
- [ ] What are the main characteristics of Sets?
- [ ] Are Sets ordered?
- [ ] Can a Set contain duplicate values?
- [ ] Are Sets mutable?
- [ ] How do you create an empty Set?
- [ ] Why does `{}` create a dictionary instead of a Set?
- [ ] Can Sets use indexing?
- [ ] Can a Set contain a list?
- [ ] Why can't a list be a Set element?
- [ ] Can a Set contain a tuple?
- [ ] What happens when you convert a List to a Set?
- [ ] What happens when you convert a String to a Set?
- [ ] What is the difference between a Set and a Frozenset?

---

# 📝 Quick Revision

## Create a Set

```python
numbers = {10, 20, 30}
```

---

## Create an Empty Set

```python
numbers = set()
```

---

## Create a Set from a List

```python
numbers = set([10, 20, 30])
```

---

## Remove Duplicates

```python
numbers = [10, 20, 10, 30]

unique = set(numbers)

print(unique)
```

---

## Set from String

```python
letters = set("hello")
```

---

## Set from Tuple

```python
numbers = set((10, 20, 30))
```

---

## Set from Range

```python
numbers = set(range(1, 6))
```

---

## Check Type

```python
numbers = {10, 20, 30}

print(type(numbers))
```

Output:

```text
<class 'set'>
```

---

# 🧠 Easy Memory Trick

Remember:

```text
SET
 ↓
Unique Values
 ↓
No Duplicates
 ↓
Unordered
 ↓
Mutable
```

And remember:

```python
{}       # Dictionary
set()    # Empty Set
{1, 2, 3}  # Set
```

### ⭐ Most Important Rule

> **Use `set()` to create an empty Set. `{}` creates an empty dictionary.**

---

# 🎯 Topic Completion Checklist

- [x] I understand what a Set is.
- [x] I know how to create a Set.
- [x] I understand that Sets do not allow duplicates.
- [x] I understand that Sets are unordered.
- [x] I understand that Sets are mutable.
- [x] I can create an empty Set.
- [x] I understand `{}` vs `set()`.
- [x] I can convert a List into a Set.
- [x] I can convert a Tuple into a Set.
- [x] I can convert a String into a Set.
- [x] I can convert a Range into a Set.
- [x] I understand why Lists cannot be Set elements.
- [x] I understand why Tuples can be Set elements in appropriate cases.
- [x] I can use Sets to remove duplicates.
- [x] I completed the practice programs.
- [x] I completed the challenges.

---

# 🎉 Topic Progress

## 📦 Phase 6: Collections

### Tuples

- [x] Creating Tuples
- [x] Tuple Packing
- [x] Tuple Unpacking
- [x] Tuple Methods

### Sets

- [x] Creating Sets
- [ ] Set Methods
- [ ] Set Operations
- [ ] Set Comprehension

---


