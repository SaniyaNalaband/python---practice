# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 13:** Constants in Python

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a constant is.
- [ ] Know why constants are used.
- [ ] Learn how constants are created in Python.
- [ ] Understand Python naming conventions for constants.
- [ ] Differentiate between variables and constants.
- [ ] Follow best practices for using constants.

---

# 📖 1. What is a Constant?

A **constant** is a value that is **intended not to change** during the execution of a program.

Think of a constant as a **fixed value**.

Examples:

- Number of days in a week → `7`
- Number of months in a year → `12`
- Value of π (Pi) → `3.14159`
- Speed of light → `299792458`

These values usually remain the same.

---

# 🤔 2. Does Python Have Real Constants?

**No.**

Unlike languages such as C++ or Java, **Python does not have built-in constant variables.**

Instead, Python programmers follow a **naming convention**.

If a variable name is written in **ALL CAPITAL LETTERS**, it is treated as a constant by convention.

Example:

```python
PI = 3.14159
```

Python **does not prevent** you from changing it, but other programmers understand that it **should not** be modified.

---

# 📝 3. Creating Constants

Example:

```python
PI = 3.14159
```

```python
MAX_USERS = 100
```

```python
GRAVITY = 9.8
```

```python
COLLEGE_NAME = "ABC College"
```

---

# 💻 4. Examples

## Example 1

```python
PI = 3.14159

print(PI)
```

Output:

```text
3.14159
```

---

## Example 2

```python
MAX_SPEED = 120

print(MAX_SPEED)
```

Output:

```text
120
```

---

## Example 3

```python
COUNTRY = "India"

print(COUNTRY)
```

Output:

```text
India
```

---

# ⚠️ 5. Can We Change a Constant?

Technically, **yes**.

Example:

```python
PI = 3.14159

PI = 22 / 7

print(PI)
```

Output:

```text
3.142857142857143
```

The program runs without any error.

This is because Python **trusts the programmer**.

Even though you *can* change it, you **shouldn't** if it represents a constant value.

---

# 📊 6. Variables vs Constants

| Variable | Constant |
|----------|----------|
| Value can change | Intended to remain unchanged |
| Usually written in `snake_case` | Usually written in `UPPER_CASE` |
| Example: `age` | Example: `PI` |

Example:

```python
age = 20
```

Variable:

```python
age = 21
```

The value changes.

---

Constant:

```python
PI = 3.14159
```

The value is intended to remain the same throughout the program.

---

# 🌍 7. Real-World Examples

Temperature conversion:

```python
FREEZING_POINT = 0
BOILING_POINT = 100
```

---

Mathematics:

```python
PI = 3.14159
```

---

School:

```python
MAX_MARKS = 100
```

---

Application settings:

```python
APP_NAME = "Python Master Course"
VERSION = "1.0"
```

---

# 🧠 8. Naming Convention

According to **PEP 8**, constants should be written in **UPPER_CASE**.

Good:

```python
MAX_SIZE = 500
```

```python
DATABASE_NAME = "school_db"
```

Bad:

```python
max_size = 500
```

```python
databaseName = "school_db"
```

---

# ⚠️ 9. Common Mistakes

## ❌ Using lowercase for constants

```python
pi = 3.14159
```

Not recommended if you intend it to be a constant.

---

## ❌ Changing constant values unnecessarily

```python
MAX_USERS = 100

MAX_USERS = 200
```

If the value is meant to stay fixed, avoid changing it.

---

## ❌ Using unclear names

```python
x = 3.14159
```

Better:

```python
PI = 3.14159
```

---

# 💡 10. Best Practices

✅ Write constants in **UPPER_CASE**.

✅ Give constants meaningful names.

✅ Avoid changing constants after assigning them.

✅ Use constants for values that remain the same throughout the program.

---

# 🚀 11. Pro Tips

Instead of writing:

```python
radius = 5

area = 3.14159 * radius * radius
```

Use:

```python
PI = 3.14159

radius = 5

area = PI * radius * radius
```

This makes your code easier to read and maintain.

---

# 💻 12. Practice Programs

## Example 1

```python
PI = 3.14159

print(PI)
```

---

## Example 2

```python
MAX_MARKS = 100

print(MAX_MARKS)
```

---

## Example 3

```python
COUNTRY = "India"

print(COUNTRY)
```

---

## Example 4

```python
APP_NAME = "Python Master Course"

print(APP_NAME)
```

---

## Example 5

```python
GRAVITY = 9.8

print(GRAVITY)
```

---

# 🏋️ Practice Questions

## Easy

Create constants for:

- Your country
- Your college
- Maximum marks

Print all of them.

---

## Medium

Create constants:

```python
PI
```

```python
GRAVITY
```

```python
MAX_SPEED
```

Print each value.

---

## Hard

Write a program that calculates the area of a circle using:

```python
PI = 3.14159
```

and a variable named `radius`.

Formula:

```text
Area = PI × radius × radius
```

---

# 📝 Assignment

Complete the following:

- [x] Create five constants.
- [x] Print each constant.
- [x] Write a short note explaining why constants are useful.
- [x] Explain the difference between variables and constants.
- [x] Rewrite a program by replacing repeated fixed values with constants.

---

# 🧠 Quick Revision

- A constant is a value intended not to change.
- Python does not enforce constants.
- Use **UPPER_CASE** for constant names.
- Constants improve readability and maintainability.

---

# 📚 Summary

In this lesson, you learned:

- What a constant is.
- Why constants are useful.
- Python's approach to constants.
- Constant naming conventions.
- Variables vs constants.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what a constant is.
- [x] I know that Python does not enforce constants.
- [x] I use `UPPER_CASE` for constant names.
- [x] I know the difference between variables and constants.
- [x] I completed all practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 14: Input and Output**

---

## ⭐ Quote of the Day

> **"A well-named constant explains your program without needing extra comments."** 🐍