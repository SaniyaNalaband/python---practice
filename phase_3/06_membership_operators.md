# 🐍 Python Master Course

> **Phase 3:** Operators  
> **Topic 6:** Membership Operators

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand membership operators.
- [ ] Use `in` and `not in`.
- [ ] Check whether an element exists in a sequence or collection.
- [ ] Use membership operators with strings, lists, tuples, sets, and dictionaries.
- [ ] Write real-world programs using membership operators.

---

# 📖 What are Membership Operators?

Membership operators are used to check whether a value **exists inside** a sequence or collection.

Python has **two membership operators**:

| Operator | Meaning |
|----------|---------|
| `in` | Returns `True` if the value exists |
| `not in` | Returns `True` if the value does not exist |

Membership operators always return a Boolean value:

- `True`
- `False`

---

# 📚 Types of Membership Operators

| Operator | Description |
|----------|-------------|
| `in` | Checks if a value exists |
| `not in` | Checks if a value does not exist |

---

# 1️⃣ `in` Operator

The `in` operator checks whether a value exists in a sequence.

### Syntax

```python
value in collection
```

---

## Example with String

```python
text = "Python"

print("P" in text)
```

Output

```text
True
```

---

```python
print("z" in "Python")
```

Output

```text
False
```

---

## Example with List

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
```

Output

```text
True
```

---

```python
print(100 in numbers)
```

Output

```text
False
```

---

## Example with Tuple

```python
fruits = ("Apple", "Mango", "Banana")

print("Apple" in fruits)
```

Output

```text
True
```

---

## Example with Set

```python
colors = {"Red", "Blue", "Green"}

print("Blue" in colors)
```

Output

```text
True
```

---

## Example with Dictionary

Membership checks **keys**, not values.

```python
student = {
    "name": "Saniya",
    "age": 21
}

print("name" in student)
```

Output

```text
True
```

---

```python
print("Saniya" in student)
```

Output

```text
False
```

Because `"Saniya"` is a **value**, not a key.

---

# 2️⃣ `not in` Operator

Checks whether a value does **not** exist.

### Syntax

```python
value not in collection
```

---

## Example with String

```python
print("x" not in "Python")
```

Output

```text
True
```

---

## Example with List

```python
numbers = [1, 2, 3]

print(10 not in numbers)
```

Output

```text
True
```

---

## Example with Tuple

```python
fruits = ("Apple", "Orange")

print("Banana" not in fruits)
```

Output

```text
True
```

---

## Example with Set

```python
colors = {"Red", "Blue"}

print("Green" not in colors)
```

Output

```text
True
```

---

## Example with Dictionary

```python
student = {
    "name": "Saniya",
    "age": 21
}

print("city" not in student)
```

Output

```text
True
```

---

# 📖 Membership with Dictionary Values

To check dictionary **values**, use `.values()`.

```python
student = {
    "name": "Saniya",
    "age": 21
}

print("Saniya" in student.values())
```

Output

```text
True
```

---

To check dictionary **keys**, use `.keys()`.

```python
print("name" in student.keys())
```

Output

```text
True
```

---

# 📖 Membership with Dictionary Items

Use `.items()` to check complete key-value pairs.

```python
student = {
    "name": "Saniya",
    "age": 21
}

print(("name", "Saniya") in student.items())
```

Output

```text
True
```

---

# 📊 Summary Table

| Collection | Example | Result |
|------------|---------|--------|
| String | `"P" in "Python"` | `True` |
| List | `20 in [10,20,30]` | `True` |
| Tuple | `"Apple" in ("Apple","Mango")` | `True` |
| Set | `"Red" in {"Red","Blue"}` | `True` |
| Dictionary Key | `"name" in student` | `True` |
| Dictionary Value | `"Saniya" in student.values()` | `True` |

---

# ⚠️ Common Mistakes

## ❌ Expecting Dictionary Values to Be Checked

```python
student = {
    "name": "Saniya"
}

print("Saniya" in student)
```

Output

```text
False
```

Reason:

Membership checks dictionary **keys**.

Correct:

```python
print("Saniya" in student.values())
```

---

## ❌ Confusing `in` with `==`

Incorrect

```python
print("P" == "Python")
```

Output

```text
False
```

Correct

```python
print("P" in "Python")
```

Output

```text
True
```

---

## ❌ Case Sensitivity

```python
print("python" in "Python")
```

Output

```text
False
```

Python is case-sensitive.

---

# 💡 Best Practices

- Use `in` for readability.
- Use `not in` instead of writing `not (value in collection)`.
- Remember that dictionary membership checks keys by default.
- Use `.values()` or `.items()` when appropriate.

---

# 🚀 Pro Tips

Membership operators are commonly used in:

- Searching lists
- Input validation
- Password validation
- Login systems
- Data filtering
- AI & Machine Learning
- Web Development

---

# 🌍 Real-World Programs

## Check Username

```python
users = ["Rahul", "Saniya", "Aisha"]

print("Saniya" in users)
```

Output

```text
True
```

---

## Check Allowed File Extension

```python
filename = "photo.jpg"

print(".jpg" in filename)
```

Output

```text
True
```

---

## Check Available Product

```python
products = ["Laptop", "Mouse", "Keyboard"]

print("Laptop" in products)
```

Output

```text
True
```

---

## Check Subject

```python
subjects = ("Math", "Science", "English")

print("History" not in subjects)
```

Output

```text
True
```

---

# ❓ Interview Questions

- [ ] What are membership operators?
- [ ] What is the difference between `in` and `not in`?
- [ ] Which collections support membership operators?
- [ ] What does `in` check in a dictionary?
- [ ] How do you check dictionary values?

---

# 🏋️ Practice Programs

## Easy

```python
print("a" in "Apple")
```

---

```python
numbers = [10, 20, 30]

print(20 in numbers)
```

---

```python
print(100 not in [10, 20, 30])
```

---

## Medium

```python
fruits = ("Apple", "Banana", "Mango")

print("Orange" not in fruits)
```

---

```python
colors = {"Red", "Blue"}

print("Green" in colors)
```

---

```python
student = {
    "name": "Rahul",
    "age": 20
}

print("name" in student)
```

---

## Advanced

```python
student = {
    "name": "Saniya",
    "course": "AI & ML",
    "year": 2
}

print("course" in student)
print("AI & ML" in student.values())
print(("name", "Saniya") in student.items())
```

---

# 🎯 Challenge

Write a program that:

1. Creates a list of five programming languages.
2. Takes a language as input from the user.
3. Prints:
   - `"Language Found"` if it exists.
   - `"Language Not Found"` if it doesn't.

Example

```text
Enter language: Python

Language Found
```

---

# 📝 Assignment

- [x] Check if a character exists in a string.
- [x] Check if a number exists in a list.
- [x] Check if a fruit exists in a tuple.
- [x] Check if a color exists in a set.
- [x] Check if a key exists in a dictionary.
- [x] Check if a value exists using `.values()`.
- [x] Check a key-value pair using `.items()`.

---

# 📚 Summary

You learned:

- ✅ `in`
- ✅ `not in`
- ✅ Membership with strings
- ✅ Membership with lists
- ✅ Membership with tuples
- ✅ Membership with sets
- ✅ Membership with dictionary keys
- ✅ Membership with dictionary values using `.values()`
- ✅ Membership with key-value pairs using `.items()`

Remember:

- `in` → Checks whether a value exists.
- `not in` → Checks whether a value does not exist.
- In dictionaries, `in` checks **keys by default**, not values.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `in` operator.
- [x] I understand the `not in` operator.
- [x] I know how membership works with strings, lists, tuples, and sets.
- [x] I know that dictionaries check keys by default.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 7: Bitwise Operators**