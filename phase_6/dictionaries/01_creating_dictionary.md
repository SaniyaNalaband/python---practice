# 🐍 Python Master Course

# 📦 Phase 6: Collections – Dictionaries

## 📌 Topic 1: Creating Dictionary

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what a dictionary is.
* [ ] Understand the structure of a dictionary.
* [ ] Create dictionaries using `{}`.
* [ ] Understand keys and values.
* [ ] Create an empty dictionary.
* [ ] Create dictionaries with multiple key-value pairs.
* [ ] Use different data types as dictionary values.
* [ ] Understand the rules for dictionary keys.
* [ ] Create dictionaries using `dict()`.
* [ ] Create dictionaries from a list of tuples.
* [ ] Understand duplicate keys.
* [ ] Understand why dictionaries are different from sets.
* [ ] Create dictionaries for real-world data.
* [ ] Avoid common mistakes when creating dictionaries.

---

# 📖 1. What is a Dictionary?

A **dictionary** is a built-in Python data structure used to store data in **key-value pairs**.

Instead of accessing data using positions or indexes, dictionaries use **keys**.

Example:

```python id="w4u2qg"
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}

print(student)
```

Output:

```text id="q7h4j1"
{'name': 'Saniya', 'age': 20, 'course': 'BCA'}
```

Here:

```text id="u9r3qv"
"name"   → "Saniya"
"age"    → 20
"course" → "BCA"
```

The left side is the **key**.

The right side is the **value**.

---

# 🧠 2. Understanding Key-Value Pairs

A dictionary stores information like this:

```text id="v6o5ek"
key → value
```

Example:

```python id="j9k4e2"
student = {
    "name": "Saniya",
    "age": 20
}
```

Here:

```text id="m5w7tq"
"name" → "Saniya"
"age"  → 20
```

So:

* `"name"` is a key.
* `"Saniya"` is its value.
* `"age"` is a key.
* `20` is its value.

---

# 🏗️ 3. Basic Dictionary Syntax

The basic syntax is:

```python id="g3k8pd"
dictionary_name = {
    key: value,
    key: value
}
```

Example:

```python id="1b2y4a"
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}
```

---

# 🔑 4. What is a Key?

A **key** is used to identify a value inside a dictionary.

Example:

```python id="2l1z4v"
student = {
    "name": "Saniya",
    "age": 20
}
```

Keys are:

```text id="qj5s1c"
name
age
```

Values are:

```text id="w0w5c7"
Saniya
20
```

Think of it like a real dictionary:

```text id="b7w1ka"
Word → Meaning
```

Python dictionary:

```text id="7x4g0q"
Key → Value
```

---

# 💡 5. Simple Dictionary Example

```python id="g8t6cw"
person = {
    "name": "Asha",
    "age": 21,
    "city": "Bengaluru"
}

print(person)
```

Output:

```text id="9s7q5d"
{'name': 'Asha', 'age': 21, 'city': 'Bengaluru'}
```

---

# 📝 6. Creating an Empty Dictionary

You can create an empty dictionary using `{}`.

```python id="6v0q4m"
student = {}

print(student)
```

Output:

```text id="n8b4q1"
{}
```

The dictionary currently contains no key-value pairs.

---

# 🔍 7. Checking the Type

You can use `type()` to check whether an object is a dictionary.

```python id="k7y4t3"
student = {}

print(type(student))
```

Output:

```text id="c4x8s2"
<class 'dict'>
```

---

# ⚠️ 8. Empty Dictionary vs Empty Set

This is an important beginner concept.

```python id="x1v5k9"
data = {}
```

This creates an **empty dictionary**.

It does NOT create an empty set.

To create an empty set:

```python id="p4n8z6"
data = set()
```

To create an empty dictionary:

```python id="t3m7q2"
data = {}
```

Remember:

```text id="5d8h1r"
{}       → Empty dictionary
set()    → Empty set
```

---

# 📚 9. Dictionary with Multiple Items

A dictionary can contain many key-value pairs.

```python id="q5w8e1"
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA",
    "college": "ABC College",
    "year": 2
}

print(student)
```

Each pair is separated by a comma.

---

# 🔢 10. Dictionary with Different Value Types

Dictionary values can have different data types.

```python id="h3v7k2"
student = {
    "name": "Saniya",
    "age": 20,
    "percentage": 85.5,
    "passed": True
}

print(student)
```

Here:

```text id="k8m1z5"
"name"       → string
"age"        → integer
"percentage" → float
"passed"     → boolean
```

---

# 📦 11. Dictionary Values Can Be Lists

A dictionary value can also be a list.

```python id="p8r3w6"
student = {
    "name": "Saniya",
    "skills": ["Python", "SQL", "Git"]
}

print(student)
```

Output:

```text id="a6n4c2"
{'name': 'Saniya', 'skills': ['Python', 'SQL', 'Git']}
```

---

# 📦 12. Dictionary Values Can Be Tuples

```python id="d7q2m9"
student = {
    "name": "Asha",
    "coordinates": (12.97, 77.59)
}

print(student)
```

Output:

```text id="v1f8x4"
{'name': 'Asha', 'coordinates': (12.97, 77.59)}
```

---

# 📦 13. Dictionary Values Can Be Sets

```python id="r6w3k8"
student = {
    "name": "Neha",
    "skills": {"Python", "SQL", "Git"}
}

print(student)
```

The value can be a set.

---

# 📦 14. Dictionary Values Can Be Dictionaries

A dictionary can contain another dictionary as a value.

```python id="y4t8p1"
student = {
    "name": "Asha",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(student)
```

This is called a **nested dictionary**.

Nested dictionaries will be studied in detail in a later topic.

---

# 🔑 15. Rules for Dictionary Keys

Dictionary keys must be **hashable**.

Common examples of valid keys include:

```python id="n2f7c4"
data = {
    "name": "Asha",
    1: "One",
    2.5: "Two Point Five",
    True: "Yes",
    (1, 2): "Tuple"
}

print(data)
```

Strings, integers, floats, booleans, and tuples can be used as keys when they are hashable.

---

# ❌ 16. Lists Cannot Be Dictionary Keys

This is invalid:

```python id="k5r8v2"
data = {
    [1, 2, 3]: "Numbers"
}
```

It produces an error because lists are mutable and unhashable.

Typical error:

```text id="u6p3m9"
TypeError: unhashable type: 'list'
```

---

# ❌ 17. Sets Cannot Be Dictionary Keys

This is also invalid:

```python id="z8q4w1"
data = {
    {1, 2, 3}: "Numbers"
}
```

A normal set is mutable and unhashable.

---

# 🧠 18. Why Must Keys Be Hashable?

Dictionaries use a **hash table** internally to quickly find values using keys.

Therefore, dictionary keys need to be hashable.

Simple rule:

```text id="a7m2x5"
Hashable
   ↓
Can generally be used as a dictionary key

Not hashable
   ↓
Cannot be used as a dictionary key
```

Examples:

```text id="c9v4n6"
String     → ✅
Integer    → ✅
Float      → ✅
Boolean    → ✅
Tuple      → ✅
List       → ❌
Set        → ❌
Dictionary → ❌
```

---

# 🔢 19. Numeric Keys

Dictionary keys do not have to be strings.

You can use integers.

```python id="w3k8p5"
marks = {
    1: 85,
    2: 90,
    3: 78
}

print(marks)
```

Here:

```text id="y6r1t4"
1 → 85
2 → 90
3 → 78
```

---

# 🔤 20. String Keys

String keys are the most common type of dictionary key.

```python id="q9m5v2"
student = {
    "name": "Asha",
    "course": "BCA",
    "city": "Bengaluru"
}
```

---

# 🔀 21. Mixed Key Types

Python allows different hashable types as keys.

```python id="x4c7n8"
data = {
    "name": "Asha",
    1: "One",
    2.5: "Decimal",
    True: "Boolean"
}

print(data)
```

However, using consistent key types often makes your code easier to understand.

---

# ⚠️ 22. Duplicate Dictionary Keys

Dictionary keys must be unique.

Consider:

```python id="e8k2r6"
student = {
    "name": "Asha",
    "age": 20,
    "name": "Neha"
}

print(student)
```

Output:

```text id="b3m7q9"
{'name': 'Neha', 'age': 20}
```

The second `"name"` replaces the first `"name"` value.

---

# 🧠 23. What Happens with Duplicate Keys?

Python keeps the **last value** assigned to a duplicate key.

Example:

```python id="v5t1k8"
data = {
    "score": 50,
    "score": 75,
    "score": 90
}

print(data)
```

Output:

```text id="s2q6m4"
{'score': 90}
```

Only the last value remains.

---

# ⚠️ 24. Important: Duplicate Values Are Allowed

Keys must be unique, but values do not need to be unique.

Example:

```python id="j8p4w2"
students = {
    "student1": "Python",
    "student2": "Python",
    "student3": "SQL"
}

print(students)
```

This is perfectly valid.

Here:

```text id="r6n1y5"
Keys   → Unique
Values → Can repeat
```

---

# 🏷️ 25. Dictionary with Student Information

A dictionary is excellent for representing structured information.

```python id="u7c3m9"
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA",
    "semester": 4,
    "percentage": 86.5
}

print(student)
```

This is much easier to understand than storing unrelated values separately.

---

# 🌍 26. Real-World Example: Product

```python id="p4k8s2"
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 55000,
    "in_stock": True
}

print(product)
```

The dictionary represents information about a product.

---

# 🌍 27. Real-World Example: Employee

```python id="n6w3q9"
employee = {
    "id": 101,
    "name": "Asha",
    "department": "IT",
    "salary": 45000
}

print(employee)
```

---

# 🌍 28. Real-World Example: Mobile Phone

```python id="x8r5m1"
phone = {
    "brand": "Samsung",
    "model": "Galaxy",
    "price": 45000,
    "storage": "256GB"
}

print(phone)
```

---

# 🌍 29. Real-World Example: Book

```python id="c2v7k4"
book = {
    "title": "Python Basics",
    "author": "John Smith",
    "pages": 350,
    "price": 499
}

print(book)
```

---

# 🏗️ 30. Creating a Dictionary Using `dict()`

You can also create a dictionary using the built-in `dict()` function.

Example:

```python id="m5q8w3"
student = dict(
    name="Asha",
    age=20,
    course="BCA"
)

print(student)
```

Output:

```text id="h7n2c6"
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

---

# 🔍 31. `dict()` Function Syntax

The basic syntax is:

```python id="k9r4v1"
dict(**kwargs)
```

Example:

```python id="t6p3x8"
person = dict(
    name="Neha",
    age=21,
    city="Mysuru"
)

print(person)
```

---

# ⚖️ 32. `{}` vs `dict()`

Both can create dictionaries.

### Using `{}`

```python id="f2m7q5"
student = {
    "name": "Asha",
    "age": 20
}
```

### Using `dict()`

```python id="z8c4n1"
student = dict(
    name="Asha",
    age=20
)
```

Both create dictionaries.

---

# 🧠 33. When Should You Use `{}`?

The `{}` syntax is commonly used when you want to write key-value pairs directly.

```python id="v5k2r7"
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}
```

It is clear and easy to read.

---

# 🧠 34. When Should You Use `dict()`?

`dict()` is useful when:

* Creating a dictionary from keyword arguments.
* Converting another iterable into a dictionary.
* Dynamically creating dictionaries.

Example:

```python id="q4w8m3"
student = dict(
    name="Asha",
    age=20
)
```

---

# 🧩 35. Creating a Dictionary from Tuples

You can create a dictionary from a sequence of key-value pairs.

Example:

```python id="y7n2p5"
student = dict([
    ("name", "Asha"),
    ("age", 20),
    ("course", "BCA")
])

print(student)
```

Output:

```text id="c3v8k1"
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

Each tuple contains:

```text id="m6q4r9"
(key, value)
```

---

# 🧩 36. Creating a Dictionary from a List of Tuples

```python id="r1t7w5"
data = [
    ("Python", 90),
    ("SQL", 85),
    ("Git", 80)
]

marks = dict(data)

print(marks)
```

Output:

```text id="x4p9c2"
{'Python': 90, 'SQL': 85, 'Git': 80}
```

---

# 🧩 37. Creating a Dictionary from Two Lists

You can use `zip()` with `dict()`.

Example:

```python id="n8k3v6"
keys = ["name", "age", "course"]

values = ["Asha", 20, "BCA"]

student = dict(zip(keys, values))

print(student)
```

Output:

```text id="q5m7r1"
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

Here:

```text id="w2c8p4"
name   → Asha
age    → 20
course → BCA
```

---

# 🧠 38. Understanding `zip()`

`zip()` pairs elements from two sequences.

Example:

```python id="f6v1k9"
keys = ["name", "age"]

values = ["Asha", 20]

print(list(zip(keys, values)))
```

Output:

```text id="b3r8t5"
[('name', 'Asha'), ('age', 20)]
```

Then:

```python id="k7m2q4"
student = dict(zip(keys, values))
```

converts those pairs into a dictionary.

---

# ⚠️ 39. Unequal Lists with `zip()`

If the lists have different lengths:

```python id="p5x8n2"
keys = ["name", "age", "course"]

values = ["Asha", 20]

student = dict(zip(keys, values))

print(student)
```

Output:

```text id="j9c4v7"
{'name': 'Asha', 'age': 20}
```

The unmatched `"course"` key is ignored because there is no corresponding value.

---

# 🏗️ 40. Creating a Dictionary with `fromkeys()`

Python provides `dict.fromkeys()` to create a dictionary using a sequence of keys.

Example:

```python id="w4r7m1"
keys = ["name", "age", "course"]

student = dict.fromkeys(keys)

print(student)
```

Output:

```text id="q6n3v8"
{'name': None, 'age': None, 'course': None}
```

---

# 🔢 41. `fromkeys()` with a Common Value

You can provide a value for all keys.

```python id="t8p2k5"
subjects = ["Python", "SQL", "Git"]

marks = dict.fromkeys(subjects, 0)

print(marks)
```

Output:

```text id="m4v9c1"
{'Python': 0, 'SQL': 0, 'Git': 0}
```

Every key receives the same initial value.

---

# 🧠 42. Dictionary Creation Summary

There are several ways to create dictionaries.

### Method 1: Curly Braces

```python id="q7w3n8"
student = {
    "name": "Asha",
    "age": 20
}
```

### Method 2: `dict()`

```python id="x2m6r4"
student = dict(
    name="Asha",
    age=20
)
```

### Method 3: List of Tuples

```python id="k9p5v1"
student = dict([
    ("name", "Asha"),
    ("age", 20)
])
```

### Method 4: `zip()`

```python id="c4t8m2"
keys = ["name", "age"]
values = ["Asha", 20]

student = dict(zip(keys, values))
```

### Method 5: `fromkeys()`

```python id="r6w1q9"
keys = ["name", "age"]

student = dict.fromkeys(keys)
```

---

# 📊 43. Dictionary Creation Methods

| Method            | Example                    | Best Used For          |
| ----------------- | -------------------------- | ---------------------- |
| `{}`              | `{"name": "Asha"}`         | Direct creation        |
| `dict()`          | `dict(name="Asha")`        | Keyword-based creation |
| `dict()` + tuples | `dict([("name", "Asha")])` | Key-value pairs        |
| `dict(zip())`     | `dict(zip(keys, values))`  | Two sequences          |
| `dict.fromkeys()` | `dict.fromkeys(keys)`      | Same initial value     |

---

# ⚠️ 44. Common Mistakes

## ❌ Mistake 1: Forgetting the Colon

Wrong:

```python id="f5r8k2"
student = {
    "name" "Asha",
    "age" 20
}
```

Correct:

```python id="m7q3v9"
student = {
    "name": "Asha",
    "age": 20
}
```

The colon separates the key and value:

```text id="z1c6w4"
key : value
```

---

## ❌ Mistake 2: Using `=` Instead of `:`

Wrong:

```python id="u8n2p5"
student = {
    "name" = "Asha"
}
```

Correct:

```python id="j4r7m1"
student = {
    "name": "Asha"
}
```

---

## ❌ Mistake 3: Using a List as a Key

Wrong:

```python id="k3v9q6"
data = {
    [1, 2]: "Numbers"
}
```

Lists are unhashable.

---

## ❌ Mistake 4: Duplicate Keys

```python id="p7m2x8"
data = {
    "name": "Asha",
    "name": "Neha"
}

print(data)
```

Output:

```text id="c5w9r3"
{'name': 'Neha'}
```

The last value replaces the earlier value.

---

## ❌ Mistake 5: Confusing Dictionary and Set

This:

```python id="a6t1k4"
data = {"Python", "SQL", "Git"}
```

is a **set**.

This:

```python id="m8q3v7"
data = {
    "language": "Python",
    "database": "SQL"
}
```

is a **dictionary**.

The colon `:` is the key difference.

---

# 🔑 45. Dictionary vs Set

| Feature               | Dictionary         | Set                 |
| --------------------- | ------------------ | ------------------- |
| Stores                | Key-value pairs    | Values              |
| Syntax                | `{key: value}`     | `{value}`           |
| Uses `:`              | ✅                  | ❌                   |
| Duplicate keys/values | Keys unique        | Elements unique     |
| Example               | `{"name": "Asha"}` | `{"Python", "SQL"}` |
| Empty `{}`            | Dictionary         | ❌                   |
| Empty creation        | `{}`               | `set()`             |

---

# 🌍 46. Real-World Example: Student Record

```python id="x5p8n2"
student = {
    "id": 101,
    "name": "Asha",
    "age": 20,
    "course": "BCA",
    "skills": [
        "Python",
        "SQL",
        "Git"
    ]
}

print(student)
```

This dictionary represents a complete student record.

---

# 🌍 47. Real-World Example: Product Record

```python id="r3m7v1"
product = {
    "id": 501,
    "name": "Laptop",
    "price": 55000,
    "brand": "Dell",
    "available": True
}

print(product)
```

---

# 🌍 48. Real-World Example: Employee Record

```python id="q8c2k5"
employee = {
    "employee_id": 1001,
    "name": "Neha",
    "department": "Development",
    "experience": 2,
    "remote": True
}

print(employee)
```

---

# 💻 49. Practice Programs

## 🟢 Easy

### Program 1: Create a Student Dictionary

```python id="w4n8p2"
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

print(student)
```

---

### Program 2: Create a Product Dictionary

```python id="m6r1v9"
product = {
    "name": "Laptop",
    "price": 50000,
    "brand": "Dell"
}

print(product)
```

---

### Program 3: Create an Empty Dictionary

```python id="t2q7k4"
data = {}

print(data)
print(type(data))
```

---

### Program 4: Dictionary with Different Value Types

```python id="p9c5x3"
data = {
    "name": "Asha",
    "age": 20,
    "percentage": 85.5,
    "passed": True
}

print(data)
```

---

# 🟡 Medium

### Program 5: Dictionary Using `dict()`

```python id="v7m2r8"
student = dict(
    name="Asha",
    age=20,
    course="BCA"
)

print(student)
```

---

### Program 6: Dictionary from Tuples

```python id="k4n8w1"
data = [
    ("Python", 90),
    ("SQL", 85),
    ("Git", 80)
]

marks = dict(data)

print(marks)
```

---

### Program 7: Dictionary Using `zip()`

```python id="q3p6t9"
keys = ["name", "age", "course"]

values = ["Asha", 20, "BCA"]

student = dict(zip(keys, values))

print(student)
```

---

### Program 8: Dictionary Using `fromkeys()`

```python id="r8c1m5"
subjects = ["Python", "SQL", "Git"]

marks = dict.fromkeys(subjects, 0)

print(marks)
```

---

# 🔴 Advanced

## Program 9: Student Database Record

```python id="x7v3k2"
student = {
    "id": 101,
    "name": "Asha",
    "age": 20,
    "course": "BCA",
    "skills": [
        "Python",
        "SQL",
        "Git"
    ],
    "percentage": 87.5,
    "passed": True
}

print(student)
```

---

## Program 10: Creating Multiple Student Records

```python id="n5q8r4"
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    },

    "student2": {
        "name": "Neha",
        "age": 21
    }
}

print(students)
```

This introduces the idea of **nested dictionaries**, which will be covered in detail later.

---

# 🏆 50. Challenge

Create a dictionary representing a product.

It should contain:

```text id="u2m7c9"
product_id
name
brand
price
category
in_stock
rating
features
```

Example structure:

```python id="f6p1x8"
product = {
    "product_id": 101,
    "name": "Laptop",
    "brand": "Dell",
    "price": 55000,
    "category": "Electronics",
    "in_stock": True,
    "rating": 4.5,
    "features": [
        "16GB RAM",
        "512GB SSD",
        "WiFi"
    ]
}

print(product)
```

Try creating your own product without copying the example.

---

# 🧪 51. Mini Project: Student Profile

Create a student profile using a dictionary.

Your dictionary should contain:

* Student ID
* Name
* Age
* Course
* Semester
* Percentage
* Skills
* Passed status

Example:

```python id="z4r8m2"
student = {
    "student_id": 101,
    "name": "Asha",
    "age": 20,
    "course": "BCA",
    "semester": 4,
    "percentage": 85.5,
    "skills": [
        "Python",
        "SQL",
        "Git"
    ],
    "passed": True
}

print(student)
```

### Your Goal

Create your own student profile using different values.

---

# 🎤 52. Interview Questions

* [ ] What is a dictionary in Python?
* [ ] What is a key-value pair?
* [ ] How do you create a dictionary?
* [ ] How do you create an empty dictionary?
* [ ] What is the difference between `{}` and `set()`?
* [ ] Can dictionary keys be duplicated?
* [ ] What happens when a dictionary contains duplicate keys?
* [ ] Can dictionary values be duplicated?
* [ ] What data types can be used as dictionary keys?
* [ ] Can a list be used as a dictionary key?
* [ ] Why must dictionary keys be hashable?
* [ ] Can a dictionary contain a list as a value?
* [ ] Can a dictionary contain another dictionary as a value?
* [ ] What is the `dict()` function?
* [ ] How can you create a dictionary using `zip()`?
* [ ] What does `dict.fromkeys()` do?
* [ ] What is the difference between a dictionary and a set?
* [ ] Can dictionary values have different data types?
* [ ] Are dictionary keys and values the same thing?
* [ ] What happens if two keys have the same value?

---

# 📝 53. Assignment

Complete the following programs.

### Task 1

Create a dictionary containing:

```text
name
age
city
```

---

### Task 2

Create a dictionary representing a laptop.

Include:

```text
brand
model
price
RAM
storage
```

---

### Task 3

Create an empty dictionary and verify its type using `type()`.

---

### Task 4

Create a dictionary using the `dict()` function.

---

### Task 5

Create a dictionary from a list of tuples.

---

### Task 6

Create two lists:

```python id="n6q3w8"
keys = [...]
values = [...]
```

Use `zip()` and `dict()` to create a dictionary.

---

### Task 7

Create a dictionary using `dict.fromkeys()`.

---

### Task 8

Create a dictionary containing values of different data types.

Use:

```text
string
integer
float
boolean
list
tuple
set
```

---

### Task 9

Create a dictionary with duplicate keys.

Observe what happens.

---

### Task 10

Create a real-world student profile using a dictionary.

---

# 🧠 54. Memory Tricks

Remember the basic structure:

```text id="q4m7x1"
Dictionary

     key
      ↓
   "name" : "Asha"
            ↑
          value
```

Think:

> **Key identifies the data, and value stores the data.**

---

Remember the syntax:

```text id="r8p2k6"
{
    key : value
}
```

The colon `:` separates the key and value.

---

Remember the uniqueness rule:

```text id="w5c9n3"
Keys   → Must be unique
Values → Can be duplicated
```

---

# 📌 55. Important Rules to Remember

```text
1. Dictionaries store key-value pairs.

2. Dictionaries are created using {} or dict().

3. Each key is separated from its value using :.

4. Key-value pairs are separated using commas.

5. Dictionary keys must be hashable.

6. Dictionary keys must be unique.

7. Dictionary values can be duplicated.

8. Dictionary values can contain different data types.

9. Lists can be values but cannot normally be keys.

10. Sets can be values but cannot normally be keys.

11. Dictionaries can contain other dictionaries.

12. {} creates an empty dictionary.

13. set() creates an empty set.

14. Duplicate keys result in the last value being retained.
```

---

# 📊 56. Dictionary Structure

```text
                    DICTIONARY
                         │
                         ↓
                  Key-Value Pairs
                         │
             ┌───────────┴───────────┐
             ↓                       ↓
            KEY                    VALUE
             │                       │
       Must be unique        Can be duplicated
       Must be hashable       Any appropriate type
             │                       │
             ↓                       ↓
        "name"                  "Asha"
        "age"                     20
        "course"                 "BCA"
```

---

# 📚 57. Complete Dictionary Creation Cheat Sheet

### Basic Dictionary

```python id="p7v3k9"
student = {
    "name": "Asha",
    "age": 20
}
```

### Empty Dictionary

```python id="c4m8r1"
student = {}
```

### Using `dict()`

```python id="x6q2w5"
student = dict(
    name="Asha",
    age=20
)
```

### From Tuples

```python id="n9t4k7"
student = dict([
    ("name", "Asha"),
    ("age", 20)
])
```

### Using `zip()`

```python id="m3p8v2"
keys = ["name", "age"]
values = ["Asha", 20]

student = dict(zip(keys, values))
```

### Using `fromkeys()`

```python id="w5r1c6"
keys = ["name", "age"]

student = dict.fromkeys(keys)
```

---

# 🏆 58. Dictionary Creation Mastery

```text
                 CREATE DICTIONARY
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
         {}           dict()       fromkeys()
          │             │             │
          ↓             ↓             ↓
    Direct pairs    Keyword data    Same value
          │
          └──────────────┐
                         ↓
                       zip()
                         │
                         ↓
                 Two sequences
                  → Key + Value
```

---

# 📚 59. Summary

In this lesson, you learned:

* What a dictionary is.
* What key-value pairs are.
* How to create dictionaries using `{}`.
* How to create empty dictionaries.
* How to check dictionary types.
* The difference between empty dictionaries and empty sets.
* How to create dictionaries with multiple key-value pairs.
* How dictionary values can contain different data types.
* The rules for dictionary keys.
* Why dictionary keys must be hashable.
* Why lists and sets cannot normally be dictionary keys.
* How duplicate keys behave.
* Why dictionary values can be duplicated.
* How to create dictionaries using `dict()`.
* How to create dictionaries from lists of tuples.
* How to use `zip()` with `dict()`.
* How to use `dict.fromkeys()`.
* How to create dictionaries for real-world data.
* The difference between dictionaries and sets.
* Common mistakes when creating dictionaries.

---

# 🎯 Topic Completion Checklist

* [ ] I know what a dictionary is.
* [ ] I understand key-value pairs.
* [ ] I can create a dictionary using `{}`.
* [ ] I can create an empty dictionary.
* [ ] I know the difference between `{}` and `set()`.
* [ ] I understand dictionary keys.
* [ ] I understand dictionary values.
* [ ] I know that dictionary keys must be unique.
* [ ] I understand duplicate keys.
* [ ] I know that values can be duplicated.
* [ ] I understand which types can be dictionary keys.
* [ ] I understand why lists cannot be dictionary keys.
* [ ] I understand why sets cannot be dictionary keys.
* [ ] I can create dictionaries using `dict()`.
* [ ] I can create dictionaries from tuples.
* [ ] I can use `zip()` to create a dictionary.
* [ ] I understand `dict.fromkeys()`.
* [ ] I can create real-world dictionaries.
* [ ] I understand the difference between dictionaries and sets.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can create dictionaries without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Accessing Dictionary Values**

In the next topic, you will learn:

* How to access dictionary values.
* Accessing values using keys.
* Using square brackets `[]`.
* Using the `get()` method.
* Difference between `[]` and `get()`.
* Handling missing keys.
* Accessing values from dictionaries containing lists.
* Accessing values from nested dictionaries.
* Practical examples and challenges.

---

## ⭐ Quote of the Day

> **"A dictionary connects a key to its value, making it easy to organize and retrieve related information."** 🐍📚
