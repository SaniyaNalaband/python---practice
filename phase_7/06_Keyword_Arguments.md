# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 6: Keyword Arguments

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what keyword arguments are.
* [ ] Understand the difference between positional and keyword arguments.
* [ ] Call functions using keyword arguments.
* [ ] Pass arguments using parameter names.
* [ ] Understand how keyword arguments improve code readability.
* [ ] Change the order of arguments using keyword arguments.
* [ ] Mix positional and keyword arguments correctly.
* [ ] Understand the rules for mixing positional and keyword arguments.
* [ ] Use default parameters with keyword arguments.
* [ ] Override default values using keyword arguments.
* [ ] Understand keyword arguments with multiple parameters.
* [ ] Use keyword arguments with built-in functions.
* [ ] Use keyword arguments with user-defined functions.
* [ ] Understand common mistakes with keyword arguments.
* [ ] Use keyword arguments in real-world applications.
* [ ] Understand keyword-only arguments.
* [ ] Use `**kwargs` to handle variable keyword arguments.
* [ ] Combine keyword arguments with `*args` and `**kwargs`.
* [ ] Build practical programs using keyword arguments.

---

# 📖 1. What are Keyword Arguments?

Keyword arguments are arguments passed to a function by explicitly specifying the **parameter name**.

Instead of depending on the position of an argument, we specify:

```python
parameter_name=value
```

Example:

```python
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(name="Asha", age=20)
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

The parameter names `name` and `age` are explicitly mentioned.

---

# 🧠 2. Understanding Keyword Arguments

Consider:

```python
def student_info(name, age, course):
    print(name)
    print(age)
    print(course)
```

We can call the function using keyword arguments:

```python
student_info(
    name="Asha",
    age=20,
    course="BCA"
)
```

Python matches the values with the corresponding parameter names.

```text
name   → "Asha"
age    → 20
course → "BCA"
```

Therefore, the order of the keyword arguments does not have to match the parameter order.

---

# 📚 3. Basic Syntax of Keyword Arguments

The general syntax is:

```python
function_name(parameter=value)
```

Example:

```python
def greet(name):
    print("Hello", name)

greet(name="Asha")
```

Output:

```text
Hello Asha
```

Here:

```text
name="Asha"
```

is a keyword argument.

---

# ⚖️ 4. Positional Arguments vs Keyword Arguments

There are two common ways to pass arguments.

### Positional argument

```python
def student(name, age):
    print(name, age)

student("Asha", 20)
```

Python matches values according to their position.

```text
"Asha" → name
20     → age
```

### Keyword argument

```python
student(name="Asha", age=20)
```

Python matches values according to their parameter names.

```text
name="Asha" → name
age=20      → age
```

---

# 🔍 5. Understanding Positional Arguments

Positional arguments are matched based on their position.

Example:

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)

employee("Neha", "Development", 45000)
```

Python interprets this as:

```text
1st value → name
2nd value → department
3rd value → salary
```

Output:

```text
Neha
Development
45000
```

---

# 🔑 6. Understanding Keyword Arguments

The same function can be called using keyword arguments:

```python
employee(
    name="Neha",
    department="Development",
    salary=45000
)
```

Output:

```text
Neha
Development
45000
```

The important difference is that the parameter names are explicitly specified.

---

# 🔄 7. Changing the Order of Keyword Arguments

One major advantage of keyword arguments is that the order can be changed.

Example:

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)

employee(
    salary=45000,
    name="Neha",
    department="Development"
)
```

Output:

```text
Neha
Development
45000
```

Even though the order is:

```text
salary
name
department
```

Python knows where each value belongs because the parameter names are specified.

---

# 🧠 8. Why Does Order Not Matter?

With positional arguments:

```python
student("Asha", 20, "BCA")
```

Python uses positions:

```text
1st → name
2nd → age
3rd → course
```

With keyword arguments:

```python
student(
    course="BCA",
    name="Asha",
    age=20
)
```

Python uses parameter names:

```text
course → course
name   → name
age    → age
```

Therefore:

```text
Positional argument → Position matters

Keyword argument → Parameter name matters
```

---

# 🧩 9. Keyword Arguments with Multiple Parameters

Example:

```python
def product(name, price, quantity):
    total = price * quantity

    print("Product:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)

product(
    name="Laptop",
    price=55000,
    quantity=2
)
```

Output:

```text
Product: Laptop
Price: 55000
Quantity: 2
Total: 110000
```

---

# 🔁 10. Reordering Keyword Arguments

We can change the order:

```python
product(
    quantity=2,
    name="Laptop",
    price=55000
)
```

The result remains the same because Python uses the parameter names.

---

# 📌 11. Keyword Arguments Improve Readability

Consider:

```python
create_account("Asha", 20, "BCA", "Bengaluru")
```

A reader must remember what each value represents.

Using keyword arguments:

```python
create_account(
    name="Asha",
    age=20,
    course="BCA",
    city="Bengaluru"
)
```

The meaning of every value is immediately clear.

Therefore, keyword arguments can make function calls:

* More readable
* More understandable
* Easier to maintain
* Less error-prone

---

# 🧠 12. Keyword Arguments with Default Parameters

Keyword arguments work very well with default parameters.

Example:

```python
def student(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)

student(name="Asha")
```

Output:

```text
Name: Asha
Course: BCA
```

The default value `"BCA"` is used.

---

# 🔄 13. Overriding a Default Value

A default value can be replaced using a keyword argument.

Example:

```python
def student(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)

student(name="Asha", course="MCA")
```

Output:

```text
Name: Asha
Course: MCA
```

The default:

```text
course="BCA"
```

was replaced by:

```text
course="MCA"
```

---

# ⚖️ 14. Default Parameter vs Keyword Argument

These are different concepts.

Example:

```python
def greet(name, message="Welcome"):
    print(message, name)
```

Here:

```text
message="Welcome"
```

is a **default parameter**.

When we call:

```python
greet(name="Asha", message="Good Morning")
```

then:

```text
name="Asha"
message="Good Morning"
```

are **keyword arguments**.

Remember:

```text
Default parameter
        ↓
Defined in the function

Keyword argument
        ↓
Used when calling the function
```

---

# 🔀 15. Mixing Positional and Keyword Arguments

Python allows positional and keyword arguments in the same function call.

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
"Asha"     → positional argument
age=20     → keyword argument
course="BCA" → keyword argument
```

---

# ⚠️ 16. Important Rule When Mixing Arguments

When positional and keyword arguments are used together:

> **Positional arguments must come before keyword arguments.**

Correct:

```python
student("Asha", age=20, course="BCA")
```

Incorrect:

```python
student(name="Asha", 20, course="BCA")
```

This produces a `SyntaxError`.

The correct order is:

```text
Positional arguments
        ↓
Keyword arguments
```

---

# ❌ 17. Common Mistake: Positional Argument After Keyword Argument

Incorrect:

```python
def student(name, age):
    print(name, age)

student(name="Asha", 20)
```

This produces:

```text
SyntaxError: positional argument follows keyword argument
```

Correct:

```python
student("Asha", age=20)
```

---

# 🔢 18. Passing All Arguments as Keyword Arguments

You can pass every argument using keywords.

Example:

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)

employee(
    name="Neha",
    department="Development",
    salary=45000
)
```

This is completely valid.

---

# 🔍 19. Keyword Arguments Must Match Parameter Names

Suppose we have:

```python
def student(name, age):
    print(name, age)
```

Correct:

```python
student(name="Asha", age=20)
```

Incorrect:

```python
student(student_name="Asha", age=20)
```

because:

```text
student_name
```

is not a parameter of the function.

Python produces:

```text
TypeError
```

---

# 🧩 20. Duplicate Values for the Same Parameter

A parameter cannot receive two values.

Example:

```python
def student(name, age):
    print(name, age)

student("Asha", name="Neha")
```

The parameter `name` receives:

```text
"Asha"
```

positionally and:

```text
"Neha"
```

as a keyword argument.

This creates:

```text
TypeError: got multiple values for argument 'name'
```

A parameter should receive only one value.

---

# 🔢 21. Keyword Arguments with Built-in Functions

Many Python functions accept keyword arguments.

Example:

```python
print("Python", "SQL", "Git", sep=" | ")
```

Output:

```text
Python | SQL | Git
```

Here:

```python
sep=" | "
```

is a keyword argument.

Another example:

```python
print("Hello", end="!")
```

Output:

```text
Hello!
```

Here:

```python
end="!"
```

is a keyword argument.

---

# 🧠 22. Understanding `sep` and `end`

The `print()` function supports keyword arguments such as:

```python
sep
end
```

Example:

```python
print("A", "B", "C", sep="-")
```

Output:

```text
A-B-C
```

Example:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Keyword arguments make the purpose of these values clear.

---

# 🔄 23. Keyword Arguments with User-Defined Functions

Example:

```python
def calculate_bill(price, quantity, discount):
    total = price * quantity
    total -= discount

    print("Final Bill:", total)

calculate_bill(
    price=1000,
    quantity=3,
    discount=200
)
```

Output:

```text
Final Bill: 2800
```

---

# 💰 24. Real-World Example: Product Order

```python
def order_product(product, quantity, price):
    total = quantity * price

    print("Product:", product)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total:", total)

order_product(
    product="Keyboard",
    quantity=2,
    price=1500
)
```

Output:

```text
Product: Keyboard
Quantity: 2
Price: 1500
Total: 3000
```

---

# 👨‍🎓 25. Real-World Example: Student Registration

```python
def register_student(name, age, course, city):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)

register_student(
    name="Asha",
    age=20,
    course="BCA",
    city="Bengaluru"
)
```

Keyword arguments make the registration information easy to understand.

---

# 🏦 26. Real-World Example: Bank Account

```python
def create_account(name, account_type, balance):
    print("Name:", name)
    print("Account Type:", account_type)
    print("Balance:", balance)

create_account(
    name="Ananya",
    balance=25000,
    account_type="Savings"
)
```

Notice that the order of keyword arguments is different from the parameter order.

The program still works because Python uses the parameter names.

---

# 🛒 27. Real-World Example: Shopping Cart

```python
def add_to_cart(product, quantity, price):
    total = quantity * price

    print("Product:", product)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total:", total)

add_to_cart(
    price=800,
    product="Mouse",
    quantity=3
)
```

Output:

```text
Product: Mouse
Quantity: 3
Price: 800
Total: 2400
```

---

# 🚗 28. Real-World Example: Vehicle Registration

```python
def register_vehicle(number, owner, model, year):
    print("Number:", number)
    print("Owner:", owner)
    print("Model:", model)
    print("Year:", year)

register_vehicle(
    model="Swift",
    owner="Ananya",
    year=2025,
    number="KA01AB1234"
)
```

Keyword arguments allow the information to be provided in any order.

---

# 🧠 29. Keyword Arguments with Conditions

Keyword arguments can be passed to functions that contain conditions.

```python
def check_result(name, marks, passing_marks=40):
    if marks >= passing_marks:
        print(name, "Passed")
    else:
        print(name, "Failed")

check_result(
    name="Asha",
    marks=75,
    passing_marks=40
)
```

Output:

```text
Asha Passed
```

---

# 🔢 30. Keyword Arguments with Multiple Default Parameters

Example:

```python
def employee(name, department="Development", city="Bengaluru"):
    print("Name:", name)
    print("Department:", department)
    print("City:", city)

employee(
    name="Neha",
    city="Mysuru"
)
```

Output:

```text
Name: Neha
Department: Development
City: Mysuru
```

The `department` parameter uses its default value.

---

# 🎯 31. Selecting Specific Default Parameters

Keyword arguments are especially useful when a function has several default parameters.

```python
def profile(name, age=20, course="BCA", city="Bengaluru"):
    print(name)
    print(age)
    print(course)
    print(city)

profile(
    name="Asha",
    course="MCA"
)
```

Output:

```text
Asha
20
MCA
Bengaluru
```

Only the `course` default was changed.

---

# 🧩 32. Keyword Arguments and Function Readability

Compare:

```python
calculate_salary(45000, 2, 5000)
```

with:

```python
calculate_salary(
    salary=45000,
    experience=2,
    bonus=5000
)
```

The second version clearly communicates what each value means.

This becomes especially useful when functions have many parameters.

---

# 🔍 33. Keyword Arguments with Expressions

Keyword argument values can be expressions.

Example:

```python
def calculate_total(price, quantity):
    print(price * quantity)

calculate_total(
    price=500 + 100,
    quantity=3
)
```

Output:

```text
1800
```

Python evaluates the expression before passing the value.

---

# 🔢 34. Keyword Arguments with Variables

Keyword arguments can also use variables.

```python
name = "Asha"
age = 20

def student(name, age):
    print(name, age)

student(
    name=name,
    age=age
)
```

Output:

```text
Asha 20
```

---

# 🧠 35. Keyword Argument Names and Variable Names

The parameter name and variable name do not have to be the same.

Example:

```python
student_name = "Asha"
student_age = 20

def student(name, age):
    print(name, age)

student(
    name=student_name,
    age=student_age
)
```

Here:

```text
name → parameter
student_name → variable
```

and:

```text
age → parameter
student_age → variable
```

---

# ⚙️ 36. Keyword-Only Arguments

Python can force certain parameters to be supplied using keywords.

Example:

```python
def student(name, *, age, course):
    print(name)
    print(age)
    print(course)
```

The `*` means that parameters after it are **keyword-only parameters**.

Correct:

```python
student(
    "Asha",
    age=20,
    course="BCA"
)
```

Incorrect:

```python
student("Asha", 20, "BCA")
```

The second version produces a `TypeError`.

---

# 🧠 37. Understanding the `*` in Keyword-Only Arguments

Consider:

```python
def employee(name, *, salary, department):
    print(name)
    print(salary)
    print(department)
```

Here:

```text
name
```

can be positional.

But:

```text
salary
department
```

must be keyword arguments.

Correct:

```python
employee(
    "Neha",
    salary=45000,
    department="Development"
)
```

---

# 🔐 38. Why Use Keyword-Only Arguments?

Keyword-only arguments can make function calls clearer and prevent accidental argument placement.

Instead of:

```python
create_user("Asha", 20, True)
```

we can require:

```python
create_user(
    "Asha",
    age=20,
    active=True
)
```

This makes the meaning of the arguments explicit.

---

# 🧩 39. Keyword Arguments with `**kwargs`

Python provides `**kwargs` for accepting a variable number of keyword arguments.

Example:

```python
def student_info(**kwargs):
    print(kwargs)

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

Inside the function, `kwargs` is a dictionary.

---

# 🔍 40. Understanding `**kwargs`

Consider:

```python
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
```

Call:

```python
student_info(
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

The keyword arguments are collected into:

```text
kwargs
   ↓
dictionary
```

---

# 🔄 41. Multiple Keyword Arguments with `**kwargs`

Example:

```python
def profile(**details):
    for key, value in details.items():
        print(key, ":", value)

profile(
    name="Asha",
    age=20,
    city="Bengaluru",
    course="BCA"
)
```

Output:

```text
name : Asha
age : 20
city : Bengaluru
course : BCA
```

---

# ⚖️ 42. `**kwargs` vs Normal Keyword Arguments

Normal keyword arguments:

```python
def student(name, age):
    print(name, age)

student(name="Asha", age=20)
```

The function expects specific parameters.

With `**kwargs`:

```python
def student(**details):
    print(details)

student(name="Asha", age=20)
```

The function can accept any number of keyword arguments.

---

# 🧠 43. Keyword Arguments with `*args` and `**kwargs`

A function can accept:

```text
*args
**kwargs
```

Example:

```python
def display(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

display(
    "Python",
    "SQL",
    level="Advanced",
    duration=6
)
```

Output:

```text
Positional: ('Python', 'SQL')
Keyword: {'level': 'Advanced', 'duration': 6}
```

Here:

```text
*args
   ↓
Tuple

**kwargs
   ↓
Dictionary
```

---

# 📊 44. Understanding the Flow of `*args` and `**kwargs`

```text
Function Call
      │
      ├───────────────┐
      ↓               ↓
 Positional        Keyword
 Arguments         Arguments
      │               │
      ↓               ↓
   *args           **kwargs
      │               │
      ↓               ↓
   Tuple          Dictionary
```

---

# ⚠️ 45. Common Mistake: Wrong Parameter Name

Incorrect:

```python
def student(name, age):
    print(name, age)

student(
    student_name="Asha",
    age=20
)
```

`student_name` is not a valid parameter.

Correct:

```python
student(
    name="Asha",
    age=20
)
```

---

# ⚠️ 46. Common Mistake: Positional Argument After Keyword Argument

Incorrect:

```python
student(
    name="Asha",
    20
)
```

Correct:

```python
student(
    "Asha",
    age=20
)
```

Remember:

```text
Positional → First
Keyword    → After
```

---

# ⚠️ 47. Common Mistake: Giving One Parameter Two Values

Incorrect:

```python
def student(name, age):
    print(name, age)

student("Asha", name="Neha")
```

The parameter `name` receives two values.

Python raises:

```text
TypeError
```

---

# ⚠️ 48. Common Mistake: Forgetting a Required Argument

Consider:

```python
def student(name, age):
    print(name, age)
```

Incorrect:

```python
student(name="Asha")
```

The required `age` argument is missing.

Python raises:

```text
TypeError
```

Correct:

```python
student(
    name="Asha",
    age=20
)
```

---

# ⚠️ 49. Common Mistake: Confusing Parameter Names and Values

Consider:

```python
def student(name, age):
    print(name, age)
```

Correct:

```python
student(name="Asha", age=20)
```

Remember:

```text
name → parameter
"Asha" → value

age → parameter
20 → value
```

---

# 🔄 50. Keyword Arguments and Dictionary Unpacking

A dictionary can be unpacked into keyword arguments using `**`.

Example:

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

def student_info(name, age, course):
    print(name)
    print(age)
    print(course)

student_info(**student)
```

Output:

```text
Asha
20
BCA
```

The dictionary keys must match the function parameter names.

---

# 🧠 51. Understanding Dictionary Unpacking with `**`

Given:

```python
student = {
    "name": "Asha",
    "age": 20
}
```

Using:

```python
student_info(**student)
```

is conceptually similar to:

```python
student_info(
    name="Asha",
    age=20
)
```

The `**` operator unpacks dictionary key-value pairs as keyword arguments.

---

# 🌍 52. Real-World Example: User Registration

```python
def register_user(name, email, age, city):
    print("Name:", name)
    print("Email:", email)
    print("Age:", age)
    print("City:", city)

user = {
    "name": "Asha",
    "email": "asha@example.com",
    "age": 20,
    "city": "Bengaluru"
}

register_user(**user)
```

This is useful when data is already stored in a dictionary.

---

# 🌍 53. Real-World Example: Employee Information

```python
def employee_info(name, department, salary, experience):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("Experience:", experience)

employee = {
    "name": "Neha",
    "department": "Development",
    "salary": 45000,
    "experience": 2
}

employee_info(**employee)
```

The dictionary values are passed as keyword arguments.

---

# 🌍 54. Real-World Example: Product Configuration

```python
def product(name, price, quantity, category):
    print("Name:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Category:", category)

details = {
    "name": "Laptop",
    "price": 55000,
    "quantity": 2,
    "category": "Electronics"
}

product(**details)
```

Output:

```text
Name: Laptop
Price: 55000
Quantity: 2
Category: Electronics
```

---

# 🔢 55. Keyword Arguments with Loops

Keyword arguments can be generated from dictionary data inside loops.

Example:

```python
students = [
    {
        "name": "Asha",
        "age": 20
    },
    {
        "name": "Ananya",
        "age": 21
    }
]

def display_student(name, age):
    print(name, age)

for student in students:
    display_student(**student)
```

Output:

```text
Asha 20
Ananya 21
```

---

# 🧩 56. Keyword Arguments with Conditions

Example:

```python
def check_marks(name, marks, passing=40):
    if marks >= passing:
        print(name, "Passed")
    else:
        print(name, "Failed")

check_marks(
    name="Asha",
    marks=82,
    passing=50
)
```

Output:

```text
Asha Passed
```

---

# 📊 57. Positional vs Keyword Arguments Comparison

| Feature                                | Positional Arguments     | Keyword Arguments           |
| -------------------------------------- | ------------------------ | --------------------------- |
| Matching                               | Based on position        | Based on parameter name     |
| Order                                  | Important                | Can be changed              |
| Readability                            | Lower for many arguments | Higher                      |
| Syntax                                 | `func("Asha", 20)`       | `func(name="Asha", age=20)` |
| Parameter names required               | ❌                        | ✅                           |
| Can use defaults                       | ✅                        | ✅                           |
| Can mix with other type                | ✅                        | ✅                           |
| Must appear after positional arguments | —                        | Positional must come first  |

---

# 📊 58. Keyword Arguments Quick Comparison

```text
Positional Argument
        ↓
student("Asha", 20)
        ↓
Position matters
```

```text
Keyword Argument
        ↓
student(name="Asha", age=20)
        ↓
Parameter name matters
```

```text
Keyword-Only Argument
        ↓
def student(name, *, age)
        ↓
age must be passed by keyword
```

```text
**kwargs
        ↓
def student(**details)
        ↓
Multiple keyword arguments
        ↓
Dictionary
```

---

# 💻 59. Practice Programs

## 🟢 Easy

### Program 1: Basic Keyword Argument

```python
def greet(name):
    print("Hello", name)

greet(name="Asha")
```

---

### Program 2: Two Keyword Arguments

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(
    name="Asha",
    age=20
)
```

---

### Program 3: Change Keyword Argument Order

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student(
    course="BCA",
    name="Asha",
    age=20
)
```

---

### Program 4: Keyword Argument with Default Value

```python
def student(name, course="BCA"):
    print(name)
    print(course)

student(
    name="Asha"
)
```

---

# 🟡 Medium

### Program 5: Override a Default Parameter

```python
def student(name, course="BCA"):
    print(name)
    print(course)

student(
    name="Asha",
    course="MCA"
)
```

---

### Program 6: Mix Positional and Keyword Arguments

```python
def employee(name, department, salary):
    print(name)
    print(department)
    print(salary)

employee(
    "Neha",
    department="Development",
    salary=45000
)
```

---

### Program 7: Shopping Cart Using Keyword Arguments

```python
def cart_total(product, price, quantity):
    total = price * quantity

    print("Product:", product)
    print("Total:", total)

cart_total(
    quantity=3,
    product="Mouse",
    price=800
)
```

---

### Program 8: Student Result

```python
def result(name, marks, passing_marks=40):
    if marks >= passing_marks:
        print(name, "Passed")
    else:
        print(name, "Failed")

result(
    name="Asha",
    marks=85,
    passing_marks=50
)
```

---

# 🔴 Advanced

## Program 9: Keyword-Only Arguments

```python
def employee(name, *, salary, department):
    print(name)
    print(salary)
    print(department)

employee(
    "Neha",
    salary=45000,
    department="Development"
)
```

---

## Program 10: Variable Keyword Arguments

```python
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(
    name="Asha",
    age=20,
    course="BCA",
    city="Bengaluru"
)
```

---

## Program 11: Dictionary Unpacking

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

def display_student(name, age, course):
    print(name)
    print(age)
    print(course)

display_student(**student)
```

---

## Program 12: Combining `*args` and `**kwargs`

```python
def display(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

display(
    "Python",
    "SQL",
    level="Advanced",
    duration=6
)
```

Output:

```text
Positional: ('Python', 'SQL')
Keyword: {'level': 'Advanced', 'duration': 6}
```

---

# 🏆 60. Challenge

Create a function for a **student registration system**.

The function should accept:

```text
name
age
course
college
city
```

Then:

1. Call the function using keyword arguments.
2. Change the order of the keyword arguments.
3. Use a default value for `city`.
4. Override the default `city`.
5. Mix one positional argument with keyword arguments.
6. Create a dictionary containing student information.
7. Pass the dictionary to the function using `**`.
8. Display all student information.

Example data:

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA",
    "college": "ABC College",
    "city": "Bengaluru"
}
```

Try solving the challenge without copying the solution.

---

# 🧪 61. Mini Project: Employee Management System

Create a function that accepts employee information:

* Employee ID
* Name
* Department
* Salary
* Experience
* Location

Example:

```python
employee = {
    "employee_id": 101,
    "name": "Neha",
    "department": "Development",
    "salary": 45000,
    "experience": 2,
    "location": "Bengaluru"
}
```

Your program should:

* [ ] Define a function with appropriate parameters.
* [ ] Call the function using keyword arguments.
* [ ] Change the order of keyword arguments.
* [ ] Use a default value for location.
* [ ] Override the default location.
* [ ] Store employee information in a dictionary.
* [ ] Pass the dictionary using `**`.
* [ ] Display the complete employee information.

### Your Goal

Build a complete employee management program that demonstrates how keyword arguments make function calls readable and flexible.

---

# 🎤 62. Interview Questions

* [ ] What are keyword arguments in Python?
* [ ] How are keyword arguments different from positional arguments?
* [ ] How do you pass a keyword argument to a function?
* [ ] Does the order of keyword arguments matter?
* [ ] Can positional and keyword arguments be used together?
* [ ] Which must come first when mixing positional and keyword arguments?
* [ ] What happens when a positional argument follows a keyword argument?
* [ ] Can a parameter receive both a positional and keyword value?
* [ ] What happens if the same parameter receives two values?
* [ ] Can keyword arguments be used with default parameters?
* [ ] How can a default parameter be overridden?
* [ ] What are keyword-only arguments?
* [ ] What does `*` mean in a function parameter list?
* [ ] What is `**kwargs`?
* [ ] What type of object is `kwargs` inside the function?
* [ ] What is the difference between keyword arguments and `**kwargs`?
* [ ] How can a dictionary be passed as keyword arguments?
* [ ] What does `**dictionary` do in a function call?
* [ ] Why are keyword arguments useful for readability?
* [ ] Can built-in functions use keyword arguments?
* [ ] Give an example of keyword arguments with `print()`.
* [ ] What is the difference between `*args` and `**kwargs`?
* [ ] Can a function use both `*args` and `**kwargs`?
* [ ] What happens if an invalid keyword name is passed to a function?

---

# 📝 63. Assignment

Complete the following programs.

### Task 1

Create a function that accepts:

```text
name
age
```

Call it using keyword arguments.

---

### Task 2

Create a function containing:

```text
name
age
course
```

Call it using keyword arguments in a different order.

---

### Task 3

Create a function with a default parameter:

```text
course="BCA"
```

Call the function without specifying the course.

---

### Task 4

Override the default course using a keyword argument.

---

### Task 5

Create a function containing:

```text
product
price
quantity
```

Calculate the total using keyword arguments.

---

### Task 6

Create a function that mixes:

```text
one positional argument
two keyword arguments
```

---

### Task 7

Create a function with keyword-only parameters using `*`.

---

### Task 8

Create a function using `**kwargs`.

Display all received keyword arguments using a loop.

---

### Task 9

Create a dictionary containing:

```text
name
age
course
city
```

Create a function with matching parameters and pass the dictionary using:

```python
**dictionary
```

---

### Task 10

Create a function using both:

```python
*args
```

and:

```python
**kwargs
```

Display both separately.

---

### Task 11

Create a real-world employee function and use at least five keyword arguments.

---

### Task 12

Create a student result function that accepts:

```text
name
marks
passing_marks
```

Use `passing_marks=40` as a default value and override it using a keyword argument.

---

### Task 13

Create a product-order function using keyword arguments.

The function should calculate:

```text
price × quantity
```

and apply a discount.

---

### Task 14

Create a user-registration function where:

```text
name
email
age
city
```

are accepted as keyword arguments.

Use a default value for `city`.

---

### Task 15

Create a function that accepts arbitrary keyword arguments using `**kwargs`.

Display only the values that are greater than `50`.

---

# 🧠 64. Memory Tricks

Remember:

```text
Positional Argument
        ↓
Position matters
        ↓
student("Asha", 20)
```

---

Remember:

```text
Keyword Argument
        ↓
Parameter name matters
        ↓
student(name="Asha", age=20)
```

---

Remember:

```text
Keyword Arguments
        ↓
Order can change
        ↓
student(age=20, name="Asha")
```

---

Remember the mixing rule:

```text
Positional
    ↓
First

Keyword
    ↓
After
```

---

Remember:

```text
* 
 ↓
Keyword-only parameters
```

---

Remember:

```text
**kwargs
    ↓
Variable keyword arguments
    ↓
Dictionary
```

---

Remember:

```text
**dictionary
      ↓
Dictionary unpacking
      ↓
Keyword arguments
```

---

# 📌 65. Important Rules to Remember

```text
1. Keyword arguments are passed using parameter_name=value.

2. Keyword arguments are matched using parameter names.

3. The order of keyword arguments does not matter.

4. Positional arguments must come before keyword arguments.

5. A parameter cannot receive two values.

6. Keyword arguments can be used with default parameters.

7. Keyword arguments can override default parameter values.

8. Keyword arguments improve function-call readability.

9. Parameter names must be valid for the function.

10. Invalid keyword names can cause a TypeError.

11. Parameters after * are keyword-only parameters.

12. **kwargs collects variable keyword arguments.

13. **kwargs stores keyword arguments as a dictionary.

14. A dictionary can be unpacked into keyword arguments using **.

15. Dictionary keys used for unpacking should match the function parameters.

16. *args collects positional arguments into a tuple.

17. **kwargs collects keyword arguments into a dictionary.

18. A function can use both *args and **kwargs.

19. Built-in functions such as print() can accept keyword arguments.

20. Keyword arguments are especially useful when a function has many parameters.
```

---

# 📊 66. Keyword Arguments Structure

```text
                         FUNCTION
                            │
                            ↓
                       ARGUMENTS
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
         POSITIONAL                    KEYWORD
         ARGUMENTS                    ARGUMENTS
              │                           │
              ↓                           ↓
       Position matters           Parameter name
                                      matters
              │                           │
              ↓                           ↓
     func("Asha", 20)        func(name="Asha", age=20)
                                          │
                                          ↓
                                   Order can change
                                          │
                                          ↓
                              func(age=20, name="Asha")
```

---

# 📊 67. Advanced Keyword Arguments Structure

```text
                       FUNCTION ARGUMENTS
                              │
             ┌────────────────┼────────────────┐
             ↓                ↓                ↓
        Positional         Keyword         Keyword-only
          values            values            values
             │                │                │
             ↓                ↓                ↓
          *args             normal             *
                              │                 │
                              ↓                 ↓
                          name=value       name=value
                                                │
                                                ↓
                                      Must use keyword
```

---

# 📊 68. `*args` and `**kwargs` Structure

```text
                         FUNCTION
                            │
                            ↓
                    *args and **kwargs
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
           *args                        **kwargs
              │                           │
              ↓                           ↓
        Positional                  Keyword arguments
         arguments                      │
              │                           │
              ↓                           ↓
           Tuple                     Dictionary
```

Example:

```python
def display(*args, **kwargs):
    print(args)
    print(kwargs)

display(
    "Python",
    "SQL",
    level="Advanced",
    duration=6
)
```

---

# 📚 69. Complete Keyword Arguments Cheat Sheet

### Basic Keyword Argument

```python
student(name="Asha", age=20)
```

### Change Order

```python
student(age=20, name="Asha")
```

### Mix Positional and Keyword Arguments

```python
student("Asha", age=20)
```

### Default Parameter

```python
def student(name, course="BCA"):
    ...
```

### Override Default

```python
student(name="Asha", course="MCA")
```

### Keyword-Only Parameter

```python
def student(name, *, age):
    ...
```

### Variable Keyword Arguments

```python
def student(**kwargs):
    ...
```

### Dictionary Unpacking

```python
student(**details)
```

### Positional and Keyword Collections

```python
def function(*args, **kwargs):
    ...
```

### Built-in Function Keyword Argument

```python
print("A", "B", sep="-")
```

---

# 🏆 70. Keyword Arguments Mastery

```text
                         FUNCTION CALL
                              │
                              ↓
                     KEYWORD ARGUMENTS
                              │
          ┌───────────────────┼───────────────────┐
          ↓                   ↓                   ↓
       name=value        order can change      readable
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ↓
                    DEFAULT PARAMETERS
                              │
                              ↓
                       Can be overridden
                              │
                              ↓
                         KEYWORD-ONLY
                              │
                              ↓
                             *
                              │
                              ↓
                           **kwargs
                              │
                              ↓
                         Dictionary
                              │
                              ↓
                       **dictionary
                              │
                              ↓
                    Dictionary Unpacking
```

---

# 📖 71. Summary

In this lesson, you learned:

* What keyword arguments are.
* How keyword arguments are written.
* How keyword arguments differ from positional arguments.
* Why keyword argument order does not matter.
* How to mix positional and keyword arguments.
* Why positional arguments must come before keyword arguments.
* How keyword arguments improve code readability.
* How keyword arguments work with default parameters.
* How to override default parameter values.
* How to use keyword arguments with built-in functions.
* How to use keyword arguments with user-defined functions.
* How keyword arguments work with conditions.
* What keyword-only arguments are.
* How `*` creates keyword-only parameters.
* What `**kwargs` means.
* How `**kwargs` collects keyword arguments.
* The difference between `*args` and `**kwargs`.
* How to combine `*args` and `**kwargs`.
* How to unpack dictionaries into keyword arguments.
* How keyword arguments are used in real-world applications.
* Common mistakes involving keyword arguments.
* How to build practical programs using keyword arguments.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what keyword arguments are.
* [ ] I understand the difference between positional and keyword arguments.
* [ ] I can call a function using keyword arguments.
* [ ] I can change the order of keyword arguments.
* [ ] I understand why positional arguments must come first.
* [ ] I can mix positional and keyword arguments correctly.
* [ ] I understand keyword arguments with default parameters.
* [ ] I can override default values using keyword arguments.
* [ ] I understand invalid keyword names.
* [ ] I understand duplicate argument errors.
* [ ] I understand keyword-only arguments.
* [ ] I can use `*` to create keyword-only parameters.
* [ ] I understand `**kwargs`.
* [ ] I can use `**kwargs` in functions.
* [ ] I understand that `**kwargs` creates a dictionary.
* [ ] I understand `*args` and `**kwargs`.
* [ ] I can use both `*args` and `**kwargs`.
* [ ] I can unpack a dictionary using `**`.
* [ ] I can use keyword arguments with built-in functions.
* [ ] I can use keyword arguments in real-world programs.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use keyword arguments without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Default Arguments**

In the next topic, you will learn:

* What default arguments are.
* Why default arguments are useful.
* How to define default parameters.
* How Python uses default values.
* How to override default values.
* Default arguments with positional arguments.
* Default arguments with keyword arguments.
* Multiple default parameters.
* Rules for placing default parameters.
* Common mistakes with default arguments.
* Default arguments with mutable objects.
* Practical real-world examples.
* Advanced default argument techniques.
* Practice programs and challenges.
* Real-world applications of default parameters.

---

## ⭐ Quote of the Day

> **"Keyword arguments make function calls clearer, flexible, and easier to understand."** 🐍📚
