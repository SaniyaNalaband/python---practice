# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 10: Return Statement

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what the `return` statement is.
* [ ] Understand why `return` is used in functions.
* [ ] Understand the difference between `print()` and `return`.
* [ ] Return a single value from a function.
* [ ] Store a returned value in a variable.
* [ ] Use a returned value in expressions.
* [ ] Return different values using conditions.
* [ ] Understand what happens when `return` is executed.
* [ ] Understand that `return` terminates function execution.
* [ ] Return multiple values from a function.
* [ ] Understand how multiple returned values are packed into a tuple.
* [ ] Unpack multiple returned values.
* [ ] Use `return` with loops.
* [ ] Use `return` with conditional statements.
* [ ] Use `return` with parameters.
* [ ] Use `return` in real-world applications.
* [ ] Understand the difference between `return`, `print()`, and `None`.
* [ ] Avoid common mistakes when using `return`.
* [ ] Build reusable functions using returned values.

---

# 📖 1. What is the `return` Statement?

The `return` statement is used inside a function to **send a value back to the place where the function was called**.

It allows a function to produce a result that can be:

* Stored in a variable.
* Used in another expression.
* Passed to another function.
* Compared using conditions.
* Printed later.
* Returned from another function.

Example:

```python
def add():
    return 10 + 20

result = add()

print(result)
```

Output:

```text
30
```

Here:

```text
add()
 ↓
10 + 20
 ↓
return 30
 ↓
result
```

The function calculates `30` and sends it back to the caller.

---

# 🧠 2. Syntax of `return`

The basic syntax is:

```python
def function_name():
    return value
```

Example:

```python
def get_name():
    return "Asha"

name = get_name()

print(name)
```

Output:

```text
Asha
```

The general structure is:

```text
def function():
    return value
```

---

# 🔄 3. How `return` Works

Consider:

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

Execution:

```text
square(5)
    ↓
number = 5
    ↓
5 * 5
    ↓
25
    ↓
return 25
    ↓
result = 25
```

Output:

```text
25
```

The `return` statement sends `25` back to the caller.

---

# 🖨️ 4. `return` vs `print()`

One of the most important concepts is understanding the difference between `return` and `print()`.

Using `print()`:

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Using `return`:

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

The difference is:

```text
print()
   ↓
Displays a value

return
   ↓
Sends a value back
```

---

# ⚖️ 5. Understanding Why `return` is Important

Suppose you need the result of a calculation later.

Using `print()`:

```python
def calculate_total(price, quantity):
    print(price * quantity)

calculate_total(500, 3)
```

The result is displayed, but it is not returned to the caller.

Using `return`:

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(500, 3)

print(total)
```

Output:

```text
1500
```

Now `total` can be used again:

```python
discount = total * 0.10
```

This is why `return` is extremely useful when creating reusable functions.

---

# 📦 6. Returning a Single Value

A function can return one value.

Example:

```python
def get_age():
    return 20

age = get_age()

print(age)
```

Output:

```text
20
```

Another example:

```python
def get_course():
    return "BCA"

course = get_course()

print(course)
```

Output:

```text
BCA
```

The returned value can be any valid Python object.

---

# 🔢 7. Returning Numbers

Functions can return integers and floating-point numbers.

Example:

```python
def calculate_sum():
    return 100 + 200

total = calculate_sum()

print(total)
```

Output:

```text
300
```

Example:

```python
def calculate_average():
    return 87.5

average = calculate_average()

print(average)
```

Output:

```text
87.5
```

---

# 🔤 8. Returning Strings

A function can return a string.

Example:

```python
def get_message():
    return "Welcome to Python"

message = get_message()

print(message)
```

Output:

```text
Welcome to Python
```

The returned string can also be combined with other strings:

```python
def get_name():
    return "Asha"

name = get_name()

print("Hello", name)
```

Output:

```text
Hello Asha
```

---

# 🔘 9. Returning Boolean Values

A function can return `True` or `False`.

Example:

```python
def is_adult(age):
    return age >= 18

result = is_adult(20)

print(result)
```

Output:

```text
True
```

Another example:

```python
def is_even(number):
    return number % 2 == 0

print(is_even(10))
```

Output:

```text
True
```

This is very useful when creating validation functions.

---

# 🧮 10. Returning the Result of an Expression

You do not need to store the calculation in another variable before returning it.

Example:

```python
def multiply(a, b):
    return a * b

print(multiply(5, 6))
```

Output:

```text
30
```

Python calculates:

```text
5 * 6
 ↓
30
 ↓
return 30
```

You can return any expression:

```python
def calculate_total(price, quantity):
    return price * quantity
```

---

# 📥 11. Storing a Returned Value

A returned value can be assigned to a variable.

Example:

```python
def add(a, b):
    return a + b

result = add(15, 25)

print(result)
```

Output:

```text
40
```

Here:

```text
add(15, 25)
      ↓
    return
      ↓
      40
      ↓
result = 40
```

This allows you to reuse the result.

---

# 🔁 12. Using a Returned Value Again

A returned value can be used multiple times.

Example:

```python
def square(number):
    return number * number

result = square(5)

print(result)
print(result + 10)
print(result * 2)
```

Output:

```text
25
35
50
```

The function returned `25`, and that value was stored in `result`.

---

# 🧩 13. Using `return` in Expressions

A function call that returns a value can be directly used in an expression.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20) * 2

print(result)
```

Output:

```text
60
```

Execution:

```text
add(10, 20)
     ↓
    30
     ↓
30 * 2
     ↓
60
```

---

# 🧠 14. Returning a Value from a Parameterized Function

`return` becomes especially useful when functions receive parameters.

Example:

```python
def calculate_area(length, width):
    return length * width

area = calculate_area(10, 5)

print(area)
```

Output:

```text
50
```

The function receives:

```text
length = 10
width = 5
```

Then:

```text
10 * 5
 ↓
50
 ↓
return 50
```

---

# 🛑 15. `return` Terminates a Function

When Python executes a `return` statement, the function immediately stops.

Example:

```python
def test():
    print("Start")
    return 100
    print("End")

result = test()

print(result)
```

Output:

```text
Start
100
```

`"End"` is never printed.

Why?

```text
print("Start")
      ↓
return 100
      ↓
FUNCTION STOPS
      ↓
print("End") is skipped
```

This is one of the most important properties of `return`.

---

# 🚦 16. Code After `return`

Any statement placed after an unconditional `return` in the same execution path will not execute.

Example:

```python
def calculate():
    return 50
    print("This will not execute")

print(calculate())
```

Output:

```text
50
```

The statement after `return` is unreachable during that execution.

---

# 🔀 17. Using `return` with `if`

`return` can be used inside conditional statements.

Example:

```python
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(20))
print(check_age(15))
```

Output:

```text
Adult
Minor
```

The function returns different values depending on the condition.

---

# 🧠 18. Multiple `return` Statements

A function can contain multiple `return` statements.

Example:

```python
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
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

Only one `return` is executed for each function call.

---

# ⚖️ 19. `return` with `if` Without `else`

You do not always need an `else`.

Example:

```python
def check_number(number):
    if number > 0:
        return "Positive"

    return "Not Positive"

print(check_number(10))
print(check_number(-5))
```

Output:

```text
Positive
Not Positive
```

The second `return` acts as the fallback result.

---

# 🔢 20. Returning Values from a Loop

`return` can be used inside a loop.

Example:

```python
def find_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

numbers = [3, 7, 9, 12, 15]

print(find_even(numbers))
```

Output:

```text
12
```

Once `12` is found:

```text
return 12
```

The function immediately stops.

---

# 🛑 21. `return` vs `break`

Both can stop something, but they work differently.

`break` stops a loop:

```python
for number in numbers:
    if number == 10:
        break
```

`return` stops the entire function:

```python
def search(numbers):
    for number in numbers:
        if number == 10:
            return number
```

Remember:

```text
break
 ↓
Stops the loop

return
 ↓
Stops the function
```

---

# 🔎 22. Finding an Item Using `return`

A common use of `return` is searching.

Example:

```python
def find_student(students, name):
    for student in students:
        if student == name:
            return "Student Found"

    return "Student Not Found"

students = ["Asha", "Neha", "Priya"]

print(find_student(students, "Neha"))
```

Output:

```text
Student Found
```

---

# 🧮 23. Returning the Maximum Value

A function can calculate and return a result.

Example:

```python
def find_largest(a, b, c):
    return max(a, b, c)

result = find_largest(25, 70, 45)

print(result)
```

Output:

```text
70
```

The caller receives the calculated result.

---

# 📊 24. Returning the Minimum Value

Example:

```python
def find_smallest(numbers):
    return min(numbers)

numbers = [45, 12, 67, 23]

print(find_smallest(numbers))
```

Output:

```text
12
```

---

# 📈 25. Returning an Average

Example:

```python
def calculate_average(marks):
    return sum(marks) / len(marks)

marks = [80, 90, 70, 85]

average = calculate_average(marks)

print(average)
```

Output:

```text
81.25
```

This demonstrates how returned values can be used for data processing.

---

# 📦 26. Returning Multiple Values

Python allows a function to return multiple values.

Example:

```python
def calculate(a, b):
    return a + b, a - b

result = calculate(20, 5)

print(result)
```

Output:

```text
(25, 15)
```

Python automatically packs the returned values into a tuple.

Conceptually:

```text
return a + b, a - b
            ↓
        (25, 15)
```

---

# 🧩 27. Understanding Multiple Return Values

Consider:

```python
def get_student():
    return "Asha", 20, "BCA"

result = get_student()

print(result)
```

Output:

```text
('Asha', 20, 'BCA')
```

The function returns a tuple containing three values.

Structure:

```text
("Asha", 20, "BCA")
      ↓
    tuple
```

---

# 📤 28. Unpacking Multiple Returned Values

You can unpack the returned tuple into separate variables.

Example:

```python
def get_student():
    return "Asha", 20, "BCA"

name, age, course = get_student()

print(name)
print(age)
print(course)
```

Output:

```text
Asha
20
BCA
```

The values are assigned in order:

```text
"Asha" → name
20     → age
"BCA"  → course
```

---

# 🔄 29. Returning a List

A function can return a list.

Example:

```python
def get_skills():
    return ["Python", "SQL", "Git"]

skills = get_skills()

print(skills)
```

Output:

```text
['Python', 'SQL', 'Git']
```

The returned list can be modified:

```python
skills.append("HTML")

print(skills)
```

Output:

```text
['Python', 'SQL', 'Git', 'HTML']
```

---

# 📚 30. Returning a Dictionary

A function can return a dictionary.

Example:

```python
def get_student():
    return {
        "name": "Asha",
        "age": 20,
        "course": "BCA"
    }

student = get_student()

print(student)
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

This is useful for returning structured information.

---

# 🧮 31. Returning a Set

A function can also return a set.

Example:

```python
def get_skills():
    return {"Python", "SQL", "Git"}

skills = get_skills()

print(skills)
```

The function returns the complete set to the caller.

---

# 🔤 32. Returning `None`

If a function does not explicitly return a value, Python automatically returns `None`.

Example:

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output:

```text
Hello
None
```

The function performs an action but does not return a value.

---

# ⚠️ 33. `return` Without a Value

You can write:

```python
return
```

This immediately stops the function and returns `None`.

Example:

```python
def test():
    print("Start")
    return
    print("End")

result = test()

print(result)
```

Output:

```text
Start
None
```

So:

```python
return
```

is effectively:

```python
return None
```

---

# ⚖️ 34. `return None` vs `return`

These two are equivalent:

```python
return
```

and:

```python
return None
```

Example:

```python
def first():
    return

def second():
    return None

print(first())
print(second())
```

Output:

```text
None
None
```

---

# 🧠 35. `return` and Function Reusability

Returning values makes functions reusable.

Example:

```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)

final_price = calculate_discount(5000, 10)

print(final_price)
```

Output:

```text
4500.0
```

The result can then be used somewhere else:

```python
tax = final_price * 0.18
```

This is much more flexible than simply printing the result inside the function.

---

# 🔗 36. Passing a Returned Value to Another Function

The result of one function can become the argument of another function.

Example:

```python
def get_price():
    return 1000

def add_tax(price):
    return price * 1.18

final_price = add_tax(get_price())

print(final_price)
```

Output:

```text
1180.0
```

Execution:

```text
get_price()
    ↓
  1000
    ↓
add_tax(1000)
    ↓
  1180
```

---

# 🔄 37. Calling a Function Inside Another Function

One function can call another function and return its result.

Example:

```python
def add(a, b):
    return a + b

def calculate():
    return add(10, 20)

print(calculate())
```

Output:

```text
30
```

This allows functions to be combined into larger programs.

---

# 🧩 38. Returning Conditional Results

Example:

```python
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

print(calculate_grade(82))
```

Output:

```text
B
```

The function converts a numerical mark into a grade.

---

# 🧮 39. Returning a Boolean for Validation

Example:

```python
def is_valid_password(password):
    return len(password) >= 8

password = "python123"

if is_valid_password(password):
    print("Valid Password")
else:
    print("Invalid Password")
```

Output:

```text
Valid Password
```

The function returns a Boolean value that can directly be used in an `if` condition.

---

# 🌍 40. Real-World Example: Student Result

```python
def calculate_total(marks):
    return sum(marks)

marks = [85, 90, 78, 88]

total = calculate_total(marks)

print("Total Marks:", total)
```

Output:

```text
Total Marks: 341
```

Here:

```text
marks
 ↓
calculate_total()
 ↓
return total
 ↓
total variable
```

---

# 🌍 41. Real-World Example: Student Grade

```python
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

grade = get_grade(86)

print("Grade:", grade)
```

Output:

```text
Grade: B
```

---

# 🌍 42. Real-World Example: Shopping Cart

```python
def calculate_total(cart):
    total = 0

    for price in cart.values():
        total += price

    return total

cart = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}

total = calculate_total(cart)

print("Cart Total:", total)
```

Output:

```text
Cart Total: 57300
```

The function calculates the total and returns it instead of directly printing it.

---

# 🌍 43. Real-World Example: Employee Salary

```python
def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus

salary = calculate_salary(45000, 5000)

print("Total Salary:", salary)
```

Output:

```text
Total Salary: 50000
```

The returned salary can be used for further calculations.

---

# 🌍 44. Real-World Example: Product Discount

```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)

final_price = calculate_discount(2000, 15)

print("Final Price:", final_price)
```

Output:

```text
Final Price: 1700.0
```

---

# 🌍 45. Real-World Example: Login Validation

```python
def login(username, password):
    if username == "admin" and password == "python123":
        return True

    return False

if login("admin", "python123"):
    print("Login Successful")
else:
    print("Invalid Login")
```

Output:

```text
Login Successful
```

Here, the function returns a Boolean value.

---

# ⚠️ 46. Common Mistake: Using `print()` Instead of `return`

Wrong:

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Correct:

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

Remember:

```text
print()
→ Displays

return
→ Sends back
```

---

# ⚠️ 47. Common Mistake: Expecting Code After `return` to Execute

Wrong assumption:

```python
def test():
    return 10
    print("Hello")

test()
```

`"Hello"` will never be printed.

Correct understanding:

```text
return
 ↓
Function immediately stops
 ↓
Remaining statements are skipped
```

---

# ⚠️ 48. Common Mistake: Forgetting to Return a Value

Consider:

```python
def add(a, b):
    result = a + b

total = add(10, 20)

print(total)
```

Output:

```text
None
```

Why?

The function calculates the result but never returns it.

Correct:

```python
def add(a, b):
    result = a + b
    return result

total = add(10, 20)

print(total)
```

Output:

```text
30
```

---

# ⚠️ 49. Common Mistake: Returning Too Early

Consider:

```python
def check_numbers(numbers):
    for number in numbers:
        if number > 50:
            return number
```

This returns the **first** number greater than `50`, not necessarily the largest number.

For example:

```python
numbers = [20, 70, 90, 60]
```

The function returns:

```text
70
```

because `return` immediately stops the function.

Remember:

```text
return inside loop
       ↓
Stops the loop
       ↓
Stops the function
```

---

# 📊 50. `print()` vs `return` Comparison

| Feature                      | `print()`   | `return` |
| ---------------------------- | ----------- | -------- |
| Displays output              | ✅           | ❌        |
| Sends value back             | ❌           | ✅        |
| Can store result in variable | ❌           | ✅        |
| Stops function               | ❌           | ✅        |
| Can be reused in expressions | ❌           | ✅        |
| Used for function results    | Usually not | ✅        |

Example:

```python
def add(a, b):
    return a + b
```

The returned value can be reused:

```python
result = add(10, 20)

double = result * 2

print(double)
```

Output:

```text
60
```

---

# 🧠 51. `return` Statement Flow

Understand the flow:

```text
                FUNCTION CALL
                      │
                      ↓
              Function executes
                      │
                      ↓
              Does it reach return?
                 /          \
               YES           NO
                ↓             ↓
         Send value back     None
                │
                ↓
        Function terminates
```

This is the basic behavior of the `return` statement.

---

# 💻 52. Practice Programs

## 🟢 Easy

### Program 1: Return a Number

```python
def get_number():
    return 100

result = get_number()

print(result)
```

---

### Program 2: Return a Name

```python
def get_name():
    return "Asha"

name = get_name()

print(name)
```

---

### Program 3: Add Two Numbers

```python
def add(a, b):
    return a + b

result = add(15, 25)

print(result)
```

---

### Program 4: Return a Boolean

```python
def is_even(number):
    return number % 2 == 0

print(is_even(20))
```

---

# 🟡 Medium

### Program 5: Calculate Square

```python
def square(number):
    return number * number

result = square(8)

print(result)
```

---

### Program 6: Calculate Average

```python
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [80, 90, 70, 85]

print(calculate_average(numbers))
```

---

### Program 7: Check Positive or Negative

```python
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-10))
```

---

### Program 8: Return Multiple Values

```python
def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(20, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)
```

---

# 🔴 Advanced

## Program 9: Find First Even Number

```python
def find_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None

numbers = [3, 7, 9, 14, 21]

print(find_even(numbers))
```

Output:

```text
14
```

---

## Program 10: Student Grade Function

```python
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

marks = [95, 82, 68, 45]

for mark in marks:
    print(mark, "→", get_grade(mark))
```

---

## Program 11: Shopping Cart Total

```python
def calculate_total(cart):
    total = 0

    for price in cart.values():
        total += price

    return total

cart = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}

total = calculate_total(cart)

print("Total:", total)
```

---

## Program 12: Employee Salary Calculator

```python
def calculate_salary(basic, bonus):
    return basic + bonus

employee_salary = calculate_salary(45000, 5000)

print("Salary:", employee_salary)
```

---

# 🏆 53. Challenge

Create a function that calculates the result of a student.

Use the following marks:

```text
Python
SQL
Git
HTML
CSS
```

Store the marks in a dictionary.

Then:

1. Create a function that accepts the marks dictionary.
2. Calculate the total marks.
3. Calculate the average.
4. Return both total and average.
5. Store the returned values in separate variables.
6. Create another function that accepts the average.
7. Return a grade based on the average.
8. Display the total.
9. Display the average.
10. Display the grade.

Example data:

```python
marks = {
    "Python": 90,
    "SQL": 85,
    "Git": 80,
    "HTML": 88,
    "CSS": 82
}
```

Try solving the challenge without copying the solution.

---

# 🧪 54. Mini Project: Student Result Management System

Create a student result program using functions and `return`.

Student information:

```python
student = {
    "name": "Asha",
    "course": "BCA",
    "marks": {
        "Python": 90,
        "SQL": 85,
        "Git": 80,
        "HTML": 88
    }
}
```

Perform the following operations:

* Create a function to return the student's name.
* Create a function to calculate and return total marks.
* Create a function to calculate and return average marks.
* Create a function to return the student's grade.
* Use returned values to display the final result.
* Use conditions to determine whether the student passed.
* Display the final student report.

### Your Goal

Build the complete student result management system using functions and the `return` statement.

---

# 🎤 55. Interview Questions

* [ ] What is the `return` statement in Python?
* [ ] Why is `return` used inside a function?
* [ ] What happens when Python executes `return`?
* [ ] Does `return` terminate a function?
* [ ] What is the difference between `return` and `print()`?
* [ ] Can a function return a string?
* [ ] Can a function return a list?
* [ ] Can a function return a dictionary?
* [ ] Can a function return multiple values?
* [ ] How does Python handle multiple returned values?
* [ ] What happens if a function has no `return` statement?
* [ ] What is returned by a function without a `return` statement?
* [ ] What is the difference between `return` and `return None`?
* [ ] Can `return` be used inside a loop?
* [ ] What happens when `return` is used inside a loop?
* [ ] What is the difference between `return` and `break`?
* [ ] Can a function contain multiple `return` statements?
* [ ] Can `return` be used with `if` statements?
* [ ] Can a returned value be stored in a variable?
* [ ] Can the returned value of one function be passed to another function?
* [ ] Why is `return` important for reusable functions?
* [ ] What happens to code written after `return`?
* [ ] Why does a function sometimes return `None` unexpectedly?
* [ ] How can `return` be used for validation?
* [ ] How can `return` be used in real-world applications?

---

# 📝 56. Assignment

Complete the following programs.

### Task 1

Create a function that returns your name.

```text
name
```

Store the returned value in a variable and display it.

---

### Task 2

Create a function that accepts two numbers and returns their sum.

---

### Task 3

Create a function that accepts a number and returns its square.

---

### Task 4

Create a function that accepts a number and returns whether it is even or odd.

---

### Task 5

Create a function that accepts three numbers and returns the largest number.

---

### Task 6

Create a function that accepts a list of marks and returns the total marks.

---

### Task 7

Create a function that accepts a list of marks and returns the average.

---

### Task 8

Create a function that accepts a student's mark and returns:

```text
A
B
C
D
```

based on the mark.

---

### Task 9

Create a function that returns multiple values:

```text
name
age
course
```

Unpack the returned values into separate variables.

---

### Task 10

Create a function that accepts a shopping cart dictionary and returns the total price.

---

### Task 11

Create a function that checks whether a username and password are valid.

Return:

```text
True
```

or:

```text
False
```

---

### Task 12

Create a real-world program that uses at least five functions.

Each function should use `return` to send a result back to the caller.

---

# 🧠 57. Memory Tricks

Remember:

```text
return
   ↓
Send a value back
```

---

Remember:

```text
print()
   ↓
Display

return
   ↓
Send back
```

---

Remember:

```text
return value
      ↓
Function stops
      ↓
Value goes back to caller
```

---

Remember:

```text
return
   ↓
Stops the function
```

---

For multiple values:

```text
return a, b
    ↓
(a, b)
    ↓
Tuple
```

---

Remember:

```text
No return
   ↓
None

return
   ↓
None

return value
   ↓
Value
```

---

Remember:

```text
return inside loop
        ↓
Stops loop
        ↓
Stops function
```

---

Remember:

```text
Function
   ↓
Calculate
   ↓
return
   ↓
Caller receives result
```

---

# 📌 58. Important Rules to Remember

```text
1. The return statement is used inside functions.

2. return sends a value back to the caller.

3. return immediately terminates the function.

4. Code after an executed return statement will not run.

5. A function can return numbers, strings, lists, tuples, dictionaries, sets, and other objects.

6. A function can return True or False.

7. A function can contain multiple return statements.

8. Only the return statement that is reached during execution is executed.

9. A function without a return statement automatically returns None.

10. return without a value is equivalent to return None.

11. print() displays a value, while return sends a value back.

12. A returned value can be stored in a variable.

13. A returned value can be used directly in an expression.

14. A returned value can be passed to another function.

15. Multiple values can be returned using commas.

16. Multiple returned values are packed into a tuple.

17. Returned values can be unpacked into separate variables.

18. return can be used inside if statements.

19. return can be used inside loops.

20. return inside a loop terminates the entire function, not just the loop.

21. break only terminates the loop in which it appears.

22. return makes functions reusable.

23. Functions that return values are useful for calculations and data processing.

24. Avoid using print() when the function's result needs to be reused.

25. A well-designed function generally performs a task and returns a useful result.
```

---

# 📊 Return Statement Structure

```text
                         FUNCTION
                             │
                             ↓
                    Function is called
                             │
                             ↓
                    Function executes
                             │
                             ↓
                      return statement
                             │
                ┌────────────┴────────────┐
                ↓                         ↓
          return value                return
                │                         │
                ↓                         ↓
          Value sent back                None
                │
                ↓
          Function stops
                │
                ↓
         Caller receives result
```

---

# 📚 Return Statement Cheat Sheet

### Return a Value

```python
def get_number():
    return 100
```

### Return a String

```python
def get_name():
    return "Asha"
```

### Return a Calculation

```python
def add(a, b):
    return a + b
```

### Return a Boolean

```python
def is_even(number):
    return number % 2 == 0
```

### Return from a Condition

```python
def check_age(age):
    if age >= 18:
        return "Adult"

    return "Minor"
```

### Return from a Loop

```python
def find_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
```

### Return Multiple Values

```python
def calculate(a, b):
    return a + b, a - b
```

### Unpack Multiple Values

```python
addition, subtraction = calculate(20, 5)
```

### Return a List

```python
def get_skills():
    return ["Python", "SQL", "Git"]
```

### Return a Dictionary

```python
def get_student():
    return {
        "name": "Asha",
        "age": 20
    }
```

### Return `None`

```python
def stop_function():
    return
```

---

# 🏆 Return Statement Mastery

```text
                           RETURN STATEMENT
                                  │
                                  ↓
                         Used inside functions
                                  │
             ┌────────────────────┼────────────────────┐
             ↓                    ↓                    ↓
          RETURN VALUE        RETURN NONE        MULTIPLE VALUES
             │                    │                    │
             ↓                    ↓                    ↓
       Sends result back      Sends None          Returns tuple
             │                                         │
             ↓                                         ↓
       Store in variable                              Unpack
             │                                         │
             ↓                                         ↓
       Reuse the result                         Multiple variables
             │
             ↓
      Use in expressions
```

---

# 📚 Summary

In this lesson, you learned:

* What the `return` statement is.
* Why `return` is used in functions.
* How `return` sends a value back to the caller.
* The difference between `return` and `print()`.
* How to return a single value.
* How to return numbers.
* How to return strings.
* How to return Boolean values.
* How to return the result of an expression.
* How to store returned values in variables.
* How to reuse returned values.
* How `return` terminates function execution.
* What happens to code written after `return`.
* How to use `return` with `if` statements.
* How to use multiple `return` statements.
* How to use `return` inside loops.
* The difference between `return` and `break`.
* How to return multiple values.
* How Python packs multiple returned values into a tuple.
* How to unpack multiple returned values.
* How to return lists.
* How to return dictionaries.
* How to return sets.
* What happens when a function does not return a value.
* The meaning of `None`.
* The difference between `return` and `return None`.
* How to pass returned values to other functions.
* How to use returned values in expressions.
* How to use `return` for validation.
* How to use `return` in real-world applications.
* Common mistakes when using the `return` statement.
* How to build reusable functions using returned values.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what the `return` statement is.
* [ ] I understand why `return` is used.
* [ ] I can return a value from a function.
* [ ] I understand the difference between `return` and `print()`.
* [ ] I can store a returned value in a variable.
* [ ] I can use returned values in expressions.
* [ ] I understand that `return` terminates a function.
* [ ] I understand what happens to code after `return`.
* [ ] I can use `return` with `if`.
* [ ] I can use multiple `return` statements.
* [ ] I can use `return` inside loops.
* [ ] I understand the difference between `return` and `break`.
* [ ] I can return multiple values.
* [ ] I understand tuple packing with multiple return values.
* [ ] I can unpack multiple returned values.
* [ ] I can return lists.
* [ ] I can return dictionaries.
* [ ] I understand `None`.
* [ ] I understand `return` without a value.
* [ ] I can pass returned values to another function.
* [ ] I can use `return` for validation.
* [ ] I can use `return` in real-world programs.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use the `return` statement without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Function Scope**

In the next topic, you will learn:

* What scope means in Python.
* What local variables are.
* What global variables are.
* Understanding local scope.
* Understanding global scope.
* Accessing local variables.
* Accessing global variables.
* The difference between local and global variables.
* How function parameters behave as local variables.
* Using the `global` keyword.
* Modifying global variables inside functions.
* Understanding variable lifetime.
* Understanding the LEGB rule.
* Local scope.
* Enclosing scope.
* Global scope.
* Built-in scope.
* Nested functions and scope.
* Practical real-world examples.
* Common scope-related mistakes.
* Advanced scope concepts.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"A function becomes truly useful when it can return a result that the rest of the program can use."** 🐍📚
