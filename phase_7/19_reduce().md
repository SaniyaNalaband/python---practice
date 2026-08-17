# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 19: `reduce()`

**Difficulty:** ⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what `reduce()` is.
* [ ] Understand why `reduce()` is used.
* [ ] Understand the syntax of `reduce()`.
* [ ] Import `reduce()` from the `functools` module.
* [ ] Use `reduce()` with lists.
* [ ] Use `reduce()` with numbers.
* [ ] Use `reduce()` with strings.
* [ ] Understand the role of the accumulator.
* [ ] Understand the role of the current value.
* [ ] Understand how `reduce()` processes elements.
* [ ] Use `reduce()` with lambda functions.
* [ ] Use an initializer with `reduce()`.
* [ ] Understand `reduce()` with and without an initializer.
* [ ] Use `reduce()` with conditions.
* [ ] Use `reduce()` with different operations.
* [ ] Combine `reduce()` with other functions.
* [ ] Use `reduce()` in real-world applications.
* [ ] Avoid common mistakes when using `reduce()`.
* [ ] Understand when `reduce()` is appropriate.

---

# 📖 1. What is `reduce()`?

`reduce()` is a function used to **combine all elements of an iterable into a single final value**.

Unlike functions such as `map()` and `filter()`, which usually produce multiple results, `reduce()` repeatedly applies a function and reduces many values into **one value**.

For example:

```python
numbers = [1, 2, 3, 4]
```

Using `reduce()`, we can calculate:

```text
1 + 2 + 3 + 4
```

The final result is:

```text
10
```

`reduce()` is available in Python's `functools` module.

---

# 🧠 2. Importing `reduce()`

Before using `reduce()`, import it from `functools`.

```python
from functools import reduce
```

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
10
```

Here:

```text
functools
   ↓
 reduce()
   ↓
Combines elements
   ↓
One final result
```

---

# 📚 3. Syntax of `reduce()`

The general syntax is:

```python
reduce(function, iterable)
```

There is also an optional initializer:

```python
reduce(function, iterable, initializer)
```

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

---

# 🔍 4. Understanding the Parameters

`reduce()` mainly works with three components:

```text
reduce(function, iterable, initializer)
```

### `function`

The operation that should be repeatedly applied.

### `iterable`

The collection whose elements will be processed.

Examples:

```text
list
tuple
set
string
```

### `initializer`

An optional starting value.

Example:

```python
reduce(lambda a, b: a + b, numbers, 10)
```

The initializer starts the reduction from `10`.

---

# 🧠 5. Basic Example of `reduce()`

Let's calculate the sum of numbers.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
15
```

The values are combined like this:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

Final result:

```text
15
```

---

# 🔄 6. How `reduce()` Works

Consider:

```python
numbers = [1, 2, 3, 4]
```

And:

```python
reduce(lambda a, b: a + b, numbers)
```

Internally, the process is approximately:

```text
Step 1:
a = 1
b = 2
1 + 2 = 3

Step 2:
a = 3
b = 3
3 + 3 = 6

Step 3:
a = 6
b = 4
6 + 4 = 10
```

Final result:

```text
10
```

The important idea is:

```text
Previous result
      +
Next element
      ↓
New result
      ↓
Next element
      ↓
Final result
```

---

# 🧩 7. Understanding the Accumulator

The first parameter of the lambda often acts as an **accumulator**.

Example:

```python
from functools import reduce

numbers = [2, 4, 6, 8]

result = reduce(lambda accumulator, current: accumulator + current, numbers)

print(result)
```

Output:

```text
20
```

Here:

```text
accumulator → stores the previous result
current     → current element
```

For example:

```text
accumulator   current
     2           4
     ↓           ↓
     2 + 4 = 6

     6           6
     ↓           ↓
     6 + 6 = 12

    12           8
     ↓           ↓
    12 + 8 = 20
```

---

# 🔢 8. `reduce()` for Multiplication

`reduce()` can also multiply values.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

Output:

```text
120
```

The calculation is:

```text
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
24 × 5 = 120
```

This type of calculation is useful for calculating factorials.

---

# 🎯 9. Calculating Factorial Using `reduce()`

Factorial of `5` is:

```text
5 × 4 × 3 × 2 × 1 = 120
```

Example:

```python
from functools import reduce

numbers = range(1, 6)

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

Output:

```text
120
```

---

# 🔢 10. Finding the Maximum Value

`reduce()` can also be used to find the largest value.

```python
from functools import reduce

numbers = [25, 80, 45, 95, 60]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print(maximum)
```

Output:

```text
95
```

The comparison happens repeatedly:

```text
25 vs 80 → 80
80 vs 45 → 80
80 vs 95 → 95
95 vs 60 → 95
```

Final result:

```text
95
```

---

# 🔽 11. Finding the Minimum Value

Similarly, we can find the smallest value.

```python
from functools import reduce

numbers = [25, 80, 45, 95, 60]

minimum = reduce(lambda a, b: a if a < b else b, numbers)

print(minimum)
```

Output:

```text
25
```

---

# 🔤 12. Using `reduce()` with Strings

`reduce()` can combine strings.

Example:

```python
from functools import reduce

words = ["Python", "is", "powerful"]

sentence = reduce(lambda a, b: a + " " + b, words)

print(sentence)
```

Output:

```text
Python is powerful
```

The process is:

```text
Python + is
        ↓
Python is

Python is + powerful
        ↓
Python is powerful
```

---

# 🔗 13. Joining Characters Using `reduce()`

Example:

```python
from functools import reduce

letters = ["P", "y", "t", "h", "o", "n"]

word = reduce(lambda a, b: a + b, letters)

print(word)
```

Output:

```text
Python
```

---

# 🧮 14. Using `reduce()` with Subtraction

`reduce()` can perform subtraction as well.

```python
from functools import reduce

numbers = [100, 20, 10, 5]

result = reduce(lambda a, b: a - b, numbers)

print(result)
```

Output:

```text
65
```

Calculation:

```text
100 - 20 = 80
80 - 10 = 70
70 - 5 = 65
```

---

# ➗ 15. Using `reduce()` with Division

Example:

```python
from functools import reduce

numbers = [100, 2, 5]

result = reduce(lambda a, b: a / b, numbers)

print(result)
```

Output:

```text
10.0
```

Calculation:

```text
100 / 2 = 50
50 / 5 = 10
```

---

# ⚙️ 16. Using an Initializer

An initializer provides the starting value for the reduction.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers, 10)

print(result)
```

Output:

```text
20
```

The calculation starts from `10`:

```text
10 + 1 = 11
11 + 2 = 13
13 + 3 = 16
16 + 4 = 20
```

---

# ⚖️ 17. `reduce()` Without Initializer vs With Initializer

Without an initializer:

```python
from functools import reduce

numbers = [1, 2, 3]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
6
```

With an initializer:

```python
result = reduce(lambda a, b: a + b, numbers, 10)

print(result)
```

Output:

```text
16
```

Comparison:

```text
Without initializer:

1 + 2 + 3
↓
6


With initializer:

10 + 1 + 2 + 3
↓
16
```

---

# 🧠 18. `reduce()` with a Tuple

`reduce()` works with tuples because tuples are iterable.

```python
from functools import reduce

numbers = (5, 10, 15, 20)

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```text
50
```

---

# 🧩 19. `reduce()` with a Set

A set can also be used because it is iterable.

```python
from functools import reduce

numbers = {2, 4, 6, 8}

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```text
20
```

Remember that sets are unordered, so you should not depend on a particular processing order for order-sensitive operations such as subtraction or division.

---

# 🔍 20. `reduce()` with Conditions

A condition can be placed inside the lambda function.

Example:

```python
from functools import reduce

numbers = [10, 25, 8, 40, 15]

maximum = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(maximum)
```

Output:

```text
40
```

Here the condition:

```python
a if a > b else b
```

means:

```text
If a is greater than b
        ↓
    keep a
Otherwise
        ↓
    keep b
```

---

# 🎯 21. Sum of Only Positive Numbers

We can use a condition to process numbers differently.

```python
from functools import reduce

numbers = [10, -5, 20, -3, 15]

result = reduce(
    lambda a, b: a + b if b > 0 else a,
    numbers,
    0
)

print(result)
```

Output:

```text
45
```

Only positive numbers are added:

```text
10 + 20 + 15 = 45
```

---

# 🧠 22. Understanding `reduce()` Step by Step

Consider:

```python
numbers = [2, 3, 4]
```

And:

```python
reduce(lambda a, b: a * b, numbers)
```

Processing:

```text
Initial:
a = 2
b = 3

2 × 3 = 6

Next:
a = 6
b = 4

6 × 4 = 24
```

Final result:

```text
24
```

The most important concept is:

```text
Two values
    ↓
Function
    ↓
One result
    ↓
Combined with next value
    ↓
One result
    ↓
Continue
    ↓
Final single value
```

---

# 🔁 23. `reduce()` vs `map()` vs `filter()`

These functions have different purposes.

| Function   | Purpose                | Typical Result          |
| ---------- | ---------------------- | ----------------------- |
| `map()`    | Transform each element | Many transformed values |
| `filter()` | Select elements        | Some elements           |
| `reduce()` | Combine elements       | One final value         |

Example:

```python
numbers = [1, 2, 3, 4]
```

`map()`:

```text
[2, 4, 6, 8]
```

`filter()`:

```text
[2, 4]
```

`reduce()`:

```text
10
```

Remember:

```text
map()
 ↓
Transform

filter()
 ↓
Select

reduce()
 ↓
Combine
```

---

# 🔗 24. Combining `filter()` and `reduce()`

You can combine functional programming tools.

Example:

```python
from functools import reduce

numbers = [10, 15, 20, 25, 30]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

total = reduce(lambda a, b: a + b, even_numbers)

print(total)
```

Output:

```text
60
```

The process is:

```text
Original:

10, 15, 20, 25, 30

filter()
   ↓

10, 20, 30

reduce()
   ↓

10 + 20 + 30

   ↓

60
```

---

# 🔗 25. Combining `map()` and `reduce()`

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

squared = map(lambda x: x ** 2, numbers)

total = reduce(lambda a, b: a + b, squared)

print(total)
```

Output:

```text
30
```

The process:

```text
1, 2, 3, 4
     ↓
   map()
     ↓
1, 4, 9, 16
     ↓
 reduce()
     ↓
30
```

---

# 🛒 26. Real-World Example: Shopping Cart

Suppose a shopping cart contains product prices.

```python
from functools import reduce

prices = [55000, 800, 1500]

total = reduce(lambda a, b: a + b, prices)

print("Cart Total:", total)
```

Output:

```text
Cart Total: 57300
```

The prices are combined into one final total.

---

# 💰 27. Real-World Example: Calculate Total Salary

Suppose a company has several employees.

```python
from functools import reduce

salaries = [35000, 42000, 50000, 38000]

total_salary = reduce(lambda a, b: a + b, salaries)

print("Total Salary:", total_salary)
```

Output:

```text
Total Salary: 165000
```

---

# 📊 28. Real-World Example: Total Marks

A student's marks are stored in a list.

```python
from functools import reduce

marks = [85, 90, 78, 88, 92]

total = reduce(lambda a, b: a + b, marks)

print("Total Marks:", total)
```

Output:

```text
Total Marks: 433
```

---

# 🧮 29. Real-World Example: Calculate Average

First calculate the total using `reduce()`.

```python
from functools import reduce

marks = [85, 90, 78, 88, 92]

total = reduce(lambda a, b: a + b, marks)

average = total / len(marks)

print("Average:", average)
```

Output:

```text
Average: 86.6
```

Here:

```text
reduce()
   ↓
Calculate total

len()
   ↓
Count values

total / count
   ↓
Average
```

---

# 🏆 30. Real-World Example: Highest Transaction

Suppose a bank account has several transactions.

```python
from functools import reduce

transactions = [2500, 8500, 1200, 15000, 6400]

highest = reduce(lambda a, b: a if a > b else b, transactions)

print("Highest Transaction:", highest)
```

Output:

```text
Highest Transaction: 15000
```

---

# 🧾 31. Real-World Example: Invoice Total

Suppose an invoice contains several item prices.

```python
from functools import reduce

prices = [1200, 850, 450, 2000]

invoice_total = reduce(lambda a, b: a + b, prices)

print("Invoice Total:", invoice_total)
```

Output:

```text
Invoice Total: 4500
```

---

# 📦 32. Real-World Example: Total Inventory

Suppose a store has quantities of different products.

```python
from functools import reduce

stock = [25, 40, 15, 30, 20]

total_stock = reduce(lambda a, b: a + b, stock)

print("Total Stock:", total_stock)
```

Output:

```text
Total Stock: 130
```

---

# 🧠 33. `reduce()` with a Dictionary

You can use `reduce()` with dictionary values.

```python
from functools import reduce

prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}

total = reduce(lambda a, b: a + b, prices.values())

print(total)
```

Output:

```text
57300
```

Here:

```python
prices.values()
```

provides:

```text
55000
800
1500
```

Then `reduce()` combines them.

---

# 🔍 34. Finding Maximum Dictionary Value

Example:

```python
from functools import reduce

marks = {
    "Python": 90,
    "SQL": 85,
    "Git": 80,
    "HTML": 88
}

highest = reduce(
    lambda a, b: a if a > b else b,
    marks.values()
)

print("Highest Marks:", highest)
```

Output:

```text
Highest Marks: 90
```

---

# 🧩 35. Finding the Student with Highest Marks

Suppose each student has a mark.

```python
from functools import reduce

marks = {
    "Asha": 85,
    "Neha": 92,
    "Kiran": 88,
    "Meera": 90
}

highest = reduce(
    lambda a, b: a if marks[a] > marks[b] else b,
    marks
)

print("Top Student:", highest)
```

Output:

```text
Top Student: Neha
```

Here, `reduce()` is reducing the dictionary keys while comparing their corresponding values.

---

# ⚠️ 36. Common Mistake: Forgetting the Import

This is incorrect:

```python
numbers = [1, 2, 3]

result = reduce(lambda a, b: a + b, numbers)
```

If `reduce` has not been imported, Python raises:

```text
NameError: name 'reduce' is not defined
```

Correct:

```python
from functools import reduce
```

Then:

```python
result = reduce(lambda a, b: a + b, numbers)
```

---

# ⚠️ 37. Common Mistake: Using an Empty Iterable

Consider:

```python
from functools import reduce

numbers = []

result = reduce(lambda a, b: a + b, numbers)
```

This raises:

```text
TypeError
```

because there is no initial value from which the reduction can begin.

You can provide an initializer:

```python
result = reduce(lambda a, b: a + b, numbers, 0)

print(result)
```

Output:

```text
0
```

---

# 🛡️ 38. Using an Initializer with Empty Data

An initializer makes the operation safer when an iterable might be empty.

```python
from functools import reduce

numbers = []

total = reduce(lambda a, b: a + b, numbers, 0)

print(total)
```

Output:

```text
0
```

Think of:

```text
initializer
     ↓
Starting value
```

---

# ⚠️ 39. Common Mistake: Confusing `reduce()` with `sum()`

For simple addition, Python already provides `sum()`.

Instead of:

```python
from functools import reduce

numbers = [10, 20, 30]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

You can simply use:

```python
total = sum(numbers)
```

Both produce:

```text
60
```

Therefore, `reduce()` should not be used merely because it is available.

Use the simplest appropriate tool.

---

# 🧠 40. When Should You Use `reduce()`?

`reduce()` is useful when:

* You need to repeatedly combine values.
* The operation depends on the previous result.
* You need one final accumulated result.
* You are working with functional-style programming.
* A reduction operation is clearer than a manual loop.

Examples:

```text
Sum
Product
Maximum
Minimum
String combination
Custom accumulation
```

---

# ⚖️ 41. `reduce()` vs a Normal Loop

Using a loop:

```python
numbers = [1, 2, 3, 4]

total = 0

for number in numbers:
    total += number

print(total)
```

Using `reduce()`:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Both produce:

```text
10
```

The loop is often easier for beginners to read.

`reduce()` can be useful when the reduction operation itself is the main idea.

---

# 🔄 42. Visualizing `reduce()`

For:

```python
numbers = [2, 4, 6, 8]
```

Using:

```python
reduce(lambda a, b: a + b, numbers)
```

The flow is:

```text
        [2, 4, 6, 8]
              │
              ↓
           2 + 4
              │
              ↓
              6
              │
              ↓
           6 + 6
              │
              ↓
             12
              │
              ↓
           12 + 8
              │
              ↓
             20
```

Final result:

```text
20
```

---

# 🧠 43. Understanding the Accumulator Flow

The general pattern is:

```text
accumulator + current value
             ↓
        new accumulator
             ↓
        next current value
             ↓
        new accumulator
             ↓
          continue
```

For multiplication:

```text
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
```

For addition:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

---

# 📊 44. `reduce()` Processing Table

For:

```python
numbers = [1, 2, 3, 4]
```

Using:

```python
reduce(lambda a, b: a + b, numbers)
```

| Step | Accumulator | Current | Result |
| ---- | ----------- | ------- | ------ |
| 1    | 1           | 2       | 3      |
| 2    | 3           | 3       | 6      |
| 3    | 6           | 4       | 10     |

Final result:

```text
10
```

---

# 🧩 45. `reduce()` with a Custom Function

The function passed to `reduce()` does not have to be a lambda.

Example:

```python
from functools import reduce

def multiply(a, b):
    return a * b

numbers = [2, 3, 4, 5]

result = reduce(multiply, numbers)

print(result)
```

Output:

```text
120
```

This can sometimes make complex logic easier to understand.

---

# 🔢 46. Using `reduce()` to Count Elements

A reduction can also maintain a count.

```python
from functools import reduce

numbers = [10, 20, 30, 40]

count = reduce(lambda count, value: count + 1, numbers, 0)

print(count)
```

Output:

```text
4
```

The values themselves are not important here.

The accumulator counts how many elements have been processed.

---

# 🔤 47. Finding the Longest String

Example:

```python
from functools import reduce

words = ["Python", "JavaScript", "SQL", "HTML"]

longest = reduce(
    lambda a, b: a if len(a) > len(b) else b,
    words
)

print(longest)
```

Output:

```text
JavaScript
```

---

# 🔤 48. Finding the Shortest String

Example:

```python
from functools import reduce

words = ["Python", "JavaScript", "SQL", "HTML"]

shortest = reduce(
    lambda a, b: a if len(a) < len(b) else b,
    words
)

print(shortest)
```

Output:

```text
SQL
```

---

# 🔢 49. Multiplying Only Even Numbers

We can combine `filter()` and `reduce()`.

```python
from functools import reduce

numbers = [2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

result = reduce(lambda a, b: a * b, even_numbers)

print(result)
```

Output:

```text
48
```

Calculation:

```text
2 × 4 × 6 = 48
```

---

# 🌍 50. Real-World Example: Calculate Total Order Value

Suppose an online order contains several item prices.

```python
from functools import reduce

order_prices = [1200, 850, 450, 1600]

total = reduce(lambda a, b: a + b, order_prices, 0)

print("Order Total:", total)
```

Output:

```text
Order Total: 4100
```

The initializer `0` represents the starting total.

---

# 🎯 51. Real-World Example: Total Working Hours

Suppose an employee worked different hours throughout a week.

```python
from functools import reduce

hours = [8, 7, 8, 6, 9]

total_hours = reduce(lambda a, b: a + b, hours, 0)

print("Total Working Hours:", total_hours)
```

Output:

```text
Total Working Hours: 38
```

---

# 📦 52. Real-World Example: Total Items Sold

Suppose a store sold different quantities of products.

```python
from functools import reduce

sold = [15, 20, 12, 18, 25]

total = reduce(lambda a, b: a + b, sold, 0)

print("Total Items Sold:", total)
```

Output:

```text
Total Items Sold: 90
```

---

# 💳 53. Real-World Example: Total Expenses

```python
from functools import reduce

expenses = [500, 1200, 350, 800, 450]

total_expenses = reduce(lambda a, b: a + b, expenses, 0)

print("Total Expenses:", total_expenses)
```

Output:

```text
Total Expenses: 3300
```

---

# 🏆 54. Real-World Example: Highest Exam Score

```python
from functools import reduce

scores = [78, 92, 85, 96, 88]

highest = reduce(
    lambda a, b: a if a > b else b,
    scores
)

print("Highest Score:", highest)
```

Output:

```text
Highest Score: 96
```

---

# ⚠️ 55. Common Mistakes with `reduce()`

### Mistake 1: Forgetting the import

```python
reduce(...)
```

without:

```python
from functools import reduce
```

causes a `NameError`.

---

### Mistake 2: Using an empty iterable without an initializer

```python
reduce(lambda a, b: a + b, [])
```

causes a `TypeError`.

Use:

```python
reduce(lambda a, b: a + b, [], 0)
```

---

### Mistake 3: Returning the wrong value from the function

The reduction function must return the next accumulated value.

Incorrect logic can produce unexpected results.

---

### Mistake 4: Confusing the accumulator with the current value

In:

```python
lambda a, b: a + b
```

`a` is generally the accumulated result and `b` is the next element.

---

### Mistake 5: Using `reduce()` when a simpler function exists

For example:

```python
reduce(lambda a, b: a + b, numbers)
```

can often be replaced with:

```python
sum(numbers)
```

Use `reduce()` when it makes the operation meaningful or when a custom reduction is required.

---

# 📊 56. `reduce()` Comparison Cheat Sheet

| Expression                              | Purpose                  | Result           |
| --------------------------------------- | ------------------------ | ---------------- |
| `reduce(lambda a,b: a+b, numbers)`      | Add values               | One total        |
| `reduce(lambda a,b: a*b, numbers)`      | Multiply values          | One product      |
| `reduce(lambda a,b: max(a,b), numbers)` | Find maximum             | Largest value    |
| `reduce(lambda a,b: min(a,b), numbers)` | Find minimum             | Smallest value   |
| `reduce(lambda a,b: a+b, words)`        | Combine strings          | One string       |
| `reduce(function, iterable, initial)`   | Start with initial value | One final result |

---

# 💻 57. Practice Programs

## 🟢 Easy

### Program 1: Find the Sum

```python
from functools import reduce

numbers = [10, 20, 30, 40]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

---

### Program 2: Find the Product

```python
from functools import reduce

numbers = [2, 3, 4, 5]

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

---

### Program 3: Combine Words

```python
from functools import reduce

words = ["Python", "is", "easy"]

result = reduce(lambda a, b: a + " " + b, words)

print(result)
```

---

### Program 4: Find the Maximum

```python
from functools import reduce

numbers = [25, 80, 45, 95, 60]

result = reduce(lambda a, b: a if a > b else b, numbers)

print(result)
```

---

# 🟡 Medium

### Program 5: Find the Minimum

```python
from functools import reduce

numbers = [25, 80, 45, 95, 60]

result = reduce(lambda a, b: a if a < b else b, numbers)

print(result)
```

---

### Program 6: Use an Initializer

```python
from functools import reduce

numbers = [5, 10, 15]

result = reduce(lambda a, b: a + b, numbers, 100)

print(result)
```

---

### Program 7: Calculate Factorial

```python
from functools import reduce

numbers = range(1, 6)

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

---

### Program 8: Find the Longest Word

```python
from functools import reduce

words = ["Python", "Java", "JavaScript", "SQL"]

result = reduce(
    lambda a, b: a if len(a) > len(b) else b,
    words
)

print(result)
```

---

# 🔴 Advanced

## Program 9: Sum Only Even Numbers

```python
from functools import reduce

numbers = [10, 15, 20, 25, 30]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

result = reduce(lambda a, b: a + b, even_numbers, 0)

print(result)
```

Output:

```text
60
```

---

## Program 10: Product of Even Numbers

```python
from functools import reduce

numbers = [2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

result = reduce(lambda a, b: a * b, even_numbers, 1)

print(result)
```

Output:

```text
48
```

---

## Program 11: Calculate Total Dictionary Values

```python
from functools import reduce

products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}

total = reduce(lambda a, b: a + b, products.values(), 0)

print("Total:", total)
```

---

## Program 12: Find Highest Mark

```python
from functools import reduce

marks = {
    "Python": 90,
    "SQL": 85,
    "Git": 80,
    "HTML": 88
}

highest = reduce(
    lambda a, b: a if a > b else b,
    marks.values()
)

print("Highest:", highest)
```

---

# 🏆 58. Challenge

Create a list containing:

```text
25
40
15
80
60
35
90
```

Then:

1. Import `reduce()` from `functools`.
2. Calculate the total using `reduce()`.
3. Calculate the product using `reduce()`.
4. Find the highest number using `reduce()`.
5. Find the lowest number using `reduce()`.
6. Calculate the total of only even numbers.
7. Count the number of elements using `reduce()`.
8. Use an initializer while calculating the total.
9. Display all results.
10. Try solving the challenge without copying the solution.

---

# 🧪 59. Mini Project: Sales Analysis System

Create a sales analysis program containing daily sales:

```python
sales = [12500, 18000, 9500, 22000, 16500]
```

Perform the following operations:

* Calculate total sales using `reduce()`.
* Find the highest sale using `reduce()`.
* Find the lowest sale using `reduce()`.
* Count the number of sales using `reduce()`.
* Calculate the average sales.
* Display the final analysis.

Example data:

```python
sales = [12500, 18000, 9500, 22000, 16500]
```

Your program should produce information similar to:

```text
Total Sales: ...
Highest Sale: ...
Lowest Sale: ...
Number of Sales: ...
Average Sale: ...
```

### Your Goal

Build the complete sales analysis program using `reduce()` and related Python functions.

---

# 🎤 60. Interview Questions

* [ ] What is `reduce()` in Python?
* [ ] Which module provides `reduce()`?
* [ ] How do you import `reduce()`?
* [ ] What is the syntax of `reduce()`?
* [ ] What is the purpose of the first argument of `reduce()`?
* [ ] What is the purpose of the iterable argument?
* [ ] What is an initializer?
* [ ] What happens when `reduce()` receives an empty iterable without an initializer?
* [ ] What is an accumulator?
* [ ] How does `reduce()` process elements?
* [ ] Can `reduce()` work with lists?
* [ ] Can `reduce()` work with tuples?
* [ ] Can `reduce()` work with sets?
* [ ] Can `reduce()` work with strings?
* [ ] Can `reduce()` work with dictionary values?
* [ ] What is the difference between `map()` and `reduce()`?
* [ ] What is the difference between `filter()` and `reduce()`?
* [ ] How can `reduce()` be used to calculate a factorial?
* [ ] How can `reduce()` find the maximum value?
* [ ] How can `reduce()` find the minimum value?
* [ ] Can `reduce()` be used with a normal function instead of a lambda?
* [ ] Why might `sum()` be preferred over `reduce()` for simple addition?
* [ ] What happens if the reduction function returns an incorrect value?
* [ ] Can `reduce()` be combined with `filter()`?
* [ ] Can `reduce()` be combined with `map()`?
* [ ] When should you avoid using `reduce()`?

---

# 📝 61. Assignment

Complete the following programs.

### Task 1

Create a list of five numbers.

Use `reduce()` to calculate their sum.

---

### Task 2

Create a list of numbers.

Use `reduce()` to calculate their product.

---

### Task 3

Create a list of numbers.

Use `reduce()` to find the highest number.

---

### Task 4

Create a list of numbers.

Use `reduce()` to find the lowest number.

---

### Task 5

Create a list of words.

Use `reduce()` to combine all words into one sentence.

---

### Task 6

Create a list of numbers.

Use `reduce()` to calculate the factorial of a number.

---

### Task 7

Create an empty list.

Use `reduce()` with an initializer to calculate its total safely.

---

### Task 8

Create a list containing positive and negative numbers.

Use `filter()` and `reduce()` to calculate the sum of positive numbers.

---

### Task 9

Create a dictionary containing five products and their prices.

Use `reduce()` with `values()` to calculate the total price.

---

### Task 10

Create a dictionary containing subjects and marks.

Use `reduce()` to find the highest mark.

---

### Task 11

Create a real-world list of expenses.

Use at least three different `reduce()` operations.

---

### Task 12

Create a program that uses `filter()` and `reduce()` together to calculate the product of all even numbers in a list.

---

# 🧠 62. Memory Tricks

Remember:

```text
reduce()
   ↓
Combine
   ↓
Many values
   ↓
One final value
```

---

Remember the accumulator:

```text
Accumulator
     ↓
Previous result
     +
Current value
     ↓
New result
```

---

Remember the functional tools:

```text
map()
 ↓
Transform


filter()
 ↓
Select


reduce()
 ↓
Combine
```

---

Remember the basic syntax:

```text
reduce(function, iterable)
```

With initializer:

```text
reduce(function, iterable, initializer)
```

---

Remember:

```text
reduce()
   ↓
Repeated operation
   ↓
Accumulation
   ↓
Single result
```

---

# 📌 63. Important Rules to Remember

```text
1. reduce() is available in the functools module.

2. You normally import it using:
   from functools import reduce

3. reduce() repeatedly applies a function to elements.

4. reduce() produces one final accumulated result.

5. The first argument is the function used for reduction.

6. The second argument is the iterable.

7. An initializer can provide the starting accumulator value.

8. Without an initializer, the first two elements begin the reduction.

9. An empty iterable requires an initializer.

10. reduce() can work with lists, tuples, sets, strings, and other iterables.

11. reduce() can be used with lambda functions.

12. reduce() can also use normal functions.

13. The accumulator stores the previous result.

14. The current value is processed with the accumulator.

15. reduce() can calculate sums and products.

16. reduce() can find maximum and minimum values.

17. reduce() can combine strings.

18. reduce() can be combined with filter().

19. reduce() can be combined with map().

20. For simple addition, sum() is usually clearer than reduce().
```

---

# 📊 64. `reduce()` Structure

```text
                         reduce()
                            │
                            ↓
                     functools module
                            │
                            ↓
                    reduce(function,
                           iterable,
                           initializer)
                            │
             ┌──────────────┴──────────────┐
             ↓                             ↓
         FUNCTION                       ITERABLE
             │                             │
             ↓                             ↓
       Operation                      List / Tuple
             │                         Set / String
             ↓                             ↓
      Accumulator +                 Elements
      Current Value                     │
             │                          │
             └──────────────┬───────────┘
                            ↓
                     Repeated Process
                            │
                            ↓
                       One Result
```

---

# 📚 65. Complete `reduce()` Cheat Sheet

### Import `reduce()`

```python
from functools import reduce
```

### Basic Reduction

```python
result = reduce(lambda a, b: a + b, numbers)
```

### Multiplication

```python
result = reduce(lambda a, b: a * b, numbers)
```

### Maximum

```python
result = reduce(lambda a, b: a if a > b else b, numbers)
```

### Minimum

```python
result = reduce(lambda a, b: a if a < b else b, numbers)
```

### Using an Initializer

```python
result = reduce(lambda a, b: a + b, numbers, 0)
```

### Combine Strings

```python
result = reduce(lambda a, b: a + " " + b, words)
```

### Reduce Dictionary Values

```python
result = reduce(lambda a, b: a + b, dictionary.values())
```

### Combine with `filter()`

```python
result = reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 0, numbers),
    0
)
```

### Combine with `map()`

```python
result = reduce(
    lambda a, b: a + b,
    map(lambda x: x ** 2, numbers)
)
```

---

# 🏆 66. `reduce()` Mastery

```text
                         REDUCE()
                            │
                            ↓
                 Repeatedly Combine
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
           SUM           PRODUCT       COMPARISON
             │              │              │
             ↓              ↓              ↓
        Add values     Multiply       Max / Min
                            │
                            ↓
                     String Combining
                            │
                            ↓
                     Custom Reduction
                            │
                            ↓
                      ONE FINAL VALUE
```

---

# 📚 67. Summary

In this lesson, you learned:

* What `reduce()` is.
* Why `reduce()` is used.
* How to import `reduce()` from `functools`.
* The syntax of `reduce()`.
* The meaning of the function argument.
* The meaning of the iterable argument.
* The purpose of the initializer.
* How the accumulator works.
* How `reduce()` processes elements step by step.
* How to use `reduce()` with lists.
* How to use `reduce()` with tuples.
* How to use `reduce()` with sets.
* How to use `reduce()` with strings.
* How to calculate sums using `reduce()`.
* How to calculate products using `reduce()`.
* How to find maximum values.
* How to find minimum values.
* How to combine strings.
* How to use conditions inside reduction functions.
* How to use an initializer.
* How to handle empty iterables.
* How to combine `reduce()` with `filter()`.
* How to combine `reduce()` with `map()`.
* How to use `reduce()` with dictionary values.
* How to use `reduce()` in real-world applications.
* The difference between `map()`, `filter()`, and `reduce()`.
* Common mistakes when using `reduce()`.
* When `reduce()` is appropriate.
* Why simpler functions such as `sum()` can sometimes be preferred.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `reduce()` is.
* [ ] I know where `reduce()` comes from.
* [ ] I can import `reduce()` correctly.
* [ ] I understand the syntax of `reduce()`.
* [ ] I understand the accumulator.
* [ ] I understand the current value.
* [ ] I understand how `reduce()` processes elements.
* [ ] I can use `reduce()` with lists.
* [ ] I can use `reduce()` with tuples.
* [ ] I can use `reduce()` with sets.
* [ ] I can use `reduce()` with strings.
* [ ] I can calculate sums using `reduce()`.
* [ ] I can calculate products using `reduce()`.
* [ ] I can find maximum values using `reduce()`.
* [ ] I can find minimum values using `reduce()`.
* [ ] I understand the initializer.
* [ ] I can use `reduce()` with an initializer.
* [ ] I understand empty iterable behavior.
* [ ] I can combine `reduce()` with `filter()`.
* [ ] I can combine `reduce()` with `map()`.
* [ ] I can use `reduce()` with dictionary values.
* [ ] I understand the difference between `map()`, `filter()`, and `reduce()`.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use `reduce()` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Advanced Function Concepts**

In the next topic, you will learn:

* Advanced function concepts.
* Function composition.
* Higher-order functions.
* Functions as first-class objects.
* Passing functions as arguments.
* Returning functions from functions.
* Nested functions.
* Closures.
* Practical functional programming patterns.
* Combining `map()`, `filter()`, and `reduce()`.
* Advanced real-world examples.
* Common mistakes.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Reduce many values into one meaningful result."** 🐍📚
