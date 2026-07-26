# 🐍 Python Master Course

> **Phase 3:** Operators  
> **Topic 4:** Logical Operators

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand logical operators.
- [ ] Combine multiple conditions.
- [ ] Make decisions using logical expressions.
- [ ] Understand short-circuit evaluation.
- [ ] Write real-world logical programs.

---

# 📖 What are Logical Operators?

Logical operators are used to **combine or modify conditions**.

They always return either:

- `True`
- `False`

Python has **three logical operators**:

| Operator | Meaning |
|----------|---------|
| `and` | Returns `True` if **both** conditions are `True` |
| `or` | Returns `True` if **at least one** condition is `True` |
| `not` | Reverses the Boolean value |

---

# 1️⃣ AND Operator (`and`)

The `and` operator returns **True only if both conditions are True**.

### Syntax

```python
condition1 and condition2
```

### Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

### Example

```python
age = 25

print(age > 18 and age < 60)
```

Output

```text
True
```

---

### Another Example

```python
marks = 80

print(marks >= 35 and marks <= 100)
```

Output

```text
True
```

---

# 🌍 Real-World Example

Eligible for a driving license.

```python
age = 22
has_license_test = True

print(age >= 18 and has_license_test)
```

Output

```text
True
```

---

# 2️⃣ OR Operator (`or`)

The `or` operator returns **True if at least one condition is True**.

### Syntax

```python
condition1 or condition2
```

### Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

### Example

```python
age = 16

print(age < 18 or age > 60)
```

Output

```text
True
```

---

### Another Example

```python
username = "admin"
password = "1234"

print(username == "admin" or password == "admin123")
```

Output

```text
True
```

---

# 🌍 Real-World Example

Weekend check.

```python
day = "Saturday"

print(day == "Saturday" or day == "Sunday")
```

Output

```text
True
```

---

# 3️⃣ NOT Operator (`not`)

The `not` operator **reverses** the Boolean result.

### Syntax

```python
not condition
```

### Truth Table

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

---

### Example

```python
is_logged_in = True

print(not is_logged_in)
```

Output

```text
False
```

---

### Another Example

```python
print(not (10 > 5))
```

Output

```text
False
```

---

# 🌍 Real-World Example

Store closed.

```python
shop_open = False

print(not shop_open)
```

Output

```text
True
```

Meaning: the shop is **not open**.

---

# 🔗 Combining Logical Operators

You can combine multiple logical operators.

```python
age = 25
citizen = True

print(age >= 18 and citizen)
```

Output

```text
True
```

---

```python
marks = 90

print((marks >= 90) or (marks == 100))
```

Output

```text
True
```

---

```python
is_raining = False

print(not is_raining)
```

Output

```text
True
```

---

# 📖 Short-Circuit Evaluation

Python stops checking conditions as soon as the final result is known.

## Example 1

```python
print(True or (10 / 0))
```

Output

```text
True
```

Python never evaluates `10 / 0` because the first condition is already `True`.

---

## Example 2

```python
print(False and (10 / 0))
```

Output

```text
False
```

Python never evaluates `10 / 0` because the first condition is already `False`.

---

# 📊 Summary Table

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both conditions must be True | `5 > 2 and 10 > 3` | `True` |
| `or` | At least one condition is True | `5 > 8 or 10 > 3` | `True` |
| `not` | Reverses the result | `not(True)` | `False` |

---

# ⚠️ Common Mistakes

## ❌ Using `&` Instead of `and`

Incorrect

```python
print(True & False)
```

Although this works with Boolean values, use:

```python
print(True and False)
```

`and` is the logical operator used for conditions.

---

## ❌ Forgetting Parentheses

Incorrect

```python
print(not 10 > 5)
```

This works, but writing it as:

```python
print(not (10 > 5))
```

is clearer and easier to read.

---

## ❌ Confusing `or` with `and`

```python
age = 20

print(age > 18 or age < 60)
```

This returns `True` because only one condition needs to be `True`.

If both conditions are required, use:

```python
print(age > 18 and age < 60)
```

---

# 💡 Best Practices

- Use `and` when **all conditions** must be satisfied.
- Use `or` when **any one condition** is enough.
- Use `not` to reverse a condition.
- Use parentheses for complex expressions to improve readability.

---

# 🚀 Pro Tips

Logical operators are used extensively with:

- `if` statements
- `while` loops
- Login systems
- Validation
- Games
- AI/ML decision-making
- Web development

Mastering logical operators makes writing conditions much easier.

---

# 🌍 Real-World Programs

## Voting Eligibility

```python
age = 19
citizen = True

print(age >= 18 and citizen)
```

Output

```text
True
```

---

## Login Validation

```python
username = "admin"
password = "python123"

print(username == "admin" and password == "python123")
```

Output

```text
True
```

---

## Holiday Check

```python
day = "Sunday"

print(day == "Saturday" or day == "Sunday")
```

Output

```text
True
```

---

## Internet Connection

```python
internet = False

print(not internet)
```

Output

```text
True
```

---

# ❓ Interview Questions

- [ ] What are logical operators?
- [ ] What is the difference between `and` and `or`?
- [ ] What does the `not` operator do?
- [ ] What is short-circuit evaluation?
- [ ] Why are logical operators important in Python?

---

# 🏋️ Practice Programs

## Easy

```python
print(True and True)
```

---

```python
print(True or False)
```

---

```python
print(not False)
```

---

## Medium

```python
age = 25

print(age > 18 and age < 60)
```

---

```python
marks = 85

print(marks >= 35 or marks == 100)
```

---

```python
logged_in = False

print(not logged_in)
```

---

## Advanced

```python
username = "admin"
password = "python123"
age = 21

print(username == "admin" and password == "python123" and age >= 18)
```

---

# 🎯 Challenge

Write a program that:

1. Takes the user's age.
2. Takes whether the user has an ID card (`True` or `False`).
3. Prints whether the user is eligible to enter an event.

Condition:

- Age must be **18 or above**
- The user **must have an ID card**

Expected Output

```text
Eligible: True
```

or

```text
Eligible: False
```

---

# 📝 Assignment

- [x] Use `and` to compare two conditions.
- [x] Use `or` to compare two conditions.
- [x] Use `not` to reverse a condition.
- [x] Write a program to check voting eligibility.
- [x] Write a login validation program.
- [x] Experiment with short-circuit evaluation.

---

# 📚 Summary

You learned:

- ✅ `and`
- ✅ `or`
- ✅ `not`
- ✅ Truth tables
- ✅ Short-circuit evaluation
- ✅ Real-world applications

Logical operators help combine and control conditions in Python programs.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `and` operator.
- [x] I understand the `or` operator.
- [x] I understand the `not` operator.
- [x] I understand short-circuit evaluation.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 5: Identity Operators**