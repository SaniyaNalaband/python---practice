    # 🐍 Python Master Course

> **Phase 2:** Data Types
> **Collections → Tuple**
> **Part 1:** What is a Tuple?

**Difficulty:** ⭐⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a tuple is.
- [ ] Know why tuples are used.
- [ ] Create tuples.
- [ ] Differentiate tuples from lists.

---

# 📖 What is a Tuple?

A **tuple** is an **ordered collection** of items.

Like a list, a tuple can store multiple values.

Example:

```python
student = ("Saniya", 20, "AI ML", 8.9)

print(student)
```

Output

```text
('Saniya', 20, 'AI ML', 8.9)
```

---

# 📖 Why Use Tuples?

Suppose a student's roll number should never change.

Instead of a list:

```python
student = [101, "Saniya"]
```

Use a tuple:

```python
student = (101, "Saniya")
```

This prevents accidental modification.

---

# 📖 Tuple Syntax

```python
tuple_name = (item1, item2, item3)
```

Example

```python
colors = ("Red", "Green", "Blue")
```

Tuples use **parentheses `()`**.

---

# 📖 Empty Tuple

```python
empty = ()

print(empty)
```

Output

```text
()
```

---

# 📖 Single-Element Tuple

This is one of the most common beginner mistakes.

❌ Wrong

```python
num = (10)

print(type(num))
```

Output

```text
<class 'int'>
```

Python treats `(10)` as just the integer `10`.

---

✅ Correct

```python
num = (10,)

print(type(num))
```

Output

```text
<class 'tuple'>
```

The comma makes it a tuple.

---

# 📖 Tuples Can Store Different Data Types

```python
data = (
    "Python",
    100,
    True,
    95.5
)

print(data)
```

Output

```text
('Python', 100, True, 95.5)
```

---

# 📖 Tuples Allow Duplicates

```python
numbers = (10, 20, 20, 30)

print(numbers)
```

Output

```text
(10, 20, 20, 30)
```

---

# 📖 Ordered Collection

The order of elements is preserved.

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits)
```

Output

```text
('Apple', 'Banana', 'Mango')
```

Indexes:

```text
Apple  → 0
Banana → 1
Mango  → 2
```

---

# 🌍 Real-World Examples

## GPS Coordinates

```python
location = (12.9716, 77.5946)
```

Latitude and longitude usually shouldn't change.

---

## RGB Color

```python
red = (255, 0, 0)
```

---

## Student Record

```python
student = (
    101,
    "Saniya",
    "AI ML"
)
```

---

# 📊 List vs Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Brackets | `[]` | `()` |
| Ordered | ✅ | ✅ |
| Mutable | ✅ | ❌ |
| Duplicates | ✅ | ✅ |
| Mixed Data Types | ✅ | ✅ |

---

# ⚠️ Common Mistakes

## ❌ Forgetting the Comma

```python
value = (5)
```

This is an `int`.

Correct:

```python
value = (5,)
```

---

## ❌ Trying to Modify a Tuple

```python
colors = ("Red", "Green")

colors[0] = "Blue"
```

Output

```text
TypeError: 'tuple' object does not support item assignment
```

---

# 💡 Best Practices

- Use tuples for fixed data.
- Use lists for data that changes.
- Use meaningful variable names.

---

# 🧠 Memory Trick

```
Tuple

↓

()

↓

Ordered

↓

Immutable

↓

Duplicates Allowed
```

Remember:

**OID**

- **O** → Ordered
- **I** → Immutable
- **D** → Duplicates Allowed

---

# ❓ Interview Questions

- [x] What is a tuple?
- [x] Which brackets are used for tuples?
- [x] Are tuples mutable?
- [x] Can tuples contain duplicate values?
- [x] How do you create a single-element tuple?

---

# 🏋️ Practice Programs

## Easy

```python
colors = ("Red", "Green", "Blue")

print(colors)
```

---

```python
number = (10,)

print(type(number))
```

---

## Medium

```python
student = (
    "Saniya",
    20,
    True
)

print(student)
```

---

## Advanced

```python
employee = (
    101,
    "Rahul",
    0"Developer",
    50000
)

print(employee)
```

---

# 🎯 Challenge

Create tuples named:

- `countries`
- `marks`
- `languages`
- `rgb`

Print all of them.

---

# 📝 Assignment

- [x] Create a tuple of five fruits.
- [x] Create a tuple of five numbers.
- [x] Create a mixed-data-type tuple.
- [x] Create an empty tuple.
- [x] Create a single-element tuple.
- [x] Explain why the comma is needed in a single-element tuple.

---

# 📚 Summary

You learned:

- What a tuple is.
- Tuple syntax.
- Empty tuples.
- Single-element tuples.
- Mixed data types.
- Ordered collection.
- Duplicate values.

---

# 🎯 Topic Completion Checklist

- [x] I understand what a tuple is.
- [x] I know tuple syntax.
- [x] I know how to create a single-element tuple.
- [x] I understand the difference between a list and a tuple.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Tuple – Part 2: Tuple Characteristics**