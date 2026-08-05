# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 3:** Nested Loops

**Difficulty:** ⭐⭐ Intermediate → ⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what nested loops are.
- [ ] Learn how nested loops work.
- [ ] Write nested `for` loops.
- [ ] Write nested `while` loops.
- [ ] Combine `for` and `while` loops.
- [ ] Solve pattern-printing problems.
- [ ] Solve real-world problems using nested loops.

---

# 📖 What is a Nested Loop?

A **Nested Loop** is a **loop inside another loop**.

- The outer loop controls how many times the inner loop runs.
- For every one iteration of the outer loop, the inner loop completes all of its iterations.

---

# 🤔 Why Do We Need Nested Loops?

Nested loops are useful when working with:

- Tables
- Matrices
- Patterns
- 2D Lists
- Games
- Coordinates
- Grid-based problems

---

# 📖 Syntax

## Nested `for` Loop

```python
for outer in iterable1:
    for inner in iterable2:
        # Code
```

---

## Nested `while` Loop

```python
while condition1:

    while condition2:
        # Code

    # Update outer loop
```

---

## `for` Inside `while`

```python
while condition:
    for item in iterable:
        print(item)
```

---

## `while` Inside `for`

```python
for item in iterable:

    while condition:
        print(item)
```

---

# 🔄 Flow of Execution

```text
Start
   │
   ▼
Outer Loop Starts
   │
   ▼
Inner Loop Starts
   │
   ▼
Inner Loop Completes
   │
   ▼
Outer Loop Moves to Next Iteration
   │
   ▼
Inner Loop Runs Again
   │
   ▼
Outer Loop Ends
```

---

# 📖 How Does a Nested Loop Work?

Example

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

### Execution

Outer Loop = 1

```text
(1,1)
(1,2)
(1,3)
```

Outer Loop = 2

```text
(2,1)
(2,2)
(2,3)
```

Outer Loop = 3

```text
(3,1)
(3,2)
(3,3)
```

---

# 📊 Trace Table

Program

```python
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)
```

| Outer (`i`) | Inner (`j`) | Output |
|-------------|-------------|---------|
| 1 | 1 | 1 1 |
| 1 | 2 | 1 2 |
| 1 | 3 | 1 3 |
| 2 | 1 | 2 1 |
| 2 | 2 | 2 2 |
| 2 | 3 | 2 3 |

---

# 1️⃣ Nested `for` Loop

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Output

```text
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

# 2️⃣ Nested `while` Loop

```python
i = 1

while i <= 3:

    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1
```

Output

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

---

# 3️⃣ `for` Inside `while`

```python
i = 1

while i <= 3:

    for j in range(1, 4):
        print(i, j)

    i += 1
```

---

# 4️⃣ `while` Inside `for`

```python
for i in range(1, 4):

    j = 1

    while j <= 3:
        print(i, j)
        j += 1
```

---

# 📖 Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
```

Output

```text
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
```

---

# 📖 Pattern Printing

## Square Pattern

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
```

Output

```text
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

---

## Right Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output

```text
*
* *
* * *
* * * *
* * * * *
```

---

## Number Triangle

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

Output

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## Repeated Number Pattern

```python
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
```

Output

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

# 🌍 Real-World Programs

## Seating Arrangement

```python
for row in range(1, 4):
    for seat in range(1, 6):
        print(f"Row {row} Seat {seat}")
```

---

## Chessboard Coordinates

```python
for row in range(1, 9):
    for col in range(1, 9):
        print(f"({row},{col})", end=" ")
    print()
```

---

## Student Marks

```python
students = ["Rahul", "Aisha"]

subjects = ["Math", "Science", "English"]

for student in students:
    for subject in subjects:
        print(student, "-", subject)
```

---

## Times Tables (1 to 3)

```python
for table in range(1, 4):
    print(f"\nTable of {table}")

    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting to Reset the Inner Loop Variable

Incorrect

```python
i = 1
j = 1

while i <= 3:
    while j <= 3:
        print(i, j)
        j += 1
    i += 1
```

`j` is never reset, so the inner loop only runs during the first outer iteration.

Correct

```python
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1
```

---

## ❌ Wrong Indentation

Incorrect

```python
for i in range(3):
for j in range(3):
    print(i, j)
```

Correct

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

## ❌ Missing `print()` for a New Line

Incorrect

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")
```

Correct

```python
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
```

---

# 💡 Best Practices

- Keep nesting levels as low as possible.
- Use meaningful variable names (`row`, `col`).
- Reset inner loop variables when using nested `while` loops.
- Use nested loops mainly for 2D data and pattern problems.

---

# 🚀 Pro Tips

Nested loops are commonly used in:

- Matrix operations
- Data science
- Image processing
- Pattern printing
- Game development
- Sudoku solvers
- Chess programs
- Spreadsheet processing

---

# ❓ Interview Questions

- [ ] What is a nested loop?
- [ ] How many times does the inner loop execute?
- [ ] Can you nest `while` inside `for`?
- [ ] What happens if you don't reset the inner `while` loop variable?
- [ ] Name some real-world applications of nested loops.

---

# 🏋️ Practice Programs

## Easy

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

```python
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
```

---

## Medium

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
```

---

## Advanced

```python
for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()
```

---

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3}", end=" ")
    print()
```

---

# 🎯 Challenge

Write a program that prints the following pattern:

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

Then modify it to print:

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

# 📝 Assignment

- [x] Print a 5 × 5 square of `*`.
- [x] Print a right triangle of `*`.
- [x] Print a number triangle.
- [x] Print multiplication tables from 1 to 5.
- [x] Print all coordinate pairs from `(1,1)` to `(5,5)`.
- [x] Create a seating chart with 3 rows and 5 seats.

---

# 📚 Summary

You learned:

- ✅ What nested loops are.
- ✅ How nested `for` and `while` loops work.
- ✅ How to combine `for` and `while` loops.
- ✅ Pattern printing with nested loops.
- ✅ Real-world applications.
- ✅ Common mistakes and best practices.

Remember:

- A nested loop is **a loop inside another loop**.
- The **inner loop completes all its iterations** for **every single iteration** of the outer loop.
- Nested loops are especially useful for working with **2D data, grids, tables, and patterns**.

---

# 🎯 Topic Completion Checklist

- [x] I understand nested loops.
- [x] I can write nested `for` loops.
- [x] I can write nested `while` loops.
- [x] I can print basic patterns.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 4: Infinite Loops**