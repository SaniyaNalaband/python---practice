# 🐍 Python Master Course

# 📦 Phase 6: Collections – Dictionaries

## 📌 Topic 2: Accessing Dictionary Values

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand how dictionary values are accessed.
* [ ] Access dictionary values using keys.
* [ ] Use square brackets `[]` to access values.
* [ ] Understand how dictionary keys work when accessing values.
* [ ] Use the `get()` method.
* [ ] Understand the difference between `[]` and `get()`.
* [ ] Handle missing keys.
* [ ] Use default values with `get()`.
* [ ] Access values of different data types.
* [ ] Access values stored inside lists.
* [ ] Access values stored inside tuples.
* [ ] Access values stored inside sets.
* [ ] Access values stored inside dictionaries.
* [ ] Access values from nested dictionaries.
* [ ] Access multiple dictionary values.
* [ ] Use dictionary access in real-world programs.
* [ ] Avoid common mistakes when accessing dictionary values.

---

# 📖 1. What Does Accessing a Dictionary Value Mean?

A dictionary stores data in **key-value pairs**.

To retrieve a value from a dictionary, we use its **key**.

Example:

```python
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
```

Output:

```text
Saniya
```

Here:

```text
"name" → key
"Saniya" → value
```

We use the key `"name"` to access its value `"Saniya"`.

---

# 🔑 2. Accessing Values Using Keys

The most basic way to access a dictionary value is by using the key inside square brackets `[]`.

Syntax:

```python
dictionary_name[key]
```

Example:

```python
student = {
    "name": "Saniya",
    "age": 20
}

print(student["name"])
print(student["age"])
```

Output:

```text
Saniya
20
```

The key tells Python which value we want.

---

# 🏗️ 3. Basic Syntax for Accessing Values

The basic syntax is:

```python
dictionary_name[key]
```

Example:

```python
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}

print(student["course"])
```

Output:

```text
BCA
```

Here:

```text
student → dictionary
"course" → key
"BCA" → value
```

---

# 🔍 4. Accessing a Single Value

You can access one particular value using its key.

Example:

```python
person = {
    "name": "Asha",
    "age": 21,
    "city": "Bengaluru"
}

print(person["city"])
```

Output:

```text
Bengaluru
```

Only the value associated with `"city"` is returned.

---

# 📚 5. Accessing Multiple Values

You can access multiple values by using their keys separately.

Example:

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
print(student["age"])
print(student["course"])
```

Output:

```text
Asha
20
BCA
```

Each key retrieves its corresponding value.

---

# 🔢 6. Accessing Values Using Numeric Keys

Dictionary keys do not have to be strings.

You can also use integers as keys.

Example:

```python
marks = {
    1: 85,
    2: 90,
    3: 78
}

print(marks[1])
print(marks[2])
print(marks[3])
```

Output:

```text
85
90
78
```

Here:

```text
1 → 85
2 → 90
3 → 78
```

---

# 🔤 7. Accessing Values Using String Keys

String keys are very common in Python dictionaries.

Example:

```python
student = {
    "name": "Asha",
    "course": "BCA",
    "city": "Mysuru"
}

print(student["name"])
print(student["course"])
```

Output:

```text
Asha
BCA
```

---

# 🧠 8. Dictionary Access Is Different from List Indexing

Lists use **positions/indexes**.

Dictionaries use **keys**.

List:

```python
names = ["Asha", "Neha", "Priya"]

print(names[0])
```

Output:

```text
Asha
```

Dictionary:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student["name"])
```

Output:

```text
Asha
```

Remember:

```text
List       → Index
Dictionary → Key
```

---

# 🔑 9. Accessing Values Does Not Use Numerical Position

A dictionary is not normally accessed using the position of an item.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student["name"])
```

This is correct.

You should not think of `"name"` as position `0`.

The key itself identifies the value.

---

# ⚠️ 10. What Happens If the Key Does Not Exist?

Consider:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student["city"])
```

There is no `"city"` key.

Python produces an error:

```text
KeyError: 'city'
```

This happens because square brackets require the key to exist.

---

# ❌ 11. Understanding KeyError

A `KeyError` occurs when you try to access a dictionary using a key that does not exist.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student["course"])
```

Output:

```text
KeyError: 'course'
```

The key `"course"` does not exist.

---

# 🛡️ 12. Using `get()` to Access Values

Python provides the `get()` method to access dictionary values.

Syntax:

```python
dictionary_name.get(key)
```

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("name"))
```

Output:

```text
Asha
```

---

# 🧠 13. How `get()` Works

The `get()` method searches for the specified key.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("age"))
```

Output:

```text
20
```

It finds the key `"age"` and returns its value.

---

# ⚖️ 14. `[]` vs `get()`

There are two common ways to access dictionary values.

### Using `[]`

```python
student = {
    "name": "Asha"
}

print(student["name"])
```

### Using `get()`

```python
student = {
    "name": "Asha"
}

print(student.get("name"))
```

Both produce:

```text
Asha
```

However, they behave differently when the key does not exist.

---

# ⚠️ 15. `[]` with a Missing Key

Example:

```python
student = {
    "name": "Asha"
}

print(student["city"])
```

Output:

```text
KeyError: 'city'
```

Square brackets raise a `KeyError` when the key is missing.

---

# 🛡️ 16. `get()` with a Missing Key

Example:

```python
student = {
    "name": "Asha"
}

print(student.get("city"))
```

Output:

```text
None
```

Instead of producing a `KeyError`, `get()` returns `None` by default.

---

# 🔢 17. Using `get()` with a Default Value

You can provide a default value to `get()`.

Syntax:

```python
dictionary_name.get(key, default_value)
```

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("city", "Not Available"))
```

Output:

```text
Not Available
```

The key `"city"` does not exist, so the default value is returned.

---

# 💡 18. Why Use a Default Value?

Default values are useful when a key may not exist.

Example:

```python
product = {
    "name": "Laptop",
    "price": 55000
}

print(product.get("brand", "Brand not provided"))
```

Output:

```text
Brand not provided
```

This prevents the program from failing because of a missing key.

---

# 🔍 19. `get()` When the Key Exists

If the key exists, `get()` returns the actual value.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("age", 0))
```

Output:

```text
20
```

The default value `0` is not used because `"age"` exists.

---

# 🧠 20. Important Difference Between `[]` and `get()`

Remember:

```text
dictionary[key]
```

If key exists:

```text
→ Returns value
```

If key does not exist:

```text
→ KeyError
```

With:

```text
dictionary.get(key)
```

If key exists:

```text
→ Returns value
```

If key does not exist:

```text
→ Returns None
```

---

# 📊 21. `[]` vs `get()` Comparison

| Feature                | `[]`          | `get()`         |
| ---------------------- | ------------- | --------------- |
| Access existing key    | ✅             | ✅               |
| Missing key            | `KeyError`    | `None`          |
| Supports default value | ❌             | ✅               |
| Syntax                 | `data[key]`   | `data.get(key)` |
| Useful for safe access | Less suitable | More suitable   |

---

# 🧩 22. Accessing String Values

Example:

```python
student = {
    "name": "Asha",
    "course": "BCA"
}

name = student["name"]
course = student["course"]

print(name)
print(course)
```

Output:

```text
Asha
BCA
```

---

# 🔢 23. Accessing Integer Values

Example:

```python
student = {
    "age": 20,
    "semester": 4
}

print(student["age"])
print(student["semester"])
```

Output:

```text
20
4
```

---

# 🔢 24. Accessing Float Values

Example:

```python
student = {
    "percentage": 85.5,
    "cgpa": 8.7
}

print(student["percentage"])
print(student["cgpa"])
```

Output:

```text
85.5
8.7
```

---

# ✅ 25. Accessing Boolean Values

Example:

```python
student = {
    "passed": True,
    "active": False
}

print(student["passed"])
print(student["active"])
```

Output:

```text
True
False
```

---

# 📦 26. Accessing a List Stored as a Value

A dictionary value can be a list.

Example:

```python
student = {
    "name": "Asha",
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"])
```

Output:

```text
['Python', 'SQL', 'Git']
```

The complete list is returned.

---

# 🔍 27. Accessing an Individual List Item Inside a Dictionary

You can access an individual list item by combining dictionary access and list indexing.

Example:

```python
student = {
    "name": "Asha",
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"][0])
```

Output:

```text
Python
```

Here:

```text
student["skills"] → accesses the list
[0]               → accesses the first list item
```

---

# 🔢 28. Accessing Different List Items

Example:

```python
student = {
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"][0])
print(student["skills"][1])
print(student["skills"][2])
```

Output:

```text
Python
SQL
Git
```

---

# 📦 29. Accessing a Tuple Stored as a Value

A dictionary can contain a tuple as a value.

Example:

```python
student = {
    "coordinates": (12.97, 77.59)
}

print(student["coordinates"])
```

Output:

```text
(12.97, 77.59)
```

---

# 🔍 30. Accessing an Individual Tuple Item

You can combine dictionary access with tuple indexing.

Example:

```python
student = {
    "coordinates": (12.97, 77.59)
}

print(student["coordinates"][0])
print(student["coordinates"][1])
```

Output:

```text
12.97
77.59
```

---

# 📦 31. Accessing a Set Stored as a Value

A dictionary can contain a set as a value.

Example:

```python
student = {
    "skills": {"Python", "SQL", "Git"}
}

print(student["skills"])
```

Output:

```text
{'Python', 'SQL', 'Git'}
```

The exact display order of a set is not guaranteed.

---

# 📦 32. Accessing a Dictionary Stored as a Value

A dictionary can contain another dictionary as a value.

Example:

```python
student = {
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(student["address"])
```

Output:

```text
{'city': 'Bengaluru', 'state': 'Karnataka'}
```

This is called a **nested dictionary**.

---

# 🔍 33. Accessing a Value from a Nested Dictionary

You can access the inner value by using multiple keys.

Example:

```python
student = {
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(student["address"]["city"])
```

Output:

```text
Bengaluru
```

Here:

```text
student["address"]        → inner dictionary
["city"]                  → value inside inner dictionary
```

---

# 🏗️ 34. Accessing Multiple Nested Values

Example:

```python
student = {
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "pincode": 560001
    }
}

print(student["address"]["city"])
print(student["address"]["state"])
print(student["address"]["pincode"])
```

Output:

```text
Bengaluru
Karnataka
560001
```

---

# 🧠 35. Accessing Deeply Nested Dictionaries

A dictionary can contain dictionaries inside dictionaries.

Example:

```python
company = {
    "employee": {
        "address": {
            "city": "Bengaluru",
            "state": "Karnataka"
        }
    }
}

print(company["employee"]["address"]["city"])
```

Output:

```text
Bengaluru
```

The access path is:

```text
company
   ↓
employee
   ↓
address
   ↓
city
   ↓
Bengaluru
```

---

# 📝 36. Storing an Accessed Value in a Variable

You do not have to print the value directly.

You can store it in another variable.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

name = student["name"]

print(name)
```

Output:

```text
Asha
```

---

# 🔄 37. Updating a Variable Using an Accessed Value

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

age = student["age"]

print("Student age:", age)
```

Output:

```text
Student age: 20
```

---

# 🔁 38. Accessing Values in a Loop

You can use dictionary keys to access values inside a loop.

Example:

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key, "=", student[key])
```

Output:

```text
name = Asha
age = 20
course = BCA
```

The loop gives each key, which can then be used to access its value.

---

# 🧠 39. Accessing Values Using `get()` in a Loop

Example:

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key, "=", student.get(key))
```

Output:

```text
name = Asha
age = 20
course = BCA
```

---

# ⚠️ 40. Common Mistake: Using the Value Instead of the Key

Consider:

```python
student = {
    "name": "Asha",
    "age": 20
}
```

Wrong:

```python
print(student["Asha"])
```

This produces:

```text
KeyError: 'Asha'
```

Why?

Because `"Asha"` is a value, not a key.

Correct:

```python
print(student["name"])
```

Output:

```text
Asha
```

---

# ⚠️ 41. Common Mistake: Using the Wrong Key

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student["Name"])
```

This causes:

```text
KeyError: 'Name'
```

Dictionary keys are case-sensitive.

These are different:

```text
"name"
"Name"
"NAME"
```

---

# 🔤 42. Dictionary Keys Are Case-Sensitive

Example:

```python
student = {
    "name": "Asha"
}

print(student["name"])
```

Correct output:

```text
Asha
```

But:

```python
print(student["Name"])
```

produces:

```text
KeyError: 'Name'
```

The capitalization must match the key exactly.

---

# ⚠️ 43. Common Mistake: Using Parentheses Instead of Square Brackets

Wrong:

```python
student = {
    "name": "Asha"
}

print(student("name"))
```

This is incorrect.

Correct:

```python
print(student["name"])
```

For dictionary access, use square brackets `[]`.

---

# ⚠️ 44. Common Mistake: Forgetting Quotes Around String Keys

Consider:

```python
student = {
    "name": "Asha"
}
```

Correct:

```python
print(student["name"])
```

Do not write:

```python
print(student[name])
```

unless `name` is a variable containing the intended key.

---

# 🧠 45. Using a Variable as a Dictionary Key

A key can also be stored inside a variable.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

key = "name"

print(student[key])
```

Output:

```text
Asha
```

Here:

```text
key → "name"
```

Therefore:

```text
student[key] → student["name"]
```

---

# 🔍 46. Using `get()` with a Variable

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

key = "age"

print(student.get(key))
```

Output:

```text
20
```

---

# 🛡️ 47. Checking for a Key Before Accessing Its Value

You can use the `in` operator to check whether a key exists.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

if "name" in student:
    print(student["name"])
```

Output:

```text
Asha
```

---

# ⚠️ 48. Checking a Missing Key Before Accessing

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

if "city" in student:
    print(student["city"])
else:
    print("City is not available")
```

Output:

```text
City is not available
```

This prevents a `KeyError`.

---

# 🧠 49. `in` Checks Keys

When used directly with a dictionary, `in` checks for keys.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print("name" in student)
print("city" in student)
```

Output:

```text
True
False
```

---

# ⚠️ 50. `in` Does Not Directly Check Values

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

print("Asha" in student)
```

Output:

```text
False
```

The dictionary contains `"Asha"` as a value, not as a key.

---

# 🌍 51. Real-World Example: Student Record

```python
student = {
    "id": 101,
    "name": "Asha",
    "age": 20,
    "course": "BCA",
    "percentage": 86.5
}

print(student["name"])
print(student["course"])
print(student["percentage"])
```

Output:

```text
Asha
BCA
86.5
```

---

# 🌍 52. Real-World Example: Product

```python
product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 55000,
    "in_stock": True
}

print(product["name"])
print(product["price"])
print(product["in_stock"])
```

Output:

```text
Laptop
55000
True
```

---

# 🌍 53. Real-World Example: Employee

```python
employee = {
    "id": 101,
    "name": "Neha",
    "department": "IT",
    "salary": 45000
}

print(employee["name"])
print(employee["department"])
print(employee["salary"])
```

Output:

```text
Neha
IT
45000
```

---

# 🌍 54. Real-World Example: Mobile Phone

```python
phone = {
    "brand": "Samsung",
    "model": "Galaxy",
    "price": 45000,
    "storage": "256GB"
}

print(phone["brand"])
print(phone["model"])
print(phone["storage"])
```

Output:

```text
Samsung
Galaxy
256GB
```

---

# 🌍 55. Real-World Example: Book

```python
book = {
    "title": "Python Basics",
    "author": "John Smith",
    "pages": 350,
    "price": 499
}

print(book["title"])
print(book["author"])
print(book["price"])
```

Output:

```text
Python Basics
John Smith
499
```

---

# 🧩 56. Real-World Example: Accessing a List Inside a Dictionary

```python
student = {
    "name": "Asha",
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"])
print(student["skills"][0])
print(student["skills"][1])
```

Output:

```text
['Python', 'SQL', 'Git']
Python
SQL
```

---

# 🧩 57. Real-World Example: Accessing a Nested Dictionary

```python
student = {
    "name": "Asha",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(student["address"]["city"])
print(student["address"]["state"])
```

Output:

```text
Bengaluru
Karnataka
```

---

# 🧠 58. Understanding the Access Path

Consider:

```python
student = {
    "name": "Asha",
    "address": {
        "city": "Bengaluru"
    }
}

print(student["address"]["city"])
```

Break it down:

```text
student
   ↓
["address"]
   ↓
Inner dictionary
   ↓
["city"]
   ↓
"Bengaluru"
```

So:

```text
student["address"]["city"]
```

returns:

```text
Bengaluru
```

---

# 📊 59. Accessing Different Types of Values

```python
data = {
    "name": "Asha",
    "age": 20,
    "percentage": 85.5,
    "passed": True,
    "skills": ["Python", "SQL"],
    "coordinates": (12.97, 77.59)
}

print(data["name"])
print(data["age"])
print(data["percentage"])
print(data["passed"])
print(data["skills"])
print(data["coordinates"])
```

Output:

```text
Asha
20
85.5
True
['Python', 'SQL']
(12.97, 77.59)
```

---

# ⚖️ 60. Choosing Between `[]` and `get()`

Use:

```python
dictionary[key]
```

when the key is expected to exist and you want an error if it does not.

Use:

```python
dictionary.get(key)
```

when the key may be missing and you want safe access.

Example:

```python
student = {
    "name": "Asha"
}

print(student["name"])
```

Use:

```python
print(student.get("city"))
```

when `"city"` may not exist.

---

# 🧠 61. Important: `get()` Does Not Modify the Dictionary

The `get()` method only retrieves a value.

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

value = student.get("age")

print(value)
print(student)
```

Output:

```text
20
{'name': 'Asha', 'age': 20}
```

The dictionary remains unchanged.

---

# ⚠️ 62. `get()` with `None`

If the key does not exist and no default value is provided:

```python
student = {
    "name": "Asha"
}

result = student.get("city")

print(result)
```

Output:

```text
None
```

`None` means that no value was returned for the requested key.

---

# 🔢 63. `get()` with Different Default Values

You can choose your own default value.

Example:

```python
student = {
    "name": "Asha"
}

print(student.get("age", 0))
print(student.get("course", "Unknown"))
print(student.get("passed", False))
```

Output:

```text
0
Unknown
False
```

---

# 🧠 64. Accessing Values with a Condition

Example:

```python
student = {
    "name": "Asha",
    "percentage": 85
}

percentage = student.get("percentage", 0)

if percentage >= 40:
    print("Passed")
else:
    print("Failed")
```

Output:

```text
Passed
```

---

# 💻 65. Practice Programs

## 🟢 Easy

### Program 1: Access Student Name

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
```

---

### Program 2: Access Student Age

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

print(student["age"])
```

---

### Program 3: Access Product Price

```python
product = {
    "name": "Laptop",
    "price": 50000,
    "brand": "Dell"
}

print(product["price"])
```

---

### Program 4: Access Multiple Values

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
print(student["age"])
print(student["course"])
```

---

# 🟡 Medium

### Program 5: Access Value Using `get()`

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

print(student.get("name"))
```

---

### Program 6: Handle Missing Key Using `get()`

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("course"))
```

---

### Program 7: Use a Default Value

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("course", "Not Available"))
```

---

### Program 8: Access a List Inside a Dictionary

```python
student = {
    "name": "Asha",
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"])
print(student["skills"][0])
```

---

# 🔴 Advanced

## Program 9: Access Student Record

```python
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

print(student["name"])
print(student["course"])
print(student["skills"][0])
print(student["percentage"])
print(student["passed"])
```

---

## Program 10: Access Nested Student Information

```python
student = {
    "name": "Asha",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "pincode": 560001
    }
}

print(student["address"]["city"])
print(student["address"]["state"])
print(student["address"]["pincode"])
```

---

# 🏆 66. Challenge

Create a dictionary representing a product.

It should contain:

```text
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

```python
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

print(product["name"])
print(product["price"])
print(product["brand"])
print(product["features"][0])
```

Try accessing different values from the dictionary without copying the example.

---

# 🧪 67. Mini Project: Student Profile

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
* Address

Example:

```python
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
    "passed": True,
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(student["name"])
print(student["course"])
print(student["skills"][0])
print(student["address"]["city"])
```

### Your Goal

Create your own student profile using different values.

Then access:

```text
1. Student name
2. Course
3. Percentage
4. First skill
5. City
6. Passed status
```

---

# 🎤 68. Interview Questions

* [ ] What does accessing a dictionary value mean?
* [ ] How do you access a dictionary value using a key?
* [ ] What is the syntax for accessing a dictionary value?
* [ ] Can dictionary values be accessed using numerical positions?
* [ ] What happens if you access a key that does not exist?
* [ ] What is a `KeyError`?
* [ ] What is the `get()` method?
* [ ] What happens when `get()` cannot find a key?
* [ ] What is the difference between `[]` and `get()`?
* [ ] How do you provide a default value using `get()`?
* [ ] Can dictionary values be lists?
* [ ] How do you access an item inside a list stored in a dictionary?
* [ ] Can dictionary values be tuples?
* [ ] Can dictionary values be sets?
* [ ] Can a dictionary contain another dictionary as a value?
* [ ] How do you access a nested dictionary value?
* [ ] Are dictionary keys case-sensitive?
* [ ] What happens if you use a value instead of a key?
* [ ] Can a variable be used to access a dictionary value?
* [ ] What does the `in` operator check when used with a dictionary?
* [ ] Does `get()` modify the dictionary?
* [ ] What does `None` mean when returned by `get()`?

---

# 📝 69. Assignment

Complete the following programs.

### Task 1

Create a dictionary containing:

```text
name
age
city
```

Access and print each value.

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

Access and print the `brand`, `price`, and `storage`.

---

### Task 3

Create a dictionary containing:

```text
name
age
course
```

Access the values using `get()`.

---

### Task 4

Create a dictionary and try accessing a key that does not exist using `[]`.

Observe the error.

---

### Task 5

Create a dictionary and try accessing a missing key using `get()`.

Observe the result.

---

### Task 6

Create a dictionary with a default value.

Example:

```python
student.get("city", "Not Available")
```

---

### Task 7

Create a dictionary containing a list of skills.

Access:

```text
The complete list
The first skill
The second skill
The third skill
```

---

### Task 8

Create a nested dictionary containing:

```text
name
address
    city
    state
    pincode
```

Access each nested value.

---

### Task 9

Create a product dictionary and use the `in` operator to check whether:

```text
price
brand
category
```

exist as keys.

---

### Task 10

Create a real-world student profile using a dictionary.

Access at least five different values.

---

# 🧠 70. Memory Tricks

Remember:

```text
Dictionary

       key
        ↓
"name" : "Asha"
          ↑
        value
```

To access the value:

```text
Dictionary
     ↓
   [key]
     ↓
   value
```

Think:

> **Key identifies the data, and the key is used to retrieve its value.**

---

Remember the syntax:

```text
dictionary[key]
```

Example:

```python
student["name"]
```

The key `"name"` gives:

```text
"Asha"
```

---

Remember `get()`:

```text
dictionary.get(key)
```

If the key exists:

```text
→ value
```

If the key does not exist:

```text
→ None
```

---

Remember the difference:

```text
[]      → KeyError if key is missing
get()   → None if key is missing
```

---

# 📌 71. Important Rules to Remember

```text
1. Dictionary values are accessed using keys.

2. Square brackets [] can be used to access dictionary values.

3. dictionary[key] returns the value associated with the key.

4. Accessing a missing key with [] produces a KeyError.

5. The get() method can be used for safer access.

6. get() returns None when the requested key does not exist and no default is provided.

7. get() can accept a default value.

8. Dictionary keys are case-sensitive.

9. A dictionary uses keys, not numerical positions, for normal value access.

10. Dictionary values can be strings, integers, floats, booleans, lists, tuples, sets, or dictionaries.

11. A list stored as a dictionary value can be accessed using another index.

12. A nested dictionary can be accessed using multiple keys.

13. The in operator checks whether a key exists in a dictionary.

14. get() does not modify the dictionary.

15. A variable can be used as a dictionary key when accessing a value.

16. Using a value instead of its key produces a KeyError when that value is not itself a key.
```

---

# 📊 72. Dictionary Value Access Structure

```text
                    DICTIONARY
                         │
                         ↓
                    KEY-VALUE PAIR
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
             KEY                  VALUE
              │                     │
              ↓                     ↓
           "name"                "Asha"
              │
              ↓
       student["name"]
              │
              ↓
           "Asha"
```

Using `get()`:

```text
          student.get("name")
                  │
                  ↓
               "Asha"
```

Missing key:

```text
student["city"]
      │
      ↓
  KeyError
```

Using `get()`:

```text
student.get("city")
      │
      ↓
    None
```

---

# 📚 73. Complete Dictionary Value Access Cheat Sheet

### Using Square Brackets

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student["name"])
```

---

### Using `get()`

```python
student = {
    "name": "Asha",
    "age": 20
}

print(student.get("name"))
```

---

### Using `get()` with Default Value

```python
print(student.get("city", "Not Available"))
```

---

### Accessing a List

```python
student = {
    "skills": ["Python", "SQL", "Git"]
}

print(student["skills"])
```

---

### Accessing an Item Inside a List

```python
print(student["skills"][0])
```

---

### Accessing a Tuple

```python
student = {
    "coordinates": (12.97, 77.59)
}

print(student["coordinates"])
```

---

### Accessing an Item Inside a Tuple

```python
print(student["coordinates"][0])
```

---

### Accessing a Nested Dictionary

```python
student = {
    "address": {
        "city": "Bengaluru"
    }
}

print(student["address"]["city"])
```

---

### Checking a Key

```python
if "name" in student:
    print(student["name"])
```

---

### Using a Variable as a Key

```python
key = "name"

print(student[key])
```

---

# 🏆 74. Dictionary Value Access Mastery

```text
                  ACCESS DICTIONARY VALUE
                           │
              ┌────────────┴────────────┐
              ↓                         ↓
             []                       get()
              │                         │
              ↓                         ↓
       dictionary[key]        dictionary.get(key)
              │                         │
       ┌──────┴──────┐          ┌───────┴───────┐
       ↓             ↓          ↓               ↓
    Exists        Missing    Exists          Missing
       │             │          │               │
       ↓             ↓          ↓               ↓
    Value         KeyError    Value           None
```

With a default value:

```text
dictionary.get(key, default)
              │
              ↓
      ┌───────┴────────┐
      ↓                ↓
   Key exists       Key missing
      ↓                ↓
    Value            Default
```

Nested access:

```text
Dictionary
     ↓
   [key]
     ↓
Inner Dictionary
     ↓
   [key]
     ↓
   Value
```

---

# 📚 75. Summary

In this lesson, you learned:

* How to access dictionary values.
* How to access values using keys.
* How to use square brackets `[]`.
* How dictionary access differs from list indexing.
* What happens when a key does not exist.
* What a `KeyError` is.
* How to use the `get()` method.
* How `get()` behaves with missing keys.
* How to use default values with `get()`.
* The difference between `[]` and `get()`.
* How to access string values.
* How to access integer values.
* How to access float values.
* How to access boolean values.
* How to access lists stored as dictionary values.
* How to access individual list items inside dictionaries.
* How to access tuples stored as dictionary values.
* How to access sets stored as dictionary values.
* How to access dictionaries stored as values.
* How to access nested dictionary values.
* How to access deeply nested values.
* How to use variables as dictionary keys.
* How to check for keys using the `in` operator.
* How to access values inside loops.
* Common mistakes when accessing dictionary values.
* How to access dictionary values in real-world programs.

---

# 🎯 Topic Completion Checklist

* [x] I understand what accessing a dictionary value means.
* [x] I can access values using dictionary keys.
* [x] I understand `dictionary[key]`.
* [x] I understand dictionary keys are not numerical positions.
* [x] I understand what happens when a key is missing.
* [x] I understand `KeyError`.
* [x] I can use the `get()` method.
* [x] I understand the difference between `[]` and `get()`.
* [x] I can use default values with `get()`.
* [x] I can access string values.
* [x] I can access integer values.
* [x] I can access float values.
* [x] I can access boolean values.
* [x] I can access lists stored inside dictionaries.
* [x] I can access individual list items inside dictionaries.
* [x] I can access tuples stored inside dictionaries.
* [x] I can access sets stored inside dictionaries.
* [x] I can access nested dictionaries.
* [x] I can access values from nested dictionaries.
* [x] I understand case-sensitive dictionary keys.
* [x] I can use variables as dictionary keys.
* [x] I can check whether a key exists using `in`.
* [x] I understand that `get()` does not modify the dictionary.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the mini project.
* [x] I completed the assignment.
* [x] I can access dictionary values without looking at my notes.
---

# 🚀 Next Topic

➡️ **Next Topic: Adding and Updating Dictionary Items**

In the next topic, you will learn:

* How to add new key-value pairs.
* How to update existing dictionary values.
* How to add items using square brackets `[]`.
* How to update values using keys.
* How to use `update()`.
* Difference between adding and updating.
* Adding multiple items.
* Updating multiple items.
* Adding and updating nested dictionary values.
* Practical examples and challenges.

---

## ⭐ Quote of the Day

> **"A dictionary stores information using keys, and accessing the right key helps you retrieve exactly the value you need."** 🐍📚
