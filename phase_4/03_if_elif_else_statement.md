# 🐍 Python Master Course

> **Phase 4:** Conditional statements 
> **Topic 3:** `if...elif...else` Statement

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand the `if...elif...else` statement.
- [ ] Make decisions using multiple conditions.
- [ ] Understand the execution flow.
- [ ] Avoid common mistakes.
- [ ] Solve real-world decision-making problems.

---

# 📖 What is an `if...elif...else` Statement?

The `if...elif...else` statement is used when there are **more than two possible outcomes**.

Instead of checking only one condition (`if`) or two outcomes (`if...else`), you can check **multiple conditions one after another**.

Think of it like this:

```text
IF Condition 1 is True
      ↓
Otherwise check Condition 2
      ↓
Otherwise check Condition 3
      ↓
Otherwise execute else
```

Python checks each condition **from top to bottom** and executes **only the first condition that is True**.

---

# 📖 Syntax

```python
if condition1:
    # Code Block 1

elif condition2:
    # Code Block 2

elif condition3:
    # Code Block 3

else:
    # Default Code Block
```

---

# 🔍 Syntax Breakdown

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

| Keyword | Meaning |
|----------|---------|
| `if` | First condition |
| `elif` | Checks another condition if previous one was False |
| `else` | Runs if none of the conditions are True |

---

# 🔄 Flow of Execution

```text
                Start
                   │
                   ▼
          Check if Condition 1
                   │
          ┌────────┴────────┐
          │                 │
        True              False
          │                 │
          ▼                 ▼
     Execute Block 1   Check Condition 2
                            │
                    ┌───────┴────────┐
                    │                │
                  True            False
                    │                │
                    ▼                ▼
              Execute Block 2  Check Condition 3
                                      │
                             ┌────────┴────────┐
                             │                 │
                           True             False
                             │                 │
                             ▼                 ▼
                       Execute Block 3    Execute Else
                                      │
                                      ▼
                                Continue Program
```

---

# 📖 How Does It Work?

Python checks the conditions **one by one**.

- If the first condition is `True`, Python executes it and **stops**.
- If it is `False`, Python checks the next `elif`.
- This continues until a condition becomes `True`.
- If none of the conditions are `True`, the `else` block executes.

---

# 1️⃣ Basic Example

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

else:
    print("Grade C")
```

Output

```text
Grade B
```

---

# 2️⃣ Multiple `elif`

```python
number = 0

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

Output

```text
Zero
```

---

# 3️⃣ Student Grade System

```python
marks = 67

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

elif marks >= 60:
    print("C")

elif marks >= 35:
    print("Pass")

else:
    print("Fail")
```

Output

```text
C
```

---

# 4️⃣ Traffic Signal

```python
signal = "Red"

if signal == "Green":
    print("Go")

elif signal == "Yellow":
    print("Ready")

elif signal == "Red":
    print("Stop")

else:
    print("Invalid Signal")
```

Output

```text
Stop
```

---

# 5️⃣ Weather Advice

```python
weather = "Rainy"

if weather == "Sunny":
    print("Wear Sunglasses")

elif weather == "Rainy":
    print("Carry an Umbrella")

elif weather == "Cold":
    print("Wear a Jacket")

else:
    print("Check the Weather Forecast")
```

Output

```text
Carry an Umbrella
```

---

# 📖 Order Matters

Conditions should be written from **most specific** to **least specific**.

### ❌ Incorrect

```python
marks = 95

if marks >= 35:
    print("Pass")

elif marks >= 90:
    print("A+")
```

Output

```text
Pass
```

Why?

Because `95 >= 35` is already `True`, so Python never checks the next condition.

---

### ✅ Correct

```python
marks = 95

if marks >= 90:
    print("A+")

elif marks >= 35:
    print("Pass")
```

Output

```text
A+
```

---

# 📖 Using Logical Operators

```python
age = 25

if age < 18:
    print("Minor")

elif age >= 18 and age <= 60:
    print("Adult")

else:
    print("Senior Citizen")
```

---

# 📖 Using Membership Operators

```python
language = "Python"

if language in ["Python", "Java"]:
    print("Programming Language")

elif language in ["HTML", "CSS"]:
    print("Web Technology")

else:
    print("Unknown")
```

---

# 📖 Using Identity Operators

```python
value = None

if value is None:
    print("No Value")

elif value is not None:
    print("Value Exists")
```

---

# 📊 Summary Table

| Situation | Block Executed |
|-----------|----------------|
| First condition is True | `if` |
| First False, second True | First `elif` |
| First two False, third True | Second `elif` |
| All False | `else` |

---

# 🌍 Real-World Programs

## ATM Withdrawal

```python
balance = 3000
amount = 1500

if amount <= 0:
    print("Invalid Amount")

elif amount > balance:
    print("Insufficient Balance")

else:
    print("Withdrawal Successful")
```

---

## Login Role

```python
role = "Teacher"

if role == "Admin":
    print("Full Access")

elif role == "Teacher":
    print("Teaching Access")

elif role == "Student":
    print("Learning Access")

else:
    print("Guest Access")
```

---

## Ticket Pricing

```python
age = 10

if age < 5:
    print("Free Entry")

elif age < 18:
    print("Child Ticket")

elif age < 60:
    print("Adult Ticket")

else:
    print("Senior Citizen Ticket")
```

---

# ⚠️ Common Mistakes

## ❌ Using `else` with a Condition

Incorrect

```python
else marks >= 35:
    print("Pass")
```

Correct

```python
elif marks >= 35:
    print("Pass")
```

---

## ❌ Forgetting the Colon

Incorrect

```python
elif marks >= 80
    print("A")
```

Correct

```python
elif marks >= 80:
    print("A")
```

---

## ❌ Wrong Order of Conditions

Incorrect

```python
age = 25

if age >= 18:
    print("Adult")

elif age >= 60:
    print("Senior")
```

The second condition will never run for someone who is 60 or older because the first condition already matches.

Correct

```python
if age >= 60:
    print("Senior")

elif age >= 18:
    print("Adult")
```

---

## ❌ Multiple `else` Blocks

Incorrect

```python
if number > 0:
    print("Positive")

else:
    print("Zero")

else:
    print("Negative")
```

A single `if` statement can have **only one `else`**.

---

# 💡 Best Practices

- Arrange conditions from **most specific** to **least specific**.
- Use `elif` instead of multiple separate `if` statements when only one outcome should occur.
- Keep conditions readable.
- Use meaningful variable names.

---

# 🚀 Pro Tips

Use `if...elif...else` for:

- Grade calculators
- Menu-driven applications
- Login systems
- Weather applications
- ATM software
- E-commerce discounts
- Role-based access control

---

# ❓ Interview Questions

- [ ] What is the difference between `if...else` and `if...elif...else`?
- [ ] How many `elif` blocks can a program have?
- [ ] Can there be more than one `else` block?
- [ ] Why does the order of conditions matter?
- [ ] Does Python check all `elif` conditions?

---

# 🏋️ Practice Programs

## Easy

```python
number = -5

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")
```

---

```python
day = "Sunday"

if day == "Monday":
    print("Start of Week")

elif day == "Sunday":
    print("Holiday")

else:
    print("Working Day")
```

---

## Medium

```python
marks = 88

if marks >= 90:
    print("A+")

elif marks >= 80:
    print("A")

elif marks >= 70:
    print("B")

else:
    print("Needs Improvement")
```

---

```python
temperature = 15

if temperature > 35:
    print("Hot")

elif temperature >= 20:
    print("Pleasant")

else:
    print("Cold")
```

---

## Advanced

```python
username = "admin"
password = "python123"

if username != "admin":
    print("Invalid Username")

elif password != "python123":
    print("Incorrect Password")

else:
    print("Login Successful")
```

---

# 🎯 Challenge

Write a program that:

1. Takes a student's marks as input.
2. Prints:

- `A+` for marks **90–100**
- `A` for marks **80–89**
- `B` for marks **70–79**
- `C` for marks **60–69**
- `Pass` for marks **35–59**
- `Fail` for marks **below 35**

---

# 📝 Assignment

- [x] Create a grade calculator.
- [x] Create a weather suggestion program.
- [x] Create a ticket price calculator based on age.
- [x] Create a role-based login system.
- [x] Create a temperature classification program.

---

# 📚 Summary

You learned:

- ✅ What `if...elif...else` is.
- ✅ How Python checks multiple conditions.
- ✅ Why the order of conditions matters.
- ✅ Using logical, membership, and identity operators.
- ✅ Real-world applications.
- ✅ Common mistakes and best practices.

Remember:

- `if` → First condition
- `elif` → Additional conditions
- `else` → Runs only if all previous conditions are `False`
- Python executes **only the first matching block**.

---

# 🎯 Topic Completion Checklist

- [x] I understand `if...elif...else`.
- [x] I know how Python checks multiple conditions.
- [x] I understand why condition order matters.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 4 – Topic 4: Nested `if` Statement**