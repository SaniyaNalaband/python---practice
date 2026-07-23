# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Collections → Dictionary**
> **Part 1:** What is a Dictionary?

**Difficulty:** ⭐⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a dictionary is.
- [ ] Create dictionaries.
- [ ] Access values using keys.
- [ ] Understand dictionary characteristics.
- [ ] Differentiate dictionaries from lists and sets.

---

# 📖 What is a Dictionary?

A **dictionary** is a collection of **key-value pairs**.

Each key is unique and is used to access its corresponding value.

Example:

```python
student = {
    "name": "Saniya",
    "age": 20,
    "course": "AI ML"
}

print(student)
```

Output

```text
{'name': 'Saniya', 'age': 20, 'course': 'AI ML'}
```

---

# 📖 Why Use a Dictionary?

Suppose you want to store information about a student.

Using a list:

```python
student = ["Saniya", 20, "AI ML"]
```

Problem:

What does `20` represent?

Age?

Marks?

Roll Number?

Not clear.

Dictionary:

```python
student = {
    "name": "Saniya",
    "age": 20,
    "course": "AI ML"
}
```

Now everything is clear because every value has a key.

---

# 📖 Dictionary Syntax

```python
dictionary = {
    key1: value1,
    key2: value2
}
```

Example

```python
car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2024
}
```

---

# 📖 Empty Dictionary

```python
data = {}

print(type(data))
```

Output

```text
<class 'dict'>
```

Another way:

```python
data = dict()
```

---

# 📖 Accessing Values

Use the key inside square brackets.

```python
student = {
    "name": "Saniya",
    "age": 20
}

print(student["name"])
print(student["age"])
```

Output

```text
Saniya
20
```

---

# 📖 Dictionaries are Mutable

Values can be changed.

```python
student = {
    "name": "Saniya",
    "age": 20
}

student["age"] = 21

print(student)
```

Output

```text
{'name': 'Saniya', 'age': 21}
```

---

# 📖 Keys Must Be Unique

```python
student = {
    "name": "Saniya",
    "name": "Rahul"
}

print(student)
```

Output

```text
{'name': 'Rahul'}
```

The last value overwrites the previous one.

---

# 📖 Values Can Be Duplicates

```python
marks = {
    "Math": 90,
    "Science": 90,
    "English": 85
}

print(marks)
```

Output

```text
{'Math': 90, 'Science': 90, 'English': 85}
```

Duplicate values are allowed.

---

# 📖 Allowed Key Types

Keys must be **immutable (hashable)**.

✅ Valid keys:

```python
data = {
    1: "One",
    "name": "Saniya",
    (10, 20): "Tuple"
}
```

---

❌ Invalid key:

```python
data = {
    [1, 2]: "List"
}
```

Output

```text
TypeError: unhashable type: 'list'
```

Lists are mutable, so they cannot be dictionary keys.

---

# 📖 Mixed Data Types

```python
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000,
    "is_manager": False
}

print(employee)
```

---

# 🌍 Real-World Examples

## Student Record

```python
student = {
    "name": "Saniya",
    "roll": 101,
    "course": "AI ML"
}
```

---

## User Profile

```python
user = {
    "username": "saniya123",
    "email": "saniya@gmail.com",
    "active": True
}
```

---

## Product Details

```python
product = {
    "name": "Laptop",
    "price": 55000,
    "stock": 25
}
```

---

# 📊 List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---------|------|-------|-----|------------|
| Ordered | ✅ | ✅ | ❌ | ✅* |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | Keys ❌ / Values ✅ |
| Indexing | ✅ | ✅ | ❌ | ❌ (Uses keys) |
| Brackets | `[]` | `()` | `{}` | `{key: value}` |

> **Note:** Dictionaries preserve insertion order in Python 3.7+.

---

# ⚠️ Common Mistakes

## ❌ Accessing a Missing Key

```python
student = {
    "name": "Saniya"
}

print(student["age"])
```

Output

```text
KeyError: 'age'
```

---

## ❌ Duplicate Keys

```python
data = {
    "a": 10,
    "a": 20
}

print(data)
```

Output

```text
{'a': 20}
```

---

## ❌ Using a List as a Key

```python
data = {
    [1, 2]: "Python"
}
```

Output

```text
TypeError
```

---

# 💡 Best Practices

- Use meaningful key names.
- Keep keys unique.
- Use immutable data types as keys.
- Use dictionaries when data has labels.

---

# 🚀 Pro Tips

A dictionary can store almost anything as a value.

```python
student = {
    "name": "Saniya",
    "marks": [90, 95, 88],
    "address": {
        "city": "Hubli",
        "state": "Karnataka"
    }
}

print(student)
```

Values can even be lists or other dictionaries.

---

# 🧠 Memory Trick

```text
Dictionary

↓

Key

↓

Value

↓

Key

↓

Value
```

Remember:

**K → V**

Every key has one corresponding value.

---

# ❓ Interview Questions

- [ ] What is a dictionary?
- [ ] What is a key-value pair?
- [ ] Are dictionary keys unique?
- [ ] Can values be duplicated?
- [ ] Can lists be dictionary keys?
- [ ] Are dictionaries mutable?

---

# 🏋️ Practice Programs

## Easy

```python
student = {
    "name": "Saniya",
    "age": 20
}

print(student)
```

---

```python
car = {
    "brand": "Toyota",
    "year": 2024
}

print(car["brand"])
```

---

## Medium

```python
employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 45000
}

employee["salary"] = 50000

print(employee)
```

---

## Advanced

```python
company = {
    "name": "TechSoft",
    "employees": 150,
    "departments": ["HR", "IT", "Finance"],
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

print(company)
```

---

# 🎯 Challenge

Create a dictionary named `book` with the following keys:

```text
title
author
price
pages
available
```

Perform the following:

1. Print the entire dictionary.
2. Print only the title.
3. Change the price.
4. Add a new key called `publisher`.
5. Print the updated dictionary.

---

# 📝 Assignment

- [x] Create a student dictionary.
- [x] Create an employee dictionary.
- [x] Create a product dictionary.
- [x] Access values using keys.
- [x] Modify one value.
- [x] Explain why dictionary keys must be unique.

---

# 📚 Summary

You learned:

- What a dictionary is.
- Key-value pairs.
- Dictionary syntax.
- Empty dictionaries.
- Accessing values.
- Mutable nature.
- Unique keys.
- Duplicate values.
- Valid key types.

---

# 🎯 Topic Completion Checklist

- [x] I understand what a dictionary is.
- [x] I know how to create a dictionary.
- [x] I know how to access values.
- [x] I understand dictionary characteristics.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Dictionary – Part 2: Dictionary Methods (`get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `popitem()`, `clear()`, `copy()`, `setdefault()`, `fromkeys()`, etc.)**