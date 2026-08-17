# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 7: Positional Arguments

**Difficulty:** ⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what positional arguments are.
* [ ] Understand how positional arguments work in Python functions.
* [ ] Understand the relationship between parameters and arguments.
* [ ] Pass arguments based on their position.
* [ ] Understand the importance of argument order.
* [ ] Use multiple positional arguments.
* [ ] Use positional arguments with different data types.
* [ ] Understand what happens when arguments are passed in the wrong order.
* [ ] Understand the difference between parameters and positional arguments.
* [ ] Understand positional arguments with return values.
* [ ] Use positional arguments with conditions.
* [ ] Use positional arguments with loops.
* [ ] Use positional arguments in real-world applications.
* [ ] Understand common mistakes with positional arguments.
* [ ] Understand positional arguments with default parameters.
* [ ] Understand positional arguments with `*args`.
* [ ] Use positional arguments effectively in practical programs.

---

# 📖 1. What are Positional Arguments?

Positional arguments are arguments passed to a function based on their **position or order**.

The first argument is assigned to the first parameter.

The second argument is assigned to the second parameter.

The third argument is assigned to the third parameter, and so on.

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
"Asha" → first argument → name
20     → second argument → age
```

The values are assigned according to their position.

---

# 🧠 2. Understanding Parameters and Arguments

A **parameter** is a variable written inside the function definition.

An **argument** is the actual value passed when calling the function.

Example:

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
```

and:

```text
"Asha"
 ↓
Argument
```

So:

```text
Parameter → Variable that receives the value

Argument → Actual value supplied to the function
```

---

# 🔢 3. Basic Positional Argument Syntax

The general structure is:

```python
def function_name(parameter1, parameter2):
    # function body

function_name(argument1, argument2)
```

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

The assignment happens like this:

```text
a ← 10
b ← 20
```

because `10` is in the first position and `20` is in the second position.

---

# 📍 4. Why are They Called Positional Arguments?

They are called positional arguments because Python determines which parameter receives an argument based on its **position**.

Example:

```python
def introduce(name, age, course):
    print(name)
    print(age)
    print(course)

introduce("Asha", 20, "BCA")
```

Python matches:

```text
Position 1 → "Asha" → name
Position 2 → 20      → age
Position 3 → "BCA"   → course
```

---

# 🔄 5. Order Matters in Positional Arguments

The order of positional arguments is important.

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

If the values are reversed:

```python
student(20, "Asha")
```

Output:

```text
Name: 20
Age: Asha
```

Python does not automatically understand that `20` is supposed to represent age.

It simply follows the position.

---

# ⚖️ 6. Positional Argument Mapping

Consider:

```python
def display(a, b, c):
    print(a)
    print(b)
    print(c)

display(10, 20, 30)
```

The mapping is:

```text
a ← 10
b ← 20
c ← 30
```

Think of it as:

```text
Parameter Position       Argument Position

a  ← position 1 ← 10
b  ← position 2 ← 20
c  ← position 3 ← 30
```

---

# 🧩 7. Multiple Positional Arguments

A function can accept multiple positional arguments.

Example:

```python
def employee(name, department, salary):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)

employee("Neha", "Development", 45000)
```

Output:

```text
Name: Neha
Department: Development
Salary: 45000
```

Each argument is assigned according to its position.

---

# 🔢 8. Positional Arguments with Numbers

Positional arguments can be numbers.

Example:

```python
def multiply(a, b):
    print("Result:", a * b)

multiply(8, 5)
```

Output:

```text
Result: 40
```

Mapping:

```text
a ← 8
b ← 5
```

---

# 🔤 9. Positional Arguments with Strings

Positional arguments can also be strings.

Example:

```python
def message(name, city):
    print(name, "lives in", city)

message("Asha", "Bengaluru")
```

Output:

```text
Asha lives in Bengaluru
```

---

# 🔢 10. Positional Arguments with Different Data Types

Different parameters can receive different data types.

Example:

```python
def product(name, price, available):
    print("Product:", name)
    print("Price:", price)
    print("Available:", available)

product("Laptop", 55000, True)
```

Output:

```text
Product: Laptop
Price: 55000
Available: True
```

Mapping:

```text
name      ← "Laptop"
price     ← 55000
available ← True
```

---

# 🧠 11. Positional Arguments and Function Calls

The function definition specifies the parameters:

```python
def calculate(a, b):
    print(a + b)
```

The function call supplies the arguments:

```python
calculate(15, 25)
```

Therefore:

```text
Function Definition
       ↓
def calculate(a, b)

Function Call
       ↓
calculate(15, 25)

Mapping
       ↓
a ← 15
b ← 25
```

---

# ⚠️ 12. Too Few Positional Arguments

If a function requires two arguments but only one is supplied, Python raises a `TypeError`.

Example:

```python
def add(a, b):
    print(a + b)

add(10)
```

Typical error:

```text
TypeError: add() missing 1 required positional argument: 'b'
```

Python cannot call the function because `b` has not received a value.

---

# ⚠️ 13. Too Many Positional Arguments

If a function accepts two parameters but three arguments are supplied, Python raises a `TypeError`.

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20, 30)
```

Typical error:

```text
TypeError: add() takes 2 positional arguments but 3 were given
```

The function has only two parameters.

---

# 🔄 14. Changing the Order of Arguments

Consider:

```python
def student(name, course):
    print("Name:", name)
    print("Course:", course)

student("Asha", "BCA")
```

Output:

```text
Name: Asha
Course: BCA
```

Now reverse the arguments:

```python
student("BCA", "Asha")
```

Output:

```text
Name: BCA
Course: Asha
```

The function still executes because both values are valid arguments.

However, the data is assigned incorrectly.

---

# 🧠 15. Positional Arguments are Order-Dependent

Remember:

```text
Positional Arguments
        ↓
Depend on order
```

Example:

```python
def details(name, age, city):
    print(name, age, city)

details("Asha", 20, "Bengaluru")
```

Correct order:

```text
name → Asha
age  → 20
city → Bengaluru
```

Changing the order can change the meaning of the data.

---

# 📚 16. Positional Arguments with Return Values

Positional arguments can be used with functions that return values.

Example:

```python
def add(a, b):
    return a + b

result = add(25, 15)

print(result)
```

Output:

```text
40
```

Mapping:

```text
a ← 25
b ← 15
```

Then:

```text
25 + 15 = 40
```

---

# ➕ 17. Positional Arguments with Arithmetic Operations

Example:

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 4)

print("Total:", total)
```

Output:

```text
Total: 2000
```

Here:

```text
price    ← 500
quantity ← 4
```

---

# 🧮 18. Positional Arguments with Multiple Operations

Example:

```python
def calculate(a, b, c):
    return (a + b) * c

result = calculate(10, 20, 2)

print(result)
```

Output:

```text
60
```

Mapping:

```text
a ← 10
b ← 20
c ← 2
```

Calculation:

```text
(10 + 20) × 2
= 30 × 2
= 60
```

---

# 🔍 19. Positional Arguments with Conditions

Functions can use positional arguments with `if` statements.

Example:

```python
def check_result(name, marks):
    if marks >= 40:
        print(name, "Passed")
    else:
        print(name, "Failed")

check_result("Asha", 75)
```

Output:

```text
Asha Passed
```

Mapping:

```text
name  ← "Asha"
marks ← 75
```

---

# 🔁 20. Positional Arguments with Loops

A function can receive positional arguments and process them using loops.

Example:

```python
def print_numbers(start, end):
    for number in range(start, end + 1):
        print(number)

print_numbers(1, 5)
```

Output:

```text
1
2
3
4
5
```

Here:

```text
start ← 1
end   ← 5
```

---

# 🧩 21. Positional Arguments with Lists

A list can be passed as a positional argument.

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

The entire list is passed as the first positional argument.

---

# 🧩 22. Positional Arguments with Dictionaries

A dictionary can also be passed as a positional argument.

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

# 🔀 23. Passing Different Data Types Positionally

Example:

```python
def profile(name, age, skills):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)

profile(
    "Asha",
    20,
    ["Python", "SQL", "Git"]
)
```

Output:

```text
Name: Asha
Age: 20
Skills: ['Python', 'SQL', 'Git']
```

Each argument occupies a different position.

---

# ⚖️ 24. Positional Arguments vs Parameters

| Concept             | Meaning                                  |
| ------------------- | ---------------------------------------- |
| Parameter           | Variable in function definition          |
| Argument            | Actual value passed during function call |
| Positional argument | Argument assigned according to position  |

Example:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

Here:

```text
name → Parameter
"Asha" → Positional Argument
```

---

# 🔢 25. Multiple Positional Arguments Example

Example:

```python
def employee(name, age, department, salary):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)
    print("Salary:", salary)

employee("Neha", 24, "Development", 45000)
```

Output:

```text
Name: Neha
Age: 24
Department: Development
Salary: 45000
```

Mapping:

```text
name       ← "Neha"
age        ← 24
department ← "Development"
salary     ← 45000
```

---

# 🧠 26. Positional Arguments with Default Parameters

A function can have default parameter values.

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

The first argument is positional.

The second parameter uses its default value.

---

# 🔄 27. Positional Argument Overriding a Default Value

A positional argument can provide a different value for a parameter with a default.

Example:

```python
def student(name, course="BCA"):
    print(name, course)

student("Asha", "MCA")
```

Output:

```text
Asha MCA
```

Here:

```text
name   ← "Asha"
course ← "MCA"
```

The supplied positional argument replaces the default value.

---

# ⚠️ 28. Positional Arguments Before Default Parameters

Python requires parameters without defaults to appear before parameters with defaults.

Correct:

```python
def student(name, age=20):
    print(name, age)
```

Incorrect:

```python
def student(age=20, name):
    print(name, age)
```

Typical error:

```text
SyntaxError: non-default argument follows default argument
```

Remember:

```text
Required parameters
        ↓
Default parameters
```

---

# 🔗 29. Positional Arguments and Keyword Arguments

Python allows positional and keyword arguments.

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

# ⚠️ 30. Positional Arguments Must Come Before Keyword Arguments

Correct:

```python
def student(name, age, course):
    print(name, age, course)

student("Asha", age=20, course="BCA")
```

Incorrect:

```python
student(name="Asha", 20, "BCA")
```

Typical error:

```text
SyntaxError: positional argument follows keyword argument
```

Remember:

```text
Positional arguments
        ↓
Keyword arguments
```

---

# 🧠 31. Positional Arguments and Function Flexibility

Positional arguments make functions reusable.

Example:

```python
def square(number):
    return number * number

print(square(5))
print(square(10))
print(square(20))
```

Output:

```text
25
100
400
```

The same function works with different arguments.

---

# 🔁 32. Reusing a Function with Different Positional Arguments

Example:

```python
def greet(name):
    print("Welcome", name)

greet("Asha")
greet("Neha")
greet("Kiran")
```

Output:

```text
Welcome Asha
Welcome Neha
Welcome Kiran
```

The parameter remains the same while the positional argument changes.

---

# 🧮 33. Real-World Example: Product Billing

```python
def calculate_bill(price, quantity):
    return price * quantity

bill = calculate_bill(1500, 3)

print("Total Bill:", bill)
```

Output:

```text
Total Bill: 4500
```

Mapping:

```text
price    ← 1500
quantity ← 3
```

---

# 🌍 34. Real-World Example: Student Result

```python
def result(name, marks):
    if marks >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print(name, ":", status)

result("Asha", 78)
```

Output:

```text
Asha : Pass
```

---

# 🌍 35. Real-World Example: Employee Salary

```python
def employee_salary(name, salary):
    print("Employee:", name)
    print("Salary:", salary)

employee_salary("Neha", 45000)
```

Output:

```text
Employee: Neha
Salary: 45000
```

---

# 🌍 36. Real-World Example: Shipping Cost

```python
def shipping_cost(weight, rate):
    return weight * rate

cost = shipping_cost(5, 80)

print("Shipping Cost:", cost)
```

Output:

```text
Shipping Cost: 400
```

Here:

```text
weight ← 5
rate   ← 80
```

---

# 🌍 37. Real-World Example: User Profile

```python
def create_profile(username, age, city):
    print("Username:", username)
    print("Age:", age)
    print("City:", city)

create_profile("asha20", 20, "Bengaluru")
```

Output:

```text
Username: asha20
Age: 20
City: Bengaluru
```

---

# 🌍 38. Real-World Example: Shopping Cart

```python
def cart_total(product, price, quantity):
    total = price * quantity
    print(product, "Total:", total)

cart_total("Laptop", 55000, 2)
```

Output:

```text
Laptop Total: 110000
```

---

# 🌍 39. Real-World Example: Temperature Conversion

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

temperature = celsius_to_fahrenheit(25)

print("Temperature:", temperature)
```

Output:

```text
Temperature: 77.0
```

---

# 🌍 40. Real-World Example: Course Registration

```python
def register_student(name, course, semester):
    print("Student:", name)
    print("Course:", course)
    print("Semester:", semester)

register_student("Asha", "BCA", 4)
```

Output:

```text
Student: Asha
Course: BCA
Semester: 4
```

---

# 🧠 41. Positional Arguments with `*args`

Python also provides `*args` for accepting a variable number of positional arguments.

Example:

```python
def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40))
```

Output:

```text
30
60
100
```

`*args` collects positional arguments into a tuple.

---

# 🔢 42. Understanding `*args`

Example:

```python
def display(*args):
    print(args)

display(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

The positional arguments are collected into a tuple:

```text
10
20
30
 ↓
args
 ↓
(10, 20, 30)
```

---

# 🔄 43. Normal Positional Arguments with `*args`

A function can have normal parameters followed by `*args`.

Example:

```python
def student(name, *subjects):
    print("Name:", name)
    print("Subjects:", subjects)

student("Asha", "Python", "SQL", "Git")
```

Output:

```text
Name: Asha
Subjects: ('Python', 'SQL', 'Git')
```

Here:

```text
name → first positional argument
subjects → remaining positional arguments
```

---

# ⚠️ 44. Common Mistake: Wrong Argument Order

Consider:

```python
def employee(name, salary):
    print(name)
    print(salary)

employee(45000, "Neha")
```

The program may run because both arguments are valid Python values.

But the values are assigned incorrectly:

```text
name   ← 45000
salary ← "Neha"
```

This can produce incorrect program logic.

---

# ⚠️ 45. Common Mistake: Forgetting Required Arguments

Example:

```python
def calculate(price, quantity):
    return price * quantity

calculate(500)
```

This produces a `TypeError` because `quantity` has not been supplied.

Correct:

```python
calculate(500, 3)
```

---

# ⚠️ 46. Common Mistake: Supplying Too Many Arguments

Example:

```python
def greet(name):
    print("Hello", name)

greet("Asha", "BCA")
```

Typical error:

```text
TypeError: greet() takes 1 positional argument but 2 were given
```

The function expects only one positional argument.

---

# ⚠️ 47. Common Mistake: Mixing Positional and Keyword Arguments Incorrectly

Incorrect:

```python
def student(name, age, course):
    print(name, age, course)

student(name="Asha", 20, "BCA")
```

A positional argument cannot follow a keyword argument.

Correct:

```python
student("Asha", 20, "BCA")
```

or:

```python
student("Asha", age=20, course="BCA")
```

---

# 📊 48. Positional Arguments Comparison

| Situation                   | Result                                |
| --------------------------- | ------------------------------------- |
| Correct number of arguments | Function executes                     |
| Too few arguments           | `TypeError`                           |
| Too many arguments          | `TypeError`                           |
| Correct order               | Values assigned correctly             |
| Wrong order                 | Values assigned incorrectly           |
| Positional before keyword   | Valid                                 |
| Positional after keyword    | `SyntaxError`                         |
| `*args`                     | Accepts variable positional arguments |

---

# 💻 49. Practice Programs

## 🟢 Easy

### Program 1: Greet a User

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

### Program 4: Display Product Details

```python
def product(name, price):
    print("Product:", name)
    print("Price:", price)

product("Laptop", 55000)
```

---

# 🟡 Medium

### Program 5: Calculate Total Price

```python
def total_price(price, quantity):
    return price * quantity

print(total_price(500, 4))
```

---

### Program 6: Check Pass or Fail

```python
def check_result(name, marks):
    if marks >= 40:
        print(name, "Passed")
    else:
        print(name, "Failed")

check_result("Asha", 75)
```

---

### Program 7: Calculate Employee Salary

```python
def employee(name, salary):
    print("Employee:", name)
    print("Salary:", salary)

employee("Neha", 45000)
```

---

### Program 8: Calculate Rectangle Area

```python
def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)

print("Area:", area)
```

---

# 🔴 Advanced

## Program 9: Calculate Student Average

```python
def average(name, marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    average_marks = total / 3

    print("Student:", name)
    print("Average:", average_marks)

average("Asha", 85, 90, 80)
```

Output:

```text
Student: Asha
Average: 85.0
```

---

## Program 10: Shopping Cart Calculation

```python
def cart_total(product, price, quantity):
    total = price * quantity

    print("Product:", product)
    print("Total:", total)

cart_total("Laptop", 55000, 2)
```

---

## Program 11: Employee Bonus Calculation

```python
def calculate_bonus(name, salary, percentage):
    bonus = salary * percentage / 100

    print("Employee:", name)
    print("Bonus:", bonus)

calculate_bonus("Neha", 45000, 10)
```

---

## Program 12: Shipping Cost Calculator

```python
def shipping(weight, rate):
    cost = weight * rate

    print("Weight:", weight)
    print("Shipping Cost:", cost)

shipping(8, 75)
```

---

# 🏆 50. Challenge

Create a function for a **student result management system**.

The function should accept the following positional arguments:

```text
Student Name
Python Marks
SQL Marks
Git Marks
HTML Marks
```

Then:

1. Display the student's name.
2. Display each subject mark.
3. Calculate total marks.
4. Calculate average marks.
5. Check whether the student passed or failed.
6. Display the result.
7. Call the function using positional arguments.
8. Try calling the function with the arguments in the wrong order.
9. Observe what happens.
10. Try calling the function with too few arguments.
11. Observe the error.

Example data:

```python
def student_result(name, python, sql, git, html):
    # write your logic here
    pass

student_result(
    "Asha",
    90,
    85,
    80,
    88
)
```

Try solving the challenge without copying a complete solution.

---

# 🧪 51. Mini Project: Employee Salary Management

Create a function that accepts these positional arguments:

```text
Employee Name
Department
Basic Salary
Experience
```

Example:

```python
def employee_details(name, department, salary, experience):
    # write your logic here
    pass

employee_details(
    "Neha",
    "Development",
    45000,
    2
)
```

Perform the following operations:

* Display the employee name.
* Display the department.
* Display the salary.
* Display experience.
* Calculate a bonus based on salary.
* Display the final salary.
* Use positional arguments when calling the function.
* Call the function for at least three employees.
* Try changing the order of arguments and observe the result.

### Your Goal

Build a reusable employee salary function using **positional arguments**.

---

# 🎤 52. Interview Questions

* [ ] What are positional arguments in Python?
* [ ] Why are they called positional arguments?
* [ ] What is the difference between a parameter and an argument?
* [ ] How does Python match positional arguments to parameters?
* [ ] Why does the order of positional arguments matter?
* [ ] What happens if too few positional arguments are supplied?
* [ ] What happens if too many positional arguments are supplied?
* [ ] Can positional arguments have different data types?
* [ ] Can positional arguments be used with return statements?
* [ ] Can positional arguments be used with default parameters?
* [ ] What is the correct order of positional and keyword arguments?
* [ ] What happens if a positional argument follows a keyword argument?
* [ ] What is `*args`?
* [ ] How does `*args` handle positional arguments?
* [ ] Can a function accept normal positional arguments and `*args`?
* [ ] What is the difference between positional and keyword arguments?
* [ ] Why can passing positional arguments in the wrong order cause logical errors?
* [ ] Can lists and dictionaries be passed as positional arguments?
* [ ] What is a required positional argument?
* [ ] How can positional arguments make functions reusable?

---

# 📝 53. Assignment

Complete the following programs.

### Task 1

Create a function that accepts:

```text
name
age
```

Use positional arguments to display both values.

---

### Task 2

Create a function that accepts two numbers and returns their sum.

Call the function using positional arguments.

---

### Task 3

Create a function that accepts:

```text
product
price
quantity
```

Calculate the total price.

---

### Task 4

Create a function that accepts:

```text
name
marks
```

Use an `if` statement to display whether the student passed or failed.

---

### Task 5

Create a function that accepts:

```text
name
course
semester
```

Display all student information.

---

### Task 6

Create a function that accepts:

```text
length
width
```

Calculate the area of a rectangle.

---

### Task 7

Create a function that accepts:

```text
employee_name
salary
bonus_percentage
```

Calculate the bonus.

---

### Task 8

Create a function with one normal positional parameter and a default parameter.

Example structure:

```python
def student(name, course="BCA"):
    pass
```

Call it once using only the positional argument and once using both arguments.

---

### Task 9

Create a function that accepts five subject marks as positional arguments.

Calculate:

```text
Total
Average
```

---

### Task 10

Create a function using `*args` that accepts any number of numbers and calculates their total.

---

### Task 11

Create a real-world function that uses at least four positional arguments.

---

### Task 12

Create a program that intentionally passes positional arguments in the wrong order.

Observe the output and explain why the result is incorrect.

---

# 🧠 54. Memory Tricks

Remember:

```text
Positional Arguments
        ↓
Depend on Position
        ↓
First argument → First parameter
Second argument → Second parameter
Third argument → Third parameter
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

Remember:

```text
def student(name, age):
        ↑     ↑
      param  param

student("Asha", 20)
          ↑      ↑
         arg    arg
```

---

Remember:

```text
Position 1 → Parameter 1
Position 2 → Parameter 2
Position 3 → Parameter 3
```

---

Remember:

```text
Positional Arguments
        ↓
Order Matters
```

---

# 📌 55. Important Rules to Remember

```text
1. Positional arguments are assigned according to their position.

2. The first positional argument goes to the first parameter.

3. The second positional argument goes to the second parameter.

4. The order of positional arguments matters.

5. The number of required arguments must match the function parameters.

6. Too few arguments can produce a TypeError.

7. Too many arguments can produce a TypeError.

8. Positional arguments can contain different data types.

9. Positional arguments can be used with return statements.

10. Positional arguments can be used with default parameters.

11. Positional arguments must come before keyword arguments.

12. A positional argument cannot normally appear after a keyword argument.

13. Lists can be passed as positional arguments.

14. Dictionaries can be passed as positional arguments.

15. Functions can accept multiple positional arguments.

16. *args can collect multiple positional arguments into a tuple.

17. Passing values in the wrong order can create logical errors.

18. Positional arguments make functions reusable.
```

---

# 📊 56. Positional Arguments Structure

```text
                         FUNCTION
                            │
                            ↓
                    Function Definition
                            │
                            ↓
                 ┌──────────┴──────────┐
                 ↓                     ↓
             Parameters             Function Body
                 │
                 ↓
        ┌────────┼────────┐
        ↓        ↓        ↓
       name     age     course
        │        │        │
        ↑        ↑        ↑
        │        │        │
        └────────┼────────┘
                 ↑
                 │
          Positional Arguments
                 │
        ┌────────┼────────┐
        ↓        ↓        ↓
      "Asha"    20      "BCA"
```

---

# 📚 57. Complete Positional Arguments Cheat Sheet

### Basic Function

```python
def greet(name):
    print("Hello", name)
```

### Positional Argument

```python
greet("Asha")
```

### Multiple Positional Arguments

```python
def student(name, age, course):
    print(name, age, course)

student("Asha", 20, "BCA")
```

### Return Value

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

### Positional Argument with Condition

```python
def result(name, marks):
    if marks >= 40:
        print(name, "Passed")
```

### Positional Arguments with Default Parameter

```python
def student(name, course="BCA"):
    print(name, course)
```

### Positional + Keyword

```python
student("Asha", course="BCA")
```

### Variable Positional Arguments

```python
def add(*numbers):
    return sum(numbers)
```

### Calling with Multiple Values

```python
add(10, 20, 30, 40)
```

---

# 🏆 58. Positional Arguments Mastery

```text
                         FUNCTIONS
                             │
                             ↓
                    FUNCTION ARGUMENTS
                             │
              ┌──────────────┴──────────────┐
              ↓                             ↓
         POSITIONAL                      KEYWORD
         ARGUMENTS                      ARGUMENTS
              │                             │
              ↓                             ↓
         Based on Order              Based on Name
              │
       ┌──────┼──────┐
       ↓      ↓      ↓
      1st    2nd    3rd
       ↓      ↓      ↓
      P1     P2     P3
```

The key idea:

```text
Positional Argument
        ↓
Position determines assignment
```

---

# 📚 59. Summary

In this lesson, you learned:

* What positional arguments are.
* Why they are called positional arguments.
* The difference between parameters and arguments.
* How Python maps arguments to parameters.
* Why argument order matters.
* How to pass one positional argument.
* How to pass multiple positional arguments.
* How to use positional arguments with numbers.
* How to use positional arguments with strings.
* How to use positional arguments with different data types.
* How to use positional arguments with return values.
* How to use positional arguments with conditions.
* How to use positional arguments with loops.
* How to pass lists as positional arguments.
* How to pass dictionaries as positional arguments.
* How to use positional arguments with default parameters.
* How positional arguments interact with keyword arguments.
* Why positional arguments must come before keyword arguments.
* What happens when too few arguments are supplied.
* What happens when too many arguments are supplied.
* How incorrect argument order can cause logical errors.
* What `*args` is.
* How `*args` handles multiple positional arguments.
* How positional arguments are used in real-world programs.
* Common mistakes when using positional arguments.
* How to build practical functions using positional arguments.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what positional arguments are.
* [ ] I understand why they are called positional arguments.
* [ ] I understand the difference between parameters and arguments.
* [ ] I know how positional arguments are assigned.
* [ ] I understand why order matters.
* [ ] I can pass one positional argument.
* [ ] I can pass multiple positional arguments.
* [ ] I can use positional arguments with numbers.
* [ ] I can use positional arguments with strings.
* [ ] I can use positional arguments with different data types.
* [ ] I can use positional arguments with return values.
* [ ] I can use positional arguments with conditions.
* [ ] I can use positional arguments with loops.
* [ ] I can pass lists as positional arguments.
* [ ] I can pass dictionaries as positional arguments.
* [ ] I understand positional arguments with default parameters.
* [ ] I understand positional and keyword arguments.
* [ ] I know that positional arguments must come before keyword arguments.
* [ ] I understand `*args`.
* [ ] I can use `*args` to accept multiple positional arguments.
* [ ] I understand common positional argument errors.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use positional arguments without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Keyword Arguments**

In the next topic, you will learn:

* What keyword arguments are.
* Why keyword arguments are useful.
* Basic keyword argument syntax.
* Passing arguments using parameter names.
* Difference between positional and keyword arguments.
* Using multiple keyword arguments.
* Changing the order of keyword arguments.
* Keyword arguments with default parameters.
* Combining positional and keyword arguments.
* Rules for mixing positional and keyword arguments.
* Keyword arguments with return values.
* Keyword arguments with conditions.
* Keyword arguments with loops.
* Practical real-world examples.
* Common mistakes.
* Advanced keyword argument techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Positional arguments teach you an important rule of functions: when the position changes, the meaning can change too."** 🐍📚
