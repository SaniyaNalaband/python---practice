# 🐍 Python Master Course

# 📦 Phase 6: Collections – Dictionaries

## 📌 Topic 3: Updating Dictionary

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what updating a dictionary means.
* [ ] Understand how dictionaries are mutable.
* [ ] Update an existing dictionary value.
* [ ] Update values using dictionary keys.
* [ ] Add new key-value pairs using `[]`.
* [ ] Update multiple dictionary values.
* [ ] Use the `update()` method.
* [ ] Update a dictionary using another dictionary.
* [ ] Update a dictionary using keyword arguments.
* [ ] Understand the difference between adding and updating.
* [ ] Understand what happens when a key already exists.
* [ ] Understand what happens when a key does not exist.
* [ ] Update nested dictionaries.
* [ ] Update dictionary values containing lists.
* [ ] Avoid common mistakes while updating dictionaries.
* [ ] Use dictionary updating in real-world programs.

---

# 📖 1. What Does Updating a Dictionary Mean?

**Updating a dictionary** means changing existing values or adding new key-value pairs to a dictionary.

Dictionaries are **mutable**, which means their contents can be changed after creation.

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["age"] = 21 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21} 
```

Here, the value of `"age"` was changed from `20` to `21`.

---

# 🧠 2. Dictionaries Are Mutable

A dictionary can be changed after it has been created.

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["name"] = "Neha" 
 
print(student) 
```

Output:

```text
{'name': 'Neha', 'age': 20} 
```

The dictionary itself was modified.

This is called **mutation**.

---

# 🔑 3. Updating a Value Using a Key

The most basic way to update a dictionary is by using its key.

Syntax:

```python
dictionary_name[key] = new_value 
```

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["age"] = 21 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21} 
```

---

# 🔄 4. Updating a String Value

You can replace a string value with another string.

```python
student = { 
    "name": "Asha", 
    "course": "BCA" 
} 
 
student["course"] = "MCA" 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'course': 'MCA'} 
```

The value of `"course"` changed from `"BCA"` to `"MCA"`.

---

# 🔢 5. Updating an Integer Value

Dictionary values can be updated to another integer.

```python
product = { 
    "name": "Laptop", 
    "price": 50000 
} 
 
product["price"] = 55000 
 
print(product) 
```

Output:

```text
{'name': 'Laptop', 'price': 55000} 
```

---

# 🔢 6. Updating a Float Value

You can also update floating-point values.

```python
product = { 
    "name": "Laptop", 
    "rating": 4.2 
} 
 
product["rating"] = 4.6 
 
print(product) 
```

Output:

```text
{'name': 'Laptop', 'rating': 4.6} 
```

---

# 🔘 7. Updating a Boolean Value

Boolean values can also be updated.

```python
product = { 
    "name": "Laptop", 
    "in_stock": False 
} 
 
product["in_stock"] = True 
 
print(product) 
```

Output:

```text
{'name': 'Laptop', 'in_stock': True} 
```

---

# 📦 8. Updating a List Value

A dictionary can contain a list as a value, and the entire list can be replaced.

```python
student = { 
    "name": "Asha", 
    "skills": ["Python", "SQL"] 
} 
 
student["skills"] = ["Python", "SQL", "Git"] 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'skills': ['Python', 'SQL', 'Git']} 
```

---

# 🧩 9. Updating a Tuple Value

Tuple values can also be replaced.

```python
student = { 
    "name": "Asha", 
    "location": (12.97, 77.59) 
} 
 
student["location"] = (13.08, 80.27) 
 
print(student) 
```

The tuple value was replaced with another tuple.

---

# ➕ 10. Adding a New Key-Value Pair

Using `[]` can also add a new key-value pair.

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["course"] = "BCA" 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'} 
```

The key `"course"` did not exist before, so Python added it.

---

# 🧠 11. Updating vs Adding

The same syntax is used for both updating and adding.

### If the key already exists

The value is **updated**.

```python
student = { 
    "age": 20 
} 
 
student["age"] = 21 
```

Result:

```text
{'age': 21} 
```

### If the key does not exist

A new key-value pair is **added**.

```python
student = { 
    "age": 20 
} 
 
student["course"] = "BCA" 
```

Result:

```text
{'age': 20, 'course': 'BCA'} 
```

Remember:

```text
Key exists
    ↓
Update value
 
Key does not exist
    ↓
Add new key-value pair
```

---

# 🔄 12. Updating Multiple Values

You can update several dictionary values one after another.

```python
student = { 
    "name": "Asha", 
    "age": 20, 
    "course": "BCA" 
} 
 
student["name"] = "Neha" 
student["age"] = 21 
student["course"] = "MCA" 
 
print(student) 
```

Output:

```text
{'name': 'Neha', 'age': 21, 'course': 'MCA'} 
```

---

# 🛠️ 13. Using the `update()` Method

Python provides the `update()` method for updating dictionaries.

Syntax:

```python
dictionary_name.update(iterable) 
```

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update({"age": 21}) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21} 
```

---

# 🔄 14. Updating Multiple Values Using `update()`

You can update multiple values at once.

```python
student = { 
    "name": "Asha", 
    "age": 20, 
    "course": "BCA" 
} 
 
student.update({ 
    "age": 21, 
    "course": "MCA" 
}) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21, 'course': 'MCA'} 
```

---

# ➕ 15. Adding New Keys Using `update()`

`update()` can also add keys that do not already exist.

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update({ 
    "course": "BCA", 
    "city": "Bengaluru" 
}) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA', 'city': 'Bengaluru'} 
```

So `update()` can both **modify existing keys** and **add new keys**.

---

# 🧠 16. How `update()` Works

Suppose we have:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
```

Now:

```python
student.update({ 
    "age": 21, 
    "course": "BCA" 
}) 
```

Python checks each key:

```text
"age"
  ↓
Already exists
  ↓
Value becomes 21
 
"course"
  ↓
Does not exist
  ↓
New key-value pair is added
```

Final dictionary:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA'} 
```

---

# 🏗️ 17. Updating Using Keyword Arguments

The `update()` method can also receive keyword arguments.

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update( 
    age=21, 
    course="BCA" 
) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA'} 
```

---

# 🔤 18. Rules for Keyword Arguments in `update()`

When using keyword arguments, dictionary keys must be valid Python identifiers.

This works:

```python
student.update( 
    age=21, 
    course="BCA" 
) 
```

But keys containing spaces cannot be written directly as keyword arguments.

For such keys, use another dictionary:

```python
student.update({ 
    "student age": 21 
}) 
```

---

# 🔄 19. Updating from Another Dictionary

One dictionary can be used to update another dictionary.

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
new_data = { 
    "age": 21, 
    "course": "BCA" 
} 
 
student.update(new_data) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA'} 
```

The values from `new_data` are applied to `student`.

---

# ⚠️ 20. Existing Keys Are Replaced by `update()`

If the same key exists in both dictionaries, the value from the updating dictionary replaces the old value.

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
new_data = { 
    "age": 25 
} 
 
student.update(new_data) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 25} 
```

The old value `20` was replaced by `25`.

---

# ➕ 21. New Keys Are Added by `update()`

If a key does not exist, `update()` adds it.

```python
student = { 
    "name": "Asha" 
} 
 
student.update({ 
    "age": 20 
}) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 20} 
```

---

# 🔀 22. Updating with `dict()`

You can create another dictionary and use it with `update()`.

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update(dict( 
    age=21, 
    course="BCA" 
)) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA'} 
```

---

# 🧩 23. Updating Using a List of Tuples

`update()` can accept an iterable containing key-value pairs.

Example:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update([ 
    ("age", 21), 
    ("course", "BCA") 
]) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA'} 
```

Each tuple contains:

```text
(key, value)
```

---

# 🧠 24. Updating Using `zip()`

You can also use `zip()` with `update()`.

```python
student = { 
    "name": "Asha" 
} 
 
keys = ["age", "course"] 
values = [20, "BCA"] 
 
student.update(zip(keys, values)) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'} 
```

---

# 🔢 25. Updating a Numeric Value

Dictionary values can be updated using calculations.

```python
product = { 
    "name": "Laptop", 
    "price": 50000 
} 
 
product["price"] = product["price"] + 5000 
 
print(product) 
```

Output:

```text
{'name': 'Laptop', 'price': 55000} 
```

You can also write:

```python
product["price"] += 5000 
```

---

# ➕ 26. Increasing a Dictionary Value

This is useful for counters.

```python
scores = { 
    "Python": 80, 
    "SQL": 75 
} 
 
scores["Python"] += 5 
 
print(scores) 
```

Output:

```text
{'Python': 85, 'SQL': 75} 
```

---

# 🔢 27. Updating a Counter

Dictionaries are commonly used to store counts.

```python
visits = { 
    "Monday": 10, 
    "Tuesday": 15 
} 
 
visits["Monday"] += 1 
 
print(visits) 
```

Output:

```text
{'Monday': 11, 'Tuesday': 15} 
```

---

# ⚠️ 28. Updating a Missing Key with `+=`

This causes an error if the key does not already exist.

```python
scores = { 
    "Python": 80 
} 
 
scores["SQL"] += 5 
```

Typical error:

```text
KeyError: 'SQL'
```

Why?

Python first tries to read `scores["SQL"]`, but the key does not exist.

For a missing key, assign an initial value first:

```python
scores["SQL"] = 5 
```

---

# 🧠 29. Updating vs Assigning

Consider:

```python
student["age"] = 21 
```

This statement can mean two things depending on whether `"age"` already exists.

```text
Key exists
    ↓
Existing value is replaced
 
Key does not exist
    ↓
New key-value pair is created
```

So square-bracket assignment is both an **update operation** and an **addition operation**.

---

# 📦 30. Updating a List Inside a Dictionary

You can replace a list value.

```python
student = { 
    "name": "Asha", 
    "skills": ["Python", "SQL"] 
} 
 
student["skills"] = ["Python", "SQL", "Git"] 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'skills': ['Python', 'SQL', 'Git']} 
```

---

# ➕ 31. Adding an Item to a List Inside a Dictionary

You can also modify the list itself.

```python
student = { 
    "name": "Asha", 
    "skills": ["Python", "SQL"] 
} 
 
student["skills"].append("Git") 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'skills': ['Python', 'SQL', 'Git']} 
```

Here, the dictionary value is a list, and `.append()` modifies that list.

---

# 🏠 32. Updating a Nested Dictionary

A dictionary can contain another dictionary.

```python
student = { 
    "name": "Asha", 
    "address": { 
        "city": "Bengaluru", 
        "state": "Karnataka" 
    } 
} 
 
student["address"]["city"] = "Mysuru" 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'address': {'city': 'Mysuru', 'state': 'Karnataka'}} 
```

The inner dictionary was updated.

---

# 🧩 33. Adding a New Key to a Nested Dictionary

You can add new information to the nested dictionary.

```python
student = { 
    "name": "Asha", 
    "address": { 
        "city": "Bengaluru" 
    } 
} 
 
student["address"]["pincode"] = 560001 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'address': {'city': 'Bengaluru', 'pincode': 560001}} 
```

---

# 🔄 34. Updating Nested Data Using `update()`

You can use `update()` on an inner dictionary.

```python
student = { 
    "name": "Asha", 
    "address": { 
        "city": "Bengaluru", 
        "state": "Karnataka" 
    } 
} 
 
student["address"].update({ 
    "city": "Mysuru", 
    "pincode": 570001 
}) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'address': {'city': 'Mysuru', 'state': 'Karnataka', 'pincode': 570001}} 
```

---

# 🌍 35. Real-World Example: Updating Student Information

```python
student = { 
    "name": "Asha", 
    "age": 20, 
    "course": "BCA", 
    "percentage": 82.5 
} 
 
student["age"] = 21 
student["percentage"] = 87.5 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA', 'percentage': 87.5} 
```

---

# 🌍 36. Real-World Example: Updating Product Information

```python
product = { 
    "name": "Laptop", 
    "price": 50000, 
    "in_stock": True 
} 
 
product.update({ 
    "price": 55000, 
    "in_stock": False 
}) 
 
print(product) 
```

Output:

```text
{'name': 'Laptop', 'price': 55000, 'in_stock': False} 
```

---

# 🌍 37. Real-World Example: Updating Employee Information

```python
employee = { 
    "id": 101, 
    "name": "Neha", 
    "department": "IT", 
    "salary": 40000 
} 
 
employee.update({ 
    "department": "Development", 
    "salary": 45000 
}) 
 
print(employee) 
```

Output:

```text
{'id': 101, 'name': 'Neha', 'department': 'Development', 'salary': 45000} 
```

---

# 🌍 38. Real-World Example: Updating Mobile Phone Information

```python
phone = { 
    "brand": "Samsung", 
    "model": "Galaxy", 
    "price": 45000, 
    "storage": "128GB" 
} 
 
phone.update({ 
    "price": 42000, 
    "storage": "256GB" 
}) 
 
print(phone) 
```

Output:

```text
{'brand': 'Samsung', 'model': 'Galaxy', 'price': 42000, 'storage': '256GB'} 
```

---

# 🛠️ 39. `update()` Does Not Create a New Dictionary

The `update()` method changes the existing dictionary.

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
result = student.update({ 
    "age": 21 
}) 
 
print(student) 
print(result) 
```

Output:

```text
{'name': 'Asha', 'age': 21} 
None 
```

The dictionary is modified **in place**, and `update()` returns `None`.

---

# 🧠 40. Important: `update()` Returns `None`

This is a common beginner mistake.

Wrong expectation:

```python
student = { 
    "name": "Asha" 
} 
 
print(student.update({"age": 20})) 
```

Output:

```text
None 
```

Correct approach:

```python
student.update({"age": 20}) 
 
print(student) 
```

Output:

```text
{'name': 'Asha', 'age': 20} 
```

---

# ⚖️ 41. `[]` vs `update()`

Both can update dictionaries, but they are useful in different situations.

### Using `[]`

```python
student["age"] = 21 
```

Best for changing one specific key.

### Using `update()`

```python
student.update({ 
    "age": 21, 
    "course": "BCA" 
}) 
```

Best for updating multiple keys at once.

---

# 📊 42. Difference Between `[]` and `update()`

| Feature                     | `[]`                              | `update()` |
| --------------------------- | --------------------------------- | ---------- |
| Update one value            | ✅                                 | ✅          |
| Update multiple values      | Possible with multiple statements | ✅          |
| Add new keys                | ✅                                 | ✅          |
| Uses a key directly         | ✅                                 | ❌          |
| Updates dictionary in place | ✅                                 | ✅          |
| Returns updated dictionary  | ❌                                 | ❌          |
| Returns `None`              | ❌                                 | ✅          |

---

# ⚠️ 43. Common Mistakes

## ❌ Mistake 1: Using `=` Instead of Dictionary Assignment

Wrong:

```python
student = { 
    "age": 20 
} 
 
age = 21 
```

This creates or changes a separate variable. It does not update the dictionary.

Correct:

```python
student["age"] = 21 
```

---

## ❌ Mistake 2: Updating a Key That Is Spelled Differently

```python
student = { 
    "name": "Asha" 
} 
 
student["Name"] = "Neha" 
```

Output:

```text
{'name': 'Asha', 'Name': 'Neha'} 
```

Python treats `"name"` and `"Name"` as different keys.

---

## ❌ Mistake 3: Confusing Adding and Updating

```python
student = { 
    "name": "Asha" 
} 
 
student["age"] = 20 
```

This does not update an existing `"age"` key because it does not exist.

It **adds** a new key.

---

## ❌ Mistake 4: Expecting `update()` to Return the Dictionary

Wrong:

```python
student = { 
    "name": "Asha" 
} 
 
student = student.update({"age": 20}) 
 
print(student) 
```

Output:

```text
None 
```

Correct:

```python
student = { 
    "name": "Asha" 
} 
 
student.update({"age": 20}) 
 
print(student) 
```

---

## ❌ Mistake 5: Updating a Missing Key with `+=`

Wrong:

```python
scores = { 
    "Python": 80 
} 
 
scores["SQL"] += 5 
```

This produces:

```text
KeyError: 'SQL' 
```

The key must exist before using `+=`.

---

# 🧠 44. Updating a Dictionary Step by Step

Consider:

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["age"] = 21 
student["course"] = "BCA" 
```

Step 1:

```text
age → 20 
```

becomes:

```text
age → 21 
```

Step 2:

```text
course 
```

does not exist, so Python adds:

```text
course → BCA 
```

Final dictionary:

```text
{'name': 'Asha', 'age': 21, 'course': 'BCA'} 
```

---

# 📚 45. Updating Methods Summary

| Method      | Purpose                    | Example                           |
| ----------- | -------------------------- | --------------------------------- |
| `[]`        | Update/add one key         | `student["age"] = 21`             |
| `update()`  | Update/add multiple keys   | `student.update({"age": 21})`     |
| `+=`        | Increase an existing value | `scores["Python"] += 5`           |
| `.append()` | Modify a list value        | `student["skills"].append("Git")` |

---

# 💻 46. Practice Programs

## 🟢 Easy

### Program 1: Update Student Age

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["age"] = 21 
 
print(student) 
```

---

### Program 2: Update Student Course

```python
student = { 
    "name": "Asha", 
    "course": "BCA" 
} 
 
student["course"] = "MCA" 
 
print(student) 
```

---

### Program 3: Add a New Key

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student["city"] = "Bengaluru" 
 
print(student) 
```

---

### Program 4: Update Multiple Values

```python
student = { 
    "name": "Asha", 
    "age": 20, 
    "course": "BCA" 
} 
 
student["age"] = 21 
student["course"] = "MCA" 
 
print(student) 
```

---

# 🟡 Medium

### Program 5: Use `update()`

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update({ 
    "age": 21, 
    "course": "BCA" 
}) 
 
print(student) 
```

---

### Program 6: Update from Another Dictionary

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
new_data = { 
    "age": 21, 
    "course": "BCA" 
} 
 
student.update(new_data) 
 
print(student) 
```

---

### Program 7: Update Using Keyword Arguments

```python
student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update( 
    age=21, 
    course="BCA" 
) 
 
print(student) 
```

---

### Program 8: Update Using List of Tuples

```python
student = { 
    "name": "Asha" 
} 
 
student.update([ 
    ("age", 20), 
    ("course", "BCA") 
]) 
 
print(student) 
```

---

# 🔴 Advanced

## Program 9: Student Record Update

```python
student = { 
    "id": 101, 
    "name": "Asha", 
    "age": 20, 
    "course": "BCA", 
    "percentage": 82.5 
} 
 
student.update({ 
    "age": 21, 
    "course": "MCA", 
    "percentage": 88.5 
}) 
 
print(student) 
```

---

## Program 10: Nested Dictionary Update

```python
student = { 
    "name": "Asha", 
    "address": { 
        "city": "Bengaluru", 
        "state": "Karnataka" 
    } 
} 
 
student["address"].update({ 
    "city": "Mysuru", 
    "pincode": 570001 
}) 
 
print(student) 
```

---

# 🏆 47. Challenge

Create a product dictionary containing:

```text
product_id 
name 
brand 
price 
category 
in_stock 
rating 
```

Then update the following information:

```text
price 
rating 
in_stock 
category 
```

Also add a new key:

```text
discount 
```

Try solving the challenge without copying the example.

---

# 🧪 48. Mini Project: Student Record Updater

Create a student dictionary containing:

* Student ID
* Name
* Age
* Course
* Semester
* Percentage
* Skills
* Passed status

Then perform the following updates:

* Change the student's age.
* Change the course.
* Update the percentage.
* Add a city.
* Add a new skill.
* Update the passed status.

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
        "SQL" 
    ], 
    "passed": True 
} 
 
student["age"] = 21 
student["course"] = "MCA" 
student["percentage"] = 88.5 
student["city"] = "Bengaluru" 
student["skills"].append("Git") 
student["passed"] = True 
 
print(student) 
```

### Your Goal

Create your own student record and update it using both `[]` and `update()`.

---

# 🎤 49. Interview Questions

* [ ] What does updating a dictionary mean?
* [ ] Are dictionaries mutable?
* [ ] How do you update a dictionary value?
* [ ] How do you add a new key-value pair?
* [ ] What happens when you assign a value to an existing key?
* [ ] What happens when you assign a value to a new key?
* [ ] What is the `update()` method?
* [ ] How do you update multiple dictionary values?
* [ ] Can `update()` add new keys?
* [ ] What happens when `update()` receives an existing key?
* [ ] Can `update()` accept another dictionary?
* [ ] Can `update()` accept a list of tuples?
* [ ] Can `update()` use keyword arguments?
* [ ] What does `update()` return?
* [ ] Why does `update()` return `None`?
* [ ] What is the difference between `[]` and `update()`?
* [ ] How can you update a nested dictionary?
* [ ] How can you update a list stored inside a dictionary?
* [ ] What happens if you use `+=` with a missing dictionary key?
* [ ] How can dictionaries be used as counters?

---

# 📝 50. Assignment

Complete the following programs.

### Task 1

Create a dictionary containing:

```text
name 
age 
course 
```

Update the age.

---

### Task 2

Create a product dictionary.

Update:

```text
price 
rating 
in_stock 
```

---

### Task 3

Create a dictionary and add a new key using `[]`.

---

### Task 4

Create a dictionary and update multiple values using `update()`.

---

### Task 5

Create two dictionaries and use the second dictionary to update the first dictionary.

---

### Task 6

Use `update()` with keyword arguments.

---

### Task 7

Use a list of tuples with `update()`.

---

### Task 8

Create a dictionary containing a list of skills.

Add a new skill to the list using `.append()`.

---

### Task 9

Create a nested dictionary and update a value inside the nested dictionary.

---

### Task 10

Create a real-world student profile and perform at least five updates.

---

# 🧠 51. Memory Tricks

Remember the basic update syntax:

```text
dictionary[key] = new_value
```

Think:

> **Existing key → change its value.**

---

Remember adding a new key:

```text
New key
   ↓
dictionary[key] = value
   ↓
Added to dictionary
```

---

Remember `update()`:

```text
update()
   ↓
Existing key → Replace value
New key      → Add key-value pair
```

---

Remember:

```text
[]       → Best for direct/single updates
update() → Best for multiple updates
```

---

# 📌 52. Important Rules to Remember

```text
1. Dictionaries are mutable.

2. Existing dictionary values can be changed.

3. Use dictionary[key] = value to update a value.

4. If the key does not exist, [] assignment adds a new key.

5. update() can modify existing keys.

6. update() can add new keys.

7. update() can update multiple keys at once.

8. update() can accept another dictionary.

9. update() can accept a list of key-value pairs.

10. update() can accept keyword arguments.

11. update() modifies the dictionary in place.

12. update() returns None.

13. Existing keys are replaced by new values.

14. Dictionary keys are case-sensitive.

15. += requires the key to already exist.

16. Nested dictionaries can be updated using multiple keys.

17. Lists stored inside dictionaries can be modified using list methods.
```

---

# 📊 53. Dictionary Updating Structure

```text
                    UPDATE DICTIONARY
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
        dictionary[key]              update()
             │                           │
             ↓                           ↓
       Single update              Multiple updates
             │                           │
             ↓                           ↓
      Existing key?              Existing key?
        │       │                   │       │
       YES     NO                  YES     NO
        ↓       ↓                   ↓       ↓
     Replace   Add                Replace   Add
      value   key-value            value   key-value
```

---

# 📚 54. Complete Dictionary Updating Cheat Sheet

### Update One Value

```python
student["age"] = 21
```

### Add a New Key

```python
student["city"] = "Bengaluru"
```

### Update Multiple Values

```python
student.update({
    "age": 21,
    "course": "MCA"
})
```

### Update from Another Dictionary

```python
student.update(new_data)
```

### Update Using Keyword Arguments

```python
student.update(
    age=21,
    course="MCA"
)
```

### Update Using Tuples

```python
student.update([
    ("age", 21),
    ("course", "MCA")
])
```

### Update a Nested Dictionary

```python
student["address"]["city"] = "Mysuru"
```

### Modify a List Inside a Dictionary

```python
student["skills"].append("Git")
```

---

# 🏆 55. Dictionary Updating Mastery

```text
                 UPDATE DICTIONARY
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
         []          update()       Nested
          │             │             │
          ↓             ↓             ↓
     One key       Many keys      Inner data
          │             │             │
          ↓             ↓             ↓
     Update/Add    Update/Add     Update/Add
```

---

# 📚 56. Summary

In this lesson, you learned:

* What updating a dictionary means.
* Why dictionaries are mutable.
* How to update values using dictionary keys.
* How to add new key-value pairs using `[]`.
* The difference between adding and updating.
* How to update multiple values.
* How to use the `update()` method.
* How `update()` can add new keys.
* How `update()` replaces existing values.
* How to update dictionaries using another dictionary.
* How to use keyword arguments with `update()`.
* How to update using a list of tuples.
* How to use `zip()` with `update()`.
* How to update numeric values.
* How dictionaries can be used as counters.
* Why `+=` cannot be directly used with a missing key.
* How to update lists stored inside dictionaries.
* How to update nested dictionaries.
* Why `update()` returns `None`.
* The difference between `[]` and `update()`.
* Common mistakes when updating dictionaries.
* How to update dictionaries in real-world programs.

---

# 🎯 Topic Completion Checklist

* [x] I understand what updating a dictionary means.
* [x] I understand that dictionaries are mutable.
* [x] I can update a value using `[]`.
* [x] I can add a new key using `[]`.
* [x] I understand the difference between adding and updating.
* [x] I can update multiple values.
* [x] I understand the `update()` method.
* [x] I can use `update()` with a dictionary.
* [x] I can use `update()` with keyword arguments.
* [x] I can use `update()` with a list of tuples.
* [x] I understand that `update()` modifies the dictionary in place.
* [x] I know that `update()` returns `None`.
* [x] I understand how existing keys behave during `update()`.
* [x] I understand how new keys behave during `update()`.
* [x] I can update nested dictionaries.
* [x] I can modify lists stored inside dictionaries.
* [x] I understand the difference between `[]` and `update()`.
* [x] I understand why `+=` fails for missing keys.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the assignment.
* [x] I can update dictionaries without looking at my notes.



---

## ⭐ Quote of the Day

> **"A mutable dictionary can change as your data changes—update existing values, add new information, and keep your data current."** 🐍📚
