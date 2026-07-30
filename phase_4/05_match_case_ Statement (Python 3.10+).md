# 🐍 Python Master Course

> **Phase 4:** Control Flow (Decision Making)  
> **Topic 5:** `match...case` Statement (Python 3.10+)

**Difficulty:** ⭐⭐⭐ Intermediate

> **Available from:** Python **3.10 and later**

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `match...case` statement is.
- [ ] Write cleaner code using `match...case`.
- [ ] Understand how pattern matching works.
- [ ] Know when to use `match...case` instead of `if...elif...else`.   
- [ ] Solve real-world problems using `match...case`.

---

# 📖 What is `match...case`?

The `match...case` statement is Python's **pattern matching** feature.

It allows you to compare **one value** against **multiple possible cases**.

It works similarly to the **switch-case statement** found in languages like Java, C++, and C#.

Instead of writing many `elif` conditions, you can write cleaner and more readable code.

---

# 🧠 Syntax

```python
match expression:

    case value1:
        # Code

    case value2:
        # Code

    case value3:
        # Code

    case _:
        # Default block
```

---

# 🔍 Syntax Breakdown

```python
day = 2

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case _:
        print("Invalid Day")
```

| Keyword | Meaning |
|----------|---------|
| `match` | Starts pattern matching |
| `case` | One possible value |
| `_` | Default case (similar to `else`) |

---

# 🔄 Flow of Execution

```text
               Start
                  │
                  ▼
         Evaluate Expression
                  │
        ┌─────────┴─────────┐
        │                   │
     Matches?            No Match
        │                   │
        ▼                   ▼
 Execute Matching      Check Next Case
     Case Block              │
                             ▼
                    Repeat Until Found
                             │
                             ▼
                     case _ (Default)
```

---

# 📖 How Does It Work?

Python follows these steps:

1. Evaluate the expression after `match`.
2. Compare it with the first `case`.
3. If it matches, execute that block.
4. Stop checking the remaining cases.
5. If nothing matches, execute `case _:` if it exists.

---

# 1️⃣ Basic Example

```python
day = 1

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid Day")
```

Output

```text
Monday
```

---

# 2️⃣ Month Example

```python
month = 4

match month:

    case 1:
        print("January")

    case 2:
        print("February")

    case 3:
        print("March")

    case 4:
        print("April")

    case _:
        print("Invalid Month")
```

Output

```text
April
```

---

# 3️⃣ Grade Example

```python
grade = "A"

match grade:

    case "A":
        print("Excellent")

    case "B":
        print("Very Good")

    case "C":
        print("Good")

    case "D":
        print("Pass")

    case _:
        print("Fail")
```

Output

```text
Excellent
```

---

# 4️⃣ Calculator Example

```python
operator = "+"

match operator:

    case "+":
        print(20 + 10)

    case "-":
        print(20 - 10)

    case "*":
        print(20 * 10)

    case "/":
        print(20 / 10)

    case _:
        print("Invalid Operator")
```

Output

```text
30
```

---

# 5️⃣ Menu Program

```python
choice = 2

match choice:

    case 1:
        print("Add Student")

    case 2:
        print("Delete Student")

    case 3:
        print("Update Student")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")
```

Output

```text
Delete Student
```

---

# 📖 Multiple Values in One Case

You can match multiple values using the `|` (OR) operator.

```python
day = "Saturday"

match day:

    case "Saturday" | "Sunday":
        print("Weekend")

    case _:
        print("Weekday")
```

Output

```text
Weekend
```

---

# 📖 Matching Boolean Values

```python
status = True

match status:

    case True:
        print("Login Successful")

    case False:
        print("Login Failed")
```

Output

```text
Login Successful
```

---

# 📖 Matching Strings

```python
language = "Python"

match language:

    case "Python":
        print("Programming Language")

    case "HTML":
        print("Markup Language")

    case _:
        print("Unknown")
```

Output

```text
Programming Language
```

---

# 📖 Matching Numbers

```python
number = 100

match number:

    case 50:
        print("Fifty")

    case 100:
        print("Hundred")

    case _:
        print("Other Number")
```

Output

```text
Hundred
```

---

# 📖 `case _` (Default Case)

`case _:` works like the `else` block in an `if...elif...else` statement.

Example

```python
fruit = "Orange"

match fruit:

    case "Apple":
        print("Apple")

    case "Banana":
        print("Banana")

    case _:
        print("Unknown Fruit")
``` 

Output

```text
Unknown Fruit
```

---

# 📖 `match...case` vs `if...elif...else`

## Using `if...elif...else`

```python
day = 3

if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

else:
    print("Invalid")
```

---

## Using `match...case`

```python
day = 3

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid")
```

The `match...case` version is shorter and easier to read when checking a **single value** against many options.

---

# 📖 When Should You Use `match...case`?

Use it when:

- One variable is compared against many fixed values.
- Creating menu-driven programs.
- Handling commands.
- Building calculators.
- Working with days, months, grades, or options.

Avoid it when conditions involve comparisons like:

```python
marks > 90
age >= 18
salary < 50000
```

For these, use `if...elif...else`.

---

# 📊 Summary Table

| Feature | `match...case` | `if...elif...else` |
|----------|----------------|--------------------|
| Compare one value | ✅ | ✅ |
| Compare ranges (`>`, `<`) | ❌ | ✅ |
| Cleaner for many fixed values | ✅ | ❌ |
| Default block | `case _:` | `else:` |

---

# 🌍 Real-World Programs

## ATM Menu

```python
choice = 3

match choice:

    case 1:
        print("Balance")

    case 2:
        print("Deposit")

    case 3:
        print("Withdraw")

    case 4:
        print("Exit")

    case _:
        print("Invalid Option")
```

---

## Food Ordering System

```python
food = "Pizza"

match food:

    case "Pizza":
        print("₹250")

    case "Burger":
        print("₹120")

    case "Pasta":
        print("₹180")

    case _:
        print("Item Not Available")
```

---

## Traffic Signal

```python
signal = "Green"

match signal:

    case "Green":
        print("Go")

    case "Yellow":
        print("Slow Down")

    case "Red":
        print("Stop")

    case _:
        print("Invalid Signal")
```

---

## Language Selection

```python
language = "English"

match language:

    case "English":
        print("Welcome")

    case "Hindi":
        print("स्वागत है")

    case "Kannada":
        print("ಸ್ವಾಗತ")

    case _:
        print("Language Not Supported")
```

---

# ⚠️ Common Mistakes

## ❌ Using Python Older Than 3.10

```python
match value:
```

This causes a syntax error in Python **3.9 or earlier**.

---

## ❌ Forgetting `case`

Incorrect

```python
match day:

    1:
        print("Monday")
```

Correct

```python
match day:

    case 1:
        print("Monday")
```

---

## ❌ Expecting Range Comparisons

Incorrect

```python
match marks:

    case > 90:
        print("A")
```

This is **not valid**.

Use `if...elif...else` for range checks.

---

## ❌ Forgetting the Colon

Incorrect

```python
case 1
```

Correct

```python
case 1:
```

---

# 💡 Best Practices

- Use `match...case` only when comparing **one value**.
- Always include `case _:` for unexpected values.
- Keep each case simple.
- Use meaningful case values.

---

# 🚀 Pro Tips

`match...case` is excellent for:

- Calculator menus
- ATM software
- Restaurant ordering systems
- CLI (Command-Line Interface) applications
- Game menus
- Language selection
- Configuration settings

---

# ❓ Interview Questions

- [ ] What is the `match...case` statement?
- [ ] Which Python version introduced it?
- [ ] What does `case _:` mean?
- [ ] When should you use `match...case` instead of `if...elif...else`?
- [ ] Can `match...case` directly compare ranges like `> 90`?

---

# 🏋️ Practice Programs

## Easy

```python
day = 5

match day:

    case 1:
        print("Monday")

    case 5:
        print("Friday")

    case _:
        print("Other Day")
```

---

```python
color = "Blue"

match color:

    case "Red":
        print("Stop")

    case "Blue":
        print("Sky")

    case _:
        print("Unknown")
```

---

## Medium

```python
operator = "*"

match operator:

    case "+":
        print(5 + 3)

    case "-":
        print(5 - 3)

    case "*":
        print(5 * 3)

    case "/":
        print(5 / 3)

    case _:
        print("Invalid")
```

---

```python
month = 12

match month:

    case 12 | 1 | 2:
        print("Winter")

    case 3 | 4 | 5:
        print("Summer")

    case _:
        print("Other Season")
```

---

## Advanced

```python
role = "Admin"

match role:

    case "Admin":
        print("Full Access")

    case "Teacher":
        print("Teaching Panel")

    case "Student":
        print("Student Dashboard")

    case _:
        print("Guest")
```

---

# 🎯 Challenge

Create a simple calculator.

1. Ask the user to enter:
   - First number
   - Operator (`+`, `-`, `*`, `/`)
   - Second number

2. Use `match...case` to perform the operation.

Example

```text
Enter first number: 20
Operator: *
Enter second number: 5

Result: 100
```

---

# 📝 Assignment

- [x] Create a calculator using `match...case`.
- [x] Create an ATM menu.
- [x] Create a restaurant menu.
- [x] Create a language selection program.
- [x] Create a day and month converter.

---

# 📚 Summary

You learned:

- ✅ What `match...case` is.
- ✅ How pattern matching works.
- ✅ The purpose of `case _`.
- ✅ Multiple values in a single case using `|`.
- ✅ Differences between `match...case` and `if...elif...else`.
- ✅ Real-world applications.
- ✅ Common mistakes and best practices.

Remember:

- `match...case` compares **one expression** against multiple fixed values.
- `case _:` is the default case.
- Use `if...elif...else` when checking ranges or complex conditions.

---

# 🎯 Topic Completion Checklist

- [x] I understand `match...case`.
- [x] I know when to use it.
- [x] I understand `case _`.
- [x] I know the difference between `match...case` and `if...elif...else`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 4 – Topic 6: Ternary Operator (Conditional Expression)**