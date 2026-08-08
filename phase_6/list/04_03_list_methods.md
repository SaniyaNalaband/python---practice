# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 4 (Part 3): Searching & Counting List Elements**

**Topics Covered:**

- ✅ `index()`
- ✅ `count()`
- ✅ `in` operator

**Difficulty:** ⭐ Beginner → ⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Find the position of an element using `index()`.
- [ ] Count occurrences using `count()`.
- [ ] Check whether an element exists using `in`.
- [ ] Understand the difference between `index()`, `count()`, and `in`.
- [ ] Use these operations in real-world programs.

---

# 📌 Method 1: `index()`

## 📖 What is `index()`?

The `index()` method returns the **index position of the first occurrence** of a specified value.

### Syntax

```python
list_name.index(value)
```

---

## Example 1

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

position = fruits.index("Mango")

print(position)
```

Output

```text
2
```

The index of `"Mango"` is `2`.

---

# 📖 Example 2: First Occurrence

```python
numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))
```

Output

```text
1
```

Although `20` appears twice, `index()` returns the position of the **first occurrence**.

---

# 📖 Example 3: Using a Variable

```python
colors = ["Red", "Blue", "Green"]

color = "Blue"

position = colors.index(color)

print("Position:", position)
```

Output

```text
Position: 1
```

---

# 📖 Searching Within a Specific Range

`index()` can also accept optional `start` and `stop` positions.

### Syntax

```python
list_name.index(value, start, stop)
```

Example:

```python
numbers = [10, 20, 30, 20, 40, 20]

print(numbers.index(20, 2))
```

Output

```text
3
```

Python starts searching from index `2`.

---

# ⚠️ Value Not Found

```python
numbers = [10, 20, 30]

print(numbers.index(50))
```

Output

```text
ValueError: 50 is not in list
```

So, before using `index()`, you can check whether the value exists.

```python
numbers = [10, 20, 30]

if 50 in numbers:
    print(numbers.index(50))
else:
    print("Value not found")
```

Output

```text
Value not found
```

---

# 📌 Method 2: `count()`

## 📖 What is `count()`?

The `count()` method returns the **number of times a value appears** in a list.

### Syntax

```python
list_name.count(value)
```

---

## Example 1

```python
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))
```

Output

```text
3
```

`20` appears three times.

---

# 📖 Example 2

```python
fruits = ["Apple", "Mango", "Apple", "Orange"]

print(fruits.count("Apple"))
```

Output

```text
2
```

---

# 📖 Example 3: Value Does Not Exist

```python
numbers = [10, 20, 30]

print(numbers.count(100))
```

Output

```text
0
```

Unlike `index()`, `count()` does not raise an error if the value is absent.

---

# 📌 Method 3: `in` Operator

## 📖 What is `in`?

The `in` operator checks whether an element **exists inside a list**.

It returns either:

```text
True
```

or

```text
False
```

### Syntax

```python
value in list_name
```

---

## Example 1

```python
fruits = ["Apple", "Banana", "Mango"]

print("Mango" in fruits)
```

Output

```text
True
```

---

## Example 2

```python
fruits = ["Apple", "Banana", "Mango"]

print("Orange" in fruits)
```

Output

```text
False
```

---

# 📖 Using `in` with `if`

```python
students = ["Aisha", "Saniya", "Rohan"]

if "Saniya" in students:
    print("Student Found")
```

Output

```text
Student Found
```

---

# 📖 Using `not in`

Python also provides the `not in` operator.

```python
fruits = ["Apple", "Banana", "Mango"]

print("Orange" not in fruits)
```

Output

```text
True
```

---

# 📊 `index()` vs `count()` vs `in`

| Operation | Purpose | Result |
|----------|---------|--------|
| `index()` | Finds position | Index number |
| `count()` | Counts occurrences | Integer |
| `in` | Checks existence | `True` / `False` |
| `not in` | Checks absence | `True` / `False` |

---

# 🔥 Important Difference

Consider:

```python
numbers = [10, 20, 20, 30, 20]
```

### `index()`

```python
print(numbers.index(20))
```

Output:

```text
1
```

It tells you **where the first `20` is located**.

---

### `count()`

```python
print(numbers.count(20))
```

Output:

```text
3
```

It tells you **how many times `20` appears**.

---

### `in`

```python
print(20 in numbers)
```

Output:

```text
True
```

It tells you **whether `20` exists**.

---

# 📊 Trace Table

```python
numbers = [10, 20, 30, 20, 40]
```

| Expression | Result | Meaning |
|-----------|--------|---------|
| `numbers.index(20)` | `1` | First position |
| `numbers.count(20)` | `2` | Appears twice |
| `20 in numbers` | `True` | Exists |
| `50 in numbers` | `False` | Doesn't exist |

---

# 🌍 Real-World Examples

## Student Search

```python
students = ["Aisha", "Saniya", "Rohan", "Karan"]

if "Saniya" in students:
    print("Student is registered")
```

Output

```text
Student is registered
```

---

## Product Search

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

if "Mouse" in products:
    print("Product Available")
else:
    print("Product Not Available")
```

Output

```text
Product Available
```

---

## Counting Votes

```python
votes = ["Yes", "No", "Yes", "Yes", "No"]

yes_votes = votes.count("Yes")

print("Yes Votes:", yes_votes)
```

Output

```text
Yes Votes: 3
```

---

## Finding a Student's Position

```python
students = ["Aisha", "Saniya", "Rohan", "Karan"]

position = students.index("Rohan")

print("Position:", position)
```

Output

```text
Position: 2
```

---

# 📖 Combining the Methods

You can use these operations together.

```python
numbers = [10, 20, 30, 20, 40, 20]

if 20 in numbers:
    print("20 exists")
    print("First Position:", numbers.index(20))
    print("Total Occurrences:", numbers.count(20))
```

Output

```text
20 exists
First Position: 1
Total Occurrences: 3
```

---

# ⚠️ Common Mistakes

## ❌ Using `index()` When You Only Need to Check Existence

Instead of:

```python
if numbers.index(50):
    print("Found")
```

Use:

```python
if 50 in numbers:
    print("Found")
```

`index()` is meant to **find a position**, while `in` is meant to **check existence**.

---

## ❌ Forgetting That `index()` Starts from 0

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Apple"))
```

Output:

```text
0
```

The first element has index `0`.

---

## ❌ Thinking `count()` Returns an Index

```python
numbers = [10, 20, 20, 30]

print(numbers.count(20))
```

Output:

```text
2
```

This means `20` occurs **two times**. It does not mean the index is `2`.

---

# 💡 Best Practices

- Use `index()` when you need the **position**.
- Use `count()` when you need the **number of occurrences**.
- Use `in` when you only need to know whether an element exists.
- Check with `in` before using `index()` if the value might not exist.

---

# 🚀 Pro Tips

These operations are useful in:

- Search systems
- Student management
- Inventory systems
- Attendance applications
- Voting systems
- Data analysis
- Duplicate detection

---

# ❓ Interview Questions

- [ ] What does `index()` return?
- [ ] What happens if `index()` cannot find the value?
- [ ] What does `count()` return?
- [ ] What is the difference between `index()` and `count()`?
- [ ] What does the `in` operator return?
- [ ] What is the difference between `in` and `not in`?

---

# 🏋️ Practice Programs

## Easy

```python
numbers = [10, 20, 30, 40]

print(numbers.index(30))
```

---

```python
numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))
```

---

```python
fruits = ["Apple", "Banana", "Mango"]

print("Mango" in fruits)
```

---

## Medium

```python
students = ["Aisha", "Saniya", "Rohan", "Karan"]

if "Rohan" in students:
    print("Student Found")
```

---

```python
numbers = [5, 10, 5, 20, 5, 30]

print("First Position:", numbers.index(5))
print("Occurrences:", numbers.count(5))
```

---

## Advanced

```python
products = ["Laptop", "Mouse", "Keyboard", "Mouse", "Monitor"]

product = "Mouse"

if product in products:
    print("Product Available")
    print("First Position:", products.index(product))
    print("Quantity:", products.count(product))
else:
    print("Product Not Available")
```

---

# 🎯 Challenge

Write programs to:

1. Check whether a city exists in a list.
2. Find the position of a particular student.
3. Count how many times a number occurs.
4. Check whether a product is available.
5. Combine `in`, `index()`, and `count()` in one program.

---

# 📝 Assignment

- [ ] Find the index of an element using `index()`.
- [ ] Find the number of occurrences using `count()`.
- [ ] Check whether an element exists using `in`.
- [ ] Check whether an element does not exist using `not in`.
- [ ] Handle a value that doesn't exist before using `index()`.
- [ ] Create a real-world program using all three.

---

# 📚 Summary

You learned:

- ✅ `index()` finds the **first position** of a value.
- ✅ `count()` finds **how many times** a value occurs.
- ✅ `in` checks whether a value **exists**.
- ✅ `not in` checks whether a value **doesn't exist**.

### Key Points to Remember

```python
numbers.index(20)
```

➡️ **Where is it?**

```python
numbers.count(20)
```

➡️ **How many are there?**

```python
20 in numbers
```

➡️ **Does it exist?**

---

# 🎯 Topic Completion Checklist

- [ ] I understand `index()`.
- [ ] I understand `count()`.
- [ ] I understand the `in` operator.
- [ ] I understand `not in`.
- [ ] I know the difference between all three.
- [ ] I completed the practice programs.
- [ ] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 4 (Part 4): Sorting & Reversing**
- `sort()`
- `reverse()`
- `sorted()`