# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 1:** `while` Loop

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a `while` loop is.
- [ ] Learn how a `while` loop works.
- [ ] Write programs using a `while` loop.
- [ ] Understand the importance of the loop condition.
- [ ] Solve real-world problems using `while` loops.

---

# 📖 What is a `while` Loop?

A **`while` loop** is a control flow statement that **repeatedly executes a block of code as long as a specified condition is `True`.**

Unlike a `for` loop, which iterates over a sequence, a `while` loop continues to run **until its condition becomes `False`.**

---

# 🤔 Why Do We Need a `while` Loop?

Suppose you want to print numbers from **1 to 5**.

### Without a Loop

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

This works, but it becomes impractical for large numbers.

---

### With a `while` Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```text
1
2
3
4
5
```

The `while` loop performs the repetition automatically.

---

# 📖 Syntax

```python
while condition:
    # Code Block
```

---

## General Syntax

```python
while condition:
    statement1
    statement2
```

---

# 🔍 Syntax Breakdown

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

| Part | Meaning |
|------|---------|
| `while` | Starts the loop |
| `count <= 5` | Condition to check before each iteration |
| `:` | Starts the loop block |
| `print(count)` | Executes while the condition is `True` |
| `count += 1` | Updates the loop variable |

---

# 🔄 Flow of Execution

```text
              Start
                 │
                 ▼
        Initialize Variable
                 │
                 ▼
        Check Condition
          │            │
        True         False
          │            │
          ▼            ▼
    Execute Loop      Stop
          │
          ▼
   Update Variable
          │
          └──────────────► Back to Condition
```

---

# 📖 How Does a `while` Loop Work?

Python performs these steps:

1. Initialize a variable (if required).
2. Check the condition.
3. If the condition is `True`, execute the loop body.
4. Update the variable.
5. Go back and check the condition again.
6. Repeat until the condition becomes `False`.

---

# 1️⃣ Basic Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```text
1
2
3
4
5
```

---

# 2️⃣ Printing a Message Multiple Times

```python
count = 1

while count <= 3:
    print("Welcome")
    count += 1
```

Output

```text
Welcome
Welcome
Welcome
```

---

# 3️⃣ Countdown

```python
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Blast Off!")
```

Output

```text
5
4
3
2
1
Blast Off!
```

---

# 4️⃣ Print Even Numbers

```python
number = 2

while number <= 10:
    print(number)
    number += 2
```

Output

```text
2
4
6
8
10
```

---

# 5️⃣ Print Odd Numbers

```python
number = 1

while number <= 9:
    print(number)
    number += 2
```

Output

```text
1
3
5
7
9
```

---

# 📖 Importance of Updating the Variable

Every `while` loop should update the loop variable.

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Without the update:

```python
count = 1

while count <= 5:
    print(count)
```

Output

```text
1
1
1
1
1
...
```

The condition never becomes `False`, so the loop runs forever.

---

# 📖 Loop Condition

The loop runs **only while the condition is `True`.**

Example

```python
x = 10

while x > 0:
    print(x)
    x -= 1
```

The loop stops automatically when `x` becomes `0`.

---

# 📖 Using User Input

```python
count = 1
limit = int(input("Enter a limit: "))

while count <= limit:
    print(count)
    count += 1
```

Example

```text
Enter a limit: 4

1
2
3
4
```

---

# 📊 Example Trace Table

Program

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

| Iteration | `count` Before | Condition | Output | `count` After |
|-----------|---------------:|-----------|--------|--------------:|
| 1 | 1 | True | 1 | 2 |
| 2 | 2 | True | 2 | 3 |
| 3 | 3 | True | 3 | 4 |
| 4 | 4 | False | — | Stop |

---

# 🌍 Real-World Programs

## Print Multiples of 5

```python
num = 5

while num <= 25:
    print(num)
    num += 5
```

---

## Password Attempts

```python
attempts = 1

while attempts <= 3:
    print("Attempt", attempts)
    attempts += 1
```

---

## Water Bottle Counter

```python
bottles = 5

while bottles > 0:
    print("Bottle", bottles)
    bottles -= 1

print("No Bottles Left")
```

---

## Print Squares

```python
num = 1

while num <= 5:
    print(num ** 2)
    num += 1
```

---

## Sum of First Five Numbers

```python
count = 1
total = 0

while count <= 5:
    total += count
    count += 1

print("Sum =", total)
```

Output

```text
Sum = 15
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting the Colon

Incorrect

```python
while count <= 5
    print(count)
```

Correct

```python
while count <= 5:
    print(count)
```

---

## ❌ Wrong Indentation

Incorrect

```python
while count <= 5:
print(count)
```

Output

```text
IndentationError
```

Correct

```python
while count <= 5:
    print(count)
```

---

## ❌ Forgetting to Update the Variable

Incorrect

```python
count = 1

while count <= 5:
    print(count)
```

This creates an **infinite loop** because `count` never changes.

---

## ❌ Wrong Condition

Incorrect

```python
count = 10

while count < 5:
    print(count)
```

Output

```text
(No Output)
```

The condition is `False` before the loop starts.

---

# 💡 Best Practices

- Initialize the loop variable before the loop.
- Always update the loop variable inside the loop.
- Write conditions that eventually become `False`.
- Keep the loop body simple and readable.

---

# 🚀 Pro Tips

`while` loops are commonly used for:

- Login systems
- Menu-driven programs
- ATM software
- Games
- Input validation
- Reading data until a condition is met
- Network and server programs

---

# ❓ Interview Questions

- [ ] What is a `while` loop?
- [ ] How does a `while` loop work?
- [ ] What happens if the condition is initially `False`?
- [ ] Why must the loop variable be updated?
- [ ] What is the difference between a `while` loop and a `for` loop?

---

# 🏋️ Practice Programs

## Easy

```python
count = 1

while count <= 5:
    print("Python")
    count += 1
```

---

```python
num = 1

while num <= 10:
    print(num)
    num += 1
```

---

```python
num = 10

while num >= 1:
    print(num)
    num -= 1
```

---

## Medium

```python
num = 2

while num <= 20:
    print(num)
    num += 2
```

---

```python
count = 1

while count <= 5:
    print(count ** 2)
    count += 1
```

---

```python
total = 0
count = 1

while count <= 10:
    total += count
    count += 1

print(total)
```

---

## Advanced

```python
number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reversed Number:", reverse)
```

---

```python
password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted")
```

---

# 🎯 Challenge

Write a program that:

1. Takes a number `n` from the user.
2. Uses a `while` loop to print the multiplication table of `n` from `1` to `10`.

Example

```text
Enter a number: 7

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

# 📝 Assignment

- [x] Print numbers from 1 to 20.
- [x] Print numbers from 20 to 1.
- [x] Print even numbers from 2 to 50.
- [x] Print odd numbers from 1 to 49.
- [x] Find the sum of the first 100 natural numbers.
- [x] Print the multiplication table of a given number.

---

# 📚 Summary

You learned:

- ✅ What a `while` loop is.
- ✅ How it works.
- ✅ The importance of the loop condition.
- ✅ Why updating the loop variable is necessary.
- ✅ Real-world uses of `while` loops.
- ✅ Common mistakes and best practices.

Remember:

- A `while` loop repeats **as long as the condition is `True`.**
- Always update the loop variable to avoid infinite loops.
- `while` loops are best when the number of iterations is **not known in advance**.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `while` loop.
- [x] I know how it works.
- [x] I can write `while` loop programs.
- [x] I understand why the loop variable must be updated.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 2: `for` Loop**