# 🐍 Python Master Course

> **Phase 4:** Conditional statements
> **Topic 6:** Ternary Operator (Conditional Expression)

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the ternary operator is.
- [ ] Write `if...else` statements in a single line.
- [ ] Know when to use the ternary operator.
- [ ] Improve code readability.
- [ ] Solve real-world problems using the ternary operator.

---

# 📖 What is the Ternary Operator?

The **Ternary Operator** (also called the **Conditional Expression**) is a **short, one-line way** of writing a simple `if...else` statement.

Instead of writing multiple lines, you can write the condition and both possible outcomes in a single line.

Think of it as:

> **If the condition is True, return one value; otherwise, return another value.**

---

# 🤔 Why is it Called "Ternary"?

The word **ternary** means **three parts**.

A ternary expression has **three components**:

1. Condition
2. Value if the condition is `True`
3. Value if the condition is `False`

Example:

```python
result = "Adult" if age >= 18 else "Minor"
```

- Condition → `age >= 18`
- True value → `"Adult"`
- False value → `"Minor"`

---

# 📖 Syntax

```python
value_if_true if condition else value_if_false
```

---

## General Form

```python
variable = value_if_true if condition else value_if_false
```

---

# 🔍 Syntax Breakdown

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

| Part | Meaning |
|------|---------|
| `"Adult"` | Returned if condition is `True` |
| `age >= 18` | Condition |
| `else` | Separates the two outcomes |
| `"Minor"` | Returned if condition is `False` |

Output

```text
Adult
```

---

# 🔄 Flow of Execution

```text
                 Start
                    │
                    ▼
           Evaluate Condition
                    │
           ┌────────┴────────┐
           │                 │
         True             False
           │                 │
           ▼                 ▼
 Return True Value    Return False Value
           │                 │
           └────────┬────────┘
                    ▼
              Store/Print Result
```

---

# 📖 How Does It Work?

Python performs these steps:

1. Evaluate the condition.
2. If the condition is `True`, return the value before `if`.
3. If the condition is `False`, return the value after `else`.
4. Store or print the result.

---

# 1️⃣ Basic Example

### Using `if...else`

```python
age = 20

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)
```

---

### Using Ternary Operator

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output

```text
Adult
```

---

# 2️⃣ Even or Odd

```python
number = 15

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

Output

```text
Odd
```

---

# 3️⃣ Positive or Negative

```python
number = -10

result = "Positive" if number > 0 else "Negative"

print(result)
```

Output

```text
Negative
```

---

# 4️⃣ Maximum of Two Numbers

```python
a = 20
b = 15

maximum = a if a > b else b

print(maximum)
```

Output

```text
20
```

---

# 5️⃣ Voting Eligibility

```python
age = 16

message = "Eligible to Vote" if age >= 18 else "Not Eligible"

print(message)
```

Output

```text
Not Eligible
```

---

# 📖 Using Comparison Operators

```python
marks = 85

result = "Pass" if marks >= 35 else "Fail"

print(result)
```

---

```python
number = 10

result = "Equal" if number == 10 else "Not Equal"

print(result)
```

---

# 📖 Using Logical Operators

```python
age = 25
citizen = True

status = "Eligible" if age >= 18 and citizen else "Not Eligible"

print(status)
```

Output

```text
Eligible
```

---

# 📖 Using Membership Operators

```python
fruit = "Apple"

message = "Available" if fruit in ["Apple", "Banana"] else "Not Available"

print(message)
```

Output

```text
Available
```

---

# 📖 Using Identity Operators

```python
value = None

result = "Empty" if value is None else "Not Empty"

print(result)
```

Output

```text
Empty
```

---

# 📖 Nested Ternary Operator

A ternary operator can also contain another ternary operator.

### Syntax

```python
value1 if condition1 else value2 if condition2 else value3
```

---

### Example

```python
marks = 82

grade = (
    "A"
    if marks >= 90
    else "B"
    if marks >= 75
    else "C"
)

print(grade)
```

Output

```text
B
```

⚠️ **Note:** Nested ternary operators work, but they can become difficult to read. For many conditions, prefer `if...elif...else`.

---

# 📖 Multiple Assignment Example

```python
salary = 50000

bonus = 5000 if salary >= 50000 else 1000

print(bonus)
```

Output

```text
5000
```

---

# 📖 Printing Directly

You do not always need a variable.

```python
age = 21

print("Adult" if age >= 18 else "Minor")
```

Output

```text
Adult
```

---

# 📊 Ternary Operator vs `if...else`

## Using `if...else`

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## Using Ternary Operator

```python
age = 18

print("Adult" if age >= 18 else "Minor")
```

The ternary operator is shorter, but use it only for **simple conditions**.

---

# 📖 When Should You Use the Ternary Operator?

✅ Use it for:

- Simple decisions
- Assigning one of two values
- Returning one of two results
- Short, readable conditions

❌ Avoid it for:

- Complex conditions
- Multiple `elif` cases
- Long expressions
- Deeply nested logic

---

# 📊 Summary Table

| Feature | Ternary Operator | `if...else` |
|----------|------------------|-------------|
| One-line syntax | ✅ | ❌ |
| Multiple statements | ❌ | ✅ |
| Simple conditions | ✅ | ✅ |
| Complex conditions | ❌ | ✅ |
| Better readability for long logic | ❌ | ✅ |

---

# 🌍 Real-World Programs

## Login Status

```python
logged_in = True

message = "Welcome" if logged_in else "Please Login"

print(message)
```

---

## Shopping Discount

```python
amount = 2500

discount = "10% Discount" if amount >= 2000 else "No Discount"

print(discount)
```

---

## Temperature Check

```python
temperature = 30

status = "Hot" if temperature >= 30 else "Cool"

print(status)
```

---

## Password Length

```python
password = "python123"

result = "Strong" if len(password) >= 8 else "Weak"

print(result)
```

---

## Student Result

```python
marks = 60

result = "Pass" if marks >= 35 else "Fail"

print(result)
```

---

# ⚠️ Common Mistakes

## ❌ Wrong Order

Incorrect

```python
result = if age >= 18 "Adult" else "Minor"
```

Correct

```python
result = "Adult" if age >= 18 else "Minor"
```

---

## ❌ Forgetting `else`

Incorrect

```python
result = "Adult" if age >= 18
```

A ternary operator **must always include `else`**.

Correct

```python
result = "Adult" if age >= 18 else "Minor"
```

---

## ❌ Using It for Complex Logic

Incorrect

```python
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "Fail"
```

Although valid, it is difficult to read.

Prefer:

```python
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "Fail"
```

---

# 💡 Best Practices

- Use the ternary operator only for simple decisions.
- Keep the expression short.
- Prefer `if...else` for multiple conditions.
- Write readable code.

---

# 🚀 Pro Tips

The ternary operator is commonly used for:

- UI messages
- Status labels
- Validation results
- Simple assignments
- Short return statements in functions

---

# ❓ Interview Questions

- [ ] What is a ternary operator?
- [ ] Why is it called a ternary operator?
- [ ] What is the syntax of the ternary operator?
- [ ] When should you use the ternary operator?
- [ ] Can you write nested ternary operators?
- [ ] What is the difference between a ternary operator and an `if...else` statement?

---

# 🏋️ Practice Programs

## Easy

```python
age = 19

result = "Adult" if age >= 18 else "Minor"

print(result)
```

---

```python
number = 8

print("Even" if number % 2 == 0 else "Odd")
```

---

## Medium

```python
salary = 60000

bonus = 10000 if salary >= 50000 else 3000

print(bonus)
```

---

```python
fruit = "Mango"

print("Available" if fruit in ["Apple", "Mango"] else "Not Available")
```

---

## Advanced

```python
marks = 95

grade = (
    "A+"
    if marks >= 90
    else "A"
    if marks >= 80
    else "B"
)

print(grade)
```

---

```python
username = "admin"
password = "python123"

print(
    "Login Successful"
    if username == "admin" and password == "python123"
    else "Login Failed"
)
```

---

# 🎯 Challenge

Write a program that:

1. Takes two numbers from the user.
2. Uses a **ternary operator** to find the larger number.
3. Prints the result.

Example

```text
Enter first number: 15
Enter second number: 22

Larger Number: 22
```

---

# 📝 Assignment

- [x] Find the larger of two numbers using a ternary operator.
- [x] Check whether a number is even or odd.
- [x] Check voting eligibility.
- [x] Check whether a password is strong.
- [x] Create a simple login status message.

---

# 📚 Summary

You learned:

- ✅ What the ternary operator is.
- ✅ Why it is called a conditional expression.
- ✅ Its syntax and execution flow.
- ✅ How to use comparison, logical, membership, and identity operators.
- ✅ Nested ternary operators.
- ✅ Differences between the ternary operator and `if...else`.
- ✅ Real-world applications.
- ✅ Common mistakes and best practices.

Remember:

- **Syntax:** `value_if_true if condition else value_if_false`
- The ternary operator is best for **simple, single-condition decisions**.
- For multiple conditions or complex logic, use `if...elif...else`.

---

# 🎯 Topic Completion Checklist

- [x] I understand the ternary operator.
- [x] I know its syntax.
- [x] I know when to use it.
- [x] I understand nested ternary operators.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 🎉 Phase 4 Completed!

## ✅ Topics Covered

- [x] `if` Statement
- [x] `if...else` Statement
- [x] `if...elif...else` Statement
- [x] Nested `if`
- [x] `match...case` Statement (Python 3.10+)
- [x] Ternary Operator

---

# 📚 Next Phase

➡️ **Phase 5: Loops**
