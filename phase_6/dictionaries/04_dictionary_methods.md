# 🐍 Python Master Course

# 📦 Phase 6: Collections – Dictionaries

## 📌 Topic 4: Dictionary Methods

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what dictionary methods are.
* [ ] Understand how dictionary methods work.
* [ ] Use the `get()` method.
* [ ] Use the `keys()` method.
* [ ] Use the `values()` method.
* [ ] Use the `items()` method.
* [ ] Use the `update()` method.
* [ ] Use the `pop()` method.
* [ ] Use the `popitem()` method.
* [ ] Use the `clear()` method.
* [ ] Use the `copy()` method.
* [ ] Use the `setdefault()` method.
* [ ] Use the `fromkeys()` method.
* [ ] Understand the difference between dictionary methods.
* [ ] Understand which methods modify the original dictionary.
* [ ] Understand which methods return a value.
* [ ] Use dictionary methods in real-world examples.
* [ ] Avoid common mistakes when using dictionary methods.

---

# 📖 1. What are Dictionary Methods?

**Dictionary methods** are built-in functions provided by Python that allow you to work with dictionaries.

They can be used to:

* Access data.
* Add data.
* Update data.
* Remove data.
* Copy dictionaries.
* Get keys and values.
* Clear dictionaries.

Example:

```python  
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.keys())  
```

Output:

```text 
dict_keys(['name', 'age'])  
```

Here, `keys()` is a dictionary method.

---

# 🧠 2. Basic Dictionary Method Syntax

The general syntax is:

```python  
dictionary.method()  
```

Example:

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.keys())  
```

The dictionary is:

```text  
student  
```

The method is:

```text
keys()  
```

Together:

```text 
student.keys()  
```

---

# 📚 3. Important Dictionary Methods

Python provides several useful dictionary methods.

| Method         | Purpose                                  |
| -------------- | ---------------------------------------- |
| `get()`        | Gets a value using a key                 |
| `keys()`       | Returns all dictionary keys              |
| `values()`     | Returns all dictionary values            |
| `items()`      | Returns key-value pairs                  |
| `update()`     | Adds or updates key-value pairs          |
| `pop()`        | Removes a specified key                  |
| `popitem()`    | Removes the last inserted key-value pair |
| `clear()`      | Removes all items                        |
| `copy()`       | Creates a shallow copy                   |
| `setdefault()` | Gets a value or inserts a default        |
| `fromkeys()`   | Creates a dictionary from keys           |

---

# 🔍 4. The `get()` Method

The `get()` method is used to retrieve the value associated with a key.

Example:

```python   
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.get("name"))  
```

Output:

```text 
Asha  
```

---

# 🧠 5. Understanding `get()`

Consider:

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

Here:

```text  
"age" → key  
20    → value  
```

The `get()` method finds the value associated with `"age"`.

---

# ⚠️ 6. `get()` with a Missing Key

If the key does not exist, `get()` returns `None` by default.

```python id="p5r8x2"  
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.get("city"))  
```

Output:

```text   
None  
```

The program does not produce a `KeyError`.

---

# 🛡️ 7. `get()` with a Default Value

You can provide a default value when the key does not exist.

```python" 
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

Syntax:

```python 
dictionary.get(key, default_value)  
```

---

# ⚖️ 8. `[]` vs `get()`

There are two common ways to access a dictionary value.

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

Both return:

```text  
Asha  
```

But their behavior is different when the key is missing.

---

# ⚠️ 9. Missing Key with `[]`

```python 
student = {  
    "name": "Asha"  
}  
  
print(student["city"])  
```

This produces:

```text 
KeyError: 'city'  
```

---

# 🛡️ 10. Missing Key with `get()`

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

Therefore:

```text 
[]       → KeyError if key is missing  
get()    → None if key is missing  
```

---

# 🔑 11. The `keys()` Method

The `keys()` method returns a view containing all dictionary keys.

Example:

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.keys())  
```

Output:

```text 
dict_keys(['name', 'age', 'course'])  
```

---

# 🔄 12. Converting `keys()` to a List

The result of `keys()` can be converted into a list.

student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
keys = list(student.keys())  
  
print(keys)  
```

Output:

```text 
['name', 'age', 'course']  
```

---

# 🔁 13. Looping Through `keys()`

You can use `keys()` with a loop.

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
for key in student.keys():  
    print(key)  
```

Output:

```text 
name  
age  
course  
```

---

# 💰 14. The `values()` Method

The `values()` method returns a view containing all dictionary values.

Example:

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.values())  
```

Output:

```text 
dict_values(['Asha', 20, 'BCA'])  
```

---

# 🔄 15. Converting `values()` to a List

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
values = list(student.values())  
  
print(values)  
```

Output:

```text 
['Asha', 20, 'BCA']  
```

---

# 🔁 16. Looping Through `values()`

```python   
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
for value in student.values():  
    print(value)  
```

Output:

```text  
Asha  
20  
BCA  
```

---

# 🔗 17. The `items()` Method

The `items()` method returns all dictionary key-value pairs.

Example:

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.items())  
```

Output:

dict_items([('name', 'Asha'), ('age', 20), ('course', 'BCA')])  
```

---

# 🧩 18. Understanding `items()`

Each item is returned as a tuple.
  
('name', 'Asha')  
('age', 20)  
('course', 'BCA')  
```

Each tuple contains:

```text
(key, value)  
```

---

# 🔁 19. Looping Through `items()`

`items()` is commonly used when you need both keys and values.

```python id="c7m4n1"  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
for key, value in student.items():  
    print(key, "=", value)  
```

Output:

```text 
name = Asha  
age = 20  
course = BCA  
```

---

# 🧠 20. `keys()` vs `values()` vs `items()`

| Method     | Returns         |
| ---------- | --------------- |
| `keys()`   | Keys            |
| `values()` | Values          |
| `items()`  | Key-value pairs |

Example:

```python   
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.keys())  
print(student.values())  
print(student.items())  
```

---

# 🔄 21. The `update()` Method

The `update()` method is used to add new key-value pairs or modify existing values.

Example:

```python   
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
student.update({  
    "course": "BCA"  
})  
  
print(student)  
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}  
```

---

# ✏️ 22. Updating an Existing Value with `update()`

If the key already exists, its value is replaced.

```python   
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
student.update({  
    "age": 21  
})  
  
print(student)  
```

Output:

```text  
{'name': 'Asha', 'age': 21}  
```

---

# ➕ 23. Adding Multiple Items with `update()`

```python 
student = {  
    "name": "Asha"  
}  
  
student.update({  
    "age": 20,  
    "course": "BCA",  
    "city": "Bengaluru"  
})  
  
print(student)  
```

Output:

```text   
{'name': 'Asha', 'age': 20, 'course': 'BCA', 'city': 'Bengaluru'}  
```

---

# 🧩 24. `update()` Using Keyword Arguments

You can also provide key-value pairs as keyword arguments.

```python 
student = {  
    "name": "Asha"  
}  
  
student.update(age=20, course="BCA")  
  
print(student)  
```

Output:

```text 
{'name': 'Asha', 'age': 20, 'course': 'BCA'}  
```

---

# 🗑️ 25. The `pop()` Method

The `pop()` method removes a specified key and returns its value.

Example:

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
removed_value = student.pop("age")  
  
print(removed_value)  
print(student)  
```

Output:

```text 
20  
{'name': 'Asha', 'course': 'BCA'}  
```

---

# 🧠 26. Understanding `pop()`

Before `pop()`:

```text 
name   → Asha  
age    → 20  
course → BCA  
```

After:

```python 
student.pop("age")  
```

The `"age"` key and its value are removed.

After:

```text 
name   → Asha  
course → BCA  
```

---

# ⚠️ 27. `pop()` with a Missing Key

If the key does not exist, `pop()` raises a `KeyError` unless a default value is provided.

```python   
student = {  
    "name": "Asha"  
}  
  
print(student.pop("city"))  
```

This produces:

```text  
KeyError: 'city'  
```

---

# 🛡️ 28. `pop()` with a Default Value

You can provide a default value.

```python
student = {  
    "name": "Asha"  
}  
  
result = student.pop("city", "Not Found")  
  
print(result)  
```

Output:

```text 
Not Found  
```

---

# 🗑️ 29. The `popitem()` Method

The `popitem()` method removes and returns the **last inserted key-value pair**.

Example:

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
item = student.popitem()  
  
print(item)  
print(student)  
```

Output:

```text
('course', 'BCA')  
{'name': 'Asha', 'age': 20}  
```

---

# 🧠 30. Understanding `popitem()`

Before:

```text 
name   → Asha  
age    → 20  
course → BCA  
```

The last inserted item is:

```text i
course → BCA  
```

After `popitem()`:

```text
name → Asha  
age  → 20  
```

---

# ⚠️ 31. `pop()` vs `popitem()`

| Method      | Removes                      |
| ----------- | ---------------------------- |
| `pop(key)`  | A specified key              |
| `popitem()` | Last inserted key-value pair |

Example:

```python 
student.pop("age")  
```

removes `"age"`.

Whereas:

```python 
student.popitem()  
```

removes the last inserted item.

---

# 🧹 32. The `clear()` Method

The `clear()` method removes all items from a dictionary.

Example:

```python id="x9c3w5"  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
student.clear()  
  
print(student)  
```

Output:

```text 
{}  
```

---

# 🧠 33. Understanding `clear()`

Before:

```text 
name   → Asha  
age    → 20  
course → BCA  
```

After:

```text 
{}  
```

The dictionary still exists, but it contains no items.

---

# 📋 34. The `copy()` Method

The `copy()` method creates a **shallow copy** of a dictionary.

Example:

```python   
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
new_student = student.copy()  
  
print(new_student)  
```

Output:

```text 
{'name': 'Asha', 'age': 20}  
```

---

# 🔍 35. Understanding `copy()`

The original dictionary is:

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
```

Create a copy:

```python
new_student = student.copy()  
```

Now there are two separate dictionary objects.

```text 
student      → Original dictionary  
new_student  → Copied dictionary  
```

---

# ⚖️ 36. `copy()` vs Assignment

These are different:

### Assignment

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
new_student = student  
```

Both variables refer to the same dictionary object.

### `copy()`

```python 
new_student = student.copy()  
```

This creates a separate shallow copy.

---

# 🧠 37. Demonstrating `copy()`

```python  
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
new_student = student.copy()  
  
new_student["age"] = 21  
  
print(student)  
print(new_student)  
```

Output:

```text 
{'name': 'Asha', 'age': 20}  
{'name': 'Asha', 'age': 21}  
```

Changing the copied dictionary does not change the original for these simple values.

---

# ⚙️ 38. The `setdefault()` Method

The `setdefault()` method returns the value of a key if it exists.

If the key does not exist, it inserts the key with a default value.

Example:

```python  
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
result = student.setdefault("age", 25)  
  
print(result)  
print(student)  
```

Output:

```text 
20  
{'name': 'Asha', 'age': 20}  
```

Because `"age"` already exists, its value is not changed.

---

# ➕ 39. `setdefault()` with a Missing Key

```python  
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
result = student.setdefault("city", "Bengaluru")  
  
print(result)  
print(student)  
```

Output:

```text  
Bengaluru  
{'name': 'Asha', 'age': 20, 'city': 'Bengaluru'}  
```

The missing key is added to the dictionary.

---

# ⚖️ 40. `get()` vs `setdefault()`

These methods may look similar, but they behave differently.

### `get()`

```python
student = {  
    "name": "Asha"  
}  
  
print(student.get("city", "Bengaluru"))  
print(student)  
```

Output:

```text  
Bengaluru  
{'name': 'Asha'}  
```

`get()` does not add the key.

### `setdefault()`

```python
student = {  
    "name": "Asha"  
}  
  
print(student.setdefault("city", "Bengaluru"))  
print(student)  
```

Output:

```text 
Bengaluru  
{'name': 'Asha', 'city': 'Bengaluru'}  
```

`setdefault()` adds the key if it does not exist.

---

# 🏗️ 41. The `fromkeys()` Method

The `fromkeys()` method creates a new dictionary using a sequence of keys.

Example:

```python 
keys = ["name", "age", "course"]  
  
student = dict.fromkeys(keys)  
  
print(student)  
```

Output:

```text  
{'name': None, 'age': None, 'course': None}  
```

---

# 🔢 42. `fromkeys()` with a Default Value

You can provide a common value for all keys.

```python 
subjects = ["Python", "SQL", "Git"]  
  
marks = dict.fromkeys(subjects, 0)  
  
print(marks)  
```

Output:

```text 
{'Python': 0, 'SQL': 0, 'Git': 0}  
```

---

# 🧠 43. Understanding `fromkeys()`

Consider:

```python  
keys = ["Python", "SQL", "Git"]  
  
marks = dict.fromkeys(keys, 0)  
```

Python creates:

```text 
Python → 0  
SQL    → 0  
Git    → 0  
```

All keys receive the same initial value.

---

# ⚠️ 44. Dictionary Methods That Modify the Dictionary

Some dictionary methods directly modify the original dictionary.

These include:

```text
update()  
pop()  
popitem()  
clear()  
setdefault()  
```

Example:

```python  
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
student.update({"course": "BCA"})  
  
print(student)  
```

The original dictionary is changed.

---

# 🔍 45. Dictionary Methods That Return Information

Some methods are mainly used to retrieve or inspect data.

These include:

```text   
get()  
keys()  
values()  
items()  
```

Example:

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.get("name"))  
print(student.keys())  
print(student.values())  
print(student.items())  
```

---

# 📊 46. Dictionary Methods Comparison

| Method         | Main Purpose            | Modifies Dictionary?     |
| -------------- | ----------------------- | ------------------------ |
| `get()`        | Get a value             | ❌                        |
| `keys()`       | Get keys                | ❌                        |
| `values()`     | Get values              | ❌                        |
| `items()`      | Get key-value pairs     | ❌                        |
| `update()`     | Add/update items        | ✅                        |
| `pop()`        | Remove specified item   | ✅                        |
| `popitem()`    | Remove last item        | ✅                        |
| `clear()`      | Remove all items        | ✅                        |
| `copy()`       | Create a shallow copy   | ❌                        |
| `setdefault()` | Get/add default value   | Sometimes                |
| `fromkeys()`   | Create a new dictionary | Creates a new dictionary |

---

# 🌍 47. Real-World Example: Student Record

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA",  
    "percentage": 85.5  
}  
  
print(student.get("name"))  
  
student.update({  
    "semester": 4  
})  
  
print(student)  
```

Output:

```text 
Asha  
{'name': 'Asha', 'age': 20, 'course': 'BCA', 'percentage': 85.5, 'semester': 4}  
```

---

# 🌍 48. Real-World Example: Product Inventory

```python 
product = {  
    "name": "Laptop",  
    "price": 55000,  
    "stock": 10  
}  
  
product.update({  
    "brand": "Dell"  
})  
  
product["stock"] = product["stock"] - 1  
  
print(product)  
```

Output:

```text id="m8r4x6"  
{'name': 'Laptop', 'price': 55000, 'stock': 9, 'brand': 'Dell'}  
```

---

# 🌍 49. Real-World Example: Employee Information

```python id="v2k7q4"  
employee = {  
    "id": 101,  
    "name": "Neha",  
    "department": "IT",  
    "salary": 45000  
}  
  
for key, value in employee.items():  
    print(key, ":", value)  
```

Output:

```text 
id : 101  
name : Neha  
department : IT  
salary : 45000  
```

---

# 🌍 50. Real-World Example: Removing Product Data

```python id="r9w3n5"  
product = {  
    "name": "Laptop",  
    "brand": "Dell",  
    "price": 55000,  
    "stock": 10  
}  
  
removed_price = product.pop("price")  
  
print("Removed price:", removed_price)  
print(product)  
```

Output:

```text  
Removed price: 55000  
{'name': 'Laptop', 'brand': 'Dell', 'stock': 10}  
```

---

# 💻 51. Practice Programs

## 🟢 Easy

### Program 1: Use `get()`

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.get("name"))  
```

---

### Program 2: Use `keys()`

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.keys())  
```

---

### Program 3: Use `values()`

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.values())  
```

---

### Program 4: Use `items()`

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
print(student.items())  
```

---

# 🟡 Medium

### Program 5: Update a Dictionary

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

---

### Program 6: Remove an Item Using `pop()`

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
student.pop("age")  
  
print(student)  
```

---

### Program 7: Remove the Last Item

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA"  
}  
  
print(student.popitem())  
print(student)  
```

---

### Program 8: Clear a Dictionary

```python 
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
student.clear()  
  
print(student)  
```

---

# 🔴 Advanced

## Program 9: Use `setdefault()`

```python   
student = {  
    "name": "Asha",  
    "age": 20  
}  
  
student.setdefault("city", "Bengaluru")  
  
print(student)  
```

---

## Program 10: Student Information System

```python  
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA",  
    "percentage": 86.5  
}  
  
print("Student Name:", student.get("name"))  
  
student.update({  
    "semester": 4  
})  
  
for key, value in student.items():  
    print(key, ":", value)  
```

---

## Program 11: Product Inventory Management

```python 
product = {  
    "name": "Laptop",  
    "brand": "Dell",  
    "price": 55000,  
    "stock": 10  
}  
  
product.update({  
    "category": "Electronics"  
})  
  
removed_item = product.pop("stock")  
  
print("Removed stock:", removed_item)  
print(product)  
```

---

## Program 12: Create a Dictionary Using `fromkeys()`

```python 
subjects = [  
    "Python",  
    "SQL",  
    "Git",  
    "HTML"  
]  
  
progress = dict.fromkeys(subjects, "Not Started")  
  
print(progress)  
```

---

# 🏆 52. Challenge

Create a student dictionary containing:

```text
name  
age  
course  
semester  
percentage  
city  
```

Then perform the following operations:

1. Display the student's name using `get()`.
2. Display all keys using `keys()`.
3. Display all values using `values()`.
4. Display all key-value pairs using `items()`.
5. Add a new `"college"` key using `update()`.
6. Remove `"city"` using `pop()`.
7. Add a default `"status"` using `setdefault()`.
8. Display the final dictionary.

Example structure:

```python 
student = {  
    "name": "Asha",  
    "age": 20,  
    "course": "BCA",  
    "semester": 4,  
    "percentage": 85.5,  
    "city": "Bengaluru"  
}  
```

Try completing the challenge without copying the solution.

---

# 🧪 53. Mini Project: Product Inventory

Create a product inventory using a dictionary.

Your dictionary should contain:

* Product ID
* Product name
* Brand
* Price
* Category
* Stock

Perform the following operations:

* Display the product name using `get()`.
* Display all keys.
* Display all values.
* Display all key-value pairs.
* Add a rating using `update()`.
* Remove the stock using `pop()`.
* Add a default availability status using `setdefault()`.

Example:

```python id="r6v2k9"  
product = {  
    "product_id": 101,  
    "name": "Laptop",  
    "brand": "Dell",  
    "price": 55000,  
    "category": "Electronics",  
    "stock": 10  
}  
```

### Your Goal

Create your own product inventory and use as many dictionary methods as possible.

---

# 🎤 54. Interview Questions

* [ ] What are dictionary methods in Python?
* [ ] What is the `get()` method?
* [ ] What happens when `get()` is used with a missing key?
* [ ] How can you provide a default value using `get()`?
* [ ] What is the difference between `get()` and `[]`?
* [ ] What does the `keys()` method return?
* [ ] What does the `values()` method return?
* [ ] What does the `items()` method return?
* [ ] How can you loop through dictionary keys?
* [ ] How can you loop through dictionary values?
* [ ] How can you loop through both keys and values?
* [ ] What is the `update()` method?
* [ ] Can `update()` add new keys?
* [ ] Can `update()` modify existing values?
* [ ] What is the `pop()` method?
* [ ] What happens if `pop()` is used with a missing key?
* [ ] What is the `popitem()` method?
* [ ] What does `clear()` do?
* [ ] What does `copy()` do?
* [ ] What is the difference between assignment and `copy()`?
* [ ] What is the `setdefault()` method?
* [ ] What is the difference between `get()` and `setdefault()`?
* [ ] What does `fromkeys()` do?
* [ ] Which dictionary methods modify the original dictionary?
* [ ] Which dictionary methods are commonly used for retrieving information?

---

# 📝 55. Assignment

Complete the following programs.

### Task 1

Create a dictionary containing:

```text
name  
age  
course  
city  
```

Use `get()` to display the student's name.

---

### Task 2

Create a dictionary containing three subjects and their marks.

Use `keys()` to display all subjects.

---

### Task 3

Create a dictionary containing three products and their prices.

Use `values()` to display all prices.

---

### Task 4

Create a dictionary containing employee information.

Use `items()` to display every key and value.

---

### Task 5

Create a student dictionary and add two new items using `update()`.

---

### Task 6

Create a product dictionary and remove one item using `pop()`.

---

### Task 7

Create a dictionary and remove the last inserted item using `popitem()`.

---

### Task 8

Create a dictionary and remove all items using `clear()`.

---

### Task 9

Create a dictionary and make a copy using `copy()`.

Modify the copy and observe the original dictionary.

---

### Task 10

Create a dictionary containing student information.

Use `setdefault()` to add a `"status"` key if it does not already exist.

---

### Task 11

Create a dictionary using `dict.fromkeys()`.

Use the following keys:

```text
Python  
SQL  
Git  
HTML  
```

Set the initial value to `"Not Started"`.

---

### Task 12

Create a real-world dictionary and use at least five different dictionary methods on it.

---

# 🧠 56. Memory Tricks

Remember the most important dictionary methods:

```text
get()       → Get a value  
keys()      → Get keys  
values()    → Get values  
items()     → Get key-value pairs  
update()    → Add / Update  
pop()       → Remove specified key  
popitem()   → Remove last item  
clear()     → Remove everything  
copy()      → Make a copy  
setdefault()→ Get or add default  
fromkeys()  → Create dictionary from keys  
```

---

Remember the three most commonly used inspection methods:

```text id="w4m8q2"  
keys()  
  ↓  
Keys  
  
values()  
  ↓  
Values  
  
items()  
  ↓  
Key + Value  
```

---

Remember the removal methods:

```text id="n7c3r5"  
pop(key)  
   ↓  
Remove specified key  
  
popitem()  
   ↓  
Remove last inserted item  
  
clear()  
   ↓  
Remove everything  
```

---

# 📌 57. Important Rules to Remember

```text
1. Dictionary methods are called using dot notation.  
  
2. get() retrieves a value without raising KeyError for a missing key.  
  
3. keys() returns the dictionary keys.  
  
4. values() returns the dictionary values.  
  
5. items() returns key-value pairs.  
  
6. update() adds new items or changes existing values.  
  
7. pop() removes a specified key.  
  
8. popitem() removes the last inserted key-value pair.  
  
9. clear() removes all dictionary items.  
  
10. copy() creates a shallow copy of the dictionary.  
  
11. setdefault() returns an existing value or inserts a default value.  
  
12. fromkeys() creates a new dictionary from a sequence of keys.  
  
13. get() does not add a missing key.  
  
14. setdefault() can add a missing key.  
  
15. pop() can accept a default value for a missing key.  
  
16. Dictionary methods make dictionary operations easier and more readable.  
```

---

# 📊 58. Dictionary Methods Structure

```text
                     DICTIONARY METHODS  
                              │  
        ┌─────────────────────┼─────────────────────┐  
        ↓                     ↓                     ↓  
      ACCESS                MODIFY                REMOVE  
        │                     │                     │  
   ┌────┼────┐          ┌─────┼─────┐         ┌────┼────┐  
   ↓    ↓    ↓          ↓     ↓     ↓         ↓    ↓    ↓  
 get() keys values     update() setdefault()  pop() popitem() clear()  
        │  
        ↓  
      items()  
        │  
        ↓  
   Key + Value  
```

---

# 📚 59. Complete Dictionary Methods Cheat Sheet

### `get()`

```python  
student.get("name")  
```

### `keys()`

```python   
student.keys()  
```

### `values()`

```python   
student.values()  
```

### `items()`

```python 
student.items()  
```

### `update()`

```python 
student.update({"age": 21})  
```

### `pop()`

```python 
student.pop("age")  
```

### `popitem()`

```python   
student.popitem()  
```

### `clear()`

```python i 
student.clear()  
```

### `copy()`

```python   
new_student = student.copy()  
```

### `setdefault()`

```python 
student.setdefault("city", "Bengaluru")  
```

### `fromkeys()`

```python  
student = dict.fromkeys(["name", "age", "course"])  
```

---

# 🏆 60. Dictionary Methods Mastery

```text
                    DICTIONARY  
                         │  
                         ↓  
                Dictionary Methods  
                         │  
       ┌─────────────────┼─────────────────┐  
       ↓                 ↓                 ↓  
     ACCESS            MODIFY            REMOVE  
       │                 │                 │  
   ┌───┼───┐         ┌───┼────┐       ┌───┼────┐  
   ↓   ↓   ↓         ↓        ↓       ↓   ↓    ↓  
 get keys values   update setdefault pop popitem clear  
       │  
       ↓  
     items()  
       │  
       ↓  
  Key + Value  
```

---

# 📚 61. Summary

In this lesson, you learned:

* What dictionary methods are.
* How dictionary methods are called using dot notation.
* How to use the `get()` method.
* How `get()` behaves with missing keys.
* How to provide default values using `get()`.
* The difference between `get()` and `[]`.
* How to use the `keys()` method.
* How to use the `values()` method.
* How to use the `items()` method.
* How to loop through keys, values, and items.
* How to use the `update()` method.
* How to add and modify dictionary items using `update()`.
* How to use the `pop()` method.
* How to remove the last inserted item using `popitem()`.
* How to remove all items using `clear()`.
* How to create a shallow copy using `copy()`.
* The difference between assignment and `copy()`.
* How to use the `setdefault()` method.
* The difference between `get()` and `setdefault()`.
* How to use the `fromkeys()` method.
* Which dictionary methods modify the original dictionary.
* How dictionary methods are used in real-world programs.
* Common mistakes when using dictionary methods.

---

# 🎯 Topic Completion Checklist

* [x] I understand what dictionary methods are.
* [x] I know how to use dot notation with dictionary methods.
* [x] I can use `get()`.
* [x] I understand how `get()` handles missing keys.
* [x] I understand the difference between `get()` and `[]`.
* [x] I can use `keys()`.
* [x] I can use `values()`.
* [x] I can use `items()`.
* [x] I can loop through dictionary keys.
* [x] I can loop through dictionary values.
* [x] I can loop through dictionary key-value pairs.
* [x] I can use `update()`.
* [x] I can use `pop()`.
* [x] I can use `popitem()`.
* [x] I can use `clear()`.
* [x] I can use `copy()`.
* [x] I can use `setdefault()`.
* [x] I can use `fromkeys()`.
* [x] I understand which methods modify dictionaries.
* [x] I understand the difference between `get()` and `setdefault()`.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the assignment.
* [x] I can use dictionary methods without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Nested Dictionary**

In the next topic, you will learn:

* What a nested dictionary is.
* How to create nested dictionaries.
* Understanding dictionaries inside dictionaries.
* Accessing values from nested dictionaries.
* Modifying nested dictionary values.
* Adding new nested dictionary items.
* Removing items from nested dictionaries.
* Looping through nested dictionaries.
* Working with multiple nested dictionaries.
* Real-world examples of nested dictionaries.
* Student database examples.
* Product and employee records.
* Practical programs and challenges.

---

## ⭐ Quote of the Day

> **"Dictionary methods give you the power to access, update, organize, and manage your data efficiently."** 🐍📚
