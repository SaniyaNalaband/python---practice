# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 13: Global Variables

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what global variables are.
* [ ] Understand the scope of a variable.
* [ ] Understand where global variables are created.
* [ ] Access global variables inside functions.
* [ ] Understand local variables vs global variables.
* [ ] Understand the `global` keyword.
* [ ] Modify global variables inside functions.
* [ ] Create global variables outside functions.
* [ ] Understand what happens when local and global variables have the same name.
* [ ] Understand variable lookup inside functions.
* [ ] Use global variables in real-world applications.
* [ ] Avoid common mistakes with global variables.
* [ ] Understand why excessive use of global variables can be problematic.
* [ ] Combine global variables with functions, loops, and conditions.
* [ ] Understand best practices for using global variables.

---

# 📖 1. What is a Global Variable?

A **global variable** is a variable that is created outside of all functions and can generally be accessed from different parts of the program.

Example:

```python
name = "Asha"

def display():
    print(name)

display()
```

Output:

```text
Asha
```

Here:

```text
name = "Asha"
```

is a global variable because it is created outside the function.

The function `display()` can access it.

---

# 🌍 2. Why is it Called a Global Variable?

It is called **global** because its scope is not limited to a single function.

Example:

```python
course = "Python"

def first():
    print(course)

def second():
    print(course)

first()
second()
```

Output:

```text
Python
Python
```

The same global variable can be accessed by both functions.

---

# 🧠 3. Where is a Global Variable Created?

A global variable is created outside a function.

Example:

```python
language = "Python"

def show_language():
    print(language)
```

Here:

```text
language
   ↓
Created outside function
   ↓
Global variable
```

The function can access it because it exists in the global scope.

---

# 📚 4. Global Scope

**Global scope** means the part of a program where a variable can be accessed globally.

Example:

```python
college = "ABC College"

print(college)

def show():
    print(college)

show()
```

Output:

```text
ABC College
ABC College
```

The variable `college` is available both outside and inside the function.

---

# 🔍 5. Accessing a Global Variable Inside a Function

A function can normally read a global variable without using the `global` keyword.

Example:

```python
language = "Python"

def display():
    print(language)

display()
```

Output:

```text
Python
```

The function is only **reading** the global variable.

---

# 🧠 6. Global Variable with Multiple Functions

The same global variable can be accessed by multiple functions.

Example:

```python
company = "Tech Solutions"

def show_company():
    print(company)

def display_company():
    print("Company:", company)

show_company()
display_company()
```

Output:

```text
Tech Solutions
Company: Tech Solutions
```

Both functions can read the same global variable.

---

# 🔄 7. Global Variable Outside and Inside a Function

Consider:

```python
score = 100

def show():
    print(score)

print(score)
show()
```

Output:

```text
100
100
```

The global variable `score` is accessible both outside and inside the function.

---

# ⚖️ 8. Global Variable vs Local Variable

A **global variable** is created outside a function.

A **local variable** is created inside a function.

Example:

```python
course = "Python"

def student():
    name = "Asha"
    print(course)
    print(name)

student()
```

Here:

```text
course
   ↓
Global variable

name
   ↓
Local variable
```

---

# 📊 9. Global vs Local Variables

| Variable        | Created          | Scope          |
| --------------- | ---------------- | -------------- |
| Global variable | Outside function | Global scope   |
| Local variable  | Inside function  | Function scope |

Example:

```python
course = "Python"

def student():
    name = "Asha"
    print(course)
    print(name)
```

`course` is global.

`name` is local.

---

# 🧩 10. Local Variable Cannot Normally Be Accessed Outside Its Function

Example:

```python
def student():
    name = "Asha"
    print(name)

student()

print(name)
```

The first `print()` works.

But the second `print()` produces:

```text
NameError
```

because `name` is a local variable.

Its scope is limited to the function.

---

# 🌍 11. Global Variable Can Be Accessed Outside the Function

Example:

```python
name = "Asha"

def student():
    print(name)

student()

print(name)
```

Output:

```text
Asha
Asha
```

The variable `name` is global, so it can be accessed from both locations.

---

# 🧠 12. Same Variable Name in Global and Local Scope

A local variable can have the same name as a global variable.

Example:

```python
name = "Asha"

def student():
    name = "Neha"
    print(name)

student()

print(name)
```

Output:

```text
Neha
Asha
```

Why?

Inside the function, Python uses the local variable.

Outside the function, Python uses the global variable.

---

# 🔎 13. Understanding Variable Shadowing

When a local variable has the same name as a global variable, the local variable **shadows** the global variable inside that function.

Example:

```python
status = "Active"

def account():
    status = "Inactive"
    print(status)

account()

print(status)
```

Output:

```text
Inactive
Active
```

Inside the function:

```text
status → local variable
```

Outside the function:

```text
status → global variable
```

---

# 🔑 14. The `global` Keyword

The `global` keyword is used inside a function when you want to modify a global variable.

Syntax:

```python
global variable_name
```

Example:

```python
count = 0

def increase():
    global count
    count += 1

increase()

print(count)
```

Output:

```text
1
```

The `global` keyword tells Python that `count` refers to the global variable.

---

# ⚙️ 15. Why Do We Need the `global` Keyword?

Consider:

```python
count = 10

def increase():
    count = count + 1

increase()
```

This produces an error because Python treats `count` inside the function as a local variable.

Python sees:

```python
count = count + 1
```

and assumes that `count` is local to the function.

But the right-hand side tries to use that local variable before it has been assigned.

Therefore, we use:

```python
global count
```

---

# 🔄 16. Modifying a Global Variable

Example:

```python
balance = 5000

def deposit():
    global balance
    balance += 1000

deposit()

print(balance)
```

Output:

```text
6000
```

The function modifies the global variable `balance`.

---

# ➕ 17. Adding to a Global Variable

Example:

```python
total = 0

def add_amount():
    global total
    total += 500

add_amount()
add_amount()

print(total)
```

Output:

```text
1000
```

The same global variable is modified each time the function is called.

---

# ➖ 18. Decreasing a Global Variable

Example:

```python
stock = 20

def sell():
    global stock
    stock -= 1

sell()
sell()

print(stock)
```

Output:

```text
18
```

The global variable `stock` is changed by the function.

---

# 🔁 19. Updating a Global Variable Multiple Times

Example:

```python
score = 0

def add_score(points):
    global score
    score += points

add_score(10)
add_score(20)
add_score(15)

print(score)
```

Output:

```text
45
```

Each function call modifies the same global variable.

---

# 🧠 20. Global Keyword Does Not Create the Variable

The `global` keyword does not mean "create a new global variable."

It tells Python that a variable inside the function refers to a variable in the global scope.

Example:

```python
count = 10

def update():
    global count
    count = 20

update()

print(count)
```

Output:

```text
20
```

The existing global variable `count` was modified.

---

# ⚖️ 21. Reading vs Modifying a Global Variable

There is an important difference.

### Reading

You normally do not need `global`.

```python
price = 500

def show():
    print(price)
```

### Modifying

You need `global` when assigning to the global variable inside the function.

```python
price = 500

def update():
    global price
    price = 600
```

Remember:

```text
Read global variable
       ↓
global keyword usually not required

Modify global variable
       ↓
global keyword required
```

---

# 🔍 22. Global Variable with `if`

Global variables can be used with conditions.

Example:

```python
temperature = 35

def check_weather():
    if temperature > 30:
        print("Hot weather")
    else:
        print("Cool weather")

check_weather()
```

Output:

```text
Hot weather
```

The function reads the global variable `temperature`.

---

# 🔁 23. Global Variable with Loops

Example:

```python
count = 0

def count_numbers():
    global count

    for i in range(1, 6):
        count += 1

count_numbers()

print(count)
```

Output:

```text
5
```

The loop modifies the global variable through the function.

---

# 🧮 24. Global Variable for Calculations

Example:

```python
total = 0

def add_price(price):
    global total
    total += price

add_price(1000)
add_price(500)
add_price(250)

print("Total:", total)
```

Output:

```text
Total: 1750
```

---

# 🌍 25. Real-World Example: Shopping Cart

A global variable can represent the cart total.

```python
cart_total = 0

def add_item(price):
    global cart_total
    cart_total += price

add_item(1200)
add_item(800)
add_item(500)

print("Cart Total:", cart_total)
```

Output:

```text
Cart Total: 2500
```

---

# 🌍 26. Real-World Example: Bank Balance

Example:

```python
balance = 10000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    balance -= amount

deposit(2000)
withdraw(1500)

print("Balance:", balance)
```

Output:

```text
Balance: 10500
```

---

# 🌍 27. Real-World Example: Game Score

Example:

```python
score = 0

def add_points(points):
    global score
    score += points

add_points(100)
add_points(50)
add_points(200)

print("Score:", score)
```

Output:

```text
Score: 350
```

---

# 🌍 28. Real-World Example: Login Status

Example:

```python
logged_in = False

def login():
    global logged_in
    logged_in = True

login()

print("Logged in:", logged_in)
```

Output:

```text
Logged in: True
```

---

# 🌍 29. Real-World Example: Employee Count

Example:

```python
employee_count = 0

def add_employee():
    global employee_count
    employee_count += 1

add_employee()
add_employee()
add_employee()

print("Employees:", employee_count)
```

Output:

```text
Employees: 3
```

---

# 🌍 30. Real-World Example: Website Visitors

Example:

```python
visitors = 0

def visit():
    global visitors
    visitors += 1

visit()
visit()
visit()
visit()

print("Visitors:", visitors)
```

Output:

```text
Visitors: 4
```

---

# 🧠 31. Global Constants

Global variables are also commonly used for values that should remain unchanged.

These are often written using uppercase letters.

Example:

```python
PI = 3.14159
MAX_USERS = 100
COMPANY_NAME = "Tech Solutions"
```

These are commonly treated as **constants by convention**.

Python does not actually prevent you from changing them.

---

# 📐 32. Global Constant in a Function

Example:

```python
PI = 3.14159

def area(radius):
    return PI * radius * radius

print(area(5))
```

Output:

```text
78.53975
```

The function reads the global constant `PI`.

---

# ⚠️ 33. Global Variables Can Be Changed Accidentally

Because global variables can be accessed from many places, they can sometimes be changed unintentionally.

Example:

```python
score = 100

def game():
    global score
    score = 0

game()

print(score)
```

Output:

```text
0
```

The original value was changed.

This is one reason excessive use of global variables is discouraged.

---

# ⚠️ 34. Common Mistake: Forgetting `global`

Wrong:

```python
count = 0

def increase():
    count += 1

increase()
```

This produces:

```text
UnboundLocalError
```

Correct:

```python
count = 0

def increase():
    global count
    count += 1

increase()
```

Now the global variable can be modified.

---

# ⚠️ 35. Common Mistake: Assuming Local and Global Variables Are the Same

Example:

```python
value = 10

def change():
    value = 20
    print(value)

change()

print(value)
```

Output:

```text
20
10
```

The local variable does not change the global variable.

---

# ⚠️ 36. Common Mistake: Using `global` Unnecessarily

You do not need `global` just to read a global variable.

Unnecessary:

```python
name = "Asha"

def show():
    global name
    print(name)
```

Better:

```python
name = "Asha"

def show():
    print(name)
```

Use `global` when you actually need to assign to the global variable.

---

# ⚖️ 37. Global Variable vs Local Variable

| Feature                                   | Global Variable                           | Local Variable            |
| ----------------------------------------- | ----------------------------------------- | ------------------------- |
| Created                                   | Outside function                          | Inside function           |
| Scope                                     | Global                                    | Function                  |
| Accessible inside function                | Usually yes                               | Yes                       |
| Accessible outside function               | Yes                                       | No                        |
| Requires `global` to read                 | No                                        | No                        |
| Requires `global` to modify from function | Yes                                       | No                        |
| Lifetime                                  | Generally while program/module is running | During function execution |

---

# 🧩 38. Global Variable vs Function Parameter

A function parameter is local to the function.

Example:

```python
name = "Asha"

def display(name):
    print(name)

display("Neha")

print(name)
```

Output:

```text
Neha
Asha
```

The parameter `name` is local.

The global `name` remains unchanged.

---

# 🔄 39. Using Global Variables with Function Parameters

Example:

```python
total = 0

def add(number):
    global total
    total += number

add(10)
add(20)

print(total)
```

Output:

```text
30
```

Here:

```text
number → local parameter
total  → global variable
```

---

# 🧠 40. Function Parameters Are Usually Better Than Global State

Instead of:

```python
total = 0

def add():
    global total
    total += 100
```

you can often use:

```python
def add(total):
    return total + 100

total = 0
total = add(total)

print(total)
```

This makes the function easier to understand and test.

---

# 🔍 41. Understanding Global Variable Lookup

When Python encounters a variable inside a function, it first looks for a local variable.

Example:

```python
language = "Python"

def show():
    language = "Java"
    print(language)

show()
```

Python finds:

```text
Local language
      ↓
"Java"
```

So it prints:

```text
Java
```

---

# 🧠 42. LEGB Rule

Python follows the **LEGB rule** when looking for names.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

The order is:

```text
Local
  ↓
Enclosing
  ↓
Global
  ↓
Built-in
```

Example:

```python
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()
```

Output:

```text
Local
```

Python finds the local variable first.

---

# 🔗 43. Global Scope and Built-in Scope

If Python cannot find a variable locally or globally, it can look in the built-in namespace.

Example:

```python
def show():
    print(len("Python"))

show()
```

Here `len()` is a built-in function.

The simplified lookup order is:

```text
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
```

---

# 🧪 44. Checking Global Variables with `globals()`

Python provides the built-in `globals()` function.

It returns a dictionary representing the current global namespace.

Example:

```python
course = "Python"

print(globals()["course"])
```

Output:

```text
Python
```

`globals()` can be useful for understanding how Python stores global names.

---

# 🧠 45. Global Variables and Mutable Objects

A global variable can refer to a mutable object such as a list.

Example:

```python
students = []

def add_student(name):
    students.append(name)

add_student("Asha")
add_student("Neha")

print(students)
```

Output:

```text
['Asha', 'Neha']
```

Notice that `global` is not required here.

Why?

The function is modifying the list object, not assigning a new object to the variable `students`.

---

# ⚖️ 46. Mutating vs Reassigning a Global Variable

This distinction is important.

### Mutating the object

```python
students = []

def add_student(name):
    students.append(name)
```

No `global` is required.

### Reassigning the variable

```python
students = []

def reset():
    global students
    students = []
```

Here `global` is required because the variable itself is being reassigned.

Remember:

```text
Modify object
     ↓
global usually not required

Reassign global variable
     ↓
global required
```

---

# 🔄 47. Global Dictionary Inside a Function

Example:

```python
student = {
    "name": "Asha",
    "age": 20
}

def update_student():
    student["age"] = 21

update_student()

print(student)
```

Output:

```text
{'name': 'Asha', 'age': 21}
```

The dictionary is modified without using `global`.

---

# 🧠 48. Reassigning a Global Dictionary

Example:

```python
student = {
    "name": "Asha"
}

def reset_student():
    global student
    student = {}

reset_student()

print(student)
```

Output:

```text
{}
```

Here the variable `student` is reassigned, so `global` is required.

---

# ⚠️ 49. Why Too Many Global Variables Can Be Problematic

Using many global variables can make a program difficult to maintain.

Problems include:

* [ ] Accidental modification.
* [ ] Difficult debugging.
* [ ] Difficult testing.
* [ ] Functions becoming dependent on outside data.
* [ ] Unexpected changes from other parts of the program.
* [ ] Reduced code readability.
* [ ] Increased coupling between functions.

For small programs, global variables can be convenient.

For larger programs, parameters, return values, classes, and other structured approaches are often better.

---

# 🏗️ 50. Better Alternative: Function Parameters

Instead of relying heavily on global variables:

```python
tax_rate = 0.18

def calculate_tax(price):
    return price * tax_rate
```

You can make the dependency explicit:

```python
def calculate_tax(price, tax_rate):
    return price * tax_rate

print(calculate_tax(1000, 0.18))
```

This makes the function more independent.

---

# 🏆 51. Real-World Example: Shopping Cart

Using a global variable:

```python
cart_total = 0

def add_product(price):
    global cart_total
    cart_total += price

add_product(1500)
add_product(800)
add_product(700)

print("Cart Total:", cart_total)
```

Output:

```text
Cart Total: 3000
```

The global variable stores the current cart total.

---

# 🏆 52. Real-World Example: Game Score

```python
score = 0

def score_points(points):
    global score
    score += points

score_points(50)
score_points(100)
score_points(25)

print("Final Score:", score)
```

Output:

```text
Final Score: 175
```

---

# 🏆 53. Real-World Example: Inventory

```python
stock = 50

def sell(quantity):
    global stock
    stock -= quantity

sell(5)
sell(10)

print("Remaining Stock:", stock)
```

Output:

```text
Remaining Stock: 35
```

---

# 🏆 54. Real-World Example: Website Visitors

```python
visitor_count = 0

def new_visit():
    global visitor_count
    visitor_count += 1

for i in range(5):
    new_visit()

print("Visitors:", visitor_count)
```

Output:

```text
Visitors: 5
```

---

# 📊 55. Global Variables Structure

```text
                         VARIABLES
                             │
              ┌──────────────┴──────────────┐
              ↓                             ↓
           GLOBAL                         LOCAL
              │                             │
       Outside function              Inside function
              │                             │
              ↓                             ↓
     Accessible globally          Limited to function
              │
              ↓
       Can be read inside
         functions
              │
              ↓
    Use global keyword to
      modify/reassign
```

---

# 🧠 56. Global Keyword Structure

```text
                    global variable
                          │
                          ↓
                 Used inside function
                          │
             ┌────────────┴────────────┐
             ↓                         ↓
          Read only                Modify
             │                         │
             ↓                         ↓
       global usually            global keyword
       not required               required
```

---

# 📚 57. Global Variables Cheat Sheet

### Create a Global Variable

```python
name = "Asha"
```

### Read a Global Variable Inside a Function

```python
def show():
    print(name)
```

### Modify a Global Variable

```python
count = 0

def increase():
    global count
    count += 1
```

### Reassign a Global Variable

```python
status = "Inactive"

def activate():
    global status
    status = "Active"
```

### Local Variable with Same Name

```python
name = "Asha"

def show():
    name = "Neha"
    print(name)
```

### Global Constant by Convention

```python
PI = 3.14159
MAX_USERS = 100
```

---

# 📊 58. Global vs Local vs Parameter

| Feature                          | Global      | Local    | Parameter |
| -------------------------------- | ----------- | -------- | --------- |
| Created outside function         | ✅           | ❌        | ❌         |
| Created inside function          | ❌           | ✅        | ✅         |
| Scope                            | Global      | Function | Function  |
| Passed into function             | ❌           | ❌        | ✅         |
| Can be accessed inside function  | Usually yes | Yes      | Yes       |
| Accessible outside function      | Yes         | No       | No        |
| `global` needed for reassignment | Yes         | No       | No        |

---

# ⚠️ 59. Common Mistakes

### Mistake 1: Forgetting `global`

```python
count = 0

def increase():
    count += 1
```

Correct:

```python
def increase():
    global count
    count += 1
```

---

### Mistake 2: Thinking Local Changes Global

```python
value = 10

def change():
    value = 20

change()

print(value)
```

Output:

```text
10
```

The local variable did not change the global variable.

---

### Mistake 3: Using `global` for Reading

Unnecessary:

```python
name = "Asha"

def show():
    global name
    print(name)
```

Better:

```python
def show():
    print(name)
```

---

### Mistake 4: Using Too Many Global Variables

Avoid creating a large number of global variables when function parameters and return values can be used instead.

---

# 🧪 60. Practice Programs

## 🟢 Easy

### Program 1: Access a Global Variable

```python
name = "Asha"

def display():
    print(name)

display()
```

---

### Program 2: Display a Global Course

```python
course = "Python"

def show_course():
    print(course)

show_course()
```

---

### Program 3: Use a Global Variable in a Condition

```python
marks = 85

def check_marks():
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

check_marks()
```

---

### Program 4: Use a Global Variable in a Loop

```python
limit = 5

def display_numbers():
    for i in range(1, limit + 1):
        print(i)

display_numbers()
```

---

# 🟡 Medium

### Program 5: Modify a Global Counter

```python
count = 0

def increase():
    global count
    count += 1

increase()
increase()
increase()

print(count)
```

---

### Program 6: Modify a Global Score

```python
score = 0

def add_score(points):
    global score
    score += points

add_score(20)
add_score(30)

print(score)
```

---

### Program 7: Modify a Global Balance

```python
balance = 5000

def deposit(amount):
    global balance
    balance += amount

deposit(1000)

print(balance)
```

---

### Program 8: Local and Global Variables with the Same Name

```python
city = "Bengaluru"

def show_city():
    city = "Mysuru"
    print(city)

show_city()

print(city)
```

---

# 🔴 Advanced

## Program 9: Global Shopping Cart Total

```python
cart_total = 0

def add_item(price):
    global cart_total
    cart_total += price

add_item(1500)
add_item(2500)
add_item(1000)

print("Total:", cart_total)
```

---

## Program 10: Global Inventory Management

```python
stock = 100

def sell(quantity):
    global stock

    if quantity <= stock:
        stock -= quantity
        print("Sale completed")
    else:
        print("Insufficient stock")

sell(20)
sell(30)

print("Remaining:", stock)
```

---

## Program 11: Global Game Score

```python
score = 0

def add_points(points):
    global score
    score += points

def display_score():
    print("Score:", score)

add_points(50)
add_points(100)
display_score()
```

---

## Program 12: Global Visitor Counter

```python
visitors = 0

def visit():
    global visitors
    visitors += 1

for i in range(10):
    visit()

print("Visitors:", visitors)
```

---

# 🏆 61. Challenge

Create a program for a simple **Bank Account System**.

Create a global variable:

```text
balance
```

Set its initial value.

Then create functions for:

1. Displaying the balance.
2. Depositing money.
3. Withdrawing money.
4. Checking whether sufficient balance exists.
5. Updating the global balance using `global`.
6. Performing multiple transactions.
7. Displaying the final balance.

Example starting data:

```python
balance = 10000
```

Try solving the challenge without copying the solution.

---

# 🧪 62. Mini Project: Game Score Management System

Create a small game score system using a global variable.

Start with:

```python
score = 0
```

Create functions to:

* Add points.
* Remove points.
* Display the current score.
* Reset the score.
* Add points using user input.
* Display the final score.

Your program should demonstrate the use of:

```text
global
functions
parameters
if
input()
```

### Your Goal

Build a complete score management program using global variables and functions.

---

# 🎤 63. Interview Questions

* [ ] What is a global variable in Python?
* [ ] Where is a global variable created?
* [ ] What is global scope?
* [ ] Can a function access a global variable?
* [ ] Is the `global` keyword required to read a global variable?
* [ ] When is the `global` keyword required?
* [ ] What happens if you try to modify a global variable without `global`?
* [ ] What is the difference between a global variable and a local variable?
* [ ] What happens when a local and global variable have the same name?
* [ ] What is variable shadowing?
* [ ] What is the purpose of the `global` keyword?
* [ ] Can a global list be modified inside a function without `global`?
* [ ] What is the difference between mutating and reassigning a global object?
* [ ] What is the LEGB rule?
* [ ] Why should excessive use of global variables be avoided?
* [ ] What are global constants?
* [ ] Can a function parameter have the same name as a global variable?
* [ ] What is the difference between a global variable and a function parameter?
* [ ] How can `globals()` be used?
* [ ] What are better alternatives to excessive global variables?

---

# 📝 64. Assignment

Complete the following programs.

### Task 1

Create a global variable containing:

```text
name
```

Create a function that displays it.

---

### Task 2

Create a global variable:

```text
course = "Python"
```

Create a function that prints the course.

---

### Task 3

Create a global variable containing marks.

Use a function and `if` to determine whether the student has passed.

---

### Task 4

Create a global counter starting at `0`.

Create a function that increases the counter by `1`.

Call the function five times.

---

### Task 5

Create a global variable:

```text
balance
```

Create a function that deposits money into the account.

---

### Task 6

Create a global variable containing stock quantity.

Create a function that decreases the stock when a product is sold.

---

### Task 7

Create a global variable called `score`.

Create a function that adds points to the score.

---

### Task 8

Create a global variable and a local variable with the same name.

Observe which value is printed inside and outside the function.

---

### Task 9

Create a global list of programming skills.

Create a function that adds a new skill to the list.

---

### Task 10

Create a global dictionary containing student information.

Create a function that modifies one of its values.

---

### Task 11

Create a real-world program that uses at least three global variables and three functions.

---

### Task 12

Create a program that demonstrates the difference between:

```text
Reading a global variable
```

and:

```text
Modifying a global variable
```

Use the `global` keyword where required.

---

# 🧠 65. Memory Tricks

Remember:

```text
GLOBAL VARIABLE
       ↓
Created outside function
       ↓
Can be accessed inside function
```

---

Remember:

```text
READ GLOBAL
     ↓
Usually no global keyword
```

---

Remember:

```text
MODIFY / REASSIGN GLOBAL
          ↓
    Use global keyword
```

---

Remember:

```text
GLOBAL
  ↓
Outside function

LOCAL
  ↓
Inside function
```

---

Remember the quick rule:

```text
Read       → No global usually needed
Modify     → global
Reassign   → global
```

---

# 📌 66. Important Rules to Remember

```text
1. A global variable is created outside a function.

2. Global variables belong to the global scope.

3. A function can normally read a global variable.

4. The global keyword is usually not required just to read a global variable.

5. The global keyword is required when assigning to a global variable from inside a function.

6. A local variable is created inside a function.

7. A local variable is normally accessible only inside its function.

8. A local variable can have the same name as a global variable.

9. A local variable with the same name can shadow the global variable.

10. Function parameters are local to the function.

11. A global list can often be mutated inside a function without using global.

12. Reassigning a global variable requires global inside the function.

13. Excessive use of global variables can make programs harder to maintain.

14. Function parameters and return values are often better alternatives.

15. Global constants are commonly written using uppercase names.

16. Python follows the LEGB rule when resolving names.

17. LEGB means Local, Enclosing, Global, and Built-in.

18. Global variables can be useful for shared configuration or program-wide state.
```

---

# 📊 67. Global Variables Structure

```text
                         FUNCTIONS
                             │
                             ↓
                         VARIABLES
                             │
              ┌──────────────┴──────────────┐
              ↓                             ↓
           GLOBAL                         LOCAL
              │                             │
       Outside function              Inside function
              │                             │
              ↓                             ↓
      Read inside function          Function-specific
              │                             │
              ↓                             ↓
      global usually not needed       Cannot normally
             for reading              be accessed outside
              │
              ↓
      Modify / Reassign
              │
              ↓
        global keyword
```

---

# 📚 68. Complete Global Variables Cheat Sheet

### Create a Global Variable

```python
name = "Asha"
```

### Access a Global Variable

```python
def show():
    print(name)
```

### Modify a Global Variable

```python
count = 0

def increase():
    global count
    count += 1
```

### Reassign a Global Variable

```python
status = "Inactive"

def activate():
    global status
    status = "Active"
```

### Create a Local Variable

```python
def student():
    name = "Asha"
```

### Use a Global Constant

```python
PI = 3.14159
```

### Mutate a Global List

```python
skills = []

def add_skill(skill):
    skills.append(skill)
```

### Reassign a Global List

```python
skills = []

def reset():
    global skills
    skills = []
```

### Check Global Namespace

```python
print(globals())
```

---

# 🏆 69. Global Variables Mastery

```text
                         VARIABLES
                             │
                             ↓
                    Variable Scope
                             │
             ┌───────────────┴───────────────┐
             ↓                               ↓
          GLOBAL                           LOCAL
             │                               │
      Outside function                Inside function
             │                               │
             ↓                               ↓
        Read in function             Function-specific
             │
             ↓
      Modify / Reassign
             │
             ↓
       global keyword
             │
             ↓
      Shared program state
```

---

# 📚 70. Summary

In this lesson, you learned:

* What global variables are.
* Where global variables are created.
* What global scope means.
* How functions access global variables.
* The difference between global and local variables.
* How local variables can shadow global variables.
* What the `global` keyword does.
* When the `global` keyword is required.
* How to modify global variables inside functions.
* The difference between reading and modifying global variables.
* How global variables work with conditions.
* How global variables work with loops.
* How global variables work with lists and dictionaries.
* The difference between mutating and reassigning global objects.
* What global constants are.
* What the LEGB rule means.
* How `globals()` can be used.
* Why excessive global variables can cause problems.
* How function parameters can reduce dependence on global variables.
* How to use global variables in real-world applications.
* Common mistakes when using global variables.
* How to build programs using global variables and functions.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what a global variable is.
* [ ] I know where global variables are created.
* [ ] I understand global scope.
* [ ] I can access a global variable inside a function.
* [ ] I understand local variables.
* [ ] I understand global vs local variables.
* [ ] I understand variable shadowing.
* [ ] I understand the `global` keyword.
* [ ] I know when to use `global`.
* [ ] I can modify a global variable inside a function.
* [ ] I can use global variables with conditions.
* [ ] I can use global variables with loops.
* [ ] I understand global variables with lists.
* [ ] I understand global variables with dictionaries.
* [ ] I understand mutation vs reassignment.
* [ ] I understand the LEGB rule.
* [ ] I understand global constants.
* [ ] I know the disadvantages of excessive global variables.
* [ ] I can use function parameters instead of unnecessary global state.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use global variables without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Local Variables**

In the next topic, you will learn:

* What local variables are.
* Where local variables are created.
* Local variable scope.
* Accessing local variables inside functions.
* Why local variables cannot normally be accessed outside functions.
* Local variables with function parameters.
* Local variables with conditions.
* Local variables with loops.
* Local variables in nested functions.
* Local vs global variables.
* Variable shadowing.
* Scope and lifetime of local variables.
* Real-world examples.
* Common mistakes.
* Practice programs.
* Challenges.

---

## ⭐ Quote of the Day

> **"Understanding variable scope is the key to understanding how Python manages data inside and outside functions."** 🐍📚
