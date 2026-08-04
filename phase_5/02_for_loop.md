# 🐍 Python Master Course

> **Phase 5:** Loops  
> **Topic 2:** `for` Loop

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a `for` loop is.
- [ ] Learn how a `for` loop works.
- [ ] Understand what an iterable is.
- [ ] Iterate through different data types.
- [ ] Write efficient programs using `for` loops.

---

# 📖 What is a `for` Loop?

A **`for` loop** is used to **iterate (loop) through each element of an iterable (sequence) one by one.**

Unlike a `while` loop, a `for` loop automatically stops after processing all elements in the iterable.

It is commonly used when the **number of iterations is known** or when working with collections like strings, lists, tuples, sets, and dictionaries.

---

# 🤔 Why Do We Need a `for` Loop?

Suppose you want to print every letter of the word **"Python"**.

Without a loop:

```python
print("P")
print("y")
print("t")
print("h")
print("o")
print("n")
```

Using a `for` loop:

```python
for letter in "Python":
    print(letter)
```

Output

```text
P
y
t
h
o
n
```

The `for` loop makes the code shorter, cleaner, and easier to maintain.

---

# 📖 Syntax

```python
for variable in iterable:
    # Code Block
```

---

## General Syntax

```python
for item in iterable:
    statement
```

---

# 🔍 Syntax Breakdown

```python
for letter in "Python":
    print(letter)
```

| Part | Meaning |
|------|---------|
| `for` | Starts the loop |
| `letter` | Loop variable |
| `in` | Retrieves one item at a time |
| `"Python"` | Iterable (sequence) |
| `:` | Begins the loop block |
| Indentation | Code executed in every iteration |

---

# 📖 What is an Iterable?

An **iterable** is an object whose elements can be accessed **one at a time**.

Python supports many iterable objects.

Examples:

```python
"Python"                # String
[10, 20, 30]            # List
(1, 2, 3)               # Tuple
{"A", "B", "C"}         # Set
{"x": 1, "y": 2}        # Dictionary
range(5)                # Range Object
```

---

# 🔄 Flow of Execution

```text
              Start
                 │
                 ▼
      Get First Element
                 │
                 ▼
         Execute Code
                 │
                 ▼
      More Elements Left?
           │           │
         Yes          No
           │           │
           ▼           ▼
    Get Next Element   Stop
```

---

# 📖 How Does a `for` Loop Work?

Python performs these steps:

1. Takes the first element from the iterable.
2. Stores it in the loop variable.
3. Executes the loop body.
4. Moves to the next element.
5. Repeats until no elements remain.

---

# 1️⃣ Loop Through a String

```python
for letter in "Python":
    print(letter)
```

Output

```text
P
y
t
h
o
n
```

---

# 2️⃣ Loop Through a List

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output

```text
Apple
Banana
Mango
```

---

# 3️⃣ Loop Through a Tuple

```python
numbers = (10, 20, 30)

for num in numbers:
    print(num)
```

Output

```text
10
20
30
```

---

# 4️⃣ Loop Through a Set

```python
colors = {"Red", "Green", "Blue"}

for color in colors:
    print(color)
```

Possible Output

```text
Green
Blue
Red
```

> **Note:** Sets are unordered, so the output order may differ every time.

---

# 5️⃣ Loop Through a Dictionary (Keys)

```python
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key)
```

Output

```text
name
age
course
```

---

# 6️⃣ Loop Through Dictionary Values

```python
student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}

for value in student.values():
    print(value)
```

Output

```text
Saniya
20
BCA
```

---

# 7️⃣ Loop Through Dictionary Keys and Values

```python
student = {
    "name": "Saniya",
    "age": 20
}

for key, value in student.items():
    print(key, ":", value)
```

Output

```text
name : Saniya
age : 20
```

---

# 8️⃣ Loop Using `range()`

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

> We will learn `range()` in detail later in this phase.

---

# 📖 Understanding the Loop Variable

The loop variable stores one element of the iterable during each iteration.

Example

```python
numbers = [5, 10, 15]

for num in numbers:
    print(num)
```

### Iteration Table

| Iteration | Value of `num` |
|-----------|---------------:|
| 1 | 5 |
| 2 | 10 |
| 3 | 15 |

---

# 📖 Using `_` as a Loop Variable

If you don't need the loop variable, use `_`.

```python
for _ in range(3):
    print("Hello")
```

Output

```text
Hello
Hello
Hello
```

---

# 📊 `for` Loop vs `while` Loop

| Feature | `for` Loop | `while` Loop |
|----------|------------|--------------|
| Iterates over an iterable | ✅ | ❌ |
| Uses a condition | ❌ | ✅ |
| Best when iterations are known | ✅ | ❌ |
| Best when iterations are unknown | ❌ | ✅ |
| Automatic iteration | ✅ | ❌ (manual update required) |

---

# 🌍 Real-World Programs

## Print Student Names

```python
students = ["Rahul", "Aisha", "Saniya"]

for student in students:
    print(student)
```

---

## Display Product List

```python
products = ["Laptop", "Mouse", "Keyboard"]

for product in products:
    print(product)
```

---

## Print Employee IDs

```python
employee_ids = [101, 102, 103]

for emp_id in employee_ids:
    print(emp_id)
```

---

## Print Characters of a Name

```python
name = "Saniya"

for ch in name:
    print(ch)
```

---

## Print Squares

```python
for number in [1, 2, 3, 4, 5]:
    print(number ** 2)
```

Output

```text
1
4
9
16
25
```

---

# ⚠️ Common Mistakes

## ❌ Forgetting the Colon

Incorrect

```python
for i in range(5)
    print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

## ❌ Wrong Indentation

Incorrect

```python
for i in range(3):
print(i)
```

Output

```text
IndentationError
```

Correct

```python
for i in range(3):
    print(i)
```

---

## ❌ Looping Over a Non-Iterable

Incorrect

```python
for i in 10:
    print(i)
```

Output

```text
TypeError: 'int' object is not iterable
```

Correct

```python
for i in range(10):
    print(i)
```

---

## ❌ Modifying the Iterable While Iterating

Incorrect

```python
numbers = [1, 2, 3]

for num in numbers:
    numbers.append(4)
```

This can produce unexpected behavior. Avoid modifying a collection while iterating over it.

---

# 💡 Best Practices

- Use meaningful loop variable names.
- Use `_` when the loop variable isn't needed.
- Keep loop bodies simple.
- Choose a `for` loop when iterating through sequences.

---

# 🚀 Pro Tips

`for` loops are widely used in:

- Data Analysis
- Machine Learning
- File Processing
- Automation Scripts
- Web Development
- Game Development
- Reading CSV files
- Processing API responses

---

# ❓ Interview Questions

- [ ] What is a `for` loop?
- [ ] What is an iterable?
- [ ] Which Python data types are iterable?
- [ ] What is the purpose of the `in` keyword?
- [ ] Why is `_` sometimes used as the loop variable?

---

# 🏋️ Practice Programs

## Easy

```python
for ch in "Hello":
    print(ch)
```

---

```python
for fruit in ["Apple", "Banana", "Mango"]:
    print(fruit)
```

---

```python
for number in (1, 2, 3, 4):
    print(number)
```

---

## Medium

```python
student = {
    "Name": "Saniya",
    "Age": 20
}

for key in student:
    print(key)
```

---

```python
student = {
    "Name": "Saniya",
    "Age": 20
}

for value in student.values():
    print(value)
```

---

```python
for i in range(1, 11):
    print(i)
```

---

## Advanced

```python
employees = {
    101: "Rahul",
    102: "Aisha",
    103: "Saniya"
}

for emp_id, name in employees.items():
    print(emp_id, "->", name)
```

---

```python
numbers = [5, 10, 15, 20]

for number in numbers:
    if number % 10 == 0:
        print(number, "is divisible by 10")
```

---

# 🎯 Challenge

Write a program that:

1. Creates a list of five favorite books.
2. Uses a `for` loop to print each book on a separate line.

Example

```text
Atomic Habits
The Alchemist
Rich Dad Poor Dad
Deep Work
Clean Code
```

---

# 📝 Assignment

- [x] Print each character of your name.
- [x] Print all elements of a list.
- [x] Print all elements of a tuple.
- [x] Print all elements of a set.
- [x] Print dictionary keys.
- [x] Print dictionary values.
- [x] Print dictionary keys and values together.
- [x] Print numbers from 1 to 20 using `range()`.

---

# 📚 Summary

You learned:

- ✅ What a `for` loop is.
- ✅ What an iterable is.
- ✅ How a `for` loop works.
- ✅ How to iterate through strings, lists, tuples, sets, dictionaries, and `range()`.
- ✅ The purpose of the loop variable.
- ✅ Common mistakes and best practices.

Remember:

- A `for` loop processes one element at a time.
- It automatically stops after all elements have been processed.
- Use a `for` loop whenever you need to iterate over an iterable.

---

# 🎯 Topic Completion Checklist

- [x] I understand the `for` loop.
- [x] I know what an iterable is.
- [x] I can iterate through different Python collections.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 5 – Topic 3: Nested Loops**