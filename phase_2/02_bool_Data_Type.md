# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Topic 5:** Boolean (`bool`)

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a Boolean is.
- [ ] Learn the two Boolean values.
- [ ] Create Boolean variables.
- [ ] Understand truthy and falsy values.
- [ ] Convert values to Boolean.
- [ ] Perform Boolean operations.
- [ ] Use Boolean values in real-world programs.
- [ ] Avoid common mistakes.

---

# 📖 1. What is a Boolean?

A **Boolean** is a data type that can store **only one of two values**:

- `True`
- `False`

There are no other Boolean values.

Example:

```python
is_logged_in = True

has_permission = False
```

---

# 🌍 2. Real-World Examples

### Login System

```python
is_logged_in = True
```

---

### Online Exam

```python
exam_completed = False
```

---

### ATM Machine

```python
pin_correct = True
```

---

### Website

```python
is_admin = False
```

---

# 💻 3. Creating Boolean Variables

```python
x = True
```

```python
y = False
```

Check the type:

```python
print(type(x))
print(type(y))
```

Output:

```text
<class 'bool'>
<class 'bool'>
```

---

# ⚠️ 4. `True` and `False` Are Keywords

Correct:

```python
status = True
```

Wrong:

```python
status = true
```

Output:

```text
NameError
```

Python is **case-sensitive**.

Always write:

```python
True
False
```

---

# 🔄 5. Converting Values to Boolean

Use the `bool()` function.

```python
print(bool(1))
```

Output:

```text
True
```

---

```python
print(bool(0))
```

Output:

```text
False
```

---

```python
print(bool("Python"))
```

Output:

```text
True
```

---

```python
print(bool(""))
```

Output:

```text
False
```

---

```python
print(bool([]))
```

Output:

```text
False
```

---

```python
print(bool([1, 2]))
```

Output:

```text
True
```

---

# 📚 6. Truthy and Falsy Values

Python treats many values as either **truthy** or **falsy**.

### Falsy Values

```python
False
0
0.0
0j
None
''
""
[]
()
{}
set()
```

Each of these becomes:

```python
False
```

---

### Truthy Values

Everything else is truthy.

Examples:

```python
1
-5
3.14
"Hello"
[10]
(5,)
{1}
True
```

These become:

```python
True
```

---

# ➕ 7. Boolean Operations

```python
print(True and False)
```

Output:

```text
False
```

---

```python
print(True or False)
```

Output:

```text
True
```

---

```python
print(not True)
```

Output:

```text
False
```

We'll study these operators in detail in the Operators phase.

---

# 🧠 8. Booleans Behave Like Integers

In Python:

```python
True == 1
False == 0
```

Example:

```python
print(True + True)
```

Output:

```text
2
```

---

```python
print(False + True)
```

Output:

```text
1
```

This works because:

```text
True  → 1
False → 0
```

---

# 🌍 9. Real-World Decision Example

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

The comparison itself returns a Boolean.

---

# 💡 10. Best Practices

✅ Use meaningful names.

```python
is_student = True
```

Instead of:

```python
x = True
```

---

Good Boolean variable names often start with:

- `is_`
- `has_`
- `can_`
- `should_`

Examples:

```python
is_admin
has_license
can_vote
should_save
```

---

# ⚠️ 11. Common Mistakes

## ❌ Using Quotes

```python
x = "True"
```

This is a string.

Correct:

```python
x = True
```

---

## ❌ Using Lowercase

```python
x = true
```

This causes a `NameError`.

Correct:

```python
x = True
```

---

## ❌ Comparing to `True` Unnecessarily

Instead of:

```python
if is_logged_in == True:
```

Write:

```python
if is_logged_in:
```

It's shorter and more Pythonic.

---

# 🚀 12. Pro Tips

Use `bool()` to test any value.

```python
values = [0, 1, "", "Python", [], [5], None]

for value in values:
    print(value, "→", bool(value))
```

---

# 🧠 Memory Trick

```
Boolean

↓

Only Two Values

↓

True

False
```

Think of a light switch:

```
ON  → True
OFF → False
```

---

# ❓ Interview Questions

- [ ] What is a Boolean?
- [ ] How many Boolean values exist?
- [ ] What does `bool()` do?
- [ ] What are truthy and falsy values?
- [ ] Why does `True + True` equal `2`?

---

# 🏋️ Practice Programs

## Easy

```python
is_student = True

print(is_student)
print(type(is_student))
```

---

```python
print(bool(0))
print(bool(1))
```

---

## Medium

```python
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))
```

---

```python
age = 20

print(age >= 18)
```

---

## Advanced

```python
values = [
    False,
    True,
    0,
    1,
    "",
    "Hello",
    [],
    [10],
    {},
    {"name": "Saniya"},
    None
]

for value in values:
    print(f"{value!r:20} -> {bool(value)}")
```

---

# 🎯 Challenge

Create variables:

```python
is_student = True
age = 19
has_id = False
```

Print:

- Type of each variable
- Boolean conversion of each
- Whether `age >= 18`

---

# 📝 Assignment

Complete the following:

- [x] Create five Boolean variables.
- [x] Print their values and types.
- [x] Convert numbers, strings, lists, and dictionaries using `bool()`.
- [x] Write down five truthy values.
- [x] Write down five falsy values.
- [x] Explain truthy and falsy values in your own words.

---

# 📚 Summary

In this lesson, you learned:

- What a Boolean is.
- `True` and `False`.
- The `bool()` function.
- Truthy and falsy values.
- Boolean operations.
- Real-world uses.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what a Boolean is.
- [x] I know the two Boolean values.
- [x] I understand truthy and falsy values.
- [x] I can use `bool()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Text (`str`)**

---

## ⭐ Quote of the Day

> **"Every decision a Python program makes begins with a Boolean value."** 🐍