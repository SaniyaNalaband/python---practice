# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 3: Parameters

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what parameters are in Python functions.
* [ ] Understand the difference between parameters and arguments.
* [ ] Create functions with parameters.
* [ ] Pass values to parameters.
* [ ] Use multiple parameters.
* [ ] Understand positional arguments.
* [ ] Understand keyword arguments.
* [ ] Understand default parameters.
* [ ] Use multiple default parameters.
* [ ] Understand the order of parameters.
* [ ] Use keyword arguments with default parameters.
* [ ] Understand variable-length parameters.
* [ ] Use `*args`.
* [ ] Use `**kwargs`.
* [ ] Understand positional-only parameters.
* [ ] Understand keyword-only parameters.
* [ ] Combine different types of parameters.
* [ ] Use parameters with conditions.
* [ ] Use parameters with loops.
* [ ] Use parameters with return values.
* [ ] Use parameters in real-world applications.
* [ ] Avoid common mistakes when using parameters.

---

# 📖 1. What are Parameters?

A **parameter** is a variable written inside the parentheses of a function definition.

Parameters allow a function to receive data from outside the function.

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
```

and:

```text
"Asha"
 ↓
Argument
```

A parameter acts like a placeholder for the value that will be passed to the function.

---

# 🧠 2. Why Do We Use Parameters?

Without parameters, a function always works with the same data.

Example:

```python
def greet():
    print("Hello Asha")

greet()
```

This function can only print the same name.

With a parameter:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
greet("Neha")
greet("Priya")
```

Output:

```text
Hello Asha
Hello Neha
Hello Priya
```

The same function can now work with different data.

---

# 🔍 3. Parameter vs Argument

Parameters and arguments are related, but they are not the same.

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

"Asha"
 ↓
Argument
```

### Parameter

A parameter is the variable defined in the function.

```python
def greet(name):
```

### Argument

An argument is the actual value passed when calling the function.

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

# 📚 4. Basic Function with a Parameter

Example:

```python
def greet(name):
    print("Welcome", name)

greet("Asha")
```

Output:

```text
Welcome Asha
```

The value `"Asha"` is assigned to the parameter `name`.

Conceptually:

```text
name = "Asha"
```

inside the function call.

---

# 🧩 5. Parameter Flow

Consider:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

The flow is:

```text
"Asha"
   ↓
Function Call
   ↓
name parameter
   ↓
print()
   ↓
Hello Asha
```

Parameters allow information to flow into a function.

---

# 🔢 6. Multiple Parameters

A function can have multiple parameters.

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

The values are assigned according to their positions.

---

# 🧠 7. Three Parameters

You can define three or more parameters.

Example:

```python
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info("Asha", 20, "BCA")
```

Output:

```text
Name: Asha
Age: 20
Course: BCA
```

The values are assigned as:

```text
name   → "Asha"
age    → 20
course → "BCA"
```

---

# 🔄 8. Positional Arguments

When arguments are passed according to their position, they are called **positional arguments**.

Example:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student("Asha", 20, "BCA")
```

The first argument goes to the first parameter.

The second argument goes to the second parameter.

The third argument goes to the third parameter.

```text
"Asha" → name
20     → age
"BCA"  → course
```

---

# ⚖️ 9. Position Matters

Consider:

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

If the order changes:

```python
student(20, "Asha")
```

Output:

```text
Name: 20
Age: Asha
```

Python does not automatically understand your intention.

It assigns positional arguments according to their position.

---

# ⚠️ 10. Too Few Arguments

If a function requires more arguments than you provide, Python raises a `TypeError`.

Example:

```python
def student(name, age, course):
    print(name, age, course)

student("Asha", 20)
```

Typical error:

```text
TypeError: student() missing 1 required positional argument: 'course'
```

The function requires three arguments, but only two were provided.

---

# ⚠️ 11. Too Many Arguments

The opposite situation also produces an error.

Example:

```python
def student(name, age):
    print(name, age)

student("Asha", 20, "BCA")
```

Typical error:

```text
TypeError: student() takes 2 positional arguments but 3 were given
```

The number of arguments must match the parameters unless the function is designed to accept variable numbers of arguments.

---

# 🔑 12. Keyword Arguments

Arguments can also be passed using parameter names.

These are called **keyword arguments**.

Example:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student(name="Asha", age=20, course="BCA")
```

Output:

```text
Asha
20
BCA
```

Here Python matches values using parameter names.

---

# 🧠 13. Keyword Arguments Can Change Order

With keyword arguments, the order does not have to match the parameter order.

Example:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student(course="BCA", name="Asha", age=20)
```

Output:

```text
Asha
20
BCA
```

Python uses the parameter names to match the values.

---

# ⚖️ 14. Positional vs Keyword Arguments

| Type       | Meaning                    | Example                        |
| ---------- | -------------------------- | ------------------------------ |
| Positional | Value assigned by position | `student("Asha", 20)`          |
| Keyword    | Value assigned by name     | `student(name="Asha", age=20)` |

Remember:

```text
Positional Argument
        ↓
Position matters

Keyword Argument
        ↓
Parameter name matters
```

---

# 🔀 15. Mixing Positional and Keyword Arguments

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

However, positional arguments must come before keyword arguments.

Correct:

```python
student("Asha", age=20, course="BCA")
```

Incorrect:

```python
student(name="Asha", 20, course="BCA")
```

This produces a syntax error.

---

# ⚙️ 16. Default Parameters

A parameter can have a default value.

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

```python
name="Guest"
```

is a default parameter.

---

# 🔄 17. Replacing a Default Value

A default value is used only when no argument is supplied.

Example:

```python
def greet(name="Guest"):
    print("Hello", name)

greet("Asha")
greet()
```

Output:

```text
Hello Asha
Hello Guest
```

The supplied argument replaces the default value.

---

# 🧩 18. Default Parameter with Another Parameter

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

The `course` parameter automatically receives `"BCA"`.

---

# 🔢 19. Multiple Default Parameters

A function can have multiple default parameters.

Example:

```python
def student(name="Guest", course="BCA", city="Bengaluru"):
    print(name, course, city)

student()
```

Output:

```text
Guest BCA Bengaluru
```

You can also override individual values using keyword arguments.

```python
student(name="Asha", city="Mysuru")
```

Output:

```text
Asha BCA Mysuru
```

---

# ⚠️ 20. Rule for Default Parameters

A parameter with a default value cannot normally appear before a required parameter.

Incorrect:

```python
def student(course="BCA", name):
    print(name, course)
```

This produces:

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
Required parameters
        ↓
Default parameters
```

---

# 🧠 21. Parameter Order

Python functions can use different parameter categories, but their order matters.

A commonly useful order is:

```text
1. Positional / required parameters
2. Default parameters
3. *args
4. Keyword-only parameters
5. **kwargs
```

For example:

```python
def example(name, age=20, *skills, city="Bengaluru", **details):
    pass
```

Understanding parameter order becomes important when working with advanced functions.

---

# 📦 22. Passing Lists to Parameters

A parameter can receive a list.

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

The parameter `skills` receives the entire list.

---

# 📦 23. Passing Tuples to Parameters

Example:

```python
def display_numbers(numbers):
    for number in numbers:
        print(number)

numbers = (10, 20, 30)

display_numbers(numbers)
```

Output:

```text
10
20
30
```

Parameters can receive different types of objects.

---

# 🗂️ 24. Passing Dictionaries to Parameters

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

A parameter can receive a dictionary just like any other object.

---

# 🧮 25. Parameters with Calculations

Parameters are extremely useful for calculations.

Example:

```python
def calculate_total(price, quantity):
    total = price * quantity
    print("Total:", total)

calculate_total(500, 3)
```

Output:

```text
Total: 1500
```

The function can calculate totals for different prices and quantities.

---

# 🔁 26. Parameters with Loops

Parameters can provide data to loops.

Example:

```python
def print_numbers(numbers):
    for number in numbers:
        print(number)

print_numbers([10, 20, 30, 40])
```

Output:

```text
10
20
30
40
```

---

# 🔍 27. Parameters with Conditions

Parameters can also be used with conditions.

Example:

```python
def check_marks(mark):
    if mark >= 40:
        print("Pass")
    else:
        print("Fail")

check_marks(75)
```

Output:

```text
Pass
```

The parameter `mark` controls the condition.

---

# 🎯 28. Parameters with Return Values

Parameters become especially useful when combined with `return`.

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

The flow is:

```text
10, 20
   ↓
parameters a, b
   ↓
a + b
   ↓
return 30
   ↓
result
```

---

# 🧠 29. Parameters Make Functions Reusable

Without parameters:

```python
def calculate():
    print(10 + 20)
```

The function always performs the same calculation.

With parameters:

```python
def calculate(a, b):
    print(a + b)

calculate(10, 20)
calculate(50, 25)
calculate(100, 200)
```

Output:

```text
30
75
300
```

Parameters make functions reusable.

---

# 🧩 30. Function with Three Parameters

Example:

```python
def calculate_bill(price, quantity, discount):
    total = price * quantity
    total = total - discount
    print("Final Bill:", total)

calculate_bill(1000, 3, 200)
```

Output:

```text
Final Bill: 2800
```

Here:

```text
price    → 1000
quantity → 3
discount → 200
```

---

# 🏷️ 31. Keyword Arguments in Real-World Functions

Keyword arguments can make function calls easier to understand.

Example:

```python
def employee(name, department, salary):
    print(name, department, salary)

employee(
    name="Neha",
    department="Development",
    salary=45000
)
```

Keyword arguments clearly communicate what each value represents.

---

# 🔄 32. Default Parameters in Real-World Functions

Example:

```python
def create_profile(name, city="Bengaluru"):
    print("Name:", name)
    print("City:", city)

create_profile("Asha")
```

Output:

```text
Name: Asha
City: Bengaluru
```

The default city is used when no city is provided.

---

# 🌍 33. Real-World Example: Student Information

```python
def student_info(name, age, course="BCA"):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info("Asha", 20)
```

Output:

```text
Name: Asha
Age: 20
Course: BCA
```

The default course is automatically assigned.

---

# 🌍 34. Real-World Example: Shopping Cart

```python
def calculate_cart(price, quantity):
    total = price * quantity
    print("Cart Total:", total)

calculate_cart(1500, 2)
```

Output:

```text
Cart Total: 3000
```

The function can be reused for different products.

---

# 🌍 35. Real-World Example: Employee Salary

```python
def employee_salary(basic_salary, bonus=5000):
    total = basic_salary + bonus
    print("Total Salary:", total)

employee_salary(40000)
```

Output:

```text
Total Salary: 45000
```

The bonus has a default value of `5000`.

---

# 🌍 36. Real-World Example: Login System

```python
def login(username, role="User"):
    print("Username:", username)
    print("Role:", role)

login("asha20")
```

Output:

```text
Username: asha20
Role: User
```

The role can be changed when needed:

```python
login("admin01", role="Admin")
```

Output:

```text
Username: admin01
Role: Admin
```

---

# 🧮 37. Real-World Example: Product Price

```python
def product_price(price, quantity=1):
    total = price * quantity
    return total

print(product_price(500))
print(product_price(500, 3))
```

Output:

```text
500
1500
```

The default quantity is `1`.

---

# 🧠 38. Parameters and Mutable Objects

Python parameters receive references to objects.

Consider:

```python
def add_skill(skills):
    skills.append("Python")

my_skills = ["SQL", "Git"]

add_skill(my_skills)

print(my_skills)
```

Output:

```text
['SQL', 'Git', 'Python']
```

The list was modified because lists are mutable.

---

# ⚖️ 39. Parameters and Immutable Objects

Consider an integer:

```python
def change_number(number):
    number = 100

x = 50

change_number(x)

print(x)
```

Output:

```text
50
```

Changing the local parameter `number` does not change `x`.

This is related to Python's object-reference model and mutability.

---

# 🔢 40. Variable-Length Positional Parameters: `*args`

Sometimes we do not know how many positional arguments will be provided.

Python provides `*args`.

Example:

```python
def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    print(total)

add_numbers(10, 20)
add_numbers(10, 20, 30, 40)
```

Output:

```text
30
100
```

`*args` collects multiple positional arguments into a tuple.

---

# 🧠 41. Understanding `*args`

Example:

```python
def show(*items):
    print(items)

show("Python", "SQL", "Git")
```

Output:

```text
('Python', 'SQL', 'Git')
```

So:

```text
Multiple positional arguments
            ↓
          *args
            ↓
          tuple
```

---

# 🔁 42. Looping Through `*args`

Example:

```python
def display(*skills):
    for skill in skills:
        print(skill)

display("Python", "SQL", "Git")
```

Output:

```text
Python
SQL
Git
```

---

# 🔢 43. Regular Parameter with `*args`

A normal parameter can appear before `*args`.

Example:

```python
def student(name, *skills):
    print("Name:", name)

    for skill in skills:
        print("Skill:", skill)

student("Asha", "Python", "SQL", "Git")
```

Output:

```text
Name: Asha
Skill: Python
Skill: SQL
Skill: Git
```

Here:

```text
name   → "Asha"
skills → ("Python", "SQL", "Git")
```

---

# 🔑 44. Variable-Length Keyword Parameters: `**kwargs`

Sometimes we want to accept any number of keyword arguments.

Python provides `**kwargs`.

Example:

```python
def student_info(**details):
    print(details)

student_info(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

`**kwargs` collects keyword arguments into a dictionary.

---

# 🧠 45. Understanding `**kwargs`

The flow is:

```text
Multiple keyword arguments
            ↓
         **kwargs
            ↓
        dictionary
```

Example:

```python
def show(**data):
    for key, value in data.items():
        print(key, ":", value)

show(name="Asha", city="Bengaluru")
```

Output:

```text
name : Asha
city : Bengaluru
```

---

# ⚖️ 46. `*args` vs `**kwargs`

| Feature        | `*args`              | `**kwargs`         |
| -------------- | -------------------- | ------------------ |
| Accepts        | Positional arguments | Keyword arguments  |
| Stores data as | Tuple                | Dictionary         |
| Example        | `func(10, 20)`       | `func(x=10, y=20)` |
| Symbol         | `*`                  | `**`               |

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

# 🔀 47. Using `*args` and `**kwargs` Together

Example:

```python
def display(name, *skills, **details):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", details)

display(
    "Asha",
    "Python",
    "SQL",
    city="Bengaluru",
    course="BCA"
)
```

Output:

```text
Name: Asha
Skills: ('Python', 'SQL')
Details: {'city': 'Bengaluru', 'course': 'BCA'}
```

This allows a function to accept flexible data.

---

# 🚪 48. Positional-Only Parameters

Python allows parameters to be defined as positional-only using `/`.

Example:

```python
def add(a, b, /):
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

The parameters before `/` must be supplied positionally.

This is not allowed:

```python
add(a=10, b=20)
```

---

# 🔐 49. Keyword-Only Parameters

Python also allows parameters that must be supplied using keywords.

The `*` can be used to define keyword-only parameters.

Example:

```python
def student(name, *, course):
    print(name, course)

student("Asha", course="BCA")
```

Output:

```text
Asha BCA
```

This is not allowed:

```python
student("Asha", "BCA")
```

because `course` is keyword-only.

---

# 🧠 50. Positional-Only and Keyword-Only Together

Example:

```python
def student(name, /, age, *, course):
    print(name, age, course)

student("Asha", 20, course="BCA")
```

Here:

```text
name
 ↓
Positional-only

age
 ↓
Can be positional or keyword

course
 ↓
Keyword-only
```

This is an advanced parameter concept.

---

# 🧩 51. Combining Parameter Types

A function can combine different parameter types.

Example:

```python
def employee(name, age=20, *skills, city="Bengaluru", **details):
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("City:", city)
    print("Details:", details)

employee(
    "Asha",
    21,
    "Python",
    "SQL",
    city="Mysuru",
    department="Development"
)
```

Output:

```text
Name: Asha
Age: 21
Skills: ('Python', 'SQL')
City: Mysuru
Details: {'department': 'Development'}
```

---

# ⚠️ 52. Common Mistake: Forgetting Required Arguments

Incorrect:

```python
def calculate(a, b):
    return a + b

calculate(10)
```

The function requires two arguments.

Correct:

```python
calculate(10, 20)
```

---

# ⚠️ 53. Common Mistake: Wrong Argument Order

Consider:

```python
def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)

employee(45000, "Neha")
```

Output:

```text
Name: 45000
Salary: Neha
```

The arguments were supplied in the wrong order.

Keyword arguments can make the call clearer:

```python
employee(name="Neha", salary=45000)
```

---

# ⚠️ 54. Common Mistake: Positional Argument After Keyword Argument

Incorrect:

```python
def student(name, age, course):
    print(name, age, course)

student(name="Asha", 20, course="BCA")
```

This produces a syntax error.

Correct:

```python
student("Asha", age=20, course="BCA")
```

---

# ⚠️ 55. Common Mistake: Default Parameter Before Required Parameter

Incorrect:

```python
def student(course="BCA", name):
    print(name, course)
```

Correct:

```python
def student(name, course="BCA"):
    print(name, course)
```

Required parameters should come before default parameters.

---

# ⚠️ 56. Common Mistake: Reusing Mutable Default Values

Consider:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("Python"))
print(add_item("SQL"))
```

The output is:

```text
['Python']
['Python', 'SQL']
```

The same default list is reused between calls.

A safer approach is:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

This creates a new list when no list is supplied.

---

# 🧠 57. Parameters with User Input

Parameters can receive values obtained through `input()`.

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

The flow is:

```text
input()
  ↓
name
  ↓
function argument
  ↓
parameter
```

---

# 🔢 58. Parameters with Numeric Input

Example:

```python
def square(number):
    print("Square:", number * number)

number = int(input("Enter a number: "))

square(number)
```

If the user enters:

```text
5
```

Output:

```text
Square: 25
```

---

# 🌍 59. Real-World Example with Input

Consider a simple shopping system.

```python
def calculate_bill(price, quantity):
    total = price * quantity
    print("Total:", total)

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

calculate_bill(price, quantity)
```

The user provides the data, and the function processes it through parameters.

---

# 📊 60. Real-World Example: Marks

```python
def check_result(name, marks):
    if marks >= 40:
        print(name, "has passed")
    else:
        print(name, "has failed")

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

check_result(name, marks)
```

The function can be reused for many students.

---

# 🏦 61. Real-World Example: Bank Withdrawal

```python
def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")

withdraw(50000, 12000)
```

Output:

```text
Remaining Balance: 38000
```

The function receives the balance and withdrawal amount through parameters.

---

# 🛒 62. Real-World Example: Discount Calculator

```python
def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

price = calculate_discount(5000, 10)

print("Final Price:", price)
```

Output:

```text
Final Price: 4500.0
```

---

# 🧑‍💼 63. Real-World Example: Employee Profile

```python
def employee_profile(name, department, salary, city="Bengaluru"):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("City:", city)

employee_profile(
    "Neha",
    "Development",
    45000
)
```

Output:

```text
Name: Neha
Department: Development
Salary: 45000
City: Bengaluru
```

---

# 🧠 64. Parameters and Function Reusability

One function can process many different values.

```python
def calculate_area(length, width):
    return length * width

print(calculate_area(10, 5))
print(calculate_area(20, 8))
print(calculate_area(15, 4))
```

Output:

```text
50
160
60
```

Instead of writing three separate functions, one parameterized function can handle all three cases.

---

# 📌 65. Parameter Scope

Parameters are local variables.

Example:

```python
def greet(name):
    print(name)

greet("Asha")
```

The parameter `name` exists inside the function's local scope.

Trying to use it outside the function:

```python
print(name)
```

may produce:

```text
NameError
```

unless another variable named `name` exists outside the function.

---

# 🔄 66. Parameter Values Change Between Calls

Example:

```python
def greet(name):
    print("Hello", name)

greet("Asha")
greet("Neha")
greet("Priya")
```

Output:

```text
Hello Asha
Hello Neha
Hello Priya
```

The parameter receives a different value during each function call.

---

# 🧩 67. Nested Function Calls with Parameters

A function can receive the result of another function.

Example:

```python
def square(number):
    return number * number

def display(result):
    print("Result:", result)

value = square(5)

display(value)
```

Output:

```text
Result: 25
```

The flow is:

```text
5
↓
square()
↓
25
↓
display()
↓
Result: 25
```

---

# 🔗 68. Passing One Function's Result as Another Function's Argument

Example:

```python
def add(a, b):
    return a + b

def multiply(number, factor):
    return number * factor

result = multiply(add(10, 20), 5)

print(result)
```

Output:

```text
150
```

The result of `add()` becomes an argument to `multiply()`.

---

# 📚 69. Parameter Categories

Python functions can use several parameter styles.

| Parameter Type            | Purpose                                  |
| ------------------------- | ---------------------------------------- |
| Required parameter        | Must receive a value                     |
| Default parameter         | Uses a default value if none is supplied |
| `*args`                   | Accepts multiple positional arguments    |
| Keyword-only parameter    | Must be supplied by keyword              |
| `**kwargs`                | Accepts multiple keyword arguments       |
| Positional-only parameter | Must be supplied positionally            |

---

# 📊 70. Parameter Structure

```text
                         FUNCTION PARAMETERS
                                  │
             ┌────────────────────┼────────────────────┐
             ↓                    ↓                    ↓
         REQUIRED              DEFAULT             VARIABLE
             │                    │                    │
             ↓                    ↓             ┌──────┴──────┐
          name              course="BCA"        ↓             ↓
                                               *args       **kwargs
                                                 ↓             ↓
                                               tuple       dictionary
```

---

# ⚖️ 71. Parameters Comparison

| Parameter       | Example     | Main Purpose                |
| --------------- | ----------- | --------------------------- |
| Required        | `name`      | Required input              |
| Default         | `age=20`    | Optional input with default |
| `*args`         | `*numbers`  | Multiple positional values  |
| Keyword-only    | `*, city`   | Must use keyword            |
| `**kwargs`      | `**details` | Multiple keyword values     |
| Positional-only | `name, /`   | Must use position           |

---

# 💡 72. Parameter Best Practices

Good parameter design makes functions easier to understand.

### Use meaningful names

Good:

```python
def calculate_total(price, quantity):
    pass
```

Less clear:

```python
def calculate_total(x, y):
    pass
```

### Keep the number of parameters reasonable

Instead of creating functions with many unrelated parameters, consider using a suitable data structure such as a dictionary or object.

### Use defaults for common values

Example:

```python
def create_account(name, country="India"):
    pass
```

---

# 🧪 73. Practice Programs

## 🟢 Easy

### Program 1: Greet a User

```python
def greet(name):
    print("Hello", name)

greet("Asha")
```

---

### Program 2: Display Age

```python
def display_age(age):
    print("Age:", age)

display_age(20)
```

---

### Program 3: Add Two Numbers

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

### Program 4: Display Student Details

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Asha", 20)
```

---

# 🟡 Medium

### Program 5: Calculate Rectangle Area

```python
def rectangle_area(length, width):
    print("Area:", length * width)

rectangle_area(10, 5)
```

---

### Program 6: Use Keyword Arguments

```python
def student(name, age, course):
    print(name, age, course)

student(
    course="BCA",
    name="Asha",
    age=20
)
```

---

### Program 7: Use Default Parameters

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Asha")
```

---

### Program 8: Calculate Bill

```python
def calculate_bill(price, quantity):
    return price * quantity

total = calculate_bill(1500, 3)

print("Total:", total)
```

---

# 🔴 Advanced

### Program 9: Use `*args`

```python
def total_marks(*marks):
    total = 0

    for mark in marks:
        total += mark

    print("Total:", total)

total_marks(80, 85, 90, 75)
```

Output:

```text
Total: 330
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

### Program 11: Filter Numbers Using Parameters

```python
def display_greater(numbers, limit):
    for number in numbers:
        if number > limit:
            print(number)

display_greater([10, 25, 40, 15, 50], 20)
```

Output:

```text
25
40
50
```

---

### Program 12: Student Result System

```python
def check_result(name, marks):
    if marks >= 40:
        return name + " passed"
    else:
        return name + " failed"

result = check_result("Asha", 85)

print(result)
```

---

# 🏆 74. Challenge

Create a function called:

```text
student_report()
```

The function should accept:

```text
name
age
course
```

Then:

1. Display the student's name.
2. Display the student's age.
3. Display the student's course.
4. Use a default value for the city.
5. Add a parameter for marks.
6. Use an `if` condition to determine pass or fail.
7. Return the result.
8. Call the function using positional arguments.
9. Call the function again using keyword arguments.
10. Test the function with different students.

Example data:

```python
name = "Asha"
age = 20
course = "BCA"
marks = 85
```

Try solving the challenge without copying a solution.

---

# 🧪 75. Mini Project: Employee Information System

Create a function that accepts employee information.

The function should contain parameters for:

* Employee name
* Employee ID
* Department
* Salary
* Experience
* City

Example:

```python
def employee_info(
    employee_id,
    name,
    department,
    salary,
    experience,
    city="Bengaluru"
):
    pass
```

Perform the following operations:

* Display employee information.
* Use a default value for the city.
* Check whether the employee has more than 2 years of experience.
* Calculate an annual salary.
* Return the employee information.
* Call the function using positional arguments.
* Call the function using keyword arguments.

### Your Goal

Build a reusable employee information function using different types of parameters.

---

# 🎤 76. Interview Questions

* [ ] What is a parameter in Python?
* [ ] What is an argument?
* [ ] What is the difference between a parameter and an argument?
* [ ] Why are parameters used in functions?
* [ ] What are positional arguments?
* [ ] What are keyword arguments?
* [ ] Can keyword arguments be passed in any order?
* [ ] What happens if a required argument is missing?
* [ ] What happens if too many arguments are supplied?
* [ ] What is a default parameter?
* [ ] Why are default parameters useful?
* [ ] Where should default parameters appear?
* [ ] What is `*args`?
* [ ] What type of object does `*args` create?
* [ ] What is `**kwargs`?
* [ ] What type of object does `**kwargs` create?
* [ ] What is the difference between `*args` and `**kwargs`?
* [ ] What are positional-only parameters?
* [ ] What are keyword-only parameters?
* [ ] What does `/` mean in a function definition?
* [ ] What does `*` mean when used for keyword-only parameters?
* [ ] Can parameters receive lists?
* [ ] Can parameters receive dictionaries?
* [ ] Can parameters have mutable objects?
* [ ] What is the problem with mutable default parameters?
* [ ] What is parameter scope?
* [ ] Can a function have both `*args` and `**kwargs`?
* [ ] How do parameters make functions reusable?

---

# 📝 77. Assignment

Complete the following programs.

### Task 1

Create a function with a parameter called `name`.

Use it to display:

```text
Hello <name>
```

---

### Task 2

Create a function with two parameters:

```text
number1
number2
```

Calculate and display their sum.

---

### Task 3

Create a function that accepts:

```text
length
width
```

Calculate the area of a rectangle.

---

### Task 4

Create a function with three parameters:

```text
name
age
course
```

Display all three values.

---

### Task 5

Create a function that uses keyword arguments.

Call the function by changing the order of the keyword arguments.

---

### Task 6

Create a function with a default parameter:

```text
city = "Bengaluru"
```

Call the function once without providing the city and once with a different city.

---

### Task 7

Create a function that accepts five marks and calculates their total.

---

### Task 8

Create a function using `*args`.

Pass different numbers of values to the function and calculate their sum.

---

### Task 9

Create a function using `**kwargs`.

Pass:

```text
name
age
course
city
```

Display all the information using a loop.

---

### Task 10

Create a function that accepts a list of numbers and a limit.

Display only numbers greater than the limit.

---

### Task 11

Create a real-world function and use at least four different parameters.

Use:

* Required parameters
* A default parameter
* `*args` or `**kwargs`
* A return value

---

### Task 12

Create a student result program using parameters.

The function should accept:

```text
name
marks
```

Use an `if-else` condition to display:

```text
Pass
```

or:

```text
Fail
```

---

# 🧠 78. Memory Tricks

Remember:

```text
PARAMETER
    ↓
Placeholder inside function
```

```text
ARGUMENT
    ↓
Actual value passed to function
```

---

Remember positional arguments:

```text
Position
   ↓
Parameter
```

Example:

```python
student("Asha", 20)
```

```text
"Asha" → first parameter
20     → second parameter
```

---

Remember keyword arguments:

```text
Parameter Name
      ↓
    Value
```

Example:

```python
student(name="Asha", age=20)
```

---

Remember default parameters:

```text
No value supplied
       ↓
Default value used
```

---

Remember:

```text
*args
  ↓
Multiple positional arguments
  ↓
Tuple
```

---

Remember:

```text
**kwargs
  ↓
Multiple keyword arguments
  ↓
Dictionary
```

---

# 📌 79. Important Rules to Remember

```text
1. Parameters are variables defined inside a function definition.

2. Arguments are actual values passed during a function call.

3. Positional arguments are assigned according to position.

4. Keyword arguments are assigned according to parameter names.

5. Positional arguments should come before keyword arguments.

6. Required parameters must receive values.

7. Default parameters provide fallback values.

8. Required parameters normally come before default parameters.

9. *args collects extra positional arguments into a tuple.

10. **kwargs collects extra keyword arguments into a dictionary.

11. Parameters can receive strings, numbers, lists, tuples, dictionaries, and other objects.

12. Parameters can be used with conditions and loops.

13. Parameters can be combined with return values.

14. Parameters make functions reusable.

15. Function parameters have local scope.

16. Avoid mutable objects as default parameter values.

17. / can be used to define positional-only parameters.

18. * can be used to define keyword-only parameters.

19. A function can combine required, default, *args, keyword-only, and **kwargs parameters.

20. Good parameter names make functions easier to understand.
```

---

# 📊 80. Parameters Structure

```text
                         FUNCTION
                            │
                            ↓
                       PARAMETERS
                            │
        ┌───────────────────┼───────────────────┐
        ↓                   ↓                   ↓
     REQUIRED            DEFAULT             VARIABLE
        │                   │                   │
        ↓                   ↓            ┌──────┴──────┐
      name             age=20            ↓             ↓
                                      *args         **kwargs
                                        ↓               ↓
                                      tuple         dictionary
```

---

# 📚 81. Complete Parameters Cheat Sheet

### Basic Parameter

```python
def greet(name):
    print(name)
```

### Multiple Parameters

```python
def add(a, b):
    return a + b
```

### Positional Arguments

```python
add(10, 20)
```

### Keyword Arguments

```python
add(a=10, b=20)
```

### Default Parameter

```python
def greet(name="Guest"):
    print(name)
```

### Variable Positional Parameters

```python
def add(*numbers):
    pass
```

### Variable Keyword Parameters

```python
def display(**details):
    pass
```

### Positional-Only Parameters

```python
def add(a, b, /):
    pass
```

### Keyword-Only Parameters

```python
def student(name, *, course):
    pass
```

### Combined Parameters

```python
def example(name, age=20, *skills, city="Bengaluru", **details):
    pass
```

---

# 🏆 82. Parameters Mastery

```text
                         PARAMETERS
                              │
                              ↓
                    FUNCTION INPUT
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
        POSitional         KEYWORD          DEFAULT
             │                │                │
             ↓                ↓                ↓
         func(10)       func(x=10)        x=10
             │
             ↓
          *args
             │
             ↓
           tuple

        **kwargs
             │
             ↓
        dictionary
```

---

# 📖 83. Summary

In this lesson, you learned:

* What parameters are.
* Why parameters are used.
* The difference between parameters and arguments.
* How to create functions with parameters.
* How positional arguments work.
* How keyword arguments work.
* The difference between positional and keyword arguments.
* How to use multiple parameters.
* How to use default parameters.
* How default parameters work.
* The rules for ordering parameters.
* How to pass lists to functions.
* How to pass tuples to functions.
* How to pass dictionaries to functions.
* How parameters work with conditions.
* How parameters work with loops.
* How parameters work with return values.
* How parameters make functions reusable.
* How parameters interact with mutable objects.
* How parameters interact with immutable objects.
* What `*args` is.
* How `*args` stores positional arguments.
* What `**kwargs` is.
* How `**kwargs` stores keyword arguments.
* The difference between `*args` and `**kwargs`.
* What positional-only parameters are.
* What keyword-only parameters are.
* How to use parameters with user input.
* How to use parameters in real-world programs.
* Common mistakes when using parameters.
* Best practices for designing function parameters.

---

# 🎯 Topic Completion Checklist

* [x] I understand what parameters are.
* [x] I understand what arguments are.
* [x] I understand the difference between parameters and arguments.
* [x] I can create functions with parameters.
* [x] I can use multiple parameters.
* [x] I understand positional arguments.
* [x] I understand keyword arguments.
* [x] I can mix positional and keyword arguments correctly.
* [x] I can use default parameters.
* [x] I understand the order of parameters.
* [x] I can pass lists to functions.
* [x] I can pass tuples to functions.
* [x] I can pass dictionaries to functions.
* [x] I can use parameters with conditions.
* [x] I can use parameters with loops.
* [x] I can use parameters with return values.
* [x] I understand `*args`.
* [x] I understand `**kwargs`.
* [x] I understand the difference between `*args` and `**kwargs`.
* [x] I understand positional-only parameters.
* [x] I understand keyword-only parameters.
* [x] I understand parameter scope.
* [x] I understand mutable default parameter problems.
* [x] I can use parameters with `input()`.
* [x] I can use parameters in real-world programs.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the assignment.
* [x] I can use function parameters without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Arguments**

In the next topic, you will learn:

* What arguments are.
* Difference between parameters and arguments.
* Positional arguments.
* Keyword arguments.
* Default arguments.
* Passing arguments to functions.
* Passing multiple arguments.
* Passing lists as arguments.
* Passing tuples as arguments.
* Passing dictionaries as arguments.
* Unpacking arguments.
* Using `*` for argument unpacking.
* Using `**` for dictionary unpacking.
* Combining positional and keyword arguments.
* Real-world examples.
* Common argument mistakes.
* Advanced argument techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Parameters make functions flexible, reusable, and powerful."** 🐍📚
