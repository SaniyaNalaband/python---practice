# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 5:** `break` Statement

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `break` statement is.
- [ ] Learn how `break` works.
- [ ] Use `break` with `while` loops.
- [ ] Use `break` with `for` loops.
- [ ] Use `break` inside nested loops.
- [ ] Solve real-world problems using `break`.

---

# 📖 What is the `break` Statement?

The **`break`** statement is used to **immediately terminate (exit) a loop**, even if the loop condition is still `True` or there are more iterations remaining.

Once Python encounters a `break` statement:

- The current loop stops immediately.
- Control moves to the first statement after the loop.

---

# 🤔 Why Do We Need `break`?

Sometimes we don't want a loop to continue until its natural end.

For example:

- Stop searching when an item is found.
- Exit a menu when the user chooses "Exit".
- Stop taking input after receiving valid data.
- End a game when the player quits.

The `break` statement allows us to exit the loop early.

---

# 📖 Syntax

```python
break
```

Usually used inside an `if` statement.

```python
while condition:

    if condition_to_stop:
        break

    # Remaining code
```

---

# 🔄 Flow of Execution

```text
          Start
             │
             ▼
      Loop Starts
             │
             ▼
      Execute Code
             │
             ▼
    Is break Executed?
        │          │
      Yes         No
        │          │
        ▼          ▼
 Exit the Loop   Next Iteration
        │
        ▼
 Continue Program
```

---

# 📖 Example 1: `break` in a `while` Loop

```python
count = 1

while True:
    print(count)

    if count == 5:
        break

    count += 1

print("Loop Ended")
```

Output

```text
1
2
3
4
5
Loop Ended
```

---

# 📖 Example 2: `break` in a `for` Loop

```python
for i in range(1, 11):

    if i == 6:
        break

    print(i)
```

Output

```text
1
2
3
4
5
```

The loop stops before printing `6`.

---

# 📖 Example 3: Stop When a Number is Found

```python
numbers = [10, 20, 35, 40, 50]

for num in numbers:

    if num == 35:
        print("Found!")
        break

    print(num)
```

Output

```text
10
20
Found!
```

---

# 📖 Example 4: Exit on User Input

```python
while True:

    text = input("Enter something (type 'exit' to quit): ")

    if text == "exit":
        break

    print("You entered:", text)

print("Program Ended")
```

---

# 📖 Example 5: Searching a List

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

search = "Mango"

for fruit in fruits:

    if fruit == search:
        print("Fruit Found")
        break
```

Output

```text
Fruit Found
```

---

# 📖 `break` in Nested Loops

```python
for i in range(1, 4):

    for j in range(1, 4):

        if j == 2:
            break

        print(i, j)
```

Output

```text
1 1
2 1
3 1
```

### Important

The `break` statement only exits the **innermost loop**.

The outer loop continues running.

---

# 📊 Trace Table

Program

```python
for i in range(1, 6):

    if i == 4:
        break

    print(i)
```

| Iteration | `i` | `i == 4` | Output |
|-----------|----:|----------|--------|
| 1 | 1 | False | 1 |
| 2 | 2 | False | 2 |
| 3 | 3 | False | 3 |
| 4 | 4 | True | Loop Ends |

---

# 🌍 Real-World Examples

## Login System

```python
correct_password = "python123"

while True:

    password = input("Enter Password: ")

    if password == correct_password:
        print("Login Successful")
        break

    print("Wrong Password")
```

---

## ATM Menu

```python
while True:

    print("1. Balance")
    print("2. Exit")

    choice = input("Choice: ")

    if choice == "2":
        break
```

---

## Guess the Number

```python
secret = 7

while True:

    guess = int(input("Guess: "))

    if guess == secret:
        print("Correct!")
        break
```

---

## Stop Reading Data

```python
for number in [5, 10, 15, 20, 25]:

    if number == 20:
        break

    print(number)
```

Output

```text
5
10
15
```

---

# ⚠️ Common Mistakes

## ❌ Using `break` Outside a Loop

Incorrect

```python
break
```

Output

```text
SyntaxError: 'break' outside loop
```

---

## ❌ Assuming `break` Stops All Nested Loops

```python
for i in range(3):

    for j in range(3):
        break

    print(i)
```

Only the inner loop stops.

---

## ❌ Writing Code After `break` in the Same Block

```python
for i in range(5):

    break

    print(i)
```

`print(i)` is never executed because `break` exits the loop immediately.

---

# 💡 Best Practices

- Use `break` only when an early exit is needed.
- Avoid unnecessary `break` statements.
- Write clear exit conditions.
- Keep loop logic simple and readable.

---

# 🚀 Pro Tips

The `break` statement is commonly used in:

- Search algorithms
- Login systems
- Menu-driven programs
- Games
- File processing
- Data validation
- Input loops

---

# ❓ Interview Questions

- [ ] What is the purpose of the `break` statement?
- [ ] Can `break` be used in both `for` and `while` loops?
- [ ] What happens when `break` is executed?
- [ ] Can `break` be used outside a loop?
- [ ] What happens when `break` is used inside nested loops?

---

# 🏋️ Practice Programs

## Easy

```python
for i in range(1, 11):

    if i == 5:
        break

    print(i)
```

---

```python
count = 1

while True:

    print(count)

    if count == 3:
        break

    count += 1
```

---

## Medium

```python
numbers = [12, 45, 67, 89, 100]

for num in numbers:

    if num == 67:
        print("Found")
        break
```

---

```python
while True:

    age = int(input("Enter age: "))

    if age >= 18:
        print("Eligible")
        break

    print("Try Again")
```

---

## Advanced

```python
secret = 25

while True:

    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct Guess!")
        break

    elif guess < secret:
        print("Too Small")

    else:
        print("Too Large")
```

---

```python
students = ["Rahul", "Aisha", "Saniya", "Rohan"]

for student in students:

    if student == "Saniya":
        print("Student Found")
        break

    print(student)
```

---

# 🎯 Challenge

Write a program that:

1. Continuously asks the user to enter a password.
2. Stops only when the correct password is entered.
3. Prints **"Access Granted"** before exiting the loop.

Example

```text
Enter Password: abc
Wrong Password

Enter Password: 123
Wrong Password

Enter Password: python123
Access Granted
```

---

# 📝 Assignment

- [x] Print numbers from 1 to 20 but stop at 10.
- [x] Search for a name in a list and stop when found.
- [x] Create a login system using `break`.
- [x] Create a menu-driven program that exits when the user selects "Exit".
- [x] Guess-the-number game using `break`.

---

# 📚 Summary

You learned:

- ✅ What the `break` statement is.
- ✅ How `break` works.
- ✅ How to use `break` with `for` and `while` loops.
- ✅ How `break` behaves in nested loops.
- ✅ Common mistakes and best practices.

Remember:

- `break` immediately terminates the **current loop**.
- It works in both `for` and `while` loops.
- In nested loops, it exits **only the innermost loop**.
- Use `break` when you need to stop a loop before it finishes naturally.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `break` statement.
- [x] I can use `break` in `for` loops.
- [x] I can use `break` in `while` loops.
- [x] I understand how `break` works in nested loops.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 6: `continue` Statement**