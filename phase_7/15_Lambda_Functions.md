# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 15: Lambda Functions

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what lambda functions are.
* [ ] Understand the difference between normal functions and lambda functions.
* [ ] Understand the syntax of lambda functions.
* [ ] Create simple lambda functions.
* [ ] Use lambda functions with multiple arguments.
* [ ] Use lambda functions with variables.
* [ ] Use lambda functions with conditions.
* [ ] Use lambda functions with `if-else`.
* [ ] Use lambda functions with `map()`.
* [ ] Use lambda functions with `filter()`.
* [ ] Use lambda functions with `sorted()`.
* [ ] Understand the `key` parameter with lambda.
* [ ] Use lambda functions with lists.
* [ ] Use lambda functions with dictionaries.
* [ ] Use lambda functions with tuples.
* [ ] Use lambda functions in real-world applications.
* [ ] Understand when to use lambda functions.
* [ ] Avoid common mistakes when using lambda functions.
* [ ] Understand the limitations of lambda functions.
* [ ] Combine lambda functions with other Python functions.

---

# 📖 1. What is a Lambda Function?

A **lambda function** is a small anonymous function in Python.

The word **anonymous** means that the function does not need a regular function name.

A normal function is created using `def`.

Example:

```python
def square(x):
    return x * x

print(square(5))
```

Output:

```text
25
```

The same operation can be written using a lambda function:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

Here:

```text
lambda → creates the anonymous function
x      → parameter
:      → separates parameter from expression
x * x  → expression
```

---

# 🧠 2. Basic Lambda Syntax

The general syntax is:

```python
lambda arguments: expression
```

Example:

```python
lambda x: x * 2
```

Here:

```text
lambda → keyword
x      → argument
:      → separates argument and expression
x * 2  → expression
```

A lambda function automatically returns the result of its expression.

---

# 📚 3. Lambda Function vs Normal Function

A normal function:

```python
def square(x):
    return x * x
```

Lambda version:

```python
square = lambda x: x * x
```

Both can be called like this:

```python
print(square(5))
```

Output:

```text
25
```

The main difference is that lambda functions are designed for **small, simple operations**.

---

# 🔍 4. Creating a Simple Lambda Function

Example:

```python
double = lambda x: x * 2

print(double(10))
```

Output:

```text
20
```

The lambda function receives `10` and calculates:

```text
10 * 2 = 20
```

---

# 🧠 5. Lambda Function with One Argument

A lambda function can accept one argument.

Example:

```python
cube = lambda x: x ** 3

print(cube(4))
```

Output:

```text
64
```

Because:

```text
4³ = 64
```

---

# ➕ 6. Lambda Function with Multiple Arguments

Lambda functions can accept multiple arguments.

Example:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Syntax:

```python
lambda argument1, argument2: expression
```

---

# 🧮 7. Lambda Function with Three Arguments

Example:

```python
total = lambda a, b, c: a + b + c

print(total(10, 20, 30))
```

Output:

```text
60
```

The arguments are:

```text
a = 10
b = 20
c = 30
```

The expression becomes:

```text
10 + 20 + 30
```

---

# 🔢 8. Lambda Function for Square

Example:

```python
square = lambda number: number ** 2

print(square(7))
```

Output:

```text
49
```

This is useful when a small calculation is required.

---

# 🧮 9. Lambda Function for Even Numbers

Example:

```python
is_even = lambda number: number % 2 == 0

print(is_even(10))
print(is_even(7))
```

Output:

```text
True
False
```

The expression:

```python
number % 2 == 0
```

checks whether the number is divisible by `2`.

---

# 🔤 10. Lambda Function with Strings

Lambda functions can also work with strings.

Example:

```python
length = lambda word: len(word)

print(length("Python"))
```

Output:

```text
6
```

The lambda function receives a string and returns its length.

---

# 🧠 11. Lambda Function with String Conversion

Example:

```python
upper = lambda text: text.upper()

print(upper("python"))
```

Output:

```text
PYTHON
```

Lambda functions can call built-in functions and methods inside their expression.

---

# ⚖️ 12. Lambda Function with `if-else`

Lambda functions can contain conditional expressions.

Syntax:

```python
lambda value: result_if_true if condition else result_if_false
```

Example:

```python
check = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check(8))
```

Output:

```text
Even
```

---

# 🔍 13. Lambda Function to Find Greater Number

Example:

```python
greater = lambda a, b: a if a > b else b

print(greater(25, 40))
```

Output:

```text
40
```

The condition checks:

```python
a > b
```

If true, `a` is returned.

Otherwise, `b` is returned.

---

# 🧠 14. Lambda Function for Pass/Fail

Example:

```python
result = lambda marks: "Pass" if marks >= 40 else "Fail"

print(result(75))
```

Output:

```text
Pass
```

This is useful in simple decision-making operations.

---

# 🔁 15. Lambda Functions with `map()`

The `map()` function applies a function to every item in an iterable.

Lambda functions are commonly used with `map()`.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

Here:

```text
numbers
   ↓
map()
   ↓
lambda
   ↓
square each number
```

---

# 🔄 16. Using `map()` to Double Values

Example:

```python
numbers = [10, 20, 30, 40]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[20, 40, 60, 80]
```

The lambda function runs once for every element.

---

# 🔢 17. Using `map()` with Strings

Example:

```python
names = ["asha", "neha", "kiran"]

result = map(lambda name: name.upper(), names)

print(list(result))
```

Output:

```text
['ASHA', 'NEHA', 'KIRAN']
```

---

# 🧩 18. Lambda Functions with `filter()`

The `filter()` function selects items based on a condition.

Example:

```python
numbers = [10, 15, 20, 25, 30]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))
```

Output:

```text
[10, 20, 30]
```

Here the lambda returns either:

```text
True
```

or

```text
False
```

Only elements producing `True` are kept.

---

# 🔍 19. Filtering Marks

Example:

```python
marks = [35, 78, 45, 92, 28, 85]

passed = filter(lambda mark: mark >= 40, marks)

print(list(passed))
```

Output:

```text
[78, 45, 92, 85]
```

Only marks greater than or equal to `40` are selected.

---

# 🔤 20. Filtering Names

Example:

```python
names = ["Asha", "Neha", "Kiran", "Anita"]

result = filter(lambda name: len(name) > 4, names)

print(list(result))
```

Output:

```text
['Kiran', 'Anita']
```

The lambda checks the length of each name.

---

# 📊 21. Lambda Functions with `sorted()`

Lambda functions are extremely useful with `sorted()`.

Example:

```python
numbers = [45, 12, 89, 23, 7]

result = sorted(numbers, key=lambda x: x)

print(result)
```

Output:

```text
[7, 12, 23, 45, 89]
```

The `key` parameter tells Python what value should be used for sorting.

---

# 🔢 22. Sorting Numbers by Their Last Digit

Example:

```python
numbers = [25, 14, 31, 42, 18]

result = sorted(numbers, key=lambda x: x % 10)

print(result)
```

Output:

```text
[31, 42, 14, 25, 18]
```

The sorting is based on:

```text
25 → 5
14 → 4
31 → 1
42 → 2
18 → 8
```

So the numbers are sorted according to their last digit.

---

# 🔤 23. Sorting Strings by Length

Example:

```python
names = ["Asha", "Christopher", "Neha", "Kiran"]

result = sorted(names, key=lambda name: len(name))

print(result)
```

Output:

```text
['Asha', 'Neha', 'Kiran', 'Christopher']
```

The lambda function returns the length of each name.

---

# 🔄 24. Sorting in Descending Order

You can combine `lambda` with `reverse=True`.

Example:

```python
numbers = [10, 50, 20, 40, 30]

result = sorted(numbers, key=lambda x: x, reverse=True)

print(result)
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

# 📦 25. Lambda with Tuples

Suppose we have:

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 78)
]
```

We can sort students according to their marks:

```python
result = sorted(students, key=lambda student: student[1])

print(result)
```

Output:

```text
[('Kiran', 78), ('Asha', 85), ('Neha', 92)]
```

Here:

```python
student[1]
```

represents the marks.

---

# 📊 26. Sorting Tuples by Name

Example:

```python
students = [
    ("Neha", 92),
    ("Asha", 85),
    ("Kiran", 78)
]

result = sorted(students, key=lambda student: student[0])

print(result)
```

Output:

```text
[('Asha', 85), ('Kiran', 78), ('Neha', 92)]
```

Here:

```python
student[0]
```

represents the name.

---

# 🧠 27. Lambda with Dictionaries

Lambda functions are commonly used when working with dictionaries stored inside lists.

Example:

```python
employees = [
    {"name": "Asha", "salary": 45000},
    {"name": "Neha", "salary": 52000},
    {"name": "Kiran", "salary": 48000}
]

result = sorted(employees, key=lambda employee: employee["salary"])

for employee in result:
    print(employee)
```

Output:

```text
{'name': 'Asha', 'salary': 45000}
{'name': 'Kiran', 'salary': 48000}
{'name': 'Neha', 'salary': 52000}
```

The lambda tells `sorted()` to use the `"salary"` value.

---

# 💰 28. Sorting Products by Price

Example:

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500}
]

result = sorted(products, key=lambda product: product["price"])

for product in result:
    print(product)
```

Output:

```text
{'name': 'Mouse', 'price': 800}
{'name': 'Keyboard', 'price': 1500}
{'name': 'Laptop', 'price': 55000}
```

---

# 🔥 29. Finding the Maximum Using Lambda

The `max()` function can also use a lambda expression through the `key` parameter.

Example:

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 78)
]

top_student = max(students, key=lambda student: student[1])

print(top_student)
```

Output:

```text
('Neha', 92)
```

---

# 🔻 30. Finding the Minimum Using Lambda

Example:

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 78)
]

lowest = min(students, key=lambda student: student[1])

print(lowest)
```

Output:

```text
('Kiran', 78)
```

---

# 🧮 31. Lambda with `reduce()`

The `reduce()` function can repeatedly apply a function to items.

It is available from the `functools` module.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```text
15
```

The calculation happens like:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

---

# 🔢 32. Using `reduce()` to Multiply Numbers

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

Output:

```text
24
```

Because:

```text
1 × 2 × 3 × 4 = 24
```

---

# 🔗 33. Combining `map()`, `filter()` and `lambda`

Lambda functions can be combined with multiple functional tools.

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squares = map(lambda x: x ** 2, even_numbers)

print(list(squares))
```

Output:

```text
[4, 16, 36]
```

Process:

```text
Original numbers
       ↓
   filter()
       ↓
[2, 4, 6]
       ↓
    map()
       ↓
[4, 16, 36]
```

---

# 🧠 34. Lambda Functions with Variables

A lambda can use variables from its surrounding scope.

Example:

```python
tax = 0.18

calculate_tax = lambda price: price * tax

print(calculate_tax(1000))
```

Output:

```text
180.0
```

The lambda uses the value of `tax`.

---

# 🧮 35. Lambda Function for Discount Calculation

Example:

```python
discount = lambda price: price * 0.10

print(discount(5000))
```

Output:

```text
500.0
```

This calculates a 10% discount amount.

---

# 💰 36. Lambda Function for Final Price

Example:

```python
final_price = lambda price: price * 0.90

print(final_price(5000))
```

Output:

```text
4500.0
```

Here, 10% is discounted from the original price.

---

# 🔍 37. Lambda with Conditions and `map()`

Example:

```python
marks = [35, 48, 72, 90]

result = map(lambda mark: "Pass" if mark >= 40 else "Fail", marks)

print(list(result))
```

Output:

```text
['Fail', 'Pass', 'Pass', 'Pass']
```

---

# 🔢 38. Lambda with Conditions and `filter()`

Example:

```python
numbers = [12, 17, 24, 31, 40]

result = filter(lambda x: x > 20, numbers)

print(list(result))
```

Output:

```text
[24, 31, 40]
```

---

# 📊 39. Real-World Example: Student Marks

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 67),
    ("Anita", 78)
]

top_student = max(students, key=lambda student: student[1])

print("Top Student:", top_student)
```

Output:

```text
Top Student: ('Neha', 92)
```

The lambda allows `max()` to compare students using their marks.

---

# 🌍 40. Real-World Example: Employee Salaries

```python
employees = [
    {"name": "Asha", "salary": 45000},
    {"name": "Neha", "salary": 60000},
    {"name": "Kiran", "salary": 52000}
]

highest_paid = max(employees, key=lambda employee: employee["salary"])

print(highest_paid)
```

Output:

```text
{'name': 'Neha', 'salary': 60000}
```

---

# 🌍 41. Real-World Example: Product Sorting

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Monitor", "price": 12000}
]

products = sorted(products, key=lambda product: product["price"])

for product in products:
    print(product["name"], ":", product["price"])
```

Output:

```text
Mouse : 800
Monitor : 12000
Laptop : 55000
```

---

# 🌍 42. Real-World Example: Filtering Products

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Monitor", "price": 12000},
    {"name": "Keyboard", "price": 1500}
]

expensive = filter(lambda product: product["price"] > 10000, products)

for product in expensive:
    print(product)
```

Output:

```text
{'name': 'Laptop', 'price': 55000}
{'name': 'Monitor', 'price': 12000}
```

---

# ⚠️ 43. Common Mistake: Forgetting the Expression

Wrong:

```python
square = lambda x:
```

A lambda function must contain an expression after `:`.

Correct:

```python
square = lambda x: x * x
```

---

# ⚠️ 44. Common Mistake: Using Multiple Statements

A lambda is designed for a single expression.

This is not valid:

```python
result = lambda x:
    y = x * 2
    return y
```

Instead, use a normal function:

```python
def result(x):
    y = x * 2
    return y
```

Use lambda when the operation is short and simple.

---

# ⚠️ 45. Common Mistake: Expecting `lambda` to Replace Every Function

Lambda functions are useful for short operations.

For example:

```python
square = lambda x: x ** 2
```

is simple and readable.

But a large operation containing many steps should normally use `def`.

Example:

```python
def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        return "Pass"
    return "Fail"
```

A normal function is clearer here.

---

# ⚠️ 46. Common Mistake: Confusing Lambda with Calling a Function

Consider:

```python
square = lambda x: x ** 2
```

This creates the lambda function.

To call it:

```python
print(square(5))
```

Output:

```text
25
```

The difference is:

```text
square
   ↓
function object

square(5)
   ↓
function call
```

---

# 🧠 47. Lambda Function as an Argument

A lambda can be passed directly to another function.

Example:

```python
numbers = [5, 2, 8, 1]

result = sorted(numbers, key=lambda x: x)

print(result)
```

Here the lambda is passed directly to `sorted()`.

There is no need to create a separate function variable.

---

# 🔄 48. Lambda vs `def`

| Feature      | `def` Function             | Lambda Function                                   |
| ------------ | -------------------------- | ------------------------------------------------- |
| Name         | Usually named              | Usually anonymous                                 |
| Syntax       | Multiple lines possible    | Single expression                                 |
| Statements   | Multiple statements        | One expression                                    |
| `return`     | Uses `return`              | Automatically returns expression                  |
| Complexity   | Suitable for complex logic | Suitable for simple logic                         |
| Reusability  | Highly reusable            | Usually used for short operations                 |
| Common usage | General functions          | `map()`, `filter()`, `sorted()`, `min()`, `max()` |

---

# 📊 49. Lambda Functions with Common Built-in Functions

Lambda functions are frequently used with:

```text
map()
   ↓
Transform data

filter()
   ↓
Select data

sorted()
   ↓
Sort data

min()
   ↓
Find minimum

max()
   ↓
Find maximum
```

They are especially useful when these functions need a custom operation.

---

# 💻 50. Practice Programs

## 🟢 Easy

### Program 1: Create a Lambda for Square

```python
square = lambda x: x ** 2

print(square(6))
```

---

### Program 2: Create a Lambda for Cube

```python
cube = lambda x: x ** 3

print(cube(4))
```

---

### Program 3: Add Two Numbers

```python
add = lambda a, b: a + b

print(add(15, 25))
```

---

### Program 4: Check Even or Odd

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(17))
```

---

# 🟡 Medium

### Program 5: Double Every Number

```python
numbers = [5, 10, 15, 20]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

---

### Program 6: Filter Even Numbers

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

---

### Program 7: Sort Names by Length

```python
names = ["Asha", "Christopher", "Neha", "Kiran"]

result = sorted(names, key=lambda name: len(name))

print(result)
```

---

### Program 8: Find Highest Mark

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 78)
]

result = max(students, key=lambda student: student[1])

print(result)
```

---

# 🔴 Advanced

## Program 9: Filter Students by Marks

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 67),
    ("Anita", 78)
]

result = filter(lambda student: student[1] >= 80, students)

print(list(result))
```

Output:

```text
[('Asha', 85), ('Neha', 92)]
```

---

## Program 10: Sort Employees by Salary

```python
employees = [
    {"name": "Asha", "salary": 45000},
    {"name": "Neha", "salary": 60000},
    {"name": "Kiran", "salary": 52000}
]

result = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

for employee in result:
    print(employee)
```

---

## Program 11: Convert Marks to Pass/Fail

```python
marks = [35, 48, 72, 90, 28]

result = map(
    lambda mark: "Pass" if mark >= 40 else "Fail",
    marks
)

print(list(result))
```

---

## Program 12: Filter Expensive Products

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Monitor", "price": 12000},
    {"name": "Keyboard", "price": 1500}
]

result = filter(
    lambda product: product["price"] > 10000,
    products
)

for product in result:
    print(product)
```

---

# 🏆 51. Challenge

Create a list containing student records:

```text
Asha    85
Neha    92
Kiran   67
Anita   78
Priya   95
```

Store them as tuples.

Then:

1. Use `lambda` with `sorted()` to sort students by marks.
2. Sort students by marks in descending order.
3. Use `lambda` with `filter()` to find students who scored at least 80.
4. Use `lambda` with `max()` to find the highest-scoring student.
5. Use `lambda` with `min()` to find the lowest-scoring student.
6. Use `lambda` with `map()` to create a list containing only the student names.
7. Display the final results.

Example data:

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Kiran", 67),
    ("Anita", 78),
    ("Priya", 95)
]
```

Try solving the challenge without copying the solution.

---

# 🧪 52. Mini Project: Employee Salary Analysis

Create an employee list containing:

* Employee name
* Department
* Salary

Example:

```python
employees = [
    {
        "name": "Asha",
        "department": "Development",
        "salary": 45000
    },
    {
        "name": "Neha",
        "department": "Testing",
        "salary": 52000
    },
    {
        "name": "Kiran",
        "department": "Development",
        "salary": 60000
    },
    {
        "name": "Anita",
        "department": "Design",
        "salary": 48000
    }
]
```

Perform the following operations:

* Sort employees according to salary using `sorted()` and `lambda`.
* Find the highest-paid employee using `max()` and `lambda`.
* Find the lowest-paid employee using `min()` and `lambda`.
* Filter employees whose salary is greater than `50000`.
* Create a list containing employee names using `map()` and `lambda`.
* Display the results.

### Your Goal

Build a complete employee salary analysis program using lambda functions with `sorted()`, `filter()`, `map()`, `min()`, and `max()`.

---

# 🎤 53. Interview Questions

* [ ] What is a lambda function in Python?
* [ ] Why are lambda functions called anonymous functions?
* [ ] What is the syntax of a lambda function?
* [ ] Can a lambda function have multiple arguments?
* [ ] Can a lambda function contain multiple statements?
* [ ] What does a lambda function return?
* [ ] What is the difference between `def` and `lambda`?
* [ ] When should you use a lambda function?
* [ ] When should you avoid using a lambda function?
* [ ] Can lambda functions be stored in variables?
* [ ] Can lambda functions be passed as arguments?
* [ ] How is lambda commonly used with `map()`?
* [ ] How is lambda commonly used with `filter()`?
* [ ] How is lambda commonly used with `sorted()`?
* [ ] What is the purpose of the `key` parameter in `sorted()`?
* [ ] How can lambda be used with `max()`?
* [ ] How can lambda be used with `min()`?
* [ ] Can lambda functions contain `if-else`?
* [ ] What is the difference between an expression and a statement?
* [ ] Why is `lambda` useful with functional programming tools?
* [ ] What is `reduce()`?
* [ ] How can lambda be used with `reduce()`?
* [ ] What are the limitations of lambda functions?

---

# 📝 54. Assignment

Complete the following programs.

### Task 1

Create a lambda function that calculates the square of a number.

---

### Task 2

Create a lambda function that accepts two numbers and returns their product.

---

### Task 3

Create a lambda function that checks whether a number is positive or negative.

---

### Task 4

Create a list of numbers and use `map()` with lambda to calculate their cubes.

---

### Task 5

Create a list of numbers and use `filter()` with lambda to display only numbers greater than `50`.

---

### Task 6

Create a list of names and use `sorted()` with lambda to sort them according to their length.

---

### Task 7

Create a list of student tuples containing names and marks. Use `sorted()` with lambda to sort them according to marks.

---

### Task 8

Create a list of student tuples and use `max()` with lambda to find the student with the highest marks.

---

### Task 9

Create a list of student tuples and use `filter()` with lambda to display students who scored at least `75`.

---

### Task 10

Create a list of five products containing names and prices. Use `sorted()` with lambda to sort the products according to price.

---

### Task 11

Create a real-world employee dictionary list and use at least five different lambda-based operations.

---

### Task 12

Create a program that uses:

```text
map()
filter()
sorted()
```

together with lambda functions to process a list of numbers.

---

# 🧠 55. Memory Tricks

Remember the basic lambda structure:

```text
lambda
   ↓
arguments
   ↓
:
   ↓
expression
```

Example:

```python
lambda x: x * 2
```

---

Remember the most common lambda combinations:

```text
map()
 ↓
Transform
```

```text
filter()
 ↓
Select
```

```text
sorted()
 ↓
Sort
```

```text
max()
 ↓
Highest
```

```text
min()
 ↓
Lowest
```

---

Remember:

```text
lambda x: x * 2
       ↑       ↑
   argument  expression
```

---

# 📌 56. Important Rules to Remember

```text
1. Lambda functions are anonymous functions.

2. Lambda functions are created using the lambda keyword.

3. The basic syntax is lambda arguments: expression.

4. A lambda function can accept multiple arguments.

5. A lambda function contains one expression.

6. The expression is automatically returned.

7. Lambda functions are useful for short and simple operations.

8. Lambda functions are commonly used with map().

9. Lambda functions are commonly used with filter().

10. Lambda functions are commonly used with sorted().

11. Lambda functions can be used with min() and max().

12. Lambda functions can contain conditional expressions.

13. Lambda functions can be assigned to variables.

14. Lambda functions can be passed directly as arguments.

15. The key parameter is commonly used with lambda for custom sorting.

16. map() transforms elements.

17. filter() selects elements based on a condition.

18. sorted() can use lambda to determine the sorting key.

19. Complex multi-step logic is usually better written using def.

20. Lambda functions improve convenience, but they should not be used when they reduce readability.
```

---

# 📊 57. Lambda Functions Structure

```text
                         LAMBDA FUNCTION
                                │
                                ↓
                       lambda arguments
                                │
                                ↓
                            expression
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
            DIRECT             MAP              FILTER
              │                 │                 │
              ↓                 ↓                 ↓
        Simple operation   Transform data    Select data
                                │
                                ↓
                             SORTED
                                │
                                ↓
                          Custom sorting
                                │
                    ┌───────────┴───────────┐
                    ↓                       ↓
                   MAX                     MIN
                    │                       │
                    ↓                       ↓
               Highest value          Lowest value
```

---

# 📚 58. Complete Lambda Functions Cheat Sheet

### Basic Lambda

```python
lambda x: x * 2
```

### Store Lambda in a Variable

```python
double = lambda x: x * 2
```

### Multiple Arguments

```python
add = lambda a, b: a + b
```

### Conditional Lambda

```python
result = lambda x: "Even" if x % 2 == 0 else "Odd"
```

### Transform Data with `map()`

```python
result = map(lambda x: x * 2, numbers)
```

### Filter Data with `filter()`

```python
result = filter(lambda x: x > 10, numbers)
```

### Sort Using Lambda

```python
result = sorted(names, key=lambda name: len(name))
```

### Find Maximum

```python
result = max(students, key=lambda student: student[1])
```

### Find Minimum

```python
result = min(students, key=lambda student: student[1])
```

### Use Lambda with `reduce()`

```python
from functools import reduce

result = reduce(lambda a, b: a + b, numbers)
```

---

# 🏆 Lambda Functions Mastery

```text
                         LAMBDA
                            │
                            ↓
                  Anonymous Function
                            │
                            ↓
                     One Expression
                            │
         ┌──────────────────┼──────────────────┐
         ↓                  ↓                  ↓
       map()             filter()            sorted()
         │                  │                  │
         ↓                  ↓                  ↓
     Transform           Select              Sort
         │                  │                  │
         └──────────────────┼──────────────────┘
                            ↓
                     min() / max()
                            │
                            ↓
                   Find Lowest / Highest
                            │
                            ↓
                         reduce()
                            │
                            ↓
                    Combine / Accumulate
```

---

# 📚 Summary

In this lesson, you learned:

* What lambda functions are.
* Why lambda functions are called anonymous functions.
* How to create lambda functions.
* The syntax of lambda functions.
* How to use one argument with lambda.
* How to use multiple arguments with lambda.
* How to use lambda functions with numbers.
* How to use lambda functions with strings.
* How to use conditional expressions with lambda.
* How to use lambda functions with `map()`.
* How to use lambda functions with `filter()`.
* How to use lambda functions with `sorted()`.
* How to use lambda functions with the `key` parameter.
* How to sort strings using lambda.
* How to sort tuples using lambda.
* How to sort dictionaries using lambda.
* How to use lambda with `min()`.
* How to use lambda with `max()`.
* How to use lambda with `reduce()`.
* How to combine lambda with `map()` and `filter()`.
* How to use lambda functions in real-world programs.
* The difference between lambda functions and normal functions.
* Common mistakes when using lambda functions.
* The limitations of lambda functions.
* When to use lambda functions.
* When to prefer a normal `def` function.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what lambda functions are.
* [ ] I know why lambda functions are called anonymous functions.
* [ ] I understand lambda syntax.
* [ ] I can create a simple lambda function.
* [ ] I can use multiple arguments with lambda.
* [ ] I can use lambda with numbers.
* [ ] I can use lambda with strings.
* [ ] I can use `if-else` with lambda.
* [ ] I can use lambda with `map()`.
* [ ] I can use lambda with `filter()`.
* [ ] I can use lambda with `sorted()`.
* [ ] I understand the `key` parameter.
* [ ] I can sort tuples using lambda.
* [ ] I can sort dictionaries using lambda.
* [ ] I can use lambda with `min()`.
* [ ] I can use lambda with `max()`.
* [ ] I understand the purpose of `reduce()`.
* [ ] I can use lambda with `reduce()`.
* [ ] I understand the difference between lambda and `def`.
* [ ] I know when to use lambda functions.
* [ ] I know when not to use lambda functions.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use lambda functions without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: `map()`, `filter()` and `reduce()` Functions**

In the next topic, you will learn:

* What `map()` is.
* What `filter()` is.
* What `reduce()` is.
* How `map()` works internally.
* How `filter()` works internally.
* How `reduce()` works internally.
* Using `map()` with functions.
* Using `map()` with lambda functions.
* Using `filter()` with functions.
* Using `filter()` with lambda functions.
* Using `reduce()` with functions.
* Using `reduce()` with lambda functions.
* Combining `map()` and `filter()`.
* Combining `filter()` and `reduce()`.
* Combining `map()`, `filter()`, and `reduce()`.
* Processing lists using functional programming.
* Practical real-world examples.
* Common mistakes.
* Advanced functional programming techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Lambda functions turn small ideas into powerful one-line operations."** 🐍📚
