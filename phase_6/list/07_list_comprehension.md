# 🐍 Python Master Course

# 📦 Phase 6: Collections – Lists

## 📌 Topic 7: List Comprehension

**Difficulty:** ⭐⭐⭐ Intermediate → ⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand what list comprehension is.
- [ ] Understand the syntax of list comprehension.
- [ ] Create lists using list comprehension.
- [ ] Use expressions in list comprehension.
- [ ] Use conditions with list comprehension.
- [ ] Use `if-else` with list comprehension.
- [ ] Work with strings using list comprehension.
- [ ] Use functions inside list comprehension.
- [ ] Work with nested list comprehension.
- [ ] Convert normal loops into list comprehensions.
- [ ] Use list comprehension in real-world programs.
- [ ] Understand when list comprehension should and should not be used.

---

# 📖 What is List Comprehension?

**List comprehension** is a short and powerful way to create a new list from an existing iterable.

Instead of writing several lines of code using a `for` loop, we can often create the same list in a single line.

---

# 📌 Basic Syntax

```python
new_list = [expression for item in iterable]
```

There are three important parts:

```text
[ expression   for   item   in   iterable ]
       ↓          ↓      ↓       ↓
      WHAT?     LOOP   VALUE   SOURCE
```

---

# 📖 Basic Example

Suppose we want to create a list containing numbers from `1` to `5`.

### Normal `for` loop

```python
numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

### Using List Comprehension

```python
numbers = [number for number in range(1, 6)]

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5]
```

The list comprehension is shorter.

---

# 📌 Example 1: Squares

Create a list containing the squares of numbers from `1` to `5`.

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]

```

---

# 📌 Understanding the Code

```python
[number ** 2 for number in range(1, 6)]
```

Break it down:

```text
number ** 2
     ↓
Expression

for number
     ↓
Loop variable

range(1, 6)
     ↓
Iterable
```

Python takes each number:

```text
1 → 1² → 1
2 → 2² → 4
3 → 3² → 9
4 → 4² → 16
5 → 5² → 25
```

Result:

```text
[1, 4, 9, 16, 25]
```

---

# 📌 Example 2: Cubes

```python
cubes = [number ** 3 for number in range(1, 6)]

print(cubes)
```

Output:

```text
[1, 8, 27, 64, 125]
```

---

# 📌 Example 3: Multiply by 10

```python
numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers]

print(result)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 📌 Example 4: Add 5

```python
numbers = [10, 20, 30, 40]

result = [number + 5 for number in numbers]

print(result)
```

Output:

```text
[15, 25, 35, 45]
```

---

# 📌 Example 5: Convert Strings to Uppercase

```python
names = ["aisha", "saniya", "rohan"]

upper_names = [name.upper() for name in names]

print(upper_names)
```

Output:

```text
['AISHA', 'SANIYA', 'ROHAN']
```

---

# 📌 Example 6: Convert Strings to Lowercase

```python
names = ["APPLE", "BANANA", "MANGO"]

lower_names = [name.lower() for name in names]

print(lower_names)
```

Output:

```text
['apple', 'banana', 'mango']
```

---

# 📌 Example 7: Get String Lengths

```python
names = ["Aisha", "Saniya", "Rohan"]

lengths = [len(name) for name in names]

print(lengths)
```

Output:

```text
[5, 6, 5]
```

---

# 📌 List Comprehension with `range()`

`range()` is commonly used with list comprehension.

```python
numbers = [number for number in range(1, 11)]

print(numbers)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

# 📌 Even Numbers

We can use a condition to select only even numbers.

### Syntax

```python
new_list = [expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

---

# 🧠 Understanding the Condition

```python
[number for number in numbers if number % 2 == 0]
```

means:

```text
Take number
     ↓
from numbers
     ↓
but only if
     ↓
number % 2 == 0
```

So:

```text
1 → ❌
2 → ✅
3 → ❌
4 → ✅
5 → ❌
6 → ✅
```

Result:

```text
[2, 4, 6]
```

---

# 📌 Odd Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = [number for number in numbers if number % 2 != 0]

print(odd_numbers)
```

Output:

```text
[1, 3, 5]
```

---

# 📌 Numbers Greater Than 10

```python
numbers = [5, 12, 8, 20, 15, 3]

result = [number for number in numbers if number > 10]

print(result)
```

Output:

```text
[12, 20, 15]
```

---

# 📌 Numbers Less Than 50

```python
numbers = [10, 60, 25, 80, 40]

result = [number for number in numbers if number < 50]

print(result)
```

Output:

```text
[10, 25, 40]
```

---

# 📌 Numbers Divisible by 5

```python
numbers = [10, 12, 15, 22, 25, 31, 40]

result = [number for number in numbers if number % 5 == 0]

print(result)
```

Output:

```text
[10, 15, 25, 40]
```

---

# 📌 Using `if-else`

List comprehension can also contain an `if-else`.

### Syntax

```python
new_list = [value_if_true if condition else value_if_false for item in iterable]
```

---

# 📖 Example: Even or Odd

```python
numbers = [1, 2, 3, 4, 5]

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# 📌 Example: Pass or Fail

```python
marks = [85, 32, 76, 28, 90]

result = [
    "Pass" if mark >= 35 else "Fail"
    for mark in marks
]

print(result)
```

Output:

```text
['Pass', 'Fail', 'Pass', 'Fail', 'Pass']
```

---

# 📌 Example: Positive or Negative

```python
numbers = [10, -5, 20, -8, 0]

result = [
    "Positive" if number > 0 else "Not Positive"
    for number in numbers
]

print(result)
```

Output:

```text
['Positive', 'Not Positive', 'Positive', 'Not Positive', 'Not Positive']
```

---

# 📌 Example: Adult or Minor

```python
ages = [12, 18, 25, 15, 30]

result = [
    "Adult" if age >= 18 else "Minor"
    for age in ages
]

print(result)
```

Output:

```text
['Minor', 'Adult', 'Adult', 'Minor', 'Adult']
```

---

# 📌 List Comprehension with Strings

You can use list comprehension with strings.

---

## Example: Characters

```python
word = "Python"

letters = [letter for letter in word]

print(letters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n']
```

---

# 📌 Example: Uppercase Characters

```python
word = "python"

letters = [letter.upper() for letter in word]

print(letters)
```

Output:

```text
['P', 'Y', 'T', 'H', 'O', 'N']
```

---

# 📌 Example: Vowels

```python
word = "programming"

vowels = [
    letter
    for letter in word
    if letter in "aeiou"
]

print(vowels)
```

Output:

```text
['o', 'a', 'i']
```

---

# 📌 Example: Remove Spaces

```python
text = "Python is easy"

characters = [char for char in text if char != " "]

print(characters)
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n', 'i', 's', 'e', 'a', 's', 'y']
```

---

# 📌 Example: Words with More Than 5 Characters

```python
words = ["Python", "Java", "Programming", "C", "Developer"]

result = [word for word in words if len(word) > 5]

print(result)
```

Output:

```text
['Python', 'Programming', 'Developer']
```

---

# 📌 List Comprehension with Functions

You can call functions inside a list comprehension.

```python
numbers = [1, 2, 3, 4, 5]

result = [abs(number - 3) for number in numbers]

print(result)
```

Output:

```text
[2, 1, 0, 1, 2]
```

---

# 📌 Using `round()`

```python
prices = [10.567, 20.432, 30.876]

rounded_prices = [round(price, 2) for price in prices]

print(rounded_prices)
```

Output:

```text
[10.57, 20.43, 30.88]
```

---

# 📌 Using `str()`

```python
numbers = [10, 20, 30]

text_numbers = [str(number) for number in numbers]

print(text_numbers)
```

Output:

```text
['10', '20', '30']
```

---

# 📌 Using `int()`

```python
values = ["10", "20", "30"]

numbers = [int(value) for value in values]

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

# 📌 Nested List Comprehension

List comprehension can also be used with nested loops.

Consider:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

We can flatten it into one list.

```python
result = [
    value
    for row in matrix
    for value in row
]

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

---

# 🧠 Understanding Nested List Comprehension

This:

```python
result = [
    value
    for row in matrix
    for value in row
]
```

is equivalent to:

```python
result = []

for row in matrix:
    for value in row:
        result.append(value)
```

The first `for` processes the rows.

The second `for` processes each value inside the row.

---

# 📌 Creating a Matrix

Nested list comprehension can create a matrix.

```python
matrix = [
    [0 for column in range(3)]
    for row in range(3)
]

print(matrix)
```

Output:

```text
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

# 📌 Creating a Multiplication Pattern

```python
matrix = [
    [row * column for column in range(1, 4)]
    for row in range(1, 4)
]

print(matrix)
```

Output:

```text
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

# 📌 Nested List with a Condition

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_numbers = [
    value
    for row in matrix
    for value in row
    if value % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 📌 Multiple Conditions

You can use multiple conditions.

```python
numbers = range(1, 21)

result = [
    number
    for number in numbers
    if number % 2 == 0
    if number > 10
]

print(result)
```

Output:

```text
[12, 14, 16, 18, 20]
```

This means:

```text
Number must be even
AND
Number must be greater than 10
```

---

# 📌 Using `and`

You can also combine conditions.

```python
numbers = range(1, 21)

result = [
    number
    for number in numbers
    if number % 2 == 0 and number > 10
]

print(result)
```

Output:

```text
[12, 14, 16, 18, 20]
```

---

# 📌 Using `or`

```python
numbers = range(1, 11)

result = [
    number
    for number in numbers
    if number < 3 or number > 8
]

print(result)
```

Output:

```text
[1, 2, 9, 10]
```

---

# 🌍 Real-World Example 1: Student Marks

```python
marks = [45, 78, 32, 90, 28, 65]

passed = [mark for mark in marks if mark >= 35]

print(passed)
```

Output:

```text
[45, 78, 90, 65]
```

---

# 🌍 Real-World Example 2: Product Prices

Increase every price by 10%.

```python
prices = [100, 200, 300, 400]

new_prices = [price * 1.10 for price in prices]

print(new_prices)
```

Output:

```text
[110.00000000000001, 220.00000000000003, 330.0, 440.00000000000006]
```

For cleaner output:

```python
new_prices = [round(price * 1.10, 2) for price in prices]

print(new_prices)
```

Output:

```text
[110.0, 220.0, 330.0, 440.0]
```

---

# 🌍 Real-World Example 3: Filtering Products

```python
prices = [500, 1200, 800, 2500, 300]

expensive = [price for price in prices if price > 1000]

print(expensive)
```

Output:

```text
[1200, 2500]
```

---

# 🌍 Real-World Example 4: Convert Temperatures

Convert Celsius to Fahrenheit.

Formula:

```text
F = (C × 9/5) + 32
```

```python
celsius = [0, 10, 20, 30, 40]

fahrenheit = [
    (temperature * 9 / 5) + 32
    for temperature in celsius
]

print(fahrenheit)
```

Output:

```text
[32.0, 50.0, 68.0, 86.0, 104.0]
```

---

# 🌍 Real-World Example 5: Extract Emails

```python
contacts = [
    "aisha@gmail.com",
    "rohan@yahoo.com",
    "saniya@gmail.com",
    "admin@company.com"
]

gmail_users = [
    email
    for email in contacts
    if email.endswith("@gmail.com")
]

print(gmail_users)
```

Output:

```text
['aisha@gmail.com', 'saniya@gmail.com']
```

---

# 🌍 Real-World Example 6: Clean Data

```python
names = [" Aisha ", " Saniya ", " Rohan "]

clean_names = [name.strip() for name in names]

print(clean_names)
```

Output:

```text
['Aisha', 'Saniya', 'Rohan']
```

---

# 🌍 Real-World Example 7: Extract Positive Numbers

```python
numbers = [-10, 20, -5, 30, -2, 40]

positive = [number for number in numbers if number > 0]

print(positive)
```

Output:

```text
[20, 30, 40]
```

---

# 📌 Normal Loop vs List Comprehension

## Normal Loop

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

## List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Both produce:

```text
[1, 4, 9, 16, 25]
```

---

# 📊 Comparison

| Normal Loop | List Comprehension |
|---|---|
| More lines | Fewer lines |
| Easy for beginners | More concise |
| Can be easier for complex logic | Best for simple transformations |
| Uses `append()` | Creates list directly |

---

# 📌 When Should You Use List Comprehension?

Use list comprehension when:

- The operation is simple.
- You are creating a new list.
- The logic is easy to understand.
- You are transforming or filtering values.

Example:

```python
squares = [x ** 2 for x in numbers]
```

---

# ⚠️ When Should You NOT Use List Comprehension?

Avoid very complicated comprehensions.

### Hard to Read

```python
result = [x * 2 if x > 10 else x / 2 if x > 5 else x + 1 for x in numbers]
```

Although valid Python, this can be difficult to understand.

A normal loop may be clearer:

```python
result = []

for x in numbers:
    if x > 10:
        result.append(x * 2)
    elif x > 5:
        result.append(x / 2)
    else:
        result.append(x + 1)
```

### 🧠 Rule

> **Shorter code is not always better code. Readability is important.**

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Incorrect Order

Incorrect:

```python
[x for x in numbers x > 5]
```

Correct:

```python
[x for x in numbers if x > 5]
```

---

# ❌ Mistake 2: Forgetting the Expression

Incorrect:

```python
[for x in numbers]
```

Correct:

```python
[x for x in numbers]
```

---

# ❌ Mistake 3: Confusing `if` Position

For filtering:

```python
[x for x in numbers if x > 5]
```

For `if-else`:

```python
["Yes" if x > 5 else "No" for x in numbers]
```

Notice the difference.

---

# 📊 `if` vs `if-else`

### Filtering

```python
[x for x in numbers if x > 5]
```

Meaning:

```text
Keep only values greater than 5.
```

### `if-else`

```python
["Large" if x > 5 else "Small" for x in numbers]
```

Meaning:

```text
Every value gets a result:
Large OR Small.
```

---

# 🧠 Important Syntax Patterns

## Basic

```python
[expression for item in iterable]
```

---

## With Condition

```python
[expression for item in iterable if condition]
```

---

## With `if-else`

```python
[value_if_true if condition else value_if_false for item in iterable]
```

---

## Nested

```python
[expression for item1 in iterable1 for item2 in iterable2]
```

---

# 🔥 Advanced Example: Flatten a Matrix

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [value for row in matrix for value in row]

print(flat)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

# 🔥 Advanced Example: Flatten Only Even Values

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_values = [
    value
    for row in matrix
    for value in row
    if value % 2 == 0
]

print(even_values)
```

Output:

```text
[2, 4, 6, 8]
```

---

# 🔥 Advanced Example: Create a Multiplication Table

```python
table = [
    [row * column for column in range(1, 6)]
    for row in range(1, 6)
]

for row in table:
    print(row)
```

Output:

```text
[1, 2, 3, 4, 5]
[2, 4, 6, 8, 10]
[3, 6, 9, 12, 15]
[4, 8, 12, 16, 20]
[5, 10, 15, 20, 25]
```

---

# 🔥 Advanced Example: Find Vowels in Multiple Words

```python
words = ["python", "programming", "developer"]

vowels = [
    letter
    for word in words
    for letter in word
    if letter in "aeiou"
]

print(vowels)
```

Output:

```text
['o', 'o', 'a', 'i', 'e', 'e', 'o', 'e']
```

---

# 🔥 Advanced Example: Convert Nested Marks

```python
marks = [
    [80, 90, 70],
    [75, 85, 95],
    [88, 92, 84]
]

updated_marks = [
    mark + 5
    for student in marks
    for mark in student
]

print(updated_marks)
```

Output:

```text
[85, 95, 75, 80, 90, 100, 93, 97, 89]
```

---

# 🏋️ Practice Programs

## Beginner

### 1. Create numbers from 1 to 10

```python
numbers = [x for x in range(1, 11)]

print(numbers)
```

---

### 2. Create squares

```python
squares = [x ** 2 for x in range(1, 11)]

print(squares)
```

---

### 3. Create cubes

```python
cubes = [x ** 3 for x in range(1, 6)]

print(cubes)
```

---

### 4. Multiply every number by 5

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 5 for x in numbers]

print(result)
```

---

# 🏋️ Intermediate Practice

### 5. Extract even numbers

```python
numbers = range(1, 21)

even = [x for x in numbers if x % 2 == 0]

print(even)
```

---

### 6. Extract odd numbers

```python
numbers = range(1, 21)

odd = [x for x in numbers if x % 2 != 0]

print(odd)
```

---

### 7. Find numbers greater than 50

```python
numbers = [10, 60, 45, 80, 25, 90]

result = [x for x in numbers if x > 50]

print(result)
```

---

### 8. Convert names to uppercase

```python
names = ["aisha", "saniya", "rohan"]

result = [name.upper() for name in names]

print(result)
```

---

# 🚀 Advanced Practice

### 9. Pass or Fail

```python
marks = [85, 32, 90, 28, 76]

result = [
    "Pass" if mark >= 35 else "Fail"
    for mark in marks
]

print(result)
```

---

### 10. Flatten a nested list

```python
numbers = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = [x for row in numbers for x in row]

print(result)
```

---

### 11. Extract even numbers from a matrix

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    x
    for row in matrix
    for x in row
    if x % 2 == 0
]

print(result)
```

---

# 🏆 Challenge 1: Student Marks

Given:

```python
marks = [35, 42, 78, 29, 90, 33, 67]
```

Create:

1. [x] A list of passing marks.
2. [x] A list of failing marks.
3. [x] A list containing `"Pass"` or `"Fail"` for every mark.
4. [x] A list of marks increased by 5.

---

# 🏆 Challenge 2: Product Prices

Given:

```python
prices = [500, 1200, 800, 2500, 300]
```

Create:

1. [x] A list containing prices above `1000`.
2. [x] A list containing prices below `1000`.
3. [x] A list with a 10% discount applied.
4. [x] A list containing only even prices.

---

# 🏆 Challenge 3: Strings

Given:

```python
words = ["Python", "Java", "JavaScript", "C", "HTML"]
```

Create:

1. [x] A list containing the lengths of all words.
2. [x] A list containing uppercase versions.
3. [x] A list containing words longer than 4 characters.
4. [x] A list containing words starting with `"J"`.

---

# 🏆 Challenge 4: Nested Lists

Given:

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

Use list comprehension to:

1. [x] Flatten the matrix.
2. [x] Extract all even numbers.
3. [x] Extract numbers greater than 50.
4. [x] Create a list containing every number multiplied by 2.

---

# ❓ Interview Questions

- [x] What is list comprehension?
- [x] What is the syntax of list comprehension?
- [x] What is the advantage of list comprehension?
- [x] How do you add a condition to list comprehension?
- [x] How do you use `if-else` in list comprehension?
- [x] What is nested list comprehension?
- [x] Can list comprehension work with strings?
- [x] Can functions be used inside list comprehension?
- [x] How is list comprehension different from a normal `for` loop?
- [x] When should you avoid list comprehension?
- [x] How do you flatten a nested list using list comprehension?

---

# 📊 List Comprehension Cheat Sheet

| Task | List Comprehension |
|---|---|
| Create numbers | `[x for x in range(10)]` |
| Squares | `[x ** 2 for x in numbers]` |
| Even numbers | `[x for x in numbers if x % 2 == 0]` |
| Odd numbers | `[x for x in numbers if x % 2 != 0]` |
| Greater than 10 | `[x for x in numbers if x > 10]` |
| Uppercase | `[x.upper() for x in words]` |
| String length | `[len(x) for x in words]` |
| If-else | `["Even" if x % 2 == 0 else "Odd" for x in numbers]` |
| Flatten nested list | `[x for row in matrix for x in row]` |

---

# 🧠 Easy Memory Trick

Remember the basic pattern:

```text
[ WHAT  for  EACH  in  SOURCE ]
```

Example:

```python
[x ** 2 for x in numbers]
```

Read it as:

> **For each `x` in `numbers`, put `x ** 2` into the new list.**

With filtering:

```python
[x for x in numbers if x > 10]
```

Read it as:

> **For each `x` in `numbers`, put `x` into the list if `x > 10`.**

With `if-else`:

```python
["Even" if x % 2 == 0 else "Odd" for x in numbers]
```

Read it as:

> **For each `x`, put `"Even"` if it is even, otherwise put `"Odd"`.**

---

# 🎯 Topic Completion Checklist

- [x] I understand list comprehension.
- [x] I know the basic syntax.
- [x] I can create lists using `range()`.
- [x] I can perform calculations.
- [x] I can filter values using `if`.
- [x] I can use `if-else`.
- [x] I can work with strings.
- [x] I can use functions.
- [x] I understand nested list comprehension.
- [x] I can flatten nested lists.
- [x] I can use multiple conditions.
- [x] I can convert normal loops into list comprehensions.
- [x] I know when list comprehension is useful.
- [x] I know when a normal loop is more readable.
- [x] I completed the practice programs.
- [x] I completed all challenges.

---

# 🎉 Phase 6 – Lists Completed!

You have now covered all the topics in the **Lists** section:

- [x] Creating Lists
- [x] Indexing
- [x] Slicing
- [x] List Methods
- [x] Nested Lists
- [x] Copying Lists
- [x] List Comprehension

---

# 🚀 Next Topic

➡️ **Next Collection Topic: Tuples**

Topics will include:

- Creating Tuples
- Tuple Methods
- Tuple Packing
- Tuple Unpacking



