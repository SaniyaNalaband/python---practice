# 🐍 Python Master Course

> **Phase 4:** Conditional statements
> **Topic 4:** Nested `if` Statement

**Difficulty:** ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a nested `if` statement is.
- [ ] Write `if` statements inside other `if` statements.
- [ ] Understand the execution flow of nested conditions.
- [ ] Solve real-world problems using nested `if`.
- [ ] Know when to use nested `if` instead of logical operators.

---

# 📖 What is a Nested `if` Statement?

A **Nested `if`** means **placing one `if` statement inside another `if` statement**.

The inner `if` executes **only if the outer `if` condition is `True`.**

Think of it like entering a building:

```text
Step 1:
Are you allowed to enter the building?

       YES
        │
        ▼
Step 2:
Can you enter the VIP room?

       YES
        │
        ▼
Access Granted
```

If you cannot enter the building, Python will never check the VIP room.

---

# 📖 Syntax

```python
if condition1:

    if condition2:
        # Code

    else:
        # Code

else:
    # Code
```

---

# 🔍 Syntax Breakdown

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")
```

Explanation

- Outer `if` checks the age.
- Inner `if` checks citizenship.
- Both conditions must be satisfied.

---

# 🔄 Flow of Execution

```text
                  Start
                     │
                     ▼
         Check Outer Condition
                     │
           ┌─────────┴─────────┐
           │                   │
         True               False
           │                   │
           ▼                   ▼
    Check Inner Condition    Skip Inner
           │                   │
     ┌─────┴──────┐            │
     │            │            │
   True        False           │
     │            │            │
     ▼            ▼            ▼
 Execute      Execute       Continue
 Inner if    Inner else
```

---

# 📖 How Does It Work?

Python follows these steps:

1. Evaluate the outer `if`.
2. If it is `False`, the inner `if` is skipped completely.
3. If it is `True`, Python evaluates the inner `if`.
4. Execute the appropriate inner block.
5. Continue with the remaining program.

---

# 1️⃣ Basic Example

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")
```

Output

```text
Eligible to Vote
```

---

# 2️⃣ Outer Condition is False

```python
age = 15
citizen = True

if age >= 18:

    if citizen:
        print("Eligible")
```

Output

```text
(No Output)
```

The inner `if` is never checked because the outer condition failed.

---

# 3️⃣ Nested `if...else`

```python
age = 25
citizen = False

if age >= 18:

    if citizen:
        print("Eligible")

    else:
        print("Citizen Required")

else:
    print("Under Age")
```

Output

```text
Citizen Required
```

---

# 4️⃣ Student Login Example

```python
username = "Saniya"
password = "python123"

if username == "Saniya":

    if password == "python123":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("Wrong Username")
```

Output

```text
Login Successful
```

---

# 5️⃣ ATM Withdrawal

```python
balance = 5000
amount = 3000

if balance >= amount:

    pin = 1234

    if pin == 1234:
        print("Withdrawal Successful")

    else:
        print("Incorrect PIN")

else:
    print("Insufficient Balance")
```

Output

```text
Withdrawal Successful
```

---

# 6️⃣ College Admission

```python
marks = 85
documents_verified = True

if marks >= 75:

    if documents_verified:
        print("Admission Confirmed")

    else:
        print("Verify Documents")

else:
    print("Admission Rejected")
```

Output

```text
Admission Confirmed
```

---

# 📖 Nested `if` vs Logical Operator

Sometimes a nested `if` can be replaced with `and`.

## Nested `if`

```python
age = 22
citizen = True

if age >= 18:

    if citizen:
        print("Eligible")
```

---

## Using `and`

```python
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

Both produce the same output.

---

# 📖 When Should You Use Nested `if`?

Use a nested `if` when the second condition **depends on** the first condition.

### Example

A user must first log in before checking whether they are an administrator.

```python
logged_in = True
is_admin = True

if logged_in:

    if is_admin:
        print("Admin Panel")
```

This is easier to understand than combining unrelated conditions.

---

# 📊 Summary Table

| Outer Condition | Inner Condition | Output |
|-----------------|-----------------|--------|
| True | True | Inner `if` block |
| True | False | Inner `else` block |
| False | Not Checked | Outer `else` (if present) or skip |

---

# 🌍 Real-World Programs

## Banking System

```python
balance = 10000
amount = 2000

if balance >= amount:

    otp_verified = True

    if otp_verified:
        print("Transaction Successful")

    else:
        print("OTP Verification Failed")

else:
    print("Insufficient Balance")
```

---

## Online Shopping

```python
logged_in = True
payment_done = True

if logged_in:

    if payment_done:
        print("Order Confirmed")

    else:
        print("Complete Payment")

else:
    print("Please Login")
```

---

## Exam Result

```python
marks = 80
attendance = 90

if marks >= 35:

    if attendance >= 75:
        print("Pass")

    else:
        print("Attendance Shortage")

else:
    print("Fail")
```

---

## Door Security

```python
door_unlocked = True
fingerprint_verified = True

if door_unlocked:

    if fingerprint_verified:
        print("Access Granted")

    else:
        print("Fingerprint Required")

else:
    print("Door Locked")
```

---

# ⚠️ Common Mistakes

## ❌ Wrong Indentation

Incorrect

```python
if age >= 18:

if citizen:
    print("Eligible")
```

Output

```text
IndentationError
```

Correct

```python
if age >= 18:

    if citizen:
        print("Eligible")
```

---

## ❌ Forgetting the Colon

Incorrect

```python
if age >= 18
```

Correct

```python
if age >= 18:
```

---

## ❌ Using Nested `if` Unnecessarily

Instead of

```python
if marks >= 35:

    if marks <= 100:
        print("Valid")
```

You can write

```python
if 35 <= marks <= 100:
    print("Valid")
```

This is shorter and easier to read.

---

## ❌ Using `=` Instead of `==`

Incorrect

```python
if pin = 1234:
```

Correct

```python
if pin == 1234:
```

---

# 💡 Best Practices

- Keep nesting levels as small as possible.
- Use logical operators when conditions are simple.
- Use nested `if` only when one condition depends on another.
- Indent consistently using 4 spaces.

---

# 🚀 Pro Tips

Nested `if` statements are commonly used in:

- Login systems
- Banking applications
- ATM software
- Security systems
- Online shopping
- Hospital management
- Student admission portals
- Role-based access control

---

# ❓ Interview Questions

- [ ] What is a nested `if` statement?
- [ ] When should you use a nested `if`?
- [ ] Can a nested `if` be replaced with `and`?
- [ ] What happens if the outer `if` is `False`?
- [ ] What is the biggest disadvantage of deep nesting?

---

# 🏋️ Practice Programs

## Easy

```python
age = 20
student = True

if age >= 18:

    if student:
        print("Eligible for Student Discount")
```

---

```python
number = 10

if number > 0:

    if number % 2 == 0:
        print("Positive Even Number")
```

---

## Medium

```python
username = "admin"
password = "python"

if username == "admin":

    if password == "python":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("Wrong Username")
```

---

```python
marks = 90
attendance = 80

if marks >= 35:

    if attendance >= 75:
        print("Pass")

    else:
        print("Attendance Shortage")

else:
    print("Fail")
```

---

## Advanced

```python
balance = 15000
amount = 5000
pin = 1234

if balance >= amount:

    if pin == 1234:

        otp = True

        if otp:
            print("Transaction Successful")

        else:
            print("OTP Failed")

    else:
        print("Wrong PIN")

else:
    print("Insufficient Balance")
```

---

# 🎯 Challenge

Write a program that:

1. Takes the user's age.
2. Takes whether they have a driving license (`True` or `False`).
3. If the age is **18 or above**, check the license.
4. Print:

- `"Eligible to Drive"` if both conditions are satisfied.
- `"License Required"` if age is sufficient but there is no license.
- `"Under Age"` if the user is younger than 18.

Example

```text
Enter Age: 20
Has License: True

Eligible to Drive
```

---

# 📝 Assignment

- [x] Create a login system using nested `if`.
- [x] Create an ATM withdrawal program.
- [x] Create a college admission program.
- [x] Create a banking transaction program with OTP verification.
- [x] Create a door security program.

---

# 📚 Summary

You learned:

- ✅ What a nested `if` statement is.
- ✅ How Python executes nested conditions.
- ✅ When to use nested `if`.
- ✅ Difference between nested `if` and using `and`.
- ✅ Real-world applications.
- ✅ Common mistakes and best practices.

Remember:

- The **inner `if` runs only if the outer `if` is `True`.**
- Avoid excessive nesting because it makes code harder to read.
- Use logical operators when multiple independent conditions can be combined.

---

# 🎯 Topic Completion Checklist

- [x] I understand nested `if`.
- [x] I know how Python executes nested conditions.
- [x] I know when to use nested `if`.
- [x] I understand the difference between nested `if` and `and`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 4 – Topic 5: `match...case` Statement (Python 3.10+)**