# 🐍 Python Master Course

> **Phase 4:** Conditional statements 
> **Topic 1:** `if` Statement

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what an `if` statement is.
- [ ] Write simple decision-making programs.
- [ ] Understand how Python executes an `if` statement.
- [ ] Use comparison and logical operators with `if`.
- [ ] Solve real-world problems using `if`.

---

# 📖 What is an `if` Statement?

An `if` statement is used to **execute a block of code only when a condition is `True`.**

If the condition is `False`, Python skips the block and continues with the next statement.

Think of it like this:

> **IF a condition is true → Do something.**

Otherwise, do nothing.

---

# 🧠 Syntax

```python
if condition:
    # Code to execute if the condition is True
```

### Syntax Breakdown

```python
if age >= 18:
    print("Eligible to Vote")
```

| Part | Meaning |
|------|---------|
| `if` | Keyword that starts the condition |
| `age >= 18` | Condition being checked |
| `:` | Colon marks the start of the block |
| Indentation | Code inside the `if` block |

---

# 🔄 Flow of Execution

```text
Start
   │
   ▼
Check Condition
   │
 ┌─┴───────────┐
 │             │
True         False
 │             │
 ▼             │
Run if Block   │
 │             │
 └──────┬──────┘
        ▼
 Continue Program
```

---

# 📖 How Does It Work?

Python follows these steps:

1. Read the condition.
2. Evaluate it.
3. If the result is `True`, execute the indented block.
4. If the result is `False`, skip the block.
5. Continue with the remaining program.

---

# 1️⃣ Basic Example

```python
age = 20

if age >= 18:
    print("You can vote.")
```

Output

```text
You can vote.
```

---

# 2️⃣ Condition is False

```python
age = 15

if age >= 18:
    print("You can vote.")

print("Program Finished")
```

Output

```text
Program Finished
```

The `if` block was skipped because the condition was `False`.

---

# 3️⃣ Multiple Statements Inside `if`

```python
marks = 90

if marks >= 35:
    print("Pass")
    print("Congratulations!")
    print("Collect your report card.")
```

Output

```text
Pass
Congratulations!
Collect your report card.
```

All indented statements belong to the `if` block.

---

# 📖 Importance of Indentation

Python uses indentation to determine which statements belong to the `if` block.

Correct:

```python
age = 18

if age >= 18:
    print("Adult")
```

Incorrect:

```python
age = 18

if age >= 18:
print("Adult")
```

Output

```text
IndentationError
```

---

# 📖 Using Comparison Operators

```python
number = 50

if number > 10:
    print("Greater than 10")
```

---

```python
marks = 90

if marks == 90:
    print("Excellent")
```

---

```python
temperature = 20

if temperature != 30:
    print("Temperature changed")
```

---

# 📖 Using Logical Operators

```python
age = 25

if age > 18 and age < 60:
    print("Working Age")
```

---

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

# 📖 Using Membership Operators

```python
fruits = ["Apple", "Mango", "Banana"]

if "Apple" in fruits:
    print("Fruit Available")
```

---

# 📖 Using Identity Operators

```python
value = None

if value is None:
    print("No value assigned")
```

---

# 📖 Truthy and Falsy Values

An `if` statement doesn't always need `True` or `False`.

Python automatically treats some values as **truthy** and others as **falsy**.

## Truthy Values

```python
if 10:
    print("Executed")
```

Output

```text
Executed
```

---

```python
if "Python":
    print("Executed")
```

Output

```text
Executed
```

---

```python
if [1, 2]:
    print("Executed")
```

Output

```text
Executed
```

---

## Falsy Values

```python
if 0:
    print("Executed")
```

Nothing is printed.

---

```python
if "":
    print("Executed")
```

Nothing is printed.

---

```python
if []:
    print("Executed")
```

Nothing is printed.

---

Common falsy values:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `''`
- `[]`
- `{}`
- `set()`
- `()`

Everything else is generally truthy.

---

# 📊 Summary Table

| Condition | Result |
|-----------|--------|
| `if True:` | Executes |
| `if False:` | Skips |
| `if 1:` | Executes |
| `if 0:` | Skips |
| `if "Hello":` | Executes |
| `if "":` | Skips |
| `if []:` | Skips |
| `if [1]:` | Executes |

---

# 🌍 Real-World Programs

## Check Voting Eligibility

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

## Check Account Balance

```python
balance = 1500

if balance >= 1000:
    print("Minimum balance maintained")
```

---

## Check Password Length

```python
password = "python123"

if len(password) >= 8:
    print("Strong Password")
```

---

## Check Product Availability

```python
products = ["Laptop", "Mouse", "Keyboard"]

if "Laptop" in products:
    print("Product Available")
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting the Colon

Incorrect

```python
if age >= 18
    print("Adult")
```

Output

```text
SyntaxError
```

Correct

```python
if age >= 18:
    print("Adult")
```

---

## ❌ Wrong Indentation

Incorrect

```python
if True:
print("Hello")
```

Output

```text
IndentationError
```

---

## ❌ Using `=` Instead of `==`

Incorrect

```python
if marks = 90:
    print("Excellent")
```

Output

```text
SyntaxError
```

Correct

```python
if marks == 90:
    print("Excellent")
```

---

# 💡 Best Practices

- Always use meaningful conditions.
- Keep `if` blocks short and readable.
- Use proper indentation (4 spaces).
- Use parentheses only when they improve readability.

---

# 🚀 Pro Tips

An `if` statement can check almost anything:

- Numbers
- Strings
- Lists
- Dictionaries
- Functions
- Objects
- Boolean expressions

This makes it one of the most powerful statements in Python.

---

# ❓ Interview Questions

- [ ] What is an `if` statement?
- [ ] When does an `if` block execute?
- [ ] What happens if the condition is `False`?
- [ ] Why is indentation important in Python?
- [ ] What are truthy and falsy values?

---

# 🏋️ Practice Programs

## Easy

```python
age = 21

if age >= 18:
    print("Adult")
```

---

```python
number = 15

if number > 10:
    print("Greater than 10")
```

---

```python
if True:
    print("Python")
```

---

## Medium

```python
marks = 82

if marks >= 35:
    print("Pass")
```

---

```python
name = "Saniya"

if name == "Saniya":
    print("Welcome")
```

---

```python
fruits = ["Apple", "Banana"]

if "Banana" in fruits:
    print("Available")
```

---

## Advanced

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
```

---

```python
password = "python123"

if len(password) >= 8:
    print("Password Accepted")
```

---

# 🎯 Challenge

Write a program that:

1. Takes the user's age as input.
2. If the age is 18 or above, print:

```text
You are eligible to vote.
```

3. Do **not** use `else`.

Example

```text
Enter age: 20

You are eligible to vote.
```

If the age is 16, the program should simply finish without printing the voting message.

---

# 📝 Assignment

- [x] Check whether a number is positive.
- [x] Check whether a student passed.
- [x] Check if a string starts with `"P"`.
- [x] Check whether a list contains `"Python"`.
- [x] Check whether a variable is `None`.

---
# 📚 Summary

You learned:

- ✅ What an `if` statement is.
- ✅ How Python evaluates conditions.
- ✅ The importance of indentation.
- ✅ Truthy and falsy values.
- ✅ Using comparison, logical, membership, and identity operators inside `if`.
- ✅ Real-world applications of `if`.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `if` statement.
- [x] I know when an `if` block executes.
- [x] I understand indentation.
- [x] I understand truthy and falsy values.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 4 – Topic 2: `if...else` Statement**