# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 1: Defining Functions

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what a function is.
* [ ] Understand why functions are used.
* [ ] Understand the difference between built-in and user-defined functions.
* [ ] Understand how to define a function.
* [ ] Understand the syntax of a function.
* [ ] Understand the `def` keyword.
* [ ] Understand function names.
* [ ] Understand function bodies.
* [ ] Understand indentation in functions.
* [ ] Understand how function definitions work.
* [ ] Create simple user-defined functions.
* [ ] Create functions for real-world tasks.
* [ ] Understand function documentation using docstrings.
* [ ] Understand local variables inside functions.
* [ ] Understand global variables at a basic level.
* [ ] Understand how functions improve code reusability.
* [ ] Avoid common mistakes when defining functions.
* [ ] Build reusable programs using functions.

---

# 📖 1. What is a Function?

A **function** is a reusable block of code designed to perform a specific task.

Instead of writing the same code again and again, we can place that code inside a function and reuse it whenever required.

Example:

```python
def greet():
    print("Hello!")
```

Here:

```text
def     → keyword used to define a function
greet   → function name
()      → parameter list
:       → starts the function body
```

The function contains:

```python
print("Hello!")
```

which is the code that performs the task.

---

# 🧠 2. Why Do We Use Functions?

Functions are useful because they make programs:

* Easier to understand.
* Easier to maintain.
* Easier to test.
* Easier to debug.
* More organized.
* More reusable.
* Less repetitive.

Without a function:

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

With a function:

```python
def welcome():
    print("Welcome to Python")
```

The same task can then be reused whenever needed.

---

# 🔄 3. Code Reusability

One of the biggest advantages of functions is **code reusability**.

Suppose you need to display a welcome message many times.

Instead of repeating:

```python
print("Welcome to the course")
```

you can define:

```python
def welcome():
    print("Welcome to the course")
```

Now the same function can be reused throughout the program.

This follows an important programming principle:

```text
Write Once
    ↓
Reuse Many Times
```

---

# 🏗️ 4. Defining a Function

A function is defined using the `def` keyword.

Example:

```python
def greet():
    print("Hello!")
```

This is called a **function definition**.

Important:

Defining a function does not execute the function body immediately.

It only tells Python:

> "Create a function named `greet` containing this code."

---

# 🧩 5. Basic Function Syntax

The general syntax is:

```python
def function_name():
    # function body
```

Example:

```python
def calculate():
    print("Calculating...")
```

The structure is:

```text
def
 ↓
function_name
 ↓
()
 ↓
:
 ↓
indented function body
```

---

# 🔑 6. The `def` Keyword

The `def` keyword is used to define a function in Python.

Example:

```python
def display_message():
    print("Python is powerful")
```

Here:

```text
def → tells Python that a function is being defined
```

Without `def`, Python will not recognize the statement as a function definition.

---

# 🏷️ 7. Function Name

A function must have a name.

Example:

```python
def greet():
    print("Hello")
```

Here:

```text
greet
```

is the function name.

A function name should describe what the function does.

Good names:

```python
def calculate_total():
    pass

def display_student():
    pass

def check_password():
    pass

def calculate_average():
    pass
```

Poor names:

```python
def abc():
    pass

def x():
    pass

def something():
    pass
```

Descriptive names make programs easier to understand.

---

# 📏 8. Rules for Function Names

Function names follow Python's identifier rules.

A function name:

* Can contain letters.
* Can contain numbers.
* Can contain underscores.
* Cannot start with a number.
* Cannot contain spaces.
* Cannot be a Python keyword.
* Is case-sensitive.

Valid:

```python
def calculate_total():
    pass

def student_details():
    pass

def task1():
    pass
```

Invalid:

```python
def 1task():
    pass
```

Invalid:

```python
def student details():
    pass
```

---

# 🔤 9. Function Names are Case-Sensitive

Python treats uppercase and lowercase letters as different.

Example:

```python
def greet():
    print("Hello")

def Greet():
    print("Hi")
```

These are two different functions:

```text
greet
Greet
```

Therefore, consistent naming is important.

---

# 📐 10. Indentation in Functions

Python uses indentation to identify the function body.

Example:

```python
def greet():
    print("Hello")
    print("Welcome")
```

Both `print()` statements belong to the function because they are indented.

Incorrect:

```python
def greet():
print("Hello")
```

This causes an `IndentationError`.

Remember:

```text
def function():
    statement
    statement
    statement
```

---

# 🧱 11. Function Body

The **function body** contains the statements that should execute when the function runs.

Example:

```python
def student_info():
    name = "Asha"
    age = 20
    print(name)
    print(age)
```

The following statements are inside the function:

```python
name = "Asha"
age = 20
print(name)
print(age)
```

---

# ▶️ 12. Defining a Function Does Not Execute It

Consider:

```python
def greet():
    print("Hello")
```

If you run this program, nothing is printed.

Why?

Because the function has only been **defined**.

The function must be called separately.

```python
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
```

The important concept is:

```text
Function Definition
        ↓
Creates the function
        ↓
Function Call
        ↓
Executes the function
```

---

# 🧠 13. Function Definition vs Function Call

These two concepts are different.

### Function Definition

```python
def greet():
    print("Hello")
```

This creates the function.

### Function Call

```python
greet()
```

This executes the function.

Think of it as:

```text
def greet():
    ↓
Build the function

greet()
    ↓
Use the function
```

---

# 🔁 14. Calling a Function Multiple Times

Once a function is defined, it can be called multiple times.

Example:

```python
def greet():
    print("Welcome!")

greet()
greet()
greet()
```

Output:

```text
Welcome!
Welcome!
Welcome!
```

This demonstrates **code reuse**.

---

# 🟢 15. Simple Function Example

```python
def show_message():
    print("Learning Python")

show_message()
```

Output:

```text
Learning Python
```

The function performs one simple task:

```text
show_message()
        ↓
Print "Learning Python"
```

---

# 🔢 16. Function with Multiple Statements

A function can contain multiple statements.

Example:

```python
def student_details():
    name = "Asha"
    age = 20
    course = "BCA"

    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_details()
```

Output:

```text
Name: Asha
Age: 20
Course: BCA
```

All three variables and all three `print()` statements belong to the function.

---

# 🧩 17. Function for a Specific Task

A good function generally performs a specific task.

Example:

```python
def calculate_square():
    number = 8
    print(number * number)

calculate_square()
```

Output:

```text
64
```

The function has a clear purpose:

```text
calculate_square()
        ↓
Calculate square
```

---

# 🏗️ 18. Functions Improve Program Structure

Without functions:

```python
print("Student Details")
print("Name: Asha")
print("Course: BCA")

print("Employee Details")
print("Name: Neha")
print("Department: Development")
```

With functions:

```python
def student_details():
    print("Student Details")
    print("Name: Asha")
    print("Course: BCA")


def employee_details():
    print("Employee Details")
    print("Name: Neha")
    print("Department: Development")


student_details()
employee_details()
```

The program is easier to organize.

---

# 🧠 19. Functions as Small Building Blocks

A large program can be divided into smaller functions.

For example, an online shopping system might contain:

```text
Shopping System
       │
       ├── display_products()
       ├── add_to_cart()
       ├── remove_from_cart()
       ├── calculate_total()
       └── checkout()
```

Each function performs one specific task.

This makes large programs easier to manage.

---

# 📚 20. Built-in Functions vs User-Defined Functions

Python provides many functions automatically.

These are called **built-in functions**.

Examples:

```python
print()
len()
max()
min()
sum()
type()
input()
```

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

We can also create our own functions.

These are called **user-defined functions**.

Example:

```python
def greet():
    print("Hello")
```

---

# ⚖️ 21. Built-in vs User-Defined Functions

| Type                  | Meaning                    | Example   |
| --------------------- | -------------------------- | --------- |
| Built-in function     | Already provided by Python | `len()`   |
| User-defined function | Created by the programmer  | `greet()` |

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Here:

```text
len() → Built-in function
```

Example:

```python
def greet():
    print("Hello")
```

Here:

```text
greet() → User-defined function
```

---

# 🧪 22. Function with `pass`

Sometimes we want to define a function but do not want to write its implementation yet.

Python provides the `pass` statement for this.

Example:

```python
def calculate_salary():
    pass
```

The function is valid but currently does nothing.

This is useful when developing a program step by step.

---

# 📝 23. Function with a Docstring

A function can contain a **docstring** that describes what the function does.

Example:

```python
def greet():
    """Display a welcome message."""
    print("Welcome to Python")
```

The text:

```python
"""Display a welcome message."""
```

is a docstring.

Docstrings make functions easier to understand and document.

---

# 🔍 24. Accessing a Function's Docstring

The `__doc__` attribute can be used to access a function's docstring.

Example:

```python
def greet():
    """Display a welcome message."""
    print("Welcome")

print(greet.__doc__)
```

Output:

```text
Display a welcome message.
```

---

# 🧠 25. Function with a Local Variable

Variables created inside a function are generally local to that function.

Example:

```python
def student():
    name = "Asha"
    print(name)

student()
```

Output:

```text
Asha
```

Here:

```text
name
 ↓
Created inside student()
 ↓
Local variable
```

---

# ⚠️ 26. Local Variable Cannot Normally Be Used Outside the Function

Consider:

```python
def student():
    name = "Asha"

student()

print(name)
```

This produces an error because `name` was created inside the function.

The variable belongs to the function's local scope.

---

# 🌍 27. Global Variables

A variable created outside a function is called a global variable.

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

The function can read the global variable.

For beginners, remember:

```text
Outside function
      ↓
Global scope

Inside function
      ↓
Local scope
```

---

# ⚖️ 28. Local vs Global Variables

| Variable        | Created          | Scope          |
| --------------- | ---------------- | -------------- |
| Local variable  | Inside function  | Function       |
| Global variable | Outside function | Program/module |

Example:

```python
course = "BCA"

def student():
    name = "Asha"
    print(course)
    print(name)

student()
```

Here:

```text
course → global variable
name   → local variable
```

---

# 🔄 29. Functions and Loops

Functions can contain loops.

Example:

```python
def display_numbers():
    for number in range(1, 6):
        print(number)

display_numbers()
```

Output:

```text
1
2
3
4
5
```

Functions allow us to reuse the loop whenever required.

---

# 🔀 30. Functions and Conditions

Functions can also contain conditions.

Example:

```python
def check_age():
    age = 20

    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

check_age()
```

Output:

```text
Eligible
```

---

# 🧮 31. Function for Mathematical Calculation

Functions can be used for calculations.

Example:

```python
def calculate_total():
    price = 500
    quantity = 3

    total = price * quantity

    print("Total:", total)

calculate_total()
```

Output:

```text
Total: 1500
```

---

# 🌍 32. Real-World Example: Login System

A function can represent a specific operation in a login system.

```python
def display_login_message():
    print("Welcome to the login system")
    print("Please enter your credentials")

display_login_message()
```

The function represents one logical part of the application.

A larger application could eventually contain:

```text
login()
logout()
validate_user()
display_dashboard()
```

---

# 🌍 33. Real-World Example: Student Management

```python
def display_student():
    print("Student Name: Asha")
    print("Course: BCA")
    print("Semester: 4")

display_student()
```

Output:

```text
Student Name: Asha
Course: BCA
Semester: 4
```

The function groups related student information together.

---

# 🌍 34. Real-World Example: Shopping System

```python
def display_cart():
    print("Laptop")
    print("Mouse")
    print("Keyboard")

display_cart()
```

Output:

```text
Laptop
Mouse
Keyboard
```

A real shopping application could later divide its operations into functions such as:

```text
display_cart()
add_product()
remove_product()
calculate_total()
checkout()
```

---

# 🌍 35. Real-World Example: Employee System

```python
def display_employee():
    print("Employee ID: 101")
    print("Name: Neha")
    print("Department: Development")

display_employee()
```

Output:

```text
Employee ID: 101
Name: Neha
Department: Development
```

Functions help organize employee-related operations.

---

# 🧠 36. One Function, One Responsibility

A useful programming principle is:

> A function should ideally have one clear responsibility.

Good:

```python
def calculate_total():
    pass

def display_invoice():
    pass

def save_customer():
    pass
```

Each function has a specific responsibility.

Less organized:

```python
def everything():
    # calculate salary
    # display products
    # save student
    # send email
    # calculate marks
    pass
```

Large functions containing unrelated tasks are harder to understand and maintain.

---

# 🔁 37. Reusing a Function

Suppose we need to display a welcome message for several sections.

Instead of:

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

we can write:

```python
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()
```

The function allows the same operation to be reused.

---

# 🧱 38. Function Definition Structure

A function definition can be understood as:

```text
def function_name():
    statement
    statement
    statement
```

Example:

```python
def calculate_bill():
    price = 1000
    quantity = 2
    total = price * quantity
    print(total)
```

Breakdown:

```text
def
 ↓
Keyword

calculate_bill
 ↓
Function name

()
 ↓
Parameter section

:
 ↓
Start of function body

Indented statements
 ↓
Function body
```

---

# 📌 39. Empty Parameter List

A function can be defined without parameters.

Example:

```python
def show_message():
    print("Hello Python")
```

The parentheses are still required:

```python
()
```

Even when the function does not accept any parameters.

---

# 🧠 40. Function Definition with a Comment

Comments can be used inside functions to explain the code.

Example:

```python
def calculate_total():
    # Store the product price
    price = 500

    # Store the quantity
    quantity = 2

    print(price * quantity)
```

Comments help explain the purpose of the statements.

---

# 📖 41. Function Documentation

Good functions should be understandable to other programmers.

Example:

```python
def display_student():
    """Display basic student information."""
    print("Name: Asha")
    print("Course: BCA")
```

The docstring explains the function's purpose.

For larger projects, documentation becomes very important.

---

# ⚠️ 42. Common Mistake: Forgetting `def`

Incorrect:

```python
greet():
    print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

The `def` keyword is required when defining a function.

---

# ⚠️ 43. Common Mistake: Forgetting the Colon

Incorrect:

```python
def greet()
    print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

The colon `:` is required after the function header.

---

# ⚠️ 44. Common Mistake: Incorrect Indentation

Incorrect:

```python
def greet():
print("Hello")
```

Correct:

```python
def greet():
    print("Hello")
```

Python uses indentation to identify the function body.

---

# ⚠️ 45. Common Mistake: Defining but Not Calling

Consider:

```python
def greet():
    print("Hello")
```

Nothing is displayed because the function was only defined.

Correct:

```python
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
```

---

# ⚠️ 46. Common Mistake: Calling Before Definition

Consider:

```python
greet()

def greet():
    print("Hello")
```

This causes an error because the function has not yet been defined when Python reaches the call.

Generally, define the function before calling it:

```python
def greet():
    print("Hello")

greet()
```

---

# ⚠️ 47. Common Mistake: Using a Poor Function Name

Avoid unclear names:

```python
def x():
    print("Calculating total")
```

Prefer:

```python
def calculate_total():
    print("Calculating total")
```

A descriptive function name makes the code self-explanatory.

---

# ⚠️ 48. Common Mistake: Mixing Unrelated Tasks

Avoid putting many unrelated operations into one function.

Poor structure:

```python
def process():
    print("Student details")
    print("Calculate shopping total")
    print("Display employee")
```

Better structure:

```python
def display_student():
    pass

def calculate_cart_total():
    pass

def display_employee():
    pass
```

This makes the program more modular.

---

# 📊 49. Function Definition Summary

| Component     | Purpose                     |
| ------------- | --------------------------- |
| `def`         | Defines a function          |
| Function name | Identifies the function     |
| `()`          | Contains parameters         |
| `:`           | Starts the function body    |
| Indentation   | Defines the function body   |
| Statements    | Perform the function's task |
| Docstring     | Documents the function      |

---

# 🧪 50. Practice Programs

## 🟢 Easy

### Program 1: Create a Greeting Function

Define a function named `greet()` that displays:

```text
Hello, welcome to Python!
```

---

### Program 2: Display a Message

Create a function named `show_message()` that prints:

```text
I am learning functions.
```

---

### Program 3: Display Course Information

Create a function named `course_info()` that displays:

```text
Course: BCA
Subject: Python
```

---

### Program 4: Display Numbers

Create a function named `display_numbers()` that uses a loop to display numbers from `1` to `5`.

---

## 🟡 Medium

### Program 5: Student Details

Create a function named `student_details()` that displays:

```text
Name
Age
Course
College
```

Use suitable values.

---

### Program 6: Calculate Square

Create a function named `calculate_square()`.

Inside the function:

```text
number = 8
```

Calculate and display its square.

---

### Program 7: Calculate Total

Create a function named `calculate_total()`.

Inside the function:

```text
price = 750
quantity = 4
```

Calculate the total price.

---

### Program 8: Check Voting Eligibility

Create a function named `check_eligibility()`.

Inside the function:

```text
age = 21
```

Use an `if-else` statement to determine whether the person is eligible to vote.

---

## 🔴 Advanced

### Program 9: Student Result

Create a function named `student_result()`.

Inside the function, store marks for five subjects.

Calculate:

* Total marks
* Average marks

Then display the results.

---

### Program 10: Employee Information

Create a function named `employee_details()`.

Store:

```text
Employee ID
Name
Department
Salary
Experience
```

Display all employee information.

---

### Program 11: Shopping Cart

Create a function named `calculate_cart_total()`.

Store prices of several products.

Use a loop to calculate and display the total.

---

### Program 12: Product Stock Checker

Create a function named `check_stock()`.

Store the stock quantity of a product.

Use an `if-else` statement:

```text
If stock > 0
    Display "Product Available"

Otherwise
    Display "Out of Stock"
```

---

# 🏆 51. Challenge

Create a **Student Information System** using a function.

Define a function named:

```python
student_information()
```

Inside the function:

1. Store the student's name.
2. Store the student's age.
3. Store the course.
4. Store marks for five subjects.
5. Calculate total marks.
6. Calculate average marks.
7. Use an `if-else` statement to determine whether the student passed.
8. Display all student information.
9. Call the function.

Try solving the challenge without copying a solution.

---

# 🧪 52. Mini Project: Simple Employee Management System

Create a simple employee management program using functions.

Create separate functions for:

```text
display_employee()
calculate_salary()
check_experience()
```

The employee data can contain:

```text
Employee ID
Name
Department
Salary
Experience
```

### Requirements

* [ ] Create a function to display employee information.
* [ ] Create a function to calculate annual salary.
* [ ] Create a function to check whether the employee has more than 2 years of experience.
* [ ] Call each function.
* [ ] Display the results clearly.

### Your Goal

Understand how a larger program can be divided into smaller functions.

---

# 🎤 53. Interview Questions

* [ ] What is a function in Python?
* [ ] Why are functions used?
* [ ] What is a user-defined function?
* [ ] What is the purpose of the `def` keyword?
* [ ] How do you define a function?
* [ ] What is the syntax of a function?
* [ ] What is a function body?
* [ ] Why is indentation important in functions?
* [ ] What is the difference between defining and calling a function?
* [ ] Does defining a function execute it immediately?
* [ ] How can you call a function multiple times?
* [ ] What are built-in functions?
* [ ] What are user-defined functions?
* [ ] Give examples of built-in functions.
* [ ] What is a function name?
* [ ] What are the rules for naming functions?
* [ ] What is a docstring?
* [ ] What is a local variable?
* [ ] What is a global variable?
* [ ] What is the difference between local and global variables?
* [ ] Why should a function ideally have one responsibility?
* [ ] What does the `pass` statement do inside a function?
* [ ] What happens if you forget the colon after a function definition?
* [ ] What happens if indentation is incorrect?
* [ ] What happens if you define a function but never call it?
* [ ] Why are functions important in large programs?
* [ ] How do functions improve code reusability?
* [ ] How do functions improve code organization?

---

# 📝 54. Assignment

Complete the following programs.

### Task 1

Create a function named `welcome()`.

Display:

```text
Welcome to Python Programming
```

---

### Task 2

Create a function named `student_details()`.

Display:

```text
Name
Age
Course
City
```

---

### Task 3

Create a function that displays numbers from `1` to `10`.

---

### Task 4

Create a function that calculates the square of a number.

---

### Task 5

Create a function that calculates the total price of a product.

Use:

```text
price
quantity
```

---

### Task 6

Create a function that checks whether a number is positive, negative, or zero.

---

### Task 7

Create a function that displays the marks of five subjects and calculates the total.

---

### Task 8

Create a function named `employee_details()`.

Display:

```text
Employee ID
Name
Department
Salary
Experience
```

---

### Task 9

Create a function with a docstring explaining what the function does.

---

### Task 10

Create three separate functions:

```text
display_name()
display_course()
display_college()
```

Call all three functions.

---

### Task 11

Create a real-world program that uses at least five user-defined functions.

---

### Task 12

Create a program containing separate functions for:

```text
Input/display student information
Calculate total marks
Calculate average marks
Check result
Display final result
```

---

# 🧠 55. Memory Tricks

Remember the basic function structure:

```text
def
 ↓
Function Name
 ↓
()
 ↓
:
 ↓
Indented Body
```

Example:

```python
def greet():
    print("Hello")
```

---

Remember:

```text
def function():
    ↓
Define the function

function()
    ↓
Call the function
```

---

Remember the difference:

```text
Definition
   ↓
Creates the function

Call
   ↓
Executes the function
```

---

Remember:

```text
def
 ↓
Define

()
 ↓
Parameters

:
 ↓
Start body

Indentation
 ↓
Function body
```

---

Remember the main purpose:

```text
Function
   ↓
Reusable Code
   ↓
Less Repetition
   ↓
Better Organization
   ↓
Easier Maintenance
```

---

# 📌 56. Important Rules to Remember

```text
1. Functions are reusable blocks of code.

2. Functions are defined using the def keyword.

3. A function must have a valid function name.

4. Parentheses () are required in a function definition.

5. A colon : is required after the function header.

6. The function body must be properly indented.

7. Defining a function does not execute it.

8. A function is executed when it is called.

9. A function can be called multiple times.

10. Functions help reduce code repetition.

11. Functions improve program organization.

12. Functions can contain variables, loops, and conditions.

13. Functions can contain multiple statements.

14. A function can be documented using a docstring.

15. Variables created inside functions are generally local variables.

16. Variables created outside functions are global variables.

17. Built-in functions are provided by Python.

18. User-defined functions are created by programmers.

19. A good function should generally have one clear responsibility.

20. Descriptive function names make programs easier to understand.
```

---

# 📊 57. Function Structure

```text
                         FUNCTION
                             │
                             ↓
                    FUNCTION DEFINITION
                             │
                             ↓
                          def
                             │
                             ↓
                     FUNCTION NAME
                             │
                             ↓
                           ( )
                             │
                             ↓
                            :
                             │
                             ↓
                    INDENTED FUNCTION BODY
                             │
               ┌─────────────┼─────────────┐
               ↓             ↓             ↓
            Statements      Loops       Conditions
               │             │             │
               └─────────────┼─────────────┘
                             ↓
                    FUNCTION IS CREATED
                             │
                             ↓
                      FUNCTION CALL
                             │
                             ↓
                     FUNCTION EXECUTES
```

---

# 📚 58. Complete Function Definition Cheat Sheet

### Define a Function

```python
def greet():
    print("Hello")
```

### Call a Function

```python
greet()
```

### Function with Multiple Statements

```python
def student():
    print("Name: Asha")
    print("Course: BCA")
```

### Function with a Loop

```python
def display_numbers():
    for number in range(1, 6):
        print(number)
```

### Function with a Condition

```python
def check_age():
    age = 20

    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
```

### Function with a Local Variable

```python
def student():
    name = "Asha"
    print(name)
```

### Function with a Docstring

```python
def greet():
    """Display a greeting message."""
    print("Hello")
```

### Empty Function

```python
def future_task():
    pass
```

---

# 🏆 59. Functions Mastery

```text
                         FUNCTIONS
                              │
                              ↓
                       User-Defined
                              │
                              ↓
                         Definition
                              │
                              ↓
                            def
                              │
                              ↓
                       Function Name
                              │
                              ↓
                            ( )
                              │
                              ↓
                             :
                              │
                              ↓
                       Function Body
                              │
              ┌───────────────┼───────────────┐
              ↓               ↓               ↓
          Statements         Loops         Conditions
              │               │               │
              └───────────────┼───────────────┘
                              ↓
                       Function Definition
                              │
                              ↓
                        Function Call
                              │
                              ↓
                         Code Executes
                              │
                              ↓
                        Code Reusability
```

---

# 📚 60. Summary

In this lesson, you learned:

* [ ] What a function is.
* [ ] Why functions are used.
* [ ] How functions improve code reusability.
* [ ] How functions improve program organization.
* [ ] The difference between built-in and user-defined functions.
* [ ] How to define a function.
* [ ] The purpose of the `def` keyword.
* [ ] How to choose a function name.
* [ ] The rules for function names.
* [ ] How indentation works inside functions.
* [ ] What a function body is.
* [ ] The difference between defining and calling a function.
* [ ] How to call a function multiple times.
* [ ] How functions can contain multiple statements.
* [ ] How functions can contain loops.
* [ ] How functions can contain conditions.
* [ ] How to use `pass` inside an empty function.
* [ ] How to use docstrings.
* [ ] What local variables are.
* [ ] What global variables are.
* [ ] The difference between local and global variables.
* [ ] How functions can be used in real-world programs.
* [ ] Common mistakes when defining functions.
* [ ] How to divide large programs into smaller functions.
* [ ] How to build reusable program components.

---

# 🎯 Topic Completion Checklist

* [x] I understand what a function is.
* [x] I understand why functions are used.
* [x] I understand code reusability.
* [x] I know how to define a function.
* [x] I understand the `def` keyword.
* [x] I know the rules for function names.
* [x] I understand function indentation.
* [x] I understand the function body.
* [x] I understand the difference between definition and calling.
* [x] I can create a simple function.
* [x] I can call a function multiple times.
* [x] I can create functions containing multiple statements.
* [x] I can create functions containing loops.
* [x] I can create functions containing conditions.
* [x] I understand built-in functions.
* [x] I understand user-defined functions.
* [x] I understand local variables.
* [x] I understand global variables.
* [x] I understand docstrings.
* [x] I understand the `pass` statement.
* [x] I can create functions for real-world tasks.
* [x] I can divide a program into multiple functions.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the assignment.
* [x] I can define functions without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Function Parameters and Arguments**

In the next topic, you will learn:

* What parameters are.
* What arguments are.
* The difference between parameters and arguments.
* How to define functions with parameters.
* How to pass arguments to functions.
* Positional arguments.
* Keyword arguments.
* Default arguments.
* Multiple parameters.
* Passing different types of values.
* Using parameters with calculations.
* Using parameters with conditions.
* Using parameters with loops.
* Real-world examples using parameters.
* Common mistakes with parameters and arguments.
* Practice programs and challenges.
* Advanced parameter concepts.

---

## ⭐ Quote of the Day

> **"A function turns a piece of code into a reusable building block."** 🐍📚
