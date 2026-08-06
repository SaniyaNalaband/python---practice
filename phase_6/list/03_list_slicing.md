# 🐍 Python Master Course

> **Phase 6:** Collections – Lists  
> **Topic 3:** List Slicing

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what list slicing is.
- [ ] Learn the syntax of list slicing.
- [ ] Slice lists using `start`, `stop`, and `step`.
- [ ] Use positive and negative indexes in slicing.
- [ ] Reverse a list using slicing.
- [ ] Solve real-world problems using list slicing.

---

# 📖 What is List Slicing?

**List slicing** is the process of extracting a **portion (part)** of a list.

Instead of accessing one element like indexing, slicing returns **multiple elements** as a **new list**.

---

# 🤔 Why Do We Need List Slicing?

Suppose you have a list of 100 students, but you only want the first 10 students.

Instead of creating another list manually, you can use slicing.

---

# 📖 Syntax

```python
list_name[start : stop : step]
```

| Parameter | Description |
|-----------|-------------|
| `start` | Starting index (included) |
| `stop` | Ending index (excluded) |
| `step` | Number of positions to move |

---

# ⭐ Important Rule

- ✅ `start` is **included**
- ❌ `stop` is **not included**

---

# 📖 Example List

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"]
```

```text
Index →      0        1        2        3         4          5

           ┌────────┬────────┬────────┬────────┬──────────┬────────────┐
fruits =   │ Apple  │ Banana │ Mango  │ Orange │ Grapes   │ Pineapple  │
           └────────┴────────┴────────┴────────┴──────────┴────────────┘

Negative →  -6      -5       -4       -3        -2         -1
```

---

# 📖 Slice from Start to Stop

```python
print(fruits[1:4])
```

Output

```text
['Banana', 'Mango', 'Orange']
```

Explanation

```text
Start = 1 ✅ Included

Stop = 4 ❌ Not Included
```

---

# 📖 Slice from Beginning

If `start` is omitted, Python starts from index `0`.

```python
print(fruits[:3])
```

Output

```text
['Apple', 'Banana', 'Mango']
```

Equivalent to:

```python
print(fruits[0:3])
```

---

# 📖 Slice to the End

If `stop` is omitted, Python goes until the last element.

```python
print(fruits[2:])
```

Output

```text
['Mango', 'Orange', 'Grapes', 'Pineapple']
```

---

# 📖 Copy the Entire List

```python
copy_list = fruits[:]

print(copy_list)
```

Output

```text
['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Pineapple']
```

---

# 📖 Using the `step` Parameter

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[::2])
```

Output

```text
[1, 3, 5, 7, 9]
```

Every second element is selected.

---

# 📖 Every Third Element

```python
numbers = list(range(1,16))

print(numbers[::3])
```

Output

```text
[1, 4, 7, 10, 13]
```

---

# 📖 Reverse a List

Use a negative step.

```python
numbers = [10,20,30,40,50]

print(numbers[::-1])
```

Output

```text
[50, 40, 30, 20, 10]
```

---

# 📖 Reverse Every Second Element

```python
numbers = [1,2,3,4,5,6,7,8]

print(numbers[::-2])
```

Output

```text
[8, 6, 4, 2]
```

---

# 📖 Negative Index Slicing

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits[-4:-1])
```

Output

```text
['Banana', 'Mango', 'Orange']
```

---

# 📖 Mixed Positive and Negative Indexes

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits[1:-1])
```

Output

```text
['Banana', 'Mango', 'Orange']
```

---

# 📖 Empty Slice

```python
numbers = [10,20,30]

print(numbers[2:1])
```

Output

```text
[]
```

Why?

The start index comes after the stop index, so there are no elements to return.

---

# 📖 Slice with Negative Step

```python
numbers = [1,2,3,4,5,6]

print(numbers[5:1:-1])
```

Output

```text
[6, 5, 4, 3]
```

Explanation

```text
Start = Index 5 (6)

Move Backwards

Stop before Index 1
```

---

# 📊 Trace Table

Program

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

| Start | Stop | Result |
|-------:|-----:|--------|
| 1 | 4 | `[20, 30, 40]` |

---

# 🌍 Real-World Examples

## First Five Students

```python
students = [
    "Rahul",
    "Aisha",
    "Saniya",
    "Rohan",
    "Karan",
    "Neha"
]

print(students[:5])
```

---

## Last Three Transactions

```python
transactions = [1200, 500, 900, 1500, 700, 300]

print(transactions[-3:])
```

Output

```text
[1500, 700, 300]
```

---

## Every Alternate Day

```python
days = [
    "Mon","Tue","Wed",
    "Thu","Fri","Sat","Sun"
]
print(days[::2])
```

Output

```text
['Mon', 'Wed', 'Fri', 'Sun']
```

---

## Reverse Leaderboard

```python
scores = [100,95,90,85,80]

print(scores[::-1])
```

Output

```text
[80, 85, 90, 95, 100]
```

---

# ⚠️ Common Mistakes

## ❌ Expecting `stop` to Be Included

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])
```

Output

```text
[20, 30, 40]
```

The element at index `4` (`50`) is **not included**.

---

## ❌ Confusing Indexing with Slicing

```python
numbers = [10,20,30]

print(numbers[1])
```

Output

```text
20
```

Returns a **single value**.

```python
print(numbers[1:2])
```

Output

```text
[20]
```

Returns a **list**.

---

## ❌ Wrong Step Direction

```python
numbers = [1,2,3,4]

print(numbers[1:4:-1])
```

Output

```text
[]
```

A negative step requires the start index to be greater than the stop index.

---

# 💡 Best Practices

- Remember: `start` is included, `stop` is excluded.
- Use `[:]` to create a shallow copy of a list.
- Use `[::-1]` to reverse a list quickly.
- Use slicing instead of loops when extracting parts of a list.

---

# 🚀 Pro Tips

List slicing is commonly used in:

- Data analysis
- Machine learning
- Web development
- Image processing
- Pagination
- Data filtering
- Report generation

---

# ❓ Interview Questions

- [ ] What is list slicing?
- [ ] What is the syntax of list slicing?
- [ ] Is the `stop` index included?
- [ ] How do you reverse a list using slicing?
- [ ] What does `list[:]` do?

---

# 🏋️ Practice Programs

## Easy

```python
numbers = [10,20,30,40,50]

print(numbers[:3])
```

---

```python
fruits = ["Apple","Banana","Mango","Orange"]

print(fruits[1:3])
```

---

## Medium

```python
numbers = list(range(1,11))

print(numbers[::2])
```

---

```python
colors = [
    "Red","Blue","Green",
    "Yellow","Black"
]

print(colors[-3:])
```

---

## Advanced

```python
numbers = list(range(1,21))

print(numbers[5:15:2])
```

---

```python
matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(matrix[:2])
```

---

# 🎯 Challenge

Write programs to:

1. Print the first five elements of a list.
2. Print the last four elements.
3. Print every third element.
4. Reverse a list using slicing.
5. Print elements from index `2` to `8` with a step of `2`.

---

# 📝 Assignment

- [x] Create a list of 10 numbers and print the first 5.
- [x] Print the last 3 elements using negative slicing.
- [x] Print every alternate element.
- [x] Reverse a list using `[::-1]`.
- [x] Create a copy of a list using slicing.
- [x] Print every fourth element from a list.
- [x] Slice a list using both positive and negative indexes.

---

# 📚 Summary

You learned:

- ✅ What list slicing is.
- ✅ The syntax `list[start:stop:step]`.
- ✅ Positive and negative slicing.
- ✅ Using the `step` parameter.
- ✅ Reversing a list using slicing.
- ✅ Common mistakes and best practices.

### Key Points to Remember

- `start` is **included**.
- `stop` is **excluded**.
- Omitting `start` begins from index `0`.
- Omitting `stop` goes to the end of the list.
- `[::-1]` reverses a list.
- Slicing returns a **new list**.

---

# 🎯 Topic Completion Checklist

- [x] I understand list slicing.
- [x] I can use `start`, `stop`, and `step`.
- [x] I can use positive and negative slicing.
- [x] I can reverse a list using slicing.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 6 – Topic 4: List Methods**