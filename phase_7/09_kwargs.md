# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 9: `**kwargs`

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what `**kwargs` means in Python.
* [ ] Understand why `**kwargs` is used in functions.
* [ ] Understand the difference between `*args` and `**kwargs`.
* [ ] Learn how keyword arguments are collected using `**kwargs`.
* [ ] Understand that `kwargs` is stored as a dictionary.
* [ ] Access values from `kwargs`.
* [ ] Use `kwargs.keys()`.
* [ ] Use `kwargs.values()`.
* [ ] Use `kwargs.items()`.
* [ ] Loop through `kwargs`.
* [ ] Check whether a key exists in `kwargs`.
* [ ] Use `**kwargs` with conditions.
* [ ] Combine `*args` and `**kwargs`.
* [ ] Understand argument unpacking using `**`.
* [ ] Use `**kwargs` with dictionaries.
* [ ] Understand the difference between `**kwargs` and a normal dictionary.
* [ ] Use `**kwargs` in real-world applications.
* [ ] Avoid common mistakes when using `**kwargs`.
* [ ] Build flexible functions using `**kwargs`.

---

# 📖 1. What is `**kwargs`?

`**kwargs` is a special syntax used in Python functions to accept a variable number of **keyword arguments**.

The word `kwargs` means:

```text
keyword arguments
```

The name `kwargs` is a convention.

You can technically use another name, but `kwargs` is the standard and recommended name.

Example:

```python
def student_info(**kwargs):
    print(kwargs)

student_info(name="Asha", age=20, course="BCA")
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

Here, all keyword arguments are collected into a dictionary.

---

# 🧠 2. Understanding Keyword Arguments

Before learning `**kwargs`, you should understand keyword arguments.

Consider:

```python
def student(name, age):
    print(name)
    print(age)

student(name="Asha", age=20)
```

Here:

```text
name="Asha"
age=20
```

are keyword arguments.

The argument name is explicitly provided.

---

# 🔍 3. What Problem Does `**kwargs` Solve?

Suppose a function accepts a fixed number of arguments:

```python
def student(name, age, course):
    print(name, age, course)
```

This function expects exactly these parameters.

But sometimes you may want to pass additional information:

```text
name
age
course
city
phone
email
college
semester
```

You could keep adding parameters:

```python
def student(name, age, course, city, phone, email, college, semester):
    ...
```

This becomes difficult to manage.

Instead, you can use:

```python
def student(**kwargs):
    print(kwargs)
```

Now the function can accept any number of keyword arguments.

---

# 📚 4. Basic Syntax of `**kwargs`

The general syntax is:

```python
def function_name(**kwargs):
    # function body
```

Example:

```python
def display(**kwargs):
    print(kwargs)

display(name="Asha", age=20)
```

Output:

```text
{'name': 'Asha', 'age': 20}
```

---

# 🧠 5. Why Are Two Asterisks Used?

The two asterisks:

```python
**
```

tell Python to collect keyword arguments into a dictionary.

Compare:

```text
*args
   ↓
Positional arguments
   ↓
Tuple
```

and:

```text
**kwargs
   ↓
Keyword arguments
   ↓
Dictionary
```

Remember:

```text
*args   → tuple
**kwargs → dictionary
```

---

# 🔢 6. `**kwargs` Stores Data as a Dictionary

Consider:

```python
def student_info(**kwargs):
    print(kwargs)
    print(type(kwargs))

student_info(name="Asha", age=20, course="BCA")
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
<class 'dict'>
```

Therefore:

```text
kwargs
   ↓
Dictionary
```

---

# 🔑 7. Accessing Values from `kwargs`

Since `kwargs` is a dictionary, you can access values using keys.

Example:

```python
def student_info(**kwargs):
    print(kwargs["name"])
    print(kwargs["course"])

student_info(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
Asha
BCA
```

---

# 🛡️ 8. Using `get()` with `kwargs`

Because `kwargs` is a dictionary, dictionary methods can be used.

Example:

```python
def student_info(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("city"))

student_info(
    name="Asha",
    age=20
)
```

Output:

```text
Asha
None
```

`get()` is useful when a key may not exist.

---

# ⚖️ 9. `kwargs["key"]` vs `kwargs.get("key")`

Consider:

```python
def student_info(**kwargs):
    print(kwargs["city"])
```

If `"city"` does not exist, Python raises:

```text
KeyError
```

Using:

```python
def student_info(**kwargs):
    print(kwargs.get("city"))
```

returns:

```text
None
```

Therefore:

```text
kwargs["city"]
       ↓
KeyError if missing

kwargs.get("city")
       ↓
None if missing
```

---

# 🔄 10. Passing Multiple Keyword Arguments

`**kwargs` can accept many keyword arguments.

Example:

```python
def profile(**kwargs):
    print(kwargs)

profile(
    name="Asha",
    age=20,
    course="BCA",
    city="Bengaluru",
    semester=4
)
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA', 'city': 'Bengaluru', 'semester': 4}
```

There is no fixed number of keyword arguments.

---

# 🧩 11. Passing Only One Keyword Argument

`**kwargs` does not require multiple arguments.

Example:

```python
def display(**kwargs):
    print(kwargs)

display(name="Asha")
```

Output:

```text
{'name': 'Asha'}
```

---

# 🧩 12. Passing No Keyword Arguments

You can also call the function without any keyword arguments.

Example:

```python
def display(**kwargs):
    print(kwargs)

display()
```

Output:

```text
{}
```

The function receives an empty dictionary.

---

# 🔁 13. Looping Through `kwargs`

Since `kwargs` is a dictionary, you can loop through it.

Example:

```python
def display(**kwargs):
    for key in kwargs:
        print(key)

display(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
name
age
course
```

---

# 🔗 14. Using `items()` with `kwargs`

`items()` is useful when you need both keys and values.

Example:

```python
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(
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

---

# 🔑 15. Using `keys()` with `kwargs`

You can retrieve all keyword argument names using `keys()`.

Example:

```python
def display(**kwargs):
    print(kwargs.keys())

display(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
dict_keys(['name', 'age', 'course'])
```

---

# 💰 16. Using `values()` with `kwargs`

You can retrieve all values using `values()`.

Example:

```python
def display(**kwargs):
    print(kwargs.values())

display(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
dict_values(['Asha', 20, 'BCA'])
```

---

# 🧠 17. Checking Whether a Key Exists

You can use the `in` operator with `kwargs`.

Example:

```python
def student_info(**kwargs):
    if "city" in kwargs:
        print("City is available")
    else:
        print("City is not available")

student_info(
    name="Asha",
    age=20
)
```

Output:

```text
City is not available
```

---

# 🔄 18. Modifying `kwargs`

Because `kwargs` is a dictionary, you can modify it inside the function.

Example:

```python
def student_info(**kwargs):
    kwargs["status"] = "Active"
    print(kwargs)

student_info(
    name="Asha",
    age=20
)
```

Output:

```text
{'name': 'Asha', 'age': 20, 'status': 'Active'}
```

The local `kwargs` dictionary has been modified.

---

# ➕ 19. Adding Data Using `kwargs`

You can add new key-value pairs.

Example:

```python
def employee(**kwargs):
    kwargs["status"] = "Employed"
    print(kwargs)

employee(
    name="Neha",
    department="Development"
)
```

Output:

```text
{'name': 'Neha', 'department': 'Development', 'status': 'Employed'}
```

---

# ✏️ 20. Updating Data Inside `kwargs`

You can update an existing value.

Example:

```python
def student(**kwargs):
    kwargs["age"] = 21
    print(kwargs)

student(
    name="Asha",
    age=20
)
```

Output:

```text
{'name': 'Asha', 'age': 21}
```

---

# 🗑️ 21. Removing Data from `kwargs`

Dictionary methods such as `pop()` can also be used.

Example:

```python
def student(**kwargs):
    removed = kwargs.pop("age")
    print("Removed:", removed)
    print(kwargs)

student(
    name="Asha",
    age=20,
    course="BCA"
)
```

Output:

```text
Removed: 20
{'name': 'Asha', 'course': 'BCA'}
```

---

# 🧹 22. Clearing `kwargs`

You can use `clear()`.

Example:

```python
def display(**kwargs):
    print(kwargs)

    kwargs.clear()

    print(kwargs)

display(
    name="Asha",
    age=20
)
```

Output:

```text
{'name': 'Asha', 'age': 20}
{}
```

---

# 📋 23. Copying `kwargs`

You can create a shallow copy.

Example:

```python
def student(**kwargs):
    new_data = kwargs.copy()

    new_data["status"] = "Active"

    print(kwargs)
    print(new_data)

student(
    name="Asha",
    age=20
)
```

Output:

```text
{'name': 'Asha', 'age': 20}
{'name': 'Asha', 'age': 20, 'status': 'Active'}
```

---

# ⚙️ 24. Using `setdefault()` with `kwargs`

You can use `setdefault()` to insert a value if a key is missing.

Example:

```python
def student(**kwargs):
    kwargs.setdefault("city", "Bengaluru")
    print(kwargs)

student(
    name="Asha",
    age=20
)
```

Output:

```text
{'name': 'Asha', 'age': 20, 'city': 'Bengaluru'}
```

---

# ⚖️ 25. `**kwargs` vs Normal Parameters

Normal parameters:

```python
def student(name, age, course):
    print(name, age, course)
```

The function expects these specific parameters.

With `**kwargs`:

```python
def student(**kwargs):
    print(kwargs)
```

The function can receive flexible keyword arguments.

Comparison:

| Feature             | Normal Parameters    | `**kwargs`        |
| ------------------- | -------------------- | ----------------- |
| Number of arguments | Fixed                | Variable          |
| Argument type       | Named parameters     | Keyword arguments |
| Storage             | Individual variables | Dictionary        |
| Flexibility         | Lower                | Higher            |
| Missing arguments   | Usually error        | Allowed           |

---

# 🔀 26. `*args` vs `**kwargs`

`*args` collects positional arguments.

```python
def numbers(*args):
    print(args)

numbers(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`**kwargs` collects keyword arguments.

```python
def student(**kwargs):
    print(kwargs)

student(name="Asha", age=20)
```

Output:

```text
{'name': 'Asha', 'age': 20}
```

Remember:

```text
*args
  ↓
Positional arguments
  ↓
Tuple

**kwargs
  ↓
Keyword arguments
  ↓
Dictionary
```

---

# 🧠 27. Using `*args` and `**kwargs` Together

A function can accept both.

Example:

```python
def display(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

display(
    10,
    20,
    30,
    name="Asha",
    age=20
)
```

Output:

```text
Args: (10, 20, 30)
Kwargs: {'name': 'Asha', 'age': 20}
```

---

# 🔢 28. Understanding the Difference in Storage

Consider:

```python
def example(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

example(
    10,
    20,
    name="Asha",
    age=20
)
```

Output:

```text
<class 'tuple'>
<class 'dict'>
```

Therefore:

```text
args   → tuple
kwargs → dictionary
```

---

# 🔗 29. Using `**kwargs` with Conditions

You can use `if` statements with `kwargs`.

Example:

```python
def student(**kwargs):
    if kwargs.get("age", 0) >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

student(age=20)
```

Output:

```text
Eligible
```

---

# 🧩 30. Filtering Data Using `kwargs`

Example:

```python
def marks(**kwargs):
    for subject, mark in kwargs.items():
        if mark >= 80:
            print(subject, ":", mark)

marks(
    Python=90,
    SQL=75,
    Git=85,
    HTML=68
)
```

Output:

```text
Python : 90
Git : 85
```

This is similar to processing a dictionary.

---

# 🔍 31. Finding the Highest Value in `kwargs`

Example:

```python
def highest_mark(**kwargs):
    highest = max(kwargs.values())
    print("Highest:", highest)

highest_mark(
    Python=90,
    SQL=85,
    Git=80
)
```

Output:

```text
Highest: 90
```

---

# 🧮 32. Calculating the Total of `kwargs` Values

Example:

```python
def total_marks(**kwargs):
    total = 0

    for mark in kwargs.values():
        total += mark

    print("Total:", total)

total_marks(
    Python=90,
    SQL=85,
    Git=80
)
```

Output:

```text
Total: 255
```

---

# 📊 33. Calculating Average Using `kwargs`

Example:

```python
def average_marks(**kwargs):
    total = sum(kwargs.values())
    average = total / len(kwargs)

    print("Average:", average)

average_marks(
    Python=90,
    SQL=85,
    Git=80
)
```

Output:

```text
Average: 85.0
```

---

# 🏆 34. Finding Subjects Above a Certain Mark

Example:

```python
def filter_marks(**kwargs):
    for subject, mark in kwargs.items():
        if mark >= 85:
            print(subject)

filter_marks(
    Python=90,
    SQL=85,
    Git=80,
    HTML=88
)
```

Output:

```text
Python
SQL
HTML
```

---

# 📦 35. Passing a Dictionary Using `**`

`**` can also be used to unpack a dictionary when calling a function.

Example:

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

def display(**kwargs):
    print(kwargs)

display(**student)
```

Output:

```text
{'name': 'Asha', 'age': 20, 'course': 'BCA'}
```

Here:

```python
**student
```

unpacks the dictionary into keyword arguments.

---

# 🧠 36. Understanding Dictionary Unpacking

Consider:

```python
student = {
    "name": "Asha",
    "age": 20
}
```

When you write:

```python
display(**student)
```

Python treats it approximately like:

```python
display(
    name="Asha",
    age=20
)
```

Therefore:

```text
Dictionary
    ↓
**
    ↓
Keyword arguments
```

---

# ⚖️ 37. `kwargs` vs `**dictionary`

These are related but not identical.

Inside a function:

```python
def display(**kwargs):
    print(kwargs)
```

`kwargs` is the dictionary containing the received keyword arguments.

When calling a function:

```python
display(**student)
```

`**student` means:

```text
Unpack dictionary
       ↓
Pass its key-value pairs
       ↓
As keyword arguments
```

---

# 🔄 38. Passing Dictionary Data to a Function

Example:

```python
employee = {
    "name": "Neha",
    "department": "Development",
    "salary": 45000
}

def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_info(**employee)
```

Output:

```text
name : Neha
department : Development
salary : 45000
```

---

# 🧩 39. Combining Normal Parameters with `**kwargs`

You can have regular parameters along with `**kwargs`.

Example:

```python
def student(name, **kwargs):
    print("Name:", name)
    print("Other Details:", kwargs)

student(
    "Asha",
    age=20,
    course="BCA",
    city="Bengaluru"
)
```

Output:

```text
Name: Asha
Other Details: {'age': 20, 'course': 'BCA', 'city': 'Bengaluru'}
```

---

# 🔢 40. Combining Positional, `*args`, and `**kwargs`

A function can accept all three.

Example:

```python
def student(name, *args, **kwargs):
    print("Name:", name)
    print("Args:", args)
    print("Kwargs:", kwargs)

student(
    "Asha",
    20,
    "BCA",
    city="Bengaluru",
    semester=4
)
```

Output:

```text
Name: Asha
Args: (20, 'BCA')
Kwargs: {'city': 'Bengaluru', 'semester': 4}
```

---

# 🧠 41. Parameter Order

When using different types of parameters, their order matters.

A common structure is:

```python
def function(positional, *args, **kwargs):
    ...
```

Example:

```python
def example(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
```

The general flow is:

```text
Normal parameters
       ↓
*args
       ↓
**kwargs
```

---

# 🔍 42. Using `kwargs.items()` for Data Processing

Example:

```python
def product_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

product_info(
    name="Laptop",
    price=55000,
    stock=5
)
```

Output:

```text
name = Laptop
price = 55000
stock = 5
```

This approach is useful when processing flexible data.

---

# 🌍 43. Real-World Example: Student Profile

```python
def student_profile(**kwargs):
    print("Student Profile")

    for key, value in kwargs.items():
        print(key, ":", value)

student_profile(
    name="Asha",
    age=20,
    course="BCA",
    semester=4,
    city="Bengaluru"
)
```

Output:

```text
Student Profile
name : Asha
age : 20
course : BCA
semester : 4
city : Bengaluru
```

---

# 🌍 44. Real-World Example: Employee Record

```python
def employee_record(**kwargs):
    print("Employee Record")

    for key, value in kwargs.items():
        print(key, ":", value)

employee_record(
    employee_id=101,
    name="Neha",
    department="Development",
    salary=45000,
    experience=2
)
```

Output:

```text
Employee Record
employee_id : 101
name : Neha
department : Development
salary : 45000
experience : 2
```

---

# 🌍 45. Real-World Example: Product Information

```python
def product(**kwargs):
    print("Product Details")

    for key, value in kwargs.items():
        print(key, ":", value)

product(
    name="Laptop",
    brand="Dell",
    price=55000,
    stock=10
)
```

Output:

```text
Product Details
name : Laptop
brand : Dell
price : 55000
stock : 10
```

---

# 🌍 46. Real-World Example: User Profile

```python
def user_profile(**kwargs):
    username = kwargs.get("username", "Guest")
    email = kwargs.get("email", "Not Provided")

    print("Username:", username)
    print("Email:", email)

user_profile(
    username="asha20",
    email="asha@example.com"
)
```

Output:

```text
Username: asha20
Email: asha@example.com
```

---

# 🌍 47. Real-World Example: Configuration Settings

`**kwargs` can be useful for flexible configuration.

```python
def configure_application(**kwargs):
    for setting, value in kwargs.items():
        print(setting, "=", value)

configure_application(
    theme="dark",
    language="English",
    notifications=True,
    font_size=14
)
```

Output:

```text
theme = dark
language = English
notifications = True
font_size = 14
```

---

# 🌍 48. Real-World Example: Shopping Product

```python
def add_product(**kwargs):
    print("Product Added")

    for key, value in kwargs.items():
        print(key, ":", value)

add_product(
    name="Wireless Mouse",
    price=800,
    quantity=2,
    category="Electronics"
)
```

Output:

```text
Product Added
name : Wireless Mouse
price : 800
quantity : 2
category : Electronics
```

---

# ⚠️ 49. Common Mistake: Forgetting the Double Asterisk

Wrong:

```python
def student(kwargs):
    print(kwargs)
```

Calling:

```python
student(name="Asha", age=20)
```

causes an error because `kwargs` is just a normal parameter.

Correct:

```python
def student(**kwargs):
    print(kwargs)
```

---

# ⚠️ 50. Common Mistake: Treating `kwargs` as a Tuple

Remember:

```text
*args
   ↓
Tuple

**kwargs
   ↓
Dictionary
```

Therefore:

```python
def example(**kwargs):
    print(kwargs["name"])
```

is valid.

But treating it like a tuple is incorrect:

```python
kwargs[0]
```

because dictionary indexing uses keys, not numerical positions.

---

# ⚠️ 51. Common Mistake: Passing Positional Arguments to `**kwargs`

Consider:

```python
def student(**kwargs):
    print(kwargs)
```

This is correct:

```python
student(name="Asha", age=20)
```

But this is incorrect:

```python
student("Asha", 20)
```

because `**kwargs` only collects keyword arguments.

---

# ⚠️ 52. Common Mistake: Duplicate Keyword Arguments

Consider:

```python
def student(**kwargs):
    print(kwargs)

student(name="Asha", name="Neha")
```

This causes a syntax error because the same keyword argument cannot be provided twice.

---

# ⚠️ 53. Common Mistake: Using an Invalid Keyword Name

Keyword argument names must be valid Python identifiers.

For example:

```python
def display(**kwargs):
    print(kwargs)
```

This is valid:

```python
display(name="Asha")
```

But arbitrary keys containing characters that cannot be written as normal keyword arguments cannot be passed directly using keyword syntax.

If such data is already in a dictionary, dictionary unpacking has its own restrictions for keyword argument names.

---

# ⚖️ 54. `**kwargs` and Dictionary Methods

Because `kwargs` is a dictionary, many dictionary methods work with it.

| Dictionary Method | Can Be Used with `kwargs`? |
| ----------------- | -------------------------- |
| `get()`           | ✅                          |
| `keys()`          | ✅                          |
| `values()`        | ✅                          |
| `items()`         | ✅                          |
| `update()`        | ✅                          |
| `pop()`           | ✅                          |
| `popitem()`       | ✅                          |
| `clear()`         | ✅                          |
| `copy()`          | ✅                          |
| `setdefault()`    | ✅                          |

Example:

```python
def student(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.items())

student(
    name="Asha",
    age=20
)
```

---

# 📊 55. `*args` vs `**kwargs` Comparison

| Feature    | `*args`                  | `**kwargs`          |
| ---------- | ------------------------ | ------------------- |
| Accepts    | Positional arguments     | Keyword arguments   |
| Stored as  | Tuple                    | Dictionary          |
| Uses       | `*`                      | `**`                |
| Example    | `10, 20, 30`             | `name="Asha"`       |
| Access     | Index                    | Key                 |
| Useful for | Variable positional data | Variable named data |

Remember:

```text
*args
→ variable positional arguments
→ tuple

**kwargs
→ variable keyword arguments
→ dictionary
```

---

# 📊 56. Function Parameters Comparison

| Parameter Type    | Purpose                  | Example    |
| ----------------- | ------------------------ | ---------- |
| Normal parameter  | Fixed data               | `name`     |
| Default parameter | Optional default data    | `age=20`   |
| `*args`           | Variable positional data | `*args`    |
| `**kwargs`        | Variable keyword data    | `**kwargs` |

Example:

```python
def example(name, age=20, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
```

---

# 🧠 57. Important Concept: `kwargs` Is a Dictionary

This is one of the most important points in this lesson.

When Python receives:

```python
student(
    name="Asha",
    age=20,
    course="BCA"
)
```

and the function is:

```python
def student(**kwargs):
    ...
```

Python collects the arguments into:

```python
{
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}
```

Therefore:

```text
Keyword arguments
       ↓
Python collects them
       ↓
Dictionary
       ↓
kwargs
```

---

# 🔄 58. Dictionary → `**kwargs` → Dictionary

There are two related operations.

### Dictionary to keyword arguments

```python
student = {
    "name": "Asha",
    "age": 20
}

display(**student)
```

The `**` unpacks the dictionary.

### Keyword arguments to dictionary

```python
def display(**kwargs):
    print(kwargs)
```

Python collects keyword arguments into a dictionary.

Therefore:

```text
Dictionary
   ↓
** unpacking
   ↓
Keyword arguments
   ↓
**kwargs
   ↓
Dictionary
```

---

# 💻 59. Practice Programs

## 🟢 Easy

### Program 1: Display `kwargs`

```python
def display(**kwargs):
    print(kwargs)

display(
    name="Asha",
    age=20
)
```

---

### Program 2: Display the Type of `kwargs`

```python
def display(**kwargs):
    print(type(kwargs))

display(
    name="Asha",
    age=20
)
```

---

### Program 3: Display a Specific Value

```python
def student(**kwargs):
    print(kwargs["name"])

student(
    name="Asha",
    age=20
)
```

---

### Program 4: Safely Access a Value

```python
def student(**kwargs):
    print(kwargs.get("city", "Not Available"))

student(
    name="Asha",
    age=20
)
```

---

# 🟡 Medium

### Program 5: Display All Keys

```python
def student(**kwargs):
    for key in kwargs.keys():
        print(key)

student(
    name="Asha",
    age=20,
    course="BCA"
)
```

---

### Program 6: Display All Values

```python
def student(**kwargs):
    for value in kwargs.values():
        print(value)

student(
    name="Asha",
    age=20,
    course="BCA"
)
```

---

### Program 7: Display Key-Value Pairs

```python
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(
    name="Asha",
    age=20,
    course="BCA"
)
```

---

### Program 8: Check Whether a Key Exists

```python
def student(**kwargs):
    if "city" in kwargs:
        print("City exists")
    else:
        print("City does not exist")

student(
    name="Asha",
    age=20
)
```

---

# 🔴 Advanced

## Program 9: Filter Marks

```python
def filter_marks(**kwargs):
    for subject, mark in kwargs.items():
        if mark >= 80:
            print(subject, ":", mark)

filter_marks(
    Python=90,
    SQL=75,
    Git=85,
    HTML=68
)
```

Output:

```text
Python : 90
Git : 85
```

---

## Program 10: Calculate Total Marks

```python
def total_marks(**kwargs):
    total = 0

    for mark in kwargs.values():
        total += mark

    print("Total:", total)

total_marks(
    Python=90,
    SQL=85,
    Git=80
)
```

---

## Program 11: Calculate Average Marks

```python
def average_marks(**kwargs):
    total = sum(kwargs.values())
    average = total / len(kwargs)

    print("Average:", average)

average_marks(
    Python=90,
    SQL=85,
    Git=80
)
```

---

## Program 12: Dictionary Unpacking

```python
student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}

def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(**student)
```

---

# 🏆 60. Challenge

Create a function using `**kwargs` to manage student information.

The function should accept information such as:

```text
name
age
course
semester
city
Python
SQL
Git
```

Then:

1. Display all keys using `keys()`.
2. Display all values using `values()`.
3. Display key-value pairs using `items()`.
4. Display the student name using `get()`.
5. Check whether `"city"` exists.
6. Add `"status": "Active"` using `setdefault()`.
7. Calculate the total marks.
8. Display subjects with marks greater than or equal to `80`.
9. Display the final `kwargs` dictionary.

Example function call:

```python
student_info(
    name="Asha",
    age=20,
    course="BCA",
    semester=4,
    city="Bengaluru",
    Python=90,
    SQL=85,
    Git=80
)
```

Try solving the challenge without copying the solution.

---

# 🧪 61. Mini Project: Flexible Employee Management System

Create a function that accepts employee information using `**kwargs`.

The employee information can contain:

* Employee ID
* Name
* Department
* Salary
* Experience
* Location
* Status

Example:

```python
employee = {
    "employee_id": 101,
    "name": "Neha",
    "department": "Development",
    "salary": 45000,
    "experience": 2
}
```

Create a function:

```python
def employee_management(**kwargs):
    ...
```

Perform the following operations:

* Display the employee name using `get()`.
* Display all keys.
* Display all values.
* Display all key-value pairs.
* Add `"location"` using `setdefault()`.
* Add `"status"` using `update()`.
* Check whether `"salary"` exists.
* Display employees with salary greater than a specified amount.
* Display the final employee information.

### Your Goal

Build a flexible employee management program using `**kwargs` and dictionary methods.

---

# 🎤 62. Interview Questions

* [ ] What is `**kwargs` in Python?
* [ ] What does `kwargs` stand for?
* [ ] Why are two asterisks used with `kwargs`?
* [ ] What type of object is `kwargs`?
* [ ] What is the difference between `*args` and `**kwargs`?
* [ ] Can `**kwargs` accept positional arguments?
* [ ] Can `**kwargs` accept keyword arguments?
* [ ] Can a function have both `*args` and `**kwargs`?
* [ ] Can a function have normal parameters and `**kwargs`?
* [ ] What happens when no keyword arguments are passed?
* [ ] How do you access a value from `kwargs`?
* [ ] What is the difference between `kwargs["name"]` and `kwargs.get("name")`?
* [ ] How do you get all keys from `kwargs`?
* [ ] How do you get all values from `kwargs`?
* [ ] How do you get key-value pairs from `kwargs`?
* [ ] How do you loop through `kwargs`?
* [ ] Can you modify `kwargs` inside a function?
* [ ] Can dictionary methods be used with `kwargs`?
* [ ] What does `**dictionary` do when calling a function?
* [ ] What is dictionary unpacking?
* [ ] How is `**kwargs` useful in real-world applications?
* [ ] What is the difference between `kwargs` and a normal dictionary?
* [ ] Can `**kwargs` receive zero keyword arguments?
* [ ] Can `**kwargs` receive one keyword argument?
* [ ] Can `**kwargs` receive unlimited keyword arguments?

---

# 📝 63. Assignment

Complete the following programs.

### Task 1

Create a function using `**kwargs`.

Pass:

```text
name
age
course
```

Display the dictionary.

---

### Task 2

Create a function using `**kwargs`.

Use `keys()` to display all keys.

---

### Task 3

Create a function using `**kwargs`.

Use `values()` to display all values.

---

### Task 4

Create a function using `**kwargs`.

Use `items()` to display every key and value.

---

### Task 5

Create a function that uses `get()` to display:

```text
name
city
```

If the city does not exist, display:

```text
Not Provided
```

---

### Task 6

Create a function using `**kwargs`.

Check whether `"email"` exists using `in`.

---

### Task 7

Create a function that uses `setdefault()` to add:

```text
status = "Active"
```

---

### Task 8

Create a function that accepts student marks using `**kwargs`.

Calculate the total marks using `values()`.

---

### Task 9

Create a function that accepts subject marks using `**kwargs`.

Display only subjects whose marks are greater than `80`.

---

### Task 10

Create a dictionary containing:

```text
name
age
course
city
```

Pass the dictionary to a function using:

```python
**dictionary
```

---

### Task 11

Create a function that accepts:

```python
*args
**kwargs
```

Display both separately.

---

### Task 12

Create a real-world function using `**kwargs`.

Use at least seven different dictionary operations or methods inside the function.

---

# 🧠 64. Memory Tricks

Remember:

```text
*args
   ↓
Arguments
   ↓
Tuple
```

Remember:

```text
**kwargs
   ↓
Keyword Arguments
   ↓
Dictionary
```

---

Remember:

```text
kwargs["name"]
      ↓
Access using key
```

---

Remember:

```text
kwargs.get("name")
      ↓
Safe access
```

---

Remember:

```text
kwargs.keys()
      ↓
All keys
```

---

Remember:

```text
kwargs.values()
      ↓
All values
```

---

Remember:

```text
kwargs.items()
      ↓
Keys + Values
```

---

Remember:

```text
function(**dictionary)
       ↓
Unpack dictionary
       ↓
Keyword arguments
```

---

# 📌 65. Important Rules to Remember

```text
1. **kwargs is used to accept a variable number of keyword arguments.

2. kwargs is a conventional name, but another valid parameter name can technically be used.

3. kwargs stores keyword arguments in a dictionary.

4. *args stores positional arguments in a tuple.

5. **kwargs stores keyword arguments in a dictionary.

6. **kwargs can accept zero or more keyword arguments.

7. kwargs can be accessed like a normal dictionary.

8. Dictionary methods such as get(), keys(), values(), and items() can be used with kwargs.

9. kwargs["key"] raises KeyError when the key does not exist.

10. kwargs.get("key") returns None when the key does not exist unless a default is provided.

11. kwargs can be modified inside the function.

12. kwargs can be combined with normal parameters.

13. kwargs can be combined with *args.

14. **dictionary can unpack a dictionary into keyword arguments.

15. Dictionary keys used through keyword argument syntax must satisfy Python's keyword/identifier rules.

16. The order of function parameters matters.

17. **kwargs is useful when the number of keyword arguments is not known in advance.

18. kwargs is especially useful for flexible APIs, configurations, and data-processing functions.
```

---

# 📊 66. `*args` and `**kwargs` Structure

```text
                         FUNCTION
                            │
             ┌──────────────┼──────────────┐
             ↓              ↓              ↓
        NORMAL PARAMS     *args         **kwargs
             │              │              │
             ↓              ↓              ↓
          Fixed Data    Positional     Keyword
                         Arguments     Arguments
                            │              │
                            ↓              ↓
                          Tuple        Dictionary
```

---

# 📊 67. `**kwargs` Data Flow

```text
             Keyword Arguments
                    │
                    ↓
          name="Asha"
          age=20
          course="BCA"
                    │
                    ↓
                **kwargs
                    │
                    ↓
              Dictionary
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
        keys()   values()   items()
          │         │         │
          ↓         ↓         ↓
         Keys     Values    Key + Value
```

---

# 📚 68. Complete `**kwargs` Cheat Sheet

### Define a Function with `**kwargs`

```python
def display(**kwargs):
    print(kwargs)
```

### Pass Keyword Arguments

```python
display(
    name="Asha",
    age=20
)
```

### Access a Value

```python
kwargs["name"]
```

### Safely Access a Value

```python
kwargs.get("name")
```

### Get All Keys

```python
kwargs.keys()
```

### Get All Values

```python
kwargs.values()
```

### Get Key-Value Pairs

```python
kwargs.items()
```

### Check for a Key

```python
"name" in kwargs
```

### Add a Value

```python
kwargs["city"] = "Bengaluru"
```

### Update Data

```python
kwargs.update({"status": "Active"})
```

### Remove a Key

```python
kwargs.pop("age")
```

### Copy Data

```python
new_data = kwargs.copy()
```

### Add Default Data

```python
kwargs.setdefault("city", "Bengaluru")
```

### Unpack a Dictionary

```python
display(**student)
```

---

# 🏆 69. `**kwargs` Mastery

```text
                           **kwargs
                              │
                              ↓
                  Variable Keyword Arguments
                              │
                              ↓
                         Dictionary
                              │
         ┌────────────────────┼────────────────────┐
         ↓                    ↓                    ↓
       ACCESS               MODIFY              PROCESS
         │                    │                    │
    ┌────┼────┐          ┌────┴────┐         ┌────┴────┐
    ↓    ↓    ↓          ↓         ↓         ↓         ↓
  get  keys values     update   setdefault  loops   conditions
         │
         ↓
      items()
         │
         ↓
    Key + Value
```

---

# 📚 70. Summary

In this lesson, you learned:

* What `**kwargs` is.
* What the term `kwargs` means.
* Why two asterisks are used.
* How `**kwargs` collects keyword arguments.
* That `kwargs` is stored as a dictionary.
* How to access values from `kwargs`.
* How to safely access values using `get()`.
* How to use `keys()`.
* How to use `values()`.
* How to use `items()`.
* How to loop through `kwargs`.
* How to check whether a key exists.
* How to modify `kwargs`.
* How to add and remove data from `kwargs`.
* How to use dictionary methods with `kwargs`.
* The difference between `*args` and `**kwargs`.
* How to combine `*args` and `**kwargs`.
* How to combine normal parameters with `**kwargs`.
* How dictionary unpacking works using `**`.
* How to pass dictionary data to a function.
* How to use `**kwargs` with conditions.
* How to process marks using `**kwargs`.
* How to calculate totals and averages.
* How to filter data using `kwargs`.
* How to use `**kwargs` in real-world applications.
* Common mistakes when using `**kwargs`.
* How to build flexible functions using `**kwargs`.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `**kwargs` means.
* [ ] I understand why two asterisks are used.
* [ ] I know that `kwargs` is a dictionary.
* [ ] I understand keyword arguments.
* [ ] I can create a function using `**kwargs`.
* [ ] I can pass multiple keyword arguments.
* [ ] I understand what happens when no keyword arguments are passed.
* [ ] I can access values from `kwargs`.
* [ ] I can use `get()` with `kwargs`.
* [ ] I can use `keys()` with `kwargs`.
* [ ] I can use `values()` with `kwargs`.
* [ ] I can use `items()` with `kwargs`.
* [ ] I can loop through `kwargs`.
* [ ] I can use conditions with `kwargs`.
* [ ] I can modify `kwargs`.
* [ ] I understand the difference between `*args` and `**kwargs`.
* [ ] I can combine `*args` and `**kwargs`.
* [ ] I can combine normal parameters with `**kwargs`.
* [ ] I understand dictionary unpacking.
* [ ] I can pass a dictionary using `**`.
* [ ] I understand the difference between `kwargs` and `**dictionary`.
* [ ] I can use `**kwargs` in real-world programs.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use `**kwargs` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: Function Scope and Lifetime**

In the next topic, you will learn:

* What function scope means.
* What local scope is.
* What global scope is.
* Understanding local variables.
* Understanding global variables.
* Local vs global variables.
* The `global` keyword.
* Modifying global variables inside functions.
* Nested function scope.
* Understanding enclosing scope.
* The LEGB rule.
* Local, Enclosing, Global, and Built-in scopes.
* Variable lifetime.
* When local variables are created.
* When local variables are destroyed.
* Scope-related common mistakes.
* Real-world examples.
* Advanced scope concepts.
* Practice programs.
* Challenges.

---

## ⭐ Quote of the Day

> **"The power of `**kwargs` is flexibility — it allows a function to work with data that may change without changing the function itself."** 🐍📚
