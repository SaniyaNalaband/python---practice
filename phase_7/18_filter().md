# 🐍 Python Master Course

# 📦 Phase 7: Functions

## 📌 Topic 18: `filter()`

**Difficulty:** ⭐ Intermediate → Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what the `filter()` function is.
* [ ] Understand why `filter()` is used.
* [ ] Understand the syntax of `filter()`.
* [ ] Understand how `filter()` works internally.
* [ ] Use `filter()` with functions.
* [ ] Use `filter()` with lambda functions.
* [ ] Use `filter()` with lists.
* [ ] Use `filter()` with tuples.
* [ ] Use `filter()` with sets.
* [ ] Use `filter()` with strings.
* [ ] Use `filter()` with dictionaries.
* [ ] Use `filter()` with conditions.
* [ ] Filter even and odd numbers.
* [ ] Filter positive and negative numbers.
* [ ] Filter values based on ranges.
* [ ] Filter strings based on length.
* [ ] Filter data using multiple conditions.
* [ ] Understand the `filter` object.
* [ ] Convert a `filter` object into a list.
* [ ] Convert a `filter` object into a tuple.
* [ ] Understand `filter()` vs list comprehension.
* [ ] Understand `filter()` vs normal loops.
* [ ] Combine `filter()` with `lambda`.
* [ ] Combine `filter()` with other functions.
* [ ] Use `filter()` in real-world applications.
* [ ] Avoid common mistakes when using `filter()`.

---

# 📖 1. What is `filter()`?

`filter()` is a built-in Python function used to **select elements from an iterable based on a condition**.

In simple words:

> `filter()` keeps the elements for which the condition is `True`.

For example, suppose we have a list of numbers:

```python
numbers = [10, 15, 20, 25, 30]
```

If we want only the even numbers, we can use `filter()`.

```python
def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)

print(list(result))
```

Output:

```text
[10, 20, 30]
```

Here:

* `is_even` → function containing the condition
* `numbers` → iterable
* `filter()` → selects matching elements
* `list()` → converts the filter object into a list

---

# 🧠 2. Why Do We Use `filter()`?

`filter()` is useful when we need to select only specific data from a collection.

For example:

```text
Original Data
     ↓
[10, 15, 20, 25, 30]
     ↓
    filter()
     ↓
Condition: number is even
     ↓
[10, 20, 30]
```

It is commonly used for:

* Selecting valid records.
* Filtering marks.
* Finding active users.
* Selecting products within a price range.
* Filtering positive numbers.
* Filtering strings.
* Selecting employees based on salary.
* Removing unwanted values.

---

# 📚 3. `filter()` Syntax

The general syntax is:

```python
filter(function, iterable)
```

There are two main parts:

```text
filter(function, iterable)
       ↓          ↓
   condition    data
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

def check(number):
    return number > 2

result = filter(check, numbers)

print(list(result))
```

Output:

```text
[3, 4, 5]
```

---

# 🔍 4. Understanding the `filter()` Parameters

`filter()` accepts two arguments.

### 1. Function

The function decides whether an element should be kept.

```python
def check(number):
    return number > 2
```

The function should generally return:

```text
True
```

or

```text
False
```

### 2. Iterable

The iterable contains the values that need to be checked.

Examples:

```python
list
tuple
set
string
dictionary
```

---

# 🧠 5. How Does `filter()` Work?

Consider:

```python
numbers = [10, 15, 20, 25]
```

And:

```python
def is_even(number):
    return number % 2 == 0
```

Then:

```python
result = filter(is_even, numbers)
```

Conceptually, Python checks each element:

```text
10 → is_even(10) → True  → Keep
15 → is_even(15) → False → Remove
20 → is_even(20) → True  → Keep
25 → is_even(25) → False → Remove
```

Final result:

```text
[10, 20]
```

---

# 🔄 6. Basic Example of `filter()`

```python
numbers = [10, 15, 20, 25, 30]

def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)

print(list(result))
```

Output:

```text
[10, 20, 30]
```

The function returns `True` for even numbers and `False` for odd numbers.

---

# 🧩 7. `filter()` Returns a Filter Object

An important point:

`filter()` does **not directly return a list**.

Example:

```python
numbers = [10, 15, 20, 25]

def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)

print(result)
```

Output will look similar to:

```text
<filter object at 0x...>
```

Therefore, we usually convert it into a list:

```python
print(list(result))
```

Output:

```text
[10, 20]
```

---

# 📦 8. Converting `filter()` into a List

This is one of the most common uses of `filter()`.

```python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(number):
    return number % 2 == 0

result = list(filter(is_even, numbers))

print(result)
```

Output:

```text
[2, 4, 6]
```

Structure:

```text
filter()
   ↓
filter object
   ↓
list()
   ↓
list
```

---

# 🔢 9. Filtering Even Numbers

```python
numbers = [11, 12, 13, 14, 15, 16]

def is_even(number):
    return number % 2 == 0

even_numbers = list(filter(is_even, numbers))

print(even_numbers)
```

Output:

```text
[12, 14, 16]
```

---

# 🔢 10. Filtering Odd Numbers

```python
numbers = [11, 12, 13, 14, 15, 16]

def is_odd(number):
    return number % 2 != 0

odd_numbers = list(filter(is_odd, numbers))

print(odd_numbers)
```

Output:

```text
[11, 13, 15]
```

---

# ➕ 11. Filtering Positive Numbers

```python
numbers = [-10, 5, -3, 8, 12, -7]

def is_positive(number):
    return number > 0

positive_numbers = list(filter(is_positive, numbers))

print(positive_numbers)
```

Output:

```text
[5, 8, 12]
```

---

# ➖ 12. Filtering Negative Numbers

```python
numbers = [-10, 5, -3, 8, 12, -7]

def is_negative(number):
    return number < 0

negative_numbers = list(filter(is_negative, numbers))

print(negative_numbers)
```

Output:

```text
[-10, -3, -7]
```

---

# 🟰 13. Filtering Numbers Greater Than a Value

```python
numbers = [10, 25, 40, 15, 60, 5]

def greater_than_20(number):
    return number > 20

result = list(filter(greater_than_20, numbers))

print(result)
```

Output:

```text
[25, 40, 60]
```

---

# 🔽 14. Filtering Numbers Less Than a Value

```python
numbers = [10, 25, 40, 15, 60, 5]

def less_than_20(number):
    return number < 20

result = list(filter(less_than_20, numbers))

print(result)
```

Output:

```text
[10, 15, 5]
```

---

# 📏 15. Filtering Numbers Within a Range

Suppose we want numbers between 20 and 50.

```python
numbers = [10, 20, 25, 35, 50, 60, 75]

def in_range(number):
    return 20 <= number <= 50

result = list(filter(in_range, numbers))

print(result)
```

Output:

```text
[20, 25, 35, 50]
```

---

# 🧠 16. `filter()` with a Lambda Function

Instead of creating a separate function, we can use a `lambda` function.

Example:

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[10, 20, 30]
```

Structure:

```text
filter()
   ↓
lambda condition
   ↓
iterable
   ↓
filtered result
```

---

# ⚡ 17. Why Use `lambda` with `filter()`?

When the condition is short, using `lambda` makes the code compact.

Without lambda:

```python
def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
```

With lambda:

```python
result = filter(lambda number: number % 2 == 0, numbers)
```

Both perform the same filtering operation.

---

# 🔍 18. Filtering Strings

`filter()` can also be used with strings.

Example:

```python
letters = "PythonProgramming"

result = filter(lambda letter: letter.isupper(), letters)

print(list(result))
```

Output:

```text
['P']
```

Here, only uppercase characters are selected.

---

# 🔤 19. Filtering Lowercase Characters

```python
text = "PyThOn"

result = filter(lambda character: character.islower(), text)

print(list(result))
```

Output:

```text
['y', 'h', 'n']
```

---

# 🔢 20. Filtering Digits from a String

```python
text = "Python123Programming45"

result = filter(lambda character: character.isdigit(), text)

print(list(result))
```

Output:

```text
['1', '2', '3', '4', '5']
```

---

# 🔤 21. Filtering Alphabetic Characters

```python
text = "Python123@Programming"

result = filter(lambda character: character.isalpha(), text)

print(list(result))
```

Output:

```text
['P', 'y', 't', 'h', 'o', 'n', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
```

---

# 📏 22. Filtering Strings by Length

Suppose we have:

```python
names = ["Asha", "Ananya", "Ravi", "Priyanka", "Sam"]
```

We want names having more than four characters.

```python
result = filter(lambda name: len(name) > 4, names)

print(list(result))
```

Output:

```text
['Ananya', 'Priyanka']
```

---

# 🧵 23. Filtering Names Starting with a Specific Letter

```python
names = ["Asha", "Ananya", "Ravi", "Arjun", "Priya"]

result = filter(lambda name: name.startswith("A"), names)

print(list(result))
```

Output:

```text
['Asha', 'Ananya', 'Arjun']
```

---

# 🧩 24. Filtering Names Ending with a Specific Letter

```python
names = ["Asha", "Ananya", "Ravi", "Arjun", "Priya"]

result = filter(lambda name: name.endswith("a"), names)

print(list(result))
```

Output:

```text
['Asha', 'Ananya', 'Priya']
```

---

# 📚 25. Filtering a Tuple

`filter()` can work with tuples.

```python
numbers = (10, 15, 20, 25, 30)

result = filter(lambda number: number % 5 == 0, numbers)

print(tuple(result))
```

Output:

```text
(10, 15, 20, 25, 30)
```

Since every number is divisible by 5, all values remain.

---

# 🔵 26. Filtering a Set

```python
numbers = {10, 15, 20, 25, 30}

result = filter(lambda number: number > 20, numbers)

print(set(result))
```

Possible output:

```text
{25, 30}
```

Remember that sets are unordered, so their displayed order should not be relied upon.

---

# 📖 27. Filtering Dictionary Values

Suppose:

```python
marks = {
    "Python": 90,
    "SQL": 72,
    "Git": 85,
    "HTML": 68
}
```

We can filter the dictionary items.

```python
result = filter(lambda item: item[1] >= 80, marks.items())

print(list(result))
```

Output:

```text
[('Python', 90), ('Git', 85)]
```

Here:

```text
item[0] → key
item[1] → value
```

---

# 🔑 28. Filtering Dictionary Keys

```python
students = {
    "Asha": 20,
    "Ananya": 21,
    "Ravi": 19,
    "Arjun": 22
}

result = filter(lambda name: name.startswith("A"), students.keys())

print(list(result))
```

Output:

```text
['Asha', 'Ananya', 'Arjun']
```

---

# 💰 29. Filtering Products by Price

```python
products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

result = filter(lambda item: item[1] > 5000, products.items())

print(list(result))
```

Output:

```text
[('Laptop', 55000), ('Monitor', 12000)]
```

---

# 🧑‍💼 30. Filtering Employees by Salary

```python
employees = {
    "Employee1": 35000,
    "Employee2": 52000,
    "Employee3": 45000,
    "Employee4": 65000
}

result = filter(lambda item: item[1] >= 50000, employees.items())

print(list(result))
```

Output:

```text
[('Employee2', 52000), ('Employee4', 65000)]
```

---

# 🎓 31. Filtering Student Marks

```python
marks = {
    "Python": 90,
    "SQL": 75,
    "Git": 85,
    "HTML": 65
}

result = filter(lambda item: item[1] >= 80, marks.items())

print(list(result))
```

Output:

```text
[('Python', 90), ('Git', 85)]
```

---

# 🧠 32. Filtering with Multiple Conditions

Multiple conditions can be combined using logical operators.

Example:

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

result = filter(
    lambda number: number > 15 and number < 35,
    numbers
)

print(list(result))
```

Output:

```text
[20, 25, 30]
```

The condition requires both conditions to be `True`.

---

# 🔗 33. Using `or` with `filter()`

```python
numbers = [10, 15, 20, 25, 30]

result = filter(
    lambda number: number == 10 or number == 30,
    numbers
)

print(list(result))
```

Output:

```text
[10, 30]
```

---

# 🚫 34. Filtering Values That Are Not Zero

```python
numbers = [0, 10, 0, 25, 30, 0]

result = filter(lambda number: number != 0, numbers)

print(list(result))
```

Output:

```text
[10, 25, 30]
```

---

# 🧠 35. `filter()` with Boolean Values

`filter()` can also work with `None` as the function.

Syntax:

```python
filter(None, iterable)
```

In this case, Python keeps truthy values.

Example:

```python
values = [0, 1, "", "Python", None, 25, False]

result = filter(None, values)

print(list(result))
```

Output:

```text
[1, 'Python', 25]
```

Here, falsy values are removed.

---

# ⚖️ 36. Truthy and Falsy Values with `filter()`

Python considers values such as these falsy:

```text
0
False
None
""
[]
{}
()
```

When we use:

```python
filter(None, data)
```

these falsy values are excluded.

Example:

```python
data = [0, 1, 2, "", "Python", None]

print(list(filter(None, data)))
```

Output:

```text
[1, 2, 'Python']
```

---

# 🔄 37. `filter()` vs Normal `for` Loop

Without `filter()`:

```python
numbers = [10, 15, 20, 25]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)

print(result)
```

Output:

```text
[10, 20]
```

Using `filter()`:

```python
numbers = [10, 15, 20, 25]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[10, 20]
```

Both produce the same result.

---

# ⚖️ 38. `filter()` vs List Comprehension

Using `filter()`:

```python
numbers = [10, 15, 20, 25]

result = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(result)
```

Using list comprehension:

```python
numbers = [10, 15, 20, 25]

result = [
    number
    for number in numbers
    if number % 2 == 0
]

print(result)
```

Both produce:

```text
[10, 20]
```

### General idea:

```text
filter()
   ↓
Select elements

list comprehension
   ↓
Select and/or transform elements
```

---

# 🧠 39. When Should You Use `filter()`?

`filter()` is useful when your main goal is:

> **Keep elements that satisfy a condition.**

Example:

```python
numbers = [10, 20, 30, 40]

result = filter(lambda number: number > 20, numbers)
```

Use list comprehension when you also need to transform the values.

---

# 🔄 40. `filter()` with `map()`

`filter()` and `map()` can be combined.

Suppose:

```python
numbers = [1, 2, 3, 4, 5, 6]
```

First filter even numbers:

```python
even_numbers = filter(lambda number: number % 2 == 0, numbers)
```

Then square them:

```python
squared = map(lambda number: number ** 2, even_numbers)

print(list(squared))
```

Output:

```text
[4, 16, 36]
```

Flow:

```text
Original Data
     ↓
  filter()
     ↓
Even Numbers
     ↓
   map()
     ↓
Squared Numbers
```

---

# 🧮 41. `filter()` with `sum()`

We can filter values and then calculate their sum.

```python
numbers = [10, 15, 20, 25, 30]

even_numbers = filter(lambda number: number % 2 == 0, numbers)

total = sum(even_numbers)

print(total)
```

Output:

```text
60
```

Because:

```text
10 + 20 + 30 = 60
```

---

# 🔢 42. Counting Filtered Values

We can use `len()` after converting the result into a list.

```python
numbers = [10, 15, 20, 25, 30]

result = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(len(result))
```

Output:

```text
3
```

---

# 📊 43. Filtering Student Records

Consider:

```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Ananya", "marks": 72},
    {"name": "Ravi", "marks": 91},
    {"name": "Arjun", "marks": 68}
]
```

We can filter students who scored at least 80.

```python
result = filter(
    lambda student: student["marks"] >= 80,
    students
)

print(list(result))
```

Output:

```text
[
    {'name': 'Asha', 'marks': 85},
    {'name': 'Ravi', 'marks': 91}
]
```

---

# 🌍 44. Real-World Example: Active Users

Suppose an application stores users:

```python
users = [
    {"name": "Asha", "active": True},
    {"name": "Ravi", "active": False},
    {"name": "Ananya", "active": True},
    {"name": "Arjun", "active": False}
]
```

We can filter active users:

```python
active_users = filter(
    lambda user: user["active"],
    users
)

print(list(active_users))
```

Output:

```text
[
    {'name': 'Asha', 'active': True},
    {'name': 'Ananya', 'active': True}
]
```

---

# 🌍 45. Real-World Example: Products Within Budget

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]

budget_products = filter(
    lambda product: product["price"] <= 15000,
    products
)

print(list(budget_products))
```

Output:

```text
[
    {'name': 'Mouse', 'price': 800},
    {'name': 'Keyboard', 'price': 1500},
    {'name': 'Monitor', 'price': 12000}
]
```

---

# 🌍 46. Real-World Example: Employee Experience

```python
employees = [
    {"name": "Employee1", "experience": 1},
    {"name": "Employee2", "experience": 4},
    {"name": "Employee3", "experience": 6},
    {"name": "Employee4", "experience": 2}
]

experienced = filter(
    lambda employee: employee["experience"] >= 4,
    employees
)

print(list(experienced))
```

Output:

```text
[
    {'name': 'Employee2', 'experience': 4},
    {'name': 'Employee3', 'experience': 6}
]
```

---

# 🌍 47. Real-World Example: Passing Students

```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Ravi", "marks": 42},
    {"name": "Ananya", "marks": 76},
    {"name": "Arjun", "marks": 35}
]

passed = filter(
    lambda student: student["marks"] >= 40,
    students
)

print(list(passed))
```

Output:

```text
[
    {'name': 'Asha', 'marks': 85},
    {'name': 'Ananya', 'marks': 76},
    {'name': 'Ravi', 'marks': 42}
]
```

---

# 🔥 48. Advanced Example: Filtering by Multiple Conditions

Suppose employees must:

* Have salary greater than ₹40,000.
* Have experience of at least 3 years.

```python
employees = [
    {"name": "Employee1", "salary": 35000, "experience": 5},
    {"name": "Employee2", "salary": 55000, "experience": 4},
    {"name": "Employee3", "salary": 45000, "experience": 2},
    {"name": "Employee4", "salary": 65000, "experience": 6}
]

result = filter(
    lambda employee:
        employee["salary"] > 40000 and
        employee["experience"] >= 3,
    employees
)

print(list(result))
```

Output:

```text
[
    {'name': 'Employee2', 'salary': 55000, 'experience': 4},
    {'name': 'Employee4', 'salary': 65000, 'experience': 6}
]
```

---

# 🧠 49. Important Concept: `filter()` is Lazy

`filter()` uses lazy evaluation.

This means Python does not necessarily create all filtered results immediately.

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = filter(lambda number: number > 2, numbers)

print(result)
```

The result is a filter object.

When we iterate over it:

```python
print(list(result))
```

Python evaluates the elements and produces:

```text
[3, 4, 5]
```

This behavior can be useful when working with large amounts of data.

---

# ⚠️ 50. Common Mistake: Forgetting `list()`

Consider:

```python
numbers = [10, 20, 30]

result = filter(lambda number: number > 15, numbers)

print(result)
```

You may expect:

```text
[20, 30]
```

But Python displays a filter object.

Correct:

```python
print(list(result))
```

Output:

```text
[20, 30]
```

---

# ⚠️ 51. Common Mistake: Calling the Function Immediately

Wrong:

```python
result = filter(is_even(), numbers)
```

This calls the function immediately.

Correct:

```python
result = filter(is_even, numbers)
```

Here, the function itself is passed to `filter()`.

Remember:

```text
is_even
   ↓
function object

is_even()
   ↓
function call
```

---

# ⚠️ 52. Common Mistake: Returning the Wrong Condition

Suppose:

```python
def is_even(number):
    print(number % 2 == 0)
```

This function prints the result but does not return it.

For `filter()`, we normally need the function to return a truth value.

Correct:

```python
def is_even(number):
    return number % 2 == 0
```

---

# ⚠️ 53. Common Mistake: Reusing an Exhausted Filter Object

A `filter` object is an iterator.

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = filter(lambda number: number > 2, numbers)

print(list(result))
print(list(result))
```

Output:

```text
[3, 4, 5]
[]
```

Why?

Because the filter iterator has already been consumed.

If you need to use the results multiple times, store them in a list:

```python
result = list(
    filter(lambda number: number > 2, numbers)
)

print(result)
print(result)
```

Output:

```text
[3, 4, 5]
[3, 4, 5]
```

---

# ⚖️ 54. `filter()` vs `map()`

These functions have different purposes.

| Function   | Purpose             |
| ---------- | ------------------- |
| `filter()` | Selects elements    |
| `map()`    | Transforms elements |

Example of `filter()`:

```python
numbers = [1, 2, 3, 4]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4]
```

Example of `map()`:

```python
numbers = [1, 2, 3, 4]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

Remember:

```text
filter() → Which elements should remain?

map()    → How should each element change?
```

---

# 📊 55. `filter()` Comparison Table

| Feature                         | `filter()`               |
| ------------------------------- | ------------------------ |
| Purpose                         | Select elements          |
| Input                           | Function + iterable      |
| Function result                 | Usually `True` / `False` |
| Output                          | Filter object            |
| Converts automatically to list? | ❌                        |
| Works with lambda?              | ✅                        |
| Works with lists?               | ✅                        |
| Works with tuples?              | ✅                        |
| Works with sets?                | ✅                        |
| Works with strings?             | ✅                        |
| Lazy evaluation                 | ✅                        |
| Original iterable modified?     | ❌                        |

---

# 💻 56. Practice Programs

## 🟢 Easy

### Program 1: Filter Even Numbers

```python
numbers = [10, 15, 20, 25, 30]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

---

### Program 2: Filter Positive Numbers

```python
numbers = [-10, 20, -5, 30, -2, 40]

result = filter(lambda number: number > 0, numbers)

print(list(result))
```

---

### Program 3: Filter Numbers Greater Than 50

```python
numbers = [20, 55, 40, 80, 35, 90]

result = filter(lambda number: number > 50, numbers)

print(list(result))
```

---

### Program 4: Filter Long Names

```python
names = ["Asha", "Ananya", "Ravi", "Priyanka", "Sam"]

result = filter(lambda name: len(name) > 5, names)

print(list(result))
```

---

# 🟡 Medium

### Program 5: Filter Odd Numbers

```python
numbers = [11, 12, 13, 14, 15, 16]

result = filter(lambda number: number % 2 != 0, numbers)

print(list(result))
```

---

### Program 6: Filter Names Starting with A

```python
names = ["Asha", "Ravi", "Ananya", "Priya", "Arjun"]

result = filter(lambda name: name.startswith("A"), names)

print(list(result))
```

---

### Program 7: Filter Marks Greater Than 75

```python
marks = {
    "Python": 90,
    "SQL": 72,
    "Git": 85,
    "HTML": 68
}

result = filter(lambda item: item[1] > 75, marks.items())

print(list(result))
```

---

### Program 8: Remove Zero Values

```python
numbers = [0, 10, 0, 20, 30, 0]

result = filter(lambda number: number != 0, numbers)

print(list(result))
```

---

# 🔴 Advanced

## Program 9: Filter Students Who Passed

```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Ravi", "marks": 35},
    {"name": "Ananya", "marks": 76},
    {"name": "Arjun", "marks": 42}
]

result = filter(
    lambda student: student["marks"] >= 40,
    students
)

print(list(result))
```

---

## Program 10: Filter Products Within Budget

```python
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Mouse", "price": 800},
    {"name": "Keyboard", "price": 1500},
    {"name": "Monitor", "price": 12000}
]

result = filter(
    lambda product: product["price"] <= 15000,
    products
)

print(list(result))
```

---

## Program 11: Filter Employees by Salary

```python
employees = [
    {"name": "Employee1", "salary": 35000},
    {"name": "Employee2", "salary": 55000},
    {"name": "Employee3", "salary": 45000},
    {"name": "Employee4", "salary": 65000}
]

result = filter(
    lambda employee: employee["salary"] >= 50000,
    employees
)

print(list(result))
```

---

## Program 12: Filter Using Multiple Conditions

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

result = filter(
    lambda number:
        number > 15 and number < 35,
    numbers
)

print(list(result))
```

---

# 🏆 57. Challenge

Create a list of student records:

```text
Asha       → 85
Ravi       → 72
Ananya     → 91
Arjun      → 65
Priya      → 88
```

Store them using dictionaries inside a list.

Then:

1. Use `filter()` to find students who scored at least 80.
2. Convert the result into a list.
3. Display the filtered students.
4. Use `filter()` to find students who scored below 70.
5. Count how many students scored at least 80.
6. Create another filter to find students whose names start with `"A"`.
7. Use multiple conditions to find students whose marks are between 70 and 90.
8. Display the final filtered results.

Example starting data:

```python
students = [
    {"name": "Asha", "marks": 85},
    {"name": "Ravi", "marks": 72},
    {"name": "Ananya", "marks": 91},
    {"name": "Arjun", "marks": 65},
    {"name": "Priya", "marks": 88}
]
```

Try solving the challenge without copying the solution.

---

# 🧪 58. Mini Project: Student Performance Filter

Create a student performance filtering system.

Each student should contain:

* Student ID
* Name
* Course
* Marks
* Attendance
* Status

Example:

```python
students = [
    {
        "id": 101,
        "name": "Asha",
        "course": "BCA",
        "marks": 85,
        "attendance": 92,
        "status": "Active"
    },
    {
        "id": 102,
        "name": "Ravi",
        "course": "BCA",
        "marks": 68,
        "attendance": 75,
        "status": "Active"
    },
    {
        "id": 103,
        "name": "Ananya",
        "course": "BCA",
        "marks": 91,
        "attendance": 95,
        "status": "Active"
    }
]
```

Perform the following operations:

* Use `filter()` to find students who scored at least 80.
* Use `filter()` to find students with attendance of at least 85%.
* Use `filter()` to find active students.
* Use `filter()` to find students who satisfy both marks and attendance requirements.
* Use `filter()` to find students whose names start with `"A"`.
* Convert the filtered results into lists.
* Display the final filtered records.

### Your Goal

Build a complete student filtering program using `filter()` and `lambda`.

---

# 🎤 59. Interview Questions

* [ ] What is the `filter()` function in Python?
* [ ] Why is `filter()` used?
* [ ] What is the syntax of `filter()`?
* [ ] What are the arguments of `filter()`?
* [ ] What should the filtering function return?
* [ ] What does `filter()` return?
* [ ] Why do we use `list()` with `filter()`?
* [ ] Can `filter()` work with lambda functions?
* [ ] Can `filter()` work with lists?
* [ ] Can `filter()` work with tuples?
* [ ] Can `filter()` work with sets?
* [ ] Can `filter()` work with strings?
* [ ] Can `filter()` work with dictionaries?
* [ ] How can you filter dictionary values?
* [ ] How can you filter dictionary keys?
* [ ] What does `filter(None, iterable)` do?
* [ ] What are truthy and falsy values?
* [ ] What is lazy evaluation?
* [ ] Is a `filter` object reusable?
* [ ] What happens when a filter object is consumed?
* [ ] What is the difference between `filter()` and `map()`?
* [ ] What is the difference between `filter()` and list comprehension?
* [ ] Does `filter()` modify the original iterable?
* [ ] Can multiple conditions be used with `filter()`?
* [ ] How can `filter()` be combined with `map()`?
* [ ] How can `filter()` be used with real-world data?

---

# 📝 60. Assignment

Complete the following programs.

### Task 1

Create a list of numbers.

Use `filter()` to display only even numbers.

---

### Task 2

Create a list of numbers containing positive and negative values.

Use `filter()` to display only positive numbers.

---

### Task 3

Create a list of numbers.

Use `filter()` to display numbers greater than `50`.

---

### Task 4

Create a list of names.

Use `filter()` to display names having more than five characters.

---

### Task 5

Create a list of names.

Use `filter()` to display names starting with `"A"`.

---

### Task 6

Create a list of marks.

Use `filter()` to display marks greater than or equal to `75`.

---

### Task 7

Create a list of numbers containing zero values.

Use:

```python
filter(None, numbers)
```

to remove falsy values.

---

### Task 8

Create a dictionary containing subjects and marks.

Use `filter()` with `items()` to display subjects having marks greater than `80`.

---

### Task 9

Create a list of student dictionaries.

Use `filter()` to display students who passed.

---

### Task 10

Create a list of products containing product names and prices.

Use `filter()` to display products costing less than `10000`.

---

### Task 11

Create a real-world dataset and use at least five different filtering conditions.

Use:

* `filter()`
* `lambda`
* `items()` or dictionary indexing
* Multiple conditions
* List conversion

---

### Task 12

Create a program that uses `filter()` and `map()` together.

First filter the required values and then transform the filtered values.

---

# 🧠 61. Memory Tricks

Remember:

```text
filter()
   ↓
Keep required elements
```

Remember the basic structure:

```text
filter(function, iterable)
       ↓          ↓
   condition     data
```

Remember:

```text
True
 ↓
Keep

False
 ↓
Remove
```

Remember:

```text
filter()
   ↓
Select
```

Whereas:

```text
map()
 ↓
Transform
```

---

# 📌 62. Important Rules to Remember

```text
1. filter() is a built-in Python function.

2. filter() is used to select elements based on a condition.

3. The syntax is filter(function, iterable).

4. The function normally returns True or False.

5. True means the element is kept.

6. False means the element is excluded.

7. filter() returns a filter object.

8. Use list() to convert the filter object into a list.

9. filter() does not modify the original iterable.

10. filter() can work with lambda functions.

11. filter() can work with lists, tuples, sets, strings, and dictionaries.

12. filter(None, iterable) keeps truthy values.

13. A filter object is an iterator.

14. A filter object can be exhausted after iteration.

15. Store the result in a list if you need to reuse it.

16. Multiple conditions can be combined using and/or.

17. filter() is useful for selecting data.

18. filter() can be combined with map().

19. filter() is different from map().

20. filter() is different from list comprehension.

21. filter() is especially useful when the main operation is selection.

22. lambda is commonly used when the filtering condition is short.
```

---

# 📊 63. `filter()` Structure

```text
                         ITERABLE
                            │
                            ↓
                        filter()
                            │
                  ┌─────────┴─────────┐
                  ↓                   ↓
              FUNCTION            DATA
                  │                   │
                  ↓                   ↓
              CONDITION           VALUES
                  │
          ┌───────┴───────┐
          ↓               ↓
        True             False
          ↓               ↓
        KEEP            REMOVE
          │
          ↓
     FILTER OBJECT
          │
          ↓
       list()
          │
          ↓
   FILTERED RESULTS
```

---

# 📚 64. Complete `filter()` Cheat Sheet

### Basic `filter()`

```python
filter(function, iterable)
```

### Filter Even Numbers

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

### Filter Odd Numbers

```python
list(filter(lambda x: x % 2 != 0, numbers))
```

### Filter Positive Numbers

```python
list(filter(lambda x: x > 0, numbers))
```

### Filter Negative Numbers

```python
list(filter(lambda x: x < 0, numbers))
```

### Filter Greater Values

```python
list(filter(lambda x: x > 50, numbers))
```

### Filter Smaller Values

```python
list(filter(lambda x: x < 50, numbers))
```

### Filter by String Length

```python
list(filter(lambda x: len(x) > 5, names))
```

### Filter by Starting Character

```python
list(filter(lambda x: x.startswith("A"), names))
```

### Filter Dictionary Items

```python
list(filter(lambda item: item[1] > 80, marks.items()))
```

### Remove Falsy Values

```python
list(filter(None, values))
```

### Multiple Conditions

```python
list(
    filter(
        lambda x: x > 10 and x < 50,
        numbers
    )
)
```

### Filter Student Records

```python
list(
    filter(
        lambda student: student["marks"] >= 80,
        students
    )
)
```

### Filter Products

```python
list(
    filter(
        lambda product: product["price"] <= 10000,
        products
    )
)
```

---

# 🏆 65. `filter()` Mastery

```text
                           filter()
                              │
                              ↓
                       Select Elements
                              │
                ┌─────────────┴─────────────┐
                ↓                           ↓
             Function                    Iterable
                │                           │
                ↓                           ↓
            Condition                    Data
                │
        ┌───────┴───────┐
        ↓               ↓
      True            False
        ↓               ↓
      Keep            Remove
        │
        ↓
   Filter Object
        │
        ↓
      list()
        │
        ↓
 Filtered Data
```

---

# 📚 66. Summary

In this lesson, you learned:

* What `filter()` is.
* Why `filter()` is used.
* The syntax of `filter()`.
* The two arguments of `filter()`.
* How the filtering function works.
* How `filter()` selects elements.
* What `filter()` returns.
* Why `list()` is commonly used with `filter()`.
* How to filter even numbers.
* How to filter odd numbers.
* How to filter positive numbers.
* How to filter negative numbers.
* How to filter numbers within a range.
* How to use `filter()` with lambda functions.
* How to filter strings.
* How to filter strings by length.
* How to filter strings by starting characters.
* How to filter tuples.
* How to filter sets.
* How to filter dictionary keys.
* How to filter dictionary values.
* How to filter dictionary items.
* How to use multiple conditions.
* How to use `filter(None, iterable)`.
* What truthy and falsy values are.
* What a filter object is.
* How lazy evaluation works.
* Why a filter object can be exhausted.
* The difference between `filter()` and `map()`.
* The difference between `filter()` and list comprehension.
* How to combine `filter()` with `map()`.
* How to use `filter()` with real-world data.
* Common mistakes when using `filter()`.
* How to use `filter()` in practical programs.

---

# 🎯 Topic Completion Checklist

* [ ] I understand what `filter()` is.
* [ ] I understand why `filter()` is used.
* [ ] I know the syntax of `filter()`.
* [ ] I understand the function argument.
* [ ] I understand the iterable argument.
* [ ] I understand that the condition should return a truth value.
* [ ] I understand that `filter()` returns a filter object.
* [ ] I know how to convert a filter object into a list.
* [ ] I can filter even numbers.
* [ ] I can filter odd numbers.
* [ ] I can filter positive numbers.
* [ ] I can filter negative numbers.
* [ ] I can filter values based on a range.
* [ ] I can use `filter()` with lambda.
* [ ] I can filter strings.
* [ ] I can filter strings based on length.
* [ ] I can filter dictionary keys.
* [ ] I can filter dictionary values.
* [ ] I can filter dictionary items.
* [ ] I understand `filter(None, iterable)`.
* [ ] I understand truthy and falsy values.
* [ ] I understand lazy evaluation.
* [ ] I understand filter object exhaustion.
* [ ] I can combine `filter()` with multiple conditions.
* [ ] I understand the difference between `filter()` and `map()`.
* [ ] I understand the difference between `filter()` and list comprehension.
* [ ] I can combine `filter()` and `map()`.
* [ ] I can use `filter()` with real-world data.
* [ ] I completed all practice programs.
* [ ] I completed the challenge.
* [ ] I completed the assignment.
* [ ] I can use `filter()` without looking at my notes.

---

# 🚀 Next Topic

➡️ **Next Topic: `map()`**

In the next topic, you will learn:

* What the `map()` function is.
* Why `map()` is used.
* Basic `map()` syntax.
* How `map()` works.
* Using `map()` with normal functions.
* Using `map()` with lambda functions.
* Using `map()` with lists.
* Using `map()` with tuples.
* Using `map()` with sets.
* Using `map()` with strings.
* Using `map()` with multiple iterables.
* Using `map()` with multiple arguments.
* Transforming numbers using `map()`.
* Transforming strings using `map()`.
* Converting values using `map()`.
* Combining `map()` with `filter()`.
* Combining `map()` with `zip()`.
* Understanding the `map` object.
* Understanding lazy evaluation.
* `map()` vs list comprehension.
* Real-world examples.
* Common mistakes.
* Advanced `map()` techniques.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Filtering helps you focus on the data that actually matters."** 🐍📚
