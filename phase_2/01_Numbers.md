# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Topic 1:** Numbers

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what Numbers are.
- [ ] Learn the three numeric data types.
- [ ] Identify integer, float, and complex values.
- [ ] Understand where numbers are used.
- [ ] Differentiate between numeric types.
- [ ] Prepare for learning `int`, `float`, and `complex` individually.

---

# 📖 1. What are Numbers?

Numbers are one of Python's built-in data types.

They represent **numeric values** that can be used for:

- Mathematical calculations
- Scientific computations
- Financial applications
- Machine Learning
- Data Science
- Games
- Engineering

Example:

```python
age = 20
price = 99.99
root = 4 + 5j
```

All three are numbers.

---

# 🤔 2. Why Do We Need Numbers?

Imagine creating an online shopping website.

You need numbers for:

- Product price
- Quantity
- Discount
- Tax
- Total bill

Example:

```python
price = 500
quantity = 3

total = price * quantity

print(total)
```

Output:

```
1500
```

Without numbers, programming would be impossible.

---

# 🔢 3. Types of Numbers in Python

Python provides three built-in numeric types.

```
Numbers
│
├── Integer (int)
├── Float (float)
└── Complex (complex)
```

---

## Integer (`int`)

Whole numbers.

Examples:

```python
10
0
-50
1000
```

---

## Float (`float`)

Numbers with decimal points.

Examples:

```python
5.5
10.0
-3.14
99.99
```

---

## Complex (`complex`)

Numbers containing an imaginary part.

Examples:

```python
2 + 3j
5j
10 - 4j
```

Used in advanced mathematics, electrical engineering, signal processing, and scientific computing.

---

# 💻 4. Checking Numeric Types

```python
print(type(100))
```

Output:

```
<class 'int'>
```

---

```python
print(type(99.99))
```

Output:

```
<class 'float'>
```

---

```python
print(type(2 + 3j))
```

Output:

```
<class 'complex'>
```

---

# 🌍 5. Real-World Examples

### Banking

```python
balance = 25000
```

Integer

---

### Online Shopping

```python
price = 1499.99
```

Float

---

### Engineering

```python
voltage = 12 + 5j
```

Complex

---

# 📊 6. Comparison

| Type | Example | Description |
|------|---------|-------------|
| `int` | `100` | Whole number |
| `float` | `99.99` | Decimal number |
| `complex` | `2+3j` | Complex number |

---

# ⚠️ 7. Common Mistakes

## ❌ Thinking All Numbers Are Integers

Wrong:

```python
10.0
```

is an integer.

Correct:

```
10.0
```

is a **float**.

---

## ❌ Using `i` Instead of `j`

Wrong:

```python
3 + 4i
```

Correct:

```python
3 + 4j
```

Python uses **`j`** for imaginary numbers.

---

# 💡 8. Best Practices

✅ Use `int` for counting.

✅ Use `float` for measurements and money.

✅ Use `complex` only when solving mathematical or scientific problems.

---

# 🚀 9. Pro Tips

Use `type()` to identify numeric types.

```python
num = 50

print(type(num))
```

Always verify the type if you're unsure.

---

# 🧠 Memory Trick

Remember:

```
Numbers

↓

Three Types

↓

int

float

complex
```

Think:

> **Whole → Decimal → Imaginary**

---

# ❓ Interview Questions

- [ ] What are numeric data types?
- [ ] How many numeric types does Python have?
- [ ] What is the difference between `int` and `float`?
- [ ] Which letter represents the imaginary part in Python?
- [ ] Where are complex numbers used?

---

# 🏋️ Practice Programs

## Easy

```python
print(type(100))
```

---

```python
print(type(25.5))
```

---

```python
print(type(3 + 4j))
```

---

## Medium

```python
age = 20
height = 5.8
signal = 2 + 3j

print(type(age))
print(type(height))
print(type(signal))
```

---

## Challenge

Create three variables:

```python
num1 = 50
num2 = 10.5
num3 = 4 + 7j
```

Print the value and type of each.

---

# 📝 Assignment

Complete the following:

- [x] Create one integer variable.
- [x] Create one float variable.
- [x] Create one complex variable.
- [x] Print the type of each.
- [x] Explain the difference between the three numeric types in your own words.

---

# 📚 Summary

In this lesson, you learned:

- What Numbers are in Python.
- The three numeric data types.
- Real-world uses of numeric types.
- Common mistakes.
- Best practices.
- How to identify numeric types.

---

# 🎯 Topic Completion Checklist

- [x] I know what Numbers are.
- [x] I know the three numeric types.
- [x] I can identify `int`, `float`, and `complex`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 2: Integer (`int`)**

---

## ⭐ Quote of the Day

> **"Every calculation in Python begins with understanding numbers."** 🐍