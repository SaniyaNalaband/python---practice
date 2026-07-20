# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Text (`str`) - Part 13:** String Checking Methods

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Validate strings using `is...()` methods.
- [ ] Distinguish between letters, digits, and alphanumeric text.
- [ ] Check letter case.
- [ ] Validate identifiers.
- [ ] Understand ASCII and printable characters.

---

# 📖 1. `isalpha()`

Returns `True` if **all characters are alphabetic letters** and the string is not empty.

```python
print("Python".isalpha())
```

Output:

```text
True
```

```python
print("Python123".isalpha())
```

Output:

```text
False
```

---

# 📖 2. `isdigit()`

Returns `True` if **all characters are digits (0–9)**.

```python
print("12345".isdigit())
```

Output:

```text
True
```

```python
print("12.5".isdigit())
```

Output:

```text
False
```

---

# 📖 3. `isalnum()`

Returns `True` if the string contains **only letters and digits**.

```python
print("Python123".isalnum())
```

Output:

```text
True
```

```python
print("Python 123".isalnum())
```

Output:

```text
False
```

> Spaces and special characters make it return `False`.

---

# 📖 4. `islower()`

Returns `True` if **all alphabetic characters are lowercase**.

```python
print("python".islower())
```

Output:

```text
True
```

```python
print("Python".islower())
```

Output:

```text
False
```

---

# 📖 5. `isupper()`

Returns `True` if **all alphabetic characters are uppercase**.

```python
print("PYTHON".isupper())
```

Output:

```text
True
```

```python
print("Python".isupper())
```

Output:

```text
False
```

---

# 📖 6. `istitle()`

Returns `True` if **every word starts with a capital letter**.

```python
print("Python Programming".istitle())
```

Output:

```text
True
```

```python
print("python Programming".istitle())
```

Output:

```text
False
```

---

# 📖 7. `isspace()`

Returns `True` if the string contains **only whitespace characters**.

```python
print("   ".isspace())
```

Output:

```text
True
```

```python
print(" Python ".isspace())
```

Output:

```text
False
```

---

# 📖 8. `isdecimal()`

Returns `True` if the string contains **decimal digits only**.

```python
print("123".isdecimal())
```

Output:

```text
True
```

```python
print("12.3".isdecimal())
```

Output:

```text
False
```

---

# 📖 9. `isnumeric()`

Returns `True` for **numeric characters**, including some Unicode numerals.

```python
print("123".isnumeric())
```

Output:

```text
True
```

```python
print("Ⅳ".isnumeric())
```

Output:

```text
True
```

> `Ⅳ` (Roman numeral four) is numeric, but it is **not** a decimal digit.

---

# 📖 10. `isidentifier()`

Checks whether the string is a **valid Python identifier**.

```python
print("student_name".isidentifier())
```

Output:

```text
True
```

```python
print("123name".isidentifier())
```

Output:

```text
False
```

---

# 📖 11. `isascii()`

Returns `True` if **all characters are ASCII**.

```python
print("Python".isascii())
```

Output:

```text
True
```

```python
print("Pythön".isascii())
```

Output:

```text
False
```

---

# 📖 12. `isprintable()`

Returns `True` if **all characters are printable**.

```python
print("Hello".isprintable())
```

Output:

```text
True
```

```python
print("Hello\nWorld".isprintable())
```

Output:

```text
False
```

The newline character (`\n`) is not printable.

---

# 🌍 Real-World Examples

### Validate Username

```python
username = "Saniya123"

print(username.isalnum())
```

Output:

```text
True
```

---

### Validate Age Input

```python
age = "20"

print(age.isdigit())
```

Output:

```text
True
```

---

### Validate Variable Name

```python
name = "student_name"

print(name.isidentifier())
```

Output:

```text
True
```

---

# ⚠️ Common Mistakes

## ❌ Empty Strings

```python
print("".isalpha())
```

Output:

```text
False
```

Most `is...()` methods return `False` for an empty string.

---

## ❌ Confusing `isdigit()`, `isdecimal()`, and `isnumeric()`

```python
text = "Ⅳ"

print(text.isdigit())
print(text.isdecimal())
print(text.isnumeric())
```

Output:

```text
False
False
True
```

---

# 💡 Best Practices

- Use `isdigit()` to validate integer input.
- Use `isidentifier()` before creating variable names dynamically.
- Use `isalnum()` for usernames.
- Use `islower()` and `isupper()` for case checks.

---

# 🚀 Pro Tips

Validate input before conversion:

```python
age = input("Enter your age: ")

if age.isdigit():
    print(int(age) + 1)
else:
    print("Please enter digits only.")
```

---

# 🧠 Memory Trick

```
isalpha()       → Letters only

isdigit()       → Digits only

isalnum()       → Letters + Digits

islower()       → Lowercase

isupper()       → Uppercase

istitle()       → Title Case

isspace()       → Spaces only

isdecimal()     → Decimal digits

isnumeric()     → Numeric characters

isidentifier()  → Valid variable name

isascii()       → ASCII only

isprintable()   → Printable characters
```

---

# ❓ Interview Questions

- [x] What is the difference between `isdigit()` and `isnumeric()`?
- [x] What does `isalnum()` check?
- [x] Why is `"123name".isidentifier()` `False`?
- [x] What does `isspace()` return?
- [x] Which method checks for printable characters?

---

# 🏋️ Practice Programs

## Easy

```python
print("Python".isalpha())
print("123".isdigit())
print("Python123".isalnum())
```

---

## Medium

```python
text = "Python"

print(text.islower())
print(text.isupper())
print(text.istitle())
```

---

## Advanced

```python
samples = [
    "Python",
    "python123",
    "123",
    "Hello World",
    "student_name",
    "Ⅳ"
]

for item in samples:
    print(f"\nValue: {item}")
    print("isalpha      :", item.isalpha())
    print("isdigit      :", item.isdigit())
    print("isalnum      :", item.isalnum())
    print("islower      :", item.islower())
    print("isupper      :", item.isupper())
    print("istitle      :", item.istitle())
    print("isidentifier :", item.isidentifier())
    print("isascii      :", item.isascii())
    print("isprintable  :", item.isprintable())
```

---

# 🎯 Challenge

Create variables:

```python
username = "User123"
password = "Python@123"
roll = "007"
variable = "_student"
```

Check:

- Is the username alphanumeric?
- Is the password alphabetic?
- Is the roll number numeric?
- Is the variable name a valid identifier?
- Is the password printable?

---

# 📝 Assignment

- [x] Check if your name is alphabetic.
- [x] Check if your age contains only digits.
- [x] Check if your username is alphanumeric.
- [x] Check if your full name is in title case.
- [x] Check if `"student_name"` is a valid identifier.
- [x] Compare `isdigit()`, `isdecimal()`, and `isnumeric()`.

---

# 📚 Summary

You learned:

- `isalpha()`
- `isdigit()`
- `isalnum()`
- `islower()`
- `isupper()`
- `istitle()`
- `isspace()`
- `isdecimal()`
- `isnumeric()`
- `isidentifier()`
- `isascii()`
- `isprintable()`

These methods are essential for validating and processing text in Python.

---

# 🎯 Topic Completion Checklist

- [x] I understand all `is...()` methods.
- [x] I know the difference between `isdigit()`, `isdecimal()`, and `isnumeric()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 2: Collections – List Data Type**