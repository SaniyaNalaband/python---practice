# 🐍 Python Master Course

# 📦 Phase 6: Collections – Dictionaries

## 📌 Topic 5: Nested Dictionary

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what a nested dictionary is.
* [ ] Understand how dictionaries can be stored inside dictionaries.
* [ ] Create simple nested dictionaries.
* [ ] Access values from nested dictionaries.
* [ ] Access deeply nested values.
* [ ] Modify values inside nested dictionaries.
* [ ] Add new data to nested dictionaries.
* [ ] Remove data from nested dictionaries.
* [ ] Use loops with nested dictionaries.
* [ ] Use `keys()`, `values()`, and `items()` with nested dictionaries.
* [ ] Combine nested dictionaries with conditions.
* [ ] Work with multiple records using nested dictionaries.
* [ ] Understand different nested dictionary structures.
* [ ] Use nested dictionaries in real-world applications.
* [ ] Avoid common mistakes when working with nested dictionaries.
* [ ] Build practical programs using nested dictionaries.

---

# 📖 1. What is a Nested Dictionary?

A **nested dictionary** is a dictionary that contains another dictionary as one or more of its values.

In simple words:

> A dictionary inside another dictionary is called a nested dictionary.

Example:

```python
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

Output:

```text
{'student1': {'name': 'Asha', 'age': 20}, 'student2': {'name': 'Neha', 'age': 21}}
```

Here:

```text
students
   ↓
Outer Dictionary
   │
   ├── student1 → Inner Dictionary
   │                  ├── name
   │                  └── age
   │
   └── student2 → Inner Dictionary
                      ├── name
                      └── age
```

---

# 🧠 2. Understanding the Structure

A normal dictionary contains key-value pairs:

```python
student = {
    "name": "Asha",
    "age": 20
}
```

A nested dictionary contains another dictionary as a value:

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}
```

The structure is:

```text
Outer Dictionary
       ↓
    "student1"
       ↓
Inner Dictionary
       ↓
"name" → "Asha"
"age"  → 20
```

---

# 📚 3. Creating a Nested Dictionary

You can create a nested dictionary by placing dictionaries inside another dictionary.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "course": "BCA"
    },
    "student2": {
        "name": "Neha",
        "course": "BCA"
    }
}

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'course': 'BCA'}, 'student2': {'name': 'Neha', 'course': 'BCA'}}
```

---

# 🔑 4. Accessing an Inner Dictionary

You can access an inner dictionary using its outer key.

Example:

```python
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

print(students["student1"])
```

Output:

```text
{'name': 'Asha', 'age': 20}
```

Here:

```text
students["student1"]
        ↓
Inner dictionary
```

---

# 🎯 5. Accessing a Value Inside a Nested Dictionary

To access a specific value inside the inner dictionary, use two keys.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

print(students["student1"]["name"])
```

Output:

```text
Asha
```

The process is:

```text
students
   ↓
"student1"
   ↓
Inner dictionary
   ↓
"name"
   ↓
"Asha"
```

---

# 🧠 6. Accessing Multiple Nested Values

You can access different values from the same inner dictionary.

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }
}

print(student["student1"]["name"])
print(student["student1"]["age"])
print(student["student1"]["course"])
```

Output:

```text
Asha
20
BCA
```

---

# 🔍 7. Accessing Deeply Nested Dictionaries

A dictionary can contain another dictionary, which can contain another dictionary.

Example:

```python
company = {
    "employee": {
        "profile": {
            "name": "Neha",
            "age": 24
        }
    }
}

print(company["employee"]["profile"]["name"])
```

Output:

```text
Neha
```

The structure is:

```text
company
   ↓
employee
   ↓
profile
   ↓
name
   ↓
Neha
```

---

# 🪆 8. Multiple Levels of Nesting

Nested dictionaries can have several levels.

Example:

```python
data = {
    "college": {
        "department": {
            "student": {
                "name": "Asha",
                "course": "BCA"
            }
        }
    }
}

print(data["college"]["department"]["student"]["name"])
```

Output:

```text
Asha
```

Each additional dictionary requires another key.

---

# ✏️ 9. Modifying a Value in a Nested Dictionary

You can modify an inner value using multiple keys.

Example:

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

student["student1"]["age"] = 21

print(student)
```

Output:

```text
{'student1': {'name': 'Asha', 'age': 21}}
```

Only the inner `"age"` value was changed.

---

# ➕ 10. Adding a New Value to an Inner Dictionary

You can add a new key-value pair to an inner dictionary.

Example:

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

student["student1"]["course"] = "BCA"

print(student)
```

Output:

```text
{'student1': {'name': 'Asha', 'age': 20, 'course': 'BCA'}}
```

---

# 🔄 11. Adding a New Inner Dictionary

You can add an entirely new record to the outer dictionary.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

students["student2"] = {
    "name": "Neha",
    "age": 21
}

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'age': 20}, 'student2': {'name': 'Neha', 'age': 21}}
```

---

# 🗑️ 12. Removing a Value from an Inner Dictionary

You can use `del` to remove a specific value from an inner dictionary.

Example:

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }
}

del student["student1"]["age"]

print(student)
```

Output:

```text
{'student1': {'name': 'Asha', 'course': 'BCA'}}
```

---

# 🗑️ 13. Removing an Entire Inner Dictionary

You can remove an entire record from the outer dictionary.

Example:

```python
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

del students["student2"]

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'age': 20}}
```

---

# 🔁 14. Using `pop()` with Nested Dictionaries

`pop()` can remove an entire inner dictionary.

Example:

```python
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

removed = students.pop("student2")

print(removed)
print(students)
```

Output:

```text
{'name': 'Neha', 'age': 21}
{'student1': {'name': 'Asha', 'age': 20}}
```

---

# 🔍 15. Using `get()` with Nested Dictionaries

`get()` can be used to safely access an inner dictionary.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

print(students.get("student1"))
```

Output:

```text
{'name': 'Asha', 'age': 20}
```

You can then access the inner value:

```python
print(students.get("student1").get("name"))
```

Output:

```text
Asha
```

---

# 🛡️ 16. Safely Accessing Missing Nested Data

Nested dictionaries can produce errors if a key does not exist.

Example:

```python
student = {
    "student1": {
        "name": "Asha"
    }
}

print(student["student1"]["city"])
```

This produces:

```text
KeyError: 'city'
```

Using `get()` is safer:

```python
print(student.get("student1", {}).get("city", "Not Available"))
```

Output:

```text
Not Available
```

The `{}` provides an empty dictionary if `"student1"` is missing.

---

# 🔑 17. Using `keys()` with Nested Dictionaries

You can use `keys()` to access the keys of the outer dictionary.

Example:

```python
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

print(students.keys())
```

Output:

```text
dict_keys(['student1', 'student2'])
```

---

# 🔍 18. Getting Keys from an Inner Dictionary

You can also use `keys()` on an inner dictionary.

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }
}

print(students["student1"].keys())
```

Output:

```text
dict_keys(['name', 'age', 'course'])
```

---

# 💰 19. Using `values()` with Nested Dictionaries

`values()` returns the values of the dictionary.

Example:

```python
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

print(students.values())
```

Output:

```text
dict_values([{'name': 'Asha', 'age': 20}, {'name': 'Neha', 'age': 21}])
```

The values are themselves dictionaries.

---

# 🔗 20. Using `items()` with Nested Dictionaries

`items()` returns the outer key and its corresponding inner dictionary.

Example:

```python
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

print(students.items())
```

Output:

```text
dict_items([
    ('student1', {'name': 'Asha', 'age': 20}),
    ('student2', {'name': 'Neha', 'age': 21})
])
```

---

# 🔁 21. Looping Through a Nested Dictionary

You can use `items()` to loop through the outer dictionary.

Example:

```python
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

for student_id, details in students.items():
    print(student_id, ":", details)
```

Output:

```text
student1 : {'name': 'Asha', 'age': 20}
student2 : {'name': 'Neha', 'age': 21}
```

---

# 🔄 22. Looping Through Inner Dictionary Values

You can use another loop to access the inner dictionary.

Example:

```python
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

for student_id, details in students.items():
    print("Student:", student_id)

    for key, value in details.items():
        print(key, ":", value)
```

Output:

```text
Student: student1
name : Asha
age : 20
Student: student2
name : Neha
age : 21
```

This is called a **nested loop**.

---

# 🧠 23. Understanding Nested Loops

When working with nested dictionaries, you may need one loop for the outer dictionary and another loop for the inner dictionary.

Structure:

```text
Outer Dictionary
       ↓
    for loop
       ↓
Inner Dictionary
       ↓
    for loop
       ↓
Key + Value
```

Example:

```python
for outer_key, inner_dict in data.items():
    for inner_key, value in inner_dict.items():
        print(inner_key, value)
```

---

# ⚖️ 24. Nested Dictionary with Conditions

You can use `if` statements with nested dictionaries.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "marks": 90
    },
    "student2": {
        "name": "Neha",
        "marks": 72
    }
}

for student_id, details in students.items():
    if details["marks"] >= 80:
        print(details["name"], ":", details["marks"])
```

Output:

```text
Asha : 90
```

---

# 🔢 25. Finding Students with High Marks

You can filter nested dictionary records using conditions.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "marks": 90
    },
    "student2": {
        "name": "Neha",
        "marks": 72
    },
    "student3": {
        "name": "Kiran",
        "marks": 85
    }
}

for student_id, details in students.items():
    if details["marks"] >= 80:
        print(details["name"])
```

Output:

```text
Asha
Kiran
```

---

# 📊 26. Nested Dictionary for Multiple Subjects

A nested dictionary can store marks for multiple students.

Example:

```python
students = {
    "student1": {
        "Python": 90,
        "SQL": 85,
        "Git": 80
    },
    "student2": {
        "Python": 78,
        "SQL": 88,
        "Git": 82
    }
}

print(students["student1"]["Python"])
```

Output:

```text
90
```

---

# 🔢 27. Calculating Total Marks

You can calculate the total marks of a student using `values()`.

Example:

```python
students = {
    "student1": {
        "Python": 90,
        "SQL": 85,
        "Git": 80
    }
}

total = 0

for mark in students["student1"].values():
    total += mark

print("Total:", total)
```

Output:

```text
Total: 255
```

---

# 📈 28. Calculating Average Marks

You can calculate an average from a nested dictionary.

Example:

```python
student = {
    "Python": 90,
    "SQL": 85,
    "Git": 80
}

total = sum(student.values())
average = total / len(student)

print("Average:", average)
```

Output:

```text
Average: 85.0
```

---

# 🏆 29. Finding the Highest Mark

You can use `max()` with a nested dictionary.

Example:

```python
marks = {
    "Python": 90,
    "SQL": 85,
    "Git": 80
}

highest = max(marks.values())

print("Highest:", highest)
```

Output:

```text
Highest: 90
```

---

# 🧩 30. Nested Dictionary with `update()`

You can update values inside an inner dictionary.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

students["student1"].update({
    "course": "BCA",
    "semester": 4
})

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'age': 20, 'course': 'BCA', 'semester': 4}}
```

---

# 🛠️ 31. Updating Multiple Student Records

You can update a particular student's information.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "marks": 90
    },
    "student2": {
        "name": "Neha",
        "marks": 75
    }
}

students["student2"].update({
    "marks": 82
})

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'marks': 90}, 'student2': {'name': 'Neha', 'marks': 82}}
```

---

# 🗑️ 32. Removing an Inner Item Using `pop()`

You can remove a specific key from an inner dictionary.

Example:

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }
}

removed = student["student1"].pop("age")

print("Removed:", removed)
print(student)
```

Output:

```text
Removed: 20
{'student1': {'name': 'Asha', 'course': 'BCA'}}
```

---

# 🧹 33. Clearing an Inner Dictionary

You can use `clear()` on an inner dictionary.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

students["student1"].clear()

print(students)
```

Output:

```text
{'student1': {}}
```

The outer dictionary still exists, but the inner dictionary is empty.

---

# 📋 34. Copying a Nested Dictionary

The `copy()` method creates a **shallow copy**.

Example:

```python
student = {
    "name": "Asha",
    "details": {
        "age": 20
    }
}

new_student = student.copy()

print(new_student)
```

Output:

```text
{'name': 'Asha', 'details': {'age': 20}}
```

---

# ⚠️ 35. Shallow Copy and Nested Dictionaries

With a shallow copy, the outer dictionary is copied, but nested objects are still shared.

Example:

```python
student = {
    "name": "Asha",
    "details": {
        "age": 20
    }
}

new_student = student.copy()

new_student["details"]["age"] = 21

print(student)
print(new_student)
```

Output:

```text
{'name': 'Asha', 'details': {'age': 21}}
{'name': 'Asha', 'details': {'age': 21}}
```

Why?

Because both dictionaries refer to the same inner dictionary.

```text
student ───────┐
               ↓
          inner dictionary
               ↑
new_student ───┘
```

---

# 🧠 36. Deep Copy for Nested Dictionaries

If you need completely independent nested dictionaries, you can use `deepcopy()` from the `copy` module.

Example:

```python
import copy

student = {
    "name": "Asha",
    "details": {
        "age": 20
    }
}

new_student = copy.deepcopy(student)

new_student["details"]["age"] = 21

print(student)
print(new_student)
```

Output:

```text
{'name': 'Asha', 'details': {'age': 20}}
{'name': 'Asha', 'details': {'age': 21}}
```

Here, both the outer and inner dictionaries are independent.

---

# ⚖️ 37. Shallow Copy vs Deep Copy

| Method         | Outer Dictionary | Inner Dictionary |
| -------------- | ---------------- | ---------------- |
| Assignment `=` | Shared           | Shared           |
| `copy()`       | New              | Shared           |
| `deepcopy()`   | New              | New              |

Remember:

```text
= 
↓
Same object

copy()
↓
New outer object
Shared nested objects

deepcopy()
↓
Completely independent copy
```

---

# 🏗️ 38. Different Types of Nested Dictionaries

Nested dictionaries can be organized in different ways.

### Student-Based Structure

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}
```

### Product-Based Structure

```python
products = {
    "laptop": {
        "price": 55000,
        "stock": 5
    }
}
```

### Employee-Based Structure

```python
employees = {
    "emp101": {
        "name": "Neha",
        "salary": 45000
    }
}
```

The structure depends on the application.

---

# 🌍 39. Real-World Example: Student Management

A college application can store multiple students using nested dictionaries.

```python
students = {
    "student101": {
        "name": "Asha",
        "course": "BCA",
        "marks": 90
    },
    "student102": {
        "name": "Neha",
        "course": "BCA",
        "marks": 85
    }
}

for student_id, details in students.items():
    print(student_id)
    print("Name:", details["name"])
    print("Course:", details["course"])
    print("Marks:", details["marks"])
```

Output:

```text
student101
Name: Asha
Course: BCA
Marks: 90
student102
Name: Neha
Course: BCA
Marks: 85
```

---

# 🌍 40. Real-World Example: Employee Management

```python
employees = {
    "emp101": {
        "name": "Neha",
        "department": "Development",
        "salary": 45000
    },
    "emp102": {
        "name": "Kiran",
        "department": "Testing",
        "salary": 40000
    }
}

print(employees["emp101"]["name"])
print(employees["emp101"]["salary"])
```

Output:

```text
Neha
45000
```

---

# 🌍 41. Real-World Example: Product Inventory

```python
inventory = {
    "Laptop": {
        "price": 55000,
        "stock": 5
    },
    "Mouse": {
        "price": 800,
        "stock": 20
    },
    "Keyboard": {
        "price": 1500,
        "stock": 10
    }
}

print(inventory["Laptop"]["price"])
```

Output:

```text
55000
```

---

# 🌍 42. Real-World Example: Shopping Cart

```python
cart = {
    "Laptop": {
        "price": 55000,
        "quantity": 1
    },
    "Mouse": {
        "price": 800,
        "quantity": 2
    }
}

total = 0

for product, details in cart.items():
    total += details["price"] * details["quantity"]

print("Cart Total:", total)
```

Output:

```text
Cart Total: 56600
```

---

# 🌍 43. Real-World Example: User Profile

```python
user = {
    "profile": {
        "username": "asha20",
        "email": "asha@example.com"
    },
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(user["profile"]["username"])
print(user["address"]["city"])
```

Output:

```text
asha20
Bengaluru
```

---

# 🌍 44. Real-World Example: Company Departments

```python
company = {
    "Development": {
        "employees": 15,
        "manager": "Neha"
    },
    "Testing": {
        "employees": 8,
        "manager": "Kiran"
    }
}

for department, details in company.items():
    print(department, ":", details["employees"])
```

Output:

```text
Development : 15
Testing : 8
```

---

# 🔎 45. Searching Nested Dictionary Data

You can search for a specific value using loops and conditions.

Example:

```python
employees = {
    "emp101": {
        "name": "Neha",
        "department": "Development"
    },
    "emp102": {
        "name": "Kiran",
        "department": "Testing"
    }
}

for employee_id, details in employees.items():
    if details["department"] == "Development":
        print(details["name"])
```

Output:

```text
Neha
```

---

# 📊 46. Filtering Nested Dictionary Records

You can display only records that satisfy a condition.

Example:

```python
employees = {
    "emp101": {
        "name": "Neha",
        "salary": 45000
    },
    "emp102": {
        "name": "Kiran",
        "salary": 35000
    },
    "emp103": {
        "name": "Asha",
        "salary": 50000
    }
}

for employee_id, details in employees.items():
    if details["salary"] >= 40000:
        print(details["name"], ":", details["salary"])
```

Output:

```text
Neha : 45000
Asha : 50000
```

---

# 🔢 47. Counting Records in a Nested Dictionary

You can use `len()` to count the number of outer records.

Example:

```python
students = {
    "student1": {
        "name": "Asha"
    },
    "student2": {
        "name": "Neha"
    },
    "student3": {
        "name": "Kiran"
    }
}

print("Total Students:", len(students))
```

Output:

```text
Total Students: 3
```

---

# 🧠 48. Nested Dictionary with `setdefault()`

`setdefault()` can be useful for creating nested structures dynamically.

Example:

```python
students = {}

students.setdefault("student1", {})
students["student1"]["name"] = "Asha"
students["student1"]["age"] = 20

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'age': 20}}
```

This is useful when building dictionaries step by step.

---

# 🔄 49. Creating Nested Dictionaries Dynamically

You can create nested records using variables.

Example:

```python
students = {}

student_id = "student1"

students[student_id] = {
    "name": "Asha",
    "course": "BCA",
    "marks": 90
}

print(students)
```

Output:

```text
{'student1': {'name': 'Asha', 'course': 'BCA', 'marks': 90}}
```

---

# ⚠️ 50. Common Mistake: Using the Wrong Key

Consider:

```python
student = {
    "student1": {
        "name": "Asha"
    }
}

print(student["student2"]["name"])
```

This produces:

```text
KeyError: 'student2'
```

The outer key `"student2"` does not exist.

---

# ⚠️ 51. Common Mistake: Accessing a Missing Inner Key

Example:

```python
student = {
    "student1": {
        "name": "Asha"
    }
}

print(student["student1"]["age"])
```

This produces:

```text
KeyError: 'age'
```

The outer key exists, but the inner key does not.

---

# ⚠️ 52. Common Mistake: Confusing Outer and Inner Keys

Consider:

```python
students = {
    "student1": {
        "name": "Asha"
    }
}
```

This is correct:

```python
students["student1"]["name"]
```

But this is incorrect:

```python
students["name"]
```

Why?

Because `"name"` belongs to the inner dictionary.

The correct path is:

```text
students
   ↓
student1
   ↓
name
```

---

# ⚠️ 53. Common Mistake: Forgetting Multiple Keys

For nested data:

```python
student = {
    "student1": {
        "name": "Asha"
    }
}
```

This:

```python
print(student["student1"])
```

returns the entire inner dictionary.

This:

```python
print(student["student1"]["name"])
```

returns the actual value.

Output:

```text
{'name': 'Asha'}
Asha
```

---

# 📊 54. Nested Dictionary Operations Comparison

| Operation              | Purpose                        | Example                        |
| ---------------------- | ------------------------------ | ------------------------------ |
| `data[key]`            | Access inner dictionary        | `data["student1"]`             |
| `data[key][inner_key]` | Access nested value            | `data["student1"]["name"]`     |
| `get()`                | Safely access data             | `data.get("student1")`         |
| `keys()`               | Get keys                       | `data.keys()`                  |
| `values()`             | Get values                     | `data.values()`                |
| `items()`              | Get key-value pairs            | `data.items()`                 |
| `update()`             | Add/modify data                | `data["student1"].update(...)` |
| `pop()`                | Remove data                    | `data.pop("student1")`         |
| `clear()`              | Remove all data                | `data.clear()`                 |
| `copy()`               | Create shallow copy            | `data.copy()`                  |
| `deepcopy()`           | Create independent nested copy | `copy.deepcopy(data)`          |

---

# 💻 55. Practice Programs

## 🟢 Easy

### Program 1: Create a Nested Dictionary

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

print(student)
```

---

### Program 2: Access an Inner Dictionary

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

print(student["student1"])
```

---

### Program 3: Access a Nested Value

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

print(student["student1"]["name"])
```

---

### Program 4: Display All Student Records

```python
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

for student_id, details in students.items():
    print(student_id, details)
```

---

# 🟡 Medium

### Program 5: Modify a Nested Value

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

student["student1"]["age"] = 21

print(student)
```

---

### Program 6: Add a New Nested Value

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}

student["student1"]["course"] = "BCA"

print(student)
```

---

### Program 7: Remove a Nested Value

```python
student = {
    "student1": {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }
}

student["student1"].pop("age")

print(student)
```

---

### Program 8: Calculate Total Marks

```python
student = {
    "Python": 90,
    "SQL": 85,
    "Git": 80
}

total = sum(student.values())

print("Total:", total)
```

---

# 🔴 Advanced

## Program 9: Filter Students by Marks

```python
students = {
    "student1": {
        "name": "Asha",
        "marks": 90
    },
    "student2": {
        "name": "Neha",
        "marks": 72
    },
    "student3": {
        "name": "Kiran",
        "marks": 85
    }
}

for student_id, details in students.items():
    if details["marks"] >= 80:
        print(details["name"], ":", details["marks"])
```

Output:

```text
Asha : 90
Kiran : 85
```

---

## Program 10: Student Information Management

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }
}

students["student1"].update({
    "semester": 4
})

students["student1"].setdefault("city", "Bengaluru")

for key, value in students["student1"].items():
    print(key, ":", value)
```

---

## Program 11: Employee Salary Filter

```python
employees = {
    "emp101": {
        "name": "Neha",
        "salary": 45000
    },
    "emp102": {
        "name": "Kiran",
        "salary": 35000
    },
    "emp103": {
        "name": "Asha",
        "salary": 50000
    }
}

for employee_id, details in employees.items():
    if details["salary"] >= 40000:
        print(details["name"], ":", details["salary"])
```

---

## Program 12: Shopping Cart Total

```python
cart = {
    "Laptop": {
        "price": 55000,
        "quantity": 1
    },
    "Mouse": {
        "price": 800,
        "quantity": 2
    },
    "Keyboard": {
        "price": 1500,
        "quantity": 1
    }
}

total = 0

for product, details in cart.items():
    total += details["price"] * details["quantity"]

print("Total:", total)
```

Output:

```text
Total: 58100
```

---

# 🏆 56. Challenge

Create a nested student marks dictionary:

```text
Student 1
    Python
    SQL
    Git
    HTML
    CSS

Student 2
    Python
    SQL
    Git
    HTML
    CSS
```

Store marks for each subject.

Then:

1. Display all student IDs using `keys()`.
2. Display the complete record of each student.
3. Display the name and marks of each student.
4. Display all subjects using `keys()`.
5. Display all marks using `values()`.
6. Display subjects and marks using `items()`.
7. Update one student's marks.
8. Add a new subject using `update()`.
9. Remove one subject using `pop()`.
10. Calculate the total marks of each student.
11. Calculate the average marks of each student.
12. Find students whose average is greater than `80`.
13. Display the final nested dictionary.

Example:

```python
students = {
    "student1": {
        "name": "Asha",
        "Python": 90,
        "SQL": 85,
        "Git": 80,
        "HTML": 88,
        "CSS": 82
    },
    "student2": {
        "name": "Neha",
        "Python": 78,
        "SQL": 88,
        "Git": 82,
        "HTML": 75,
        "CSS": 80
    }
}
```

Try solving the challenge without copying the solution.

---

# 🧪 57. Mini Project: Student Management System

Create a student management system using a nested dictionary.

Each student should contain:

* Student ID
* Name
* Course
* Semester
* Marks
* City

Example:

```python
students = {
    "student101": {
        "name": "Asha",
        "course": "BCA",
        "semester": 4,
        "marks": 88,
        "city": "Bengaluru"
    },
    "student102": {
        "name": "Neha",
        "course": "BCA",
        "semester": 4,
        "marks": 82,
        "city": "Mysuru"
    }
}
```

Perform the following operations:

* Display all student IDs.
* Display the name of a particular student.
* Display the course of a particular student.
* Update a student's marks.
* Add a new student.
* Add a new field using `update()`.
* Add a default `"status"` using `setdefault()`.
* Remove a field using `pop()`.
* Display students whose marks are greater than `80`.
* Calculate the average marks.
* Display the final student records.

### Your Goal

Build the complete student management program using nested dictionaries.

---

# 🎤 58. Interview Questions

* [ ] What is a nested dictionary in Python?
* [ ] How do you create a nested dictionary?
* [ ] How do you access an inner dictionary?
* [ ] How do you access a value inside a nested dictionary?
* [ ] How do you access deeply nested values?
* [ ] How do you modify a value inside a nested dictionary?
* [ ] How do you add a new key to an inner dictionary?
* [ ] How do you add a new inner dictionary?
* [ ] How do you remove an inner dictionary?
* [ ] How do you remove an item from an inner dictionary?
* [ ] How can `get()` be used with nested dictionaries?
* [ ] How do `keys()`, `values()`, and `items()` work with nested dictionaries?
* [ ] Why are nested loops useful with nested dictionaries?
* [ ] How can conditions be used with nested dictionaries?
* [ ] What is the difference between shallow copy and deep copy?
* [ ] Why can `copy()` cause unexpected behavior with nested dictionaries?
* [ ] What does `deepcopy()` do?
* [ ] How can nested dictionaries be used to store student records?
* [ ] How can nested dictionaries be used for employee management?
* [ ] How can you calculate values stored inside nested dictionaries?

---

# 📝 59. Assignment

Complete the following programs.

### Task 1

Create a nested dictionary containing:

```text
name
age
course
city
```

Access the name and city.

---

### Task 2

Create a nested dictionary containing three students and their marks.

Use `keys()` to display all student IDs.

---

### Task 3

Create a nested dictionary containing five subjects and marks for one student.

Use `values()` to calculate the total marks.

---

### Task 4

Use `items()` to display every subject and its marks.

---

### Task 5

Create a student nested dictionary and use `update()` to add:

```text
semester
college
```

---

### Task 6

Create a nested product dictionary and remove the price of one product using `pop()`.

---

### Task 7

Create a nested employee dictionary and update the salary of one employee.

---

### Task 8

Create a nested dictionary and make a shallow copy using `copy()`.

Change a value inside the nested dictionary and observe the original.

---

### Task 9

Use `setdefault()` to add a default `"status"` value to a nested student record.

---

### Task 10

Create a nested dictionary for five programming skills.

Store the skill level of each programming language.

Example:

```text
Python → Beginner
SQL → Intermediate
Git → Beginner
HTML → Advanced
JavaScript → Intermediate
```

---

### Task 11

Create a real-world nested dictionary and use at least seven different dictionary operations.

---

### Task 12

Create a program that uses `items()` and `if` to display only nested dictionary records whose values are greater than a specified number.

---

# 🧠 60. Memory Tricks

Remember nested dictionary access:

```text
Outer Dictionary
       ↓
Outer Key
       ↓
Inner Dictionary
       ↓
Inner Key
       ↓
Value
```

Example:

```python
students["student1"]["name"]
```

Remember:

```text
["outer_key"]
      ↓
Find inner dictionary

["inner_key"]
      ↓
Find actual value
```

---

Remember the basic operations:

```text
Access
  ↓
data["student1"]["name"]

Modify
  ↓
data["student1"]["age"] = 21

Add
  ↓
data["student1"]["course"] = "BCA"

Remove
  ↓
data["student1"].pop("age")
```

---

Remember looping:

```text
Outer Loop
    ↓
student_id + details
    ↓
Inner Loop
    ↓
key + value
```

Example:

```python
for student_id, details in students.items():
    for key, value in details.items():
        print(key, value)
```

---

Remember copying:

```text
= 
↓
Same object

copy()
↓
New outer dictionary
Shared nested objects

deepcopy()
↓
Completely independent
```

---

# 📌 61. Important Rules to Remember

```text
1. A nested dictionary is a dictionary inside another dictionary.

2. The outer dictionary contains keys whose values can be dictionaries.

3. Use multiple keys to access nested values.

4. data["outer"]["inner"] accesses a value inside a nested dictionary.

5. Nested dictionaries can contain multiple levels.

6. Values inside nested dictionaries can be modified.

7. New keys can be added to inner dictionaries.

8. Entire inner dictionaries can be added or removed.

9. get() can be used for safer nested access.

10. keys(), values(), and items() can be used with nested dictionaries.

11. Nested dictionaries are commonly processed using nested loops.

12. Conditions can be combined with nested dictionary loops.

13. copy() creates a shallow copy.

14. Shallow copies still share nested mutable objects.

15. deepcopy() creates independent nested objects.

16. Nested dictionaries are useful for structured real-world data.

17. Student, employee, product, inventory, and user records can be represented using nested dictionaries.

18. Always understand whether a key belongs to the outer or inner dictionary.
```

---

# 📊 62. Nested Dictionary Structure

```text
                         NESTED DICTIONARY
                                │
                                ↓
                       OUTER DICTIONARY
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
          student1          student2          student3
              │                 │                 │
              ↓                 ↓                 ↓
       INNER DICTIONARY  INNER DICTIONARY  INNER DICTIONARY
              │                 │                 │
        ┌─────┼─────┐     ┌─────┼─────┐     ┌─────┼─────┐
        ↓     ↓     ↓     ↓     ↓     ↓     ↓     ↓     ↓
      name   age course  name   age course  name   age course
        │     │     │      │     │     │      │     │     │
        ↓     ↓     ↓      ↓     ↓     ↓      ↓     ↓     ↓
      Asha   20    BCA    Neha   21    BCA   Kiran  20    BCA
```

---

# 📚 63. Complete Nested Dictionary Cheat Sheet

### Create a Nested Dictionary

```python
students = {
    "student1": {
        "name": "Asha",
        "age": 20
    }
}
```

### Access Inner Dictionary

```python
students["student1"]
```

### Access Nested Value

```python
students["student1"]["name"]
```

### Modify Nested Value

```python
students["student1"]["age"] = 21
```

### Add Nested Value

```python
students["student1"]["course"] = "BCA"
```

### Add New Inner Dictionary

```python
students["student2"] = {
    "name": "Neha",
    "age": 21
}
```

### Get Inner Dictionary

```python
students.get("student1")
```

### Get Nested Value Safely

```python
students.get("student1", {}).get("name", "Not Available")
```

### Get Outer Keys

```python
students.keys()
```

### Get Inner Keys

```python
students["student1"].keys()
```

### Get Inner Values

```python
students["student1"].values()
```

### Get Inner Key-Value Pairs

```python
students["student1"].items()
```

### Update Nested Dictionary

```python
students["student1"].update({
    "semester": 4
})
```

### Remove Nested Item

```python
students["student1"].pop("age")
```

### Remove Entire Inner Dictionary

```python
students.pop("student1")
```

### Clear Inner Dictionary

```python
students["student1"].clear()
```

### Create Shallow Copy

```python
new_students = students.copy()
```

### Create Deep Copy

```python
import copy

new_students = copy.deepcopy(students)
```

### Loop Through Nested Dictionary

```python
for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(key, value)
```

---

# 🏆 64. Nested Dictionary Mastery

```text
                         NESTED DICTIONARY
                                │
                                ↓
                      Dictionary Inside
                         Dictionary
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
            ACCESS            MODIFY            REMOVE
              │                 │                 │
        ┌─────┼─────┐      ┌────┴────┐      ┌────┼────┐
        ↓     ↓     ↓      ↓         ↓      ↓    ↓    ↓
       get  keys values  update   setdefault pop  del clear
        │
        ↓
      items()
        │
        ↓
    Key + Value
        │
        ↓
   Nested Loops
        │
        ↓
 Conditions + Data Processing
        │
        ↓
 Real-World Applications
```

---

# 📚 65. Summary

In this lesson, you learned:

* What a nested dictionary is.
* How to create nested dictionaries.
* How dictionaries can contain other dictionaries.
* How to access inner dictionaries.
* How to access values inside nested dictionaries.
* How to access deeply nested values.
* How to modify nested values.
* How to add new nested data.
* How to add new inner dictionaries.
* How to remove nested data.
* How to use `get()` with nested dictionaries.
* How to use `keys()` with nested dictionaries.
* How to use `values()` with nested dictionaries.
* How to use `items()` with nested dictionaries.
* How to loop through nested dictionaries.
* How to use nested loops.
* How to use conditions with nested dictionaries.
* How to calculate totals and averages from nested data.
* How to filter nested dictionary records.
* How to use `update()`.
* How to use `pop()`.
* How to use `clear()`.
* How to use `setdefault()`.
* How shallow copying works with nested dictionaries.
* How deep copying works with nested dictionaries.
* The difference between `copy()` and `deepcopy()`.
* How nested dictionaries are used in real-world applications.
* Common mistakes when working with nested dictionaries.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what a nested dictionary is.
* [ ] I can create a nested dictionary.
* [ ] I can access an inner dictionary.
* [ ] I can access values inside an inner dictionary.
* [ ] I understand multiple levels of nesting.
* [ ] I can modify nested values.
* [ ] I can add nested values.
* [ ] I can add a new inner dictionary.
* [ ] I can remove nested values.
* [ ] I can use `get()` with nested dictionaries.
* [ ] I can use `keys()`.
* [ ] I can use `values()`.
* [ ] I can use `items()`.
* [ ] I can loop through nested dictionaries.
* [ ] I understand nested loops.
* [ ] I can use conditions with nested dictionaries.
* [ ] I can calculate totals from nested data.
* [ ] I can filter nested records.
* [ ] I understand shallow copying.
* [ ] I understand deep copying.
* [ ] I understand the difference between `copy()` and `deepcopy()`.
* [ ] I can use nested dictionaries in real-world programs.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use nested dictionaries without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Dictionary Comprehension**

In the next topic, you will learn:

* What dictionary comprehension is.
* Basic dictionary comprehension syntax.
* Creating dictionaries using comprehensions.
* Using expressions in dictionary comprehensions.
* Using conditions with dictionary comprehensions.
* Using `if` conditions.
* Using `if-else` conditions.
* Using loops with dictionary comprehensions.
* Creating dictionaries from lists.
* Creating dictionaries from two lists.
* Using `zip()` with dictionary comprehension.
* Practical real-world examples.
* Common mistakes.
* Advanced dictionary comprehension techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Nested dictionaries help Python represent complex real-world data in a clear and organized structure."** 🐍📚
