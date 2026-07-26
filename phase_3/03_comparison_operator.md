# 🐍 Python Master Course

> **Phase 3:** Operators  
> **Topic 3:** Comparison (Relational) Operators

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand comparison operators.
- [ ] Compare two values.
- [ ] Use comparison operators in conditions.
- [ ] Understand the difference between `=` and `==`.
- [ ] Build decision-making programs using comparisons.

---

# 📖 What are Comparison Operators?

Comparison operators are used to **compare two values**.

They always return a Boolean value:

- `True`
- `False`

Example:

```python
print(10 > 5)
```

Output

```text
True
```

---

# 📚 Types of Comparison Operators

| Operator | Name | Example |
|----------|------|---------|
| `==` | Equal To | `10 == 10` |
| `!=` | Not Equal To | `10 != 5` |
| `>` | Greater Than | `10 > 5` |
| `<` | Less Than | `5 < 10` |
| `>=` | Greater Than or Equal To | `10 >= 5` |
| `<=` | Less Than or Equal To | `5 <= 10` |

---

# 1️⃣ Equal To (`==`)

Checks whether two values are equal.

### Syntax

```python
a == b
```

### Example

```python
print(10 == 10)
```

Output

```text
True
```

---

### Example

```python
print(10 == 5)
```

Output

```text
False
```

---

# Real-World Example

```python
password = "python123"

print(password == "python123")
```

Output

```text
True
```

---

# 2️⃣ Not Equal To (`!=`)

Checks whether two values are different.

### Syntax

```python
a != b
```

### Example

```python
print(10 != 5)
```

Output

```text
True
```

---

### Example

```python
print(20 != 20)
```

Output

```text
False
```

---

# Real-World Example

```python
username = "admin"

print(username != "guest")
```

Output

```text
True
```

---

# 3️⃣ Greater Than (`>`)

Checks whether the left value is greater.

### Example

```python
print(15 > 10)
```

Output

```text
True
```

---

### Example

```python
print(5 > 10)
```

Output

```text
False
```

---

# Real-World Example

```python
age = 20

print(age > 18)
```

Output

```text
True
```

---

# 4️⃣ Less Than (`<`)

Checks whether the left value is smaller.

### Example

```python
print(5 < 10)
```

Output

```text
True
```

---

### Example

```python
print(20 < 10)
```

Output

```text
False
```

---

# Real-World Example

```python
temperature = 18

print(temperature < 25)
```

Output

```text
True
```

---

# 5️⃣ Greater Than or Equal To (`>=`)

Checks whether the left value is greater than or equal to the right value.

### Example

```python
print(18 >= 18)
```

Output

```text
True
```

---

### Example

```python
print(12 >= 20)
```

Output

```text
False
```

---

# Real-World Example

```python
marks = 35

print(marks >= 35)
```

Output

```text
True
```

Student passes because the minimum passing mark is 35.

---

# 6️⃣ Less Than or Equal To (`<=`)

Checks whether the left value is less than or equal to the right value.

### Example

```python
print(5 <= 5)
```

Output

```text
True
```

---

### Example

```python
print(15 <= 10)
```

Output

```text
False
```

---

# Real-World Example

```python
speed = 80

print(speed <= 80)
```

Output

```text
True
```

---

# 📊 Summary Table

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `==` | Equal To | `5 == 5` | `True` |
| `!=` | Not Equal To | `5 != 5` | `False` |
| `>` | Greater Than | `10 > 5` | `True` |
| `<` | Less Than | `5 < 10` | `True` |
| `>=` | Greater Than or Equal | `10 >= 10` | `True` |
| `<=` | Less Than or Equal | `5 <= 5` | `True` |

---

# ⚠️ Common Mistakes

## ❌ Using `=` Instead of `==`

Incorrect

```python
if age = 18:
    print("Adult")
```

Output

```text
SyntaxError
```

Correct

```python
if age == 18:
    print("Adult")
```

---

## ❌ Comparing Different Data Types

```python
print(10 == "10")
```

Output

```text
False
```

One is an integer and the other is a string.

---

## ❌ Assuming `True` Equals `"True"`

```python
print(True == "True")
```

Output

```text
False
```

---

# 💡 Best Practices

- Use `==` for comparison, not `=`.
- Compare values of the same data type whenever possible.
- Use meaningful variable names for better readability.
- Remember that comparison operators always return `True` or `False`.

---

# 🚀 Pro Tips

Comparison operators can compare strings alphabetically.

```python
print("Apple" < "Banana")
```

Output

```text
True
```

Python compares strings based on Unicode values.

---

# 🌍 Real-World Programs

## Check Voting Eligibility

```python
age = 21

print(age >= 18)
```

Output

```text
True
```

---

## Check Login

```python
username = "admin"

print(username == "admin")
```

Output

```text
True
```

---

## Compare Prices

```python
price = 100

print(price < 150)
```

Output

```text
True
```

---

## Compare Exam Marks

```python
marks = 75

print(marks >= 35)
```

Output

```text
True
```

---

# ❓ Interview Questions

- [ ] What are comparison operators?
- [ ] What is the difference between `=` and `==`?
- [ ] Which comparison operators are available in Python?
- [ ] What data type is returned by comparison operators?
- [ ] Can comparison operators compare strings?

---

# 🏋️ Practice Programs

## Easy

```python
print(20 == 20)
```

---

```python
print(15 != 10)
```

---

```python
print(25 > 18)
```

---

## Medium

```python
age = 17

print(age >= 18)
```

---

```python
salary = 50000

print(salary < 60000)
```

---

```python
print("Python" == "python")
```

---

## Advanced

```python
a = 15
b = 20

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)
```

---

# 🎯 Challenge

Write a program that:

1. Takes two numbers as input.
2. Displays the result of all six comparison operators.
3. Prints each result with a proper label.

Example Output

```text
Equal: False
Not Equal: True
Greater Than: True
Less Than: False
Greater Than or Equal: True
Less Than or Equal: False
```

---

# 📝 Assignment

- [x] Compare two integers using `==`.
- [x] Compare two strings using `!=`.
- [x] Check if one number is greater than another.
- [x] Check if one number is less than another.
- [x] Check if a student has passed using `>=`.
- [x] Check if a speed is within the limit using `<=`.

---

# 📚 Summary

You learned:

- ✅ Equal To (`==`)
- ✅ Not Equal To (`!=`)
- ✅ Greater Than (`>`)
- ✅ Less Than (`<`)
- ✅ Greater Than or Equal To (`>=`)
- ✅ Less Than or Equal To (`<=`)

All comparison operators return either **`True`** or **`False`**.

---

# 🎯 Topic Completion Checklist

- [x] I understand comparison operators.
- [x] I know the difference between `=` and `==`.
- [x] I can compare numbers and strings.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 4: Logical Operators**