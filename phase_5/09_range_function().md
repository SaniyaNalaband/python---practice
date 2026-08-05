# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 9:** `range()` Function

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `range()` function is.
- [ ] Learn the different forms of `range()`.
- [ ] Use `range()` with `for` loops.
- [ ] Generate increasing and decreasing sequences.
- [ ] Use positive and negative step values.
- [ ] Solve real-world problems using `range()`.

---

# 📖 What is the `range()` Function?

The **`range()`** function is a built-in Python function used to generate a **sequence of numbers**.

It is most commonly used with **`for` loops** to repeat an action a specific number of times.

> **Important:** `range()` generates numbers **one at a time** (it does not create a list automatically in Python 3).

---

# 🤔 Why Do We Need `range()`?

Without `range()`, we would have to manually write every number.

### Without `range()`

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

### With `range()`

```python
for i in range(1, 6):
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

Much shorter and easier to maintain.

---

# 📖 Syntax

## 1. One Argument

```python
range(stop)
```

---

## 2. Two Arguments

```python
range(start, stop)
```

---

## 3. Three Arguments

```python
range(start, stop, step)
```

---

# 📖 Parameters

| Parameter | Description |
|-----------|-------------|
| `start` | Starting number (default is `0`) |
| `stop` | Ending value (**not included**) |
| `step` | Difference between each number (default is `1`) |

---

# ⭐ Rule to Remember

> The **`stop` value is never included**.

Example

```python
range(1, 6)
```

Generates:

```text
1 2 3 4 5
```

The number `6` is **not** included.

---

# 📖 Form 1: `range(stop)`

Starts from `0` and goes up to `stop - 1`.

```python
for i in range(5):
    print(i)
```

Output

```text
0
1
2
3
4
```

Equivalent sequence:

```text
0 → 1 → 2 → 3 → 4
```

---

# 📖 Form 2: `range(start, stop)`

Starts from `start` and ends before `stop`.

```python
for i in range(3, 8):
    print(i)
```

Output

```text
3
4
5
6
7
```

---

# 📖 Form 3: `range(start, stop, step)`

Moves according to the `step` value.

```python
for i in range(2, 11, 2):
    print(i)
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

# 📖 Positive Step

```python
for i in range(1, 11, 3):
    print(i)
```

Output

```text
1
4
7
10
```

---

# 📖 Negative Step (Counting Backwards)

```python
for i in range(10, 0, -1):
    print(i)
```

Output

```text
10
9
8
7
6
5
4
3
2
1
```

---

# 📖 Reverse Counting by 2

```python
for i in range(20, 0, -2):
    print(i)
```

Output

```text
20
18
16
14
12
10
8
6
4
2
```

---

# 📖 Empty Range

If the values don't match the direction of the `step`, the loop doesn't execute.

```python
for i in range(1, 5, -1):
    print(i)
```

Output

```text
(No Output)
```

Why?

- Start = `1`
- Stop = `5`
- Step = `-1`

Python cannot move from `1` toward `5` using a negative step.

---

# 📖 Converting `range()` to a List

```python
numbers = list(range(1, 6))

print(numbers)
```

Output

```text
[1, 2, 3, 4, 5]
```

This is useful when you want to see all the generated values at once.

---

# 📊 Trace Table

Program

```python
for i in range(2, 10, 2):
    print(i)
```

| Iteration | `i` |
|-----------|----:|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |

---

# 🌍 Real-World Examples

## Print Numbers 1 to 10

```python
for i in range(1, 11):
    print(i)
```

---

## Multiplication Table

```python
number = 7

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

---

## Sum of Numbers

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

Output

```text
15
```

---

## Countdown Timer

```python
for i in range(10, 0, -1):
    print(i)

print("Blast Off!")
```

---

## Print Even Numbers

```python
for i in range(2, 21, 2):
    print(i)
```

---

## Print Odd Numbers

```python
for i in range(1, 20, 2):
    print(i)
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting That `stop` Is Excluded

```python
for i in range(1, 5):
    print(i)
```

Output

```text
1
2
3
4
```

Many beginners expect `5` to be included, but it is not.

---

## ❌ Using a Step of `0`

```python
range(1, 10, 0)
```

Output

```text
ValueError: range() arg 3 must not be zero
```

A step of `0` is not allowed because Python would never move to the next value.

---

## ❌ Wrong Step Direction

```python
for i in range(1, 10, -1):
    print(i)
```

Output

```text
(No Output)
```

To count upward, use a positive step. To count downward, use a negative step.

---

# 💡 Best Practices

- Remember that the `stop` value is **excluded**.
- Use meaningful variable names (`number`, `index`, `row`) instead of always using `i`.
- Use `step` when you want to skip values.
- Use negative steps for reverse counting.

---

# 🚀 Pro Tips

The `range()` function is commonly used in:

- Loops
- Pattern printing
- Matrix traversal
- Counting
- Game development
- Data processing
- Algorithm implementation

---

# ❓ Interview Questions

- [ ] What is the purpose of the `range()` function?
- [ ] How many arguments can `range()` accept?
- [ ] Is the `stop` value included?
- [ ] Can `range()` count backwards?
- [ ] Why can't the step value be `0`?

---

# 🏋️ Practice Programs

## Easy

```python
for i in range(5):
    print(i)
```

---

```python
for i in range(1, 11):
    print(i)
```

---

## Medium

```python
for i in range(2, 21, 2):
    print(i)
```

---

```python
for i in range(10, 0, -1):
    print(i)
```

---

## Advanced

```python
total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)
```

---

```python
for i in range(1, 6):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()
```

---

# 🎯 Challenge

Write programs to:

1. Print numbers from **50 to 100**.
2. Print numbers from **100 to 1**.
3. Print all multiples of **5** between **5 and 100**.
4. Print all odd numbers from **99 to 1** in reverse order.

---

# 📝 Assignment

- [x] Print numbers from 1 to 20.
- [x] Print numbers from 20 to 1.
- [x] Print even numbers from 2 to 100.
- [x] Print odd numbers from 1 to 99.
- [x] Print multiples of 3 from 3 to 60.
- [x] Print the multiplication table of any number.
- [x] Calculate the sum of numbers from 1 to 100.
- [x] Print a square pattern using nested `range()` loops.
- [x] Print a triangle pattern using nested `range()` loops.

---

# 📚 Summary

You learned:

- ✅ What the `range()` function is.
- ✅ The three forms of `range()`.
- ✅ How to use `start`, `stop`, and `step`.
- ✅ How to count forwards and backwards.
- ✅ Common mistakes and best practices.

### Key Points to Remember

- `range(stop)` → Starts at `0`.
- `range(start, stop)` → Starts at `start` and stops **before** `stop`.
- `range(start, stop, step)` → Uses a custom step size.
- The **`stop` value is never included**.
- Use a **positive step** to count up and a **negative step** to count down.
- A **step of `0` is invalid**.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `range()` function.
- [x] I know all three forms of `range()`.
- [x] I understand `start`, `stop`, and `step`.
- [x] I can use positive and negative steps.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 🎉 Phase 5 Completed!

You have now mastered:

- ✅ `while` Loop
- ✅ `for` Loop
- ✅ Nested Loops
- ✅ Infinite Loops
- ✅ `break`
- ✅ `continue`
- ✅ `pass`
- ✅ `else` with Loops
- ✅ `range()`

You are now ready to move on to **Phase 6: collections**, where you'll learn how to write reusable, modular, and professional Python code.