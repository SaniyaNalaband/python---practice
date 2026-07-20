# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Text (`str`) - Part 12:** Cleaning & Alignment Methods

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Remove unwanted spaces using `strip()`.
- [ ] Remove characters from the left using `lstrip()`.
- [ ] Remove characters from the right using `rstrip()`.
- [ ] Center text using `center()`.
- [ ] Align text using `ljust()` and `rjust()`.
- [ ] Pad numbers using `zfill()`.

---

# 📖 1. `strip()`

Removes leading and trailing whitespace.

```python
text = "   Python   "

print(text.strip())
```

Output:

```text
Python
```

Original string remains unchanged.

---

### Remove Specific Characters

```python
text = "***Python***"

print(text.strip("*"))
```

Output:

```text
Python
```

---

# 📖 2. `lstrip()`

Removes characters from the **left side** only.

```python
text = "   Python"

print(text.lstrip())
```

Output:

```text
Python
```

---

```python
text = "###Python"

print(text.lstrip("#"))
```

Output:

```text
Python
```

---

# 📖 3. `rstrip()`

Removes characters from the **right side** only.

```python
text = "Python   "

print(text.rstrip())
```

Output:

```text
Python
```

---

```python
text = "Python!!!"

print(text.rstrip("!"))
```

Output:

```text
Python
```

---

# 📖 4. `center()`

Centers text within a specified width.

Syntax:

```python
string.center(width, fillchar)
```

Example:

```python
text = "Python"

print(text.center(12))
```

Output:

```text
   Python   
```

---

Using a fill character:

```python
print(text.center(12, "*"))
```

Output:

```text
***Python***
```

---

# 📖 5. `ljust()`

Left-aligns the string.

```python
text = "Python"

print(text.ljust(12))
```

Output:

```text
Python      
```

---

Using a fill character:

```python
print(text.ljust(12, "-"))
```

Output:

```text
Python------
```

---

# 📖 6. `rjust()`

Right-aligns the string.

```python
text = "Python"

print(text.rjust(12))
```

Output:

```text
      Python
```

---

Using a fill character:

```python
print(text.rjust(12, "-"))
```

Output:

```text
------Python
```

---

# 📖 7. `zfill()`

Pads a numeric string with leading zeros.

```python
number = "25"

print(number.zfill(5))
```

Output:

```text
00025
```

---

```python
print("123".zfill(6))
```

Output:

```text
000123
```

---

Negative numbers are handled correctly.

```python
print("-25".zfill(5))
```

Output:

```text
-0025
```

---

# 🌍 Real-World Examples

### Cleaning User Input

```python
name = "   Saniya   "

print(name.strip())
```

Output:

```text
Saniya
```

---

### Student ID

```python
student_id = "25"

print(student_id.zfill(6))
```

Output:

```text
000025
```

---

### Printing a Report

```python
title = "MARKS"

print(title.center(30, "="))
```

Output:

```text
============MARKS=============
```

---

# ⚠️ Common Mistakes

## ❌ `strip()` Removes Characters, Not Words

```python
text = "Python"

print(text.strip("Py"))
```

Output:

```text
thon
```

It removes the characters `P` and `y` from the ends—not the word `"Py"`.

---

## ❌ Forgetting Strings Are Immutable

```python
text = "  Python  "

text.strip()

print(text)
```

Output:

```text
  Python  
```

Correct:

```python
text = text.strip()

print(text)
```

---

# 💡 Best Practices

- Use `strip()` before processing user input.
- Use `center()`, `ljust()`, and `rjust()` to create neat console reports.
- Use `zfill()` for IDs, invoice numbers, and serial numbers.

---

# 🚀 Pro Tips

Format a table:

```python
print("Name".ljust(15), "Marks".rjust(5))
print("Saniya".ljust(15), "95".rjust(5))
print("Rahul".ljust(15), "88".rjust(5))
```

Output:

```text
Name            Marks
Saniya             95
Rahul              88
```

---

# 🧠 Memory Trick

```
strip()

↓

Both sides

----------------

lstrip()

↓

Left side

----------------

rstrip()

↓

Right side

----------------

center()

↓

Middle

----------------

ljust()

↓

Left Align

----------------

rjust()

↓

Right Align

----------------

zfill()

↓

Leading Zeros
```

---

# ❓ Interview Questions

- [ ] What is the difference between `strip()`, `lstrip()`, and `rstrip()`?
- [ ] What does `zfill()` do?
- [ ] Can `strip()` remove specific characters?
- [ ] Which method centers text?
- [ ] Which methods are useful for formatting reports?

---

# 🏋️ Practice Programs

## Easy

```python
text = "   Python   "

print(text.strip())
```

---

```python
print("***Hello***".strip("*"))
```

---

## Medium

```python
text = "Python"

print(text.center(15, "-"))
print(text.ljust(15, "."))
print(text.rjust(15, "."))
```

---

```python
number = "42"

print(number.zfill(6))
```

---

## Advanced

```python
name = "   Saniya   "
student_id = "15"

print("Original :", repr(name))
print("Cleaned  :", repr(name.strip()))
print("ID       :", student_id.zfill(5))

print("\nReport")
print("=" * 25)
print("Name".ljust(15), "Marks".rjust(5))
print("Saniya".ljust(15), "95".rjust(5))
print("Rahul".ljust(15), "88".rjust(5))
```

---

# 🎯 Challenge

Create:

```python
name = "   Your Name   "
roll = "7"
```

Print:

- Name after removing spaces.
- Roll number using `zfill(4)`.
- Name centered in a width of 20 using `"*"`.
- Name left-aligned.
- Name right-aligned.

---

# 📝 Assignment

- [x] Remove spaces using `strip()`.
- [x] Remove `#` from the left using `lstrip()`.
- [x] Remove `!` from the right using `rstrip()`.
- [x] Center your name in 20 spaces.
- [x] Left-align and right-align your city.
- [x] Pad your roll number with zeros.

---

# 📚 Summary

You learned:

- `strip()`
- `lstrip()`
- `rstrip()`
- `center()`
- `ljust()`
- `rjust()`
- `zfill()`

These methods are commonly used for cleaning text and creating well-formatted output.

---

# 🎯 Topic Completion Checklist

- [x] I understand `strip()`.
- [x] I understand `lstrip()` and `rstrip()`.
- [x] I can use `center()`, `ljust()`, and `rjust()`.
- [x] I can use `zfill()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 5: String Checking Methods (`is...()` Methods)**