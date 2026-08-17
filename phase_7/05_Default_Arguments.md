# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 5: Default Arguments

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what default arguments are.
* [ ] Understand why default arguments are used.
* [ ] Understand the syntax of default arguments.
* [ ] Create functions with default values.
* [ ] Call functions with and without arguments.
* [ ] Understand how default values work.
* [ ] Override default values by passing arguments.
* [ ] Use multiple default arguments.
* [ ] Understand positional arguments with default arguments.
* [ ] Understand keyword arguments with default arguments.
* [ ] Understand the rules for placing default arguments.
* [ ] Avoid the `non-default argument follows default argument` error.
* [ ] Use default arguments with different data types.
* [ ] Use default arguments with real-world functions.
* [ ] Understand mutable default argument problems.
* [ ] Use `None` safely as a default value.
* [ ] Combine default arguments with `*args` and `**kwargs`.
* [ ] Use default arguments in practical programs.
* [ ] Avoid common mistakes with default arguments.

---

# 📖 1. What are Default Arguments?

A **default argument** is a parameter that already has a value assigned to it in the function definition.

If the caller does not provide a value for that parameter, Python automatically uses the default value.

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

Here:

```text
name="Guest"
```

is a default parameter.

---

# 🧠 2. Why Do We Use Default Arguments?

Default arguments are useful when a function should have a **common or standard value**.

For example, suppose we create a function that displays a user's country.

Most users may be from India:

```python
def show_country(country="India"):
    print("Country:", country)
```

If no country is provided:

```python
show_country()
```

Output:

```text
Country: India
```

If another country is provided:

```python
show_country("Canada")
```

Output:

```text
Country: Canada
```

Default arguments make functions more flexible.

---

# 📚 3. Basic Function Syntax

A normal function with a parameter:

```python
def greet(name):
    print("Hello", name)
```

A function with a default argument:

```python
def greet(name="Guest"):
    print("Hello", name)
```

The general syntax is:

```python
def function_name(parameter=default_value):
    # function body
```

Example:

```python
def display_city(city="Bengaluru"):
    print("City:", city)
```

---

# 🔍 4. Calling a Function Without an Argument

When a default parameter is used, the argument can be omitted.

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

Since no value was supplied for `name`, Python uses:

```text
Guest
```

---

# 🔄 5. Calling a Function With an Argument

A default value is only used when an argument is not provided.

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

The supplied value replaces the default value for that function call.

---

# ⚖️ 6. Default Argument vs Normal Argument

Normal parameter:

```python
def greet(name):
    print("Hello", name)
```

The argument is required:

```python
greet("Asha")
```

Default parameter:

```python
def greet(name="Guest"):
    print("Hello", name)
```

The argument is optional:

```python
greet()
```

Remember:

```text
Normal argument
      ↓
Required

Default argument
      ↓
Optional
```

---

# 🧠 7. How Default Arguments Work

Consider:

```python
def greet(name="Guest"):
    print("Hello", name)
```

When we call:

```python
greet()
```

Python uses:

```text
name = "Guest"
```

When we call:

```python
greet("Asha")
```

Python uses:

```text
name = "Asha"
```

Therefore:

```text
Argument provided?
       │
   ┌───┴───┐
   ↓       ↓
  Yes      No
   ↓       ↓
Use       Use
provided  default
value     value
```

---

# 📝 8. Simple Example

```python
def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Asha")
```

Output:

```text
Welcome Student
Welcome Asha
```

The first call uses the default value.

The second call uses the supplied value.

---

# 🔢 9. Default Argument With Numbers

Default arguments can also contain numbers.

Example:

```python
def calculate_square(number=5):
    print(number * number)

calculate_square()
```

Output:

```text
25
```

If we provide another number:

```python
calculate_square(8)
```

Output:

```text
64
```

---

# 💰 10. Default Argument With a Price

Default arguments are useful in financial calculations.

```python
def calculate_discount(price, discount=10):
    final_price = price - (price * discount / 100)
    print("Final Price:", final_price)

calculate_discount(1000)
```

Output:

```text
Final Price: 900.0
```

Here:

```text
discount=10
```

means the default discount is 10%.

---

# 🌍 11. Real-World Example: Country

```python
def show_country(name, country="India"):
    print(name, "is from", country)

show_country("Asha")
show_country("John", "Canada")
```

Output:

```text
Asha is from India
John is from Canada
```

The first function call uses the default country.

The second function call overrides it.

---

# 🧩 12. Multiple Default Arguments

A function can have multiple default parameters.

Example:

```python
def student_info(name="Unknown", course="BCA"):
    print("Name:", name)
    print("Course:", course)

student_info()
```

Output:

```text
Name: Unknown
Course: BCA
```

Both parameters have default values.

---

# 🔄 13. Overriding Multiple Default Arguments

Default values can be replaced by passing arguments.

```python
def student_info(name="Unknown", course="BCA"):
    print("Name:", name)
    print("Course:", course)

student_info("Asha", "MCA")
```

Output:

```text
Name: Asha
Course: MCA
```

Both defaults have been overridden.

---

# 📌 14. Some Arguments Default, Some Not

A function can have both required and default parameters.

Example:

```python
def student_info(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)
```

Here:

```text
name
 ↓
Required

course
 ↓
Default
```

Calling:

```python
student_info("Asha")
```

Output:

```text
Name: Asha
Course: BCA
```

---

# ⚠️ 15. Default Arguments Must Come After Required Arguments

This is valid:

```python
def student_info(name, course="BCA"):
    print(name, course)
```

This is invalid:

```python
def student_info(course="BCA", name):
    print(name, course)
```

Python raises:

```text
SyntaxError: non-default argument follows default argument
```

Remember:

```text
Required parameter
        ↓
Default parameter
```

Correct:

```python
def function(a, b=10):
```

Incorrect:

```python
def function(a=10, b):
```

---

# 🧠 16. Why Does This Rule Exist?

Consider:

```python
def example(a=10, b):
    print(a, b)
```

If we call:

```python
example(20)
```

Python cannot clearly determine whether `20` belongs to `a` or `b`.

Therefore Python requires all required parameters to come before default parameters.

Correct structure:

```python
def example(a, b=10):
```

---

# 🔢 17. Multiple Required and Default Arguments

You can have several required parameters followed by several default parameters.

Example:

```python
def employee(name, department, experience=1, status="Active"):
    print(name)
    print(department)
    print(experience)
    print(status)
```

Call:

```python
employee("Neha", "Development")
```

Output:

```text
Neha
Development
1
Active
```

---

# 🔄 18. Overriding One Default Argument

Consider:

```python
def employee(name, department, experience=1, status="Active"):
    print(name, department, experience, status)
```

We can change only the experience:

```python
employee("Neha", "Development", 3)
```

Output:

```text
Neha Development 3 Active
```

The `status` parameter still uses its default value.

---

# 🔑 19. Keyword Arguments With Default Arguments

Keyword arguments can make default arguments easier to control.

Example:

```python
def employee(name, department="Development", status="Active"):
    print(name, department, status)

employee("Neha", status="Inactive")
```

Output:

```text
Neha Development Inactive
```

Here, `department` uses its default value while `status` is explicitly provided.

---

# 🧩 20. Positional Arguments With Default Arguments

Arguments can be supplied according to their position.

Example:

```python
def student(name, age=20, course="BCA"):
    print(name, age, course)

student("Asha", 21, "MCA")
```

Output:

```text
Asha 21 MCA
```

The values are assigned according to their positions.

---

# ⚖️ 21. Positional vs Keyword Arguments

Consider:

```python
def student(name, age=20, course="BCA"):
    print(name, age, course)
```

Positional:

```python
student("Asha", 21, "MCA")
```

Keyword:

```python
student(name="Asha", age=21, course="MCA")
```

Both produce:

```text
Asha 21 MCA
```

---

# 🧠 22. Skipping a Default Argument

Suppose:

```python
def student(name, age=20, course="BCA"):
    print(name, age, course)
```

We want to change only `course`.

We can use a keyword argument:

```python
student("Asha", course="MCA")
```

Output:

```text
Asha 20 MCA
```

This is useful when we want to skip a default parameter.

---

# 🛒 23. Real-World Example: Shopping

```python
def order(product, quantity=1):
    print("Product:", product)
    print("Quantity:", quantity)

order("Laptop")
```

Output:

```text
Product: Laptop
Quantity: 1
```

If the customer orders multiple items:

```python
order("Laptop", 3)
```

Output:

```text
Product: Laptop
Quantity: 3
```

---

# 💳 24. Real-World Example: Payment

```python
def payment(amount, currency="INR"):
    print("Amount:", amount)
    print("Currency:", currency)

payment(5000)
```

Output:

```text
Amount: 5000
Currency: INR
```

Another currency can be supplied:

```python
payment(100, "USD")
```

Output:

```text
Amount: 100
Currency: USD
```

---

# 📦 25. Real-World Example: Delivery

```python
def delivery(address, method="Standard"):
    print("Address:", address)
    print("Delivery:", method)

delivery("Bengaluru")
```

Output:

```text
Address: Bengaluru
Delivery: Standard
```

The customer can choose another delivery method:

```python
delivery("Bengaluru", "Express")
```

Output:

```text
Address: Bengaluru
Delivery: Express
```

---

# 🎓 26. Real-World Example: Student Registration

```python
def register_student(name, course="BCA", semester=1):
    print("Name:", name)
    print("Course:", course)
    print("Semester:", semester)

register_student("Asha")
```

Output:

```text
Name: Asha
Course: BCA
Semester: 1
```

---

# 💼 27. Real-World Example: Employee

```python
def employee(name, department="Development", status="Active"):
    print("Name:", name)
    print("Department:", department)
    print("Status:", status)

employee("Neha")
```

Output:

```text
Name: Neha
Department: Development
Status: Active
```

---

# 🌡️ 28. Default Argument With Boolean Values

Default arguments can also use Boolean values.

```python
def account(username, active=True):
    print("Username:", username)
    print("Active:", active)

account("asha20")
```

Output:

```text
Username: asha20
Active: True
```

We can override it:

```python
account("asha20", False)
```

Output:

```text
Username: asha20
Active: False
```

---

# 🧵 29. Default Argument With Strings

Strings are commonly used as default values.

```python
def message(text="Welcome to Python"):
    print(text)

message()
```

Output:

```text
Welcome to Python
```

Another message:

```python
message("Good Morning")
```

Output:

```text
Good Morning
```

---

# 📋 30. Default Argument With Lists

A list can technically be used as a default argument:

```python
def show_skills(skills=[]):
    print(skills)

show_skills()
```

Output:

```text
[]
```

However, using a mutable object such as a list as a default argument can cause unexpected behavior.

This is an important Python concept.

---

# ⚠️ 31. The Mutable Default Argument Problem

Consider:

```python
def add_skill(skill, skills=[]):
    skills.append(skill)
    print(skills)

add_skill("Python")
add_skill("SQL")
```

You may expect:

```text
['Python']
['SQL']
```

But Python produces:

```text
['Python']
['Python', 'SQL']
```

Why?

Because the same default list is reused between function calls.

---

# 🧠 32. Why Does the Mutable Default Problem Happen?

Default argument values are evaluated when the function is **defined**, not every time the function is called.

Example:

```python
def add_skill(skill, skills=[]):
    skills.append(skill)
```

The empty list is created once.

It is then reused whenever the default value is needed.

Think of it as:

```text
Function definition
       ↓
Create default list []
       ↓
Function call
       ↓
Reuse the same list
       ↓
Function call
       ↓
Reuse the same list
```

---

# 🛡️ 33. Safe Solution Using `None`

The recommended solution is to use `None` as the default value.

```python
def add_skill(skill, skills=None):
    if skills is None:
        skills = []

    skills.append(skill)
    print(skills)

add_skill("Python")
add_skill("SQL")
```

Output:

```text
['Python']
['SQL']
```

Each function call receives a new list.

---

# 🔍 34. Why Use `None`?

`None` acts as a signal meaning:

```text
No list was provided.
```

Then we create a new list inside the function:

```python
if skills is None:
    skills = []
```

This avoids sharing the same mutable object between calls.

---

# ⚖️ 35. Immutable vs Mutable Default Values

Immutable values are generally safe as defaults:

```python
def example(name="Guest"):
```

```python
def example(age=18):
```

```python
def example(active=True):
```

Mutable values require caution:

```python
def example(items=[]):
```

```python
def example(data={}):
```

Common mutable objects include:

```text
list
dictionary
set
```

A safer pattern is:

```python
def example(items=None):
    if items is None:
        items = []
```

---

# 🧩 36. Default Dictionary Argument

Avoid:

```python
def add_user(name, users={}):
    users[name] = True
    return users
```

Instead:

```python
def add_user(name, users=None):
    if users is None:
        users = {}

    users[name] = True
    return users
```

This creates a fresh dictionary when one is not supplied.

---

# 🔄 37. Default Set Argument

Avoid:

```python
def add_skill(skill, skills=set()):
    skills.add(skill)
    return skills
```

Prefer:

```python
def add_skill(skill, skills=None):
    if skills is None:
        skills = set()

    skills.add(skill)
    return skills
```

This avoids reusing the same set.

---

# 🧮 38. Default Arguments in Calculations

Default arguments are very useful in mathematical functions.

```python
def calculate_power(number, power=2):
    return number ** power

print(calculate_power(5))
```

Output:

```text
25
```

The default power is `2`.

We can override it:

```python
print(calculate_power(5, 3))
```

Output:

```text
125
```

---

# 💰 39. Default Tax Rate Example

```python
def calculate_tax(price, tax_rate=18):
    tax = price * tax_rate / 100
    return tax

print(calculate_tax(1000))
```

Output:

```text
180.0
```

A different tax rate can be supplied:

```python
print(calculate_tax(1000, 12))
```

Output:

```text
120.0
```

---

# 🏦 40. Default Interest Rate Example

```python
def calculate_interest(principal, rate=7):
    interest = principal * rate / 100
    return interest

print(calculate_interest(10000))
```

Output:

```text
700.0
```

The default interest rate is 7%.

---

# 🔁 41. Default Arguments With Loops

Default arguments can be used inside functions containing loops.

```python
def print_numbers(limit=5):
    for number in range(1, limit + 1):
        print(number)

print_numbers()
```

Output:

```text
1
2
3
4
5
```

We can change the limit:

```python
print_numbers(3)
```

Output:

```text
1
2
3
```

---

# 🔢 42. Default Start Value With `range()`

```python
def count_numbers(start=1, end=5):
    for number in range(start, end + 1):
        print(number)

count_numbers()
```

Output:

```text
1
2
3
4
5
```

Another call:

```python
count_numbers(3, 7)
```

Output:

```text
3
4
5
6
7
```

---

# 🧠 43. Default Arguments With Conditions

Default arguments can also be used with conditions.

```python
def check_age(age, minimum_age=18):
    if age >= minimum_age:
        print("Eligible")
    else:
        print("Not Eligible")

check_age(20)
```

Output:

```text
Eligible
```

Here:

```text
minimum_age = 18
```

is the default value.

---

# 🌍 44. Real-World Example: Login System

```python
def login(username, role="user"):
    print("Username:", username)
    print("Role:", role)

login("asha20")
```

Output:

```text
Username: asha20
Role: user
```

An administrator can be specified:

```python
login("admin01", "admin")
```

Output:

```text
Username: admin01
Role: admin
```

---

# 📱 45. Real-World Example: Notification

```python
def send_notification(message, priority="Normal"):
    print("Message:", message)
    print("Priority:", priority)

send_notification("Your order has been shipped")
```

Output:

```text
Message: Your order has been shipped
Priority: Normal
```

A high-priority notification:

```python
send_notification("Server is down", "High")
```

Output:

```text
Message: Server is down
Priority: High
```

---

# 🧠 46. Default Arguments With `*args`

Default arguments can be used together with variable-length arguments, but the parameter arrangement must follow Python's function parameter rules.

Example:

```python
def calculate_total(discount=0, *prices):
    total = sum(prices)
    total -= total * discount / 100
    return total

print(calculate_total(10, 100, 200, 300))
```

Output:

```text
540.0
```

Here:

```text
discount → default parameter
prices   → *args
```

---

# 🧠 47. Default Arguments With `**kwargs`

Default values can also be used alongside keyword-based parameters.

Example:

```python
def create_profile(name, role="Student", **details):
    print("Name:", name)
    print("Role:", role)
    print("Details:", details)

create_profile("Asha", city="Bengaluru", course="BCA")
```

Output:

```text
Name: Asha
Role: Student
Details: {'city': 'Bengaluru', 'course': 'BCA'}
```

---

# 🔗 48. Combining Default Arguments With Other Function Features

A function can contain:

* Required parameters
* Default parameters
* `*args`
* `**kwargs`

Example:

```python
def report(name, department="Development", *skills, **details):
    print("Name:", name)
    print("Department:", department)
    print("Skills:", skills)
    print("Details:", details)
```

Call:

```python
report(
    "Neha",
    "Development",
    "Python",
    "SQL",
    city="Bengaluru",
    experience=2
)
```

Output:

```text
Name: Neha
Department: Development
Skills: ('Python', 'SQL')
Details: {'city': 'Bengaluru', 'experience': 2}
```

---

# ⚠️ 49. Common Mistake: Forgetting Required Arguments

Consider:

```python
def student(name, course="BCA"):
    print(name, course)
```

This is valid:

```python
student("Asha")
```

But this is invalid:

```python
student()
```

Python produces:

```text
TypeError: student() missing 1 required positional argument: 'name'
```

The default value exists only for `course`.

---

# ⚠️ 50. Common Mistake: Default Before Required Parameter

Incorrect:

```python
def student(course="BCA", name):
    print(name, course)
```

Python raises:

```text
SyntaxError: non-default argument follows default argument
```

Correct:

```python
def student(name, course="BCA"):
    print(name, course)
```

Remember:

```text
Required → Default
```

Not:

```text
Default → Required
```

---

# ⚠️ 51. Common Mistake: Expecting `None` to Mean No Argument

Consider:

```python
def greet(name="Guest"):
    print(name)

greet(None)
```

Output:

```text
None
```

The default `"Guest"` is **not** used.

Why?

Because an argument was actually provided:

```python
None
```

Default values are used only when the argument is omitted.

---

# ⚠️ 52. Common Mistake: Mutable Default Values

Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Prefer:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

This is one of the most important rules to remember about default arguments.

---

# 📊 53. Default Arguments Comparison

| Function                          | Call                     | Result         |
| --------------------------------- | ------------------------ | -------------- |
| `def greet(name="Guest")`         | `greet()`                | Uses `"Guest"` |
| `def greet(name="Guest")`         | `greet("Asha")`          | Uses `"Asha"`  |
| `def add(a, b=10)`                | `add(5)`                 | `15`           |
| `def add(a, b=10)`                | `add(5, 20)`             | `25`           |
| `def student(name, course="BCA")` | `student("Asha")`        | Uses `"BCA"`   |
| `def student(name, course="BCA")` | `student("Asha", "MCA")` | Uses `"MCA"`   |

---

# 🧮 54. Default Arguments With Return Values

Default arguments work normally with `return`.

```python
def calculate_bill(amount, tax=18):
    total = amount + (amount * tax / 100)
    return total

bill = calculate_bill(1000)

print("Bill:", bill)
```

Output:

```text
Bill: 1180.0
```

The default tax rate is applied automatically.

---

# 🧩 55. Default Arguments With Multiple Operations

```python
def calculate_salary(basic, bonus=5000, tax=10):
    gross = basic + bonus
    final_salary = gross - (gross * tax / 100)
    return final_salary

print(calculate_salary(30000))
```

Output:

```text
31500.0
```

Here:

```text
bonus = 5000
tax   = 10
```

are both default arguments.

---

# 🌍 56. Real-World Example: E-Commerce Order

```python
def create_order(product, quantity=1, delivery="Standard"):
    print("Product:", product)
    print("Quantity:", quantity)
    print("Delivery:", delivery)

create_order("Laptop")
```

Output:

```text
Product: Laptop
Quantity: 1
Delivery: Standard
```

Another order:

```python
create_order("Phone", 2, "Express")
```

Output:

```text
Product: Phone
Quantity: 2
Delivery: Express
```

---

# 🌍 57. Real-World Example: Student Result System

```python
def calculate_result(name, passing_marks=40):
    marks = {
        "Python": 85,
        "SQL": 72,
        "Git": 38
    }

    print("Student:", name)

    for subject, mark in marks.items():
        if mark >= passing_marks:
            print(subject, ":", "Pass")
        else:
            print(subject, ":", "Fail")

calculate_result("Asha")
```

Output:

```text
Student: Asha
Python : Pass
SQL : Pass
Git : Fail
```

The default passing mark is `40`.

---

# 🏆 58. Practice Programs

## 🟢 Easy

### Program 1: Greeting With Default Name

Create a function with a default name:

```text
Guest
```

Call the function without an argument.

Expected output:

```text
Hello Guest
```

---

### Program 2: Default Country

Create a function with:

```text
country="India"
```

Call the function without providing the country.

---

### Program 3: Default Age

Create a function that accepts a name and an age.

Set the default age to:

```text
18
```

Call the function with only the name.

---

### Program 4: Default Course

Create a function that accepts a student name and has:

```text
course="BCA"
```

Display both values.

---

## 🟡 Medium

### Program 5: Default Quantity

Create a shopping function:

```text
product
quantity=1
```

Call it once without quantity and once with quantity.

---

### Program 6: Default Discount

Create a function that accepts:

```text
price
discount=10
```

Calculate the final price.

---

### Program 7: Default Tax

Create a function with:

```text
amount
tax=18
```

Calculate and return the final amount.

---

### Program 8: Multiple Default Arguments

Create a function:

```text
student(name, course="BCA", semester=1)
```

Call it:

1. With only the name.
2. With name and course.
3. With all three arguments.

---

## 🔴 Advanced

### Program 9: Default Passing Marks

Create a student result function:

```text
name
passing_marks=40
```

Use a dictionary of subject marks and display whether each subject is Pass or Fail.

---

### Program 10: Employee Information

Create a function:

```text
employee(
    name,
    department="Development",
    status="Active"
)
```

Display all employee information.

Call the function with different combinations of arguments.

---

### Program 11: Shopping Cart

Create a function with:

```text
product
quantity=1
discount=0
```

Calculate the final price based on the quantity and discount.

---

### Program 12: Safe List Default

Create a function that adds a skill to a list.

Do **not** use:

```python
skills=[]
```

as the default value.

Instead, use:

```python
skills=None
```

and create a new list inside the function.

---

# 🏆 59. Challenge

Create a student registration function.

The function should accept:

```text
name
course="BCA"
semester=1
city="Bengaluru"
status="Active"
```

Then:

1. Display the student name.
2. Display the course.
3. Display the semester.
4. Display the city.
5. Display the status.
6. Call the function using only the name.
7. Call the function by changing the course.
8. Call the function by changing the semester.
9. Use keyword arguments to change only the city.
10. Use keyword arguments to change only the status.
11. Call the function with all values.
12. Observe which values come from the defaults.
13. Observe which values are overridden.

Example structure:

```python
def register_student(
    name,
    course="BCA",
    semester=1,
    city="Bengaluru",
    status="Active"
):
    # your code
```

Try solving the challenge without copying a complete solution.

---

# 🧪 60. Mini Project: E-Commerce Order System

Create an order function containing:

* Product name
* Quantity
* Price
* Discount
* Delivery type

Use the following defaults:

```text
quantity=1
discount=0
delivery="Standard"
```

Example:

```python
def create_order(
    product,
    price,
    quantity=1,
    discount=0,
    delivery="Standard"
):
    # your code
```

Perform the following operations:

* Display the product.
* Display the quantity.
* Calculate the subtotal.
* Apply the discount.
* Display the delivery type.
* Calculate the final price.
* Call the function without optional arguments.
* Call the function with a different quantity.
* Call the function with a discount.
* Use a keyword argument to change only the delivery type.
* Display the final order details.

### Your Goal

Build a complete order system that demonstrates how default arguments make a function flexible and reusable.

---

# 🎤 61. Interview Questions

* [ ] What are default arguments in Python?
* [ ] Why are default arguments used?
* [ ] How do you define a default argument?
* [ ] What happens if a default argument is not provided?
* [ ] Can a default argument be overridden?
* [ ] What is the syntax for a default argument?
* [ ] Can a function have multiple default arguments?
* [ ] Can a function have both required and default parameters?
* [ ] Where should default parameters be placed?
* [ ] What is the `non-default argument follows default argument` error?
* [ ] What is the difference between a required parameter and a default parameter?
* [ ] How can keyword arguments be used with default arguments?
* [ ] How can you skip a default argument?
* [ ] What happens if `None` is explicitly passed to a default parameter?
* [ ] When are default argument values evaluated?
* [ ] Why can mutable default arguments cause problems?
* [ ] Why is `None` commonly used instead of `[]` as a default?
* [ ] What are mutable default arguments?
* [ ] Can strings be used as default arguments?
* [ ] Can numbers be used as default arguments?
* [ ] Can Boolean values be used as default arguments?
* [ ] Can lists be used as default arguments?
* [ ] Can dictionaries be used as default arguments?
* [ ] Can sets be used as default arguments?
* [ ] How do default arguments work with `*args`?
* [ ] How do default arguments work with `**kwargs`?
* [ ] Give a real-world example of a default argument.

---

# 📝 62. Assignment

Complete the following programs.

### Task 1

Create a function with a default name:

```text
Guest
```

Call it without an argument.

---

### Task 2

Create a function with:

```text
country="India"
```

Call it with and without an argument.

---

### Task 3

Create a function that accepts:

```text
name
age=18
```

Display both values.

---

### Task 4

Create a function with:

```text
name
course="BCA"
semester=1
```

Call the function in three different ways.

---

### Task 5

Create a shopping function with:

```text
product
quantity=1
```

Calculate the total quantity.

---

### Task 6

Create a discount function with:

```text
price
discount=10
```

Calculate the final price.

---

### Task 7

Create a tax calculator with:

```text
amount
tax=18
```

Return the final amount.

---

### Task 8

Create an employee function with:

```text
name
department="Development"
status="Active"
```

Use keyword arguments to change only the status.

---

### Task 9

Create a function using:

```python
items=None
```

Add values to the list safely.

---

### Task 10

Create a function with two default arguments:

```text
bonus=5000
tax=10
```

Calculate the final salary.

---

### Task 11

Create a real-world function that uses at least four default arguments.

Use a suitable application such as:

```text
Shopping
Student Registration
Employee Management
Banking
Delivery
```

---

### Task 12

Create a function that uses:

* Required arguments
* Default arguments
* `*args`
* `**kwargs`

Call the function and display all the received information.

---

# 🧠 63. Memory Tricks

Remember:

```text
Default Argument
       ↓
Already Has a Value
       ↓
Argument Is Optional
```

---

Remember:

```text
No Argument
     ↓
Use Default
```

```text
Argument Provided
     ↓
Use Provided Value
```

---

Remember the parameter order:

```text
Required Parameters
        ↓
Default Parameters
```

Never:

```text
Default Parameters
        ↓
Required Parameters
```

---

Remember the mutable default rule:

```text
Avoid:

items=[]

Prefer:

items=None
```

---

Remember:

```text
def greet(name="Guest"):
             ↑
       Default Value
```

---

# 📌 64. Important Rules to Remember

```text
1. A default argument has a predefined value.

2. Default arguments make parameters optional.

3. If an argument is omitted, Python uses the default value.

4. If an argument is provided, the provided value overrides the default.

5. Default parameters are written using the = operator.

6. Required parameters must come before default parameters.

7. A default parameter cannot normally be followed by a required parameter.

8. Multiple default parameters are allowed.

9. Keyword arguments can be used to override specific default values.

10. Passing None is different from omitting an argument.

11. Default values are evaluated when the function is defined.

12. Mutable default arguments such as [] and {} can cause unexpected behavior.

13. Use None when you need a mutable object as a default.

14. Create the mutable object inside the function when the default is None.

15. Strings, numbers, Booleans, and None are commonly used as default values.

16. Default arguments can be used with calculations.

17. Default arguments can be used with loops.

18. Default arguments can be used with conditions.

19. Default arguments can be combined with *args and **kwargs.

20. Default arguments make functions reusable and flexible.
```

---

# 📊 65. Default Arguments Structure

```text
                         FUNCTION
                            │
                            ↓
                       PARAMETERS
                            │
                ┌───────────┴───────────┐
                ↓                       ↓
             REQUIRED                 DEFAULT
                │                       │
                │                  Has a value
                │                  automatically
                │                       │
                └───────────┬───────────┘
                            ↓
                     FUNCTION CALL
                            │
                     Argument provided?
                            │
                    ┌───────┴───────┐
                    ↓               ↓
                   YES              NO
                    ↓               ↓
              Use provided      Use default
                  value             value
```

---

# 📚 66. Complete Default Arguments Cheat Sheet

### Create a Default Argument

```python
def greet(name="Guest"):
    print(name)
```

### Call Without Argument

```python
greet()
```

### Override Default Value

```python
greet("Asha")
```

### Required + Default

```python
def student(name, course="BCA"):
    print(name, course)
```

### Multiple Defaults

```python
def student(name="Unknown", course="BCA"):
    print(name, course)
```

### Keyword Argument

```python
student(course="MCA")
```

### Safe Mutable Default

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
```

### Default Numeric Value

```python
def square(number=5):
    return number ** 2
```

### Default Boolean Value

```python
def account(active=True):
    print(active)
```

### Default String Value

```python
def message(text="Welcome"):
    print(text)
```

---

# 🏆 67. Default Arguments Mastery

```text
                         DEFAULT ARGUMENTS
                                │
                                ↓
                         Optional Parameters
                                │
              ┌─────────────────┴─────────────────┐
              ↓                                   ↓
        Argument Given                     Argument Omitted
              ↓                                   ↓
       Use Provided Value                    Use Default
              │                                   │
              └─────────────────┬─────────────────┘
                                ↓
                         Flexible Function
                                │
                ┌───────────────┼───────────────┐
                ↓               ↓               ↓
             Simple          Real World       Advanced
                ↓               ↓               ↓
             name="Guest"    tax=18        items=None
             age=18          quantity=1     *args
             course="BCA"    status="Active" **kwargs
```

---

# 📚 68. Summary

In this lesson, you learned:

* What default arguments are.
* Why default arguments are used.
* How to define default arguments.
* How to call functions without optional arguments.
* How to override default values.
* How to use multiple default arguments.
* The difference between required and default parameters.
* The correct order of function parameters.
* How to use positional arguments with default arguments.
* How to use keyword arguments with default arguments.
* How to skip a default argument using keyword arguments.
* How default arguments work with numbers.
* How default arguments work with strings.
* How default arguments work with Boolean values.
* How default arguments work with `None`.
* How default arguments work with calculations.
* How default arguments work with loops.
* How default arguments work with conditions.
* The mutable default argument problem.
* Why `None` is commonly used for mutable defaults.
* How to safely use lists as default parameters.
* How to safely use dictionaries as default parameters.
* How to safely use sets as default parameters.
* How default arguments work with `*args`.
* How default arguments work with `**kwargs`.
* How to use default arguments in real-world applications.
* Common mistakes when using default arguments.
* How default arguments make functions flexible and reusable.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what default arguments are.
* [ ] I know why default arguments are used.
* [ ] I can create a function with a default argument.
* [ ] I can call a function without providing a default argument.
* [ ] I can override a default value.
* [ ] I understand required and default parameters.
* [ ] I understand the correct order of parameters.
* [ ] I can use multiple default arguments.
* [ ] I can use positional arguments with defaults.
* [ ] I can use keyword arguments with defaults.
* [ ] I can skip a default argument using a keyword argument.
* [ ] I understand how default values are evaluated.
* [ ] I understand the mutable default argument problem.
* [ ] I know why `None` is used for mutable defaults.
* [ ] I can safely use a list inside a function.
* [ ] I can safely use a dictionary inside a function.
* [ ] I can safely use a set inside a function.
* [ ] I can use default arguments with calculations.
* [ ] I can use default arguments with loops.
* [ ] I can use default arguments with conditions.
* [ ] I can combine default arguments with `*args`.
* [ ] I can combine default arguments with `**kwargs`.
* [ ] I can use default arguments in real-world programs.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use default arguments without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Keyword Arguments**

In the next topic, you will learn:

* What keyword arguments are.
* Why keyword arguments are useful.
* Positional arguments vs keyword arguments.
* How to pass arguments using parameter names.
* Using keyword arguments with multiple parameters.
* Mixing positional and keyword arguments.
* Rules for mixing positional and keyword arguments.
* Using keyword arguments with default arguments.
* Skipping parameters using keyword arguments.
* Improving function readability with keyword arguments.
* Using keyword arguments in real-world functions.
* Using keyword arguments with `*args` and `**kwargs`.
* Common mistakes with keyword arguments.
* Practice programs.
* Real-world examples.
* Advanced keyword argument techniques.
* Challenges and mini projects.

---

## ⭐ Quote of the Day

> **"Default arguments make functions flexible by giving them useful values when no specific value is provided."** 🐍📚
