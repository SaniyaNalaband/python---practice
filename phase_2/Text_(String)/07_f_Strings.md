# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Text (`str`) - Part 8:** f-Strings (Formatted String Literals)

**Difficulty:** ⭐ Beginner → ⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what an f-string is.
- [ ] Insert variables into strings.
- [ ] Evaluate expressions inside `{}`.
- [ ] Format numbers.
- [ ] Align text.
- [ ] Use f-strings like a professional.

---

# 📖 1. What is an f-String?

An **f-string** is a string prefixed with the letter `f` or `F`.

It allows you to insert **variables and expressions directly inside curly braces `{}`**.

Syntax:

```python
f"Text {variable}"
```

Example:

```python
name = "Saniya"

print(f"My name is {name}")
```

Output:

```text
My name is Saniya
```

---

# 🌍 2. Why Use f-Strings?

Without f-strings:

```python
name = "Python"

print("Language: " + name)
```

Using f-strings:

```python
name = "Python"

print(f"Language: {name}")
```

The f-string version is cleaner and easier to read.

---

# 💻 3. Multiple Variables

```python
name = "Saniya"
age = 20

print(f"Name: {name}, Age: {age}")
```

Output:

```text
Name: Saniya, Age: 20
```

---

# ➕ 4. Expressions Inside `{}`

You can perform calculations directly.

```python
a = 10
b = 5

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 15
```

---

```python
print(f"Product = {a * b}")
```

Output:

```text
Product = 50
```

---

# 📏 5. Formatting Floats

```python
pi = 3.1415926535

print(f"{pi:.2f}")
```

Output:

```text
3.14
```

---

```python
print(f"{pi:.4f}")
```

Output:

```text
3.1416
```

---

# 🔠 6. Text Alignment

### Left Align

```python
name = "Python"

print(f"|{name:<10}|")
```

Output:

```text
|Python    |
```

---

### Right Align

```python
print(f"|{name:>10}|")
```

Output:

```text
|    Python|
```

---

### Center Align

```python
print(f"|{name:^10}|")
```

Output:

```text
|  Python  |
```

---

# 🔢 7. Formatting Integers

```python
number = 42

print(f"{number:5}")
```

Output:

```text
   42
```

---

Add leading zeros:

```python
print(f"{number:05}")
```

Output:

```text
00042
```

---

# 💰 8. Real-World Examples

### Student Details

```python
name = "Saniya"
course = "AI ML"
cgpa = 8.92

print(f"Student: {name}")
print(f"Course : {course}")
print(f"CGPA   : {cgpa:.2f}")
```

---

### Shopping Bill

```python
product = "Laptop"
price = 58999.5

print(f"{product} costs ₹{price:.2f}")
```

Output:

```text
Laptop costs ₹58999.50
```

---

# 🚀 9. Calling Functions

You can call functions inside `{}`.

```python
name = "python"

print(f"{name.upper()}")
```

Output:

```text
PYTHON
```

---

```python
print(f"Length = {len(name)}")
```

Output:

```text
Length = 6
```

---

# 🔍 10. Debugging Feature (Python 3.8+)

Instead of:

```python
x = 10

print(x)
```

You can write:

```python
x = 10

print(f"{x=}")
```

Output:

```text
x=10
```

This is useful for debugging.

---

# ⚠️ 11. Common Mistakes

## ❌ Forgetting the `f`

Wrong:

```python
name = "Python"

print("Hello {name}")
```

Output:

```text
Hello {name}
```

Correct:

```python
print(f"Hello {name}")
```

---

## ❌ Forgetting Curly Braces

Wrong:

```python
print(f"Hello name")
```

Correct:

```python
print(f"Hello {name}")
```

---

# 💡 12. Best Practices

- Prefer f-strings in new Python code.
- Keep expressions inside `{}` simple.
- Use formatting specifiers like `.2f` for floats.
- Use meaningful variable names.

---

# 🧠 Memory Trick

```
f

↓

String

↓

{}

↓

Variable / Expression
```

Example:

```python
f"My age is {age}"
```

---

# ❓ Interview Questions

- [ ] What is an f-string?
- [ ] Why are f-strings preferred?
- [ ] How do you format floats?
- [ ] Can you use expressions inside `{}`?
- [ ] What does `f"{x=}"` do?

---

# 🏋️ Practice Programs

## Easy

```python
name = "Saniya"

print(f"Hello, {name}")
```

---

```python
age = 20

print(f"Age: {age}")
```

---

## Medium

```python
a = 15
b = 5

print(f"Sum = {a + b}")
print(f"Division = {a / b:.2f}")
```

---

```python
pi = 3.1415926535

print(f"PI = {pi:.3f}")
```

---

## Advanced

```python
name = "Saniya"
course = "AI ML"
cgpa = 8.9234

print(f"""
Student Report
--------------
Name   : {name}
Course : {course}
CGPA   : {cgpa:.2f}
""")
```

---

# 🎯 Challenge

Create variables:

```python
name = "Your Name"
age = 20
height = 165.5
weight = 50
```

Using **only f-strings**, print:

- Name
- Age
- Height (2 decimal places)
- Weight
- BMI (calculate inside `{}`)

---

# 📝 Assignment

Complete the following:

- [x] Print your name using an f-string.
- [x] Print two variables in one sentence.
- [x] Print the result of a calculation inside `{}`.
- [x] Format a float to two decimal places.
- [x] Print a value using the debugging syntax (`{variable=}`).

---

# 📚 Summary

You learned:

- What an f-string is.
- Variable interpolation.
- Expressions inside `{}`.
- Float formatting.
- Text alignment.
- Debugging syntax.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I understand f-strings.
- [x] I can insert variables into strings.
- [x] I can evaluate expressions.
- [x] I can format floats.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 9: String Methods – Part 1**