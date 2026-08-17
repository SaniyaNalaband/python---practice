# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 11: Scope

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what scope means in Python.
* [ ] Understand why scope is important.
* [ ] Understand Local Scope.
* [ ] Understand Global Scope.
* [ ] Understand Enclosing Scope.
* [ ] Understand Built-in Scope.
* [ ] Understand the LEGB rule.
* [ ] Access local and global variables correctly.
* [ ] Understand how functions create their own scope.
* [ ] Use the `global` keyword.
* [ ] Understand the difference between local and global variables.
* [ ] Understand nested function scope.
* [ ] Use the `nonlocal` keyword.
* [ ] Understand variable shadowing.
* [ ] Understand how Python searches for variables.
* [ ] Combine scope concepts with functions and loops.
* [ ] Understand common scope-related errors.
* [ ] Use scope concepts in real-world programs.

---

# 📖 1. What is Scope?

**Scope** refers to the region of a Python program where a variable or name can be accessed.

In simple words:

> **Scope determines where a variable is available and where Python can find it.**

Example:

```python
def greet():
    message = "Hello"

    print(message)

greet()
```

Output:

```text
Hello
```

Here, `message` is created inside the function.

Therefore, it belongs to the **local scope** of the function.

---

# 🧠 2. Why is Scope Important?

Scope helps Python manage variables and prevents different parts of a program from accidentally interfering with each other.

For example:

```python
def student_details():
    name = "Asha"
    print(name)

student_details()
```

The variable `name` exists inside the function.

It is not automatically available outside the function.

Scope helps us:

* Organize variables.
* Avoid naming conflicts.
* Control where variables can be accessed.
* Create reusable functions.
* Protect local data.
* Manage nested functions.
* Understand how Python searches for variables.

---

# 🌳 3. Types of Scope in Python

Python mainly follows four levels of scope:

| Scope     | Meaning                                       |
| --------- | --------------------------------------------- |
| Local     | Inside the current function                   |
| Enclosing | Inside an outer function of a nested function |
| Global    | At the module/program level                   |
| Built-in  | Names provided by Python                      |

These scopes form the **LEGB rule**.

```text
                 SCOPE
                   │
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      LOCAL     ENCLOSING   GLOBAL
                              │
                              ↓
                           BUILT-IN
```

---

# 📍 4. Local Scope

A variable created inside a function normally belongs to the **local scope**.

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
total
  ↓
Local to calculate()
```

The variable `total` can be accessed inside `calculate()`.

---

# ⚠️ 5. Local Variable Cannot Normally Be Accessed Outside

Example:

```python
def calculate():
    total = 100

calculate()

print(total)
```

This produces an error:

```text
NameError: name 'total' is not defined
```

Why?

Because `total` belongs to the local scope of `calculate()`.

It does not exist in the global scope.

---

# 🧠 6. Understanding Local Scope

Consider:

```python
def employee():
    name = "Neha"
    salary = 45000

    print(name)
    print(salary)

employee()
```

Here:

```text
employee()
     │
     ├── name
     └── salary
```

Both variables belong to the local scope of the function.

---

# 🌍 7. Global Scope

A variable created outside all functions belongs to the **global scope**.

Example:

```python
company = "Tech Solutions"

def display():
    print(company)

display()
```

Output:

```text
Tech Solutions
```

Here:

```text
company
   ↓
Global Scope
```

The function can read the global variable.

---

# 🔍 8. Accessing a Global Variable Inside a Function

Example:

```python
course = "BCA"

def show_course():
    print(course)

show_course()
```

Output:

```text
BCA
```

The function searches for `course`.

Python finds it in the global scope.

---

# ⚖️ 9. Local vs Global Scope

| Local Scope                                            | Global Scope                      |
| ------------------------------------------------------ | --------------------------------- |
| Created inside a function                              | Created outside functions         |
| Available inside that function                         | Available throughout the module   |
| Usually cannot be accessed directly outside            | Can be accessed inside functions  |
| Exists while the relevant function execution is active | Exists for the module's execution |

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
course → Global
name   → Local
```

---

# 🧩 10. Same Variable Name in Local and Global Scope

Python allows the same variable name to exist in different scopes.

Example:

```python
name = "Global Name"

def show():
    name = "Local Name"
    print(name)

show()

print(name)
```

Output:

```text
Local Name
Global Name
```

Why?

Inside the function, Python finds the local variable first.

Outside the function, Python finds the global variable.

---

# 🎭 11. Variable Shadowing

When a local variable has the same name as a global variable, the local variable **shadows** the global variable inside that local scope.

Example:

```python
status = "Available"

def check():
    status = "Busy"
    print(status)

check()

print(status)
```

Output:

```text
Busy
Available
```

Inside `check()`:

```text
status → Busy
```

Outside:

```text
status → Available
```

The local variable temporarily hides the global variable within that function.

---

# 🔎 12. How Python Finds Variables

Python follows a specific search order when looking for a variable.

This is called the:

> **LEGB Rule**

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Python searches in this order:

```text
Local
  ↓
Enclosing
  ↓
Global
  ↓
Built-in
```

It stops when it finds the name.

---

# 🧠 13. The LEGB Rule

Suppose Python encounters:

```python
print(value)
```

Python searches:

```text
1. Local Scope
       ↓
2. Enclosing Scope
       ↓
3. Global Scope
       ↓
4. Built-in Scope
```

If Python cannot find `value` anywhere, it raises:

```text
NameError
```

---

# 📦 14. Local Scope in LEGB

Example:

```python
value = "Global"

def display():
    value = "Local"
    print(value)

display()
```

Output:

```text
Local
```

Python finds `value` in the local scope first.

Therefore:

```text
Local → Found
Global → Not searched
```

---

# 🏠 15. Enclosing Scope

An **enclosing scope** exists when a function is defined inside another function.

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
outer()
   │
   ├── message
   │
   └── inner()
          │
          └── accesses message
```

`message` is not local to `inner()`.

It belongs to the enclosing function `outer()`.

---

# 🔁 16. Understanding Enclosing Scope

Example:

```python
def outer():
    course = "Python"

    def inner():
        print(course)

    inner()

outer()
```

Output:

```text
Python
```

Python searches:

```text
inner local
    ↓
outer enclosing
    ↓
global
    ↓
built-in
```

It finds `course` in the enclosing scope.

---

# 🌐 17. Global Scope in LEGB

Example:

```python
language = "Python"

def outer():
    def inner():
        print(language)

    inner()

outer()
```

Output:

```text
Python
```

Python searches:

```text
inner local
    ↓
outer enclosing
    ↓
global → language found
```

---

# 🐍 18. Built-in Scope

Python has many names that are automatically available.

Examples:

```text
print()
len()
max()
min()
sum()
type()
range()
str()
int()
list()
dict()
```

These belong to the **built-in scope**.

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

Python finds `len` in the built-in scope.

---

# 🧠 19. Complete LEGB Example

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

Python finds:

```text
Local → Found
Enclosing → Not needed
Global → Not needed
Built-in → Not needed
```

---

# 🔍 20. LEGB Example Without Local Variable

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

Python does not find `name` locally inside `inner()`.

So it searches the enclosing scope.

---

# 🔍 21. LEGB Example Without Local or Enclosing Variable

```python
name = "Global"

def outer():

    def inner():
        print(name)

    inner()

outer()
```

Output:

```text
Global
```

Python searches:

```text
Local → Not found
Enclosing → Not found
Global → Found
```

---

# 🔍 22. LEGB Example Using a Built-in

```python
numbers = [10, 20, 30]

def calculate():
    print(len(numbers))

calculate()
```

Output:

```text
3
```

Here:

```text
numbers → Global
len     → Built-in
```

---

# 🔐 23. The `global` Keyword

The `global` keyword is used when you want to modify a global variable from inside a function.

Example:

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

Output:

```text
20
```

Without `global`, assigning to `count` inside the function would create a local variable instead.

---

# ⚠️ 24. Why `global` is Needed

Consider:

```python
count = 10

def update_count():
    count = 20

update_count()

print(count)
```

Output:

```text
10
```

Why?

Because:

```python
count = 20
```

creates a new local variable inside the function.

It does not modify the global `count`.

---

# 🧠 25. Using `global` Correctly

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

Output:

```text
20
```

The `global` keyword tells Python:

> "Use the global variable instead of creating a new local variable."

---

# ⚖️ 26. Without `global` vs With `global`

### Without `global`

```python
score = 50

def change():
    score = 100

change()

print(score)
```

Output:

```text
50
```

### With `global`

```python
score = 50

def change():
    global score
    score = 100

change()

print(score)
```

Output:

```text
100
```

---

# 🧩 27. The `nonlocal` Keyword

The `nonlocal` keyword is used inside a nested function when you want to modify a variable belonging to an enclosing function.

Example:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1

    inner()

    print(count)

outer()
```

Output:

```text
1
```

Here:

```text
count
  ↓
outer() → Enclosing Scope
```

`inner()` modifies that variable using `nonlocal`.

---

# ⚖️ 28. `global` vs `nonlocal`

| Keyword    | Used For                                |
| ---------- | --------------------------------------- |
| `global`   | Modify a global variable                |
| `nonlocal` | Modify an enclosing function's variable |

Example:

```python
total = 0

def outer():
    count = 0

    def inner():
        global total
        nonlocal count
```

Here:

```text
total → Global
count → Enclosing
```

---

# 🏠 29. Nested Functions and Scope

A function can contain another function.

Example:

```python
def outer():

    def inner():
        print("Inside inner function")

    inner()

outer()
```

Output:

```text
Inside inner function
```

The nested function has access to variables from its enclosing function.

---

# 🧠 30. Nested Scope Example

```python
def employee():
    department = "Development"

    def details():
        print(department)

    details()

employee()
```

Output:

```text
Development
```

`department` belongs to the enclosing scope of `details()`.

---

# 🔄 31. Scope with Function Parameters

Function parameters are also local variables.

Example:

```python
def greet(name):
    print(name)

greet("Asha")
```

Here:

```text
name
 ↓
Local variable of greet()
```

The parameter `name` exists within the function's local scope.

---

# ⚠️ 32. Function Parameters and Global Variables

Example:

```python
name = "Global"

def greet(name):
    print(name)

greet("Asha")

print(name)
```

Output:

```text
Asha
Global
```

The function parameter creates a local variable called `name`.

It does not modify the global variable.

---

# 🔢 33. Scope with Loops

Variables created in a loop at the top level are generally available in the surrounding scope.

Example:

```python
for number in range(3):
    print(number)

print(number)
```

Output:

```text
0
1
2
2
```

Python does **not** create a separate scope for a normal `for` loop.

---

# 🧠 34. Important Point About `if` Blocks

`if` statements also do not create a separate scope.

Example:

```python
if True:
    message = "Python"

print(message)
```

Output:

```text
Python
```

The variable remains available in the surrounding scope.

---

# ⚖️ 35. Functions vs Loops and Conditions

Functions create local scope.

Normal loops and `if` statements do not create their own scope.

| Structure       | Creates Local Scope? |
| --------------- | -------------------- |
| Function        | ✅ Yes                |
| Nested function | ✅ Yes                |
| `for` loop      | ❌ No                 |
| `while` loop    | ❌ No                 |
| `if` statement  | ❌ No                 |

Example:

```python
def test():
    if True:
        value = 100

    print(value)

test()
```

Output:

```text
100
```

`value` is local to the function, not specifically to the `if` block.

---

# 🧩 36. Scope with `while` Loop

Example:

```python
def counter():
    count = 1

    while count <= 3:
        print(count)
        count += 1

    print("Final:", count)

counter()
```

Output:

```text
1
2
3
Final: 4
```

The variable `count` belongs to the function's local scope.

The `while` loop does not create another scope.

---

# 🎯 37. Scope and Assignment

Assignment inside a function normally creates a local variable.

Example:

```python
value = 100

def change():
    value = 200
    print(value)

change()

print(value)
```

Output:

```text
200
100
```

The assignment:

```python
value = 200
```

creates a local variable.

---

# ⚠️ 38. Common Scope Error: `UnboundLocalError`

Consider:

```python
count = 10

def update():
    print(count)
    count = 20

update()
```

This produces an error similar to:

```text
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

Why?

Because Python sees:

```python
count = 20
```

inside the function and treats `count` as local.

But the function tries to read that local variable before assigning a value to it.

---

# 🛠️ 39. Fixing `UnboundLocalError` with `global`

```python
count = 10

def update():
    global count
    print(count)
    count = 20

update()
```

Output:

```text
10
```

The global variable is now explicitly used.

---

# 🎭 40. Variable Shadowing with Nested Functions

Example:

```python
name = "Global"

def outer():
    name = "Outer"

    def inner():
        name = "Inner"
        print(name)

    inner()

outer()
```

Output:

```text
Inner
```

The local variable in `inner()` shadows the enclosing variable.

---

# 🔄 41. Scope Search Example

```python
language = "Python"

def outer():
    framework = "Django"

    def inner():
        print(language)
        print(framework)

    inner()

outer()
```

Python searches:

```text
language:
Local → ❌
Enclosing → ❌
Global → ✅

framework:
Local → ❌
Enclosing → ✅
```

---

# 📋 42. Using `locals()`

Python provides the `locals()` function to inspect names available in the current local scope.

Example:

```python
def student():
    name = "Asha"
    age = 20

    print(locals())

student()
```

Output will contain information similar to:

```text
{'name': 'Asha', 'age': 20}
```

`locals()` returns a dictionary representing the current local namespace.

---

# 🌍 43. Using `globals()`

The `globals()` function provides access to the global namespace dictionary.

Example:

```python
course = "Python"

def show():
    print(globals()["course"])

show()
```

Output:

```text
Python
```

Here:

```python
globals()["course"]
```

accesses the global variable.

---

# 🧠 44. `locals()` vs `globals()`

| Function    | Purpose                        |
| ----------- | ------------------------------ |
| `locals()`  | Access current local namespace |
| `globals()` | Access global namespace        |

Example:

```python
course = "Python"

def show():
    topic = "Functions"

    print(locals())
    print(globals()["course"])

show()
```

---

# 🔐 45. Scope and Data Protection

Local scope can help keep temporary data isolated.

Example:

```python
def calculate_salary():
    basic = 30000
    bonus = 5000

    total = basic + bonus

    print(total)

calculate_salary()
```

The calculation variables remain local to the function.

This helps keep the global namespace clean.

---

# 🌍 46. Real-World Example: Employee Salary

```python
company = "Tech Solutions"

def employee_salary():
    salary = 45000
    bonus = 5000

    total = salary + bonus

    print("Company:", company)
    print("Total Salary:", total)

employee_salary()
```

Output:

```text
Company: Tech Solutions
Total Salary: 50000
```

Here:

```text
company → Global
salary  → Local
bonus   → Local
total   → Local
```

---

# 🌍 47. Real-World Example: Student Result

```python
college = "ABC College"

def calculate_result():
    python = 90
    sql = 85
    git = 80

    total = python + sql + git

    print("College:", college)
    print("Total:", total)

calculate_result()
```

Output:

```text
College: ABC College
Total: 255
```

Here:

```text
college → Global
python  → Local
sql     → Local
git     → Local
total   → Local
```

---

# 🌍 48. Real-World Example: Shopping Cart

```python
store = "Online Store"

def calculate_cart():
    laptop = 55000
    mouse = 800
    keyboard = 1500

    total = laptop + mouse + keyboard

    print("Store:", store)
    print("Total:", total)

calculate_cart()
```

Output:

```text
Store: Online Store
Total: 57300
```

---

# 🌍 49. Real-World Example: Counter Using `global`

```python
visits = 0

def visit():
    global visits
    visits += 1

visit()
visit()
visit()

print("Visits:", visits)
```

Output:

```text
Visits: 3
```

Here, the global variable stores information shared across function calls.

---

# 🌍 50. Real-World Example: Nested Configuration

```python
def application():
    environment = "Production"

    def display():
        print("Environment:", environment)

    display()

application()
```

Output:

```text
Environment: Production
```

The nested function accesses the enclosing variable.

---

# 🧩 51. Scope with Multiple Functions

Example:

```python
def first():
    value = 100
    print(value)

def second():
    value = 200
    print(value)

first()
second()
```

Output:

```text
100
200
```

Each function has its own local scope.

Therefore, both functions can use the same variable name without interfering with each other.

---

# 🧠 52. Same Variable Name in Different Functions

```python
def student():
    name = "Asha"
    print(name)

def employee():
    name = "Neha"
    print(name)

student()
employee()
```

Output:

```text
Asha
Neha
```

Here:

```text
student()  → name = Asha
employee() → name = Neha
```

The variables belong to different local scopes.

---

# ⚠️ 53. Common Mistake: Assuming Functions Share Local Variables

Wrong assumption:

```python
def first():
    value = 100

def second():
    print(value)

first()
second()
```

This produces:

```text
NameError: name 'value' is not defined
```

Why?

Because `value` belongs to `first()`.

It is not available in `second()`.

---

# 🧠 54. Passing Data Between Functions

Instead of depending on global variables, pass data through function parameters.

Example:

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

This is generally cleaner than using global variables.

---

# ⚖️ 55. Global Variables vs Function Parameters

### Global Variable

```python
price = 500

def calculate():
    return price * 3
```

### Function Parameter

```python
def calculate(price):
    return price * 3

print(calculate(500))
```

Using parameters often makes functions easier to reuse and test.

---

# 🧠 56. Scope and Return Values

A local variable can be returned from a function.

Example:

```python
def calculate():
    total = 5000
    return total

amount = calculate()

print(amount)
```

Output:

```text
5000
```

Although `total` is local, its value can be returned to the caller.

---

# 🔄 57. Local Variable Lifetime

A local variable is associated with a function call.

Example:

```python
def show():
    message = "Hello"
    print(message)

show()
```

During the function execution:

```text
message → exists in local scope
```

After the function finishes, that local name is no longer accessible from outside the function.

---

# 🧩 58. Closures and Enclosing Scope

A nested function can remember a value from its enclosing scope.

Example:

```python
def create_message():
    message = "Hello"

    def display():
        print(message)

    return display

greet = create_message()

greet()
```

Output:

```text
Hello
```

The inner function retains access to the enclosing variable.

This concept is called a **closure**.

---

# 🧠 59. Understanding Closure

In this example:

```python
def create_message():
    message = "Hello"

    def display():
        print(message)

    return display
```

The variable:

```text
message
```

belongs to the enclosing scope.

The returned `display()` function remembers it.

---

# 🔐 60. Using `nonlocal` in a Closure

Example:

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_function = counter()

print(counter_function())
print(counter_function())
print(counter_function())
```

Output:

```text
1
2
3
```

The `count` variable belongs to the enclosing scope and is modified using `nonlocal`.

---

# ⚖️ 61. `global` vs `nonlocal` vs Local

```text
LOCAL
  ↓
Variable belongs to current function

NONLOCAL
  ↓
Variable belongs to an enclosing function

GLOBAL
  ↓
Variable belongs to the module/program level
```

Example:

```python
total = 0

def outer():
    count = 0

    def inner():
        value = 10
```

Here:

```text
total → Global
count → Enclosing
value → Local
```

---

# 📊 62. Scope Comparison

| Scope     | Created Where?    | Accessible From                  |
| --------- | ----------------- | -------------------------------- |
| Local     | Inside function   | Current function                 |
| Enclosing | Outer function    | Nested functions                 |
| Global    | Outside functions | Module and functions for reading |
| Built-in  | Python itself     | Throughout the program           |

---

# 🧠 63. LEGB Structure

```text
                         VARIABLE SEARCH
                               │
                               ↓
                         ┌───────────┐
                         │  LOCAL    │
                         └─────┬─────┘
                               ↓
                         ┌───────────┐
                         │ ENCLOSING │
                         └─────┬─────┘
                               ↓
                         ┌───────────┐
                         │  GLOBAL   │
                         └─────┬─────┘
                               ↓
                         ┌───────────┐
                         │  BUILT-IN │
                         └───────────┘
```

Python searches from top to bottom.

---

# 🛑 64. Common Scope Mistakes

### Mistake 1: Accessing a local variable outside a function

```python
def show():
    name = "Asha"

show()

print(name)
```

Error:

```text
NameError
```

---

### Mistake 2: Assuming assignment changes a global variable

```python
score = 50

def change():
    score = 100

change()

print(score)
```

Output:

```text
50
```

---

### Mistake 3: Forgetting `global`

```python
count = 0

def increment():
    count += 1
```

This causes an `UnboundLocalError`.

Use:

```python
global count
```

when you intentionally need to modify the global variable.

---

# ⚠️ 65. Common Mistake: Overusing Global Variables

Avoid creating many global variables unnecessarily.

Instead of:

```python
price = 500
quantity = 3

def calculate():
    global price
    global quantity
```

Prefer:

```python
def calculate(price, quantity):
    return price * quantity

print(calculate(500, 3))
```

This makes the function more independent and reusable.

---

# 🧠 66. Scope Best Practice

A good general approach is:

```text
Prefer:
Local variables
      ↓
Function parameters
      ↓
Return values
```

Use global variables only when shared global state is genuinely required.

---

# 🔍 67. Checking Variable Existence

You can use `globals()` and `locals()` to inspect namespaces.

Example:

```python
course = "Python"

def show():
    topic = "Scope"

    print("topic" in locals())
    print("course" in globals())

show()
```

Output:

```text
True
True
```

---

# 🔁 68. Combining Scope with Conditions

```python
status = "Active"

def check_user(age):
    if age >= 18:
        result = "Eligible"
    else:
        result = "Not Eligible"

    print(result)

check_user(20)
```

Output:

```text
Eligible
```

The variable `result` is local to the function.

The `if` statement itself does not create another scope.

---

# 🔢 69. Combining Scope with Loops

```python
def calculate_total():
    total = 0

    for price in [500, 800, 1200]:
        total += price

    return total

print(calculate_total())
```

Output:

```text
2500
```

Here:

```text
total → Local
price → Local to the function's scope
```

The loop does not create a separate function-like scope.

---

# 🌍 70. Real-World Example: Bank Account

```python
bank_name = "ABC Bank"

def account_details(balance):
    bonus = 1000
    final_balance = balance + bonus

    print("Bank:", bank_name)
    print("Final Balance:", final_balance)

account_details(25000)
```

Output:

```text
Bank: ABC Bank
Final Balance: 26000
```

Here:

```text
bank_name     → Global
balance       → Local
bonus         → Local
final_balance → Local
```

---

# 🌍 71. Real-World Example: Student Grade

```python
college = "ABC College"

def calculate_grade(mark):
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    else:
        grade = "C"

    print("College:", college)
    print("Grade:", grade)

calculate_grade(88)
```

Output:

```text
College: ABC College
Grade: B
```

---

# 🌍 72. Real-World Example: Inventory

```python
store = "Online Store"

def inventory_status(stock):
    if stock > 0:
        status = "Available"
    else:
        status = "Out of Stock"

    print(store)
    print(status)

inventory_status(15)
```

Output:

```text
Online Store
Available
```

---

# 🧪 73. Practice Programs

## 🟢 Easy

### Program 1: Create a Local Variable

```python
def show():
    message = "Hello Python"
    print(message)

show()
```

---

### Program 2: Create a Global Variable

```python
course = "Python"

def display():
    print(course)

display()
```

---

### Program 3: Compare Local and Global Variables

```python
name = "Global"

def show():
    name = "Local"
    print(name)

show()
print(name)
```

---

### Program 4: Use a Function Parameter

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

---

# 🟡 Medium

### Program 5: Modify a Global Variable

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)
```

---

### Program 6: Nested Function

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()
```

---

### Program 7: Use `nonlocal`

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()
    increment()

counter()
```

---

### Program 8: Inspect Local Variables

```python
def student():
    name = "Asha"
    age = 20

    print(locals())

student()
```

---

# 🔴 Advanced

## Program 9: Demonstrate LEGB

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

---

## Program 10: Closure Counter

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter_function = counter()

print(counter_function())
print(counter_function())
print(counter_function())
```

Output:

```text
1
2
3
```

---

## Program 11: Employee Salary Scope

```python
company = "Tech Solutions"

def calculate_salary(basic, bonus):
    total = basic + bonus

    print("Company:", company)
    print("Total Salary:", total)

calculate_salary(40000, 5000)
```

---

## Program 12: Student Result Scope

```python
college = "ABC College"

def result(python, sql, git):
    total = python + sql + git

    if total >= 240:
        status = "Excellent"
    else:
        status = "Needs Improvement"

    print("College:", college)
    print("Total:", total)
    print("Status:", status)

result(90, 85, 80)
```

---

# 🏆 74. Challenge

Create a **Student Management Program** using scope concepts.

Your program should contain:

```text
college
student name
Python marks
SQL marks
Git marks
```

Requirements:

1. Create a global variable for the college name.
2. Create a function that accepts student marks as parameters.
3. Calculate the total inside the function.
4. Calculate the average inside the function.
5. Use an `if-elif-else` condition to determine the grade.
6. Display the global college name.
7. Display the student's result.
8. Create a nested function that displays the grade.
9. Use enclosing scope where appropriate.
10. Return the final result from the function.

Example data:

```python
college = "ABC College"

python = 90
sql = 85
git = 80
```

Try solving the challenge without copying a solution.

---

# 🧪 75. Mini Project: Employee Salary Management

Create an **Employee Salary Management System** using Python functions and scope.

Employee information:

```python
company = "Tech Solutions"

employee_name = "Neha"
basic_salary = 45000
bonus = 5000
```

Perform the following operations:

* Create a global variable for the company.
* Create a function for salary calculation.
* Accept salary values through parameters.
* Calculate total salary using local variables.
* Display the company name.
* Determine whether the employee receives a high or standard salary.
* Create a nested function to display the salary category.
* Use enclosing scope where appropriate.
* Return the final salary.
* Display the final result outside the function.

### Your Goal

Build the complete employee salary program while clearly understanding which variables belong to:

```text
Local Scope
Enclosing Scope
Global Scope
Built-in Scope
```

---

# 🎤 76. Interview Questions

* [ ] What is scope in Python?
* [ ] Why is scope important?
* [ ] What is Local Scope?
* [ ] What is Global Scope?
* [ ] What is Enclosing Scope?
* [ ] What is Built-in Scope?
* [ ] What is the LEGB rule?
* [ ] What does LEGB stand for?
* [ ] Where is a local variable created?
* [ ] Where is a global variable created?
* [ ] Can a function access a global variable?
* [ ] Can a global scope directly access a local variable?
* [ ] What happens when the same variable name exists locally and globally?
* [ ] What is variable shadowing?
* [ ] What does the `global` keyword do?
* [ ] Why is `global` needed when modifying a global variable?
* [ ] What does the `nonlocal` keyword do?
* [ ] What is the difference between `global` and `nonlocal`?
* [ ] What is an enclosing scope?
* [ ] Do `if` statements create a new scope?
* [ ] Do `for` loops create a new scope?
* [ ] Do functions create a new scope?
* [ ] What is `UnboundLocalError`?
* [ ] What does `locals()` do?
* [ ] What does `globals()` do?
* [ ] What is variable shadowing?
* [ ] What is a closure?
* [ ] Why should global variables generally be used carefully?
* [ ] How can function parameters help avoid global variables?
* [ ] What happens when Python cannot find a variable in any LEGB scope?

---

# 📝 77. Assignment

Complete the following programs.

### Task 1

Create a function with a local variable called:

```text
name
age
course
```

Display all three values.

---

### Task 2

Create a global variable called:

```text
college
```

Access it inside a function.

---

### Task 3

Create the same variable name in global and local scope.

Observe which value is printed inside and outside the function.

---

### Task 4

Create a global variable called:

```text
count = 0
```

Use the `global` keyword to increase it three times.

---

### Task 5

Create a nested function where the inner function accesses a variable from the outer function.

---

### Task 6

Use `nonlocal` to modify a variable belonging to an outer function.

---

### Task 7

Create a program demonstrating the complete LEGB rule.

Use variables with the same name where appropriate.

---

### Task 8

Create a function that accepts marks as parameters and calculates:

```text
total
average
grade
```

Keep these variables local to the function.

---

### Task 9

Create a real-world program using:

```text
global
local
enclosing
```

scopes.

---

### Task 10

Create a counter using a closure and `nonlocal`.

The counter should increase every time the returned function is called.

---

### Task 11

Create a program using `locals()` to display the local variables inside a function.

---

### Task 12

Create a program using `globals()` to access a global variable.

---

# 🧠 78. Memory Tricks

Remember the four scopes:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Think:

```text
Local
  ↓
Enclosing
  ↓
Global
  ↓
Built-in
```

Python searches from **inside to outside**.

---

Remember:

```text
LOCAL
 ↓
Inside current function
```

```text
ENCLOSING
 ↓
Outer function
```

```text
GLOBAL
 ↓
Outside functions
```

```text
BUILT-IN
 ↓
Python's built-in names
```

---

Remember the keywords:

```text
global
   ↓
Modify global variable

nonlocal
   ↓
Modify enclosing variable
```

---

Remember:

```text
Function
   ↓
Creates scope

if
   ↓
Does not create function-like scope

for
   ↓
Does not create function-like scope

while
   ↓
Does not create function-like scope
```

---

# 📌 79. Important Rules to Remember

```text
1. Scope determines where a variable can be accessed.

2. Python mainly follows four scope levels:
   Local, Enclosing, Global, and Built-in.

3. LEGB stands for:
   Local → Enclosing → Global → Built-in.

4. Python searches for variables according to the LEGB rule.

5. A variable created inside a function normally belongs to local scope.

6. A variable created outside functions normally belongs to global scope.

7. Nested functions can access variables from their enclosing functions.

8. The global keyword allows a function to modify a global variable.

9. The nonlocal keyword allows a nested function to modify an enclosing variable.

10. A local variable can shadow a global variable with the same name.

11. Function parameters are local variables.

12. if statements do not create a separate function-like scope.

13. for loops do not create a separate function-like scope.

14. while loops do not create a separate function-like scope.

15. locals() provides access to the current local namespace.

16. globals() provides access to the global namespace.

17. Avoid unnecessary global variables.

18. Function parameters and return values are often better than global state.

19. A variable that cannot be found through LEGB causes a NameError.

20. Assigning to a variable inside a function normally makes it local unless declared global or nonlocal.
```

---

# 📊 80. Scope Structure

```text
                           SCOPE
                             │
                             ↓
                     ┌───────────────┐
                     │     LEGB      │
                     └───────┬───────┘
                             │
        ┌────────────────────┼────────────────────┐
        ↓                    ↓                    ↓
      LOCAL              ENCLOSING              GLOBAL
        │                    │                    │
        ↓                    ↓                    ↓
 Current Function       Outer Function       Program Level
        │                    │                    │
        └────────────────────┼────────────────────┘
                             ↓
                          BUILT-IN
                             │
                             ↓
                     Python Built-ins
```

---

# 📚 81. Complete Scope Cheat Sheet

### Local Scope

```python
def show():
    name = "Asha"
```

### Global Scope

```python
name = "Asha"
```

### Enclosing Scope

```python
def outer():
    name = "Asha"

    def inner():
        print(name)
```

### Built-in Scope

```python
print(len([10, 20, 30]))
```

### Global Keyword

```python
global count
```

### Nonlocal Keyword

```python
nonlocal count
```

### Local Namespace

```python
locals()
```

### Global Namespace

```python
globals()
```

### LEGB

```text
Local
Enclosing
Global
Built-in
```

---

# 🏆 82. Scope Mastery

```text
                         PYTHON SCOPE
                              │
                              ↓
                            LEGB
                              │
          ┌───────────────────┼───────────────────┐
          ↓                   ↓                   ↓
        LOCAL             ENCLOSING             GLOBAL
          │                   │                   │
          ↓                   ↓                   ↓
     Current Function     Outer Function     Module Level
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ↓
                           BUILT-IN
                              │
                              ↓
                       Python Functions
```

---

# 📚 83. Summary

In this lesson, you learned:

* What scope means in Python.
* Why scope is important.
* What Local Scope is.
* What Global Scope is.
* What Enclosing Scope is.
* What Built-in Scope is.
* How the LEGB rule works.
* How Python searches for variables.
* How functions create their own local scope.
* How function parameters behave as local variables.
* How local and global variables can have the same name.
* What variable shadowing means.
* How to use the `global` keyword.
* How to use the `nonlocal` keyword.
* The difference between `global` and `nonlocal`.
* How nested functions access enclosing variables.
* How loops and conditions behave with scope.
* What `locals()` does.
* What `globals()` does.
* What `UnboundLocalError` means.
* What closures are.
* How scope works in real-world programs.
* Why excessive use of global variables should be avoided.
* How function parameters and return values can be used instead of global state.
* Common mistakes related to scope.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what scope means.
* [ ] I understand why scope is important.
* [ ] I understand Local Scope.
* [ ] I understand Global Scope.
* [ ] I understand Enclosing Scope.
* [ ] I understand Built-in Scope.
* [ ] I understand the LEGB rule.
* [ ] I can identify the scope of a variable.
* [ ] I understand local variables.
* [ ] I understand global variables.
* [ ] I understand variable shadowing.
* [ ] I can use the `global` keyword.
* [ ] I can use the `nonlocal` keyword.
* [ ] I understand nested function scope.
* [ ] I understand how function parameters behave.
* [ ] I understand scope with `if` statements.
* [ ] I understand scope with loops.
* [ ] I can use `locals()`.
* [ ] I can use `globals()`.
* [ ] I understand `UnboundLocalError`.
* [ ] I understand closures.
* [ ] I can combine scope with functions.
* [ ] I can combine scope with conditions.
* [ ] I can combine scope with loops.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can identify LEGB scope without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Function Arguments**

In the next topic, you will learn:

* What function arguments are.
* The difference between parameters and arguments.
* Positional arguments.
* Keyword arguments.
* Default arguments.
* Variable-length arguments.
* `*args`.
* `**kwargs`.
* Combining different types of arguments.
* Argument ordering rules.
* Passing lists to functions.
* Passing dictionaries to functions.
* Unpacking arguments.
* Using `*` for argument unpacking.
* Using `**` for dictionary unpacking.
* Practical real-world examples.
* Common mistakes.
* Advanced argument techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Understanding scope means understanding where your variables live, where Python can find them, and how they interact with your functions."** 🐍📚
