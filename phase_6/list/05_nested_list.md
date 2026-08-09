# 🐍 Python Master Course

# 📦 Phase 6: Collections – Lists

## 📌 Topic 5: Nested Lists

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand what a nested list is.
- [ ] Create nested lists.
- [ ] Access elements from nested lists.
- [ ] Use multiple indexes.
- [ ] Modify nested list elements.
- [ ] Add elements to inner lists.
- [ ] Remove elements from inner lists.
- [ ] Use slicing with nested lists.
- [ ] Traverse nested lists using loops.
- [ ] Work with nested lists in real-world applications.

---

# 📖 What is a Nested List?

A **nested list** is a list that contains another list as one or more of its elements.

In simple words:

> A list inside another list is called a **nested list**.

### Example

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers)
```

Output:

```text
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Here:

```text
numbers
   ↓
┌───────────────────────┐
│ [1, 2, 3]             │
│ [4, 5, 6]             │
│ [7, 8, 9]             │
└───────────────────────┘
```

Each inner list is an element of the outer list.

---

# 📌 Basic Structure

Consider:

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]
```

The structure is:

```text
Outer List
│
├── Inner List 0 → [10, 20, 30]
│
└── Inner List 1 → [40, 50, 60]
```

The outer list contains **2 lists**.

Each inner list contains **3 elements**.

---

# 📌 Creating a Nested List

## Example 1

```python
numbers = [[1, 2], [3, 4]]

print(numbers)
```

Output:

```text
[[1, 2], [3, 4]]
```

---

## Example 2

```python
colors = [
    ["Red", "Green"],
    ["Blue", "Yellow"]
]

print(colors)
```

Output:

```text
[['Red', 'Green'], ['Blue', 'Yellow']]
```

---

## Example 3

A nested list can contain different data types.

```python
student = [
    ["Saniya", 21],
    ["Rohan", 22],
    ["Aisha", 20]
]

print(student)
```

Output:

```text
[['Saniya', 21], ['Rohan', 22], ['Aisha', 20]]
```

---

# 📌 Nested List Indexing

Nested lists use **multiple indexes** to access elements.

Consider:

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

The outer indexes are:

```text
             0              1              2
             ↓              ↓              ↓
numbers = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
```

---

# 📖 Accessing the First Inner List

```python
print(numbers[0])
```

Output:

```text
[10, 20, 30]
```

---

# 📖 Accessing the Second Inner List

```python
print(numbers[1])
```

Output:

```text
[40, 50, 60]
```

---

# 📖 Accessing an Individual Element

To access an individual element:

```python
list[outer_index][inner_index]
```

Example:

```python
print(numbers[0][1])
```

Output:

```text
20
```

Explanation:

```text
numbers[0]
       ↓
[10, 20, 30]

numbers[0][1]
          ↓
         20
```

---

# 📊 Nested List Index Table

For:

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

| Expression | Result |
|---|---:|
| `numbers[0][0]` | `10` |
| `numbers[0][1]` | `20` |
| `numbers[0][2]` | `30` |
| `numbers[1][0]` | `40` |
| `numbers[1][1]` | `50` |
| `numbers[1][2]` | `60` |
| `numbers[2][0]` | `70` |
| `numbers[2][1]` | `80` |
| `numbers[2][2]` | `90` |

---

# 📌 Negative Indexing

Nested lists also support negative indexing.

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

print(numbers[-1])
```

Output:

```text
[40, 50, 60]
```

The last inner list is accessed using `-1`.

---

## Accessing the Last Element

```python
print(numbers[-1][-1])
```

Output:

```text
60
```

Explanation:

```text
numbers[-1]       → [40, 50, 60]

numbers[-1][-1]   → 60
```

---

# 📌 Modifying Nested List Elements

Nested lists are mutable.

You can change individual elements.

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

numbers[0][1] = 200

print(numbers)
```

Output:

```text
[[10, 200, 30], [40, 50, 60]]
```

---

# 📖 Another Example

```python
students = [
    ["Aisha", 85],
    ["Saniya", 92],
    ["Rohan", 78]
]

students[2][1] = 88

print(students)
```

Output:

```text
[['Aisha', 85], ['Saniya', 92], ['Rohan', 88]]
```

Rohan's marks changed from `78` to `88`.

---

# 📌 Adding Elements to an Inner List

You can use list methods on inner lists.

```python
numbers = [
    [10, 20],
    [30, 40]
]

numbers[0].append(50)

print(numbers)
```

Output:

```text
[[10, 20, 50], [30, 40]]
```

---

# 📌 Adding a New Inner List

You can also add an entirely new list.

```python
numbers = [
    [10, 20],
    [30, 40]
]

numbers.append([50, 60])

print(numbers)
```

Output:

```text
[[10, 20], [30, 40], [50, 60]]
```

---

# 📌 Difference Between Adding an Element and Adding a List

### Adding an element to an inner list

```python
numbers[0].append(30)
```

Result:

```text
[[10, 20, 30], [40, 50]]
```

### Adding a new inner list

```python
numbers.append([60, 70])
```

Result:

```text
[[10, 20], [40, 50], [60, 70]]
```

---

# 📌 Removing Elements from an Inner List

You can use `remove()`.

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

numbers[0].remove(20)

print(numbers)
```

Output:

```text
[[10, 30], [40, 50, 60]]
```

---

# 📌 Using `pop()` on an Inner List

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

numbers[1].pop()

print(numbers)
```

Output:

```text
[[10, 20, 30], [40, 50]]
```

The last element `60` was removed.

---

# 📌 Nested List Slicing

You can also use slicing.

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(numbers[0][1:])
```

Output:

```text
[20, 30]
```

---

# 📖 Slicing the Outer List

```python
numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(numbers[1:])
```

Output:

```text
[[30, 40], [50, 60]]
```

---

# 📌 Traversing a Nested List

To access every element, we commonly use **nested loops**.

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for value in row:
        print(value)
```

Output:

```text
1
2
3
4
5
6
7
8
9
```

---

# 🧠 Understanding the Nested Loop

```python
for row in numbers:
```

The outer loop gets each inner list.

First iteration:

```text
row = [1, 2, 3]
```

Second iteration:

```text
row = [4, 5, 6]
```

Third iteration:

```text
row = [7, 8, 9]
```

Then:

```python
for value in row:
```

gets each individual element.

---

# 📌 Printing a Nested List Like a Table

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    print(row)
```

Output:

```text
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

---

# 📌 Printing Without Brackets

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for value in row:
        print(value, end=" ")
    print()
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

This is a simple way to display a matrix-like structure.

---

# 🌍 Real-World Example 1: Student Records

```python
students = [
    ["Aisha", 85, 90],
    ["Saniya", 92, 88],
    ["Rohan", 78, 82]
]

print(students[0][0])
print(students[1][1])
print(students[2][2])
```

Output:

```text
Aisha
92
82
```

---

# 🌍 Real-World Example 2: Product Information

```python
products = [
    ["Laptop", 50000],
    ["Mouse", 1000],
    ["Keyboard", 2000]
]

print(products[0][0])
print(products[0][1])
```

Output:

```text
Laptop
50000
```

---

# 🌍 Real-World Example 3: Monthly Sales

```python
sales = [
    [10000, 12000, 15000],
    [9000, 11000, 14000],
    [13000, 15000, 18000]
]

print(sales[0][1])
```

Output:

```text
12000
```

Here:

```text
sales[0] → First month's data

sales[0][1] → Second value from that month
```

---

# 🌍 Real-World Example 4: Classroom Seating

```python
seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

print(seats[1][2])
```

Output:

```text
B3
```

---

# 📌 Nested Lists with `len()`

You can use `len()` on both the outer list and inner lists.

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

print(len(numbers))
print(len(numbers[0]))
```

Output:

```text
2
3
```

Explanation:

```text
len(numbers)
→ 2 inner lists

len(numbers[0])
→ 3 elements in the first inner list
```

---

# 📌 Finding the Total Number of Elements

Suppose:

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
```

You can calculate the total number of elements:

```python
total = 0

for row in numbers:
    total += len(row)

print(total)
```

Output:

```text
6
```

---

# 📌 Nested Lists with Conditions

```python
marks = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]

for student in marks:
    for mark in student:
        if mark >= 90:
            print(mark)
```

Output:

```text
90
92
95
```

---

# 📌 Finding the Sum of Each Inner List

```python
marks = [
    [80, 90, 70],
    [85, 75, 95],
    [90, 88, 92]
]

for student in marks:
    print(sum(student))
```

Output:

```text
240
255
270
```

---

# 📌 Finding the Highest Value in Each Inner List

```python
marks = [
    [80, 90, 70],
    [85, 75, 95],
    [90, 88, 92]
]

for student in marks:
    print(max(student))
```

Output:

```text
90
95
92
```

---

# 📌 Nested Lists Can Have Different Lengths

Nested lists do not necessarily need to have the same number of elements.

```python
numbers = [
    [1, 2],
    [3, 4, 5],
    [6]
]

print(numbers)
```

Output:

```text
[[1, 2], [3, 4, 5], [6]]
```

This is perfectly valid Python.

---

# 📌 Traversing Unequal Nested Lists

```python
numbers = [
    [1, 2],
    [3, 4, 5],
    [6]
]

for row in numbers:
    for value in row:
        print(value)
```

Output:

```text
1
2
3
4
5
6
```

---

# ⚠️ Common Mistakes

## ❌ Mistake 1: Using Only One Index

```python
numbers = [
    [10, 20],
    [30, 40]
]

print(numbers[0])
```

Output:

```text
[10, 20]
```

This accesses the **inner list**, not an individual element.

To get `20`:

```python
print(numbers[0][1])
```

---

## ❌ Mistake 2: Incorrect Index

```python
numbers = [
    [10, 20],
    [30, 40]
]

print(numbers[2])
```

This causes:

```text
IndexError
```

The outer list only has indexes:

```text
0
1
```

---

## ❌ Mistake 3: Incorrect Inner Index

```python
numbers = [
    [10, 20],
    [30, 40]
]

print(numbers[0][2])
```

This also causes:

```text
IndexError
```

The first inner list contains only:

```text
[10, 20]
```

Its indexes are:

```text
0  1
```

---

# 🧠 Important Concept

For:

```python
data = [
    ["A", "B", "C"],
    ["D", "E", "F"]
]
```

Remember:

```text
data[row][column]
```

So:

```python
data[0][0]
```

means:

```text
row 0
column 0
```

Result:

```text
A
```

And:

```python
data[1][2]
```

means:

```text
row 1
column 2
```

Result:

```text
F
```

---

# 📊 Nested List Index Diagram

```text
                    COLUMN
               0       1       2
            ┌───────┬───────┬───────┐
ROW 0       │   1   │   2   │   3   │
            ├───────┼───────┼───────┤
ROW 1       │   4   │   5   │   6   │
            ├───────┼───────┼───────┤
ROW 2       │   7   │   8   │   9   │
            └───────┴───────┴───────┘
```

Therefore:

```python
numbers[2][1]
```

returns:

```text
8
```

---

# 🔥 Advanced Example: Find the Largest Number

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

largest = numbers[0][0]

for row in numbers:
    for value in row:
        if value > largest:
            largest = value

print("Largest:", largest)
```

Output:

```text
Largest: 90
```

---

# 🔥 Advanced Example: Calculate Total

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

total = 0

for row in numbers:
    for value in row:
        total += value

print("Total:", total)
```

Output:

```text
Total: 210
```

---

# 🔥 Advanced Example: Count Even Numbers

```python
numbers = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

count = 0

for row in numbers:
    for value in row:
        if value % 2 == 0:
            count += 1

print("Even Numbers:", count)
```

Output:

```text
Even Numbers: 5
```

---

# 🎯 Practice Programs

## Beginner

### 1. Create a nested list

```python
numbers = [
    [1, 2],
    [3, 4]
]

print(numbers)
```

---

### 2. Access an element

```python
numbers = [
    [10, 20],
    [30, 40]
]

print(numbers[1][0])
```

---

### 3. Modify an element

```python
numbers = [
    [10, 20],
    [30, 40]
]

numbers[0][1] = 200

print(numbers)
```

---

## Intermediate

### 4. Add to an inner list

```python
numbers = [
    [10, 20],
    [30, 40]
]

numbers[1].append(50)

print(numbers)
```

---

### 5. Remove from an inner list

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60]
]

numbers[0].remove(20)

print(numbers)
```

---

### 6. Print all elements

```python
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in numbers:
    for value in row:
        print(value)
```

---

# 🚀 Advanced Practice

### 7. Find the total

```python
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

total = 0

for row in numbers:
    for value in row:
        total += value

print(total)
```

---

### 8. Find the largest number

```python
numbers = [
    [15, 20, 35],
    [40, 12, 60],
    [25, 80, 10]
]

largest = numbers[0][0]

for row in numbers:
    for value in row:
        if value > largest:
            largest = value

print("Largest:", largest)
```

---

### 9. Count numbers greater than 50

```python
numbers = [
    [20, 60, 30],
    [80, 40, 90],
    [15, 70, 25]
]

count = 0

for row in numbers:
    for value in row:
        if value > 50:
            count += 1

print("Count:", count)
```

---

# 🏆 Challenge

Create a student marks system:

```python
students = [
    ["Aisha", 80, 85, 90],
    ["Saniya", 90, 95, 88],
    ["Rohan", 75, 82, 79]
]
```

Write a program that:

1. [x] Prints each student's name.
2. [x] Prints each student's marks.
3. [x] Calculates each student's total.
4. [x] Calculates each student's average.
5. [x] Finds the highest mark.
6. [x] Finds the student with the highest average.

---

# ❓ Interview Questions

- [x] What is a nested list?
- [x] How do you create a nested list?
- [x] How do you access an element inside a nested list?
- [x] What does `list[0][1]` mean?
- [x] Can nested lists have different lengths?
- [x] How do you modify an element inside a nested list?
- [x] How do you add an element to an inner list?
- [x] How do you traverse a nested list?
- [x] Why are nested loops commonly used with nested lists?

---

# 🧠 Quick Revision

### Create

```python
numbers = [[1, 2], [3, 4]]
```

### Access

```python
numbers[0][1]
```

### Modify

```python
numbers[0][1] = 100
```

### Add

```python
numbers[0].append(5)
```

### Remove

```python
numbers[0].remove(2)
```

### Traverse

```python
for row in numbers:
    for value in row:
        print(value)
```

---

# 📚 Key Points to Remember

```text
Nested List
     ↓
List inside another list
     ↓
list[row][column]
     ↓
Use multiple indexes
     ↓
Nested loops can traverse it
```

For example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

```python
matrix[0][2]
```

means:

```text
First inner list
       ↓
[1, 2, 3]
       ↓
Third element
       ↓
3
```

---

# 🎯 Topic Completion Checklist

- [x] I understand nested lists.
- [x] I can create nested lists.
- [x] I can access nested elements.
- [x] I understand two-dimensional indexing.
- [x] I can modify nested elements.
- [x] I can add elements to inner lists.
- [x] I can remove elements from inner lists.
- [x] I can use slicing with nested lists.
- [x] I can traverse nested lists using loops.
- [x] I completed the practice programs.
- [x] I completed the challenge.

---

# 📚 Next Topic

➡️ **Phase 6 – Topic 6: Copying Lists**

Topics:

- Assignment using `=`
- `copy()` method
- Slicing copy
- Shallow Copy
- Deep Copy