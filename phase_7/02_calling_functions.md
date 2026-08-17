# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 2: Calling Functions

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what calling a function means.
* [ ] Understand the difference between defining and calling a function.
* [ ] Call a function using its name.
* [ ] Understand function call syntax.
* [ ] Call functions multiple times.
* [ ] Understand how Python executes a function call.
* [ ] Call functions with arguments.
* [ ] Call functions without arguments.
* [ ] Understand positional arguments.
* [ ] Understand keyword arguments.
* [ ] Call functions using variables as arguments.
* [ ] Call functions inside expressions.
* [ ] Call functions inside conditions.
* [ ] Call functions inside loops.
* [ ] Understand the return value of a function call.
* [ ] Store returned values in variables.
* [ ] Call one function from another function.
* [ ] Understand nested function calls.
* [ ] Avoid common mistakes when calling functions.
* [ ] Use function calls in real-world applications.

---

# 📖 1. What Does Calling a Function Mean?

**Calling a function** means asking Python to execute the instructions written inside that function.

A function is normally defined first and then called when we want to execute it.

Example:

```python
def greet():
    print("Hello!")

greet()
```

Output:

```text
Hello!
```

Here:

```text
def greet():
```

creates the function.

And:

```python
greet()
```

calls the function.

When Python reaches `greet()`, it executes the code inside the function.

---

# 🧠 2. Defining vs Calling a Function

There is an important difference between **defining** a function and **calling** a function.

### Function definition:

```python
def greet():
    print("Hello!")
```

The function is created, but its code does not execute yet.

### Function call:

```python
greet()
```

The function is executed.

Remember:

```text
Definition
    ↓
Create the function

Call
    ↓
Execute the function
```

---

# 📚 3. Basic Function Call Syntax

The general syntax for calling a function is:

```python
function_name()
```

Example:

```python
def welcome():
    print("Welcome to Python!")

welcome()
```

Output:

```text
Welcome to Python!
```

Here:

```text
welcome
   ↓
Function name

()
   ↓
Function call
```

---

# 🔍 4. Understanding Parentheses in a Function Call

The parentheses `()` are important when calling a function.

Example:

```python
def greet():
    print("Hello")

greet()
```

Here:

```python
greet()
```

means **call the function**.

But:

```python
greet
```

refers to the function object itself.

For example:

```python
def greet():
    print("Hello")

print(greet)
```

The output will represent the function object rather than execute `"Hello"`.

Therefore:

```text
greet
   ↓
Function object

greet()
   ↓
Call and execute function
```

---

# 🧩 5. Calling a Function After Definition

A function can be called after it has been defined.

Example:

```python
def display_message():
    print("Python is easy to learn")

display_message()
```

Output:

```text
Python is easy to learn
```

Python first creates the function and then reaches the function call.

---

# 🔄 6. Calling a Function Multiple Times

A function can be called multiple times.

Example:

```python
def greet():
    print("Hello!")

greet()
greet()
greet()
```

Output:

```text
Hello!
Hello!
Hello!
```

The function does not need to be written repeatedly.

Instead, we can reuse it:

```text
One function
     ↓
Call 1
Call 2
Call 3
Call 4
```

This is one of the major advantages of functions.

---

# 🧠 7. How Python Executes a Function Call

Consider:

```python
def welcome():
    print("Welcome!")

print("Start")

welcome()

print("End")
```

Python executes it in this order:

```text
1. Create welcome()
2. print("Start")
3. Call welcome()
4. Execute print("Welcome!")
5. print("End")
```

Output:

```text
Start
Welcome!
End
```

The function's code executes only when Python reaches the function call.

---

# 🔢 8. Calling a Function Several Times in Different Places

You can call the same function from different places in your program.

Example:

```python
def show_message():
    print("Keep learning Python")

show_message()

print("Practice")

show_message()
```

Output:

```text
Keep learning Python
Practice
Keep learning Python
```

The same function can be reused whenever required.

---

# 📦 9. Calling a Function Without Arguments

Some functions do not require any information from the caller.

Example:

```python
def show_course():
    print("Python Master Course")

show_course()
```

Output:

```text
Python Master Course
```

The function is called using:

```python
show_course()
```

No value is passed between the parentheses.

---

# 🎯 10. Calling a Function With Arguments

A function can receive information when it is called.

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

The value `"Asha"` is passed when the function is called.

---

# 🧠 11. Understanding Arguments in a Function Call

Consider:

```python
def square(number):
    print(number * number)

square(5)
```

Here:

```text
number
   ↓
Parameter

5
   ↓
Argument
```

When Python executes:

```python
square(5)
```

the value `5` is assigned to `number`.

Then:

```python
number * number
```

becomes:

```python
5 * 5
```

Output:

```text
25
```

---

# 🔢 12. Calling a Function With Multiple Arguments

A function can receive multiple arguments.

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

Here:

```text
a → 10
b → 20
```

The arguments are passed in the same order as the parameters.

---

# ⚖️ 13. Positional Arguments

When arguments are passed according to their position, they are called **positional arguments**.

Example:

```python
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Asha", 20)
```

Output:

```text
Name: Asha
Age: 20
```

Python matches:

```text
"Asha" → name
20     → age
```

---

# 🔑 14. Keyword Arguments

Arguments can also be passed using parameter names.

Example:

```python
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="Asha")
```

Output:

```text
Name: Asha
Age: 20
```

The order does not matter when keyword arguments are used.

---

# 🆚 15. Positional vs Keyword Arguments

| Type       | Example                             | Order Important? |
| ---------- | ----------------------------------- | ---------------- |
| Positional | `student_info("Asha", 20)`          | ✅ Yes            |
| Keyword    | `student_info(age=20, name="Asha")` | ❌ No             |

Remember:

```text
Positional
   ↓
Position matters

Keyword
   ↓
Parameter name matters
```

---

# 🔄 16. Calling a Function Using Variables

Arguments do not have to be written directly inside the function call.

You can use variables.

Example:

```python
def greet(name):
    print("Hello", name)

student_name = "Asha"

greet(student_name)
```

Output:

```text
Hello Asha
```

Here:

```text
student_name
     ↓
"Asha"
     ↓
greet(student_name)
```

---

# 🔢 17. Calling a Function Using Multiple Variables

Example:

```python
def calculate_total(price, quantity):
    print(price * quantity)

price = 500
quantity = 3

calculate_total(price, quantity)
```

Output:

```text
1500
```

The values of the variables are passed to the function.

---

# 🧩 18. Calling Functions With Expressions

An expression can also be passed as an argument.

Example:

```python
def display(number):
    print(number)

display(10 + 5)
```

Output:

```text
15
```

Python first evaluates:

```python
10 + 5
```

Then calls:

```python
display(15)
```

---

# 🧮 19. Calling Functions Inside Expressions

A function call can be part of an expression.

Example:

```python
def get_number():
    return 10

result = get_number() + 5

print(result)
```

Output:

```text
15
```

Python first calls:

```python
get_number()
```

which returns `10`.

Then:

```text
10 + 5
```

becomes:

```text
15
```

---

# 🔙 20. Calling a Function That Returns a Value

A function can return a value when it is called.

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
add(10, 20)
      ↓
    30
      ↓
result
```

---

# 📥 21. Storing the Return Value

The result of a function call can be stored in a variable.

Example:

```python
def square(number):
    return number * number

answer = square(6)

print(answer)
```

Output:

```text
36
```

The function call:

```python
square(6)
```

produces:

```text
36
```

which is stored in:

```python
answer
```

---

# 🧠 22. Calling a Function Directly Inside `print()`

You can call a function directly inside `print()`.

Example:

```python
def get_name():
    return "Asha"

print(get_name())
```

Output:

```text
Asha
```

The function is called first, and its returned value is passed to `print()`.

---

# ⚙️ 23. Calling a Function Inside an `if` Condition

A function can be called inside a condition.

Example:

```python
def get_age():
    return 20

if get_age() >= 18:
    print("Eligible")
```

Output:

```text
Eligible
```

The function call:

```python
get_age()
```

returns `20`.

Then Python checks:

```python
20 >= 18
```

---

# 🔁 24. Calling a Function Inside a Loop

Functions can be called repeatedly inside loops.

Example:

```python
def greet():
    print("Hello")

for i in range(3):
    greet()
```

Output:

```text
Hello
Hello
Hello
```

The loop controls how many times the function is called.

---

# 🔢 25. Calling a Function Inside a `while` Loop

Example:

```python
def display_count(number):
    print("Count:", number)

count = 1

while count <= 3:
    display_count(count)
    count += 1
```

Output:

```text
Count: 1
Count: 2
Count: 3
```

Each iteration calls the function with a different argument.

---

# 🔗 26. Calling One Function From Another Function

One function can call another function.

Example:

```python
def message():
    print("Welcome")

def start():
    message()

start()
```

Output:

```text
Welcome
```

Execution:

```text
start()
   ↓
message()
   ↓
"Welcome"
```

This allows programs to be divided into smaller reusable parts.

---

# 🧩 27. Multiple Function Calls Inside a Function

A function can call multiple other functions.

Example:

```python
def first():
    print("First")

def second():
    print("Second")

def start():
    first()
    second()

start()
```

Output:

```text
First
Second
```

The `start()` function coordinates the other functions.

---

# 🔄 28. Nested Function Calls

A function call can be passed as an argument to another function.

Example:

```python
def square(number):
    return number * number

def display(value):
    print(value)

display(square(5))
```

Output:

```text
25
```

Execution:

```text
square(5)
   ↓
25
   ↓
display(25)
```

---

# 🧠 29. Calling Functions in the Correct Order

Consider:

```python
def greet():
    print("Hello")

greet()
```

The function must be defined before Python reaches the call.

For example:

```python
greet()

def greet():
    print("Hello")
```

This causes an error because Python tries to call `greet()` before the function has been defined.

Typical error:

```text
NameError
```

Remember:

```text
Define first
     ↓
Call later
```

---

# ⚠️ 30. Calling a Function With the Wrong Number of Arguments

Consider:

```python
def add(a, b):
    print(a + b)

add(10)
```

The function expects two arguments, but only one is provided.

This causes:

```text
TypeError
```

Similarly:

```python
add(10, 20, 30)
```

also causes an error because three arguments are provided when only two are expected.

---

# 🛡️ 31. Calling a Function With Correct Arguments

Correct:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

The number of arguments matches the number of required parameters.

---

# 🔢 32. Calling a Function With Different Data Types

A function can be called with different types of values if the function's operations support them.

Example:

```python
def display(value):
    print(value)

display(100)
display("Python")
display(25.5)
```

Output:

```text
100
Python
25.5
```

The function receives different values on different calls.

---

# 🧪 33. Calling the Same Function With Different Values

A major advantage of functions is reuse.

Example:

```python
def square(number):
    return number * number

print(square(2))
print(square(5))
print(square(10))
```

Output:

```text
4
25
100
```

The same function performs the same operation on different data.

---

# 📊 34. Calling Functions With User Input

A function can be called using values received from the user.

Example:

```python
def greet(name):
    print("Hello", name)

name = input("Enter your name: ")

greet(name)
```

If the user enters:

```text
Asha
```

Output:

```text
Hello Asha
```

Flow:

```text
User Input
    ↓
Variable
    ↓
Function Call
    ↓
Function Execution
```

---

# 🧮 35. Calling a Function With Converted Input

Remember that `input()` returns a string.

Therefore, numeric input often needs conversion.

Example:

```python
def square(number):
    print(number * number)

number = int(input("Enter a number: "))

square(number)
```

If the user enters:

```text
5
```

Output:

```text
25
```

---

# 🌍 36. Real-World Example: Student Greeting

```python
def welcome_student(name):
    print("Welcome,", name)

student_name = input("Enter student name: ")

welcome_student(student_name)
```

Possible output:

```text
Enter student name: Asha
Welcome, Asha
```

The function is reusable for any student name.

---

# 🌍 37. Real-World Example: Shopping Cart

```python
def calculate_total(price, quantity):
    return price * quantity

price = 500
quantity = 4

total = calculate_total(price, quantity)

print("Total:", total)
```

Output:

```text
Total: 2000
```

The function call:

```python
calculate_total(price, quantity)
```

performs the calculation.

---

# 🌍 38. Real-World Example: Student Marks

```python
def calculate_total(marks1, marks2, marks3):
    return marks1 + marks2 + marks3

total = calculate_total(85, 90, 80)

print("Total Marks:", total)
```

Output:

```text
Total Marks: 255
```

The function call receives three marks and returns their total.

---

# 🌍 39. Real-World Example: Employee Salary

```python
def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus

salary = calculate_salary(40000, 5000)

print("Final Salary:", salary)
```

Output:

```text
Final Salary: 45000
```

---

# 🌍 40. Real-World Example: Login Validation

```python
def check_login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

result = check_login("admin", "1234")

if result:
    print("Login successful")
else:
    print("Invalid login")
```

Output:

```text
Login successful
```

The function call:

```python
check_login("admin", "1234")
```

returns a Boolean value.

---

# 🔄 41. Calling Functions in a Sequence

Multiple functions can be called one after another.

Example:

```python
def login():
    print("Login successful")

def load_profile():
    print("Profile loaded")

def show_dashboard():
    print("Dashboard opened")

login()
load_profile()
show_dashboard()
```

Output:

```text
Login successful
Profile loaded
Dashboard opened
```

This type of structure is common in real applications.

---

# 🧠 42. Function Call Flow

Consider:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

The execution flow is:

```text
add(10, 20)
     ↓
a = 10
b = 20
     ↓
a + b
     ↓
10 + 20
     ↓
30
     ↓
result = 30
     ↓
print(result)
```

Output:

```text
30
```

---

# 🔗 43. Calling Functions With Keyword Arguments

Example:

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)

employee(
    name="Asha",
    department="Development",
    salary=45000
)
```

Output:

```text
Asha
Development
45000
```

Keyword arguments make function calls easier to understand.

---

# ⚖️ 44. Mixing Positional and Keyword Arguments

Positional arguments can be combined with keyword arguments.

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

However, positional arguments must come before keyword arguments.

Correct:

```python
student("Asha", age=20, course="BCA")
```

Incorrect:

```python
student(name="Asha", 20, "BCA")
```

---

# 🧩 45. Calling a Function With a List

A list can be passed as an argument.

Example:

```python
def display_subjects(subjects):
    for subject in subjects:
        print(subject)

subjects = ["Python", "SQL", "Git"]

display_subjects(subjects)
```

Output:

```text
Python
SQL
Git
```

The entire list is passed to the function.

---

# 📦 46. Calling a Function With a Dictionary

A dictionary can also be passed as an argument.

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

# 🔁 47. Calling a Function Inside a Loop With Dictionary Data

Example:

```python
def display_mark(subject, mark):
    print(subject, ":", mark)

marks = {
    "Python": 90,
    "SQL": 85,
    "Git": 80
}

for subject, mark in marks.items():
    display_mark(subject, mark)
```

Output:

```text
Python : 90
SQL : 85
Git : 80
```

The function is called once for each dictionary item.

---

# 🔢 48. Calling a Function With a Condition

Example:

```python
def check_marks(mark):
    if mark >= 40:
        return "Pass"
    return "Fail"

result = check_marks(75)

print(result)
```

Output:

```text
Pass
```

The function call returns a result that can be used later.

---

# 🧠 49. Function Calls Can Return Different Values

A function can return different values depending on the input.

Example:

```python
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))
```

Output:

```text
Positive
Negative
Zero
```

---

# ⚠️ 50. Common Mistake: Forgetting Parentheses

Consider:

```python
def greet():
    print("Hello")

greet
```

The function is not called.

Correct:

```python
greet()
```

Remember:

```text
greet
   ↓
Reference to function

greet()
   ↓
Call function
```

---

# ⚠️ 51. Common Mistake: Calling Before Definition

Wrong:

```python
greet()

def greet():
    print("Hello")
```

Python reaches `greet()` before creating the function.

This produces a `NameError`.

Correct:

```python
def greet():
    print("Hello")

greet()
```

---

# ⚠️ 52. Common Mistake: Wrong Number of Arguments

Wrong:

```python
def multiply(a, b):
    return a * b

multiply(5)
```

The function requires two arguments.

Correct:

```python
multiply(5, 2)
```

Output:

```text
10
```

---

# ⚠️ 53. Common Mistake: Confusing Parameters and Arguments

Consider:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
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

A parameter belongs to the function definition.

An argument is the actual value supplied during the function call.

---

# ⚠️ 54. Common Mistake: Ignoring the Return Value

Consider:

```python
def add(a, b):
    return a + b

add(10, 20)
```

The function returns `30`, but the returned value is not stored or displayed.

You can use:

```python
result = add(10, 20)

print(result)
```

Output:

```text
30
```

Or:

```python
print(add(10, 20))
```

Output:

```text
30
```

---

# 📊 55. Function Calling Comparison

| Function Call          | Meaning                                      |
| ---------------------- | -------------------------------------------- |
| `greet()`              | Call function without arguments              |
| `greet("Asha")`        | Call function with one argument              |
| `add(10, 20)`          | Call function with two arguments             |
| `student(name="Asha")` | Call using keyword argument                  |
| `square(number)`       | Call using a variable                        |
| `print(get_name())`    | Call function inside another function call   |
| `check_age(20)`        | Call function inside an expression/condition |

---

# 💻 56. Practice Programs

## 🟢 Easy

### Program 1: Call a Simple Function

```python
def greet():
    print("Hello, Python!")

greet()
```

---

### Program 2: Call a Function Multiple Times

```python
def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()
```

---

### Program 3: Call a Function With One Argument

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

---

### Program 4: Call a Function With Two Arguments

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

# 🟡 Medium

### Program 5: Call a Function Using Variables

```python
def multiply(a, b):
    print(a * b)

x = 5
y = 4

multiply(x, y)
```

---

### Program 6: Call a Function With User Input

```python
def greet(name):
    print("Welcome", name)

name = input("Enter your name: ")

greet(name)
```

---

### Program 7: Call a Function With a Return Value

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

---

### Program 8: Call a Function Inside `print()`

```python
def get_message():
    return "Learning Python"

print(get_message())
```

---

# 🔴 Advanced

## Program 9: Call a Function Inside a Loop

```python
def display(number):
    print("Number:", number)

for i in range(1, 6):
    display(i)
```

Output:

```text
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

---

## Program 10: Call a Function Inside a Condition

```python
def check_age(age):
    return age >= 18

age = 20

if check_age(age):
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Eligible
```

---

## Program 11: Call One Function From Another

```python
def message():
    print("Welcome")

def start():
    message()

start()
```

---

## Program 12: Function Call With Dictionary Data

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

---

# 🏆 57. Challenge

Create a program for a student.

Your program should:

1. Create a function called `student_info()`.
2. Pass the student's name as an argument.
3. Pass the student's age as an argument.
4. Pass the student's course as an argument.
5. Display all the information.
6. Call the function.
7. Call the same function again using different student information.
8. Use variables as arguments.
9. Use keyword arguments in one function call.
10. Take at least one value from the user using `input()`.

Example data:

```text
Name → Asha
Age → 20
Course → BCA
```

Try solving the challenge without copying a solution.

---

# 🧪 58. Mini Project: Student Information System

Create a simple student information program using functions.

Your program should contain a function that receives:

* Student ID
* Name
* Course
* Semester
* Marks

Example:

```python
student_id = 101
name = "Asha"
course = "BCA"
semester = 4
marks = 450
```

The function call should pass all these values to the function.

The function should display:

```text
Student ID: 101
Name: Asha
Course: BCA
Semester: 4
Marks: 450
```

### Your Goal

Practice calling the same function multiple times using different student information.

---

# 🎤 59. Interview Questions

* [ ] What does it mean to call a function?
* [ ] How do you call a function in Python?
* [ ] What is the difference between defining and calling a function?
* [ ] Why are parentheses used when calling a function?
* [ ] Can a function be called multiple times?
* [ ] What is an argument?
* [ ] What is a parameter?
* [ ] What is the difference between a parameter and an argument?
* [ ] What are positional arguments?
* [ ] What are keyword arguments?
* [ ] What is the difference between positional and keyword arguments?
* [ ] Can variables be passed as function arguments?
* [ ] Can expressions be passed as arguments?
* [ ] Can a function call be used inside `print()`?
* [ ] Can a function call be used inside an `if` condition?
* [ ] Can a function be called inside a loop?
* [ ] Can one function call another function?
* [ ] What happens when a function is called?
* [ ] What happens if a function is called before it is defined?
* [ ] What happens when the wrong number of arguments is supplied?
* [ ] How can you store the result of a function call?
* [ ] What is a nested function call?
* [ ] Can a list be passed to a function?
* [ ] Can a dictionary be passed to a function?
* [ ] Can a function return a value?
* [ ] What happens if a returned value is not stored or used?

---

# 📝 60. Assignment

Complete the following programs.

### Task 1

Create a function called `greet()` and call it three times.

---

### Task 2

Create a function that accepts a person's name and call it with your own value.

---

### Task 3

Create a function that accepts two numbers and displays their sum.

---

### Task 4

Create a function that accepts two numbers and returns their multiplication.

Store the returned value in a variable.

---

### Task 5

Create a function that accepts a student's:

```text
name
age
course
```

Call the function using positional arguments.

---

### Task 6

Call the same function using keyword arguments.

---

### Task 7

Create a function that accepts a number and determines whether it is positive, negative, or zero.

Call the function three times with different values.

---

### Task 8

Create a function that accepts a list of numbers.

Call the function using a list variable.

---

### Task 9

Create a function that accepts a dictionary containing student information.

Call the function and display the dictionary data.

---

### Task 10

Create a function that accepts a student's marks and returns `"Pass"` if the marks are 40 or greater.

Call the function inside an `if` statement.

---

### Task 11

Create a function that calculates the total price of a product.

Pass:

```text
price
quantity
```

Call the function using variables.

---

### Task 12

Create a program that uses:

* A function
* User input
* Function arguments
* A return value
* An `if` condition

Use the program to check whether a user is eligible based on age.

---

# 🧠 61. Memory Tricks

Remember:

```text
Define Function
      ↓
Create Function

Call Function
      ↓
Execute Function
```

---

Remember the basic call:

```text
function_name()
      ↓
Call function
```

---

Remember arguments:

```text
function_name(value)
       ↓
     Argument
```

---

Remember multiple arguments:

```text
function_name(value1, value2)
              ↓       ↓
          Argument  Argument
```

---

Remember return values:

```text
function()
    ↓
return value
    ↓
store/use result
```

---

Remember:

```text
Parameter
   ↓
Variable in function definition

Argument
   ↓
Actual value in function call
```

---

# 📌 62. Important Rules to Remember

```text
1. A function must generally be defined before Python reaches its call.

2. A function is called using its name followed by parentheses.

3. Parentheses are required to execute the function.

4. A function can be called multiple times.

5. Arguments are values supplied during a function call.

6. Positional arguments are matched according to position.

7. Keyword arguments are matched according to parameter names.

8. Positional arguments must come before keyword arguments.

9. Variables can be passed as function arguments.

10. Expressions can be passed as function arguments.

11. A function call can be used inside print().

12. A function call can be used inside expressions.

13. A function call can be used inside conditions.

14. A function can be called inside a loop.

15. One function can call another function.

16. A function can return a value.

17. A returned value can be stored in a variable.

18. A list can be passed to a function.

19. A dictionary can be passed to a function.

20. Passing the wrong number of arguments can cause TypeError.

21. Calling an undefined function can cause NameError.

22. Function calls allow code to be reused.

23. The same function can work with different arguments.

24. Function calls help divide a large program into smaller tasks.
```

---

# 📊 63. Function Calling Structure

```text
                         FUNCTION
                            │
                            ↓
                    FUNCTION DEFINITION
                            │
                            ↓
                       function_name
                            │
                            ↓
                     FUNCTION CALL
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
        No Arguments    Arguments       Keywords
             │              │              │
             ↓              ↓              ↓
         greet()       greet("Asha")   greet(name="Asha")
                            │
                            ↓
                       EXECUTION
                            │
                            ↓
                     Return / Output
```

---

# 🔗 64. Function Call Execution Flow

```text
             FUNCTION CALL
                   │
                   ↓
          Python finds function
                   │
                   ↓
          Arguments are passed
                   │
                   ↓
       Function code is executed
                   │
                   ↓
             return / output
                   │
                   ↓
       Program continues execution
```

---

# 📚 65. Complete Function Calling Cheat Sheet

### Call Without Arguments

```python
greet()
```

### Call With One Argument

```python
greet("Asha")
```

### Call With Multiple Arguments

```python
add(10, 20)
```

### Call Using Variables

```python
add(x, y)
```

### Call Using Keyword Arguments

```python
student(name="Asha", age=20)
```

### Store Returned Value

```python
result = add(10, 20)
```

### Call Inside `print()`

```python
print(add(10, 20))
```

### Call Inside `if`

```python
if check_age(20):
    print("Eligible")
```

### Call Inside a Loop

```python
for i in range(5):
    display(i)
```

### Call One Function From Another

```python
def start():
    greet()
```

### Call With a List

```python
display_subjects(subjects)
```

### Call With a Dictionary

```python
display_student(student)
```

---

# 🏆 66. Function Calling Mastery

```text
                         FUNCTION CALLING
                                │
             ┌──────────────────┼──────────────────┐
             ↓                  ↓                  ↓
          WITHOUT             WITH              RETURN
         ARGUMENTS          ARGUMENTS            VALUE
             │                  │                  │
             ↓                  ↓                  ↓
         greet()          greet("Asha")      result = add()
                                │
                    ┌───────────┴───────────┐
                    ↓                       ↓
                POSITIONAL               KEYWORD
                    │                       │
                    ↓                       ↓
               add(10, 20)         add(a=10, b=20)
                               
                                ↓
                         FUNCTION EXECUTION
                                │
                                ↓
                         OUTPUT / RETURN
```

---

# 📚 67. Summary

In this lesson, you learned:

* What calling a function means.
* The difference between defining and calling a function.
* How to call a function using parentheses.
* How to call a function without arguments.
* How to call a function with arguments.
* The difference between parameters and arguments.
* How positional arguments work.
* How keyword arguments work.
* The difference between positional and keyword arguments.
* How to pass variables to functions.
* How to pass expressions to functions.
* How to call functions multiple times.
* How to call functions inside `print()`.
* How to call functions inside expressions.
* How to call functions inside conditions.
* How to call functions inside loops.
* How one function can call another function.
* How nested function calls work.
* How to store returned values.
* How to call functions using user input.
* How to pass lists to functions.
* How to pass dictionaries to functions.
* Common mistakes when calling functions.
* How function calls improve code reuse.
* How function calls are used in real-world programs.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what calling a function means.
* [ ] I understand the difference between defining and calling a function.
* [ ] I know how to call a function.
* [ ] I understand why parentheses are used.
* [ ] I can call a function without arguments.
* [ ] I can call a function with arguments.
* [ ] I understand parameters and arguments.
* [ ] I understand positional arguments.
* [ ] I understand keyword arguments.
* [ ] I can call a function using variables.
* [ ] I can call a function using expressions.
* [ ] I can call a function multiple times.
* [ ] I can call a function inside `print()`.
* [ ] I can call a function inside an `if` condition.
* [ ] I can call a function inside a loop.
* [ ] I can call one function from another.
* [ ] I understand nested function calls.
* [ ] I can store a returned value.
* [ ] I can call functions using user input.
* [ ] I can pass lists to functions.
* [ ] I can pass dictionaries to functions.
* [ ] I understand common function-calling errors.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can call functions without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Function Arguments and Parameters**

In the next topic, you will learn:

* What parameters are.
* What arguments are.
* Difference between parameters and arguments.
* Positional arguments.
* Keyword arguments.
* Default arguments.
* Multiple arguments.
* Passing variables as arguments.
* Passing lists as arguments.
* Passing dictionaries as arguments.
* Passing tuples as arguments.
* Arbitrary positional arguments using `*args`.
* Arbitrary keyword arguments using `**kwargs`.
* Combining different types of arguments.
* Argument unpacking.
* Practical real-world examples.
* Common mistakes.
* Advanced argument techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"A function becomes useful when you call it, because calling is what turns reusable code into action."** 🐍📚
