# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 24:** `type()` Function

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `type()` function is.
- [ ] Learn the syntax of `type()`.
- [ ] Check the data type of variables and values.
- [ ] Understand why `type()` is useful.
- [ ] Avoid common beginner mistakes.

---

# 📖 1. What is the `type()` Function?

The `type()` function is a built-in Python function that tells you **the data type of an object**.

Syntax:

```python
type(object)
```

Example:

```python
x = 10

print(type(x))
```

Output:

```text
<class 'int'>
```

---

# 🤔 2. Why Do We Use `type()`?

When writing programs, you may not always know what type of data a variable contains.

`type()` helps you verify it.

Example:

```python
name = "Saniya"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

# 📚 3. Checking Different Data Types

## Integer

```python
print(type(100))
```

Output:

```text
<class 'int'>
```

---

## Float

```python
print(type(99.5))
```

Output:

```text
<class 'float'>
```

---

## String

```python
print(type("Python"))
```

Output:

```text
<class 'str'>
```

---

## Boolean

```python
print(type(True))
```

Output:

```text
<class 'bool'>
```

---

## Complex Number

```python
print(type(5 + 3j))
```

Output:

```text
<class 'complex'>
```

---

# 💻 4. Checking Variables

```python
age = 20
name = "Saniya"
marks = 95.5

print(type(age))
print(type(name))
print(type(marks))
```

Output:

```text
<class 'int'>
<class 'str'>
<class 'float'>
```

---

# 💻 5. Checking User Input

Remember:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```
20
```

Output:

```text
<class 'str'>
```

Because `input()` always returns a string.

---

Now convert it:

```python
age = int(input("Enter your age: "))

print(type(age))
```

Output:

```text
<class 'int'>
```

---

# 💻 6. Using `type()` After Type Casting

```python
number = "50"

print(type(number))

number = int(number)

print(type(number))
```

Output:

```text
<class 'str'>
<class 'int'>
```

---

# 🌍 7. Real-World Example

```python
price = 150
discount = 25.5
available = True
product = "Laptop"

print(type(price))
print(type(discount))
print(type(available))
print(type(product))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'str'>
```

---

# ⚠️ 8. Common Mistakes

## ❌ Confusing Value with Type

```python
print(type("100"))
```

Output:

```text
<class 'str'>
```

Even though it looks like a number, it's a string because it's inside quotes.

---

## ❌ Assuming `input()` Returns an Integer

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

Always convert it if you need a number:

```python
age = int(input("Enter age: "))
```

---

# 💡 9. Best Practices

✅ Use `type()` while learning Python.

✅ Use it to debug unexpected errors.

✅ Check variable types before performing operations.

---

# 🚀 10. Pro Tips

You can use `type()` with expressions too.

```python
print(type(10 + 5.5))
```

Output:

```text
<class 'float'>
```

---

```python
print(type(True + 5))
```

Output:

```text
<class 'int'>
```

---

# 🧠 Memory Trick

Remember:

```
type()

↓

Returns the data type
```

Think:

> **"Want to know what something is? Use `type()`."**

---

# ❓ Interview Questions

- [ ] What does the `type()` function do?
- [ ] What is the syntax of `type()`?
- [ ] What is the output of `type("100")`?
- [ ] Why does `input()` return `str`?
- [ ] What is the difference between `type()` and `id()`?

---

# 🏋️ Practice Programs

## Easy

```python
print(type(100))
```

---

```python
print(type("Hello"))
```

---

```python
print(type(True))
```

---

## Medium

```python
x = 10
y = 5.5
z = "Python"

print(type(x))
print(type(y))
print(type(z))
```

---

```python
age = int(input("Enter your age: "))

print(type(age))
```

---

## Advanced

```python
data = [
    10,
    5.5,
    "Python",
    True,
    3 + 4j
]

for item in data:
    print(item, "→", type(item))
```

---

## Challenge

Create variables with these values:

- Your name
- Your age
- Your height
- Whether you like Python (`True`/`False`)

Print each value along with its data type.

---

# 📝 Assignment

Complete the following:

- [ ] Check the type of an integer.
- [ ] Check the type of a float.
- [ ] Check the type of a string.
- [ ] Check the type of a Boolean.
- [ ] Check the type of a complex number.
- [ ] Take user input, convert it to an integer, and verify the type.

---

# 📚 Summary

In this lesson, you learned:

- What the `type()` function is.
- How to use `type()`.
- How to check the type of values and variables.
- How `type()` works with `input()` and type casting.
- Common mistakes and best practices.

---

# 🎯 Topic Completion Checklist

- [ ] I know what `type()` does.
- [ ] I can check the type of variables.
- [ ] I understand why `input()` returns a string.
- [ ] I know the difference between `type()` and `id()`.
- [ ] I completed all practice programs.
- [ ] I completed the assignment.

---

# 🔄 Comparison: `type()` vs `id()`

| Feature | `type()` | `id()` |
|---------|----------|---------|
| Returns | Data type | Object identity |
| Example Output | `<class 'int'>` | `140723456789120` (example) |
| Used For | Knowing what the object is | Identifying which object it is |
| Changes after reassignment? | Yes, if the new object has a different type | Usually yes, because the variable refers to a different object |

---

# 📚 Next Topic

➡️ **Topic 25: Memory Basics**

---

## ⭐ Quote of the Day

> **"`type()` tells you what an object is, while `id()` tells you which object it is."** 🐍