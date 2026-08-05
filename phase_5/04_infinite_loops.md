# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 4:** Infinite Loops

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what an infinite loop is.
- [ ] Learn why infinite loops occur.
- [ ] Identify common causes of infinite loops.
- [ ] Learn how to stop an infinite loop.
- [ ] Understand real-world uses of infinite loops.
- [ ] Avoid writing accidental infinite loops.

---

# 📖 What is an Infinite Loop?

An **Infinite Loop** is a loop that **never stops executing** because its condition always remains **`True`**.

The program continues running until it is manually stopped or interrupted.

---

# 🤔 Why Do Infinite Loops Happen?

An infinite loop usually occurs because:

- The loop condition never becomes `False`.
- The loop variable is never updated.
- The condition is always `True`.
- The wrong variable is updated.
- The loop has no exit condition.

---

# 📖 Syntax

```python
while True:
    # Code
```

or

```python
while condition:
    # Condition never becomes False
```

---

# 🔄 Flow of Execution

```text
          Start
             │
             ▼
     Check Condition
             │
             ▼
          True
             │
             ▼
      Execute Code
             │
             ▼
      Go Back Again
             │
             └────────────►
```

Since the condition never becomes **False**, the loop repeats forever.

---

# 📖 Example 1: `while True`

```python
while True:
    print("Hello")
```

Output

```text
Hello
Hello
Hello
Hello
...
```

The loop never ends because `True` is always `True`.

---

# 📖 Example 2: Variable Never Changes

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

### Why?

- `count` starts at `1`.
- `count <= 5` is `True`.
- `count` is never updated.
- The condition never becomes `False`.

---

# 📖 Example 3: Wrong Update

```python
x = 1
y = 1

while x <= 5:
    print(x)
    y += 1
```

Output

```text
1
1
1
1
...
```

### Why?

`x` controls the loop, but only `y` is updated.

---

# 📖 Example 4: Always True Condition

```python
while 10 > 5:
    print("Python")
```

Output

```text
Python
Python
Python
...
```

Since `10 > 5` is always `True`, the loop never stops.

---

# 📖 Example 5: Incorrect Condition

```python
num = 5

while num != 10:
    print(num)
    num -= 1
```

Output

```text
5
4
3
2
1
0
-1
-2
...
```

### Why?

`num` keeps decreasing and will **never become `10`**.

---

# 📖 Correct Version

```python
num = 5

while num != 10:
    print(num)
    num += 1
```

Output

```text
5
6
7
8
9
```

---

# 📖 How to Stop an Infinite Loop

## Method 1: Update the Loop Variable

Incorrect

```python
count = 1

while count <= 5:
    print(count)
```

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Method 2: Use `break`

```python
while True:
    name = input("Enter your name: ")

    if name == "exit":
        break

    print(name)
```

Example

```text
Enter your name: Rahul
Rahul

Enter your name: Saniya
Saniya

Enter your name: exit
```

The loop stops when `break` is executed.

---

## Method 3: Change the Condition

Incorrect

```python
while True:
    print("Running")
```

Correct

```python
running = True

while running:
    print("Running")
    running = False
```

Output

```text
Running
```

---

# 🌍 Real-World Uses of Infinite Loops

Infinite loops are **not always mistakes**. They are useful when a program should keep running until something tells it to stop.

---

## ATM Machine

```python
while True:
    print("1. Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "3":
        break
```

---

## Game Loop

```python
while True:
    print("Game Running")

    command = input("Continue? (yes/no): ")

    if command == "no":
        break
```

---

## Login System

```python
while True:

    password = input("Password: ")

    if password == "python123":
        print("Access Granted")
        break
```

---

## Chat Application

```python
while True:

    message = input("> ")

    if message == "quit":
        break

    print(message)
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting to Update the Variable

```python
count = 1

while count <= 5:
    print(count)
```

Infinite loop.

---

## ❌ Wrong Variable Updated

```python
x = 1
y = 1

while x <= 5:
    y += 1
```

`x` never changes.

---

## ❌ Always True Condition

```python
while 100 > 10:
    print("Hello")
```

Runs forever.

---

## ❌ Forgetting `break`

```python
while True:
    print("Running")
```

No exit condition.

---

# 💡 Best Practices

- Always ensure the loop condition can become `False`.
- Update the correct loop variable.
- Use `break` when appropriate.
- Test loops with small values first.
- Avoid `while True` unless you have a clear exit strategy.

---

# 🚀 Pro Tips

Infinite loops are used in:

- Video games
- ATM software
- Operating systems
- Servers
- Web applications
- Robotics
- Chat applications
- IoT devices
- Embedded systems

---

# ❓ Interview Questions

- [ ] What is an infinite loop?
- [ ] Why do infinite loops occur?
- [ ] How can you stop an infinite loop?
- [ ] Is `while True` always bad?
- [ ] Give two real-world uses of infinite loops.

---

# 🏋️ Practice Programs

## Easy

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

```python
while True:
    print("Python")
    break
```

---

## Medium

```python
while True:

    number = int(input("Enter a positive number: "))

    if number > 0:
        break

print("Thank You")
```

---

```python
while True:

    text = input("Type exit to stop: ")

    if text == "exit":
        break
```

---

## Advanced

```python
secret = "python"

while True:

    password = input("Password: ")

    if password == secret:
        print("Welcome!")
        break

    print("Wrong Password")
```

---

```python
balance = 1000

while True:

    print("\n1. Check Balance")
    print("2. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("Balance =", balance)

    elif choice == "2":
        break
```

---

# 🎯 Challenge

Write a program that:

1. Continuously asks the user to enter a number.
2. Stops only when the user enters **0**.
3. Prints every number entered before stopping.

Example

```text
Enter a number: 5
You entered: 5

Enter a number: 12
You entered: 12

Enter a number: 0
Program Ended
```

---

# 📝 Assignment

- [ ] Create a menu-driven program using `while True`.
- [ ] Create a login system that keeps asking until the correct password is entered.
- [ ] Create a number guessing loop that stops when the correct number is guessed.
- [ ] Create a simple calculator that continues until the user chooses to exit.

---

# 📚 Summary

You learned:

- ✅ What an infinite loop is.
- ✅ Why infinite loops occur.
- ✅ Common causes of accidental infinite loops.
- ✅ How to stop an infinite loop using variable updates or `break`.
- ✅ Real-world applications where infinite loops are useful.

Remember:

- An infinite loop is a loop whose condition never becomes `False`.
- Infinite loops are **useful when designed intentionally**, but accidental infinite loops are common beginner mistakes.
- Always ensure your loop has a valid exit condition.

---

# 🎯 Topic Completion Checklist

- [ ] I understand what an infinite loop is.
- [ ] I know why infinite loops happen.
- [ ] I can identify accidental infinite loops.
- [ ] I know how to stop an infinite loop.
- [ ] I completed the practice programs.
- [ ] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 5: `break` Statement**