# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 21:** Type Casting (Explicit Type Conversion)

**Difficulty:** ⭐⭐ Beginner to Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what type casting is.
- [ ] Learn why type casting is needed.
- [ ] Convert between different data types.
- [ ] Use Python's built-in casting functions.
- [ ] Avoid common type casting mistakes.
- [ ] Understand data loss during casting.

---

# 📖 1. What is Type Casting?

**Type Casting** is the process of **manually converting one data type into another**.

Unlike **Type Conversion**, Python **does not** decide automatically.

**You tell Python** what type you want.

Example:

```python
age = "20"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
20
<class 'int'>
```

---

# 🤔 2. Why Do We Need Type Casting?

Remember from Topic 16:

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters:

```
20
```

Python stores it as:

```text
<class 'str'>
```

To perform calculations, we need to convert it.

Example:

```python
age = int(input("Enter your age: "))

print(age + 5)
```

If the user enters:

```
20
```

Output:

```
25
```

---

# 📚 3. Common Type Casting Functions

| Function | Converts To |
|----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |
| `complex()` | Complex Number |

---

# 🔹 4. `int()` Function

Converts a value to an integer.

Example:

```python
print(int("100"))
```

Output:

```
100
```

---

```python
print(int(5.9))
```

Output:

```
5
```

Notice that the decimal part is removed, **not rounded**.

---

# 🔹 5. `float()` Function

Converts a value to a float.

Example:

```python
print(float(10))
```

Output:

```
10.0
```

---

```python
print(float("15.5"))
```

Output:

```
15.5
```

---

# 🔹 6. `str()` Function

Converts a value to a string.

Example:

```python
print(str(100))
```

Output:

```
100
```

Type:

```python
print(type(str(100)))
```

Output:

```
<class 'str'>
```

---

# 🔹 7. `bool()` Function

Converts a value to Boolean.

Examples:

```python
print(bool(1))
```

Output:

```
True
```

---

```python
print(bool(0))
```

Output:

```
False
```

---

```python
print(bool(""))
```

Output:

```
False
```

---

```python
print(bool("Python"))
```

Output:

```
True
```

---

# 🔹 8. `complex()` Function

Converts a number into a complex number.

Example:

```python
print(complex(10))
```

Output:

```
(10+0j)
```

---

```python
print(complex(5.5))
```

Output:

```
(5.5+0j)
```

---

# 📊 9. Conversion Table

| From | To | Example |
|------|----|---------|
| String | Integer | `int("10")` |
| Integer | Float | `float(10)` |
| Integer | String | `str(10)` |
| Float | Integer | `int(5.8)` |
| Integer | Boolean | `bool(1)` |

---

# 🌍 10. Real-World Example

Without casting:

```python
age = input("Enter age: ")

print(age + "5")
```

If user enters:

```
20
```

Output:

```
205
```

---

With casting:

```python
age = int(input("Enter age: "))

print(age + 5)
```

Output:

```
25
```

---

# ⚠️ 11. Common Mistakes

## ❌ Invalid Integer

```python
int("Hello")
```

Output:

```
ValueError
```

---

## ❌ Invalid Float

```python
float("Python")
```

Output:

```
ValueError
```

---

## ❌ Forgetting to Cast Input

```python
age = input("Enter age: ")

print(age + 5)
```

Output:

```
TypeError
```

Correct:

```python
age = int(input("Enter age: "))

print(age + 5)
```

---

# 💡 12. Best Practices

✅ Cast input values when performing calculations.

✅ Check the data type using `type()` if you're unsure.

✅ Use meaningful variable names.

---

# 🚀 13. Pro Tips

You can cast directly while taking input.

Instead of:

```python
age = input("Enter age: ")
age = int(age)
```

Write:

```python
age = int(input("Enter age: "))
```

Cleaner and more efficient.

---

# 🧠 Memory Trick

Remember:

```
Type Conversion

↓

Python decides

----------------------

Type Casting

↓

You decide
```

---

# ❓ Interview Questions

- [ ] What is type casting?
- [ ] What is the difference between type conversion and type casting?
- [ ] Name five casting functions.
- [ ] What happens when `int(5.9)` is executed?
- [ ] Why do we use `int(input())`?

---

# 🏋️ Practice Programs

## Easy

```python
print(int("100"))
```

---

```python
print(float(25))
```

---

```python
print(str(500))
```

---

## Medium

```python
age = int(input("Enter age: "))

print(age + 10)
```

---

```python
price = float(input("Enter price: "))

print(price)
```

---

## Advanced

```python
number = input("Enter a number: ")

print("Integer:", int(number))
print("Float:", float(number))
print("String:", str(number))
print("Boolean:", bool(number))
print("Complex:", complex(int(number)))
```

---

# 📝 Assignment

Complete the following:

- [x] Convert a string into an integer.
- [x] Convert an integer into a float.
- [x] Convert a float into an integer.
- [x] Convert an integer into a string.
- [x] Write a program that asks the user for two numbers and prints their sum.

---

# 📚 Summary

In this lesson, you learned:

- What type casting is.
- Why it is important.
- Built-in casting functions.
- Common mistakes.
- Best practices.
- Difference between type conversion and type casting.

---

# 🎯 Topic Completion Checklist

- [x] I know what type casting is.
- [x] I know the common casting functions.
- [x] I can convert between different data types.
- [x] I know why casting is important with `input()`.
- [x] I completed all practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 22: Dynamic Typing**

---

## ⭐ Quote of the Day

> **"Type casting gives you control over your data. Use it carefully and intentionally."** 🐍