# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 8:** `else` with Loops

**Difficulty:** ⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what `else` with loops is.
- [ ] Learn how `else` works with `for` loops.
- [ ] Learn how `else` works with `while` loops.
- [ ] Understand the relationship between `break` and `else`.
- [ ] Solve real-world problems using loop `else`.

---

# 📖 What is `else` with Loops?

In Python, an **`else` block can be used with both `for` and `while` loops**.

The `else` block executes **only if the loop finishes normally**.

If the loop is terminated using **`break`**, the `else` block **does not execute**.

---

# 🤔 Why Do We Need `else` with Loops?

The `else` block is useful when you want to perform an action **only if the loop completed successfully**.

Examples:

- Searching for an item.
- Checking whether a number is prime.
- Validating data.
- Processing files.

---

# 📖 Syntax

## `for` Loop

```python
for item in iterable:
    # Loop Body
else:
    # Executes if loop finishes normally
```

---

## `while` Loop

```python
while condition:
    # Loop Body
else:
    # Executes if condition becomes False
```

---

# 🔄 Flow of Execution

```text
             Start
                │
                ▼
          Loop Executes
                │
        ┌───────┴────────┐
        │                │
   Loop Ends        break Executed
 Normally                │
        │                │
        ▼                ▼
 Execute else      Skip else
```

---

# 📖 Rule to Remember

✅ Loop finishes normally → `else` runs.

❌ Loop ends because of `break` → `else` is skipped.

---

# 📖 Example 1: `for` Loop with `else`

```python
for i in range(1, 6):
    print(i)

else:
    print("Loop Finished Successfully")
```

Output

```text
1
2
3
4
5
Loop Finished Successfully
```

The loop completed all iterations, so the `else` block executed.

---

# 📖 Example 2: `break` Prevents `else`

```python
for i in range(1, 6):

    if i == 3:
        break

    print(i)

else:
    print("Loop Finished")
```

Output

```text
1
2
```

The `else` block does **not** execute because the loop ended with `break`.

---

# 📖 Example 3: `while` Loop with `else`

```python
count = 1

while count <= 5:
    print(count)
    count += 1

else:
    print("Loop Completed")
```

Output

```text
1
2
3
4
5
Loop Completed
```

---

# 📖 Example 4: `while` + `break`

```python
count = 1

while count <= 5:

    if count == 3:
        break

    print(count)
    count += 1

else:
    print("Loop Completed")
```

Output

```text
1
2
```

The `else` block is skipped because `break` was executed.

---

# 📖 Example 5: Searching a List

```python
fruits = ["Apple", "Banana", "Orange"]

search = "Mango"

for fruit in fruits:

    if fruit == search:
        print("Fruit Found")
        break

else:
    print("Fruit Not Found")
```

Output

```text
Fruit Not Found
```

Since the loop completed without finding `"Mango"`, the `else` block ran.

---

# 📖 Example 6: Number Found

```python
numbers = [10, 20, 30, 40]

search = 30

for number in numbers:

    if number == search:
        print("Number Found")
        break

else:
    print("Number Not Found")
```

Output

```text
Number Found
```

The `else` block did not execute because the loop ended with `break`.

---

# 📖 Example 7: Prime Number Check

```python
number = 17

for i in range(2, number):

    if number % i == 0:
        print("Not Prime")
        break

else:
    print("Prime Number")
```

Output

```text
Prime Number
```

This is one of the most common real-world uses of loop `else`.

---

# 📊 Trace Table

Program

```python
for i in range(1, 5):

    if i == 3:
        break

    print(i)

else:
    print("Done")
```

| Iteration | `i` | `break`? | Output |
|-----------|----:|----------|--------|
| 1 | 1 | No | 1 |
| 2 | 2 | No | 2 |
| 3 | 3 | Yes | Loop Ends |
| `else` | — | Skipped | — |

---

# 📊 `for-else` vs `while-else`

| Feature | `for-else` | `while-else` |
|----------|------------|--------------|
| Works with loop | ✅ | ✅ |
| Executes after normal completion | ✅ | ✅ |
| Skipped if `break` occurs | ✅ | ✅ |
| Commonly used for searching | ✅ | ✅ |

---

# 🌍 Real-World Examples

## Login Attempts

```python
correct_password = "python123"

attempts = ["abc", "123", "python123"]

for password in attempts:

    if password == correct_password:
        print("Login Successful")
        break

else:
    print("All Attempts Failed")
```

---

## Search Student

```python
students = ["Rahul", "Aisha", "Saniya"]

search = "Rohan"

for student in students:

    if student == search:
        print("Student Found")
        break

else:
    print("Student Not Found")
```

---

## Inventory Search

```python
products = ["Laptop", "Mouse", "Keyboard"]

item = "Monitor"

for product in products:

    if product == item:
        print("Available")
        break

else:
    print("Out of Stock")
```

---

## Guessing Game

```python
secret = 5
guesses = [2, 7, 8]

for guess in guesses:

    if guess == secret:
        print("Correct Guess")
        break

else:
    print("No Correct Guess")
```

---

# ⚠️ Common Mistakes

## ❌ Thinking `else` Runs Only When the Condition is False

Many beginners think loop `else` behaves like an `if-else`.

This is **incorrect**.

Loop `else` depends on **how the loop ends**, not on the loop condition.

---

## ❌ Forgetting that `break` Skips `else`

```python
for i in range(5):

    if i == 2:
        break

else:
    print("Done")
```

The `else` block will **not** run.

---

## ❌ Confusing `continue` with `break`

```python
for i in range(5):

    if i == 2:
        continue

    print(i)

else:
    print("Done")
```

Output

```text
0
1
3
4
Done
```

`continue` skips only one iteration, so the loop still finishes normally and the `else` block executes.

---

# 💡 Best Practices

- Use loop `else` mainly for search operations.
- Avoid unnecessary `else` blocks if they reduce readability.
- Remember that `break` prevents the `else` block from executing.
- Use descriptive messages in the `else` block.

---

# 🚀 Pro Tips

Loop `else` is useful in:

- Search algorithms
- Prime number checking
- Password verification
- Data validation
- File searching
- Inventory management

---

# ❓ Interview Questions

- [ ] What is the purpose of `else` with loops?
- [ ] When does the `else` block execute?
- [ ] Does `continue` prevent the `else` block from running?
- [ ] Does `break` prevent the `else` block from running?
- [ ] Give one real-world use of loop `else`.

---

# 🏋️ Practice Programs

## Easy

```python
for i in range(5):
    print(i)
else:
    print("Finished")
```

---

```python
count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Done")
```

---

## Medium

```python
numbers = [5, 8, 12, 20]

search = 10

for num in numbers:

    if num == search:
        print("Found")
        break

else:
    print("Not Found")
```

---

```python
for i in range(1, 6):

    if i == 10:
        break

    print(i)

else:
    print("Completed Normally")
```

---

## Advanced

```python
number = 29

for i in range(2, number):

    if number % i == 0:
        print("Not Prime")
        break

else:
    print("Prime")
```

---

```python
passwords = ["123", "abc", "hello"]

for password in passwords:

    if password == "python123":
        print("Login Success")
        break

else:
    print("Login Failed")
```

---

# 🎯 Challenge

Write a program that:

1. Searches for a student's name in a list.
2. If found, print `"Student Found"` and stop the loop.
3. If not found, print `"Student Not Found"` using the `else` block.

Example

```text
Students = ["Rahul", "Aisha", "Saniya"]

Search: Rohan

Output:
Student Not Found
```

---

# 📝 Assignment

- [ ] Search for a number in a list using `for-else`.
- [ ] Check whether a number is prime using `for-else`.
- [ ] Create a login system using `while-else`.
- [ ] Search for a product in an inventory list using `for-else`.
- [ ] Create a guessing game that uses `while-else`.

---

# 📚 Summary

You learned:

- ✅ What `else` with loops is.
- ✅ How `for-else` works.
- ✅ How `while-else` works.
- ✅ How `break` affects the `else` block.
- ✅ Real-world applications of loop `else`.

Remember:

- The `else` block executes **only if the loop finishes normally**.
- If the loop is terminated by **`break`**, the `else` block is skipped.
- `continue` does **not** prevent the `else` block from running.

---

# 🎯 Topic Completion Checklist

- [ ] I understand `else` with loops.
- [ ] I know when the `else` block executes.
- [ ] I know how `break` affects loop `else`.
- [ ] I completed the practice programs.
- [ ] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 9: `range()` Function**