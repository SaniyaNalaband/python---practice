# 🐍 Python Master Course

# 📦 Phase 6: Collections – Sets

## 📌 Topic 2: Set Operations

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this topic, you will be able to:

- [ ] Understand what set operations are.
- [ ] Perform Union.
- [ ] Perform Intersection.
- [ ] Perform Difference.
- [ ] Perform Symmetric Difference.
- [ ] Use set operators.
- [ ] Use set methods.
- [ ] Understand the difference between `union()` and `|`.
- [ ] Understand the difference between `intersection()` and `&`.
- [ ] Understand the difference between `difference()` and `-`.
- [ ] Understand the difference between `symmetric_difference()` and `^`.
- [ ] Perform operations on multiple sets.
- [ ] Use set operations in real-world problems.

---

# 📖 What are Set Operations?

Set operations are operations used to compare and combine two or more sets.

Python provides four major set operations:

1. **Union**
2. **Intersection**
3. **Difference**
4. **Symmetric Difference**

Example:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

We can perform different operations between `A` and `B`.

---

# 📌 1. Union

The **union** of two sets contains **all unique elements** from both sets.

### Operator

```python
|
```

### Method

```python
union()
```

---

## Example

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A | B

print(result)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

The duplicate values `3` and `4` appear only once.

---

# 📌 Union Using `union()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.union(B)

print(result)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

---

# 🧠 Union Diagram

```text
        A                  B
    ┌────────┐         ┌────────┐
    │ 1  2   │         │   5  6 │
    │   3 4  ├─────────┤ 3  4   │
    └────────┘         └────────┘

             UNION
              ↓

       {1, 2, 3, 4, 5, 6}
```

---

# 📌 Union with Multiple Sets

```python
A = {1, 2}
B = {2, 3}
C = {3, 4}

result = A | B | C

print(result)
```

Output:

```text
{1, 2, 3, 4}
```

Using the method:

```python
result = A.union(B, C)

print(result)
```

---

# 🌍 Real-World Example: Students

Suppose:

```python
python_students = {"Aisha", "Saniya", "Rohan"}
java_students = {"Saniya", "Kiran", "Meera"}
```

Find all students studying either Python or Java:

```python
all_students = python_students | java_students

print(all_students)
```

Result:

```text
{'Aisha', 'Saniya', 'Rohan', 'Kiran', 'Meera'}
```

---

# 📌 2. Intersection

The **intersection** of two sets contains only the elements that are present in **both sets**.

### Operator

```python
&
```

### Method

```python
intersection()
```

---

## Example

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A & B

print(result)
```

Output:

```text
{3, 4}
```

Only `3` and `4` are common to both sets.

---

# 📌 Intersection Using `intersection()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.intersection(B)

print(result)
```

Output:

```text
{3, 4}
```

---

# 🧠 Intersection Diagram

```text
        A                  B
    ┌────────┐         ┌────────┐
    │ 1  2   │         │   5  6 │
    │    3 4 ├─────────┤ 3  4   │
    └────────┘         └────────┘
              ↑
          COMMON
          ELEMENTS

              ↓

             {3, 4}
```

---

# 🌍 Real-World Example: Common Skills

```python
python_skills = {"Python", "SQL", "Git", "HTML"}
web_skills = {"HTML", "CSS", "JavaScript", "Git"}

common = python_skills & web_skills

print(common)
```

Output:

```text
{'HTML', 'Git'}
```

---

# 📌 3. Difference

The **difference** between two sets contains elements that are present in the first set but **not in the second set**.

### Operator

```python
-
```

### Method

```python
difference()
```

---

## Example

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A - B

print(result)
```

Output:

```text
{1, 2}
```

`1` and `2` are in `A` but not in `B`.

---

# 📌 Difference in the Opposite Direction

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = B - A

print(result)
```

Output:

```text
{5, 6}
```

This is important:

```python
A - B
```

is not necessarily equal to:

```python
B - A
```

---

# 📌 Difference Using `difference()`

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.difference(B)

print(result)
```

Output:

```text
{1, 2}
```

---

# 🌍 Real-World Example

Students enrolled in Python:

```python
python_students = {"Aisha", "Saniya", "Rohan", "Kiran"}
```

Students enrolled in Java:

```python
java_students = {"Saniya", "Kiran"}
```

Find students who are studying Python but not Java:

```python
only_python = python_students - java_students

print(only_python)
```

Output:

```text
{'Aisha', 'Rohan'}
```

---

# 📌 4. Symmetric Difference

Symmetric difference contains elements that are in **either set, but not in both**.

In simple words:

> Keep elements that are unique to either set and remove common elements.

### Operator

```python
^
```

### Method

```python
symmetric_difference()
```

---

## Example

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A ^ B

print(result)
```

Output:

```text
{1, 2, 5, 6}
```

The common elements `3` and `4` are removed.

---

# 📌 Symmetric Difference Using Method

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.symmetric_difference(B)

print(result)
```

Output:

```text
{1, 2, 5, 6}
```

---

# 🧠 Symmetric Difference Diagram

```text
        A                  B
    ┌────────┐         ┌────────┐
    │ 1  2   │         │   5  6 │
    │    3 4 ├─────────┤ 3  4   │
    └────────┘         └────────┘
      ↑                     ↑
    UNIQUE                UNIQUE

              ↓

          {1, 2, 5, 6}
```

---

# 📊 Four Main Set Operations

Given:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

| Operation | Operator | Result |
|---|---|---|
| Union | `A \| B` | `{1, 2, 3, 4, 5, 6}` |
| Intersection | `A & B` | `{3, 4}` |
| Difference | `A - B` | `{1, 2}` |
| Symmetric Difference | `A ^ B` | `{1, 2, 5, 6}` |

---

# 📌 Union vs Intersection

### Union

```python
A | B
```

Means:

> Everything from A and B.

### Intersection

```python
A & B
```

Means:

> Only what A and B have in common.

---

# 📌 Difference vs Symmetric Difference

### Difference

```python
A - B
```

Keeps:

```text
A only
```

### Symmetric Difference

```python
A ^ B
```

Keeps:

```text
A only + B only
```

It removes the common elements.

---

# 📌 Set Operations Are Non-Destructive

Most set operation expressions create a new set rather than changing the original sets.

Example:

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A | B

print(A)
print(B)
print(result)
```

Output:

```text
{1, 2, 3}
{3, 4, 5}
{1, 2, 3, 4, 5}
```

The original sets remain unchanged.

---

# 📌 Update Versions of Set Operations

Python also provides methods that modify the original set.

These include:

```python
update()
intersection_update()
difference_update()
symmetric_difference_update()
```

---

# 📌 `update()`

`update()` adds elements from another iterable to the set.

It is similar to union, but it **modifies the original set**.

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print(A)
```

Output:

```text
{1, 2, 3, 4, 5}
```

---

# 📌 `intersection_update()`

Keeps only elements that are common to both sets.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)
```

Output:

```text
{3, 4}
```

---

# 📌 `difference_update()`

Removes elements from the first set that are also present in the second set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.difference_update(B)

print(A)
```

Output:

```text
{1, 2}
```

---

# 📌 `symmetric_difference_update()`

Keeps only elements that are unique to either set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.symmetric_difference_update(B)

print(A)
```

Output:

```text
{1, 2, 5, 6}
```

---

# 📊 Operation vs Update Method

| Operation | Returns New Set | Changes Original |
|---|---:|---:|
| `A.union(B)` | ✅ | ❌ |
| `A.update(B)` | ❌ | ✅ |
| `A.intersection(B)` | ✅ | ❌ |
| `A.intersection_update(B)` | ❌ | ✅ |
| `A.difference(B)` | ✅ | ❌ |
| `A.difference_update(B)` | ❌ | ✅ |
| `A.symmetric_difference(B)` | ✅ | ❌ |
| `A.symmetric_difference_update(B)` | ❌ | ✅ |

---

# 📌 Operations with Three Sets

Set operations can be performed on more than two sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}
C = {5, 6, 7}

result = A | B | C

print(result)
```

Output:

```text
{1, 2, 3, 4, 5, 6, 7}
```

---

# 📌 Intersection of Three Sets

```python
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
C = {3, 4, 5, 6}

result = A & B & C

print(result)
```

Output:

```text
{3, 4}
```

---

# 📌 Chaining Operations

You can combine operations.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 5, 6, 7}

result = (A | B) & C

print(result)
```

Output:

```text
{4, 5, 6}
```

First:

```python
A | B
```

gives:

```text
{1, 2, 3, 4, 5, 6}
```

Then:

```python
{1, 2, 3, 4, 5, 6} & C
```

gives:

```text
{4, 5, 6}
```

---

# 🌍 Real-World Example: Course Enrollment

```python
python = {"Aisha", "Saniya", "Rohan", "Kiran"}
java = {"Saniya", "Kiran", "Meera"}
```

### All students

```python
all_students = python | java

print(all_students)
```

### Students taking both

```python
both_courses = python & java

print(both_courses)
```

### Students taking only Python

```python
only_python = python - java

print(only_python)
```

### Students taking only one course

```python
one_course = python ^ java

print(one_course)
```

---

# 🌍 Real-World Example: Website Skills

```python
frontend = {"HTML", "CSS", "JavaScript", "Git"}
backend = {"Python", "SQL", "Git", "JavaScript"}
```

### All skills

```python
all_skills = frontend | backend

print(all_skills)
```

### Common skills

```python
common_skills = frontend & backend

print(common_skills)
```

### Frontend-only skills

```python
frontend_only = frontend - backend

print(frontend_only)
```

### Skills unique to one side

```python
unique_skills = frontend ^ backend

print(unique_skills)
```

---

# 🌍 Real-World Example: Social Media Followers

```python
followers_a = {"Aisha", "Saniya", "Rohan", "Kiran"}
followers_b = {"Saniya", "Kiran", "Meera", "Arjun"}
```

### Followers of either account

```python
all_followers = followers_a | followers_b

print(all_followers)
```

### Followers of both accounts

```python
common_followers = followers_a & followers_b

print(common_followers)
```

### Followers only of account A

```python
only_a = followers_a - followers_b

print(only_a)
```

### Followers of exactly one account

```python
one_account = followers_a ^ followers_b

print(one_account)
```

---

# 📌 Set Operations with Strings

Sets can contain strings.

```python
A = {"apple", "banana", "mango"}
B = {"banana", "orange", "grapes"}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
```

Possible output:

```text
{'apple', 'banana', 'mango', 'orange', 'grapes'}
{'banana'}
{'apple', 'mango'}
{'apple', 'mango', 'orange', 'grapes'}
```

Remember that sets are **unordered**, so the printed order may differ.

---

# ⚠️ Important: Set Order

Sets do not maintain a guaranteed sequence like lists.

Example:

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

The order should not be relied upon.

Do not write programs that depend on the printed order of set elements.

---

# 📌 Set Operations Do Not Allow Duplicates

```python
A = {1, 2, 2, 3}
B = {3, 4, 4, 5}

print(A | B)
```

Output:

```text
{1, 2, 3, 4, 5}
```

Duplicates are automatically removed because sets contain unique elements.

---

# 📌 `union()` Can Accept Other Iterables

The `union()` method can work with other iterables.

```python
A = {1, 2, 3}

result = A.union([3, 4, 5])

print(result)
```

Output:

```text
{1, 2, 3, 4, 5}
```

Similarly:

```python
result = A.union((4, 5, 6))

print(result)
```

---

# ⚠️ Operators vs Methods

Set operators such as:

```python
A | B
A & B
A - B
A ^ B
```

generally require set operands.

Methods are more flexible in many cases.

For example:

```python
A = {1, 2, 3}

print(A.union([3, 4, 5]))
```

Output:

```text
{1, 2, 3, 4, 5}
```

---

# 📊 Complete Set Operations Cheat Sheet

| Operation | Operator | Method |
|---|---|---|
| Union | `\|` | `union()` |
| Intersection | `&` | `intersection()` |
| Difference | `-` | `difference()` |
| Symmetric Difference | `^` | `symmetric_difference()` |
| Union Update | — | `update()` |
| Intersection Update | — | `intersection_update()` |
| Difference Update | — | `difference_update()` |
| Symmetric Difference Update | — | `symmetric_difference_update()` |

---

# 🧠 Easy Memory Trick

Remember:

```text
|  → UNION
&  → INTERSECTION
-  → DIFFERENCE
^  → SYMMETRIC DIFFERENCE
```

A simple way to remember:

```text
|  → Everything
&  → Common
-  → Remove
^  → Unique
```

---

# 🏋️ Practice Programs

## Beginner

### 1. Union

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A | B

print(result)
```

---

### 2. Intersection

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A & B

print(result)
```

---

### 3. Difference

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A - B

print(result)
```

---

### 4. Symmetric Difference

```python
A = {1, 2, 3}
B = {3, 4, 5}

result = A ^ B

print(result)
```

---

# 🏋️ Intermediate Practice

### 5. Find common subjects

```python
student1 = {"Python", "Math", "English"}
student2 = {"Python", "Science", "Math"}

common = student1 & student2

print(common)
```

---

### 6. Find subjects only for student 1

```python
student1 = {"Python", "Math", "English"}
student2 = {"Python", "Science", "Math"}

only_student1 = student1 - student2

print(only_student1)
```

---

### 7. Find all subjects

```python
student1 = {"Python", "Math", "English"}
student2 = {"Python", "Science", "Math"}

all_subjects = student1 | student2

print(all_subjects)
```

---

# 🚀 Advanced Practice

### 8. Three-set intersection

```python
A = {10, 20, 30, 40}
B = {20, 30, 40, 50}
C = {30, 40, 50, 60}

result = A & B & C

print(result)
```

---

### 9. Chained operations

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}

result = (A | B) & C

print(result)
```

---

### 10. Update operations

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print(A)
```

---

# 🏆 Challenge

Create the following sets:

```python
python_students = {
    "Aisha",
    "Saniya",
    "Rohan",
    "Kiran",
    "Meera"
}

java_students = {
    "Saniya",
    "Kiran",
    "Meera",
    "Arjun",
    "Priya"
}
```

Find:

1. [ ] All students.
2. [ ] Students studying both Python and Java.
3. [ ] Students studying only Python.
4. [ ] Students studying only Java.
5. [ ] Students studying exactly one of the two courses.
6. [ ] Add a third set containing students studying C++.
7. [ ] Find students studying all three courses.

---

# ❓ Interview Questions

- [ ] What is a union of two sets?
- [ ] Which operator is used for union?
- [ ] Which method is used for union?
- [ ] What is an intersection?
- [ ] Which operator is used for intersection?
- [ ] What is the difference between `A - B` and `B - A`?
- [ ] What is symmetric difference?
- [ ] Which operator represents symmetric difference?
- [ ] What is the difference between `union()` and `update()`?
- [ ] What is the difference between `intersection()` and `intersection_update()`?
- [ ] What is the difference between `difference()` and `difference_update()`?
- [ ] What is the difference between `symmetric_difference()` and `symmetric_difference_update()`?
- [ ] Can set operations be performed on more than two sets?
- [ ] Are the original sets changed by normal set operations?

---

# 📚 Summary

Python provides four major set operations.

### 1. Union

```python
A | B
```

or:

```python
A.union(B)
```

Returns all unique elements from both sets.

---

### 2. Intersection

```python
A & B
```

or:

```python
A.intersection(B)
```

Returns elements common to both sets.

---

### 3. Difference

```python
A - B
```

or:

```python
A.difference(B)
```

Returns elements present in `A` but not in `B`.

---

### 4. Symmetric Difference

```python
A ^ B
```

or:

```python
A.symmetric_difference(B)
```

Returns elements present in either set but not in both.

---

# 🎯 Topic Completion Checklist

- [x] I understand Union.
- [x] I understand Intersection.
- [x] I understand Difference.
- [x] I understand Symmetric Difference.
- [x] I know the set operation operators.
- [x] I know the set operation methods.
- [x] I understand update operations.
- [x] I can perform operations on multiple sets.
- [x] I understand real-world applications of set operations.
- [x] I completed the practice programs.
- [x] I completed the challenge.
- [x] I can explain the difference between all four operations.

---

# 🎉 Set Operations Completed!

```text
Set Operations
│
├── Union
│   ├── |
│   └── union()
│
├── Intersection
│   ├── &
│   └── intersection()
│
├── Difference
│   ├── -
│   └── difference()
│
└── Symmetric Difference
    ├── ^
    └── symmetric_difference()
```

---
