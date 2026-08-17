# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 12: Local Variables

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what local variables are.
* [ ] Understand where local variables are created.
* [ ] Understand the scope of local variables.
* [ ] Understand the lifetime of local variables.
* [ ] Create and use local variables inside functions.
* [ ] Understand local variables and function parameters.
* [ ] Differentiate between local and global variables.
* [ ] Understand the LEGB rule.
* [ ] Understand why local variables cannot normally be accessed outside their function.
* [ ] Understand `UnboundLocalError`.
* [ ] Understand local variables inside conditional statements.
* [ ] Understand local variables inside loops.
* [ ] Understand local variables in nested functions.
* [ ] Understand the difference between local and nonlocal variables.
* [ ] Use `locals()` to inspect local variables.
* [ ] Understand variable lifetime.
* [ ] Avoid common mistakes involving local variables.
* [ ] Use local variables in real-world applications.
* [ ] Combine local variables with parameters, return values, loops, and conditions.

---

# 📖 1. What are Local Variables?

A **local variable** is a variable that is created inside a function and is available only within that function's local scope.

Example:

```python
def calculate():
    total = 100
    print(total)

calculate()
```

Output:

```text
100
```

Here:

```text
calculate() → function
total       → local variable
```

The variable `total` belongs to the function `calculate()`.

---

# 🧠 2. Creating a Local Variable

A variable becomes local when it is assigned inside a function.

Example:

```python
def student_details():
    name = "Asha"
    age = 20

    print(name)
    print(age)

student_details()
```

Output:

```text
Asha
20
```

Here:

```text
name → local variable
age  → local variable
```

Both variables are created inside `student_details()`.

---

# 📚 3. Basic Structure of a Local Variable

The general structure is:

```python
def function_name():
    variable = value
```

Example:

```python
def greet():
    message = "Welcome to Python"

    print(message)

greet()
```

Output:

```text
Welcome to Python
```

The variable `message` exists in the local scope of `greet()`.

---

# 🔍 4. Local Variable Exists Inside the Function

Consider:

```python
def calculate():
    number = 50
    print(number)

calculate()
```

The variable `number` can be accessed inside the function.

```text
Inside calculate()
        ↓
    number = 50
        ↓
   print(number)
```

The function knows about `number` because it is a local variable.

---

# 🚫 5. Accessing a Local Variable Outside the Function

A local variable normally cannot be accessed outside the function where it was created.

Example:

```python
def calculate():
    total = 100

    print(total)

calculate()

print(total)
```

The first `print()` works.

However, the second `print()` causes an error because `total` is not defined in the global scope.

Typical error:

```text
NameError: name 'total' is not defined
```

Remember:

```text
Local variable
     ↓
Available inside its function
     ↓
Not directly available outside
```

---

# 🧠 6. Local Scope

**Scope** means the region of a program where a variable can be accessed.

Example:

```python
def calculate():
    price = 500

    print(price)

calculate()
```

The scope of `price` is the function `calculate()`.

We can visualize it as:

```text
Program
│
├── Global Scope
│
└── calculate()
      │
      └── Local Scope
             │
             └── price
```

---

# 🔄 7. Local Variables in Multiple Functions

Different functions can have local variables with the same name.

Example:

```python
def first():
    message = "Hello"
    print(message)

def second():
    message = "Welcome"
    print(message)

first()
second()
```

Output:

```text
Hello
Welcome
```

Although both functions use the variable name `message`, they are different local variables.

```text
first()
  ↓
message = "Hello"

second()
  ↓
message = "Welcome"
```

Each function has its own local scope.

---

# ⚖️ 8. Same Variable Name in Different Functions

Example:

```python
def calculate_marks():
    marks = 90
    print("Marks:", marks)

def calculate_salary():
    marks = 50000
    print("Salary:", marks)

calculate_marks()
calculate_salary()
```

Output:

```text
Marks: 90
Salary: 50000
```

The variable `marks` in one function does not affect the variable `marks` in another function.

---

# 🔢 9. Local Variables and Parameters

Function parameters are also local to the function.

Example:

```python
def greet(name):
    message = "Hello " + name

    print(message)

greet("Asha")
```

Here:

```text
name    → local parameter
message → local variable
```

Both are available inside `greet()`.

---

# 🧩 10. Parameter vs Local Variable

Example:

```python
def calculate(price):
    tax = price * 0.10
    total = price + tax

    print(total)

calculate(1000)
```

Here:

```text
price → parameter
tax   → local variable
total → local variable
```

All three are local to the function.

---

# 🔐 11. Local Variables Are Independent

A local variable belongs to one particular function call.

Example:

```python
def calculate():
    value = 10
    print(value)

calculate()
```

The variable `value` is created when the function executes.

When the function finishes, its local execution context is no longer active.

---

# ⏳ 12. Lifetime of a Local Variable

The **lifetime** of a local variable generally lasts while the function call is executing.

Example:

```python
def calculate():
    result = 50
    print(result)

calculate()
```

During execution:

```text
Function starts
      ↓
result is created
      ↓
result is used
      ↓
Function finishes
      ↓
Local scope ends
```

This is different from global variables, which normally exist throughout the program's execution.

---

# 🌍 13. Local Variable vs Global Variable

A global variable is created outside functions.

A local variable is created inside a function.

Example:

```python
college = "ABC College"

def student():
    name = "Asha"

    print(college)
    print(name)

student()
```

Here:

```text
college → global variable
name    → local variable
```

---

# ⚖️ 14. Local vs Global Variables

| Feature  | Local Variable                    | Global Variable                        |
| -------- | --------------------------------- | -------------------------------------- |
| Created  | Inside function                   | Outside function                       |
| Scope    | Function                          | Program/module                         |
| Access   | Inside function                   | Generally accessible throughout module |
| Lifetime | During relevant execution/context | Generally throughout program           |
| Example  | `total = 100` inside function     | `total = 100` outside function         |

---

# 🧠 15. Example of Local and Global Variables

```python
course = "BCA"

def student():
    name = "Asha"

    print("Course:", course)
    print("Name:", name)

student()
```

Output:

```text
Course: BCA
Name: Asha
```

The function can read the global variable `course` because no local variable with that name exists.

---

# 🔍 16. Local Variable Shadows Global Variable

If a local variable has the same name as a global variable, the local variable takes precedence inside the function.

Example:

```python
name = "Global Name"

def student():
    name = "Asha"

    print(name)

student()

print(name)
```

Output:

```text
Asha
Global Name
```

Inside the function:

```text
name → Asha
```

Outside the function:

```text
name → Global Name
```

The local variable **shadows** the global variable inside the function.

---

# 🔄 17. Understanding Shadowing

Shadowing occurs when a local variable has the same name as a variable from an outer scope.

Example:

```python
score = 100

def test():
    score = 50
    print(score)

test()

print(score)
```

Output:

```text
50
100
```

The local `score` temporarily hides the global `score` within `test()`.

---

# 🧩 18. Local Variables Inside `if`

An `if` block does not create a separate local scope in Python.

Example:

```python
def check_age(age):

    if age >= 18:
        status = "Adult"

    print(status)

check_age(20)
```

Output:

```text
Adult
```

Here, `status` is local to the **function**, not to the `if` block.

---

# ⚠️ 19. Local Variable Inside Conditional Block

Be careful when the condition is false.

Example:

```python
def check_age(age):

    if age >= 18:
        status = "Adult"

    print(status)

check_age(15)
```

This can produce:

```text
UnboundLocalError
```

Why?

Because `status` was never assigned when the condition was false.

A safer approach is:

```python
def check_age(age):

    status = "Minor"

    if age >= 18:
        status = "Adult"

    print(status)

check_age(15)
```

Output:

```text
Minor
```

---

# 🔁 20. Local Variables Inside Loops

A loop also does not create a separate local scope.

Example:

```python
def calculate():

    for number in range(1, 4):
        square = number ** 2

        print(square)

calculate()
```

Output:

```text
1
4
9
```

The variable `square` is local to the function.

The `for` loop does not create another scope.

---

# 🔢 21. Local Counter Variable

Example:

```python
def count_students():

    count = 0

    for student in ["Asha", "Neha", "Priya"]:
        count += 1

    print("Students:", count)

count_students()
```

Output:

```text
Students: 3
```

Here:

```text
count   → local variable
student → local variable
```

Both belong to the function.

---

# 🧠 22. Local Variables and Return Values

A local variable can be returned from a function.

Example:

```python
def calculate():
    total = 500

    return total

result = calculate()

print(result)
```

Output:

```text
500
```

The variable `total` is local, but its value is returned to the caller.

Important:

```text
Local variable itself
        ↓
stays inside function scope

Returned value
        ↓
can be stored outside
```

---

# 🔄 23. Returning a Local Variable

Example:

```python
def calculate_total(price, quantity):

    total = price * quantity

    return total

amount = calculate_total(500, 3)

print("Total:", amount)
```

Output:

```text
Total: 1500
```

Here:

```text
price    → local parameter
quantity → local parameter
total    → local variable
amount   → variable outside the function
```

---

# 🧮 24. Local Variables for Calculations

Local variables are extremely useful for temporary calculations.

Example:

```python
def calculate_bill(price, tax):

    tax_amount = price * tax
    final_amount = price + tax_amount

    return final_amount

bill = calculate_bill(1000, 0.18)

print("Bill:", bill)
```

Output:

```text
Bill: 1180.0
```

`tax_amount` and `final_amount` are local variables.

---

# 🛡️ 25. Why Use Local Variables?

Local variables help:

* Avoid unnecessary global data.
* Keep data limited to where it is needed.
* Make functions easier to understand.
* Prevent accidental modification of unrelated variables.
* Make programs more modular.
* Reduce naming conflicts.

Example:

```python
def calculate_discount(price):

    discount = price * 0.10
    final_price = price - discount

    return final_price
```

The variables `discount` and `final_price` are needed only for this calculation, so keeping them local is appropriate.

---

# 🧠 26. Local Variables Improve Data Safety

Suppose we have:

```python
def calculate_salary(basic_salary):

    allowance = basic_salary * 0.20
    total_salary = basic_salary + allowance

    return total_salary
```

The temporary variable `allowance` does not need to be accessible throughout the program.

Keeping it local prevents unnecessary global state.

---

# 🌐 27. Real-World Example: Shopping Bill

```python
def calculate_bill(price, quantity):

    subtotal = price * quantity
    tax = subtotal * 0.18
    total = subtotal + tax

    return total

bill = calculate_bill(2000, 2)

print("Final Bill:", bill)
```

Output:

```text
Final Bill: 4720.0
```

Local variables:

```text
price
quantity
subtotal
tax
total
```

They are used for the calculation inside the function.

---

# 🌍 28. Real-World Example: Student Result

```python
def calculate_result(marks):

    total = sum(marks)
    average = total / len(marks)

    return total, average

result = calculate_result([80, 90, 85])

print(result)
```

Output:

```text
(255, 85.0)
```

Here:

```text
marks   → parameter
total   → local variable
average → local variable
```

---

# 💰 29. Real-World Example: Employee Salary

```python
def calculate_salary(basic_salary):

    allowance = basic_salary * 0.20
    bonus = 5000
    total_salary = basic_salary + allowance + bonus

    return total_salary

salary = calculate_salary(40000)

print("Salary:", salary)
```

Output:

```text
Salary: 53000.0
```

The calculation variables are local to the function.

---

# 🏦 30. Real-World Example: Bank Withdrawal

```python
def withdraw(balance, amount):

    remaining_balance = balance - amount

    return remaining_balance

balance = withdraw(10000, 2500)

print("Remaining Balance:", balance)
```

Output:

```text
Remaining Balance: 7500
```

`remaining_balance` is a local variable.

---

# 🧠 31. Local Variables and Function Calls

Every function call creates its own execution context.

Example:

```python
def display():

    number = 10
    print(number)

display()
display()
```

Output:

```text
10
10
```

Each function call executes the function independently.

Conceptually:

```text
First call
   ↓
number = 10

Second call
   ↓
number = 10
```

---

# 🔢 32. Local Variables with Different Arguments

Example:

```python
def calculate_square(number):

    result = number ** 2

    return result

first = calculate_square(5)
second = calculate_square(10)

print(first)
print(second)
```

Output:

```text
25
100
```

The local variable `result` is created during each function call.

---

# ⚠️ 33. Common Mistake: Expecting Local Variables Outside

Wrong:

```python
def calculate():

    total = 500

calculate()

print(total)
```

This produces a `NameError`.

Correct:

```python
def calculate():

    total = 500

    return total

result = calculate()

print(result)
```

Output:

```text
500
```

Use `return` when a value needs to be passed outside the function.

---

# ⚠️ 34. Common Mistake: Assigning a Local Variable Accidentally

Consider:

```python
score = 100

def update_score():

    score = 200
    print(score)

update_score()

print(score)
```

Output:

```text
200
100
```

The assignment:

```python
score = 200
```

creates a local variable inside `update_score()`.

It does not modify the global `score`.

---

# 🚨 35. `UnboundLocalError`

A common mistake occurs when Python determines that a variable is local because it is assigned somewhere inside the function, but the variable is read before that assignment happens.

Example:

```python
score = 100

def update():

    print(score)
    score = 200

update()
```

This produces an error similar to:

```text
UnboundLocalError: cannot access local variable 'score' where it is not associated with a value
```

Why?

Python sees:

```python
score = 200
```

inside the function and treats `score` as local to that function.

But:

```python
print(score)
```

tries to use that local variable before it has been assigned.

---

# 🧠 36. Understanding `UnboundLocalError`

Think of the execution as:

```text
def update():

    score = ?       ← Python considers it local

    print(score)    ← Trying to use it

    score = 200     ← Assignment happens later
```

The local variable does not yet have a value when `print(score)` executes.

Therefore Python raises `UnboundLocalError`.

---

# 🔑 37. Using `global` with a Global Variable

If you intentionally want to modify a global variable from inside a function, Python provides the `global` keyword.

Example:

```python
score = 100

def update():

    global score

    score = 200

update()

print(score)
```

Output:

```text
200
```

However, unnecessary use of global variables can make programs harder to understand.

For most calculations, prefer parameters and return values.

---

# ⚖️ 38. Local Variables vs `global`

| Feature                                | Local Variable | `global` Variable            |
| -------------------------------------- | -------------- | ---------------------------- |
| Created inside function                | Yes            | Can refer to global variable |
| Scope                                  | Function       | Global/module scope          |
| Modified normally inside function      | Yes            | Not directly                 |
| Recommended for temporary calculations | Yes            | Usually no                   |
| Example                                | `total = 100`  | `global total`               |

---

# 🧩 39. Local Variables in Nested Functions

A function can be defined inside another function.

Example:

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

Output:

```text
Hello
```

Here:

```text
message
```

is local to `outer()` but is accessible by the nested `inner()` function.

This introduces another concept called an **enclosing scope**.

---

# 🔍 40. Local vs Enclosing Variable

Example:

```python
def outer():

    message = "Hello"

    def inner():

        name = "Asha"

        print(message)
        print(name)

    inner()

outer()
```

Here:

```text
message → local to outer(), enclosing for inner()
name    → local to inner()
```

The `inner()` function can access `message` from the enclosing function.

---

# 🔗 41. The LEGB Rule

Python searches for variables according to the **LEGB rule**.

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches approximately in this order:

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

Python finds the nearest matching variable first.

---

# 🧠 42. Understanding LEGB with Example

```python
name = "Global"

def outer():

    name = "Enclosing"

    def inner():

        print(name)

    inner()

outer()
```

Output:

```text
Enclosing
```

Why?

Python searches:

```text
Local → no name
Enclosing → name found
```

Therefore it uses:

```text
Enclosing
```

---

# 🔄 43. The `nonlocal` Keyword

The `nonlocal` keyword allows a nested function to modify a variable belonging to its enclosing function.

Example:

```python
def counter():

    count = 0

    def increase():

        nonlocal count
        count += 1

        return count

    print(increase())
    print(increase())

counter()
```

Output:

```text
1
2
```

Here:

```text
count
```

belongs to `counter()`, while `increase()` modifies it using `nonlocal`.

---

# ⚖️ 44. Local vs `nonlocal`

| Keyword / Concept | Meaning                               |
| ----------------- | ------------------------------------- |
| Local             | Variable belongs to current function  |
| `nonlocal`        | Modify variable in enclosing function |
| `global`          | Modify variable in global scope       |

Example:

```text
Local
  ↓
Current function

nonlocal
  ↓
Outer/enclosing function

global
  ↓
Global/module scope
```

---

# 🧪 45. Inspecting Local Variables with `locals()`

Python provides the built-in `locals()` function to inspect the current local namespace.

Example:

```python
def student():

    name = "Asha"
    age = 20

    print(locals())

student()
```

Output will contain entries similar to:

```text
{'name': 'Asha', 'age': 20}
```

`locals()` returns a dictionary-like mapping containing local variables available in the current scope.

---

# 🔍 46. Using `locals()` to Inspect Variables

Example:

```python
def calculate():

    price = 500
    quantity = 2
    total = price * quantity

    print(locals())

calculate()
```

The output contains the local variables:

```text
price
quantity
total
```

This can be useful for debugging and understanding scopes.

---

# ⚠️ 47. `locals()` Is Mainly for Inspection

Although `locals()` exposes local namespace information, it should not normally be used as the main way to create or modify local variables.

Prefer normal assignments:

```python
name = "Asha"
age = 20
```

rather than trying to manipulate local variables through `locals()`.

---

# 🔄 48. Local Variables and Loops with Conditions

Local variables become especially useful when combined with loops and conditions.

Example:

```python
def calculate_passed_students(marks):

    passed = 0

    for mark in marks:

        if mark >= 40:
            passed += 1

    return passed

result = calculate_passed_students([80, 35, 60, 25, 90])

print("Passed:", result)
```

Output:

```text
Passed: 3
```

Here:

```text
marks  → parameter
passed → local variable
mark   → local loop variable
```

---

# 📊 49. Real-World Example: Product Discount

```python
def calculate_discount(price):

    discount = price * 0.10
    final_price = price - discount

    return final_price

price = calculate_discount(5000)

print("Final Price:", price)
```

Output:

```text
Final Price: 4500.0
```

The variables:

```text
discount
final_price
```

are local because they are required only inside the function.

---

# 🌍 50. Real-World Example: Student Grade

```python
def calculate_grade(mark):

    if mark >= 90:
        grade = "A"

    elif mark >= 75:
        grade = "B"

    elif mark >= 60:
        grade = "C"

    else:
        grade = "D"

    return grade

grade = calculate_grade(82)

print("Grade:", grade)
```

Output:

```text
Grade: B
```

The variable `grade` is local to `calculate_grade()`.

---

# 💻 51. Real-World Example: Login System

```python
def login(username, password):

    valid_username = "admin"
    valid_password = "1234"

    if username == valid_username and password == valid_password:
        status = "Login successful"
    else:
        status = "Invalid credentials"

    return status

result = login("admin", "1234")

print(result)
```

Output:

```text
Login successful
```

Local variables:

```text
valid_username
valid_password
status
```

These values are needed only during the function's execution.

---

# 🛒 52. Real-World Example: Shopping Cart

```python
def calculate_cart(prices):

    subtotal = 0

    for price in prices:
        subtotal += price

    discount = subtotal * 0.10
    final_total = subtotal - discount

    return final_total

total = calculate_cart([1000, 500, 1500])

print("Final Total:", total)
```

Output:

```text
Final Total: 2700.0
```

The calculation variables are local to `calculate_cart()`.

---

# 🏦 53. Real-World Example: ATM Withdrawal

```python
def withdraw(balance, amount):

    if amount <= balance:
        remaining = balance - amount
        status = "Withdrawal successful"
    else:
        remaining = balance
        status = "Insufficient balance"

    return status, remaining

status, balance = withdraw(10000, 3000)

print(status)
print("Balance:", balance)
```

Output:

```text
Withdrawal successful
Balance: 7000
```

Local variables:

```text
remaining
status
```

---

# ⚠️ 54. Common Mistake: Confusing Local and Global Variables

Consider:

```python
total = 1000

def calculate():

    total = 500

    print(total)

calculate()

print(total)
```

Output:

```text
500
1000
```

The local variable `total` does not modify the global variable.

Remember:

```text
Inside function  → local total = 500
Outside function → global total = 1000
```

---

# ⚠️ 55. Common Mistake: Forgetting `return`

Consider:

```python
def calculate():

    total = 500

calculate()

print(total)
```

This does not work because `total` is local.

Correct:

```python
def calculate():

    total = 500

    return total

result = calculate()

print(result)
```

Output:

```text
500
```

Use `return` to send a value from a function to the caller.

---

# ⚠️ 56. Common Mistake: Assuming `if` Creates a New Scope

Consider:

```python
def check():

    if True:
        message = "Hello"

    print(message)

check()
```

Output:

```text
Hello
```

The `if` block does not create a separate scope.

`message` is local to the function.

---

# ⚠️ 57. Common Mistake: Assuming Loops Create Scope

Consider:

```python
def calculate():

    for number in range(3):
        result = number * 2

    print(result)

calculate()
```

Output:

```text
4
```

The `for` loop does not create a separate scope.

`result` is local to the function.

---

# 🧠 58. Dictionary of Important Concepts

| Concept         | Meaning                                               |
| --------------- | ----------------------------------------------------- |
| Local variable  | Variable created inside a function                    |
| Local scope     | Region where local variable can be accessed           |
| Parameter       | Local name receiving an argument                      |
| Global variable | Variable defined outside functions                    |
| Shadowing       | Local variable hides an outer variable with same name |
| `return`        | Sends a value from function to caller                 |
| `global`        | Refers to a global variable inside a function         |
| `nonlocal`      | Refers to an enclosing function's variable            |
| `locals()`      | Inspects the current local namespace                  |
| LEGB            | Local → Enclosing → Global → Built-in                 |

---

# 📊 59. Local Variables Comparison

| Situation                        | Example            | Scope          |
| -------------------------------- | ------------------ | -------------- |
| Variable inside function         | `total = 500`      | Local          |
| Function parameter               | `def add(x):`      | Local          |
| Variable inside `if` in function | `if x: result = 1` | Function-local |
| Variable inside loop in function | `for x in data:`   | Function-local |
| Variable outside function        | `total = 500`      | Global         |
| Enclosing function variable      | Nested function    | Enclosing      |
| Built-in name                    | `len`, `print`     | Built-in       |

---

# 💡 60. Why Local Variables Are Important

Local variables are important because they help create:

* Modular programs.
* Reusable functions.
* Cleaner code.
* Safer data handling.
* Fewer naming conflicts.
* Easier debugging.
* Easier maintenance.
* Better separation of responsibilities.

Example:

```python
def calculate_area(length, width):

    area = length * width

    return area
```

The variable `area` does not need to exist globally.

It belongs only to the calculation function.

---

# 🏆 61. Best Practice: Prefer Local Variables

Instead of:

```python
price = 1000
tax = 180
total = price + tax

def display():
    print(total)
```

Prefer:

```python
def calculate_total(price):

    tax = price * 0.18
    total = price + tax

    return total

result = calculate_total(1000)

print(result)
```

This makes the calculation self-contained and reusable.

---

# 🧪 62. Practice Programs

## 🟢 Easy

### Program 1: Create a Local Variable

```python
def student():

    name = "Asha"

    print(name)

student()
```

---

### Program 2: Local Age Variable

```python
def student():

    age = 20

    print("Age:", age)

student()
```

---

### Program 3: Local Calculation

```python
def calculate():

    number = 10
    square = number ** 2

    print(square)

calculate()
```

---

### Program 4: Local Variable with Parameter

```python
def greet(name):

    message = "Hello " + name

    print(message)

greet("Asha")
```

---

# 🟡 Medium

### Program 5: Calculate Total Marks

```python
def calculate_total(marks):

    total = sum(marks)

    return total

result = calculate_total([80, 90, 85])

print("Total:", result)
```

---

### Program 6: Calculate Average

```python
def calculate_average(marks):

    total = sum(marks)
    average = total / len(marks)

    return average

result = calculate_average([80, 90, 70])

print("Average:", result)
```

---

### Program 7: Calculate Shopping Total

```python
def shopping_total(prices):

    total = 0

    for price in prices:
        total += price

    return total

result = shopping_total([500, 800, 1200])

print("Total:", result)
```

---

### Program 8: Local Variable with Condition

```python
def check_result(mark):

    if mark >= 40:
        status = "Pass"
    else:
        status = "Fail"

    return status

result = check_result(75)

print(result)
```

---

# 🔴 Advanced

## Program 9: Student Result System

```python
def student_result(marks):

    total = sum(marks)
    average = total / len(marks)

    if average >= 75:
        grade = "Distinction"
    elif average >= 60:
        grade = "First Class"
    elif average >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    return total, average, grade

total, average, grade = student_result([80, 75, 90])

print("Total:", total)
print("Average:", average)
print("Grade:", grade)
```

---

## Program 10: Employee Salary Calculator

```python
def calculate_salary(basic):

    allowance = basic * 0.20
    bonus = 5000
    total_salary = basic + allowance + bonus

    return total_salary

salary = calculate_salary(40000)

print("Total Salary:", salary)
```

---

## Program 11: Shopping Cart with Discount

```python
def calculate_cart(prices):

    subtotal = 0

    for price in prices:
        subtotal += price

    discount = subtotal * 0.10
    final_total = subtotal - discount

    return subtotal, discount, final_total

subtotal, discount, total = calculate_cart([1000, 2000, 1500])

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Total:", total)
```

---

## Program 12: Bank Withdrawal

```python
def withdraw(balance, amount):

    if amount <= balance:
        remaining_balance = balance - amount
        message = "Withdrawal successful"
    else:
        remaining_balance = balance
        message = "Insufficient balance"

    return message, remaining_balance

message, balance = withdraw(10000, 2500)

print(message)
print("Remaining Balance:", balance)
```

---

# 🏆 63. Challenge

Create a function for a **Student Result Management System**.

The function should receive marks as a parameter.

Then:

1. Create a local variable for the total marks.
2. Create a local variable for the average.
3. Use a condition to determine the grade.
4. Store the grade in a local variable.
5. Return the total, average, and grade.
6. Display the returned values outside the function.
7. Make sure the calculation variables are local to the function.
8. Do not use global variables for the calculation.

Example data:

```text
Python → 90
SQL    → 85
Git    → 78
HTML   → 88
CSS    → 82
```

Try solving the challenge without copying the solution.

---

# 🧪 64. Mini Project: Employee Salary Management System

Create a function that calculates an employee's final salary.

Employee information:

```python
employee = {
    "name": "Neha",
    "basic_salary": 45000,
    "experience": 3
}
```

Inside the function:

* Get the basic salary through a parameter.
* Calculate an allowance.
* Calculate a bonus.
* Calculate the final salary.
* Store each calculation in local variables.
* Return the final salary.
* Display the result outside the function.

### Your Goal

Build the complete employee salary calculation program while keeping temporary calculation variables **local to the function**.

---

# 🎤 65. Interview Questions

* [ ] What is a local variable in Python?
* [ ] Where is a local variable created?
* [ ] What is local scope?
* [ ] Can a local variable normally be accessed outside its function?
* [ ] What happens when you try to access a local variable outside its function?
* [ ] What is the difference between a local and global variable?
* [ ] Can two functions have local variables with the same name?
* [ ] What is variable shadowing?
* [ ] Are function parameters local variables?
* [ ] Do `if` statements create a new local scope in Python?
* [ ] Do `for` loops create a new local scope in Python?
* [ ] What is the lifetime of a local variable?
* [ ] How can a local variable's value be used outside a function?
* [ ] What does `return` do?
* [ ] What is `UnboundLocalError`?
* [ ] Why can `UnboundLocalError` occur when using a global variable inside a function?
* [ ] What does the `global` keyword do?
* [ ] What does the `nonlocal` keyword do?
* [ ] What is the LEGB rule?
* [ ] What does `locals()` do?
* [ ] Why are local variables useful?
* [ ] Can a nested function access a variable from its enclosing function?
* [ ] What is the difference between local and enclosing scope?
* [ ] Why should temporary calculation variables generally be kept local?

---

# 📝 66. Assignment

### Task 1

Create a function containing a local variable called:

```text
name
```

Print the variable inside the function.

---

### Task 2

Create a function that calculates the square of a number.

Use a local variable called:

```text
square
```

---

### Task 3

Create a function that accepts three marks and stores the total in a local variable.

Return the total.

---

### Task 4

Create a function that accepts a price and calculates:

```text
tax
final_price
```

Keep both as local variables.

---

### Task 5

Create a function that determines whether a number is:

```text
Positive
Negative
Zero
```

Store the result in a local variable.

---

### Task 6

Create two functions.

Both functions should have a local variable named:

```text
message
```

Give each function a different value and observe the output.

---

### Task 7

Create a global variable called:

```text
score
```

Create a function with another local variable called:

```text
score
```

Print both from the appropriate scopes.

---

### Task 8

Create a function that calculates a student's average.

Use local variables for:

```text
total
average
```

Return the average.

---

### Task 9

Create a function that calculates an employee's salary.

Use local variables for:

```text
allowance
bonus
final_salary
```

---

### Task 10

Create a nested function and demonstrate the difference between:

```text
local
enclosing
```

variables.

---

### Task 11

Use `locals()` inside a function to inspect at least three local variables.

---

### Task 12

Create a program using a function, loop, and condition where all temporary calculation variables remain local to the function.

---

# 🧠 67. Memory Tricks

Remember:

```text
LOCAL VARIABLE
      ↓
Created inside a function
      ↓
Used inside that function
```

---

Remember:

```text
PARAMETER
    ↓
Local to function

LOCAL VARIABLE
    ↓
Created inside function
```

---

Remember the scope hierarchy:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

---

Remember:

```text
return
   ↓
Send value outside
```

---

Remember:

```text
global
   ↓
Use/modify global variable
```

---

Remember:

```text
nonlocal
   ↓
Modify enclosing function variable
```

---

Remember:

```text
if / for / while
      ↓
Do NOT create a new function scope
```

---

# 📌 68. Important Rules to Remember

```text
1. A local variable is created inside a function.

2. A local variable belongs to the function's local scope.

3. A local variable cannot normally be accessed directly outside its function.

4. Function parameters are local to the function.

5. Different functions can have local variables with the same name.

6. Local variables can shadow global variables with the same name.

7. if statements do not create a separate local scope.

8. for and while loops do not create a separate local scope.

9. A local variable can be returned using return.

10. Returning a value does not make the local variable itself global.

11. Local variables generally exist for the relevant function execution.

12. UnboundLocalError can occur when a local variable is used before assignment.

13. The global keyword can be used to refer to a global variable inside a function.

14. The nonlocal keyword can be used in nested functions to modify an enclosing variable.

15. Python follows the LEGB rule when resolving variable names.

16. locals() can be used to inspect the current local namespace.

17. Temporary calculations should generally use local variables.

18. Local variables help keep functions modular and easier to maintain.

19. Local variables reduce unnecessary global state.

20. Using parameters and return values is generally preferable to relying on global variables.
```

---

# 📊 69. Local Variables Structure

```text
                         FUNCTION
                            │
                            ↓
                      LOCAL SCOPE
                            │
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
      PARAMETERS       LOCAL VARIABLES     LOCAL LOGIC
          │                 │                 │
          ↓                 ↓                 ↓
       name = x          total = 100       if / loop
                            │
                            ↓
                         return
                            │
                            ↓
                     VALUE TO CALLER
```

---

# 📚 70. Complete Local Variable Cheat Sheet

### Create a Local Variable

```python
def calculate():
    total = 500
```

### Access a Local Variable

```python
def calculate():
    total = 500
    print(total)
```

### Return a Local Variable

```python
def calculate():
    total = 500
    return total
```

### Receive a Local Parameter

```python
def calculate(price):
    total = price * 2
```

### Use a Local Variable with Condition

```python
def check(mark):
    if mark >= 40:
        result = "Pass"
```

### Use a Local Variable with Loop

```python
def calculate(numbers):
    total = 0

    for number in numbers:
        total += number
```

### Access an Enclosing Variable

```python
def outer():
    message = "Hello"

    def inner():
        print(message)
```

### Modify an Enclosing Variable

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
```

### Refer to a Global Variable

```python
score = 100

def update():
    global score
    score = 200
```

### Inspect Local Variables

```python
def calculate():
    price = 500
    quantity = 2

    print(locals())
```

---

# 🏆 71. Local Variables Mastery

```text
                         VARIABLES
                             │
             ┌───────────────┼───────────────┐
             ↓               ↓               ↓
          LOCAL          GLOBAL          BUILT-IN
             │
             ↓
        Inside Function
             │
     ┌───────┼────────┐
     ↓       ↓        ↓
 Parameters  Local   Temporary
             Values  Calculations
             │
             ↓
           return
             │
             ↓
       Value to Caller
```

---

# 📚 72. Summary

In this lesson, you learned:

* What local variables are.
* How local variables are created.
* What local scope means.
* How local variables work inside functions.
* Why local variables cannot normally be accessed outside their function.
* How function parameters behave as local variables.
* How multiple functions can have variables with the same name.
* What variable shadowing means.
* The difference between local and global variables.
* How local variables work with `if` statements.
* How local variables work with loops.
* How local variables work with function parameters.
* How to return local values using `return`.
* The lifetime of local variables.
* Why local variables are useful.
* What `UnboundLocalError` means.
* Why `UnboundLocalError` can occur.
* How the `global` keyword works.
* How the `nonlocal` keyword works.
* What enclosing scope means.
* What the LEGB rule means.
* How `locals()` can inspect local variables.
* How local variables can be used in real-world applications.
* Common mistakes involving local variables.
* How to combine local variables with loops and conditions.
* How to design cleaner functions using local variables.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what local variables are.
* [ ] I know where local variables are created.
* [ ] I understand local scope.
* [ ] I can create local variables inside functions.
* [ ] I understand function parameters as local variables.
* [ ] I understand the difference between local and global variables.
* [ ] I understand variable shadowing.
* [ ] I know that `if` blocks do not create a separate function scope.
* [ ] I know that loops do not create a separate function scope.
* [ ] I can return a local variable's value.
* [ ] I understand the lifetime of local variables.
* [ ] I understand `UnboundLocalError`.
* [ ] I understand the `global` keyword.
* [ ] I understand the `nonlocal` keyword.
* [ ] I understand enclosing scope.
* [ ] I understand the LEGB rule.
* [ ] I can use `locals()`.
* [ ] I can use local variables with loops.
* [ ] I can use local variables with conditions.
* [ ] I can use local variables in real-world functions.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can explain local variables without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Global Variables**

In the next topic, you will learn:

* What global variables are.
* Where global variables are created.
* Global scope.
* Accessing global variables inside functions.
* Modifying global variables.
* The `global` keyword.
* Local vs global variables.
* Variable shadowing.
* Global variables with functions.
* Global variables with loops and conditions.
* Global variables in real-world programs.
* Problems with excessive global variables.
* When to use global variables.
* When to avoid global variables.
* Global variables and function parameters.
* Global variables and return values.
* Common mistakes.
* Practice programs and challenges.
* Real-world examples.
* Advanced scope concepts.

---

## ⭐ Quote of the Day

> **"Good functions keep temporary data local, making your programs cleaner, safer, and easier to understand."** 🐍📚
