# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 7:** Comments in Python

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what comments are.
- [ ] Know why comments are important.
- [ ] Write single-line comments.
- [ ] Write multi-line comments.
- [ ] Follow best practices for writing comments.
- [ ] Avoid common mistakes.
- [ ] Solve practice problems related to comments.

---

# 📖 1. Introduction

Comments are lines in a Python program that are **ignored by the Python Interpreter**.

They are written for **humans**, not for the computer.

Comments help explain code, making it easier to read, understand, and maintain.

Think of comments as **notes in a notebook**.

---

# 🤔 2. Why Do We Use Comments?

Imagine you write a Python program today.

After six months, you open it again.

Without comments, you might forget what each part of the code does.

Comments help you:

- Explain your code.
- Make programs easier to understand.
- Help teammates understand your code.
- Remember why a piece of code was written.
- Temporarily disable code during testing.

---

# 🧠 3. Types of Comments

Python mainly uses:

1. Single-line Comments
2. Multi-line Comments

---

# 📝 4. Single-line Comments

A single-line comment starts with the **hash (`#`)** symbol.

Everything after `#` on that line is ignored by Python.

### Syntax

```python
# This is a comment
```

### Example

```python
# Print a welcome message
print("Welcome to Python")
```

### Output

```text
Welcome to Python
```

Notice that the comment is **not displayed**.

---

# 📚 5. Multi-line Comments

Python does not have a special syntax for multi-line comments.

The most common ways are:

### Method 1 (Recommended)

```python
# This is line 1
# This is line 2
# This is line 3
```

### Method 2 (Triple Quotes)

```python
"""
This is a multi-line text.

Many developers use triple quotes
to write long descriptions.
"""
```

Although triple quotes create a string object, they are often used as documentation (called **docstrings**) when placed at the beginning of modules, classes, or functions.

---

# 💻 6. Examples

## Example 1

```python
# My first comment
print("Hello")
```

Output

```text
Hello
```

---

## Example 2

```python
print("Python")  # Prints Python
```

Output

```text
Python
```

This is called an **inline comment**.

---

## Example 3

```python
# Student Details
print("Name : Saniya")
print("Course : BCA")
```

Output

```text
Name : Saniya
Course : BCA
```

---

## Example 4

```python
"""
Simple Calculator
Version 1.0
Created for Learning
"""

print("Calculator Started")
```

Output

```text
Calculator Started
```

---

# 🌍 7. Real-World Example

Imagine you're writing a banking application.

```python
# Calculate account balance
balance = 10000

# Deduct withdrawal amount
balance = balance - 2500

print(balance)
```

Without comments, another programmer may not immediately understand the purpose of each line.

---

# ⚠️ 8. Common Mistakes

## ❌ Writing unnecessary comments

Bad:

```python
# Print Hello
print("Hello")
```

The code is already obvious.

---

## ❌ Writing outdated comments

```python
# Adds two numbers
print(100)
```

The comment no longer matches the code.

Always keep comments updated.

---

## ❌ Commenting every line

Too many comments make code harder to read.

Comment only when necessary.

---

# 💡 9. Best Practices

✅ Write comments that explain **why**, not just **what**.

✅ Keep comments short and meaningful.

✅ Update comments when code changes.

✅ Remove unnecessary comments.

---

# 🚀 10. Pro Tips

Professional developers use comments to:

- Explain complex logic.
- Mark TODO items.

Example:

```python
# TODO: Add login validation
```

- Leave notes for teammates.

Example:

```python
# FIXME: Handle division by zero
```

---

# 📌 11. Quick Revision

| Symbol | Purpose |
|---------|---------|
| `#` | Single-line comment |
| `""" """` | Multi-line documentation (Docstring) |

---

# ❓ Interview Questions

- [ ] What is a comment?
- [ ] Why are comments used?
- [ ] Which symbol is used for single-line comments?
- [ ] Does Python execute comments?
- [ ] What is an inline comment?
- [ ] What is a docstring?
- [ ] Why should comments be updated?

---

# 🏋️ Practice Programs

## Easy

```python
# Print a greeting
print("Hello")
```

---

```python
# Print your name
print("Saniya")
```

---

## Medium

```python
# Student Information

print("Name : Saniya")
print("Age : 20")
print("Course : BCA")
```

---

## Hard

Write a program that contains:

- Program title
- Author name
- Today's date
- Purpose of the program

using comments before printing any output.

---

# 📝 Assignment

Complete the following:

- [x] Write three single-line comments.
- [x] Write one inline comment.
- [x] Write a multi-line description using triple quotes.
- [x] Explain the difference between comments and code in your own words.

---

# 📚 Summary

In this lesson you learned:

- What comments are.
- Why comments are important.
- Single-line comments.
- Inline comments.
- Multi-line comments.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what comments are.
- [x] I know why comments are used.
- [x] I can write single-line comments.
- [x] I can write inline comments.
- [x] I understand triple-quoted docstrings.
- [x] I completed all practice programs.
- [x] I completed the assignment.
- [x] I answered the interview questions.

---

# 📚 Next Topic

➡️ **Topic 8: Indentation**

---

## ⭐ Quote of the Day

> **"Good code tells you how. Great comments tell you why."**