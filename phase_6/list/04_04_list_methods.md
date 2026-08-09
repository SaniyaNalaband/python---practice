# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 4 (Part 4): Sorting & Reversing Lists**

**Topics Covered:**

- ✅ `sort()`
- ✅ `reverse()`
- ✅ `sorted()` function

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Sort a list in ascending order.
- [ ] Sort a list in descending order.
- [ ] Sort strings alphabetically.
- [ ] Sort lists using `key`.
- [ ] Reverse the order of elements.
- [ ] Understand the difference between `sort()` and `sorted()`.
- [ ] Understand the `reverse` parameter.
- [ ] Use sorting in real-world programs.

---

# 📖 Why Do We Need Sorting?

Sorting means arranging elements in a particular order.

For example:

```text
Before:

[50, 10, 40, 20, 30]

After:

[10, 20, 30, 40, 50]
```

Sorting is useful when working with:

- Student marks
- Product prices
- Employee salaries
- Names
- Scores
- Dates
- Rankings

---

# 📌 Method 1: `sort()`

## 📖 What is `sort()`?

The `sort()` method sorts the **original list**.

### Syntax

```python
list_name.sort()
```

By default, it sorts in **ascending order**.

---

# 📖 Example 1: Numbers

```python
numbers = [50, 20, 40, 10, 30]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 📖 Example 2: Already Sorted List

```python
numbers = [10, 20, 30, 40]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

The list remains unchanged because it is already sorted.

---

# 📖 Example 3: Descending Order

Use:

```python
reverse=True
```

```python
numbers = [50, 20, 40, 10, 30]

numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

# 📊 Ascending vs Descending

```python
numbers = [40, 10, 30, 20]
```

### Ascending

```python
numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### Descending

```python
numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

---

# 📌 Sorting Strings

Strings can also be sorted alphabetically.

```python
fruits = ["Mango", "Apple", "Banana", "Orange"]

fruits.sort()

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

---

# 📖 Descending Alphabetical Order

```python
fruits = ["Mango", "Apple", "Banana", "Orange"]

fruits.sort(reverse=True)

print(fruits)
```

Output:

```text
['Orange', 'Mango', 'Banana', 'Apple']
```

---

# 📌 Sorting and Case Sensitivity

Python's default string sorting is case-sensitive.

```python
names = ["apple", "Banana", "cherry", "Apple"]

names.sort()

print(names)
```

The ordering may not be what you expect because uppercase and lowercase characters have different character codes.

---

# 📖 Case-Insensitive Sorting

Use:

```python
key=str.lower
```

Example:

```python
names = ["apple", "Banana", "cherry", "Apple"]

names.sort(key=str.lower)

print(names)
```

Output:

```text
['apple', 'Apple', 'Banana', 'cherry']
```

---

# 📌 Sorting with `key`

The `key` parameter tells Python **what value should be used for comparison**.

### Syntax

```python
list_name.sort(key=function)
```

---

# 📖 Example: Sort by String Length

```python
fruits = ["Apple", "Kiwi", "Watermelon", "Fig"]

fruits.sort(key=len)

print(fruits)
```

Output:

```text
['Fig', 'Kiwi', 'Apple', 'Watermelon']
```

Python sorts according to the **length** of each string.

---

# 📖 Sort by Length in Descending Order

```python
fruits = ["Apple", "Kiwi", "Watermelon", "Fig"]

fruits.sort(key=len, reverse=True)

print(fruits)
```

Output:

```text
['Watermelon', 'Apple', 'Kiwi', 'Fig']
```

---

# 📌 Method 2: `reverse()`

## 📖 What is `reverse()`?

The `reverse()` method reverses the **current order** of elements.

### Syntax

```python
list_name.reverse()
```

---

# 📖 Example 1

```python
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)
```

Output:

```text
[50, 40, 30, 20, 10]
```

---

# 📖 Example 2

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.reverse()

print(fruits)
```

Output:

```text
['Mango', 'Banana', 'Apple']
```

---

# ⚠️ Important Difference

`reverse()` does **not sort** the list.

Example:

```python
numbers = [30, 10, 40, 20]

numbers.reverse()

print(numbers)
```

Output:

```text
[20, 40, 10, 30]
```

It simply reverses the existing order.

It does **not** produce:

```text
[10, 20, 30, 40]
```

---

# 📌 Method 3: `sorted()`

## 📖 What is `sorted()`?

`sorted()` is a **built-in Python function**, not a list method.

It creates and returns a **new sorted list**.

### Syntax

```python
sorted(iterable)
```

---

# 📖 Example 1

```python
numbers = [50, 20, 40, 10, 30]

new_numbers = sorted(numbers)

print(new_numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

---

# 📖 Original List Remains Unchanged

```python
numbers = [50, 20, 40, 10, 30]

new_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", new_numbers)
```

Output:

```text
Original: [50, 20, 40, 10, 30]
Sorted: [10, 20, 30, 40, 50]
```

This is an important difference between `sort()` and `sorted()`.

---

# 🔥 `sort()` vs `sorted()`

| Feature | `sort()` | `sorted()` |
|---|---|---|
| Type | List method | Built-in function |
| Original list changed? | ✅ Yes | ❌ No |
| Returns sorted list? | ❌ Returns `None` | ✅ Yes |
| Works with lists | ✅ | ✅ |
| Works with tuples | ❌ | ✅ |
| Works with strings | ❌ | ✅ |
| Supports `reverse` | ✅ | ✅ |
| Supports `key` | ✅ | ✅ |

---

# ⚠️ Important: Why Does `sort()` Return `None`?

Consider:

```python
numbers = [30, 10, 20]

result = numbers.sort()

print(result)
```

Output:

```text
None
```

Why?

Because `sort()` changes the original list **in place**.

Correct:

```python
numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30]
```

---

# 📌 Sorting a Tuple with `sorted()`

```python
numbers = (30, 10, 20)

result = sorted(numbers)

print(result)
```

Output:

```text
[10, 20, 30]
```

Notice that `sorted()` returns a **list**, even though the original object was a tuple.

---

# 📌 Sorting a String with `sorted()`

```python
word = "python"

result = sorted(word)

print(result)
```

Output:

```text
['h', 'n', 'o', 'p', 't', 'y']
```

`sorted()` can work with many iterable objects.

---

# 📌 Reverse Sorting with `sorted()`

```python
numbers = [10, 40, 20, 30]

result = sorted(numbers, reverse=True)

print(result)
```

Output:

```text
[40, 30, 20, 10]
```

---

# 📊 `reverse()` vs `sort(reverse=True)`

These are **not the same**.

### `reverse()`

```python
numbers = [30, 10, 40, 20]

numbers.reverse()

print(numbers)
```

Output:

```text
[20, 40, 10, 30]
```

It reverses the current order.

---

### `sort(reverse=True)`

```python
numbers = [30, 10, 40, 20]

numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

It sorts the numbers and places them in descending order.

---

# 📌 Sorting a List of Tuples

Suppose:

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]
```

By default, Python sorts using the first element.

```python
students.sort()

print(students)
```

Output:

```text
[('Aisha', 85), ('Rohan', 78), ('Saniya', 92)]
```

---

# 📖 Sorting by Marks

Use a `key` function.

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]

students.sort(key=lambda student: student[1])

print(students)
```

Output:

```text
[('Rohan', 78), ('Aisha', 85), ('Saniya', 92)]
```

---

# 📖 Highest Marks First

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78)
]

students.sort(
    key=lambda student: student[1],
    reverse=True
)

print(students)
```

Output:

```text
[('Saniya', 92), ('Aisha', 85), ('Rohan', 78)]
```

---

# 🌍 Real-World Examples

## Student Marks

```python
marks = [78, 92, 85, 66, 95]

marks.sort()

print(marks)
```

---

## Ranking

```python
scores = [450, 720, 650, 890, 530]

scores.sort(reverse=True)

print(scores)
```

Output:

```text
[890, 720, 650, 530, 450]
```

---

## Product Prices

```python
prices = [999, 499, 1499, 799, 299]

prices.sort()

print(prices)
```

---

## Names Alphabetically

```python
names = ["Saniya", "Aisha", "Rohan", "Karan"]

names.sort()

print(names)
```

---

## Sort Products by Name Length

```python
products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Phone"
]

products.sort(key=len)

print(products)
```

---

# 📊 Complete Comparison

| Operation | Purpose | Changes Original? | Returns |
|---|---|---:|---|
| `sort()` | Sort list | ✅ | `None` |
| `sort(reverse=True)` | Descending sort | ✅ | `None` |
| `reverse()` | Reverse current order | ✅ | `None` |
| `sorted()` | Create sorted version | ❌ | New list |
| `sorted(reverse=True)` | Create descending version | ❌ | New list |

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Assigning `sort()` to a Variable

```python
numbers = [30, 10, 20]

numbers = numbers.sort()

print(numbers)
```

Output:

```text
None
```

Correct:

```python
numbers = [30, 10, 20]

numbers.sort()

print(numbers)
```

---

## ❌ Mistake 2: Thinking `reverse()` Sorts

```python
numbers = [30, 10, 40, 20]

numbers.reverse()

print(numbers)
```

Output:

```text
[20, 40, 10, 30]
```

`reverse()` only reverses the existing order.

---

## ❌ Mistake 3: Expecting `sorted()` to Modify the Original List

```python
numbers = [30, 10, 20]

sorted(numbers)

print(numbers)
```

Output:

```text
[30, 10, 20]
```

The result was created but not stored.

Correct:

```python
numbers = [30, 10, 20]

numbers = sorted(numbers)

print(numbers)
```

---

# 💡 Best Practices

- Use `sort()` when you want to modify the original list.
- Use `sorted()` when you want to keep the original list unchanged.
- Use `reverse()` when you simply want to reverse the current order.
- Use `key` when sorting according to a specific property.
- Use `reverse=True` for descending sorting.

---

# 🚀 Pro Tips

A very useful pattern is:

```python
list_name.sort(key=some_function)
```

For example:

```python
names = ["Alexander", "Bob", "Christopher"]

names.sort(key=len)

print(names)
```

Output:

```text
['Bob', 'Alexander', 'Christopher']
```

Python calculates the length of each name and sorts according to that value.

---

# ❓ Interview Questions

- [ ] What is the difference between `sort()` and `sorted()`?
- [ ] Does `sort()` return a new list?
- [ ] Why does `sort()` return `None`?
- [ ] What does `reverse()` do?
- [ ] What is the difference between `reverse()` and `sort(reverse=True)`?
- [ ] What is the purpose of the `key` parameter?
- [ ] Can `sorted()` work with tuples?
- [ ] Can `sorted()` work with strings?

---

# 🏋️ Practice Programs

## Easy

```python
numbers = [50, 20, 40, 10, 30]

numbers.sort()

print(numbers)
```

---

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

---

```python
numbers = [30, 10, 20]

result = sorted(numbers)

print(result)
```

---

## Medium

```python
numbers = [10, 50, 20, 40, 30]

numbers.sort(reverse=True)

print(numbers)
```

---

```python
names = ["Saniya", "Aisha", "Rohan", "Karan"]

names.sort(key=len)

print(names)
```

---

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers, reverse=True)

print(result)
```

---

## Advanced

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78),
    ("Karan", 95)
]

students.sort(key=lambda student: student[1])

print(students)
```

---

```python
students = [
    ("Aisha", 85),
    ("Saniya", 92),
    ("Rohan", 78),
    ("Karan", 95)
]

students.sort(
    key=lambda student: student[1],
    reverse=True
)

print(students)
```

---

# 🎯 Challenge

Write programs to:

1. Sort a list of numbers in ascending order.
2. Sort the same list in descending order.
3. Reverse a list without sorting it.
4. Sort a list of names alphabetically.
5. Sort names according to their length.
6. Sort student records according to their marks.
7. Create a sorted copy while keeping the original list unchanged.

---

# 📝 Assignment

- [x] Demonstrate `sort()`.
- [x] Demonstrate `sort(reverse=True)`.
- [x] Demonstrate `reverse()`.
- [x] Demonstrate `sorted()`.
- [x] Demonstrate `sorted(reverse=True)`.
- [x] Use `key=len`.
- [x] Sort a list of tuples using `lambda`.
- [x] Explain the difference between `sort()` and `sorted()` in your own words.

---

# 📚 Summary

You learned three important sorting/reversing operations.

### `sort()`

```python
numbers.sort()
```

➡️ Sorts the **original list**.

### `reverse()`

```python
numbers.reverse()
```

➡️ Reverses the **current order**.

### `sorted()`

```python
new_numbers = sorted(numbers)
```

➡️ Creates a **new sorted list**.

---

# 🧠 Easy Way to Remember

```text
sort()
   ↓
Sort the original list

reverse()
   ↓
Reverse the original list

sorted()
   ↓
Create a sorted copy
```

And:

```python
reverse=True
```

means:

```text
Highest → Lowest
Z → A
Descending order
```

---

# 🎯 Topic Completion Checklist

- [x] I understand `sort()`.
- [x] I understand `reverse()`.
- [x] I understand `sorted()`.
- [x] I know ascending and descending order.
- [x] I understand `key`.
- [x] I understand `reverse=True`.
- [x] I know the difference between `sort()` and `sorted()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 4 (Part 5): Copying Lists**

- `copy()`
- Assignment (`=`)
- Shallow Copy
- Deep Copy