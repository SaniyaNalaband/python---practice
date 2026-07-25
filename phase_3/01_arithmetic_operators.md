# 🐍 Python Master Course

> **Phase 3:** Operators
> **Topic 1:** Arithmetic Operators

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand arithmetic operators.
- [ ] Perform mathematical calculations.
- [ ] Know the difference between `/` and `//`.
- [ ] Use `%` to find remainders.
- [ ] Use `**` for exponentiation.
- [ ] Solve real-world mathematical problems.

---

# 📖 What are Arithmetic Operators?

Arithmetic operators are used to perform **mathematical operations** on numbers.

Example:

```python
a = 10
b = 5

print(a + b)
```

Output

```text
15
```

Here, `+` is an arithmetic operator.

---

# 📚 Types of Arithmetic Operators

| Operator | Name | Example |
|----------|------|----------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Modulus | `10 % 3` |
| `**` | Exponentiation | `2 ** 3` |

---

# 1️⃣ Addition (`+`)

Adds two values.

### Syntax

```python
result = a + b
```

### Example

```python
a = 20
b = 30

print(a + b)
```

Output

```text
50
```

---

# Real-World Example

```python
monday_sales = 250
tuesday_sales = 320

total_sales = monday_sales + tuesday_sales

print(total_sales)
```

Output

```text
570
```

---

# 2️⃣ Subtraction (`-`)

Subtracts one value from another.

### Syntax

```python
result = a - b
```

### Example

```python
a = 50
b = 15

print(a - b)
```

Output

```text
35
```

---

# Real-World Example

```python
balance = 1000
purchase = 250

print(balance - purchase)
```

Output

```text
750
```

---

# 3️⃣ Multiplication (`*`)

Multiplies two values.

### Syntax

```python
result = a * b
```

### Example

```python
a = 6
b = 7

print(a * b)
```

Output

```text
42
```

---

# Real-World Example

```python
price = 25
quantity = 4

print(price * quantity)
```

Output

```text
100
```

---

# 4️⃣ Division (`/`)

Divides one number by another.

### Syntax

```python
result = a / b
```

### Example

```python
print(10 / 4)
```

Output

```text
2.5
```

> Division **always returns a float**.

---

# Real-World Example

```python
marks = 450
subjects = 5

average = marks / subjects

print(average)
```

Output

```text
90.0
```

---

# 5️⃣ Floor Division (`//`)

Returns the **whole number** part of the division.

### Syntax

```python
result = a // b
```

### Example

```python
print(10 // 4)
```

Output

```text
2
```

---

# Difference Between `/` and `//`

```python
print(10 / 3)
```

Output

```text
3.3333333333333335
```

```python
print(10 // 3)
```

Output

```text
3
```

---

# Real-World Example

```python
students = 25
group_size = 4

groups = students // group_size

print(groups)
```

Output

```text
6
```

---

# 6️⃣ Modulus (`%`)

Returns the remainder after division.

### Syntax

```python
result = a % b
```

### Example

```python
print(10 % 3)
```

Output

```text
1
```

---

# Real-World Example

Check if a number is even.

```python
number = 18

print(number % 2)
```

Output

```text
0
```

If the remainder is `0`, the number is even.

---

# 7️⃣ Exponentiation (`**`)

Raises a number to a power.

### Syntax

```python
result = a ** b
```

### Example

```python
print(2 ** 5)
```

Output

```text
32
```

---

# Real-World Example

```python
print(10 ** 3)
```

Output

```text
1000
```

---

# 📊 Summary Table

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulus | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

---

# ⚠️ Common Mistakes

## ❌ Division by Zero

```python
print(10 / 0)
```

Output

```text
ZeroDivisionError
```

---

## ❌ Confusing `/` and `//`

```python
print(9 / 2)
```

Output

```text
4.5
```

```python
print(9 // 2)
```

Output

```text
4
```

---

## ❌ Using `%` Incorrectly

```python
print(8 % 2)
```

Output

```text
0
```

The result is the **remainder**, not the quotient.

---

# 💡 Best Practices

- Use `/` when you need the exact result.
- Use `//` when only the whole number is required.
- Use `%` to check for even/odd numbers.
- Use `**` instead of repeated multiplication.

---

# 🚀 Pro Tips

Swap two numbers without a third variable.

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

Output

```text
20 10
```

---

# 🌍 Real-World Programs

## Area of a Rectangle

```python
length = 10
width = 5

area = length * width

print(area)
```

Output

```text
50
```

---

## Average Marks

```python
total = 480
subjects = 6

average = total / subjects

print(average)
```

Output

```text
80.0
```

---

## Find Square

```python
number = 12

print(number ** 2)
```

Output

```text
144
```

---

## Check Even or Odd

```python
number = 15

print(number % 2)
```

Output

```text
1
```

---

# ❓ Interview Questions

- [ ] What are arithmetic operators?
- [ ] What is the difference between `/` and `//`?
- [ ] What does `%` return?
- [ ] What does `**` do?
- [ ] What error occurs when dividing by zero?

---

# 🏋️ Practice Programs

## Easy

```python
print(25 + 15)
```

```python
print(100 - 35)
```

```python
print(9 * 8)
```

---

## Medium

```python
print(25 / 4)
```

```python
print(25 // 4)
```

```python
print(25 % 4)
```

---

## Advanced

```python
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)
```

---

# 🎯 Challenge

Write a program that:

1. Takes two numbers from the user.
2. Performs all seven arithmetic operations.
3. Displays each result with a label.

Expected Output

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
Floor Division: 2
Modulus: 0
Power: 100000
```

---

# 📝 Assignment

- [x] Add two numbers.
- [x] Subtract two numbers.
- [x] Multiply two numbers.
- [x] Divide two numbers.
- [x] Find floor division.
- [x] Find modulus.
- [x] Find exponentiation.
- [x] Check whether a number is even or odd using `%`.

---

# 📚 Summary

You learned:

- ✅ Addition (`+`)
- ✅ Subtraction (`-`)
- ✅ Multiplication (`*`)
- ✅ Division (`/`)
- ✅ Floor Division (`//`)
- ✅ Modulus (`%`)
- ✅ Exponentiation (`**`)

---

# 🎯 Topic Completion Checklist

- [x] I understand all arithmetic operators.
- [x] I know the difference between `/` and `//`.
- [x] I can use `%` to find remainders.
- [x] I can use `**` for powers.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 2: Assignment Operators**