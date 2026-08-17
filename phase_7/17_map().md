# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 17: `map()`

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what `map()` is.
* [ ] Understand why `map()` is used.
* [ ] Understand the syntax of `map()`.
* [ ] Understand how `map()` applies a function to every element.
* [ ] Use `map()` with built-in functions.
* [ ] Use `map()` with user-defined functions.
* [ ] Use `map()` with `lambda`.
* [ ] Convert `map` objects into lists.
* [ ] Use `map()` with strings.
* [ ] Use `map()` with numbers.
* [ ] Use `map()` with multiple iterables.
* [ ] Understand how `map()` handles multiple iterables.
* [ ] Use `map()` with conditions.
* [ ] Use `map()` with `if-else`.
* [ ] Combine `map()` with `lambda`.
* [ ] Combine `map()` with `filter()`.
* [ ] Understand the difference between `map()` and loops.
* [ ] Understand the difference between `map()` and list comprehension.
* [ ] Use `map()` in real-world applications.
* [ ] Avoid common mistakes when using `map()`.

---

# 📖 1. What is `map()`?

`map()` is a built-in Python function used to **apply a function to every item in an iterable**.

An iterable can be:

* List
* Tuple
* Set
* String
* Other iterable objects

The basic idea is:

```text
Iterable
   ↓
map()
   ↓
Apply function to every element
   ↓
New mapped result
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = map(str, numbers)

print(list(result))
```

Output:

```text
['1', '2', '3', '4', '5']
```

Here, `str()` is applied to every number.

---

# 🧠 2. Why Use `map()`?

Suppose you have:

```python
numbers = [1, 2, 3, 4, 5]
```

You want to double every number.

Using a loop:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

Output:

```text
[2, 4, 6, 8, 10]
```

Using `map()`:

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8, 10]
```

`map()` is useful when you want to perform the **same transformation on every element**.

---

# 📚 3. Syntax of `map()`

The general syntax is:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

result = map(str, numbers)

print(list(result))
```

The structure is:

```text
map(
    function,
    iterable
)
```

Where:

```text
function
   ↓
Operation to perform

iterable
   ↓
Data to process
```

---

# 🔍 4. Understanding `map()` Step by Step

Consider:

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)
```

Python conceptually performs:

```text
1 → 1 × 2 → 2
2 → 2 × 2 → 4
3 → 3 × 2 → 6
4 → 4 × 2 → 8
```

So the mapped result contains:

```text
2
4
6
8
```

To see all results as a list:

```python
print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

---

# 🧠 5. `map()` Returns a Map Object

A common beginner mistake is expecting `map()` to directly return a list.

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

Output will look similar to:

```text
<map object at 0x...>
```

This happens because `map()` returns a **map object**, not a list.

To convert it into a list:

```python
print(list(result))
```

Output:

```text
[2, 4, 6]
```

---

# 🔄 6. Converting a `map` Object to a List

Example:

```python
numbers = [10, 20, 30]

result = map(lambda x: x + 5, numbers)

result = list(result)

print(result)
```

Output:

```text
[15, 25, 35]
```

The common pattern is:

```python
list(map(function, iterable))
```

Example:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

Output:

```text
[1, 4, 9, 16]
```

---

# 🔢 7. Using `map()` with Numbers

`map()` is commonly used to transform numeric data.

Example:

```python
numbers = [2, 4, 6, 8]

result = list(map(lambda x: x * 10, numbers))

print(result)
```

Output:

```text
[20, 40, 60, 80]
```

---

# ✖️ 8. Multiplying Every Number

Example:

```python
numbers = [5, 10, 15, 20]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Output:

```text
[10, 20, 30, 40]
```

---

# 🔢 9. Squaring Every Number

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 🧮 10. Cubing Every Number

Example:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x ** 3, numbers))

print(result)
```

Output:

```text
[1, 8, 27, 64]
```

---

# 🔤 11. Using `map()` with Strings

`map()` can also process strings.

Example:

```python
names = ["asha", "neha", "priya"]

result = list(map(str.upper, names))

print(result)
```

Output:

```text
['ASHA', 'NEHA', 'PRIYA']
```

Here:

```python
str.upper
```

is applied to every string.

---

# 🔠 12. Converting Strings to Lowercase

Example:

```python
names = ["ASHA", "NEHA", "PRIYA"]

result = list(map(str.lower, names))

print(result)
```

Output:

```text
['asha', 'neha', 'priya']
```

---

# 🔢 13. Converting Strings to Integers

Suppose numbers are stored as strings:

```python
numbers = ["10", "20", "30", "40"]
```

You can convert them into integers:

```python
result = list(map(int, numbers))

print(result)
```

Output:

```text
[10, 20, 30, 40]
```

Here:

```text
"10" → 10
"20" → 20
"30" → 30
"40" → 40
```

---

# 🔢 14. Converting Numbers to Strings

Example:

```python
numbers = [10, 20, 30]

result = list(map(str, numbers))

print(result)
```

Output:

```text
['10', '20', '30']
```

This is useful when numeric values need to be displayed or combined with text.

---

# 🧩 15. Using `map()` with a User-Defined Function

You can create your own function and pass it to `map()`.

Example:

```python
def square(number):
    return number ** 2


numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16]
```

The function:

```python
square()
```

is executed for every element.

---

# 🧠 16. Understanding Function Passing

Notice this:

```python
map(square, numbers)
```

We write:

```python
square
```

not:

```python
square()
```

Why?

Because `map()` needs the **function itself** so it can call that function for each element.

Conceptually:

```text
map(square, numbers)

       ↓

square(1)
square(2)
square(3)
square(4)
```

---

# ⚡ 17. Using `map()` with `lambda`

`lambda` is commonly used with `map()` when the transformation is small.

Example:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x + 10, numbers))

print(result)
```

Output:

```text
[11, 12, 13, 14]
```

The lambda function:

```python
lambda x: x + 10
```

means:

```text
Take x
   ↓
Add 10
   ↓
Return result
```

---

# 🔄 18. `map()` with Multiple Operations

You can perform expressions inside the function.

Example:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2 + 5, numbers))

print(result)
```

Output:

```text
[7, 9, 11, 13]
```

For example:

```text
1 × 2 + 5 = 7
2 × 2 + 5 = 9
3 × 2 + 5 = 11
4 × 2 + 5 = 13
```

---

# ⚖️ 19. `map()` vs `for` Loop

Using a loop:

```python
numbers = [1, 2, 3, 4]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

Using `map()`:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Both produce:

```text
[2, 4, 6, 8]
```

The difference is mainly in the style of expressing the transformation.

---

# ⚖️ 20. `map()` vs List Comprehension

Using `map()`:

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

Using list comprehension:

```python
numbers = [1, 2, 3, 4]

result = [x * 2 for x in numbers]

print(result)
```

Both produce:

```text
[2, 4, 6, 8]
```

For simple transformations, list comprehensions are often easier to read.

---

# 🔍 21. Using `map()` with `abs()`

Built-in functions can be passed directly to `map()`.

Example:

```python
numbers = [-10, -20, 30, -40]

result = list(map(abs, numbers))

print(result)
```

Output:

```text
[10, 20, 30, 40]
```

Here:

```python
abs()
```

is applied to every element.

---

# 🔢 22. Using `map()` with `round()`

Example:

```python
prices = [10.567, 20.789, 30.123]

result = list(map(lambda x: round(x, 2), prices))

print(result)
```

Output:

```text
[10.57, 20.79, 30.12]
```

This can be useful when processing decimal data.

---

# 🧮 23. Using `map()` with Multiple Iterables

`map()` can accept more than one iterable.

Example:

```python
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = list(map(lambda x, y: x + y, numbers1, numbers2))

print(result)
```

Output:

```text
[11, 22, 33]
```

The elements are processed position by position:

```text
1 + 10 = 11
2 + 20 = 22
3 + 30 = 33
```

---

# 🔗 24. `map()` with Three Iterables

You can use more than two iterables.

Example:

```python
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]

result = list(map(lambda x, y, z: x + y + z, a, b, c))

print(result)
```

Output:

```text
[111, 222, 333]
```

---

# ⚠️ 25. Different Length Iterables

When multiple iterables are supplied, `map()` stops when the **shortest iterable is exhausted**.

Example:

```python
a = [1, 2, 3, 4]
b = [10, 20]

result = list(map(lambda x, y: x + y, a, b))

print(result)
```

Output:

```text
[11, 22]
```

The remaining elements of `a` are not processed.

---

# 🧠 26. Using `map()` with `if-else`

You can use conditional expressions inside a lambda.

Example:

```python
numbers = [10, 15, 20, 25]

result = list(map(
    lambda x: "Even" if x % 2 == 0 else "Odd",
    numbers
))

print(result)
```

Output:

```text
['Even', 'Odd', 'Even', 'Odd']
```

---

# 🔍 27. Classifying Marks Using `map()`

Example:

```python
marks = [90, 75, 60, 45]

result = list(map(
    lambda mark: "Pass" if mark >= 50 else "Fail",
    marks
))

print(result)
```

Output:

```text
['Pass', 'Pass', 'Pass', 'Fail']
```

---

# 🎓 28. Converting Marks to Grades

Example:

```python
marks = [95, 82, 68, 45]

result = list(map(
    lambda mark: "A" if mark >= 90
    else "B" if mark >= 75
    else "C" if mark >= 50
    else "F",
    marks
))

print(result)
```

Output:

```text
['A', 'B', 'C', 'F']
```

---

# 🔤 29. Adding Text to Every Element

Example:

```python
names = ["Asha", "Neha", "Priya"]

result = list(map(lambda name: "Student: " + name, names))

print(result)
```

Output:

```text
['Student: Asha', 'Student: Neha', 'Student: Priya']
```

---

# 💰 30. Applying a Discount Using `map()`

Example:

```python
prices = [1000, 2000, 3000]

discounted = list(map(lambda price: price * 0.9, prices))

print(discounted)
```

Output:

```text
[900.0, 1800.0, 2700.0]
```

Here:

```text
90% of original price
```

is calculated for every item.

---

# 🛒 31. Shopping Cart Example

Example:

```python
prices = [500, 1000, 1500, 2000]

final_prices = list(map(lambda price: price * 1.18, prices))

print(final_prices)
```

Output:

```text
[590.0, 1180.0, 1770.0, 2360.0]
```

This demonstrates applying the same calculation to every price.

---

# 👨‍🎓 32. Student Marks Example

Example:

```python
marks = [70, 80, 65, 90]

updated_marks = list(map(lambda mark: mark + 5, marks))

print(updated_marks)
```

Output:

```text
[75, 85, 70, 95]
```

---

# 🌡️ 33. Temperature Conversion

Suppose temperatures are stored in Celsius.

Formula:

```text
Fahrenheit = Celsius × 9/5 + 32
```

Example:

```python
celsius = [0, 10, 20, 30]

fahrenheit = list(
    map(lambda c: c * 9 / 5 + 32, celsius)
)

print(fahrenheit)
```

Output:

```text
[32.0, 50.0, 68.0, 86.0]
```

---

# 💵 34. Salary Increment Example

Example:

```python
salaries = [30000, 40000, 50000]

updated = list(map(lambda salary: salary * 1.10, salaries))

print(updated)
```

Output:

```text
[33000.0, 44000.0, 55000.0]
```

Here, a 10% increment is applied to every salary.

---

# 📱 35. Formatting Phone Numbers

Example:

```python
numbers = [9876543210, 8765432109, 7654321098]

formatted = list(map(lambda number: "+91-" + str(number), numbers))

print(formatted)
```

Output:

```text
['+91-9876543210', '+91-8765432109', '+91-7654321098']
```

---

# 🔄 36. Using `map()` with `split()`

Suppose:

```python
data = ["10", "20", "30", "40"]
```

You can convert every element:

```python
numbers = list(map(int, data))

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

This is one of the most common practical uses of `map()`.

---

# ⌨️ 37. Taking Multiple Inputs Using `map()`

A very common Python pattern is:

```python
numbers = list(map(int, input().split()))

print(numbers)
```

If the user enters:

```text
10 20 30 40
```

Output:

```text
[10, 20, 30, 40]
```

Here:

```text
input()
   ↓
"10 20 30 40"
   ↓
split()
   ↓
["10", "20", "30", "40"]
   ↓
map(int, ...)
   ↓
10, 20, 30, 40
   ↓
list()
   ↓
[10, 20, 30, 40]
```

---

# 🧠 38. Multiple Inputs with Two Variables

Example:

```python
a, b = map(int, input().split())

print(a)
print(b)
```

Input:

```text
10 20
```

Output:

```text
10
20
```

This is commonly used in competitive programming and coding problems.

---

# 🔢 39. Multiple Inputs with Three Variables

Example:

```python
x, y, z = map(int, input().split())

print(x + y + z)
```

Input:

```text
10 20 30
```

Output:

```text
60
```

---

# 🔗 40. Combining `map()` with `filter()`

`map()` transforms data.

`filter()` selects data.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared = map(lambda x: x ** 2, even_numbers)

print(list(squared))
```

Output:

```text
[4, 16, 36]
```

The process is:

```text
Original data
     ↓
filter()
     ↓
Even numbers
     ↓
map()
     ↓
Squares
```

---

# 🔄 41. `map()` After `filter()`

Example:

```python
numbers = [5, 10, 15, 20, 25, 30]

result = map(
    lambda x: x * 2,
    filter(lambda x: x >= 15, numbers)
)

print(list(result))
```

Output:

```text
[30, 40, 50, 60]
```

First:

```text
15, 20, 25, 30
```

Then:

```text
30, 40, 50, 60
```

---

# 🧠 42. `map()` and Lazy Evaluation

A `map` object is evaluated lazily.

This means Python does not necessarily create all transformed results immediately.

Example:

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)
```

The transformation happens as the map object is consumed.

For example:

```python
print(list(result))
```

produces:

```text
[2, 4, 6, 8]
```

This behavior can be useful when working with large iterables.

---

# ⚠️ 43. Common Mistake: Forgetting `list()`

Consider:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

You may see:

```text
<map object at 0x...>
```

This does not mean `map()` failed.

Use:

```python
print(list(result))
```

Output:

```text
[2, 4, 6]
```

---

# ⚠️ 44. Common Mistake: Calling the Function Immediately

Wrong:

```python
numbers = [1, 2, 3]

result = map(square(), numbers)
```

If `square()` requires an argument, this will cause an error.

Correct:

```python
result = map(square, numbers)
```

Remember:

```text
square
  ↓
Pass the function

square()
  ↓
Call the function immediately
```

---

# ⚠️ 45. Common Mistake: Reusing an Exhausted Map Object

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))
print(list(result))
```

Output:

```text
[2, 4, 6]
[]
```

Why?

Because the map object has already been consumed.

If you need the results multiple times:

```python
result = list(map(lambda x: x * 2, numbers))

print(result)
print(result)
```

Output:

```text
[2, 4, 6]
[2, 4, 6]
```

---

# ⚖️ 46. `map()` vs `filter()`

| Function   | Purpose                              |
| ---------- | ------------------------------------ |
| `map()`    | Transform every element              |
| `filter()` | Select elements based on a condition |

Example of `map()`:

```python
numbers = [1, 2, 3]

result = list(map(lambda x: x * 2, numbers))
```

Output:

```text
[2, 4, 6]
```

Example of `filter()`:

```python
numbers = [1, 2, 3, 4]

result = list(filter(lambda x: x % 2 == 0, numbers))
```

Output:

```text
[2, 4]
```

Remember:

```text
map()
 ↓
Transform

filter()
 ↓
Select
```

---

# ⚖️ 47. `map()` vs List Comprehension

| Feature             | `map()`                         | List Comprehension    |
| ------------------- | ------------------------------- | --------------------- |
| Main purpose        | Transform data                  | Transform/filter data |
| Returns             | Map object                      | List                  |
| Uses function       | Yes                             | Usually expression    |
| Supports conditions | Through function                | Directly              |
| Readability         | Good for simple transformations | Often very readable   |

Example:

```python
list(map(lambda x: x * 2, numbers))
```

Equivalent:

```python
[x * 2 for x in numbers]
```

---

# 📊 48. `map()` Method Comparison

| Usage              | Example                         | Result                     |
| ------------------ | ------------------------------- | -------------------------- |
| Numbers            | `map(abs, numbers)`             | Absolute values            |
| Strings            | `map(str.upper, names)`         | Uppercase strings          |
| Conversion         | `map(int, values)`              | Integers                   |
| Lambda             | `map(lambda x: x * 2, numbers)` | Doubled values             |
| Multiple iterables | `map(lambda x,y: x+y, a,b)`     | Combined values            |
| Conditions         | `map(lambda x: ..., numbers)`   | Conditional transformation |

---

# 🌍 49. Real-World Example: Product Prices

```python
prices = [500, 1000, 1500, 2000]

discounted_prices = list(
    map(lambda price: price * 0.9, prices)
)

print(discounted_prices)
```

Output:

```text
[450.0, 900.0, 1350.0, 1800.0]
```

Here, a 10% discount is applied to every product.

---

# 🌍 50. Real-World Example: Student Marks

```python
marks = [65, 72, 81, 90]

bonus_marks = list(
    map(lambda mark: mark + 5, marks)
)

print(bonus_marks)
```

Output:

```text
[70, 77, 86, 95]
```

This can represent adding bonus marks to every student's score.

---

# 🌍 51. Real-World Example: Employee Salaries

```python
salaries = [30000, 35000, 40000, 50000]

updated_salaries = list(
    map(lambda salary: salary * 1.08, salaries)
)

print(updated_salaries)
```

Output:

```text
[32400.0, 37800.0, 43200.0, 54000.0]
```

An 8% increment is applied to every salary.

---

# 🌍 52. Real-World Example: Temperature Conversion

```python
temperatures = [20, 25, 30, 35]

fahrenheit = list(
    map(lambda c: c * 9 / 5 + 32, temperatures)
)

print(fahrenheit)
```

Output:

```text
[68.0, 77.0, 86.0, 95.0]
```

---

# 🌍 53. Real-World Example: Usernames

```python
usernames = ["Asha20", "Neha25", "Priya30"]

formatted = list(
    map(lambda username: username.lower(), usernames)
)

print(formatted)
```

Output:

```text
['asha20', 'neha25', 'priya30']
```

This can be useful when normalizing user input.

---

# 🌍 54. Real-World Example: Student Grade Classification

```python
marks = [95, 82, 74, 61, 42]

grades = list(
    map(
        lambda mark:
        "A" if mark >= 90
        else "B" if mark >= 75
        else "C" if mark >= 60
        else "F",
        marks
    )
)

print(grades)
```

Output:

```text
['A', 'B', 'C', 'C', 'F']
```

---

# 💻 55. Practice Programs

## 🟢 Easy

### Program 1: Double Every Number

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

---

### Program 2: Square Every Number

```python
numbers = [2, 4, 6, 8]

result = list(map(lambda x: x ** 2, numbers))

print(result)
```

---

### Program 3: Convert Strings to Integers

```python
numbers = ["10", "20", "30", "40"]

result = list(map(int, numbers))

print(result)
```

---

### Program 4: Convert Names to Uppercase

```python
names = ["asha", "neha", "priya"]

result = list(map(str.upper, names))

print(result)
```

---

# 🟡 Medium

### Program 5: Add 10 to Every Number

```python
numbers = [10, 20, 30, 40]

result = list(map(lambda x: x + 10, numbers))

print(result)
```

---

### Program 6: Convert Celsius to Fahrenheit

```python
celsius = [0, 10, 20, 30]

result = list(
    map(lambda c: c * 9 / 5 + 32, celsius)
)

print(result)
```

---

### Program 7: Add Two Lists

```python
a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

result = list(map(lambda x, y: x + y, a, b))

print(result)
```

---

### Program 8: Classify Numbers as Even or Odd

```python
numbers = [10, 15, 20, 25]

result = list(
    map(
        lambda x: "Even" if x % 2 == 0 else "Odd",
        numbers
    )
)

print(result)
```

---

# 🔴 Advanced

## Program 9: Calculate Discounted Prices

```python
prices = [1000, 2000, 3000, 4000]

discounted = list(
    map(lambda price: price * 0.85, prices)
)

print(discounted)
```

Output:

```text
[850.0, 1700.0, 2550.0, 3400.0]
```

---

## Program 10: Student Grade Conversion

```python
marks = [95, 84, 72, 61, 45]

grades = list(
    map(
        lambda mark:
        "A" if mark >= 90
        else "B" if mark >= 75
        else "C" if mark >= 60
        else "F",
        marks
    )
)

print(grades)
```

---

## Program 11: Employee Salary Increment

```python
salaries = [30000, 40000, 50000, 60000]

updated = list(
    map(lambda salary: salary * 1.10, salaries)
)

print(updated)
```

---

## Program 12: Combine Two Lists

```python
first_names = ["Asha", "Neha", "Priya"]
last_names = ["Sharma", "Patel", "Kumar"]

full_names = list(
    map(lambda first, last: first + " " + last,
        first_names,
        last_names)
)

print(full_names)
```

Output:

```text
['Asha Sharma', 'Neha Patel', 'Priya Kumar']
```

---

# 🏆 56. Challenge

Create a list containing student marks:

```text
45
67
82
91
73
58
```

Then:

1. Add 5 bonus marks to every student using `map()`.
2. Display the updated marks.
3. Convert every mark into a grade using `map()`.
4. Display `"Pass"` or `"Fail"` for every student.
5. Convert the marks into percentages assuming the maximum mark is 100.
6. Use a user-defined function with `map()`.
7. Use `lambda` with `map()`.
8. Display the final results.

Example starting data:

```python
marks = [45, 67, 82, 91, 73, 58]
```

Try solving the challenge without copying the examples above.

---

# 🧪 57. Mini Project: Student Marks Processor

Create a student marks processing program.

Use:

```python
marks = [45, 67, 82, 91, 73, 58]
```

Perform the following operations:

* Add 5 bonus marks using `map()`.
* Make sure the marks do not exceed 100.
* Convert marks into grades.
* Determine Pass/Fail status.
* Display the updated marks.
* Display the grades.
* Display the status of each student.
* Use at least two different `map()` operations.
* Use both a user-defined function and `lambda`.

### Your Goal

Build a complete student marks processing program using `map()`.

---

# 🎤 58. Interview Questions

* [ ] What is `map()` in Python?
* [ ] Why is `map()` used?
* [ ] What is the syntax of `map()`?
* [ ] What does `map()` return?
* [ ] Why do we use `list()` with `map()`?
* [ ] Can `map()` work with strings?
* [ ] Can `map()` work with tuples?
* [ ] Can `map()` work with sets?
* [ ] Can you pass a user-defined function to `map()`?
* [ ] Can you use `lambda` with `map()`?
* [ ] Why do we pass `square` instead of `square()` to `map()`?
* [ ] Can `map()` accept multiple iterables?
* [ ] What happens when multiple iterables have different lengths?
* [ ] What is the difference between `map()` and `filter()`?
* [ ] What is the difference between `map()` and list comprehension?
* [ ] What does lazy evaluation mean in `map()`?
* [ ] Can a map object be reused after it has been consumed?
* [ ] How can you convert strings to integers using `map()`?
* [ ] How can you process multiple user inputs using `map()`?
* [ ] Can `map()` be combined with `filter()`?
* [ ] When should you prefer `map()` over a `for` loop?
* [ ] What are common mistakes when using `map()`?

---

# 📝 59. Assignment

Complete the following programs.

### Task 1

Create a list of five numbers.

Use `map()` to double every number.

---

### Task 2

Create a list of five numbers.

Use `map()` to calculate their squares.

---

### Task 3

Create a list containing numeric strings:

```text
"10"
"20"
"30"
"40"
"50"
```

Use `map()` to convert them into integers.

---

### Task 4

Create a list of names.

Use `map()` to convert every name to uppercase.

---

### Task 5

Create a list of prices.

Use `map()` to apply a 10% discount.

---

### Task 6

Create a list of employee salaries.

Use `map()` to increase every salary by 5%.

---

### Task 7

Create two lists of numbers.

Use `map()` to add corresponding elements.

---

### Task 8

Create a list of numbers.

Use `map()` to display `"Even"` or `"Odd"` for every number.

---

### Task 9

Create a list of student marks.

Use `map()` to convert every mark into:

```text
A
B
C
F
```

based on suitable conditions.

---

### Task 10

Use:

```python
input().split()
```

and `map()` to accept five integer values from the user.

---

### Task 11

Create a real-world program and use at least five different `map()` operations or `map()` patterns.

---

### Task 12

Create a program that uses both `filter()` and `map()`.

First select values satisfying a condition and then transform the selected values.

---

# 🧠 60. Memory Tricks

Remember:

```text
map()
  ↓
Apply a function
  ↓
To every element
```

---

Remember the basic syntax:

```python
map(function, iterable)
```

---

Remember:

```text
map()
 ↓
Transform
 ↓
Every element
```

---

Remember:

```text
filter()
   ↓
Select

map()
   ↓
Transform
```

---

Remember:

```text
list(map(...))
      ↓
See the results as a list
```

---

Remember:

```text
map()
 ↓
One function
 ↓
Many elements
```

---

# 📌 61. Important Rules to Remember

```text
1. map() is a built-in Python function.

2. map() applies a function to every element of an iterable.

3. The basic syntax is map(function, iterable).

4. map() returns a map object.

5. Use list() when you want to convert the result into a list.

6. map() can work with lists, tuples, strings, sets, and other iterables.

7. A user-defined function can be passed to map().

8. lambda is commonly used with map().

9. map() can accept multiple iterables.

10. When multiple iterables are used, processing stops when the shortest iterable is exhausted.

11. map() is mainly used for transformation.

12. filter() is mainly used for selection.

13. map() objects are lazy and produce results as they are consumed.

14. A map object can be exhausted after being iterated over.

15. map() can be combined with filter().

16. map() can be used with conditions through lambda or other functions.

17. map() is commonly used with input().split() for converting input values.

18. map() can be replaced by list comprehension in many situations.

19. map() is especially useful for applying the same operation to every element.

20. Choose the approach that makes the code easiest to understand.
```

---

# 📊 62. `map()` Structure

```text
                         ITERABLE
                            │
                            ↓
                         map()
                            │
                ┌───────────┴───────────┐
                ↓                       ↓
             FUNCTION                ELEMENTS
                │                       │
                └───────────┬───────────┘
                            ↓
                    Apply Function
                     to Each Element
                            │
                            ↓
                       MAP OBJECT
                            │
                            ↓
                         list()
                            │
                            ↓
                         RESULT
```

---

# 🔄 63. `map()` Processing Flow

```text
numbers = [1, 2, 3, 4]

             ↓

map(lambda x: x * 2, numbers)

             ↓

        1 → 2
        2 → 4
        3 → 6
        4 → 8

             ↓

list()

             ↓

       [2, 4, 6, 8]
```

---

# 📚 64. Complete `map()` Cheat Sheet

### Basic `map()`

```python
map(function, iterable)
```

### Convert Result to List

```python
list(map(function, iterable))
```

### Double Numbers

```python
list(map(lambda x: x * 2, numbers))
```

### Square Numbers

```python
list(map(lambda x: x ** 2, numbers))
```

### Convert Strings to Integers

```python
list(map(int, values))
```

### Convert Numbers to Strings

```python
list(map(str, numbers))
```

### Convert Strings to Uppercase

```python
list(map(str.upper, names))
```

### Use a User-Defined Function

```python
list(map(function_name, values))
```

### Use Multiple Iterables

```python
list(map(lambda x, y: x + y, list1, list2))
```

### Use Conditional Expression

```python
list(
    map(
        lambda x: "Even" if x % 2 == 0 else "Odd",
        numbers
    )
)
```

### Use with Input

```python
numbers = list(map(int, input().split()))
```

### Combine with `filter()`

```python
list(
    map(
        lambda x: x * 2,
        filter(lambda x: x > 10, numbers)
    )
)
```

---

# 🏆 65. `map()` Mastery

```text
                         map()
                           │
                           ↓
                  Apply a Function
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
          Numbers        Strings      Multiple
                                        Iterables
             │             │             │
             ↓             ↓             ↓
          Transform     Transform      Combine
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                      MAP OBJECT
                           │
                           ↓
                         list()
                           │
                           ↓
                         RESULT
```

---

# 📚 66. Summary

In this lesson, you learned:

* What `map()` is.
* Why `map()` is used.
* The syntax of `map()`.
* How `map()` applies a function to every element.
* What a map object is.
* How to convert a map object into a list.
* How to use `map()` with numbers.
* How to use `map()` with strings.
* How to use `map()` with built-in functions.
* How to use `map()` with user-defined functions.
* How to use `map()` with `lambda`.
* How to use `map()` with multiple iterables.
* What happens when iterables have different lengths.
* How to use conditional expressions with `map()`.
* How to use `map()` with `input().split()`.
* How to combine `map()` with `filter()`.
* What lazy evaluation means.
* Why map objects can be exhausted.
* The difference between `map()` and `filter()`.
* The difference between `map()` and list comprehension.
* How to use `map()` in real-world applications.
* Common mistakes when using `map()`.
* How to solve practical problems using `map()`.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `map()` is.
* [ ] I understand why `map()` is used.
* [ ] I know the syntax of `map()`.
* [ ] I understand what a map object is.
* [ ] I can convert a map object into a list.
* [ ] I can use `map()` with numbers.
* [ ] I can use `map()` with strings.
* [ ] I can use built-in functions with `map()`.
* [ ] I can use user-defined functions with `map()`.
* [ ] I can use `lambda` with `map()`.
* [ ] I can use `map()` with multiple iterables.
* [ ] I understand how different iterable lengths are handled.
* [ ] I can use conditions with `map()`.
* [ ] I can use `map()` with `input().split()`.
* [ ] I understand lazy evaluation.
* [ ] I understand why a map object can be exhausted.
* [ ] I understand the difference between `map()` and `filter()`.
* [ ] I understand the difference between `map()` and list comprehension.
* [ ] I can combine `map()` with `filter()`.
* [ ] I can use `map()` in real-world programs.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use `map()` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: `filter()`**

In the next topic, you will learn:

* What `filter()` is.
* Why `filter()` is used.
* Basic `filter()` syntax.
* How `filter()` works.
* Using `filter()` with functions.
* Using `filter()` with `lambda`.
* Filtering numbers.
* Filtering strings.
* Filtering even and odd numbers.
* Filtering values using conditions.
* Filtering data using multiple conditions.
* Understanding `filter` objects.
* Converting `filter` objects into lists.
* Combining `filter()` with `map()`.
* Comparing `filter()` with loops.
* Comparing `filter()` with list comprehension.
* Practical real-world examples.
* Common mistakes.
* Advanced filtering techniques.
* Practice programs and challenges.
* Mini projects using `filter()`.

---

## ⭐ Quote of the Day

> **"The power of `map()` is simple: give one transformation, and apply it across an entire collection."** 🐍📚
