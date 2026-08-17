# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 14: Recursion

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what recursion means in Python.
* [ ] Understand how recursive functions work.
* [ ] Understand the difference between recursion and iteration.
* [ ] Identify the base case of a recursive function.
* [ ] Identify the recursive case of a recursive function.
* [ ] Understand how recursive function calls are stored in memory.
* [ ] Trace recursive function execution step by step.
* [ ] Use recursion to solve mathematical problems.
* [ ] Calculate factorial using recursion.
* [ ] Generate Fibonacci numbers using recursion.
* [ ] Calculate the sum of numbers using recursion.
* [ ] Reverse strings using recursion.
* [ ] Check palindromes using recursion.
* [ ] Find powers using recursion.
* [ ] Find the greatest common divisor using recursion.
* [ ] Understand recursive data structures.
* [ ] Understand recursion with lists.
* [ ] Understand nested recursion.
* [ ] Understand recursion depth.
* [ ] Understand `RecursionError`.
* [ ] Compare recursion with loops.
* [ ] Avoid common recursion mistakes.
* [ ] Use recursion in real-world applications.
* [ ] Solve recursion-based programming problems.

---

# 📖 1. What is Recursion?

**Recursion** is a programming technique in which a function calls itself to solve a problem.

In simple words:

> A function calling itself is called recursion.

Example:

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)
```

Output:

```text
5
4
3
2
1
```

Here:

```text
countdown(5)
      ↓
countdown(4)
      ↓
countdown(3)
      ↓
countdown(2)
      ↓
countdown(1)
      ↓
countdown(0)
```

The function keeps calling itself with a smaller value.

---

# 🧠 2. Basic Structure of Recursion

A recursive function normally contains two important parts:

1. **Base Case**
2. **Recursive Case**

General structure:

```python
def function(parameter):

    if base_condition:
        return result

    return function(smaller_problem)
```

The structure can be visualized as:

```text
             Recursive Function
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      Base Case          Recursive Case
          │                   │
          ↓                   ↓
       Stop           Call function again
```

---

# 🛑 3. What is a Base Case?

The **base case** is the condition that stops recursion.

Without a base case, the function keeps calling itself forever.

Example:

```python
def countdown(n):

    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

Here:

```python
if n == 0:
    return
```

is the base case.

When `n` becomes `0`, the function stops calling itself.

---

# 🔁 4. What is a Recursive Case?

The **recursive case** is the part where the function calls itself.

Example:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

This line is the recursive case:

```python
countdown(n - 1)
```

The function calls itself using a smaller value.

---

# ⚖️ 5. Base Case vs Recursive Case

| Part           | Purpose                  |
| -------------- | ------------------------ |
| Base Case      | Stops recursion          |
| Recursive Case | Calls the function again |

Example:

```python
def count(n):

    if n == 0:       # Base case
        return

    print(n)

    count(n - 1)     # Recursive case
```

Remember:

```text
Base Case
   ↓
STOP

Recursive Case
   ↓
CONTINUE
```

---

# 🔍 6. Simple Recursive Example

Consider:

```python
def count_down(n):

    if n == 0:
        return

    print(n)
    count_down(n - 1)


count_down(3)
```

Execution:

```text
count_down(3)
     ↓
print(3)
     ↓
count_down(2)
     ↓
print(2)
     ↓
count_down(1)
     ↓
print(1)
     ↓
count_down(0)
     ↓
STOP
```

Output:

```text
3
2
1
```

---

# 🧠 7. Understanding Recursive Calls

Consider:

```python
def display(n):

    if n == 0:
        return

    print(n)
    display(n - 1)


display(4)
```

The calls are:

```text
display(4)
display(3)
display(2)
display(1)
display(0)
```

When `display(0)` reaches the base case, the recursive calls start returning.

This process is called **unwinding**.

---

# 🔄 8. Recursion Has Two Phases

Recursive functions usually have two phases:

### Phase 1: Calling

The function keeps calling itself.

```text
4 → 3 → 2 → 1 → 0
```

### Phase 2: Returning

The functions return back.

```text
0 → 1 → 2 → 3 → 4
```

Structure:

```text
CALLING PHASE

4
↓
3
↓
2
↓
1
↓
0


RETURNING PHASE

0
↑
1
↑
2
↑
3
↑
4
```

---

# 📚 9. Recursion and the Call Stack

Python uses a **call stack** to keep track of active function calls.

Example:

```python
def count(n):

    if n == 0:
        return

    print(n)
    count(n - 1)


count(3)
```

Conceptually:

```text
Stack

count(1)
count(2)
count(3)
count(4)
```

Each recursive call creates another function call on the stack.

When the base case is reached, calls are removed from the stack one by one.

---

# 🧠 10. Understanding Stack Unwinding

Consider:

```python
def test(n):

    if n == 0:
        return

    print("Calling:", n)
    test(n - 1)
    print("Returning:", n)


test(3)
```

Output:

```text
Calling: 3
Calling: 2
Calling: 1
Returning: 1
Returning: 2
Returning: 3
```

Notice that:

```text
Calling
```

happens while going deeper.

But:

```text
Returning
```

happens in reverse order.

---

# 🔢 11. Recursive Function to Print Numbers

Example:

```python
def print_numbers(n):

    if n == 0:
        return

    print_numbers(n - 1)
    print(n)


print_numbers(5)
```

Output:

```text
1
2
3
4
5
```

Here the `print()` statement executes while recursion is returning.

---

# 🔁 12. Printing Numbers in Reverse Using Recursion

```python
def print_reverse(n):

    if n == 0:
        return

    print(n)
    print_reverse(n - 1)


print_reverse(5)
```

Output:

```text
5
4
3
2
1
```

The position of the recursive call matters.

---

# ⚖️ 13. Recursion Before vs After the Recursive Call

Consider:

```python
print(n)
recursive_call()
```

The value is printed while going **down**.

But:

```python
recursive_call()
print(n)
```

The value is printed while coming **back up**.

Example:

```python
def example(n):

    if n == 0:
        return

    print("Before:", n)

    example(n - 1)

    print("After:", n)


example(3)
```

Output:

```text
Before: 3
Before: 2
Before: 1
After: 1
After: 2
After: 3
```

---

# 🧮 14. Factorial Using Recursion

The factorial of a number is:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Therefore:

```text
5! = 120
```

Recursive definition:

```text
n! = n × (n - 1)!
```

Base case:

```text
0! = 1
```

Python:

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

Output:

```text
120
```

---

# 🔍 15. Factorial Recursion Trace

Consider:

```python
factorial(4)
```

Execution:

```text
factorial(4)
= 4 × factorial(3)

= 4 × 3 × factorial(2)

= 4 × 3 × 2 × factorial(1)

= 4 × 3 × 2 × 1 × factorial(0)

= 4 × 3 × 2 × 1 × 1

= 24
```

Therefore:

```text
4! = 24
```

---

# ➕ 16. Sum of Numbers Using Recursion

We can calculate:

```text
1 + 2 + 3 + 4 + 5
```

using recursion.

```python
def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)


print(total(5))
```

Output:

```text
15
```

---

# 🔢 17. Sum Recursion Trace

For:

```python
total(4)
```

The calculation becomes:

```text
total(4)
= 4 + total(3)

= 4 + 3 + total(2)

= 4 + 3 + 2 + total(1)

= 4 + 3 + 2 + 1 + total(0)

= 10
```

---

# 🔢 18. Counting Digits Using Recursion

Recursion can be used to count the number of digits in an integer.

Example:

```python
def count_digits(n):

    if n == 0:
        return 0

    return 1 + count_digits(n // 10)


print(count_digits(12345))
```

Output:

```text
5
```

The operation:

```python
n // 10
```

removes the last digit.

Example:

```text
12345
 ↓
1234
 ↓
123
 ↓
12
 ↓
1
 ↓
0
```

---

# 🔢 19. Sum of Digits Using Recursion

Example:

```python
def digit_sum(n):

    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)


print(digit_sum(12345))
```

Output:

```text
15
```

Calculation:

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

# 🔄 20. Reverse a String Using Recursion

Example:

```python
def reverse_text(text):

    if text == "":
        return ""

    return reverse_text(text[1:]) + text[0]


print(reverse_text("Python"))
```

Output:

```text
nohtyP
```

The function repeatedly removes the first character and adds it back during the return phase.

---

# 🔍 21. Understanding String Recursion

For:

```text
Python
```

The recursive process is conceptually:

```text
Python
 ython
  thon
   hon
    on
     n
      ""
```

Then the characters are added back:

```text
n
on
hon
thon
ython
Python
```

The final result is:

```text
nohtyP
```

---

# 🪞 22. Checking a Palindrome Using Recursion

A palindrome reads the same forward and backward.

Examples:

```text
madam
level
radar
```

Recursive solution:

```python
def is_palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("madam"))
```

Output:

```text
True
```

---

# 🧠 23. Palindrome Recursion Logic

For:

```text
madam
```

Compare:

```text
m == m
```

Then:

```text
ada
```

Compare:

```text
a == a
```

Then:

```text
d
```

Only one character remains.

Therefore:

```text
True
```

---

# ⚡ 24. Power Using Recursion

Mathematically:

```text
2³ = 2 × 2 × 2 = 8
```

Recursive definition:

```text
aⁿ = a × aⁿ⁻¹
```

Python:

```python
def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(2, 4))
```

Output:

```text
16
```

---

# 🔢 25. Fibonacci Sequence Using Recursion

The Fibonacci sequence is:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21...
```

Each number is calculated using the previous two numbers.

Recursive definition:

```text
F(n) = F(n - 1) + F(n - 2)
```

Base cases:

```text
F(0) = 0
F(1) = 1
```

Python:

```python
def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
```

Output:

```text
13
```

---

# 🌳 26. Understanding Fibonacci Recursion

For:

```python
fibonacci(4)
```

The calls branch:

```text
                 F(4)
               /      \
            F(3)      F(2)
           /   \      /   \
        F(2) F(1)  F(1) F(0)
        / \
      F(1) F(0)
```

This creates many repeated calculations.

Therefore, the simple recursive Fibonacci implementation is useful for learning recursion but is inefficient for large values.

---

# ⚠️ 27. Recursion and `RecursionError`

If recursion never reaches a base case, Python eventually raises:

```text
RecursionError
```

Example:

```python
def test(n):

    print(n)
    test(n + 1)


test(1)
```

There is no stopping condition.

Eventually Python raises an error similar to:

```text
RecursionError: maximum recursion depth exceeded
```

---

# 🛑 28. Why the Base Case is Important

Incorrect:

```python
def count(n):

    print(n)
    count(n - 1)
```

There is no base case.

Correct:

```python
def count(n):

    if n == 0:
        return

    print(n)
    count(n - 1)
```

Remember:

```text
No Base Case
      ↓
Infinite Recursive Calls
      ↓
RecursionError
```

---

# 📊 29. Recursion Depth

Python limits how deeply function calls can normally recurse.

The exact recursion limit depends on the Python environment, and it can be inspected using:

```python
import sys

print(sys.getrecursionlimit())
```

You should not normally solve problems by simply increasing the recursion limit.

Instead, design the recursive algorithm so that it terminates safely.

---

# ⚖️ 30. Recursion vs Iteration

| Recursion                             | Iteration                             |
| ------------------------------------- | ------------------------------------- |
| Function calls itself                 | Loop repeats statements               |
| Uses call stack                       | Uses loop control                     |
| Can be elegant for recursive problems | Often more memory-efficient           |
| Can be easier for tree structures     | Usually easier for simple repetition  |
| May cause `RecursionError`            | Usually avoids recursion-depth limits |
| Can have function-call overhead       | Usually has less overhead             |

Example using recursion:

```python
def count(n):

    if n == 0:
        return

    print(n)
    count(n - 1)
```

Using a loop:

```python
for n in range(5, 0, -1):
    print(n)
```

Both produce:

```text
5
4
3
2
1
```

---

# 🧠 31. When Should You Use Recursion?

Recursion is especially useful when a problem naturally contains smaller versions of itself.

Common examples include:

* Tree traversal
* Directory traversal
* Graph algorithms
* Divide-and-conquer algorithms
* Backtracking
* Searching nested structures
* Mathematical recurrence problems

For simple counting or repetition, a loop is often preferable.

---

# 📦 32. Recursion with Lists

Recursion can process list elements one by one.

Example:

```python
def display_items(items, index=0):

    if index == len(items):
        return

    print(items[index])

    display_items(items, index + 1)


numbers = [10, 20, 30, 40]

display_items(numbers)
```

Output:

```text
10
20
30
40
```

---

# ➕ 33. Sum of a List Using Recursion

```python
def list_sum(numbers):

    if len(numbers) == 0:
        return 0

    return numbers[0] + list_sum(numbers[1:])


numbers = [10, 20, 30, 40]

print(list_sum(numbers))
```

Output:

```text
100
```

---

# 🔍 34. Find Maximum Value Using Recursion

Example:

```python
def find_max(numbers):

    if len(numbers) == 1:
        return numbers[0]

    maximum = find_max(numbers[1:])

    if numbers[0] > maximum:
        return numbers[0]

    return maximum


numbers = [15, 42, 8, 31, 27]

print(find_max(numbers))
```

Output:

```text
42
```

---

# 🔎 35. Linear Search Using Recursion

We can recursively search for a value in a list.

```python
def search(numbers, target, index=0):

    if index == len(numbers):
        return False

    if numbers[index] == target:
        return True

    return search(numbers, target, index + 1)


numbers = [10, 25, 40, 55, 70]

print(search(numbers, 40))
```

Output:

```text
True
```

---

# 🔢 36. Count Occurrences Using Recursion

Example:

```python
def count_value(numbers, target, index=0):

    if index == len(numbers):
        return 0

    if numbers[index] == target:
        return 1 + count_value(numbers, target, index + 1)

    return count_value(numbers, target, index + 1)


numbers = [10, 20, 10, 30, 10]

print(count_value(numbers, 10))
```

Output:

```text
3
```

---

# 🔢 37. Greatest Common Divisor Using Recursion

The Euclidean algorithm can calculate the greatest common divisor.

```python
def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(48, 18))
```

Output:

```text
6
```

The recursive relationship is:

```text
gcd(a, b)
=
gcd(b, a % b)
```

---

# 🔍 38. Understanding the GCD Recursion

For:

```text
gcd(48, 18)
```

The calls are:

```text
gcd(48, 18)
     ↓
gcd(18, 12)
     ↓
gcd(12, 6)
     ↓
gcd(6, 0)
```

Base case:

```python
if b == 0:
    return a
```

Therefore:

```text
GCD = 6
```

---

# 🧩 39. Recursive Dictionary Traversal

Recursion is useful for processing nested dictionaries.

Example data:

```python
company = {
    "name": "TechCorp",
    "departments": {
        "Development": {
            "employees": 25
        },
        "Testing": {
            "employees": 10
        }
    }
}
```

A recursive function can inspect nested structures.

```python
def display_data(data):

    for key, value in data.items():

        if isinstance(value, dict):
            display_data(value)
        else:
            print(key, ":", value)


display_data(company)
```

Output:

```text
name : TechCorp
employees : 25
employees : 10
```

---

# 📁 40. Real-World Example: Folder Traversal

Folders can contain:

```text
Folder
 ├── File
 ├── File
 └── Subfolder
      ├── File
      └── Subfolder
```

Because folders can contain other folders, recursion is a natural way to traverse them.

Conceptually:

```text
process folder
     ↓
process files
     ↓
if another folder exists
     ↓
call function for that folder
```

This is one reason recursion is commonly used in file-system traversal.

---

# 🌳 41. Recursion and Trees

A tree naturally contains smaller trees.

Example:

```text
             A
           /   \
          B     C
        /  \     \
       D    E     F
```

Each node can have child nodes.

A recursive tree traversal can follow:

```text
A
↓
B
↓
D
↓
E
↓
C
↓
F
```

Recursion is therefore extremely common in tree algorithms.

---

# 🔄 42. Nested Recursion

Nested recursion occurs when a recursive function's calls become more complex than simply reducing the input by one.

Example:

```python
def example(n):

    if n > 0:
        print(n)
        example(n - 1)


example(3)
```

This is ordinary recursion.

More complex recursive patterns can involve multiple recursive calls or recursive calls inside expressions.

Such techniques are usually introduced after understanding basic recursion.

---

# 🌿 43. Multiple Recursive Calls

A function can call itself more than once.

Example:

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

Here the function makes two recursive calls:

```python
fibonacci(n - 1)
```

and

```python
fibonacci(n - 2)
```

This creates a branching recursion structure.

---

# 🧠 44. Recursion with Conditions

Recursive functions often use conditions to decide whether to continue.

Example:

```python
def countdown(n):

    if n <= 0:
        return

    print(n)

    if n > 1:
        countdown(n - 1)


countdown(5)
```

Output:

```text
5
4
3
2
1
```

Conditions help control recursive execution.

---

# 🔢 45. Recursive Multiplication

Multiplication can be represented as repeated addition.

For example:

```text
4 × 3
=
4 + 4 + 4
```

Recursive implementation:

```python
def multiply(a, b):

    if b == 0:
        return 0

    return a + multiply(a, b - 1)


print(multiply(4, 3))
```

Output:

```text
12
```

---

# 🔢 46. Recursive Division Concept

Repeated subtraction can be used to understand division recursively.

Example concept:

```text
10 ÷ 2

10 - 2 = 8
8 - 2 = 6
6 - 2 = 4
4 - 2 = 2
2 - 2 = 0
```

The number of successful subtractions is:

```text
5
```

A recursive implementation can model this process.

---

# 🧠 47. Direct vs Indirect Recursion

### Direct Recursion

A function directly calls itself.

```python
def function_a():

    function_a()
```

This is:

```text
A → A
```

### Indirect Recursion

One function calls another function, which eventually calls the first function.

```python
def function_a():
    function_b()


def function_b():
    function_a()
```

This is:

```text
A → B → A → B
```

Both are forms of recursion.

---

# ⚠️ 48. Common Mistake: Forgetting the Base Case

Incorrect:

```python
def test(n):

    print(n)
    test(n - 1)
```

There is no condition to stop recursion.

Correct:

```python
def test(n):

    if n == 0:
        return

    print(n)
    test(n - 1)
```

Always ask:

> "What condition will stop my recursive calls?"

---

# ⚠️ 49. Common Mistake: Base Case Never Reached

Consider:

```python
def test(n):

    if n == 0:
        return

    test(n + 1)
```

The function starts with:

```text
1
2
3
4
5
...
```

The value moves away from `0`.

Therefore the base case is never reached.

Correct:

```python
test(n - 1)
```

when starting with a positive value.

---

# ⚠️ 50. Common Mistake: Wrong Return Statement

Incorrect:

```python
def factorial(n):

    if n == 0:
        return 1

    factorial(n - 1)
```

The recursive result is not returned.

Correct:

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)
```

The `return` allows the result to travel back through the recursive calls.

---

# ⚠️ 51. Common Mistake: Confusing Printing with Returning

Consider:

```python
def total(n):

    if n == 0:
        print(0)
        return

    print(n + total(n - 1))
```

Printing and returning are different operations.

For calculations, recursive functions commonly need:

```python
return
```

so that the result can be used by the previous call.

Example:

```python
def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)
```

---

# ⚠️ 52. Common Mistake: Using Recursion for Everything

Recursion is powerful, but it should not automatically replace loops.

For example:

```python
for number in range(1, 101):
    print(number)
```

is usually simpler than creating a recursive function for the same task.

Use recursion when the problem naturally benefits from recursive structure.

---

# 📊 53. Recursion Complexity

Recursive algorithms can have different time and space complexities.

For example, factorial recursion:

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)
```

has approximately:

```text
Time Complexity: O(n)
Space Complexity: O(n)
```

because there can be `n` active function calls on the call stack.

---

# ⚡ 54. Recursive Fibonacci and Performance

The simple recursive Fibonacci implementation:

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

performs many repeated calculations.

Its time complexity is exponential, commonly described as approximately:

```text
O(2ⁿ)
```

This makes it inefficient for large values.

A loop or memoization can be used to improve performance.

---

# 🧠 55. Recursion with Memoization

**Memoization** means storing previously calculated results so they do not have to be calculated again.

Example:

```python
def fibonacci(n, memo={}):

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


print(fibonacci(10))
```

Output:

```text
55
```

Memoization can dramatically improve recursive algorithms with repeated subproblems.

---

# 🔍 56. Recursion vs Memoization

Without memoization:

```text
Repeated calculations
        ↓
More function calls
        ↓
Slower execution
```

With memoization:

```text
Calculate once
      ↓
Store result
      ↓
Reuse result
      ↓
Faster execution
```

---

# 📚 57. Complete Recursion Cheat Sheet

### Basic Recursive Structure

```python
def function(n):

    if base_condition:
        return result

    return function(smaller_value)
```

### Factorial

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)
```

### Sum

```python
def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)
```

### Power

```python
def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)
```

### Fibonacci

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

### GCD

```python
def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)
```

### Reverse String

```python
def reverse_text(text):

    if text == "":
        return ""

    return reverse_text(text[1:]) + text[0]
```

---

# 🏆 58. Recursion Mastery

```text
                         RECURSION
                             │
                             ↓
                    FUNCTION CALLS ITSELF
                             │
                 ┌───────────┴───────────┐
                 ↓                       ↓
             BASE CASE             RECURSIVE CASE
                 │                       │
                 ↓                       ↓
              STOP                  CALL ITSELF
                                         │
                                         ↓
                                  SMALLER PROBLEM
                                         │
                                         ↓
                                  REACH BASE CASE
                                         │
                                         ↓
                                      RETURN
```

Remember:

```text
Recursion
   ↓
Function calls itself
   ↓
Base case
   ↓
Stops recursion
   ↓
Recursive case
   ↓
Solves smaller problem
```

---

# 💻 59. Practice Programs

## 🟢 Easy

### Program 1: Print Numbers Using Recursion

```python
def count(n):

    if n == 0:
        return

    print(n)
    count(n - 1)


count(5)
```

---

### Program 2: Print Numbers from 1 to N

```python
def display(n):

    if n == 0:
        return

    display(n - 1)
    print(n)


display(5)
```

---

### Program 3: Calculate Factorial

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

---

### Program 4: Calculate Sum of Numbers

```python
def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)


print(total(10))
```

---

## 🟡 Medium

### Program 5: Calculate Power

```python
def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print(power(3, 4))
```

---

### Program 6: Reverse a String

```python
def reverse_text(text):

    if text == "":
        return ""

    return reverse_text(text[1:]) + text[0]


print(reverse_text("Python"))
```

---

### Program 7: Calculate Sum of Digits

```python
def digit_sum(n):

    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)


print(digit_sum(9876))
```

---

### Program 8: Count Digits

```python
def count_digits(n):

    if n == 0:
        return 0

    return 1 + count_digits(n // 10)


print(count_digits(123456))
```

---

## 🔴 Advanced

### Program 9: Fibonacci Number

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))
```

---

### Program 10: Check Palindrome

```python
def is_palindrome(text):

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("level"))
```

---

### Program 11: Find GCD

```python
def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


print(gcd(48, 18))
```

---

### Program 12: Search an Element Recursively

```python
def search(numbers, target, index=0):

    if index == len(numbers):
        return False

    if numbers[index] == target:
        return True

    return search(numbers, target, index + 1)


numbers = [15, 25, 35, 45, 55]

print(search(numbers, 35))
```

---

# 🏆 60. Challenge

Create a recursive program that processes a list of numbers.

Given:

```text
10
20
30
40
50
```

Perform the following operations:

1. Display all numbers using recursion.
2. Calculate the total using recursion.
3. Find the largest number using recursion.
4. Search for a specified number.
5. Count how many times a specified number occurs.
6. Reverse the list using recursion.
7. Display the final results.

Example data:

```python
numbers = [10, 20, 30, 40, 50]
```

Try solving the challenge without copying the solution.

---

# 🧪 61. Mini Project: Recursive File/Folder Structure Processor

Create a nested data structure representing folders and files.

Example:

```python
folder = {
    "Documents": {
        "notes.txt": 1,
        "project.py": 1
    },
    "Pictures": {
        "photo.jpg": 1,
        "wallpaper.png": 1
    }
}
```

Create a recursive function that:

* Displays all files.
* Displays nested folders.
* Counts the total number of files.
* Searches for a particular file.
* Processes nested folders automatically.
* Uses recursion whenever another dictionary is encountered.

Conceptually:

```text
Main Folder
    ↓
Documents
    ↓
Files
    ↓
Pictures
    ↓
Files
```

### Your Goal

Build a recursive folder-processing program that can handle an arbitrary number of nested folders.

---

# 🎤 62. Interview Questions

* [ ] What is recursion in Python?
* [ ] What is a recursive function?
* [ ] What is a base case?
* [ ] What is a recursive case?
* [ ] Why is a base case necessary?
* [ ] What happens if a recursive function has no base case?
* [ ] What is `RecursionError`?
* [ ] How does Python manage recursive function calls?
* [ ] What is the call stack?
* [ ] What is stack unwinding?
* [ ] What is the difference between recursion and iteration?
* [ ] When should recursion be preferred over loops?
* [ ] How can you calculate factorial using recursion?
* [ ] How can you calculate Fibonacci numbers using recursion?
* [ ] How can you reverse a string using recursion?
* [ ] How can you check a palindrome using recursion?
* [ ] How can you calculate GCD using recursion?
* [ ] What is direct recursion?
* [ ] What is indirect recursion?
* [ ] What is multiple recursion?
* [ ] What is recursion depth?
* [ ] Why can recursion consume more memory than iteration?
* [ ] What is memoization?
* [ ] Why is simple recursive Fibonacci inefficient?
* [ ] How can memoization improve recursive algorithms?
* [ ] Can every recursive problem be solved using iteration?
* [ ] Can every iterative problem be written recursively?
* [ ] What is the importance of the `return` statement in recursion?

---

# 📝 63. Assignment

### Task 1

Create a recursive function that prints numbers from `1` to `10`.

---

### Task 2

Create a recursive function that prints numbers from `10` to `1`.

---

### Task 3

Create a recursive function to calculate the factorial of a number.

---

### Task 4

Create a recursive function to calculate the sum of numbers from `1` to `n`.

---

### Task 5

Create a recursive function to calculate the power of a number.

---

### Task 6

Create a recursive function to reverse a string.

---

### Task 7

Create a recursive function to check whether a string is a palindrome.

---

### Task 8

Create a recursive function to calculate the sum of digits of a number.

---

### Task 9

Create a recursive function to count the digits of a number.

---

### Task 10

Create a recursive function to find the greatest common divisor of two numbers.

---

### Task 11

Create a recursive function to search for an element inside a list.

---

### Task 12

Create a recursive function that finds the largest number in a list.

---

### Task 13

Create a recursive function that counts how many times a particular value appears in a list.

---

### Task 14

Create a recursive Fibonacci function.

Generate:

```text
0 1 1 2 3 5 8 13 21 34
```

---

### Task 15

Create a real-world recursive program that processes nested folders or nested dictionaries.

---

# 🧠 64. Memory Tricks

Remember the basic recursion pattern:

```text
FUNCTION
   ↓
BASE CASE
   ↓
STOP

Otherwise
   ↓
RECURSIVE CALL
   ↓
SMALLER PROBLEM
```

---

Remember factorial:

```text
factorial(n)
      ↓
n × factorial(n-1)
      ↓
factorial(0)
      ↓
1
```

---

Remember Fibonacci:

```text
F(n)
 ↓
F(n-1) + F(n-2)
```

---

Remember recursion:

```text
Base Case
   ↓
STOP

Recursive Case
   ↓
CALL AGAIN
```

---

# 📌 65. Important Rules to Remember

```text
1. Recursion occurs when a function calls itself.

2. Every useful recursive solution needs a stopping condition.

3. The stopping condition is called the base case.

4. The part that calls the function again is the recursive case.

5. Each recursive call should move toward the base case.

6. Recursive calls are stored on the call stack.

7. Recursive functions can unwind after reaching the base case.

8. The return statement is important when recursive results must be combined.

9. Recursion can make naturally recursive problems easier to understand.

10. Recursion can consume more memory because of the call stack.

11. Excessive recursion can cause RecursionError.

12. A loop is often better for simple repetitive tasks.

13. Recursion is commonly used with trees and nested structures.

14. Fibonacci recursion can perform repeated calculations.

15. Memoization can improve recursive algorithms with overlapping subproblems.

16. Direct recursion means a function directly calls itself.

17. Indirect recursion means functions call each other recursively.

18. Multiple recursive calls can create branching recursion.

19. Always verify that the recursive input moves toward the base case.

20. Understand the calling phase and returning phase when tracing recursion.
```

---

# 📊 66. Recursion Structure

```text
                         RECURSION
                             │
                             ↓
                     RECURSIVE FUNCTION
                             │
                ┌────────────┴────────────┐
                ↓                         ↓
            BASE CASE              RECURSIVE CASE
                │                         │
                ↓                         ↓
             STOP                 CALL FUNCTION AGAIN
                                          │
                                          ↓
                                  SMALLER PROBLEM
                                          │
                                          ↓
                                   BASE CASE REACHED
                                          │
                                          ↓
                                       RETURN
                                          │
                                          ↓
                                     UNWIND STACK
```

---

# 📚 67. Complete Recursion Cheat Sheet

### Recursive Function

```python
def function(n):

    if condition:
        return

    return function(n - 1)
```

### Factorial

```python
factorial(n) = n * factorial(n - 1)
```

### Sum

```python
total(n) = n + total(n - 1)
```

### Power

```python
power(a, n) = a * power(a, n - 1)
```

### Fibonacci

```python
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
```

### GCD

```python
gcd(a, b) = gcd(b, a % b)
```

### Palindrome

```text
First character == Last character
        ↓
Check remaining middle
```

### Recursion Error

```text
No Base Case
      ↓
Infinite Calls
      ↓
RecursionError
```

---

# 🏆 68. Recursion Mastery

```text
                         RECURSION
                             │
                             ↓
                  FUNCTION CALLS ITSELF
                             │
          ┌──────────────────┴──────────────────┐
          ↓                                     ↓
      BASE CASE                           RECURSIVE CASE
          │                                     │
          ↓                                     ↓
       STOP                              CALL ITSELF
                                                │
                                                ↓
                                         SMALLER INPUT
                                                │
                                                ↓
                                         BASE CASE
                                                │
                                                ↓
                                             RETURN
                                                │
                                                ↓
                                         STACK UNWINDS
                                                │
                                                ↓
                                             RESULT
```

---

# 📚 69. Summary

In this lesson, you learned:

* What recursion is.
* What a recursive function is.
* How a function can call itself.
* What a base case is.
* What a recursive case is.
* Why the base case is necessary.
* How recursive calls work.
* How the call stack stores recursive calls.
* How stack unwinding works.
* How to trace recursive execution.
* How to print numbers using recursion.
* How to calculate factorial using recursion.
* How to calculate the sum of numbers using recursion.
* How to count digits using recursion.
* How to calculate the sum of digits using recursion.
* How to reverse a string using recursion.
* How to check a palindrome using recursion.
* How to calculate powers using recursion.
* How to generate Fibonacci numbers using recursion.
* How to calculate GCD using recursion.
* How to process lists recursively.
* How to search lists recursively.
* How to find maximum values recursively.
* How recursion can work with nested dictionaries.
* How recursion can be used for folder traversal.
* How recursion is used with trees.
* What direct recursion is.
* What indirect recursion is.
* What multiple recursive calls are.
* What recursion depth means.
* What `RecursionError` means.
* The difference between recursion and iteration.
* How memoization can improve recursive algorithms.
* Common mistakes when writing recursive functions.
* Real-world applications of recursion.
* How to solve recursion-based programming problems.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what recursion means.
* [ ] I understand recursive functions.
* [ ] I can identify the base case.
* [ ] I can identify the recursive case.
* [ ] I understand why a base case is required.
* [ ] I can trace recursive function calls.
* [ ] I understand the call stack.
* [ ] I understand stack unwinding.
* [ ] I can write a basic recursive function.
* [ ] I can print numbers using recursion.
* [ ] I can calculate factorial recursively.
* [ ] I can calculate a sum recursively.
* [ ] I can calculate powers recursively.
* [ ] I can generate Fibonacci numbers recursively.
* [ ] I can reverse a string recursively.
* [ ] I can check a palindrome recursively.
* [ ] I can calculate GCD recursively.
* [ ] I can process a list recursively.
* [ ] I can search a list recursively.
* [ ] I can find a maximum value recursively.
* [ ] I understand recursion with nested structures.
* [ ] I understand direct recursion.
* [ ] I understand indirect recursion.
* [ ] I understand multiple recursive calls.
* [ ] I understand recursion depth.
* [ ] I understand `RecursionError`.
* [ ] I understand the difference between recursion and iteration.
* [ ] I understand why simple recursive Fibonacci is inefficient.
* [ ] I understand memoization.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can write recursive functions without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Lambda Functions**

In the next topic, you will learn:

* What lambda functions are.
* Why lambda functions are called anonymous functions.
* Lambda function syntax.
* Creating simple lambda functions.
* Lambda functions with one argument.
* Lambda functions with multiple arguments.
* Lambda functions with `if-else`.
* Lambda functions with `map()`.
* Lambda functions with `filter()`.
* Lambda functions with `reduce()`.
* Lambda functions with `sorted()`.
* Using lambda functions with lists.
* Using lambda functions with dictionaries.
* Using lambda functions with tuples.
* Real-world applications.
* Common mistakes.
* Advanced lambda techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Recursion solves a problem by solving smaller versions of the same problem."** 🐍📚
