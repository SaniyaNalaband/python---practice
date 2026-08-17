# 🐍 Python Master Course

# ⚙️ Phase 7: Functions

## 📌 Topic 16: Higher Order Functions

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what higher order functions are.
* [ ] Understand functions as first-class objects.
* [ ] Pass functions as arguments to other functions.
* [ ] Return functions from other functions.
* [ ] Understand the difference between normal and higher order functions.
* [ ] Use built-in higher order functions.
* [ ] Use `map()` to transform data.
* [ ] Use `filter()` to select data.
* [ ] Use `reduce()` to combine data.
* [ ] Use `sorted()` with functions.
* [ ] Use the `key` parameter with functions.
* [ ] Use `lambda` functions with higher order functions.
* [ ] Combine higher order functions with conditions.
* [ ] Combine higher order functions with loops.
* [ ] Understand function references and function calls.
* [ ] Understand functions that return functions.
* [ ] Create custom higher order functions.
* [ ] Understand callbacks in Python.
* [ ] Use higher order functions in real-world applications.
* [ ] Avoid common mistakes when using higher order functions.
* [ ] Solve advanced problems using functional programming techniques.

---

# 📖 1. What are Higher Order Functions?

A **higher order function** is a function that does at least one of the following:

1. Takes another function as an argument.
2. Returns another function as its result.

In simple words:

```text
Function working with another function
             ↓
      Higher Order Function
```

Example:

```python
def square(x):
    return x * x

def calculate(func, number):
    return func(number)

print(calculate(square, 5))
```

Output:

```text
25
```

Here:

```text
square → function
calculate → higher order function
```

`calculate()` receives another function as an argument.

---

# 🧠 2. Functions are First-Class Objects

Python treats functions as **first-class objects**.

This means a function can be:

* Stored in a variable.
* Passed as an argument.
* Returned from another function.
* Stored inside a list.
* Stored inside a dictionary.

Example:

```python
def greet():
    print("Hello")

message = greet

message()
```

Output:

```text
Hello
```

Here:

```text
greet
  ↓
stored in
  ↓
message
```

Both names refer to the same function object.

---

# 🔍 3. Function Reference vs Function Call

This is very important when working with higher order functions.

Consider:

```python
def square(x):
    return x * x
```

Function reference:

```python
square
```

Function call:

```python
square(5)
```

The difference:

```text
square
  ↓
Function object/reference

square(5)
  ↓
Execute the function
```

Example:

```python
def greet():
    return "Hello"

x = greet
print(x())
```

Output:

```text
Hello
```

Notice that:

```python
x = greet
```

does not execute the function.

But:

```python
x = greet()
```

executes it immediately.

---

# ⚖️ 4. Normal Function vs Higher Order Function

A normal function may simply receive data and return a result.

Example:

```python
def add(a, b):
    return a + b
```

A higher order function works with another function.

Example:

```python
def calculate(operation, a, b):
    return operation(a, b)
```

Here:

```text
add()
   ↓
passed into
   ↓
calculate()
```

Therefore, `calculate()` is a higher order function.

---

# 📦 5. Passing a Function as an Argument

Python allows you to pass a function to another function.

Example:

```python
def square(number):
    return number * number

def execute(function, value):
    return function(value)

result = execute(square, 6)

print(result)
```

Output:

```text
36
```

The flow is:

```text
square
   ↓
execute(square, 6)
   ↓
function(value)
   ↓
square(6)
   ↓
36
```

---

# 🧠 6. Passing Multiple Functions

A higher order function can receive different functions.

Example:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 10, 5))
print(calculate(multiply, 10, 5))
```

Output:

```text
15
50
```

The same higher order function can perform different operations.

```text
calculate()
     │
     ├── add()
     │
     └── multiply()
```

---

# 🔗 7. Why Higher Order Functions are Useful

Higher order functions allow you to write flexible and reusable code.

Without higher order functions:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

With a higher order function:

```python
def calculate(operation, a, b):
    return operation(a, b)
```

Now the operation can be changed without changing `calculate()`.

Advantages:

* Code reuse.
* Flexibility.
* Less repetitive code.
* Cleaner data processing.
* Easier customization.
* Useful for functional programming.
* Useful for callbacks and event handling.

---

# 🧩 8. Returning a Function

A function can also return another function.

Example:

```python
def create_greeting():
    def greet():
        return "Hello"

    return greet

message = create_greeting()

print(message())
```

Output:

```text
Hello
```

The structure is:

```text
create_greeting()
        ↓
    returns
        ↓
      greet
        ↓
   message()
```

---

# 🔄 9. Returning Different Functions

A function can return different functions depending on a condition.

Example:

```python
def get_operation(choice):

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    if choice == "add":
        return add
    else:
        return multiply

operation = get_operation("add")

print(operation(10, 5))
```

Output:

```text
15
```

The returned function can then be called normally.

---

# 🧠 10. Functions Stored in Variables

Functions can be stored in variables.

Example:

```python
def greet():
    return "Welcome"

say_hello = greet

print(say_hello())
```

Output:

```text
Welcome
```

This is possible because functions are first-class objects.

---

# 📋 11. Functions Stored in a List

Functions can also be stored inside lists.

Example:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operations = [add, subtract]

print(operations[0](10, 5))
print(operations[1](10, 5))
```

Output:

```text
15
5
```

The list contains function objects.

```text
operations
     │
     ├── add
     └── subtract
```

---

# 🗂️ 12. Functions Stored in a Dictionary

Functions can be stored as dictionary values.

Example:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operations = {
    "add": add,
    "multiply": multiply
}

print(operations["add"](10, 5))
print(operations["multiply"](10, 5))
```

Output:

```text
15
50
```

This technique is useful for:

* Menus.
* Command systems.
* Calculators.
* Routing logic.
* Application actions.

---

# 🗺️ 13. The `map()` Function

`map()` is a built-in higher order function.

It applies a function to every item in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

The process is:

```text
1 → 2
2 → 4
3 → 6
4 → 8
```

---

# 🔢 14. Using `map()` with a Normal Function

You do not have to use `lambda`.

Example:

```python
def square(number):
    return number * number

numbers = [2, 4, 6, 8]

result = map(square, numbers)

print(list(result))
```

Output:

```text
[4, 16, 36, 64]
```

Here:

```text
square → function
map()  → higher order function
```

---

# 🔄 15. Understanding the `map()` Flow

Consider:

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x + 10, numbers)
```

Conceptually:

```text
1 → 11
2 → 12
3 → 13
4 → 14
```

Result:

```python
[11, 12, 13, 14]
```

`map()` transforms every element.

---

# 🔤 16. `map()` with Strings

`map()` can also transform strings.

Example:

```python
names = ["asha", "neha", "riya"]

result = map(str.upper, names)

print(list(result))
```

Output:

```text
['ASHA', 'NEHA', 'RIYA']
```

Here:

```text
str.upper
   ↓
passed to map()
   ↓
applied to every name
```

---

# 🔢 17. `map()` with Multiple Iterables

`map()` can work with multiple iterables.

Example:

```python
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = map(lambda a, b: a + b, numbers1, numbers2)

print(list(result))
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

# 🔍 18. The `filter()` Function

`filter()` is another built-in higher order function.

It selects elements based on a condition.

Syntax:

```python
filter(function, iterable)
```

The function should return a truthy or falsy result.

Example:

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x >= 20, numbers)

print(list(result))
```

Output:

```text
[20, 25, 30]
```

---

# 🧠 19. Understanding `filter()`

Suppose:

```python
numbers = [5, 12, 18, 7, 25]
```

Condition:

```python
x > 10
```

The process becomes:

```text
5  → False
12 → True
18 → True
7  → False
25 → True
```

Result:

```text
[12, 18, 25]
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

# 🔢 20. `filter()` with a Normal Function

Example:

```python
def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = filter(is_even, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6]
```

Here:

```text
is_even → function
filter  → higher order function
```

---

# 🔤 21. `filter()` with Strings

You can filter strings according to their properties.

Example:

```python
names = ["Asha", "Riya", "Ananya", "Om"]

result = filter(lambda name: len(name) > 4, names)

print(list(result))
```

Output:

```text
['Ananya']
```

Only names with more than four characters are selected.

---

# ➕ 22. The `reduce()` Function

`reduce()` repeatedly applies a function to the elements of an iterable and produces a single result.

`reduce()` is available through the `functools` module.

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

The process is:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

---

# 🧠 23. Understanding `reduce()`

Consider:

```python
numbers = [2, 3, 4]
```

Using multiplication:

```python
reduce(lambda a, b: a * b, numbers)
```

The process is:

```text
2 × 3 = 6
6 × 4 = 24
```

Final result:

```text
24
```

Remember:

```text
map()
   ↓
Many values → Many transformed values

filter()
   ↓
Many values → Selected values

reduce()
   ↓
Many values → One final value
```

---

# ⚖️ 24. `map()` vs `filter()` vs `reduce()`

| Function   | Purpose               | Result                  |
| ---------- | --------------------- | ----------------------- |
| `map()`    | Transform every item  | Many transformed values |
| `filter()` | Select matching items | Some original values    |
| `reduce()` | Combine items         | One final value         |

Example:

```text
map()
[1, 2, 3] → [2, 4, 6]

filter()
[1, 2, 3, 4] → [2, 4]

reduce()
[1, 2, 3, 4] → 10
```

---

# 🔢 25. The `sorted()` Function as a Higher Order Function

`sorted()` can accept a function through its `key` parameter.

Example:

```python
names = ["banana", "Apple", "cherry"]

result = sorted(names, key=str.lower)

print(result)
```

Output:

```text
['Apple', 'banana', 'cherry']
```

Here:

```text
sorted()
   ↓
receives
   ↓
str.lower
   ↓
uses it to determine sorting order
```

---

# 🔑 26. Understanding the `key` Parameter

The `key` parameter tells Python **how to calculate the value used for comparison**.

Example:

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Riya", 78)
]

result = sorted(students, key=lambda student: student[1])

print(result)
```

Output:

```text
[('Riya', 78), ('Asha', 85), ('Neha', 92)]
```

The key function extracts the marks.

```text
("Asha", 85) → 85
("Neha", 92) → 92
("Riya", 78) → 78
```

---

# 🧩 27. Higher Order Functions with `lambda`

A `lambda` function is often used with higher order functions because it allows you to define a small function directly.

Example:

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x ** 2, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16]
```

Here:

```python
lambda x: x ** 2
```

is passed as an argument to `map()`.

---

# 🔄 28. `map()` with `lambda`

Example:

```python
prices = [100, 200, 300, 400]

updated_prices = map(lambda price: price * 1.10, prices)

print(list(updated_prices))
```

Output:

```text
[110.00000000000001, 220.00000000000003, 330.0, 440.00000000000006]
```

The function is applied to every price.

---

# 🔍 29. `filter()` with `lambda`

Example:

```python
marks = [45, 72, 88, 35, 91, 64]

passed = filter(lambda mark: mark >= 40, marks)

print(list(passed))
```

Output:

```text
[45, 72, 88, 91, 64]
```

The lambda returns:

```text
True  → keep item
False → remove item
```

---

# 🧮 30. `reduce()` with `lambda`

Example:

```python
from functools import reduce

numbers = [5, 10, 15]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

Output:

```text
30
```

The calculation is:

```text
5 + 10 = 15
15 + 15 = 30
```

---

# 🔗 31. Combining `map()` and `filter()`

Higher order functions can be combined.

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

The flow is:

```text
Original
[1, 2, 3, 4, 5, 6]
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

# 🧠 32. Combining `filter()` and `reduce()`

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

The process:

```text
[10, 15, 20, 25, 30]
            ↓
filter()
            ↓
[10, 20, 30]
            ↓
reduce()
            ↓
60
```

---

# 🔢 33. Combining `map()`, `filter()` and `reduce()`

All three can be combined.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared = map(lambda x: x ** 2, even_numbers)

total = reduce(lambda a, b: a + b, squared)

print(total)
```

Output:

```text
56
```

Calculation:

```text
Even numbers:
2, 4, 6

Squares:
4, 16, 36

Total:
4 + 16 + 36 = 56
```

---

# 📚 34. Higher Order Functions with Lists

Example:

```python
numbers = [10, 20, 30, 40]

double = map(lambda x: x * 2, numbers)

print(list(double))
```

Output:

```text
[20, 40, 60, 80]
```

Higher order functions are especially useful for processing collections.

---

# 🗂️ 35. Higher Order Functions with Dictionaries

Example:

```python
marks = {
    "Python": 90,
    "SQL": 75,
    "Git": 85
}

high_marks = filter(lambda item: item[1] >= 80, marks.items())

print(dict(high_marks))
```

Output:

```text
{'Python': 90, 'Git': 85}
```

Here:

```text
items()
   ↓
(key, value)
   ↓
filter()
   ↓
selected items
   ↓
dict()
```

---

# 🔄 36. Transforming Dictionary Values with `map()`

Example:

```python
marks = {
    "Python": 80,
    "SQL": 70,
    "Git": 90
}

updated = map(lambda item: (item[0], item[1] + 5), marks.items())

print(dict(updated))
```

Output:

```text
{'Python': 85, 'SQL': 75, 'Git': 95}
```

Each key-value pair is transformed.

---

# 🧠 37. Callback Functions

A **callback function** is a function passed to another function so that it can be called later.

Example:

```python
def greet(name):
    return "Hello " + name

def process(callback, name):
    return callback(name)

print(process(greet, "Asha"))
```

Output:

```text
Hello Asha
```

Here:

```text
greet
  ↓
callback
  ↓
process()
```

The callback technique is an important application of higher order functions.

---

# ⚙️ 38. Creating a Custom Higher Order Function

You can create your own higher order functions.

Example:

```python
def apply_operation(function, numbers):
    return [function(number) for number in numbers]

def double(number):
    return number * 2

numbers = [1, 2, 3, 4]

result = apply_operation(double, numbers)

print(result)
```

Output:

```text
[2, 4, 6, 8]
```

Here:

```text
apply_operation()
        ↓
accepts a function
        ↓
applies it to data
```

---

# 🧩 39. Returning a Customized Function

Higher order functions can create customized functions.

Example:

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))
print(triple(5))
```

Output:

```text
10
15
```

The function creates different functions based on the supplied value.

---

# 🧠 40. Understanding Closures

A function returned by another function can remember values from its enclosing scope.

Example:

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = create_multiplier(2)

print(double(10))
```

Output:

```text
20
```

Even after `create_multiplier()` finishes, the returned function remembers:

```text
factor = 2
```

This behavior is called a **closure**.

---

# 🔢 41. Creating a Discount Function

A higher order function can create customized discount functions.

Example:

```python
def create_discount(rate):

    def discount(price):
        return price - (price * rate)

    return discount

discount_10 = create_discount(0.10)

print(discount_10(1000))
```

Output:

```text
900.0
```

The same factory can create different discount functions.

---

# 🛒 42. Real-World Example: Shopping Prices

Suppose an online store wants to increase all prices by 10%.

```python
prices = [500, 1000, 1500, 2000]

updated_prices = map(lambda price: price * 1.10, prices)

print(list(updated_prices))
```

Output:

```text
[550.0, 1100.0, 1650.0000000000002, 2200.0]
```

`map()` applies the pricing rule to every product.

---

# 🎓 43. Real-World Example: Student Marks

Suppose a teacher wants to add 5 grace marks.

```python
marks = [65, 72, 81, 59, 90]

updated_marks = map(lambda mark: mark + 5, marks)

print(list(updated_marks))
```

Output:

```text
[70, 77, 86, 64, 95]
```

---

# 🧪 44. Real-World Example: Finding Passed Students

Example:

```python
marks = [35, 78, 45, 29, 88, 62]

passed = filter(lambda mark: mark >= 40, marks)

print(list(passed))
```

Output:

```text
[78, 45, 88, 62]
```

The higher order function selects only students who passed.

---

# 💰 45. Real-World Example: Employee Salaries

Suppose a company wants to increase salaries by 10%.

```python
salaries = [30000, 40000, 50000, 60000]

updated = map(lambda salary: salary * 1.10, salaries)

print(list(updated))
```

Output:

```text
[33000.0, 44000.0, 55000.00000000001, 66000.0]
```

---

# 📊 46. Real-World Example: Filtering Employee Salaries

Suppose a company wants employees earning at least 50000.

```python
salaries = [35000, 45000, 55000, 70000, 48000]

high_salary = filter(lambda salary: salary >= 50000, salaries)

print(list(high_salary))
```

Output:

```text
[55000, 70000]
```

---

# 🏪 47. Real-World Example: Product Filtering

Example:

```python
products = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]

expensive = filter(lambda product: product[1] > 10000, products)

print(list(expensive))
```

Output:

```text
[('Laptop', 55000), ('Monitor', 12000)]
```

---

# 📈 48. Real-World Example: Sorting Students by Marks

Example:

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Riya", 78)
]

result = sorted(students, key=lambda student: student[1], reverse=True)

print(result)
```

Output:

```text
[('Neha', 92), ('Asha', 85), ('Riya', 78)]
```

The `key` function tells `sorted()` to compare students by their marks.

---

# ⚠️ 49. Common Mistake: Calling Instead of Passing a Function

Wrong:

```python
def square(x):
    return x * x

def execute(function, value):
    return function(value)

print(execute(square(5), 10))
```

Here:

```python
square(5)
```

is executed immediately.

Correct:

```python
print(execute(square, 10))
```

Remember:

```text
square
  ↓
Pass the function

square()
  ↓
Call the function
```

---

# ⚠️ 50. Common Mistake: Forgetting `list()` with `map()` and `filter()`

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

The output is a map object similar to:

```text
<map object at ...>
```

To display the results:

```python
print(list(result))
```

Output:

```text
[2, 4, 6]
```

`map()` and `filter()` return iterator objects in Python 3.

---

# ⚠️ 51. Common Mistake: Forgetting to Import `reduce()`

This will not work:

```python
numbers = [1, 2, 3]

result = reduce(lambda a, b: a + b, numbers)
```

You must import `reduce()`:

```python
from functools import reduce
```

Then:

```python
result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
6
```

---

# ⚠️ 52. Common Mistake: Confusing `map()` and `filter()`

Suppose:

```python
numbers = [1, 2, 3, 4]
```

`map()` transforms:

```python
map(lambda x: x * 10, numbers)
```

Result:

```text
[10, 20, 30, 40]
```

`filter()` selects:

```python
filter(lambda x: x > 2, numbers)
```

Result:

```text
[3, 4]
```

Remember:

```text
map()   → Change
filter() → Select
```

---

# ⚠️ 53. Common Mistake: Assuming `map()` Changes the Original List

Example:

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(numbers)
print(list(result))
```

Output:

```text
[1, 2, 3]
[2, 4, 6]
```

`map()` creates an iterator for transformed values.

It does not modify the original list.

---

# 🧠 54. Higher Order Functions and Immutability

Functions such as `map()` and `filter()` are useful when you want to process data without directly changing the original collection.

Example:

```python
numbers = [10, 20, 30]

result = list(map(lambda x: x + 5, numbers))

print("Original:", numbers)
print("New:", result)
```

Output:

```text
Original: [10, 20, 30]
New: [15, 25, 35]
```

This style can make data-processing code easier to reason about.

---

# 📊 55. Higher Order Functions Comparison

| Function   |         Takes Function? | Main Purpose        | Typical Result      |
| ---------- | ----------------------: | ------------------- | ------------------- |
| `map()`    |                       ✅ | Transform items     | Iterator            |
| `filter()` |                       ✅ | Select items        | Iterator            |
| `reduce()` |                       ✅ | Combine items       | Single value        |
| `sorted()` | Optional `key` function | Sort data           | New list            |
| Custom HOF |                       ✅ | Flexible processing | Depends on function |

---

# 🔍 56. First-Class Functions vs Higher Order Functions

These concepts are related but not identical.

### First-Class Functions

Means functions can be treated like values.

```python
def greet():
    return "Hello"

x = greet
```

### Higher Order Function

Means a function accepts another function or returns a function.

```python
def execute(function):
    return function()
```

Remember:

```text
First-class function
        ↓
Python treats functions as objects

Higher order function
        ↓
Function works with other functions
```

---

# 🧠 57. Higher Order Functions Structure

```text
                         FUNCTIONS
                             │
                             ↓
                  FIRST-CLASS OBJECTS
                             │
          ┌──────────────────┼──────────────────┐
          ↓                  ↓                  ↓
       Store              Pass                Return
          │                  │                  │
          ↓                  ↓                  ↓
       Variable          Argument          Function
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ↓
                    HIGHER ORDER FUNCTIONS
                             │
            ┌────────────────┼────────────────┐
            ↓                ↓                ↓
          map()           filter()         reduce()
            │                │                │
            ↓                ↓                ↓
        Transform          Select           Combine
```

---

# 💻 58. Practice Programs

## 🟢 Easy

### Program 1: Pass a Function as an Argument

```python
def square(number):
    return number * number

def execute(function, number):
    return function(number)

print(execute(square, 5))
```

---

### Program 2: Store a Function in a Variable

```python
def greet():
    return "Welcome"

message = greet

print(message())
```

---

### Program 3: Use `map()`

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

---

### Program 4: Use `filter()`

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x >= 20, numbers)

print(list(result))
```

---

# 🟡 Medium

### Program 5: Square Every Number

```python
numbers = [2, 4, 6, 8]

result = map(lambda x: x ** 2, numbers)

print(list(result))
```

---

### Program 6: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

---

### Program 7: Calculate Total Using `reduce()`

```python
from functools import reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

---

### Program 8: Sort Students by Marks

```python
students = [
    ("Asha", 85),
    ("Neha", 92),
    ("Riya", 78)
]

result = sorted(students, key=lambda student: student[1])

print(result)
```

---

# 🔴 Advanced

## Program 9: Filter and Transform Data

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

---

## Program 10: Filter and Reduce

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

---

## Program 11: Create a Function Factory

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))
print(triple(5))
```

---

## Program 12: Custom Higher Order Function

```python
def apply_operation(function, numbers):
    return [function(number) for number in numbers]

def cube(number):
    return number ** 3

numbers = [1, 2, 3, 4]

result = apply_operation(cube, numbers)

print(result)
```

---

# 🏆 59. Challenge

Create a list of student marks:

```text
45
78
92
35
88
64
```

Then:

1. Use `filter()` to select marks greater than or equal to `40`.
2. Use `map()` to add 5 grace marks to the selected marks.
3. Use `filter()` again to find marks greater than or equal to `75`.
4. Use `reduce()` to calculate the total of the final marks.
5. Display the final list.
6. Display the total.
7. Create a function that can apply any operation to the marks.
8. Pass a function as an argument to your custom function.

Try solving the challenge without copying the solution.

---

# 🧪 60. Mini Project: Employee Salary Processor

Create a program containing employee salaries:

```python
salaries = [28000, 35000, 42000, 50000, 65000]
```

Perform the following operations:

* Use `filter()` to find salaries greater than `40000`.
* Use `map()` to increase every salary by 10%.
* Use `reduce()` to calculate the total salary.
* Use `sorted()` to arrange salaries from lowest to highest.
* Create a custom higher order function for salary processing.
* Pass different functions to your custom function.
* Display the results.

### Your Goal

Build a reusable employee salary-processing system using higher order functions.

---

# 🎤 61. Interview Questions

* [ ] What is a higher order function in Python?
* [ ] What does it mean that functions are first-class objects?
* [ ] Can a function be stored in a variable?
* [ ] Can a function be passed as an argument?
* [ ] Can a function return another function?
* [ ] What is the difference between a function reference and a function call?
* [ ] What is `map()`?
* [ ] What does `map()` return?
* [ ] What is `filter()`?
* [ ] What does `filter()` return?
* [ ] What is `reduce()`?
* [ ] Why is `reduce()` imported from `functools`?
* [ ] What is the difference between `map()` and `filter()`?
* [ ] What is the difference between `filter()` and `reduce()`?
* [ ] Can `map()` work with multiple iterables?
* [ ] Why is `lambda` commonly used with higher order functions?
* [ ] What is a callback function?
* [ ] What is a function factory?
* [ ] What is a closure?
* [ ] How does `sorted()` use a function through `key`?
* [ ] Does `map()` modify the original list?
* [ ] Does `filter()` modify the original list?
* [ ] What happens if you pass `square(5)` instead of `square`?
* [ ] How can functions be stored in a dictionary?
* [ ] How can higher order functions improve code reuse?

---

# 📝 62. Assignment

Complete the following programs.

### Task 1

Create a function that accepts another function as an argument.

---

### Task 2

Create a function and store it in a variable.

---

### Task 3

Use `map()` to multiply every number in a list by `5`.

---

### Task 4

Use `filter()` to display only numbers greater than `50`.

---

### Task 5

Use `reduce()` to calculate the sum of five numbers.

---

### Task 6

Use `map()` to convert a list of lowercase names into uppercase names.

---

### Task 7

Use `filter()` to select names containing more than five characters.

---

### Task 8

Use `sorted()` with a `lambda` function to sort students according to their marks.

---

### Task 9

Create a function factory that generates multiplication functions.

---

### Task 10

Use `map()` with two lists to add corresponding elements.

---

### Task 11

Create a real-world program that uses at least three higher order functions.

---

### Task 12

Create a program that uses:

```text
filter()
   ↓
map()
   ↓
reduce()
```

to process a list of numbers.

---

# 🧠 63. Memory Tricks

Remember:

```text
Higher Order Function
        ↓
Function works with another function
```

---

Remember first-class functions:

```text
Function
   ↓
Can Store
Can Pass
Can Return
```

---

Remember `map()`:

```text
map()
  ↓
Transform
  ↓
Every item
```

---

Remember `filter()`:

```text
filter()
    ↓
Select
    ↓
Matching items
```

---

Remember `reduce()`:

```text
reduce()
    ↓
Combine
    ↓
One final result
```

---

Remember:

```text
map()      → Transform
filter()   → Select
reduce()   → Combine
sorted()   → Arrange
```

---

# 📌 64. Important Rules to Remember

```text
1. Functions in Python are first-class objects.

2. Functions can be stored in variables.

3. Functions can be passed as arguments.

4. Functions can be returned from other functions.

5. A function that accepts or returns another function is a higher order function.

6. Passing `function` means passing the function object.

7. Calling `function()` means executing the function.

8. map() applies a function to every item.

9. filter() selects items based on a condition.

10. reduce() combines multiple items into one result.

11. reduce() is available from the functools module.

12. map() and filter() return iterators in Python 3.

13. list() can be used to view the results of map() and filter().

14. lambda functions are commonly used with higher order functions.

15. sorted() can receive a function through its key parameter.

16. Higher order functions help create reusable and flexible programs.

17. Callback functions are an example of passing functions as arguments.

18. Functions returned by other functions can form closures.

19. Higher order functions can be combined.

20. map(), filter(), and reduce() can be used together for data processing.
```

---

# 📊 65. Higher Order Functions Structure

```text
                         PYTHON FUNCTIONS
                                │
                                ↓
                     FIRST-CLASS OBJECTS
                                │
               ┌────────────────┼────────────────┐
               ↓                ↓                ↓
             STORE             PASS             RETURN
               │                │                │
               ↓                ↓                ↓
            Variable         Argument         Function
                                │
                                ↓
                     HIGHER ORDER FUNCTIONS
                                │
        ┌───────────────────────┼───────────────────────┐
        ↓                       ↓                       ↓
      map()                  filter()                reduce()
        │                       │                       │
        ↓                       ↓                       ↓
    Transform                 Select                  Combine
        │                       │                       │
        ↓                       ↓                       ↓
   Many results            Some results             One result
```

---

# 📚 66. Complete Higher Order Functions Cheat Sheet

### Pass a Function

```python
def execute(function, value):
    return function(value)
```

---

### Store a Function

```python
operation = add
```

---

### Return a Function

```python
def create_function():
    def greet():
        return "Hello"

    return greet
```

---

### Transform Data

```python
result = map(function, data)
```

---

### Filter Data

```python
result = filter(function, data)
```

---

### Combine Data

```python
from functools import reduce

result = reduce(function, data)
```

---

### Sort Using a Function

```python
result = sorted(data, key=function)
```

---

### Use `lambda`

```python
result = map(lambda x: x * 2, numbers)
```

---

### Convert Iterator to List

```python
result = list(map(lambda x: x * 2, numbers))
```

---

# 🏆 67. Higher Order Functions Mastery

```text
                         FUNCTIONS
                             │
                             ↓
                   FIRST-CLASS OBJECTS
                             │
       ┌─────────────────────┼─────────────────────┐
       ↓                     ↓                     ↓
     STORE                  PASS                  RETURN
       │                     │                     │
       ↓                     ↓                     ↓
   Variables             Arguments             Functions
                             │
                             ↓
                  HIGHER ORDER FUNCTIONS
                             │
       ┌─────────────────────┼─────────────────────┐
       ↓                     ↓                     ↓
     map()                filter()              reduce()
       │                     │                     │
       ↓                     ↓                     ↓
   Transform               Select               Combine
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             ↓
                    FUNCTIONAL PROGRAMMING
                             │
                 ┌───────────┼───────────┐
                 ↓           ↓           ↓
              lambda      callback     closure
```

---

# 📚 68. Summary

In this lesson, you learned:

* What higher order functions are.
* What first-class functions are.
* How functions can be stored in variables.
* How functions can be stored in lists and dictionaries.
* How to pass functions as arguments.
* How to return functions from other functions.
* The difference between a function reference and function call.
* How to use `map()`.
* How to use `filter()`.
* How to use `reduce()`.
* The difference between `map()`, `filter()`, and `reduce()`.
* How to use `lambda` with higher order functions.
* How to use `sorted()` with a function.
* How to use the `key` parameter.
* How to create callback functions.
* How to create custom higher order functions.
* How to create function factories.
* How closures are related to returned functions.
* How to combine `map()`, `filter()`, and `reduce()`.
* How to process lists using higher order functions.
* How to process dictionaries using higher order functions.
* How higher order functions are used in real-world applications.
* Common mistakes when using higher order functions.
* How higher order functions improve code reuse and flexibility.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what higher order functions are.
* [ ] I understand first-class functions.
* [ ] I can store a function in a variable.
* [ ] I can pass a function as an argument.
* [ ] I can return a function from another function.
* [ ] I understand the difference between a function reference and function call.
* [ ] I can use `map()`.
* [ ] I can use `filter()`.
* [ ] I can use `reduce()`.
* [ ] I understand the difference between `map()`, `filter()`, and `reduce()`.
* [ ] I can use `lambda` with higher order functions.
* [ ] I can use `sorted()` with `key`.
* [ ] I understand callback functions.
* [ ] I understand function factories.
* [ ] I understand the basic idea of closures.
* [ ] I can combine higher order functions.
* [ ] I can use higher order functions with lists.
* [ ] I can use higher order functions with dictionaries.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use higher order functions without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Functional Programming with Functions**

In the next topic, you will learn:

* What functional programming means.
* Pure functions.
* Impure functions.
* Side effects.
* Function composition.
* Reusable function pipelines.
* Immutability concepts.
* `map()`, `filter()`, and `reduce()` in functional programming.
* Lambda functions in functional programming.
* Higher order functions in functional programming.
* Closures.
* Nested functions.
* Function decorators.
* Practical functional programming examples.
* Real-world data-processing techniques.
* Common mistakes.
* Advanced functional programming techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Higher order functions make functions work together, turning simple operations into powerful and reusable solutions."** 🐍⚙️📚
