# 🐍 Python Master Course

# 📦 Phase 6: Collections – Dictionaries

## 📌 Topic 6: Dictionary Comprehension

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what dictionary comprehension is.
* [ ] Understand the syntax of dictionary comprehension.
* [ ] Create dictionaries using comprehensions.
* [ ] Use expressions in dictionary comprehensions.
* [ ] Use `for` loops with dictionary comprehensions.
* [ ] Use `if` conditions with dictionary comprehensions.
* [ ] Use `if-else` conditions with dictionary comprehensions.
* [ ] Create dictionaries from lists.
* [ ] Create dictionaries from two lists.
* [ ] Use `zip()` with dictionary comprehension.
* [ ] Transform dictionary keys and values.
* [ ] Filter dictionary data.
* [ ] Combine conditions and expressions.
* [ ] Understand nested dictionary comprehensions.
* [ ] Use dictionary comprehensions in real-world applications.
* [ ] Avoid common mistakes.
* [ ] Solve dictionary comprehension problems independently.

---

# 📖 1. What is Dictionary Comprehension?

Dictionary comprehension is a short and powerful way to create a dictionary using a single expression.

Instead of writing multiple lines of code using a `for` loop, we can create a dictionary in one line.

Example:

```python
squares = {x: x * x for x in range(1, 6)}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Here:

```text
x        → key
x * x    → value
range()  → source of values
```

---

# 🧠 2. Basic Dictionary Comprehension Syntax

The general syntax is:

```python
dictionary = {key_expression: value_expression for item in iterable}
```

Example:

```python
numbers = {x: x * 2 for x in range(1, 6)}

print(numbers)
```

Output:

```text
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
```

The basic structure is:

```text
{ key : value for item in iterable }
```

---

# 🔄 3. Dictionary Comprehension vs Normal Loop

Without dictionary comprehension:

```python
squares = {}

for x in range(1, 6):
    squares[x] = x * x

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Using dictionary comprehension:

```python
squares = {x: x * x for x in range(1, 6)}

print(squares)
```

Both produce the same result.

Dictionary comprehension is shorter and often easier to read when the logic is simple.

---

# 🔢 4. Creating a Dictionary of Numbers

```python
numbers = {x: x for x in range(1, 6)}

print(numbers)
```

Output:

```text
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
```

Here the key and value are the same.

---

# ✖️ 5. Creating a Dictionary of Squares

```python
squares = {x: x ** 2 for x in range(1, 6)}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

The key is `x` and the value is `x ** 2`.

---

# 🔢 6. Creating a Dictionary of Cubes

```python
cubes = {x: x ** 3 for x in range(1, 6)}

print(cubes)
```

Output:

```text
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

---

# 🧮 7. Using Expressions

Dictionary comprehensions can contain expressions.

Example:

```python
numbers = {x: x * 10 for x in range(1, 6)}

print(numbers)
```

Output:

```text
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
```

The expression:

```python
x * 10
```

calculates the value for every key.

---

# 🔤 8. Dictionary Comprehension with Strings

```python
names = ["Asha", "Neha", "Kiran"]

name_lengths = {name: len(name) for name in names}

print(name_lengths)
```

Output:

```text
{'Asha': 4, 'Neha': 4, 'Kiran': 5}
```

Here:

```text
Key   → name
Value → length of name
```

---

# 🔠 9. Converting Names to Uppercase

```python
names = ["Asha", "Neha", "Kiran"]

upper_names = {name: name.upper() for name in names}

print(upper_names)
```

Output:

```text
{'Asha': 'ASHA', 'Neha': 'NEHA', 'Kiran': 'KIRAN'}
```

---

# 🧩 10. Using `if` in Dictionary Comprehension

A condition can be added to a dictionary comprehension.

Syntax:

```python
{key: value for item in iterable if condition}
```

Example:

```python
even_numbers = {x: x * x for x in range(1, 11) if x % 2 == 0}

print(even_numbers)
```

Output:

```text
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

Only even numbers are included.

---

# 🔍 11. Filtering Odd Numbers

```python
odd_numbers = {x: x ** 2 for x in range(1, 11) if x % 2 != 0}

print(odd_numbers)
```

Output:

```text
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
```

---

# 🎯 12. Filtering Values Greater Than a Number

```python
numbers = {x: x for x in range(1, 11) if x > 5}

print(numbers)
```

Output:

```text
{6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
```

---

# ⚖️ 13. Using `if-else` in Dictionary Comprehension

Dictionary comprehension can also use `if-else`.

Syntax:

```python
{key: value_if_true if condition else value_if_false for item in iterable}
```

Example:

```python
result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in range(1, 6)
}

print(result)
```

Output:

```text
{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}
```

Notice the difference:

### Filtering

```python
{x: x for x in numbers if condition}
```

### `if-else`

```python
{x: "A" if condition else "B" for x in numbers}
```

---

# 🧠 14. Dictionary Comprehension with Conditions

Example:

```python
marks = {
    "Python": 90,
    "SQL": 72,
    "Git": 85,
    "HTML": 68
}

passed = {
    subject: mark
    for subject, mark in marks.items()
    if mark >= 75
}

print(passed)
```

Output:

```text
{'Python': 90, 'Git': 85}
```

Only subjects with marks of 75 or more are included.

---

# 🔄 15. Transforming Dictionary Values

Suppose we have:

```python
prices = {
    "Laptop": 50000,
    "Phone": 30000,
    "Tablet": 20000
}
```

We can increase every price by 10%:

```python
new_prices = {
    product: price * 1.10
    for product, price in prices.items()
}

print(new_prices)
```

Output:

```text
{'Laptop': 55000.0, 'Phone': 33000.0, 'Tablet': 22000.0}
```

---

# 🔑 16. Transforming Dictionary Keys

```python
prices = {
    "laptop": 50000,
    "phone": 30000,
    "tablet": 20000
}

uppercase_keys = {
    product.upper(): price
    for product, price in prices.items()
}

print(uppercase_keys)
```

Output:

```text
{'LAPTOP': 50000, 'PHONE': 30000, 'TABLET': 20000}
```

---

# 🔁 17. Transforming Both Keys and Values

```python
prices = {
    "laptop": 50000,
    "phone": 30000,
    "tablet": 20000
}

updated = {
    product.upper(): price * 2
    for product, price in prices.items()
}

print(updated)
```

Output:

```text
{'LAPTOP': 100000, 'PHONE': 60000, 'TABLET': 40000}
```

Both the keys and values are transformed.

---

# 📋 18. Creating a Dictionary from a List

```python
subjects = ["Python", "SQL", "Git"]

marks = {
    subject: 0
    for subject in subjects
}

print(marks)
```

Output:

```text
{'Python': 0, 'SQL': 0, 'Git': 0}
```

This is similar to:

```python
dict.fromkeys(subjects, 0)
```

---

# 🧩 19. Creating a Dictionary of Default Values

```python
skills = ["Python", "SQL", "HTML", "CSS"]

levels = {
    skill: "Beginner"
    for skill in skills
}

print(levels)
```

Output:

```text
{'Python': 'Beginner', 'SQL': 'Beginner', 'HTML': 'Beginner', 'CSS': 'Beginner'}
```

---

# 🔗 20. Creating a Dictionary from Two Lists

Suppose we have:

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 80]
```

We can combine them using `zip()`:

```python
result = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}

print(result)
```

Output:

```text
{'Python': 90, 'SQL': 85, 'Git': 80}
```

---

# 🔗 21. Understanding `zip()`

`zip()` combines corresponding elements from multiple iterables.

Example:

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 80]

print(list(zip(subjects, marks)))
```

Output:

```text
[('Python', 90), ('SQL', 85), ('Git', 80)]
```

Dictionary comprehension can then convert these pairs into a dictionary.

---

# 📊 22. Creating a Dictionary from Student Data

```python
names = ["Asha", "Neha", "Kiran"]
ages = [20, 21, 19]

students = {
    name: age
    for name, age in zip(names, ages)
}

print(students)
```

Output:

```text
{'Asha': 20, 'Neha': 21, 'Kiran': 19}
```

---

# 🔍 23. Filtering Data from an Existing Dictionary

```python
marks = {
    "Python": 90,
    "SQL": 65,
    "Git": 85,
    "HTML": 70
}

high_marks = {
    subject: mark
    for subject, mark in marks.items()
    if mark >= 80
}

print(high_marks)
```

Output:

```text
{'Python': 90, 'Git': 85}
```

This is called **dictionary filtering**.

---

# 🏆 24. Categorizing Values Using `if-else`

```python
marks = {
    "Python": 90,
    "SQL": 65,
    "Git": 85
}

result = {
    subject: "Pass" if mark >= 40 else "Fail"
    for subject, mark in marks.items()
}

print(result)
```

Output:

```text
{'Python': 'Pass', 'SQL': 'Pass', 'Git': 'Pass'}
```

---

# 🎓 25. Student Grade Classification

```python
marks = {
    "Python": 92,
    "SQL": 78,
    "Git": 65,
    "HTML": 35
}

grades = {
    subject: "A" if mark >= 80
    else "B" if mark >= 60
    else "C" if mark >= 40
    else "F"
    for subject, mark in marks.items()
}

print(grades)
```

Output:

```text
{'Python': 'A', 'SQL': 'B', 'Git': 'B', 'HTML': 'F'}
```

---

# 🧮 26. Creating a Dictionary of Squares for Even Numbers

```python
squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(squares)
```

Output:

```text
{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

# 🔢 27. Creating a Dictionary of Cubes for Odd Numbers

```python
cubes = {
    x: x ** 3
    for x in range(1, 11)
    if x % 2 != 0
}

print(cubes)
```

Output:

```text
{1: 1, 3: 27, 5: 125, 7: 343, 9: 729}
```

---

# 🔤 28. Dictionary Comprehension with String Characters

```python
word = "PYTHON"

characters = {
    char: ord(char)
    for char in word
}

print(characters)
```

Output:

```text
{'P': 80, 'Y': 89, 'T': 84, 'H': 72, 'O': 79, 'N': 78}
```

---

# 🔢 29. Character Frequency Using Dictionary Comprehension

Dictionary comprehension can be useful for transforming already-created frequency data.

```python
letters = ["a", "b", "c"]

frequency = {
    letter: 0
    for letter in letters
}

print(frequency)
```

Output:

```text
{'a': 0, 'b': 0, 'c': 0}
```

For actual frequency counting, a normal loop or `collections.Counter` is generally more appropriate.

---

# 🧠 30. Nested Dictionary Comprehension

A dictionary comprehension can contain another comprehension.

Example:

```python
table = {
    number: {
        multiplier: number * multiplier
        for multiplier in range(1, 4)
    }
    for number in range(1, 4)
}

print(table)
```

Output:

```text
{
    1: {1: 1, 2: 2, 3: 3},
    2: {1: 2, 2: 4, 3: 6},
    3: {1: 3, 2: 6, 3: 9}
}
```

Nested comprehensions are powerful but should be used only when the code remains readable.

---

# 🔄 31. Inverting a Dictionary

Suppose:

```python
original = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

We can swap keys and values:

```python
inverted = {
    value: key
    for key, value in original.items()
}

print(inverted)
```

Output:

```text
{1: 'a', 2: 'b', 3: 'c'}
```

⚠️ This works safely when the original values are unique and hashable.

---

# ⚠️ 32. Duplicate Values When Inverting

Consider:

```python
data = {
    "a": 1,
    "b": 1,
    "c": 2
}

inverted = {
    value: key
    for key, value in data.items()
}

print(inverted)
```

Output:

```text
{1: 'b', 2: 'c'}
```

Why?

Because dictionary keys must be unique.

The later key overwrites the earlier key.

---

# 🔍 33. Filtering Based on Keys

```python
employees = {
    "Asha": 45000,
    "Neha": 50000,
    "Kiran": 40000
}

selected = {
    name: salary
    for name, salary in employees.items()
    if name != "Kiran"
}

print(selected)
```

Output:

```text
{'Asha': 45000, 'Neha': 50000}
```

---

# 💰 34. Filtering Based on Values

```python
employees = {
    "Asha": 45000,
    "Neha": 50000,
    "Kiran": 40000
}

high_salary = {
    name: salary
    for name, salary in employees.items()
    if salary >= 45000
}

print(high_salary)
```

Output:

```text
{'Asha': 45000, 'Neha': 50000}
```

---

# 🔄 35. Applying a Calculation to All Values

```python
prices = {
    "Laptop": 50000,
    "Phone": 30000,
    "Tablet": 20000
}

discounted = {
    item: price * 0.90
    for item, price in prices.items()
}

print(discounted)
```

Output:

```text
{'Laptop': 45000.0, 'Phone': 27000.0, 'Tablet': 18000.0}
```

---

# 🛒 36. Real-World Example: Shopping Cart Discount

```python
cart = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}

discounted_cart = {
    item: price * 0.95
    for item, price in cart.items()
}

print(discounted_cart)
```

Output:

```text
{'Laptop': 52250.0, 'Mouse': 760.0, 'Keyboard': 1425.0}
```

---

# 🌍 37. Real-World Example: Student Marks

```python
marks = {
    "Python": 90,
    "SQL": 75,
    "Git": 85,
    "HTML": 68
}

passed_subjects = {
    subject: mark
    for subject, mark in marks.items()
    if mark >= 70
}

print(passed_subjects)
```

Output:

```text
{'Python': 90, 'SQL': 75, 'Git': 85}
```

---

# 🌍 38. Real-World Example: Employee Salaries

```python
employees = {
    "Asha": 45000,
    "Neha": 52000,
    "Kiran": 38000
}

increased_salary = {
    name: salary * 1.10
    for name, salary in employees.items()
}

print(increased_salary)
```

Output:

```text
{'Asha': 49500.00000000001, 'Neha': 57200.00000000001, 'Kiran': 41800.00000000001}
```

For currency calculations, rounding can be used:

```python
increased_salary = {
    name: round(salary * 1.10, 2)
    for name, salary in employees.items()
}
```

---

# 🌍 39. Real-World Example: Product Inventory

```python
inventory = {
    "Laptop": 5,
    "Mouse": 15,
    "Keyboard": 0,
    "Monitor": 8
}

available = {
    product: stock
    for product, stock in inventory.items()
    if stock > 0
}

print(available)
```

Output:

```text
{'Laptop': 5, 'Mouse': 15, 'Monitor': 8}
```

---

# 🌍 40. Real-World Example: Temperature Conversion

```python
celsius = {
    "Monday": 25,
    "Tuesday": 30,
    "Wednesday": 28
}

fahrenheit = {
    day: (temp * 9 / 5) + 32
    for day, temp in celsius.items()
}

print(fahrenheit)
```

Output:

```text
{'Monday': 77.0, 'Tuesday': 86.0, 'Wednesday': 82.4}
```

---

# 🌍 41. Real-World Example: User Status

```python
users = {
    "user1": True,
    "user2": False,
    "user3": True
}

status = {
    username: "Active" if active else "Inactive"
    for username, active in users.items()
}

print(status)
```

Output:

```text
{'user1': 'Active', 'user2': 'Inactive', 'user3': 'Active'}
```

---

# ⚠️ 42. Common Mistake: Forgetting the Colon

Wrong:

```python
squares = {x x ** 2 for x in range(5)}
```

Correct:

```python
squares = {x: x ** 2 for x in range(5)}
```

A dictionary comprehension requires:

```text
key : value
```

---

# ⚠️ 43. Common Mistake: Confusing Set and Dictionary Comprehension

This creates a set:

```python
numbers = {x * 2 for x in range(5)}
```

This creates a dictionary:

```python
numbers = {x: x * 2 for x in range(5)}
```

Remember:

```text
{x for x in iterable}
        ↓
      SET

{key: value for x in iterable}
        ↓
   DICTIONARY
```

---

# ⚠️ 44. Common Mistake: Incorrect `if-else` Position

Wrong:

```python
result = {
    x: "Even"
    for x in range(5)
    if x % 2 == 0
    else "Odd"
}
```

Correct:

```python
result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in range(5)
}
```

With `if-else`, the conditional expression belongs before the `for`.

---

# ⚠️ 45. Common Mistake: Using Too Much Logic

Avoid making a comprehension extremely complicated.

Difficult to read:

```python
result = {
    x: "A" if x > 90 else "B" if x > 80 else "C" if x > 70 else "D"
    for x in marks
}
```

For complicated logic, a normal loop may be clearer.

Dictionary comprehension should make code simpler, not harder to understand.

---

# ⚠️ 46. Common Mistake: Duplicate Dictionary Keys

```python
result = {
    x % 2: x
    for x in range(1, 6)
}

print(result)
```

Output:

```text
{1: 5, 0: 4}
```

Several values generate the same keys.

Because dictionary keys must be unique, later values replace earlier values.

---

# 📊 47. Dictionary Comprehension vs Normal Loop

| Feature      | Normal Loop            | Dictionary Comprehension         |
| ------------ | ---------------------- | -------------------------------- |
| Code length  | Longer                 | Shorter                          |
| Readability  | Good for complex logic | Good for simple logic            |
| Conditions   | Flexible               | Supported                        |
| Expressions  | Supported              | Supported                        |
| Nested logic | Easier to manage       | Can become difficult             |
| Best use     | Complex operations     | Simple transformations/filtering |

---

# 🧠 48. Dictionary Comprehension Structure

Remember:

```text
                  DICTIONARY COMPREHENSION
                            │
                            ↓
                 {key: value for item}
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
           KEY            VALUE          LOOP
             │              │              │
             ↓              ↓              ↓
         key_expression  value_expression  for
                            │
                            ↓
                         OPTIONAL
                            │
                    ┌───────┴───────┐
                    ↓               ↓
                   if            if-else
                    │               │
                    ↓               ↓
                 Filter         Choose value
```

---

# 💻 49. Practice Programs

## 🟢 Easy

### Program 1: Create a Dictionary of Squares

```python
squares = {
    x: x ** 2
    for x in range(1, 6)
}

print(squares)
```

---

### Program 2: Create a Dictionary of Cubes

```python
cubes = {
    x: x ** 3
    for x in range(1, 6)
}

print(cubes)
```

---

### Program 3: Create a Dictionary from a List

```python
subjects = ["Python", "SQL", "Git"]

marks = {
    subject: 0
    for subject in subjects
}

print(marks)
```

---

### Program 4: Create a Dictionary of Name Lengths

```python
names = ["Asha", "Neha", "Kiran"]

lengths = {
    name: len(name)
    for name in names
}

print(lengths)
```

---

# 🟡 Medium

### Program 5: Create a Dictionary of Even Numbers

```python
even_numbers = {
    x: x * x
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_numbers)
```

---

### Program 6: Filter Student Marks

```python
marks = {
    "Python": 90,
    "SQL": 72,
    "Git": 85,
    "HTML": 65
}

result = {
    subject: mark
    for subject, mark in marks.items()
    if mark >= 80
}

print(result)
```

---

### Program 7: Convert Two Lists into a Dictionary

```python
subjects = ["Python", "SQL", "Git"]
marks = [90, 85, 80]

result = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}

print(result)
```

---

### Program 8: Convert Values to Double

```python
numbers = {
    "a": 10,
    "b": 20,
    "c": 30
}

result = {
    key: value * 2
    for key, value in numbers.items()
}

print(result)
```

---

# 🔴 Advanced

## Program 9: Student Grade Classification

```python
marks = {
    "Python": 92,
    "SQL": 78,
    "Git": 65,
    "HTML": 35
}

grades = {
    subject: "A" if mark >= 80
    else "B" if mark >= 60
    else "C" if mark >= 40
    else "F"
    for subject, mark in marks.items()
}

print(grades)
```

---

## Program 10: Employee Salary Increase

```python
employees = {
    "Asha": 45000,
    "Neha": 50000,
    "Kiran": 40000
}

updated_salary = {
    name: round(salary * 1.10, 2)
    for name, salary in employees.items()
}

print(updated_salary)
```

---

## Program 11: Filter Available Products

```python
inventory = {
    "Laptop": 5,
    "Mouse": 15,
    "Keyboard": 0,
    "Monitor": 8
}

available = {
    product: stock
    for product, stock in inventory.items()
    if stock > 0
}

print(available)
```

---

## Program 12: Invert a Dictionary

```python
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = {
    value: key
    for key, value in data.items()
}

print(inverted)
```

---

# 🏆 50. Challenge

Create a student marks dictionary:

```text
Python
SQL
Git
HTML
CSS
```

Store marks for each subject.

Then:

1. Create a dictionary containing only subjects with marks greater than or equal to `80`.
2. Create a dictionary containing each subject and its grade.
3. Create a dictionary containing each subject and marks increased by `5`.
4. Create a dictionary containing each subject and whether the student passed or failed.
5. Create a dictionary of subject names and their lengths.
6. Create a dictionary from two lists using `zip()`.
7. Create a dictionary containing only odd marks.
8. Calculate transformed values using dictionary comprehension.
9. Invert a dictionary where the values are unique.
10. Display the final results.

Example:

```python
marks = {
    "Python": 90,
    "SQL": 85,
    "Git": 80,
    "HTML": 68,
    "CSS": 82
}
```

Try solving the challenge without copying the solution.

---

# 🧪 51. Mini Project: Student Performance Analyzer

Create a student performance analyzer using dictionary comprehension.

Example:

```python
marks = {
    "Python": 90,
    "SQL": 75,
    "Git": 85,
    "HTML": 68,
    "CSS": 82
}
```

Perform the following operations:

* Create a dictionary containing only subjects with marks `>= 80`.
* Create a dictionary containing grades.
* Create a dictionary containing pass/fail status.
* Increase every mark by `5`.
* Create a dictionary containing subject names and their lengths.
* Create a dictionary containing only marks below `80`.
* Display all generated dictionaries.

### Your Goal

Build a complete student performance analyzer using dictionary comprehensions.

---

# 🎤 52. Interview Questions

* [ ] What is dictionary comprehension in Python?
* [ ] What is the syntax of dictionary comprehension?
* [ ] Why is dictionary comprehension useful?
* [ ] What is the difference between a dictionary comprehension and a normal `for` loop?
* [ ] How do you create a dictionary of squares using comprehension?
* [ ] How do you use an `if` condition in dictionary comprehension?
* [ ] How do you use `if-else` in dictionary comprehension?
* [ ] Where is the `if-else` expression placed?
* [ ] How can you create a dictionary from a list?
* [ ] How can you create a dictionary from two lists?
* [ ] How is `zip()` used with dictionary comprehension?
* [ ] How can you filter dictionary items?
* [ ] How can you transform dictionary values?
* [ ] How can you transform dictionary keys?
* [ ] Can dictionary comprehension be nested?
* [ ] What happens if duplicate keys are generated?
* [ ] What is the difference between set comprehension and dictionary comprehension?
* [ ] When should you avoid dictionary comprehension?
* [ ] Can dictionary comprehension use conditions?
* [ ] Can dictionary comprehension use expressions?

---

# 📝 53. Assignment

Complete the following programs.

### Task 1

Create a dictionary containing numbers from `1` to `10` and their squares.

---

### Task 2

Create a dictionary containing numbers from `1` to `10` and their cubes.

---

### Task 3

Create a dictionary from the following list:

```text
Python
SQL
Git
HTML
CSS
```

Set every value to `"Beginner"`.

---

### Task 4

Create a dictionary containing numbers from `1` to `20`.

Include only even numbers and store their squares as values.

---

### Task 5

Create a marks dictionary and use dictionary comprehension to display only marks greater than `75`.

---

### Task 6

Create a dictionary of employee salaries and increase every salary by `10%`.

---

### Task 7

Create two lists:

```python
subjects = ["Python", "SQL", "Git", "HTML"]
marks = [90, 85, 80, 88]
```

Use `zip()` and dictionary comprehension to create a marks dictionary.

---

### Task 8

Create a dictionary of names and ages.

Use dictionary comprehension to create a dictionary containing only people whose age is `18` or above.

---

### Task 9

Create a dictionary of numbers and use `if-else` to classify every number as `"Even"` or `"Odd"`.

---

### Task 10

Create a dictionary of student marks and use dictionary comprehension to assign grades.

Use:

```text
80+  → A
60-79 → B
40-59 → C
Below 40 → F
```

---

### Task 11

Create a product dictionary and use dictionary comprehension to apply a `10%` discount to every product.

---

### Task 12

Create a real-world dictionary and use at least three different dictionary comprehension techniques:

* Transformation
* Filtering
* `if-else`

---

# 🧠 54. Memory Tricks

Remember the basic structure:

```text
{key : value for item in iterable}
          ↓
       DICTIONARY
     COMPREHENSION
```

---

Remember filtering:

```text
{key: value for item in iterable if condition}
                              ↓
                            FILTER
```

---

Remember `if-else`:

```text
{key: value_if_true if condition else value_if_false for item in iterable}
          ↓
       CHOOSE VALUE
```

---

Remember:

```text
key:value
   ↓
Dictionary
```

```text
for
 ↓
Repeat
```

```text
if
 ↓
Filter
```

```text
if-else
 ↓
Choose
```

---

# 📌 55. Important Rules to Remember

```text
1. Dictionary comprehension creates dictionaries in a compact way.

2. The basic syntax is:
   {key: value for item in iterable}

3. Dictionary comprehensions use curly braces {}.

4. A dictionary comprehension must contain key:value.

5. A simple comprehension can replace a normal for loop.

6. Expressions can be used for keys and values.

7. An if condition can be used to filter items.

8. if-else can be used to choose between values.

9. With if-else, the conditional expression comes before the for.

10. zip() can combine two lists for dictionary creation.

11. Dictionary comprehension can transform existing dictionaries.

12. Dictionary comprehension can filter existing dictionaries.

13. Dictionary keys must be unique.

14. If duplicate keys are generated, later values overwrite earlier values.

15. Set comprehension has no key:value pair.

16. Dictionary comprehension has a key:value pair.

17. Nested dictionary comprehensions are possible.

18. Very complicated comprehensions should usually be replaced with normal loops.

19. Dictionary comprehension is useful for short, readable transformations.

20. Always focus on readability when using comprehensions.
```

---

# 📊 56. Dictionary Comprehension Structure

```text
                         DICTIONARY
                              │
                              ↓
                   DICTIONARY COMPREHENSION
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
            KEY             VALUE             LOOP
             │                │                │
             ↓                ↓                ↓
       key expression   value expression    for item
                                                │
                                                ↓
                                           ITERABLE
                                                │
                                                ↓
                                          OPTIONAL
                                                │
                                      ┌─────────┴─────────┐
                                      ↓                   ↓
                                     if               if-else
                                      ↓                   ↓
                                   FILTER            CHOOSE VALUE
```

---

# 📚 57. Complete Dictionary Comprehension Cheat Sheet

### Basic Dictionary Comprehension

```python
squares = {
    x: x ** 2
    for x in range(1, 6)
}
```

### With `if`

```python
even = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}
```

### With `if-else`

```python
result = {
    x: "Even" if x % 2 == 0 else "Odd"
    for x in range(1, 6)
}
```

### From a List

```python
marks = {
    subject: 0
    for subject in subjects
}
```

### From Two Lists

```python
result = {
    key: value
    for key, value in zip(keys, values)
}
```

### Transform Dictionary Values

```python
result = {
    key: value * 2
    for key, value in data.items()
}
```

### Transform Dictionary Keys

```python
result = {
    key.upper(): value
    for key, value in data.items()
}
```

### Filter Dictionary

```python
result = {
    key: value
    for key, value in data.items()
    if value > 50
}
```

### Invert Dictionary

```python
inverted = {
    value: key
    for key, value in data.items()
}
```

### Nested Dictionary Comprehension

```python
result = {
    x: {
        y: x * y
        for y in range(1, 4)
    }
    for x in range(1, 4)
}
```

---

# 🏆 58. Dictionary Comprehension Mastery

```text
                         DICTIONARY
                              │
                              ↓
                  Dictionary Comprehension
                              │
          ┌───────────────────┼───────────────────┐
          ↓                   ↓                   ↓
       CREATE             TRANSFORM             FILTER
          │                   │                   │
          ↓                   ↓                   ↓
      From list          Keys / Values       Using if
      From two lists     Expressions         Conditions
      Using zip()        Calculations
          │                   │
          └───────────────────┼───────────────────┘
                              ↓
                         ADVANCED
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
                 if-else              Nested
                    │                   │
                    ↓                   ↓
              Classification       Dictionaries
```

---

# 📚 59. Summary

In this lesson, you learned:

* What dictionary comprehension is.
* Why dictionary comprehension is useful.
* The basic syntax of dictionary comprehension.
* How dictionary comprehension works with `for`.
* How to create dictionaries using expressions.
* How to create dictionaries from lists.
* How to create dictionaries from two lists.
* How to use `zip()` with dictionary comprehension.
* How to use `if` conditions.
* How to filter dictionary data.
* How to use `if-else`.
* How to classify dictionary values.
* How to transform dictionary keys.
* How to transform dictionary values.
* How to transform both keys and values.
* How to invert a dictionary.
* How to handle duplicate generated keys.
* How to create nested dictionary comprehensions.
* How to use dictionary comprehension in real-world applications.
* Common mistakes in dictionary comprehension.
* When to use dictionary comprehension and when to use normal loops.

---

# 🎯 Topic Completion Checklist

* [x] I understand what dictionary comprehension is.
* [x] I know the syntax of dictionary comprehension.
* [x] I can create dictionaries using comprehension.
* [x] I can use expressions in dictionary comprehension.
* [x] I can use `for` loops in dictionary comprehension.
* [x] I can use `if` conditions.
* [x] I can use `if-else` conditions.
* [x] I can filter dictionary data.
* [x] I can transform dictionary values.
* [x] I can transform dictionary keys.
* [x] I can create dictionaries from lists.
* [x] I can create dictionaries from two lists.
* [x] I can use `zip()`.
* [x] I understand duplicate-key behavior.
* [x] I can invert a dictionary.
* [x] I understand nested dictionary comprehension.
* [x] I can use dictionary comprehension with real-world data.
* [x] I understand the difference between set and dictionary comprehension.
* [x] I can identify common mistakes.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the assignment.
* [x] I can write dictionary comprehensions without looking at my notes.

---


## ⭐ Quote of the Day

> **"Dictionary comprehension turns repetitive dictionary-building code into concise, powerful, and readable Python."** 🐍📚
