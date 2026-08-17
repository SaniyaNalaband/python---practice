# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 8: `*args`

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what `*args` means in Python.
* [ ] Understand why `*args` is used.
* [ ] Understand variable-length arguments.
* [ ] Create functions that accept any number of positional arguments.
* [ ] Understand how Python packs arguments into a tuple.
* [ ] Access `*args` values using loops.
* [ ] Use `*args` with conditions.
* [ ] Use `*args` with mathematical operations.
* [ ] Understand the difference between normal parameters and `*args`.
* [ ] Understand positional arguments with `*args`.
* [ ] Combine normal parameters with `*args`.
* [ ] Understand the rules for placing `*args`.
* [ ] Use `*args` in real-world applications.
* [ ] Understand common mistakes when using `*args`.
* [ ] Use `*args` in advanced function designs.

---

# 📖 1. What is `*args`?

`*args` is used in a Python function when you want the function to accept a **variable number of positional arguments**.

Normally, a function expects a fixed number of arguments.

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

This function accepts exactly two arguments.

But what if we want to pass:

```python
add(10, 20, 30)
```

or:

```python
add(10, 20, 30, 40, 50)
```

A normal function with only `a` and `b` cannot handle this.

This is where `*args` becomes useful.

---

# 🧠 2. Meaning of `*args`

The word `args` means **arguments**.

The `*` tells Python:

> "Collect all extra positional arguments into a tuple."

Example:

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)
```

Output:

```text
(10, 20, 30, 40)
```

Here:

```text
*args
  ↓
Collects positional arguments
  ↓
Stores them inside a tuple
```

So internally:

```text
args = (10, 20, 30, 40)
```

---

# 🔍 3. Why Do We Need `*args`?

Without `*args`, you may need to create different functions for different numbers of arguments.

For example:

```python
def add_two(a, b):
    return a + b
```

For three numbers:

```python
def add_three(a, b, c):
    return a + b + c
```

For four numbers:

```python
def add_four(a, b, c, d):
    return a + b + c + d
```

This becomes inconvenient.

With `*args`:

```python
def add_numbers(*args):
    return sum(args)
```

Now you can write:

```python
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40))
print(add_numbers(10, 20, 30, 40, 50))
```

Output:

```text
30
60
100
150
```

One function can handle different numbers of arguments.

---

# 📚 4. Basic Syntax of `*args`

The general syntax is:

```python
def function_name(*args):
    # function body
```

Example:

```python
def show_numbers(*args):
    print(args)

show_numbers(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

---

# 🧠 5. `args` is a Tuple

An important concept is:

> `*args` collects positional arguments into a tuple.

Example:

```python
def show_data(*args):
    print(type(args))
    print(args)

show_data("Python", "SQL", "Git")
```

Output:

```text
<class 'tuple'>
('Python', 'SQL', 'Git')
```

Therefore:

```text
*args
   ↓
Tuple
   ↓
Contains positional arguments
```

---

# 🔢 6. Passing Different Numbers of Arguments

One of the biggest advantages of `*args` is that you can pass different numbers of arguments.

Example:

```python
def display(*args):
    print(args)

display()
display(10)
display(10, 20)
display(10, 20, 30)
```

Output:

```text
()
(10,)
(10, 20)
(10, 20, 30)
```

Notice:

```python
display()
```

creates:

```text
()
```

This is an empty tuple.

---

# 🧩 7. `*args` with One Argument

```python
def display(*args):
    print(args)

display("Python")
```

Output:

```text
('Python',)
```

The comma is important because:

```text
('Python',)
```

is a tuple containing one element.

---

# 🔁 8. Looping Through `*args`

Because `args` is a tuple, you can use a loop.

Example:

```python
def display(*args):
    for value in args:
        print(value)

display(10, 20, 30, 40)
```

Output:

```text
10
20
30
40
```

This is useful when you want to process every argument individually.

---

# ➕ 9. Adding Numbers Using `*args`

Example:

```python
def calculate_total(*args):
    total = 0

    for number in args:
        total += number

    return total

print(calculate_total(10, 20, 30))
```

Output:

```text
60
```

The function can accept any number of numbers.

---

# 🧮 10. Using `sum()` with `*args`

Because `args` is a tuple, built-in functions can work with it.

Example:

```python
def calculate_total(*args):
    return sum(args)

print(calculate_total(10, 20, 30, 40))
```

Output:

```text
100
```

---

# 🔍 11. Finding the Maximum Value

You can use `max()` with `*args`.

Example:

```python
def highest_number(*args):
    return max(args)

print(highest_number(45, 72, 18, 91, 63))
```

Output:

```text
91
```

---

# 📉 12. Finding the Minimum Value

You can use `min()`.

```python
def lowest_number(*args):
    return min(args)

print(lowest_number(45, 72, 18, 91, 63))
```

Output:

```text
18
```

---

# 📊 13. Finding the Average Using `*args`

Example:

```python
def average(*args):
    return sum(args) / len(args)

print(average(80, 90, 70, 60))
```

Output:

```text
75.0
```

Here:

```text
sum(args)
   ↓
300

len(args)
   ↓
4

300 / 4
   ↓
75.0
```

---

# 🧠 14. Accessing Individual Values

Since `args` is a tuple, you can use indexing.

Example:

```python
def display(*args):
    print(args[0])
    print(args[1])
    print(args[2])

display("Python", "SQL", "Git")
```

Output:

```text
Python
SQL
Git
```

Remember:

```text
args[0] → first argument
args[1] → second argument
args[2] → third argument
```

---

# ✂️ 15. Slicing `*args`

Because `args` is a tuple, slicing is possible.

Example:

```python
def display(*args):
    print(args[1:])

display("Python", "SQL", "Git", "HTML")
```

Output:

```text
('SQL', 'Git', 'HTML')
```

---

# ⚖️ 16. Normal Parameter vs `*args`

Consider:

```python
def display(a, b):
    print(a, b)
```

This function expects exactly two arguments.

But:

```python
def display(*args):
    print(args)
```

can accept any number of positional arguments.

Comparison:

| Function               | Number of positional arguments |
| ---------------------- | -----------------------------: |
| `def display(a, b)`    |                      Exactly 2 |
| `def display(*args)`   |                      0 or more |
| `def display(a, b, c)` |                      Exactly 3 |
| `def display(*args)`   |                       Variable |

---

# 🔗 17. Combining Normal Parameters with `*args`

You can have normal parameters before `*args`.

Example:

```python
def student_info(name, *subjects):
    print("Name:", name)
    print("Subjects:", subjects)

student_info("Asha", "Python", "SQL", "Git")
```

Output:

```text
Name: Asha
Subjects: ('Python', 'SQL', 'Git')
```

Here:

```text
name
 ↓
"Asha"

*subjects
 ↓
("Python", "SQL", "Git")
```

---

# 🧠 18. How Python Packs Arguments

Consider:

```python
def student_info(name, *subjects):
    print(name)
    print(subjects)

student_info(
    "Asha",
    "Python",
    "SQL",
    "Git"
)
```

Python interprets the arguments approximately like this:

```text
name
 ↓
"Asha"

subjects
 ↓
("Python", "SQL", "Git")
```

The extra positional arguments are packed into the tuple.

---

# 🔄 19. Looping Through Combined Parameters

Example:

```python
def student_info(name, *subjects):
    print("Student:", name)

    for subject in subjects:
        print("Subject:", subject)

student_info(
    "Asha",
    "Python",
    "SQL",
    "Git"
)
```

Output:

```text
Student: Asha
Subject: Python
Subject: SQL
Subject: Git
```

---

# 🧮 20. Calculating Student Marks Using `*args`

Example:

```python
def total_marks(name, *marks):
    total = sum(marks)

    print("Student:", name)
    print("Total:", total)

total_marks("Asha", 90, 85, 88, 92)
```

Output:

```text
Student: Asha
Total: 355
```

---

# 🎯 21. Using Conditions with `*args`

You can combine `*args` with `if`.

Example:

```python
def show_pass_marks(*marks):
    for mark in marks:
        if mark >= 40:
            print(mark)

show_pass_marks(35, 72, 48, 28, 91)
```

Output:

```text
72
48
91
```

---

# 🚦 22. Checking Whether Any Argument Meets a Condition

Example:

```python
def check_scores(*scores):
    for score in scores:
        if score >= 90:
            print("Excellent:", score)

check_scores(72, 91, 65, 95, 84)
```

Output:

```text
Excellent: 91
Excellent: 95
```

---

# 🔢 23. Counting Arguments

You can use `len()`.

Example:

```python
def count_values(*args):
    print("Number of arguments:", len(args))

count_values(10, 20, 30, 40, 50)
```

Output:

```text
Number of arguments: 5
```

---

# 🧠 24. Checking Whether `*args` is Empty

Example:

```python
def process(*args):
    if len(args) == 0:
        print("No arguments provided")
    else:
        print("Arguments received:", args)

process()
process(10, 20)
```

Output:

```text
No arguments provided
Arguments received: (10, 20)
```

---

# 📦 25. Passing a List Using `*`

There is another important use of `*`.

Suppose you have:

```python
numbers = [10, 20, 30, 40]
```

You can unpack the list when calling a function:

```python
def display(*args):
    print(args)

display(*numbers)
```

Output:

```text
(10, 20, 30, 40)
```

Here:

```text
*numbers
   ↓
Unpacks the list
   ↓
10, 20, 30, 40
   ↓
Collected by *args
   ↓
(10, 20, 30, 40)
```

---

# 🔄 26. Packing vs Unpacking

This is an important concept.

### Packing

```python
def display(*args):
    print(args)
```

When calling:

```python
display(10, 20, 30)
```

Python packs:

```text
10, 20, 30
      ↓
(10, 20, 30)
```

### Unpacking

Suppose:

```python
numbers = (10, 20, 30)
```

Then:

```python
display(*numbers)
```

unpacks:

```text
(10, 20, 30)
      ↓
10, 20, 30
```

So:

```text
*args → Packing inside function definition

*data → Unpacking during function call
```

---

# 🧩 27. `*args` with Strings

`*args` can accept strings as well.

Example:

```python
def show_languages(*languages):
    for language in languages:
        print(language)

show_languages("Python", "Java", "C++", "JavaScript")
```

Output:

```text
Python
Java
C++
JavaScript
```

---

# 🛒 28. Real-World Example: Shopping Cart

A shopping cart can contain different numbers of products.

Example:

```python
def calculate_cart_total(*prices):
    total = sum(prices)

    print("Cart Total:", total)

calculate_cart_total(55000, 800, 1500)
```

Output:

```text
Cart Total: 57300
```

The function can also handle:

```python
calculate_cart_total(55000, 800)
```

or:

```python
calculate_cart_total(55000, 800, 1500, 2500, 700)
```

---

# 🌍 29. Real-World Example: Student Subjects

A student may study different numbers of subjects.

Example:

```python
def student_subjects(name, *subjects):
    print("Student:", name)

    for subject in subjects:
        print(subject)

student_subjects(
    "Asha",
    "Python",
    "SQL",
    "HTML",
    "CSS"
)
```

Output:

```text
Student: Asha
Python
SQL
HTML
CSS
```

---

# 🌍 30. Real-World Example: Employee Skills

Employees may have different numbers of skills.

Example:

```python
def employee_skills(name, *skills):
    print("Employee:", name)

    for skill in skills:
        print("Skill:", skill)

employee_skills(
    "Neha",
    "Python",
    "SQL",
    "Git",
    "Django"
)
```

Output:

```text
Employee: Neha
Skill: Python
Skill: SQL
Skill: Git
Skill: Django
```

---

# 🌍 31. Real-World Example: Expense Tracker

An expense tracker can receive any number of expenses.

Example:

```python
def total_expenses(*expenses):
    total = sum(expenses)

    print("Total Expenses:", total)

total_expenses(500, 1200, 350, 800)
```

Output:

```text
Total Expenses: 2850
```

---

# 🌍 32. Real-World Example: Exam Marks

Example:

```python
def analyze_marks(student, *marks):
    print("Student:", student)
    print("Total:", sum(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))

analyze_marks("Asha", 90, 85, 78, 92)
```

Output:

```text
Student: Asha
Total: 345
Highest: 92
Lowest: 78
```

---

# ⚠️ 33. Common Mistake: Forgetting the `*`

Wrong:

```python
def numbers(args):
    print(args)

numbers(10, 20, 30)
```

This produces an error because the function expects only one argument.

Correct:

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

---

# ⚠️ 34. Common Mistake: Treating `args` as a Single Value

Consider:

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30)
```

`args` is:

```text
(10, 20, 30)
```

It is not:

```text
10
```

Therefore, if you want individual values, use a loop:

```python
def numbers(*args):
    for number in args:
        print(number)
```

---

# ⚠️ 35. Common Mistake: Using an Index That Does Not Exist

Example:

```python
def display(*args):
    print(args[5])

display(10, 20)
```

There is no index `5`.

This produces:

```text
IndexError
```

Remember:

```text
(10, 20)

index 0 → 10
index 1 → 20
```

---

# ⚠️ 36. Common Mistake: Expecting `*args` to Create a List

Example:

```python
def display(*args):
    print(type(args))

display(10, 20, 30)
```

Output:

```text
<class 'tuple'>
```

`*args` creates a tuple, not a list.

---

# ⚖️ 37. `*args` vs List Parameter

Consider:

```python
def display(numbers):
    print(numbers)
```

You must pass one object:

```python
display([10, 20, 30])
```

With `*args`:

```python
def display(*numbers):
    print(numbers)
```

You can write:

```python
display(10, 20, 30)
```

Comparison:

| Feature                               | Normal Parameter | `*args` |
| ------------------------------------- | ---------------- | ------- |
| Accepts multiple positional arguments | ❌                | ✅       |
| Stores arguments in tuple             | ❌                | ✅       |
| Variable number of arguments          | ❌                | ✅       |
| Requires list/tuple at call           | Usually          | ❌       |

---

# 🧠 38. `*args` and Function Flexibility

Without `*args`:

```python
def calculate(a, b, c):
    return a + b + c
```

Only three arguments are expected.

With `*args`:

```python
def calculate(*numbers):
    return sum(numbers)
```

The function becomes flexible.

It can accept:

```python
calculate(10)
calculate(10, 20)
calculate(10, 20, 30)
calculate(10, 20, 30, 40)
```

---

# 🔗 39. `*args` with a Required Parameter

You can place normal parameters before `*args`.

Example:

```python
def order(customer, *items):
    print("Customer:", customer)

    for item in items:
        print("Item:", item)

order(
    "Asha",
    "Laptop",
    "Mouse",
    "Keyboard"
)
```

Output:

```text
Customer: Asha
Item: Laptop
Item: Mouse
Item: Keyboard
```

---

# 🧠 40. Important Rule About Parameter Order

A normal parameter can come before `*args`.

Example:

```python
def function(a, *args):
    pass
```

This is valid.

Example:

```python
def function(name, age, *args):
    pass
```

This is also valid.

But `*args` collects the remaining positional arguments.

For:

```python
function("Asha", 20, "Python", "SQL")
```

the values become:

```text
name → "Asha"
age → 20
args → ("Python", "SQL")
```

---

# ⚙️ 41. Keyword Arguments After `*args`

When `*args` is used, parameters after it are keyword-only.

Example:

```python
def student(name, *subjects, city):
    print(name)
    print(subjects)
    print(city)
```

You must provide `city` using its keyword:

```python
student(
    "Asha",
    "Python",
    "SQL",
    city="Bengaluru"
)
```

Output:

```text
Asha
('Python', 'SQL')
Bengaluru
```

---

# 🧠 42. Why Keyword-Only Parameters Are Useful

They make the function call clearer.

Example:

```python
def employee(name, *skills, department):
    print(name)
    print(skills)
    print(department)
```

Calling:

```python
employee(
    "Neha",
    "Python",
    "SQL",
    "Git",
    department="Development"
)
```

Here:

```text
name
 ↓
"Neha"

skills
 ↓
("Python", "SQL", "Git")

department
 ↓
"Development"
```

---

# 🔢 43. Using `*args` with Mathematical Operations

Example:

```python
def multiply(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result

print(multiply(2, 3, 4))
```

Output:

```text
24
```

Calculation:

```text
1 × 2 × 3 × 4
      ↓
24
```

---

# 📊 44. Separating Even and Odd Numbers

Example:

```python
def separate_numbers(*numbers):
    for number in numbers:
        if number % 2 == 0:
            print("Even:", number)
        else:
            print("Odd:", number)

separate_numbers(10, 15, 22, 31, 40)
```

Output:

```text
Even: 10
Odd: 15
Even: 22
Odd: 31
Even: 40
```

---

# 🔍 45. Searching for a Specific Value

Example:

```python
def search_value(target, *numbers):
    if target in numbers:
        print(target, "found")
    else:
        print(target, "not found")

search_value(30, 10, 20, 30, 40)
```

Output:

```text
30 found
```

---

# 📈 46. Counting Values Greater Than a Number

Example:

```python
def count_greater(limit, *numbers):
    count = 0

    for number in numbers:
        if number > limit:
            count += 1

    print("Count:", count)

count_greater(50, 20, 70, 45, 90, 65)
```

Output:

```text
Count: 3
```

---

# 🧩 47. Combining `*args` with `return`

Example:

```python
def calculate_total(*numbers):
    return sum(numbers)

result = calculate_total(10, 20, 30, 40)

print("Total:", result)
```

Output:

```text
Total: 100
```

The function does not have to print the result directly.

It can return it.

---

# 🔄 48. Passing a Tuple to a `*args` Function

Suppose:

```python
numbers = (10, 20, 30, 40)
```

You can unpack it:

```python
def calculate(*args):
    print(args)

calculate(*numbers)
```

Output:

```text
(10, 20, 30, 40)
```

---

# 🔄 49. Passing a List to a `*args` Function

Example:

```python
numbers = [10, 20, 30, 40]

def calculate(*args):
    print(args)

calculate(*numbers)
```

Output:

```text
(10, 20, 30, 40)
```

The list is unpacked into individual positional arguments.

---

# 🧠 50. `*args` with Multiple Data Types

`*args` is not limited to numbers.

Example:

```python
def display(*args):
    for value in args:
        print(value)

display(
    "Python",
    90,
    3.14,
    True
)
```

Output:

```text
Python
90
3.14
True
```

The arguments can have different data types.

---

# 📊 51. Dictionary Data with `*args`

You can even pass dictionaries as individual arguments.

Example:

```python
def display(*records):
    for record in records:
        print(record)

display(
    {"name": "Asha"},
    {"name": "Neha"}
)
```

Output:

```text
{'name': 'Asha'}
{'name': 'Neha'}
```

---

# 🌍 52. Real-World Example: Multiple Products

Example:

```python
def show_products(*products):
    print("Products:")

    for product in products:
        print("-", product)

show_products(
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
)
```

Output:

```text
Products:
- Laptop
- Mouse
- Keyboard
- Monitor
```

---

# 🌍 53. Real-World Example: Course Enrollment

Example:

```python
def enroll_student(name, *courses):
    print("Student:", name)

    for course in courses:
        print("Enrolled:", course)

enroll_student(
    "Asha",
    "Python",
    "SQL",
    "Web Development"
)
```

Output:

```text
Student: Asha
Enrolled: Python
Enrolled: SQL
Enrolled: Web Development
```

---

# 🌍 54. Real-World Example: Monthly Expenses

Example:

```python
def monthly_expenses(*expenses):
    total = sum(expenses)

    print("Total Expenses:", total)
    print("Average Expense:", total / len(expenses))

monthly_expenses(
    1200,
    800,
    1500,
    700
)
```

Output:

```text
Total Expenses: 4200
Average Expense: 1050.0
```

---

# 🌍 55. Real-World Example: Employee Performance

Example:

```python
def performance(employee, *scores):
    average = sum(scores) / len(scores)

    print("Employee:", employee)
    print("Average Score:", average)

performance(
    "Neha",
    85,
    90,
    78,
    92
)
```

Output:

```text
Employee: Neha
Average Score: 86.25
```

---

# ⚠️ 56. Common Mistake: Calling with the Wrong Required Argument

Consider:

```python
def student(name, *subjects):
    print(name)
    print(subjects)
```

Calling:

```python
student()
```

produces:

```text
TypeError
```

Why?

Because `name` is a required parameter.

`*subjects` can accept zero or more arguments, but `name` cannot be omitted.

---

# ⚠️ 57. Common Mistake: Assuming `*args` Accepts Keyword Arguments

Consider:

```python
def display(*args):
    print(args)
```

Calling:

```python
display(name="Asha")
```

does not place `"Asha"` inside `args`.

Keyword arguments are handled separately.

For keyword arguments, Python provides `**kwargs`, which will be covered separately.

Remember:

```text
*args
 ↓
Positional arguments

**kwargs
 ↓
Keyword arguments
```

---

# ⚖️ 58. `*args` vs `**kwargs`

| Feature        | `*args`              | `**kwargs`        |
| -------------- | -------------------- | ----------------- |
| Handles        | Positional arguments | Keyword arguments |
| Stores data as | Tuple                | Dictionary        |
| Example        | `10, 20, 30`         | `name="Asha"`     |
| Symbol         | `*`                  | `**`              |

Example:

```python
def display(*args):
    print(args)
```

and:

```python
def display(**kwargs):
    print(kwargs)
```

`*args` → tuple

`**kwargs` → dictionary

---

# 📊 59. `*args` and `**kwargs` Together

Both can be used in the same function.

Example:

```python
def student_info(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

student_info(
    "Python",
    "SQL",
    name="Asha",
    age=20
)
```

Output:

```text
Positional: ('Python', 'SQL')
Keyword: {'name': 'Asha', 'age': 20}
```

Here:

```text
*args
 ↓
('Python', 'SQL')

**kwargs
 ↓
{'name': 'Asha', 'age': 20}
```

---

# 🧠 60. Understanding the Complete Flow

Consider:

```python
def employee(name, *skills):
    print(name)
    print(skills)

employee(
    "Neha",
    "Python",
    "SQL",
    "Git"
)
```

Step 1:

```text
"Neha"
```

goes into:

```text
name
```

Step 2:

The remaining positional arguments:

```text
"Python"
"SQL"
"Git"
```

are collected into:

```text
skills = ("Python", "SQL", "Git")
```

Step 3:

The function processes the tuple.

---

# 🧪 61. Practice Programs

## 🟢 Easy

### Program 1: Display All Arguments

```python
def display(*args):
    print(args)

display(10, 20, 30)
```

---

### Program 2: Print Arguments One by One

```python
def display(*args):
    for value in args:
        print(value)

display("Python", "SQL", "Git")
```

---

### Program 3: Count Arguments

```python
def count_values(*args):
    print("Count:", len(args))

count_values(10, 20, 30, 40)
```

---

### Program 4: Calculate Total

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)
```

---

# 🟡 Medium

### Program 5: Find Maximum

```python
def highest(*numbers):
    print(max(numbers))

highest(25, 90, 45, 72, 61)
```

---

### Program 6: Find Minimum

```python
def lowest(*numbers):
    print(min(numbers))

lowest(25, 90, 45, 72, 61)
```

---

### Program 7: Calculate Average

```python
def average(*numbers):
    print(sum(numbers) / len(numbers))

average(80, 90, 70, 60)
```

---

### Program 8: Display Only Even Numbers

```python
def even_numbers(*numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

even_numbers(10, 15, 20, 31, 40)
```

---

# 🔴 Advanced

## Program 9: Student Marks Analyzer

```python
def analyze_marks(name, *marks):
    print("Student:", name)
    print("Total:", sum(marks))
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    print("Average:", sum(marks) / len(marks))

analyze_marks(
    "Asha",
    90,
    85,
    78,
    92
)
```

---

## Program 10: Filter High Scores

```python
def high_scores(*scores):
    for score in scores:
        if score >= 80:
            print(score)

high_scores(72, 91, 65, 88, 95)
```

---

## Program 11: Shopping Cart Calculator

```python
def cart_total(*prices):
    total = sum(prices)

    print("Total:", total)

cart_total(
    55000,
    800,
    1500,
    2500
)
```

---

## Program 12: Employee Performance Analyzer

```python
def employee_performance(name, *scores):
    average = sum(scores) / len(scores)

    print("Employee:", name)
    print("Average:", average)

    if average >= 80:
        print("Performance: Excellent")
    elif average >= 60:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

employee_performance(
    "Neha",
    85,
    78,
    92,
    88
)
```

---

# 🏆 62. Challenge

Create a function that accepts a student's name and any number of subject marks using `*args`.

Example:

```python
student_marks(
    "Asha",
    90,
    85,
    88,
    76,
    92
)
```

The function should:

1. Display the student name.
2. Display all marks.
3. Count the number of subjects.
4. Calculate total marks.
5. Calculate average marks.
6. Display the highest mark.
7. Display the lowest mark.
8. Display marks greater than or equal to `80`.
9. Display `"Excellent"` if the average is `80` or above.
10. Display `"Good"` if the average is between `60` and `79`.
11. Display `"Needs Improvement"` if the average is below `60`.

Try solving the challenge without copying the solution.

---

# 🧪 63. Mini Project: Flexible Expense Calculator

Create a function called:

```python
calculate_expenses()
```

The function should accept:

```text
Any number of expenses
```

using `*args`.

Example:

```python
calculate_expenses(
    1200,
    800,
    1500,
    700,
    950
)
```

Perform the following operations:

* Display all expenses.
* Count the number of expenses.
* Calculate the total expense.
* Calculate the average expense.
* Display the highest expense.
* Display the lowest expense.
* Display expenses greater than `1000`.
* Display `"High Spending"` if the total is greater than `4000`.
* Otherwise display `"Spending is under control"`.

### Your Goal

Build the complete expense calculator using `*args`.

---

# 🎤 64. Interview Questions

* [ ] What is `*args` in Python?
* [ ] Why is `*args` used?
* [ ] What does the `*` symbol mean in a function parameter?
* [ ] What type of object is `args`?
* [ ] Can `*args` accept zero arguments?
* [ ] Can `*args` accept one argument?
* [ ] Can `*args` accept unlimited positional arguments?
* [ ] What is variable-length argument handling?
* [ ] What is the difference between a normal parameter and `*args`?
* [ ] How does Python pack arguments into `*args`?
* [ ] Can you use a loop with `*args`?
* [ ] Can you use `len()` with `args`?
* [ ] Can you use `sum()` with `args`?
* [ ] Can you use `max()` and `min()` with `args`?
* [ ] What is the type of `args`?
* [ ] What is the difference between packing and unpacking?
* [ ] How can you pass a list to a `*args` function?
* [ ] How can you pass a tuple to a `*args` function?
* [ ] Can normal parameters be used before `*args`?
* [ ] What are keyword-only parameters?
* [ ] What is the difference between `*args` and `**kwargs`?
* [ ] Can `*args` and `**kwargs` be used together?
* [ ] What happens if a required parameter is missing?
* [ ] Does `*args` collect keyword arguments?
* [ ] What happens when no arguments are passed to `*args`?

---

# 📝 65. Assignment

Complete the following programs.

### Task 1

Create a function using `*args` that displays all numbers passed to it.

---

### Task 2

Create a function using `*args` that calculates the total of all numbers.

---

### Task 3

Create a function using `*args` that calculates the average of all numbers.

---

### Task 4

Create a function using `*args` that displays the largest number.

---

### Task 5

Create a function using `*args` that displays the smallest number.

---

### Task 6

Create a function using `*args` that displays only even numbers.

---

### Task 7

Create a function using `*args` that displays only numbers greater than `50`.

---

### Task 8

Create a function with a normal parameter and `*args`.

Example structure:

```python
def student(name, *subjects):
    pass
```

Display the student name and all subjects.

---

### Task 9

Create a function that accepts an employee name and any number of skills.

Example:

```text
Employee: Neha
Skills:
Python
SQL
Git
Django
```

Use `*args`.

---

### Task 10

Create a function that accepts a list of numbers using unpacking.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

Pass the list to a function using `*`.

---

### Task 11

Create a real-world function using `*args` and at least five different operations.

---

### Task 12

Create a program that uses `*args` and `if-elif-else` to classify the average score as:

```text
80+     → Excellent
60–79   → Good
Below 60 → Needs Improvement
```

---

# 🧠 66. Memory Tricks

Remember:

```text
*args
   ↓
Any number of positional arguments
   ↓
Packed into a tuple
```

---

Remember:

```text
Normal parameter
      ↓
Fixed / expected argument

*args
      ↓
Variable number of positional arguments
```

---

Remember:

```text
*args
   ↓
Tuple
```

---

Remember:

```text
*data
   ↓
Unpack data
```

---

Remember:

```text
*args      → Positional arguments
**kwargs   → Keyword arguments
```

---

# 📌 67. Important Rules to Remember

```text
1. *args allows a function to accept a variable number of positional arguments.

2. args is a conventional name; technically, any valid name can be used.

3. The * symbol is what creates the variable-length positional parameter.

4. Python collects extra positional arguments into a tuple.

5. *args can accept zero or more positional arguments.

6. args is a tuple.

7. You can use loops with args.

8. You can use len(), sum(), max(), and min() with args when appropriate.

9. Normal parameters can appear before *args.

10. Arguments collected by *args are positional arguments.

11. *args does not collect keyword arguments.

12. **kwargs is used for variable-length keyword arguments.

13. A list or tuple can be unpacked using * during a function call.

14. Packing happens inside the function parameter.

15. Unpacking happens when * is used during a function call.

16. *args makes functions more flexible.

17. *args can be combined with normal parameters.

18. Parameters after *args become keyword-only parameters.

19. *args is commonly used when the number of positional arguments is unknown.

20. The name args is not mandatory; *values or *numbers are also valid.
```

---

# 📊 68. `*args` Structure

```text
                         FUNCTION
                            │
                            ↓
                       *args PARAMETER
                            │
                            ↓
              Variable Number of Arguments
                            │
                            ↓
                         PACKING
                            │
                            ↓
                         TUPLE
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
          args[0]        args[1]        args[2]
             │              │              │
             ↓              ↓              ↓
          Value 1        Value 2        Value 3
```

---

# 📚 69. Complete `*args` Cheat Sheet

### Define a Function with `*args`

```python
def display(*args):
    print(args)
```

### Pass Multiple Arguments

```python
display(10, 20, 30)
```

### Loop Through Arguments

```python
for value in args:
    print(value)
```

### Count Arguments

```python
len(args)
```

### Calculate Total

```python
sum(args)
```

### Find Maximum

```python
max(args)
```

### Find Minimum

```python
min(args)
```

### Access First Argument

```python
args[0]
```

### Slice Arguments

```python
args[1:]
```

### Combine with Normal Parameter

```python
def student(name, *subjects):
    pass
```

### Unpack a List

```python
numbers = [10, 20, 30]

display(*numbers)
```

### Unpack a Tuple

```python
numbers = (10, 20, 30)

display(*numbers)
```

### Combine `*args` and `**kwargs`

```python
def function(*args, **kwargs):
    pass
```

---

# 🏆 70. `*args` Mastery

```text
                         *args
                           │
                           ↓
                Variable-Length Arguments
                           │
                           ↓
                    Positional Arguments
                           │
                           ↓
                         Packing
                           │
                           ↓
                         Tuple
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       Looping          Conditions       Functions
          │                │                │
          ↓                ↓                ↓
      Process           Filter          Calculate
      Values            Values           Results
```

---

# 📚 71. Summary

In this lesson, you learned:

* What `*args` is.
* Why `*args` is used.
* What variable-length arguments mean.
* How to create functions using `*args`.
* How Python collects arguments into a tuple.
* Why `args` is a tuple.
* How to loop through `args`.
* How to use indexing with `args`.
* How to use slicing with `args`.
* How to calculate totals using `*args`.
* How to calculate averages using `*args`.
* How to find minimum and maximum values.
* How to use conditions with `*args`.
* How to combine normal parameters with `*args`.
* How to use `*args` with real-world applications.
* The difference between packing and unpacking.
* How to unpack lists and tuples using `*`.
* The difference between `*args` and `**kwargs`.
* How `*args` and `**kwargs` can work together.
* How keyword-only parameters work after `*args`.
* Common mistakes when using `*args`.
* How to use `*args` in flexible function designs.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `*args` means.
* [ ] I understand why `*args` is used.
* [ ] I understand variable-length positional arguments.
* [ ] I know that `args` is a tuple.
* [ ] I can create a function using `*args`.
* [ ] I can pass zero arguments to `*args`.
* [ ] I can pass multiple arguments to `*args`.
* [ ] I can loop through `args`.
* [ ] I can use indexing with `args`.
* [ ] I can use slicing with `args`.
* [ ] I can use `sum()` with `args`.
* [ ] I can use `max()` and `min()` with `args`.
* [ ] I can use conditions with `*args`.
* [ ] I can combine normal parameters with `*args`.
* [ ] I understand packing.
* [ ] I understand unpacking.
* [ ] I can unpack a list using `*`.
* [ ] I can unpack a tuple using `*`.
* [ ] I understand the difference between `*args` and `**kwargs`.
* [ ] I can use `*args` in real-world examples.
* [ ] I understand keyword-only parameters after `*args`.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use `*args` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: `**kwargs`**

In the next topic, you will learn:

* What `**kwargs` means.
* Why `**kwargs` is used.
* Variable-length keyword arguments.
* How Python packs keyword arguments into a dictionary.
* Basic `**kwargs` syntax.
* Accessing values from `kwargs`.
* Looping through `kwargs`.
* Using `keys()`, `values()`, and `items()` with `kwargs`.
* Combining normal parameters with `**kwargs`.
* Combining `*args` and `**kwargs`.
* Difference between `*args` and `**kwargs`.
* Packing and unpacking keyword arguments.
* Passing dictionaries using `**`.
* Using `**kwargs` in real-world applications.
* Common mistakes.
* Advanced `**kwargs` techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Flexible functions become powerful when they can handle data of different sizes."** 🐍📚
