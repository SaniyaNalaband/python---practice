# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 2:** List Indexing

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what list indexing is.
- [ ] Access list elements using positive indexing.
- [ ] Access list elements using negative indexing.
- [ ] Modify list elements using indexes.
- [ ] Understand common indexing errors.
- [ ] Solve real-world problems using indexing.

---

# 📖 What is List Indexing?

**List indexing** is the process of accessing individual elements in a list using their **position (index number)**.

Every element in a list has an index.

Python supports:

- ✅ Positive Indexing
- ✅ Negative Indexing

---

# 📖 Example List

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
```

---

# 📍 Positive Indexing

Positive indexing starts from **0**.

```text
            0         1         2         3          4
         ┌────────┬────────┬────────┬────────┬─────────┐
fruits = │ Apple  │ Banana │ Mango  │ Orange │ Grapes │
         └────────┴────────┴────────┴────────┴─────────┘
```

---

# 📍 Negative Indexing

Negative indexing starts from **-1** (last element).

```text
           -5       -4       -3       -2        -1
         ┌────────┬────────┬────────┬────────┬─────────┐
fruits = │ Apple  │ Banana │ Mango  │ Orange │ Grapes │
         └────────┴────────┴────────┴────────┴─────────┘
```

---

# 📖 Accessing Elements (Positive Index)

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
```

Output

```text
Apple
```

---

```python
print(fruits[2])
```

Output

```text
Mango
```

---

```python
print(fruits[3])
```

Output

```text
Orange
```

---

# 📖 Accessing Elements (Negative Index)

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[-1])
```

Output

```text
Orange
```

---

```python
print(fruits[-2])
```

Output

```text
Mango
```

---

```python
print(fruits[-4])
```

Output

```text
Apple
```

---

# 📖 Using Variables as Indexes

```python
numbers = [10, 20, 30, 40, 50]

index = 3

print(numbers[index])
```

Output

```text
40
```

---

# 📖 Modifying Elements Using Indexes

Lists are **mutable**, so elements can be changed.

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)
```

Output

```text
['Apple', 'Orange', 'Mango']
```

---

# 📖 Modifying the Last Element

```python
numbers = [10, 20, 30, 40]

numbers[-1] = 100

print(numbers)
```

Output

```text
[10, 20, 30, 100]
```

---

# 📖 Accessing Nested List Elements

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(matrix[1][2])
```

Output

```text
60
```

### Explanation

```text
matrix[1]
↓

[40, 50, 60]

matrix[1][2]

↓

60
```

---

# 📖 Using `len()` with Indexing

```python
colors = ["Red", "Green", "Blue"]

last_item = colors[len(colors) - 1]

print(last_item)
```

Output

```text
Blue
```

---

# 📊 Trace Table

Program

```python
animals = ["Dog", "Cat", "Lion"]

print(animals[0])
print(animals[-1])
```

| Statement | Output |
|-----------|--------|
| `animals[0]` | `Dog` |
| `animals[-1]` | `Lion` |

---

# 🌍 Real-World Examples

## Student Marks

```python
marks = [85, 90, 78, 95]

print("First Student:", marks[0])
print("Last Student:", marks[-1])
```

---

## Shopping Cart

```python
cart = ["Milk", "Bread", "Eggs"]

print(cart[1])
```

Output

```text
Bread
```

---

## Employee List

```python
employees = [
    "Rahul",
    "Aisha",
    "Saniya",
    "Rohan"
]

print(employees[2])
```

Output

```text
Saniya
```

---

## Matrix Data

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])
```

Output

```text
2
```

---

# ⚠️ Common Mistakes

## ❌ Index Out of Range

Incorrect

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Output

```text
IndexError: list index out of range
```

The list has only **3 elements** (indexes `0`, `1`, and `2`).

---

## ❌ Forgetting Index Starts at `0`

Incorrect

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[1])
```

Expected (incorrectly)

```text
Apple
```

Actual Output

```text
Banana
```

Remember:

```text
0 → Apple
1 → Banana
2 → Mango
```

---

## ❌ Using Parentheses Instead of Square Brackets

Incorrect

```python
numbers = [10, 20, 30]

print(numbers(1))
```

Output

```text
TypeError: 'list' object is not callable
```

Correct

```python
print(numbers[1])
```

---

# 💡 Best Practices

- Remember that indexing starts at `0`.
- Use negative indexing when working with the last elements.
- Check the list length before accessing indexes.
- Use meaningful variable names like `first_student` or `last_item`.

---

# 🚀 Pro Tips

List indexing is commonly used in:

- Data analysis
- Game development
- Student management systems
- Shopping cart applications
- Matrix operations
- Machine learning

---

# ❓ Interview Questions

- [x] What is list indexing?
- [x] What is the difference between positive and negative indexing?
- [x] What happens if you access an invalid index?
- [x] Can list elements be modified using indexes?
- [x] How do you access an element in a nested list?

---

# 🏋️ Practice Programs

## Easy

```python
colors = ["Red", "Green", "Blue"]

print(colors[0])
print(colors[-1])
```

---

```python
numbers = [10, 20, 30, 40]

print(numbers[2])
```

---

## Medium

```python
students = ["Rahul", "Aisha", "Saniya"]

students[1] = "Rohan"

print(students)
```

---

```python
marks = [85, 90, 78, 95]

print("First:", marks[0])
print("Last:", marks[-1])
```

---

## Advanced

```python
matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(matrix[2][1])
```

---

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

products[-2] = "Printer"

print(products)
```

---

# 🎯 Challenge

Write programs to:

1. Print the first and last element of a list.
2. Replace the second element with a new value.
3. Print the middle element of a list containing five elements.
4. Access and print an element from a nested list.

---

# 📝 Assignment

- [x] Create a list of five cities and print the first city.
- [x] Create a list of five numbers and print the last number.
- [x] Change the third element of a list.
- [x] Access an element from a nested list.
- [x] Use both positive and negative indexing in the same program.

---

# 📚 Summary

You learned:

- ✅ What list indexing is.
- ✅ Positive indexing.
- ✅ Negative indexing.
- ✅ Modifying list elements.
- ✅ Accessing nested list elements.
- ✅ Common mistakes and best practices.

### Key Points to Remember

- Indexing starts at **0**.
- The first element has index `0`.
- The last element has index `-1`.
- Lists are **mutable**, so elements can be changed using indexes.
- Access nested lists using multiple indexes (e.g., `matrix[1][2]`).

---

# 🎯 Topic Completion Checklist

- [x] I understand list indexing.
- [x] I can use positive indexing.
- [x] I can use negative indexing.
- [x] I can modify list elements using indexes.
- [x] I can access elements in nested lists.
- [x] I completed the practice programs.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 3: List Slicing**