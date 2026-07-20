# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Text (`str`) - Part 9:** String Methods - Case Conversion

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

- [ ] Convert strings to uppercase.
- [ ] Convert strings to lowercase.
- [ ] Capitalize the first letter.
- [ ] Convert text to title case.
- [ ] Swap uppercase and lowercase letters.
- [ ] Understand `casefold()`.

---

# 📖 1. `upper()`

Converts all letters to uppercase.

```python
text = "python programming"

print(text.upper())
```

Output:

```text
PYTHON PROGRAMMING
```

Original string:

```python
print(text)
```

Output:

```text
python programming
```

**Note:** Strings are immutable, so `upper()` returns a **new string**.

---

# 📖 2. `lower()`

Converts all letters to lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output:

```text
python
```

---

# 📖 3. `capitalize()`

Makes only the first character uppercase.

```python
text = "python programming"

print(text.capitalize())
```

Output:

```text
Python programming
```

---

# 📖 4. `title()`

Capitalizes the first letter of every word.

```python
text = "python programming language"

print(text.title())
```

Output:

```text
Python Programming Language
```

---

# 📖 5. `swapcase()`

Reverses the case of each letter.

```python
text = "PyThOn"

print(text.swapcase())
```

Output:

```text
pYtHoN
```

---

# 📖 6. `casefold()`

Converts to lowercase more aggressively than `lower()`.

```python
text = "PYTHON"

print(text.casefold())
```

Output:

```text
python
```

For English text, `lower()` and `casefold()` usually produce the same result. `casefold()` is mainly useful for robust, case-insensitive comparisons involving international text.

---

# 🌍 Real-World Example

```python
user_input = "PyThOn"

if user_input.lower() == "python":
    print("Matched!")
```

Output:

```text
Matched!
```

---

# ⚠️ Common Mistake

```python
text = "python"

text.upper()

print(text)
```

Output:

```text
python
```

Why?

Because `upper()` **does not change the original string**.

Correct:

```python
text = text.upper()

print(text)
```

Output:

```text
PYTHON
```

---

# 🏋️ Practice Programs

## Easy

```python
text = "python"

print(text.upper())
```

---

```python
text = "PYTHON"

print(text.lower())
```

---

## Medium

```python
text = "python programming"

print(text.capitalize())
print(text.title())
```

---

## Advanced

```python
text = "PyThOn PrOgRaMmInG"

print("Original   :", text)
print("Upper      :", text.upper())
print("Lower      :", text.lower())
print("Capitalize :", text.capitalize())
print("Title      :", text.title())
print("Swapcase   :", text.swapcase())
print("Casefold   :", text.casefold())
```

---

# 📊 Quick Reference

| Method | Example | Result |
|---------|---------|--------|
| `upper()` | `"abc".upper()` | `"ABC"` |
| `lower()` | `"ABC".lower()` | `"abc"` |
| `capitalize()` | `"hello world".capitalize()` | `"Hello world"` |
| `title()` | `"hello world".title()` | `"Hello World"` |
| `swapcase()` | `"PyThOn".swapcase()` | `"pYtHoN"` |
| `casefold()` | `"ABC".casefold()` | `"abc"` |

---

# 📝 Assignment

- [x] Convert your name to uppercase.
- [x] Convert your city to lowercase.
- [x] Use `capitalize()` on a sentence.
- [x] Use `title()` on your full name.
- [x] Use `swapcase()` on `"PyThOn"`.
- [x] Compare `lower()` and `casefold()`.

---

# 🎯 Topic Completion Checklist

- [x] I understand all six case conversion methods.
- [x] I know that string methods return new strings.
- [x] I completed the practice programs.
- [] I completed the assignment.

---

# 📚 Next Lesson

➡️ **String Methods – Part 2: Searching & Counting**
