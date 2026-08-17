# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 4: Arguments

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what arguments are in Python functions.
* [ ] Understand the difference between parameters and arguments.
* [ ] Understand positional arguments.
* [ ] Understand keyword arguments.
* [ ] Understand default arguments.
* [ ] Understand variable-length arguments.
* [ ] Use `*args` to accept multiple positional arguments.
* [ ] Use `**kwargs` to accept multiple keyword arguments.
* [ ] Understand positional-only arguments.
* [ ] Understand keyword-only arguments.
* [ ] Combine different types of arguments.
* [ ] Understand argument order rules.
* [ ] Pass different data types as arguments.
* [ ] Pass lists, tuples, sets, and dictionaries as arguments.
* [ ] Return results based on arguments.
* [ ] Combine arguments with conditions and loops.
* [ ] Use arguments in real-world applications.
* [ ] Avoid common mistakes when passing arguments.
* [ ] Build functions using flexible argument patterns.

---

# 📖 1. What are Arguments?

Arguments are the actual values that we pass to a function when calling it.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

Output:

```text
Hello Asha
```

Here:

```text
name
 ↓
Parameter

"Asha"
 ↓
Argument
```

The parameter is the variable defined in the function.

The argument is the actual value supplied when calling the function.

---

# 🧠 2. Parameters vs Arguments

This is one of the most important concepts in functions.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

Here:

```text
name → Parameter

"Asha" → Argument
```

### Parameter

A parameter is a variable listed inside the function definition.

```python
def greet(name):
```

### Argument

An argument is the actual value passed to the function.

```python
greet("Asha")
```

Remember:

```text
Function Definition
        ↓
     Parameter

Function Call
        ↓
     Argument
```

---

# 📚 3. Why Do We Use Arguments?

Arguments make functions flexible and reusable.

Without arguments:

```python
def greet():
    print("Hello Asha")
```

The function can only greet one specific person.

With arguments:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
greet("Neha")
greet("Kiran")
```

Output:

```text
Hello Asha
Hello Neha
Hello Kiran
```

The same function can now work with different values.

---

# 🔢 4. Positional Arguments

Positional arguments are arguments passed according to their position.

Example:

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Asha", 20)
```

Output:

```text
Name: Asha
Age: 20
```

Here:

```text
"Asha" → name
20     → age
```

The first argument goes to the first parameter.

The second argument goes to the second parameter.

---

# 🧠 5. Understanding Positional Matching

Consider:

```python
def display(name, course, age):
    print(name)
    print(course)
    print(age)

display("Asha", "BCA", 20)
```

Python matches them like this:

```text
name   ← "Asha"
course ← "BCA"
age    ← 20
```

The position determines which parameter receives the value.

---

# ⚠️ 6. Changing the Order of Positional Arguments

The order matters when using positional arguments.

Example:

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(20, "Asha")
```

Output:

```text
Name: 20
Age: Asha
```

Python does not automatically understand that `20` is an age.

It simply follows the position.

Therefore:

```text
First argument  → First parameter
Second argument → Second parameter
```

---

# ❌ 7. Too Few Positional Arguments

If a function requires two arguments but only one is supplied:

```python
def student(name, age):
    print(name, age)

student("Asha")
```

Python produces:

```text
TypeError
```

The function requires a value for `age`.

---

# ❌ 8. Too Many Positional Arguments

If a function accepts two arguments but three are supplied:

```python
def student(name, age):
    print(name, age)

student("Asha", 20, "BCA")
```

Python produces:

```text
TypeError
```

The function does not have a parameter to receive the third argument.

---

# 🔑 9. Keyword Arguments

Keyword arguments are arguments passed using parameter names.

Example:

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(name="Asha", age=20)
```

Output:

```text
Name: Asha
Age: 20
```

Here:

```text
name="Asha"
age=20
```

are keyword arguments.

---

# 🔄 10. Keyword Arguments Ignore Position

With keyword arguments, values are assigned using parameter names.

Example:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student(course="BCA", age=20, name="Asha")
```

Output:

```text
Asha
20
BCA
```

Even though the order is different, Python knows which parameter receives each value.

---

# ⚖️ 11. Positional vs Keyword Arguments

| Type       | Meaning                          | Example                        |
| ---------- | -------------------------------- | ------------------------------ |
| Positional | Value assigned by position       | `student("Asha", 20)`          |
| Keyword    | Value assigned by parameter name | `student(name="Asha", age=20)` |

Remember:

```text
Positional → Position matters

Keyword → Parameter name matters
```

---

# 🧩 12. Combining Positional and Keyword Arguments

You can combine positional and keyword arguments.

Example:

```python
def student(name, age, course):
    print(name, age, course)

student("Asha", age=20, course="BCA")
```

Output:

```text
Asha 20 BCA
```

Here:

```text
"Asha" → positional argument
age=20 → keyword argument
course="BCA" → keyword argument
```

---

# ⚠️ 13. Rule for Combining Arguments

When combining positional and keyword arguments:

**Positional arguments must come before keyword arguments.**

Correct:

```python
student("Asha", age=20, course="BCA")
```

Incorrect:

```python
student(name="Asha", 20, "BCA")
```

This produces a syntax error.

Remember:

```text
Positional → First
Keyword    → After
```

---

# ⚙️ 14. Default Arguments

A default argument is an argument that already has a default value.

Example:

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
```

Output:

```text
Hello Guest
```

If no argument is supplied, Python uses the default value.

---

# 🔄 15. Overriding a Default Argument

A default value can be replaced by providing an argument.

Example:

```python
def greet(name="Guest"):
    print("Hello", name)

greet("Asha")
```

Output:

```text
Hello Asha
```

The supplied argument replaces the default value.

---

# 🧠 16. Understanding Default Arguments

Example:

```python
def student(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)

student("Asha")
```

Output:

```text
Name: Asha
Course: BCA
```

Here:

```text
name   → required argument
course → default argument
```

---

# 🔢 17. Multiple Default Arguments

A function can have multiple default arguments.

Example:

```python
def student(name="Unknown", course="BCA", city="Bengaluru"):
    print(name)
    print(course)
    print(city)

student()
```

Output:

```text
Unknown
BCA
Bengaluru
```

---

# ⚠️ 18. Required Parameters and Default Parameters

A required parameter does not have a default value.

Example:

```python
def student(name, course="BCA"):
    print(name, course)
```

Here:

```text
name   → Required
course → Default
```

You must provide `name`.

```python
student("Asha")
```

---

# ❌ 19. Default Parameter Before Required Parameter

This is invalid:

```python
def student(course="BCA", name):
    print(name, course)
```

Python produces:

```text
SyntaxError
```

A required parameter cannot follow a default parameter in a normal function definition.

Correct:

```python
def student(name, course="BCA"):
    print(name, course)
```

Remember:

```text
Required parameters
        ↓
Default parameters
```

---

# 🧮 20. Arguments with Different Data Types

Arguments can contain different data types.

Example:

```python
def display(name, age, salary, active):
    print(name)
    print(age)
    print(salary)
    print(active)

display("Asha", 20, 45000.50, True)
```

Output:

```text
Asha
20
45000.5
True
```

Arguments can be:

```text
String
Integer
Float
Boolean
List
Tuple
Set
Dictionary
```

and other Python objects.

---

# 📋 21. Passing a List as an Argument

A list can be passed to a function.

Example:

```python
def display_skills(skills):
    for skill in skills:
        print(skill)

skills = ["Python", "SQL", "Git"]

display_skills(skills)
```

Output:

```text
Python
SQL
Git
```

The entire list is passed as one argument.

---

# 📦 22. Passing a Tuple as an Argument

Example:

```python
def display_numbers(numbers):
    for number in numbers:
        print(number)

values = (10, 20, 30)

display_numbers(values)
```

Output:

```text
10
20
30
```

---

# 🔵 23. Passing a Set as an Argument

Example:

```python
def display_skills(skills):
    for skill in skills:
        print(skill)

skills = {"Python", "SQL", "Git"}

display_skills(skills)
```

The set is passed as one argument.

The order of displayed elements may vary because sets are unordered collections.

---

# 📖 24. Passing a Dictionary as an Argument

Example:

```python
def display_student(student):
    for key, value in student.items():
        print(key, ":", value)

student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

display_student(student)
```

Output:

```text
name : Asha
age : 20
course : BCA
```

---

# 🔁 25. Arguments with Loops

Arguments can be processed using loops.

Example:

```python
def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    print("Total:", total)

prices = [500, 800, 1200]

calculate_total(prices)
```

Output:

```text
Total: 2500
```

---

# 🧩 26. Arguments with Conditions

Arguments can also be used with conditions.

Example:

```python
def check_result(mark):
    if mark >= 40:
        print("Pass")
    else:
        print("Fail")

check_result(75)
```

Output:

```text
Pass
```

The function behaves differently depending on the argument.

---

# 🌟 27. Real-World Example: Student Result

```python
def check_result(name, marks):
    if marks >= 40:
        print(name, "has passed")
    else:
        print(name, "has failed")

check_result("Asha", 78)
```

Output:

```text
Asha has passed
```

Arguments allow the same function to process different students.

---

# 🌍 28. Real-World Example: Shopping Cart

```python
def calculate_total(price, quantity):
    total = price * quantity
    print("Total:", total)

calculate_total(800, 3)
```

Output:

```text
Total: 2400
```

Here:

```text
800 → price
3   → quantity
```

---

# 🌍 29. Real-World Example: Employee Salary

```python
def calculate_salary(basic_salary, bonus):
    total_salary = basic_salary + bonus
    print("Total Salary:", total_salary)

calculate_salary(40000, 5000)
```

Output:

```text
Total Salary: 45000
```

---

# 🌍 30. Real-World Example: User Profile

```python
def display_profile(username, city="Not Provided"):
    print("Username:", username)
    print("City:", city)

display_profile("asha20")
```

Output:

```text
Username: asha20
City: Not Provided
```

The default argument is useful when optional information is unavailable.

---

# 📦 31. Variable-Length Arguments

Sometimes we do not know how many arguments a function will receive.

Python provides:

```text
*args
**kwargs
```

for handling variable numbers of arguments.

---

# ⭐ 32. The `*args` Syntax

`*args` allows a function to accept multiple positional arguments.

Example:

```python
def add(*numbers):
    print(numbers)

add(10, 20, 30, 40)
```

Output:

```text
(10, 20, 30, 40)
```

The arguments are collected into a tuple.

---

# 🧠 33. Understanding `*args`

Consider:

```python
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    print(total)

add(10, 20, 30, 40)
```

Output:

```text
100
```

Conceptually:

```text
10
20
30
40
 ↓
* numbers
 ↓
(10, 20, 30, 40)
```

---

# 🔢 34. `*args` with Different Numbers of Arguments

The same function can accept different numbers of arguments.

```python
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    print(total)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, 50)
```

Output:

```text
30
60
150
```

---

# 🧩 35. `*args` with a Normal Parameter

You can combine a normal parameter with `*args`.

Example:

```python
def display(category, *items):
    print("Category:", category)

    for item in items:
        print(item)

display("Skills", "Python", "SQL", "Git")
```

Output:

```text
Category: Skills
Python
SQL
Git
```

Here:

```text
category → normal parameter
items    → tuple created by *args
```

---

# ⚠️ 36. `*args` Collects Positional Arguments

Example:

```python
def display(*values):
    print(values)

display("Python", 90, True)
```

Output:

```text
('Python', 90, True)
```

The values are stored inside a tuple.

Important:

```text
*args → Tuple
```

---

# 🔑 37. The `**kwargs` Syntax

`**kwargs` allows a function to accept multiple keyword arguments.

Example:

```python
def display(**details):
    print(details)

display(name="Asha", age=20, course="BCA")
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

The keyword arguments are collected into a dictionary.

Remember:

```text
*args   → Tuple
**kwargs → Dictionary
```

---

# 🧠 38. Understanding `**kwargs`

Example:

```python
def display(**details):
    for key, value in details.items():
        print(key, ":", value)

display(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
name : Asha
age : 20
course : BCA
```

The keyword arguments are stored as key-value pairs.

---

# 🔄 39. Different Keyword Arguments with `**kwargs`

```python
def employee(**details):
    for key, value in details.items():
        print(key, ":", value)

employee(
    name="Neha",
    department="Development",
    experience=2
)
```

Output:

```text
name : Neha
department : Development
experience : 2
```

---

# ⚖️ 40. `*args` vs `**kwargs`

| Feature        | `*args`              | `**kwargs`              |
| -------------- | -------------------- | ----------------------- |
| Accepts        | Positional arguments | Keyword arguments       |
| Stores data in | Tuple                | Dictionary              |
| Example        | `10, 20, 30`         | `name="Asha"`           |
| Access         | Loop through tuple   | Loop through dictionary |

Remember:

```text
*args
 ↓
Positional
 ↓
Tuple

**kwargs
 ↓
Keyword
 ↓
Dictionary
```

---

# 🔥 41. Combining `*args` and `**kwargs`

A function can use both.

Example:

```python
def display(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

display(10, 20, 30, name="Asha", course="BCA")
```

Output:

```text
Positional: (10, 20, 30)
Keyword: {'name': 'Asha', 'course': 'BCA'}
```

---

# 🧩 42. Normal Parameters with `*args` and `**kwargs`

Example:

```python
def student(name, *subjects, **details):
    print("Name:", name)
    print("Subjects:", subjects)
    print("Details:", details)

student(
    "Asha",
    "Python",
    "SQL",
    age=20,
    city="Bengaluru"
)
```

Output:

```text
Name: Asha
Subjects: ('Python', 'SQL')
Details: {'age': 20, 'city': 'Bengaluru'}
```

---

# 📐 43. Argument Order in Function Definitions

When using different argument types, Python follows specific ordering rules.

A common pattern is:

```text
1. Positional parameters
2. *args
3. Keyword-only parameters
4. **kwargs
```

Example:

```python
def example(name, *subjects, city="Bengaluru", **details):
    print(name)
    print(subjects)
    print(city)
    print(details)
```

---

# 🔒 44. Keyword-Only Arguments

Python allows you to force certain arguments to be passed using keywords.

Example:

```python
def student(name, *, age, course):
    print(name)
    print(age)
    print(course)

student("Asha", age=20, course="BCA")
```

Output:

```text
Asha
20
BCA
```

The `*` means that arguments after it must be keyword arguments.

---

# ❌ 45. Incorrect Use of Keyword-Only Arguments

Given:

```python
def student(name, *, age, course):
    print(name, age, course)
```

This is incorrect:

```python
student("Asha", 20, "BCA")
```

because `age` and `course` must be passed by keyword.

Correct:

```python
student("Asha", age=20, course="BCA")
```

---

# 🔐 46. Positional-Only Arguments

Python also allows parameters that must be supplied positionally.

The `/` symbol is used for positional-only parameters.

Example:

```python
def student(name, age, /):
    print(name, age)

student("Asha", 20)
```

This is valid.

The parameters before `/` must be supplied positionally.

---

# ❌ 47. Incorrect Positional-Only Argument

Given:

```python
def student(name, age, /):
    print(name, age)
```

This is invalid:

```python
student(name="Asha", age=20)
```

because `name` and `age` are positional-only parameters.

Correct:

```python
student("Asha", 20)
```

---

# 🧠 48. Positional-Only and Keyword-Only Together

Python can use both `/` and `*`.

Example:

```python
def student(name, age, /, *, course, city):
    print(name)
    print(age)
    print(course)
    print(city)
```

Calling:

```python
student(
    "Asha",
    20,
    course="BCA",
    city="Bengaluru"
)
```

Here:

```text
name, age → positional-only

course, city → keyword-only
```

---

# 📊 49. Argument Types Comparison

| Argument Type       | Syntax           | Purpose                       |
| ------------------- | ---------------- | ----------------------------- |
| Positional          | `func(10, 20)`   | Match by position             |
| Keyword             | `func(x=10)`     | Match by name                 |
| Default             | `def func(x=10)` | Provide fallback value        |
| Variable positional | `*args`          | Accept many positional values |
| Variable keyword    | `**kwargs`       | Accept many keyword values    |
| Positional-only     | `/`              | Force positional passing      |
| Keyword-only        | `*`              | Force keyword passing         |

---

# 🧠 50. Argument Unpacking

Python allows collections to be unpacked into function arguments.

For positional arguments, use `*`.

Example:

```python
def add(a, b, c):
    print(a + b + c)

numbers = [10, 20, 30]

add(*numbers)
```

Output:

```text
60
```

The list is unpacked into:

```text
10, 20, 30
```

---

# 🔑 51. Dictionary Unpacking with `**`

Dictionaries can be unpacked into keyword arguments using `**`.

Example:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

details = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

student(**details)
```

Output:

```text
Asha
20
BCA
```

---

# ⚖️ 52. `*` Unpacking vs `**` Unpacking

Remember:

```text
*list_or_tuple
        ↓
Positional arguments

**dictionary
        ↓
Keyword arguments
```

Example:

```python
numbers = [10, 20, 30]

add(*numbers)
```

and:

```python
details = {
    "name": "Asha",
    "age": 20
}

student(**details)
```

---

# 🔄 53. Arguments and Return Values

Arguments can be used to calculate and return results.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

Here:

```text
10, 20
 ↓
Arguments

a, b
 ↓
Parameters

a + b
 ↓
Return value
```

---

# 🧮 54. Real-World Example: Calculate Discount

```python
def calculate_discount(price, discount):
    amount = price * discount / 100
    final_price = price - amount

    return final_price

result = calculate_discount(5000, 10)

print("Final Price:", result)
```

Output:

```text
Final Price: 4500.0
```

Arguments make the function reusable for different prices and discounts.

---

# 🌍 55. Real-World Example: Electricity Bill

```python
def calculate_bill(units, rate):
    bill = units * rate
    return bill

total = calculate_bill(250, 8)

print("Bill:", total)
```

Output:

```text
Bill: 2000
```

---

# 🌍 56. Real-World Example: Student Average

```python
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)

    return average

marks = [80, 75, 90, 85]

average = calculate_average(marks)

print("Average:", average)
```

Output:

```text
Average: 82.5
```

A list is passed as one argument.

---

# 🌍 57. Real-World Example: Product Information

```python
def display_product(name, price, quantity=1):
    total = price * quantity

    print("Product:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)

display_product("Keyboard", 1500, 2)
```

Output:

```text
Product: Keyboard
Price: 1500
Quantity: 2
Total: 3000
```

---

# 🌍 58. Real-World Example: Employee Information

```python
def display_employee(name, department="General", experience=0):
    print("Name:", name)
    print("Department:", department)
    print("Experience:", experience)

display_employee(
    "Neha",
    department="Development",
    experience=2
)
```

Output:

```text
Name: Neha
Department: Development
Experience: 2
```

---

# 🔢 59. Real-World Example: Shopping Cart with `*args`

```python
def calculate_cart_total(*prices):
    total = 0

    for price in prices:
        total += price

    return total

total = calculate_cart_total(500, 800, 1200, 300)

print("Cart Total:", total)
```

Output:

```text
Cart Total: 2800
```

The function can accept any number of prices.

---

# 📦 60. Real-World Example: User Profile with `**kwargs`

```python
def display_profile(**details):
    for key, value in details.items():
        print(key, ":", value)

display_profile(
    username="asha20",
    city="Bengaluru",
    course="BCA"
)
```

Output:

```text
username : asha20
city : Bengaluru
course : BCA
```

---

# ⚠️ 61. Common Mistake: Confusing Parameters and Arguments

Incorrect understanding:

```text
name = Argument
```

when:

```python
def greet(name):
```

Actually:

```text
name → Parameter
```

And:

```python
greet("Asha")
```

contains:

```text
"Asha" → Argument
```

Remember:

```text
Definition → Parameter
Call       → Argument
```

---

# ⚠️ 62. Common Mistake: Wrong Positional Order

Example:

```python
def student(name, age):
    print(name, age)

student(20, "Asha")
```

Python does not automatically identify the data.

It follows position:

```text
20     → name
"Asha" → age
```

Use keyword arguments when you want clearer parameter matching.

---

# ⚠️ 63. Common Mistake: Positional Argument After Keyword Argument

Incorrect:

```python
def student(name, age):
    print(name, age)

student(name="Asha", 20)
```

This is invalid.

Correct:

```python
student("Asha", age=20)
```

---

# ⚠️ 64. Common Mistake: Too Many Arguments

Example:

```python
def add(a, b):
    return a + b

add(10, 20, 30)
```

The function has only two parameters.

Python raises:

```text
TypeError
```

Use `*args` when you need to accept a variable number of positional arguments.

---

# ⚠️ 65. Common Mistake: Forgetting `**` for Dictionary Unpacking

Suppose:

```python
def student(name, age):
    print(name, age)

details = {
    "name": "Asha",
    "age": 20
}
```

Correct:

```python
student(**details)
```

Not:

```python
student(details)
```

The second version passes the entire dictionary as one positional argument.

---

# ⚠️ 66. Common Mistake: Forgetting `*` for List Unpacking

Suppose:

```python
def add(a, b, c):
    print(a + b + c)

numbers = [10, 20, 30]
```

Correct:

```python
add(*numbers)
```

Without `*`:

```python
add(numbers)
```

the entire list is passed as one argument.

---

# 📊 67. Arguments Master Comparison

| Concept    | Example                  | Meaning                      |
| ---------- | ------------------------ | ---------------------------- |
| Parameter  | `def add(a, b)`          | Variables in definition      |
| Argument   | `add(10, 20)`            | Values in function call      |
| Positional | `add(10, 20)`            | Position determines matching |
| Keyword    | `add(a=10, b=20)`        | Name determines matching     |
| Default    | `def add(a, b=10)`       | Fallback value               |
| `*args`    | `def add(*numbers)`      | Many positional arguments    |
| `**kwargs` | `def show(**details)`    | Many keyword arguments       |
| `*`        | `def show(name, *, age)` | Keyword-only arguments       |
| `/`        | `def show(name, /)`      | Positional-only arguments    |
| `*list`    | `add(*numbers)`          | Unpack positional values     |
| `**dict`   | `show(**details)`        | Unpack keyword values        |

---

# 💻 68. Practice Programs

## 🟢 Easy

### Program 1: Pass a Name as an Argument

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

---

### Program 2: Add Two Numbers

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

### Program 3: Display Student Information

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Asha", 20)
```

---

### Program 4: Use a Keyword Argument

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Asha")
```

---

## 🟡 Medium

### Program 5: Use a Default Argument

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Asha")
```

---

### Program 6: Calculate Rectangle Area

```python
def rectangle_area(length, width):
    area = length * width
    print("Area:", area)

rectangle_area(10, 5)
```

---

### Program 7: Calculate Shopping Total

```python
def calculate_total(price, quantity):
    total = price * quantity
    print("Total:", total)

calculate_total(800, 3)
```

---

### Program 8: Process a List Argument

```python
def find_total(numbers):
    total = 0

    for number in numbers:
        total += number

    print("Total:", total)

numbers = [10, 20, 30, 40]

find_total(numbers)
```

---

## 🔴 Advanced

### Program 9: Use `*args`

```python
def calculate_total(*prices):
    total = 0

    for price in prices:
        total += price

    print("Total:", total)

calculate_total(500, 800, 1200)
```

---

### Program 10: Use `**kwargs`

```python
def display_student(**details):
    for key, value in details.items():
        print(key, ":", value)

display_student(
    name="Asha",
    age=20,
    course="BCA"
)
```

---

### Program 11: Combine Normal Parameter and `*args`

```python
def display_subjects(name, *subjects):
    print("Student:", name)

    for subject in subjects:
        print(subject)

display_subjects(
    "Asha",
    "Python",
    "SQL",
    "Git"
)
```

---

### Program 12: Combine `*args` and `**kwargs`

```python
def display(*values, **details):
    print("Values:", values)
    print("Details:", details)

display(
    10,
    20,
    30,
    name="Asha",
    course="BCA"
)
```

---

# 🏆 69. Challenge

Create a function called `student_report()`.

The function should accept:

```text
Student name
Multiple subject marks
Additional student information
```

Use:

```text
Normal argument
*args
**kwargs
```

Then:

1. Display the student's name.
2. Display all marks.
3. Calculate the total marks.
4. Calculate the average.
5. Display additional information.
6. Display whether the student passed or failed.
7. Return the average.

Example data:

```python
student_report(
    "Asha",
    90,
    85,
    80,
    course="BCA",
    city="Bengaluru"
)
```

### Expected Concept

```text
"Asha"
   ↓
Normal argument

90, 85, 80
   ↓
*args

course="BCA"
city="Bengaluru"
   ↓
**kwargs
```

Try solving the challenge without copying a complete solution.

---

# 🧪 70. Mini Project: Shopping Cart Function

Create a function that calculates a shopping cart total.

The function should:

* [ ] Accept multiple product prices using `*args`.
* [ ] Calculate the total price.
* [ ] Accept customer information using `**kwargs`.
* [ ] Display customer details.
* [ ] Display the total cart amount.
* [ ] Return the total.

Example:

```python
calculate_cart(
    55000,
    800,
    1500,
    name="Asha",
    city="Bengaluru"
)
```

The function should conceptually process:

```text
55000
800
1500
   ↓
*args
   ↓
Product prices
```

and:

```text
name="Asha"
city="Bengaluru"
   ↓
**kwargs
   ↓
Customer details
```

---

# 🎤 71. Interview Questions

* [ ] What are arguments in Python?
* [ ] What is the difference between a parameter and an argument?
* [ ] What are positional arguments?
* [ ] What are keyword arguments?
* [ ] What is the difference between positional and keyword arguments?
* [ ] Can positional and keyword arguments be combined?
* [ ] What rule must be followed when combining positional and keyword arguments?
* [ ] What are default arguments?
* [ ] Why are default arguments useful?
* [ ] Can a default argument be overridden?
* [ ] Why must required parameters come before default parameters?
* [ ] What is `*args`?
* [ ] What type of object does `*args` create?
* [ ] What is `**kwargs`?
* [ ] What type of object does `**kwargs` create?
* [ ] What is the difference between `*args` and `**kwargs`?
* [ ] Can `*args` and `**kwargs` be used together?
* [ ] What are keyword-only arguments?
* [ ] What are positional-only arguments?
* [ ] What does `/` mean in a function definition?
* [ ] What does `*` mean when used before keyword-only parameters?
* [ ] What is argument unpacking?
* [ ] How do you unpack a list into function arguments?
* [ ] How do you unpack a dictionary into keyword arguments?
* [ ] What happens if too few arguments are supplied?
* [ ] What happens if too many arguments are supplied?
* [ ] Why are arguments useful in reusable functions?

---

# 📝 72. Assignment

Complete the following programs.

### Task 1

Create a function that accepts a person's:

```text
name
age
city
```

Display all three values.

---

### Task 2

Create a function that accepts two numbers and returns their sum.

---

### Task 3

Create a function that uses keyword arguments to display:

```text
name
course
semester
```

---

### Task 4

Create a function with a default argument:

```text
country = "India"
```

Call the function once without providing the country and once with a different country.

---

### Task 5

Create a function that accepts a list of marks.

Use a loop to calculate the total marks.

---

### Task 6

Create a function using `*args` to calculate the total of any number of numbers.

---

### Task 7

Create a function using `*args` to find the largest number.

---

### Task 8

Create a function using `**kwargs` to display employee information.

Use:

```text
name
department
salary
experience
```

---

### Task 9

Create a function that uses both `*args` and `**kwargs`.

Use:

```text
*args → programming skills
**kwargs → student details
```

---

### Task 10

Create a function using keyword-only arguments.

The function should accept:

```text
name → positional
age → keyword-only
course → keyword-only
```

---

### Task 11

Create a function using positional-only arguments.

The function should accept:

```text
length
width
```

Calculate the rectangle area.

---

### Task 12

Create a real-world program that uses at least five different argument concepts:

```text
Positional arguments
Keyword arguments
Default arguments
*args
**kwargs
```

---

# 🧠 73. Memory Tricks

Remember the basic difference:

```text
Parameter
   ↓
Variable in function definition

Argument
   ↓
Actual value in function call
```

---

Remember positional arguments:

```text
Position
   ↓
Matching
   ↓
First → First
Second → Second
```

---

Remember keyword arguments:

```text
Parameter Name
      ↓
Matching
      ↓
name="Asha"
age=20
```

---

Remember default arguments:

```text
No value supplied
       ↓
Default value used
```

---

Remember variable-length arguments:

```text
*args
  ↓
Many positional arguments
  ↓
Tuple
```

```text
**kwargs
   ↓
Many keyword arguments
   ↓
Dictionary
```

---

Remember unpacking:

```text
*list
   ↓
Positional arguments
```

```text
**dictionary
      ↓
Keyword arguments
```

---

Remember argument restrictions:

```text
/ 
↓
Positional-only
```

```text
*
↓
Keyword-only
```

---

# 📌 74. Important Rules to Remember

```text
1. Arguments are actual values passed to a function.

2. Parameters are variables defined in a function.

3. Positional arguments are matched according to position.

4. Keyword arguments are matched using parameter names.

5. Positional arguments must come before keyword arguments.

6. Default arguments provide fallback values.

7. Required parameters must come before default parameters.

8. *args accepts multiple positional arguments.

9. *args stores the collected arguments in a tuple.

10. **kwargs accepts multiple keyword arguments.

11. **kwargs stores the collected arguments in a dictionary.

12. A function can combine normal parameters, *args, and **kwargs.

13. Keyword-only parameters must be passed using parameter names.

14. Positional-only parameters must be passed according to position.

15. / is used to define positional-only parameters.

16. * can be used to define keyword-only parameters.

17. * can unpack a list or tuple into positional arguments.

18. ** can unpack a dictionary into keyword arguments.

19. Arguments can contain different Python data types.

20. Arguments make functions reusable and flexible.

21. Too few required arguments cause a TypeError.

22. Too many arguments cause a TypeError unless the function accepts variable-length arguments.

23. Dictionary data can be passed as a single argument or unpacked using **.

24. Lists and tuples can be passed as single arguments or unpacked using *.

25. Arguments can be combined with loops, conditions, and return statements.
```

---

# 📊 75. Arguments Structure

```text
                         FUNCTION ARGUMENTS
                                  │
                                  ↓
                           ARGUMENT TYPES
                                  │
              ┌───────────────────┼───────────────────┐
              ↓                   ↓                   ↓
          POSITIONAL           KEYWORD             DEFAULT
              │                   │                   │
              ↓                   ↓                   ↓
        func(10, 20)       func(a=10)         def func(a=10)
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ↓
                         VARIABLE-LENGTH
                                  │
                     ┌────────────┴────────────┐
                     ↓                         ↓
                   *args                    **kwargs
                     ↓                         ↓
                  Tuple                    Dictionary
                     │                         │
                     ↓                         ↓
              Positional Values         Keyword Values
```

---

# 🔐 76. Advanced Arguments Structure

```text
                         ARGUMENTS
                             │
          ┌──────────────────┼──────────────────┐
          ↓                  ↓                  ↓
      Positional          Keyword           Default
          │                  │                  │
          ↓                  ↓                  ↓
       Normal              Named          Fallback Value
          │                  │
          └──────────────┬───┘
                         ↓
                 Variable Length
                    /         \
                   /           \
                  ↓             ↓
               *args         **kwargs
                  ↓             ↓
                Tuple       Dictionary

Additional Restrictions
        │
        ├── / → Positional-only
        │
        └── * → Keyword-only

Unpacking
    │
    ├── *list/tuple → Positional
    │
    └── **dict → Keyword
```

---

# 📚 77. Complete Arguments Cheat Sheet

### Positional Arguments

```python
def student(name, age):
    print(name, age)

student("Asha", 20)
```

### Keyword Arguments

```python
student(name="Asha", age=20)
```

### Default Arguments

```python
def greet(name="Guest"):
    print(name)
```

### Variable Positional Arguments

```python
def add(*numbers):
    print(numbers)
```

### Variable Keyword Arguments

```python
def display(**details):
    print(details)
```

### Combine `*args` and `**kwargs`

```python
def display(*args, **kwargs):
    print(args)
    print(kwargs)
```

### Keyword-Only Arguments

```python
def student(name, *, age, course):
    print(name, age, course)
```

### Positional-Only Arguments

```python
def student(name, age, /):
    print(name, age)
```

### List/Tuple Unpacking

```python
numbers = [10, 20, 30]

add(*numbers)
```

### Dictionary Unpacking

```python
details = {
    "name": "Asha",
    "age": 20
}

student(**details)
```

---

# 🏆 78. Arguments Mastery

```text
                         FUNCTIONS
                             │
                             ↓
                          ARGUMENTS
                             │
       ┌─────────────────────┼─────────────────────┐
       ↓                     ↓                     ↓
   POSITIONAL             KEYWORD               DEFAULT
       │                     │                     │
       ↓                     ↓                     ↓
  Position Match        Name Match          Fallback Value
       │
       ↓
   VARIABLE LENGTH
       │
   ┌───┴────┐
   ↓        ↓
 *args    **kwargs
   ↓        ↓
 Tuple   Dictionary
   │        │
   ↓        ↓
Position  Keyword
Values    Values

Advanced Control
       │
   ┌───┴────┐
   ↓        ↓
   /        *
   ↓        ↓
Position   Keyword
Only       Only

Unpacking
   │
   ┌──────────┐
   ↓          ↓
 *list      **dict
   ↓          ↓
Position   Keyword
Arguments  Arguments
```

---

# 📚 79. Summary

In this lesson, you learned:

* What arguments are.
* The difference between parameters and arguments.
* How positional arguments work.
* How keyword arguments work.
* The difference between positional and keyword arguments.
* How to combine positional and keyword arguments.
* What default arguments are.
* How default arguments provide fallback values.
* How to override default arguments.
* How to pass lists, tuples, sets, and dictionaries as arguments.
* How arguments work with loops.
* How arguments work with conditions.
* What variable-length arguments are.
* How to use `*args`.
* Why `*args` creates a tuple.
* How to use `**kwargs`.
* Why `**kwargs` creates a dictionary.
* How to combine `*args` and `**kwargs`.
* How to use keyword-only arguments.
* How to use positional-only arguments.
* How `/` defines positional-only parameters.
* How `*` defines keyword-only parameters.
* How argument unpacking works.
* How `*` unpacks lists and tuples.
* How `**` unpacks dictionaries.
* How arguments work with return values.
* How to use arguments in real-world programs.
* Common mistakes when passing arguments.
* How to build flexible and reusable functions.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what arguments are.
* [ ] I understand the difference between parameters and arguments.
* [ ] I can use positional arguments.
* [ ] I can use keyword arguments.
* [ ] I understand positional vs keyword arguments.
* [ ] I can use default arguments.
* [ ] I understand how default arguments work.
* [ ] I can pass lists as arguments.
* [ ] I can pass tuples as arguments.
* [ ] I can pass dictionaries as arguments.
* [ ] I understand `*args`.
* [ ] I understand that `*args` creates a tuple.
* [ ] I understand `**kwargs`.
* [ ] I understand that `**kwargs` creates a dictionary.
* [ ] I can combine `*args` and `**kwargs`.
* [ ] I understand keyword-only arguments.
* [ ] I understand positional-only arguments.
* [ ] I understand `/`.
* [ ] I understand `*` for keyword-only parameters.
* [ ] I can unpack lists and tuples using `*`.
* [ ] I can unpack dictionaries using `**`.
* [ ] I can combine arguments with loops.
* [ ] I can combine arguments with conditions.
* [ ] I can use arguments with return values.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the mini project.
* [ ] I completed the assignment.
* [ ] I can use different argument types without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Return Statement**

In the next topic, you will learn:

* What the `return` statement is.
* Why functions return values.
* Difference between `print()` and `return`.
* Returning a single value.
* Returning multiple values.
* Returning strings.
* Returning numbers.
* Returning lists.
* Returning tuples.
* Returning dictionaries.
* Returning Boolean values.
* Returning calculated results.
* Using returned values in variables.
* Using returned values in conditions.
* Using returned values in loops.
* Returning from conditional statements.
* Returning from nested functions.
* Early `return`.
* Returning `None`.
* Multiple `return` statements.
* Practical real-world examples.
* Common mistakes with `return`.
* Practice programs.
* Challenges.
* Mini projects.

---

## ⭐ Quote of the Day

> **"Arguments make functions flexible; they allow one function to work with many different values."** 🐍📚
