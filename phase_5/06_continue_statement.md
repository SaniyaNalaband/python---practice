# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 6:** `continue` Statement

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `continue` statement is.
- [ ] Learn how `continue` works.
- [ ] Use `continue` with `while` loops.
- [ ] Use `continue` with `for` loops.
- [ ] Understand the difference between `continue` and `break`.
- [ ] Solve real-world problems using `continue`.

---

# 📖 What is the `continue` Statement?

The **`continue`** statement is used to **skip the remaining code of the current iteration** and immediately move to the **next iteration** of the loop.

Unlike `break`, **`continue` does not stop the loop**. It only skips the current iteration.

---

# 🤔 Why Do We Need `continue`?

Sometimes we want to ignore certain values but continue processing the remaining ones.

Examples:

- Skip negative numbers.
- Skip vowels while processing a word.
- Skip weekends while processing workdays.
- Ignore invalid user input and continue asking.

The `continue` statement makes this easy.

---

# 📖 Syntax

```python
continue
```

Usually used inside an `if` statement.

```python
for item in iterable:

    if condition:
        continue

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
    Is continue Executed?
        │            │
      Yes           No
        │            │
        ▼            ▼
Skip Remaining     Execute
Current Iteration  Remaining Code
        │            │
        └──────┬─────┘
               ▼
        Next Iteration
```

---

# 📖 Example 1: Skip a Number in a `for` Loop

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

Output

```text
1
2
4
5
```

The number `3` is skipped.

---

# 📖 Example 2: Skip Even Numbers

```python
for i in range(1, 11):

    if i % 2 == 0:
        continue

    print(i)
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

# 📖 Example 3: Skip Vowels

```python
word = "Education"

for ch in word:

    if ch.lower() in "aeiou":
        continue

    print(ch)
```

Output

```text
d
c
t
n
```

---

# 📖 Example 4: `continue` in a `while` Loop

```python
count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)
```

Output

```text
1
2
4
5
```

### Why is `count += 1` before `continue`?

If you write:

```python
count = 0

while count < 5:

    if count == 3:
        continue

    count += 1
    print(count)
```

The loop becomes infinite when `count` is `3`, because `count` never changes after `continue`.

---

# 📖 Example 5: Skip a Specific Fruit

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:

    if fruit == "Mango":
        continue

    print(fruit)
```

Output

```text
Apple
Banana
Orange
```

---

# 📖 `continue` in Nested Loops

```python
for i in range(1, 4):

    for j in range(1, 4):

        if j == 2:
            continue

        print(i, j)
```

Output

```text
1 1
1 3
2 1
2 3
3 1
3 3
```

The value `2` is skipped only in the **inner loop**.

---

# 📊 Trace Table

Program

```python
for i in range(1, 6):

    if i == 3:
        continue

    print(i)
```

| Iteration | `i` | `i == 3` | Output |
|-----------|----:|----------|--------|
| 1 | 1 | False | 1 |
| 2 | 2 | False | 2 |
| 3 | 3 | True | Skipped |
| 4 | 4 | False | 4 |
| 5 | 5 | False | 5 |

---

# 📊 `break` vs `continue`

| Feature | `break` | `continue` |
|----------|---------|------------|
| Stops the loop | ✅ Yes | ❌ No |
| Skips current iteration | ❌ No | ✅ Yes |
| Moves to next iteration | ❌ No | ✅ Yes |
| Exits loop immediately | ✅ Yes | ❌ No |

---

# 🌍 Real-World Examples

## Skip Absent Students

```python
students = ["Rahul", "Absent", "Saniya", "Aisha"]

for student in students:

    if student == "Absent":
        continue

    print(student)
```

---

## Skip Invalid Marks

```python
marks = [95, -1, 88, 76, -1, 91]

for mark in marks:

    if mark == -1:
        continue

    print(mark)
```

---

## Skip Empty Inputs

```python
names = ["Rahul", "", "Saniya", "Aisha"]

for name in names:

    if name == "":
        continue

    print(name)
```

---

## Skip Divisible by 5

```python
for i in range(1, 21):

    if i % 5 == 0:
        continue

    print(i)
```

---

# ⚠️ Common Mistakes

## ❌ Using `continue` Outside a Loop

Incorrect

```python
continue
```

Output

```text
SyntaxError: 'continue' not properly in loop
```

---

## ❌ Forgetting to Update Variables in a `while` Loop

Incorrect

```python
count = 0

while count < 5:

    if count == 3:
        continue

    count += 1
```

Infinite loop.

Correct

```python
count = 0

while count < 5:

    count += 1

    if count == 3:
        continue

    print(count)
```

---

## ❌ Confusing `break` and `continue`

Incorrect expectation:

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

This does **not** stop the loop. It only skips printing `2`.

---

# 💡 Best Practices

- Use `continue` only when skipping specific iterations.
- Ensure loop variables are updated before `continue` in `while` loops.
- Keep conditions simple and readable.
- Don't overuse `continue`, as it can make code harder to follow.

---

# 🚀 Pro Tips

The `continue` statement is commonly used in:

- Data filtering
- Input validation
- File processing
- Web scraping
- Data cleaning
- Machine learning preprocessing

---

# ❓ Interview Questions

- [ ] What is the purpose of the `continue` statement?
- [ ] What is the difference between `break` and `continue`?
- [ ] Can `continue` be used in both `for` and `while` loops?
- [ ] Why should you be careful when using `continue` in a `while` loop?
- [ ] What happens when `continue` is used inside nested loops?

---

# 🏋️ Practice Programs

## Easy

```python
for i in range(1, 11):

    if i == 5:
        continue

    print(i)
```

---

```python
for i in range(1, 21):

    if i % 2 == 0:
        continue

    print(i)
```

---

## Medium

```python
word = "Programming"

for ch in word:

    if ch.lower() in "aeiou":
        continue

    print(ch)
```

---

```python
numbers = [10, -5, 20, -8, 15]

for num in numbers:

    if num < 0:
        continue

    print(num)
```

---

## Advanced

```python
marks = [95, -1, 88, -1, 76, 100]

total = 0

for mark in marks:

    if mark == -1:
        continue

    total += mark

print("Total =", total)
```

---

```python
count = 0

while count < 10:

    count += 1

    if count % 3 == 0:
        continue

    print(count)
```

---

# 🎯 Challenge

Write a program that:

1. Prints numbers from **1 to 30**.
2. Skips all numbers divisible by **4**.

Expected Output

```text
1
2
3
5
6
7
9
10
11
...
```

---

# 📝 Assignment

- [x] Print numbers from 1 to 50, skipping multiples of 5.
- [ x] Print only consonants from a word.
- [x] Print positive numbers from a list.
- [x] Calculate the sum of positive numbers in a list (ignore negatives).
- [x] Print numbers from 1 to 100, skipping numbers divisible by both 2 and 3.

---

# 📚 Summary

You learned:

- ✅ What the `continue` statement is.
- ✅ How `continue` works.
- ✅ How to use `continue` in `for` and `while` loops.
- ✅ The difference between `break` and `continue`.
- ✅ Common mistakes and best practices.

Remember:

- `continue` **does not stop the loop**.
- It **skips only the current iteration** and moves to the next one.
- In a `while` loop, always update the loop variable before using `continue` to avoid infinite loops.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `continue` statement.
- [x] I know the difference between `break` and `continue`.
- [x] I can use `continue` in `for` loops.
- [x] I can use `continue` in `while` loops.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 7: `pass` Statement**