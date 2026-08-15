# 🐍 Python Master Course

# 📦 Phase 6: Collections – Sets


## 📌 Topic 3: Set methods

**Difficulty:** ⭐⭐ Beginner → Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* [ ] Understand what set methods are.
* [ ] Add elements to a set using `add()`.
* [ ] Add multiple elements using `update()`.
* [ ] Remove elements using `remove()`, `discard()`, `pop()`, and `clear()`.
* [ ] Understand the difference between `remove()` and `discard()`.
* [ ] Perform set operations using methods such as `union()`, `intersection()`, and `difference()`.
* [ ] Use `symmetric_difference()`.
* [ ] Check relationships between sets.
* [ ] Use `issubset()`, `issuperset()`, and `isdisjoint()`.
* [ ] Create copies of sets using `copy()`.
* [ ] Understand which set methods modify the original set.
* [ ] Avoid common mistakes when working with sets.

---

# 📖 1. What Are Set Methods?

Set methods are **built-in methods provided by Python's `set` data type**.

They allow us to:

* Add elements
* Remove elements
* Update sets
* Combine sets
* Find common elements
* Find differences
* Compare sets
* Create copies

Example:

```python
skills = {"Python", "SQL"}

skills.add("Git")

print(skills)
```

Output:

```text
{'Python', 'SQL', 'Git'}
```

The `add()` method adds a new element to the set.

---

# 🧠 2. Important Set Methods

Python provides several useful methods for sets.

| Method                          | Purpose                                           |
| ------------------------------- | ------------------------------------------------- |
| `add()`                         | Adds one element                                  |
| `update()`                      | Adds multiple elements                            |
| `remove()`                      | Removes an element                                |
| `discard()`                     | Removes an element without raising an error       |
| `pop()`                         | Removes and returns an arbitrary element          |
| `clear()`                       | Removes all elements                              |
| `copy()`                        | Creates a copy of a set                           |
| `union()`                       | Combines sets                                     |
| `intersection()`                | Finds common elements                             |
| `difference()`                  | Finds elements present only in one set            |
| `symmetric_difference()`        | Finds elements present in either set but not both |
| `intersection_update()`         | Keeps only common elements                        |
| `difference_update()`           | Removes common elements                           |
| `symmetric_difference_update()` | Keeps only non-common elements                    |
| `issubset()`                    | Checks whether one set is a subset                |
| `issuperset()`                  | Checks whether one set is a superset              |
| `isdisjoint()`                  | Checks whether two sets have no common elements   |

---

# ➕ 3. `add()` Method

The `add()` method adds **one element** to a set.

## Syntax

```python
set_name.add(element)
```

Example:

```python
skills = {"Python", "SQL"}

skills.add("Git")

print(skills)
```

Output:

```text
{'Python', 'SQL', 'Git'}
```

---

## Adding a Number

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

---

## Adding a Duplicate

Sets do not store duplicate elements.

```python
languages = {"Python", "Java"}

languages.add("Python")

print(languages)
```

Output:

```text
{'Python', 'Java'}
```

Nothing new is added because `"Python"` already exists.

---

## `add()` Modifies the Original Set

```python
skills = {"Python", "SQL"}

skills.add("Git")

print(skills)
```

The original set is changed.

---

# 📚 4. `update()` Method

The `update()` method adds **multiple elements** to a set.

## Syntax

```python
set_name.update(iterable)
```

Example:

```python
skills = {"Python", "SQL"}

skills.update(["Git", "HTML", "CSS"])

print(skills)
```

Output:

```text
{'Python', 'SQL', 'Git', 'HTML', 'CSS'}
```

---

## Using Another Set

```python
python_skills = {"Python", "SQL"}

web_skills = {"HTML", "CSS", "JavaScript"}

python_skills.update(web_skills)

print(python_skills)
```

Output:

```text
{'Python', 'SQL', 'HTML', 'CSS', 'JavaScript'}
```

---

## Using a Tuple

```python
skills = {"Python"}

skills.update(("SQL", "Git"))

print(skills)
```

Output:

```text
{'Python', 'SQL', 'Git'}
```

---

## Using a String

Be careful when passing a string to `update()`.

```python
letters = {"A", "B"}

letters.update("CD")

print(letters)
```

Output:

```text
{'A', 'B', 'C', 'D'}
```

A string is an iterable, so its characters are added individually.

---

# 🔥 5. Difference Between `add()` and `update()`

| `add()`            | `update()`             |
| ------------------ | ---------------------- |
| Adds one element   | Adds multiple elements |
| Accepts one object | Accepts an iterable    |
| `set.add(x)`       | `set.update(iterable)` |

Example:

```python
skills = {"Python"}

skills.add("SQL")

print(skills)
```

Output:

```text
{'Python', 'SQL'}
```

---

Example:

```python
skills = {"Python"}

skills.update(["SQL", "Git", "HTML"])

print(skills)
```

Output:

```text
{'Python', 'SQL', 'Git', 'HTML'}
```

### Memory Trick

```text
add()
 ↓
ONE element

update()
 ↓
MULTIPLE elements
```

---

# ❌ 6. `remove()` Method

The `remove()` method removes a specific element from a set.

## Syntax

```python
set_name.remove(element)
```

Example:

```python
skills = {"Python", "SQL", "Git"}

skills.remove("SQL")

print(skills)
```

Output:

```text
{'Python', 'Git'}
```

---

## ⚠️ What Happens If the Element Does Not Exist?

```python
skills = {"Python", "SQL"}

skills.remove("Java")
```

Output:

```text
KeyError
```

`remove()` raises a `KeyError` if the element does not exist.

---

# 🛡️ 7. `discard()` Method

The `discard()` method also removes an element.

## Syntax

```python
set_name.discard(element)
```

Example:

```python
skills = {"Python", "SQL", "Git"}

skills.discard("SQL")

print(skills)
```

Output:

```text
{'Python', 'Git'}
```

---

## What If the Element Does Not Exist?

```python
skills = {"Python", "SQL"}

skills.discard("Java")

print(skills)
```

Output:

```text
{'Python', 'SQL'}
```

No error occurs.

---

# ⚔️ 8. `remove()` vs `discard()`

This is one of the most important differences in set methods.

| Feature            | `remove()` | `discard()` |
| ------------------ | ---------- | ----------- |
| Removes element    | ✅          | ✅           |
| Element must exist | Yes        | No          |
| Error if missing   | `KeyError` | No error    |
| Safe when unsure   | ❌          | ✅           |

Example:

```python
skills = {"Python", "SQL"}

skills.remove("Java")
```

Raises:

```text
KeyError
```

But:

```python
skills = {"Python", "SQL"}

skills.discard("Java")

print(skills)
```

Works without an error.

### Memory Trick

> **remove = remove it or raise an error**
> **discard = remove it if it exists**

---

# 🎲 9. `pop()` Method

The `pop()` method removes and returns an **arbitrary element** from a set.

## Syntax

```python
set_name.pop()
```

Example:

```python
numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed:", removed)
print("Remaining:", numbers)
```

The exact removed element should not be assumed because sets are unordered.

Possible output:

```text
Removed: 10
Remaining: {20, 30, 40}
```

The output can vary.

---

## Important

Unlike lists:

```python
numbers.pop(0)
```

is not valid for sets.

A set does not support index-based removal.

---

# 🧹 10. `clear()` Method

The `clear()` method removes **all elements** from a set.

## Syntax

```python
set_name.clear()
```

Example:

```python
skills = {"Python", "SQL", "Git"}

skills.clear()

print(skills)
```

Output:

```text
set()
```

The result is an empty set.

---

## Empty Set Reminder

An empty set is created using:

```python
set()
```

Not:

```python
{}
```

Because:

```python
{}
```

creates an empty dictionary.

---

# 📋 11. `copy()` Method

The `copy()` method creates a **shallow copy** of a set.

## Syntax

```python
new_set = old_set.copy()
```

Example:

```python
skills = {"Python", "SQL", "Git"}

new_skills = skills.copy()

print(skills)
print(new_skills)
```

Output:

```text
{'Python', 'SQL', 'Git'}
{'Python', 'SQL', 'Git'}
```

---

## Modifying the Copy

```python
skills = {"Python", "SQL"}

new_skills = skills.copy()

new_skills.add("Git")

print("Original:", skills)
print("Copy:", new_skills)
```

Output:

```text
Original: {'Python', 'SQL'}
Copy: {'Python', 'SQL', 'Git'}
```

The original set is not modified.

---

# 🔗 12. `union()` Method

The `union()` method returns a new set containing elements from **both sets**.

## Syntax

```python
set1.union(set2)
```

Example:

```python
python_skills = {"Python", "SQL", "Git"}

web_skills = {"HTML", "CSS", "Git"}

all_skills = python_skills.union(web_skills)

print(all_skills)
```

Output:

```text
{'Python', 'SQL', 'Git', 'HTML', 'CSS'}
```

Duplicate `"Git"` appears only once.

---

## Important

`union()` does not modify the original sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b)

print(a)
print(b)
print(c)
```

Output:

```text
{1, 2, 3}
{3, 4, 5}
{1, 2, 3, 4, 5}
```

---

# 🔄 13. `intersection()` Method

The `intersection()` method returns elements that are **common to both sets**.

## Syntax

```python
set1.intersection(set2)
```

Example:

```python
python_students = {"A", "B", "C", "D"}

web_students = {"C", "D", "E", "F"}

common_students = python_students.intersection(web_students)

print(common_students)
```

Output:

```text
{'C', 'D'}
```

---

## Using Multiple Sets

```python
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}

result = a.intersection(b, c)

print(result)
```

Output:

```text
{3, 4}
```

---

# ➖ 14. `difference()` Method

The `difference()` method returns elements that exist in the **first set but not in the other set**.

## Syntax

```python
set1.difference(set2)
```

Example:

```python
python_skills = {"Python", "SQL", "Git"}

web_skills = {"HTML", "CSS", "Git"}

result = python_skills.difference(web_skills)

print(result)
```

Output:

```text
{'Python', 'SQL'}
```

---

## Important

The direction matters.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b))
print(b.difference(a))
```

Output:

```text
{1, 2}
{4, 5}
```

### Memory Trick

```text
A.difference(B)

↓

What is in A
but NOT in B?
```

---

# 🔀 15. `symmetric_difference()` Method

The `symmetric_difference()` method returns elements that are present in **either set, but not in both**.

## Syntax

```python
set1.symmetric_difference(set2)
```

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.symmetric_difference(b)

print(result)
```

Output:

```text
{1, 2, 4, 5}
```

The common element `3` is removed.

---

# 🔍 16. `issubset()` Method

The `issubset()` method checks whether **all elements of one set exist in another set**.

## Syntax

```python
set1.issubset(set2)
```

Example:

```python
python_skills = {"Python", "SQL"}

all_skills = {"Python", "SQL", "Git", "HTML"}

print(python_skills.issubset(all_skills))
```

Output:

```text
True
```

Because every element of `python_skills` exists in `all_skills`.

---

## Example with False

```python
skills = {"Python", "Java"}

programming = {"Python", "SQL", "Git"}

print(skills.issubset(programming))
```

Output:

```text
False
```

Because `"Java"` is not present.

---

# 🔎 17. `issuperset()` Method

The `issuperset()` method checks whether a set contains **all elements of another set**.

## Syntax

```python
set1.issuperset(set2)
```

Example:

```python
all_skills = {"Python", "SQL", "Git", "HTML"}

python_skills = {"Python", "SQL"}

print(all_skills.issuperset(python_skills))
```

Output:

```text
True
```

---

## Relationship

These two questions are opposites:

```python
A.issubset(B)
```

asks:

> Are all elements of A inside B?

While:

```python
B.issuperset(A)
```

asks:

> Does B contain all elements of A?

---

# 🚫 18. `isdisjoint()` Method

The `isdisjoint()` method checks whether two sets have **no elements in common**.

## Syntax

```python
set1.isdisjoint(set2)
```

Example:

```python
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))
```

Output:

```text
True
```

There are no common elements.

---

## Example with Common Elements

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.isdisjoint(b))
```

Output:

```text
False
```

Because both sets contain `3`.

---

# 🔄 19. `intersection_update()` Method

The `intersection_update()` method updates the original set so that it contains **only common elements**.

## Syntax

```python
set1.intersection_update(set2)
```

Example:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.intersection_update(b)

print(a)
```

Output:

```text
{3, 4}
```

Notice that `a` itself was changed.

---

## `intersection()` vs `intersection_update()`

```python
a = {1, 2, 3}
b = {2, 3, 4}

result = a.intersection(b)

print(a)
print(result)
```

Output:

```text
{1, 2, 3}
{2, 3}
```

`intersection()` creates a new set.

---

But:

```python
a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)

print(a)
```

Output:

```text
{2, 3}
```

`intersection_update()` modifies the original set.

---

# ➖ 20. `difference_update()` Method

The `difference_update()` method removes elements from the first set that are also present in another set.

## Syntax

```python
set1.difference_update(set2)
```

Example:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.difference_update(b)

print(a)
```

Output:

```text
{1, 2}
```

The common elements were removed from `a`.

---

# 🔀 21. `symmetric_difference_update()` Method

The `symmetric_difference_update()` method updates the original set with elements that are present in either set, but not both.

## Syntax

```python
set1.symmetric_difference_update(set2)
```

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)

print(a)
```

Output:

```text
{1, 2, 4, 5}
```

The common element `3` was removed.

---

# 📊 22. Methods That Return a New Set vs Modify the Set

This distinction is extremely important.

## Return a New Set

These methods do not modify the original set:

```text
union()
intersection()
difference()
symmetric_difference()
copy()
```


Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(a)
print(result)
```

---

## Modify the Original Set

These methods modify the set:

```text
add()
update()
remove()
discard()
pop()
clear()
intersection_update()
difference_update()
symmetric_difference_update()
```

Example:

```python
a = {1, 2, 3}

a.add(4)

print(a)
```

Output:

```text
{1, 2, 3, 4}
```

---

# 🧠 23. Complete Set Methods Table

| Method                          | Purpose                         | Modifies Original? |
| ------------------------------- | ------------------------------- | ------------------ |
| `add()`                         | Add one element                 | ✅                  |
| `update()`                      | Add multiple elements           | ✅                  |
| `remove()`                      | Remove an element               | ✅                  |
| `discard()`                     | Remove an element safely        | ✅                  |
| `pop()`                         | Remove arbitrary element        | ✅                  |
| `clear()`                       | Remove all elements             | ✅                  |
| `copy()`                        | Create a copy                   | ❌                  |
| `union()`                       | Combine sets                    | ❌                  |
| `intersection()`                | Find common elements            | ❌                  |
| `difference()`                  | Find elements only in first set | ❌                  |
| `symmetric_difference()`        | Find non-common elements        | ❌                  |
| `intersection_update()`         | Keep common elements            | ✅                  |
| `difference_update()`           | Remove common elements          | ✅                  |
| `symmetric_difference_update()` | Keep non-common elements        | ✅                  |
| `issubset()`                    | Check subset relationship       | ❌                  |
| `issuperset()`                  | Check superset relationship     | ❌                  |
| `isdisjoint()`                  | Check if no elements are common | ❌                  |

---

# 🔥 24. Set Methods vs Set Operators

Many set operations can also be performed using operators.

| Method                   | Operator |   |
| ------------------------ | -------- | - |
| `union()`                | `        | ` |
| `intersection()`         | `&`      |   |
| `difference()`           | `-`      |   |
| `symmetric_difference()` | `^`      |   |
| `issubset()`             | `<=`     |   |
| `issuperset()`           | `>=`     |   |

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a | b)
```

Both produce:

```text
{1, 2, 3, 4, 5}
```

---

# ⚠️ 25. Common Mistakes

## ❌ Mistake 1: Using `add()` to Add Multiple Elements

Wrong:

```python
skills = {"Python"}

skills.add("SQL", "Git")
```

This causes an error because `add()` accepts one element.

Correct:

```python
skills.update(["SQL", "Git"])
```

---

## ❌ Mistake 2: Expecting `remove()` to Ignore Missing Elements

```python
skills = {"Python", "SQL"}

skills.remove("Java")
```

This raises:

```text
KeyError
```

If you are not sure whether the element exists, use:

```python
skills.discard("Java")
```

---

## ❌ Mistake 3: Expecting `pop()` to Remove a Specific Element

Wrong:

```python
numbers = {10, 20, 30}

numbers.pop(20)
```

`set.pop()` does not accept an index or value.

Correct:

```python
numbers.remove(20)
```

or:

```python
numbers.discard(20)
```

---

## ❌ Mistake 4: Assuming Set Order

Do not depend on:

```python
numbers = {10, 20, 30}

numbers.pop()
```

always removing `10`.

Sets are unordered collections, so the removed element should not be assumed.

---

## ❌ Mistake 5: Forgetting That Update Methods Modify the Set

```python
a = {1, 2, 3}

a.intersection_update({2, 3, 4})

print(a)
```

Output:

```text
{2, 3}
```

The original set has changed.

---

# 🌍 26. Real-World Example: Student Skills

Suppose we have two groups of students.

```python
python_students = {
    "Asha",
    "Priya",
    "Neha",
    "Ananya"
}

sql_students = {
    "Priya",
    "Ananya",
    "Kavya",
    "Meera"
}
```

### Students who know both Python and SQL

```python
common = python_students.intersection(sql_students)

print(common)
```

Output:

```text
{'Priya', 'Ananya'}
```

---

### Students who know Python but not SQL

```python
python_only = python_students.difference(sql_students)

print(python_only)
```

Output:

```text
{'Asha', 'Neha'}
```

---

### Students who know either Python or SQL, but not both

```python
only_one = python_students.symmetric_difference(sql_students)

print(only_one)
```

Output:

```text
{'Asha', 'Neha', 'Kavya', 'Meera'}
```

---

# 🌍 27. Real-World Example: Website Skills

```python
frontend = {
    "HTML",
    "CSS",
    "JavaScript"
}

backend = {
    "Python",
    "SQL",
    "Git"
}

full_stack = frontend.union(backend)

print(full_stack)
```

Output:

```text
{'HTML', 'CSS', 'JavaScript', 'Python', 'SQL', 'Git'}
```

---

# 🌍 28. Real-World Example: Removing Completed Tasks

```python
tasks = {
    "Learn Python",
    "Practice Sets",
    "Learn SQL",
    "Practice Git"
}

tasks.remove("Practice Sets")

print(tasks)
```

Output:

```text
{'Learn Python', 'Learn SQL', 'Practice Git'}
```

---

# 🌍 29. Real-World Example: Updating Skills

```python
skills = {
    "Python",
    "SQL"
}

new_skills = [
    "Git",
    "HTML",
    "CSS"
]

skills.update(new_skills)

print(skills)
```

Output:

```text
{'Python', 'SQL', 'Git', 'HTML', 'CSS'}
```

---

# 💻 30. Practice Programs

## 🟢 Easy

### Program 1: Add an Element

```python
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)
```

---

### Program 2: Remove an Element

```python
fruits = {"Apple", "Banana", "Mango"}

fruits.remove("Banana")

print(fruits)
```

---

### Program 3: Discard an Element

```python
numbers = {10, 20, 30}

numbers.discard(40)

print(numbers)
```

---

### Program 4: Clear a Set

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

---

# 🟡 Medium

### Program 5: Add Multiple Skills

```python
skills = {"Python"}

skills.update(["SQL", "Git", "HTML"])

print(skills)
```

---

### Program 6: Find Common Subjects

```python
student1 = {
    "Python",
    "SQL",
    "HTML"
}

student2 = {
    "SQL",
    "HTML",
    "CSS"
}

common = student1.intersection(student2)

print(common)
```

---

### Program 7: Find Unique Skills

```python
student1 = {
    "Python",
    "SQL",
    "Git"
}

student2 = {
    "SQL",
    "HTML",
    "CSS"
}

unique = student1.difference(student2)

print(unique)
```

---

### Program 8: Check Subset

```python
basic = {
    "Python",
    "SQL"
}

all_skills = {
    "Python",
    "SQL",
    "Git",
    "HTML"
}

print(basic.issubset(all_skills))
```

Output:

```text
True
```

---

# 🔴 Advanced

## Program 9: Student Skill Analysis

```python
python_students = {
    "Asha",
    "Priya",
    "Neha",
    "Ananya"
}

sql_students = {
    "Priya",
    "Ananya",
    "Kavya",
    "Meera"
}

print("Both Python and SQL:")
print(python_students.intersection(sql_students))

print("Python only:")
print(python_students.difference(sql_students))

print("SQL only:")
print(sql_students.difference(python_students))

print("Either Python or SQL:")
print(python_students.union(sql_students))

print("Only one skill:")
print(python_students.symmetric_difference(sql_students))
```

---

## Program 10: Managing Technology Skills

```python
skills = {
    "Python",
    "SQL"
}

skills.add("Git")

skills.update(["HTML", "CSS"])

skills.discard("Java")

print(skills)
```

---

# 🏆 31. Challenge

Create two sets:

```python
morning_students = {
    "A",
    "B",
    "C",
    "D"
}

evening_students = {
    "C",
    "D",
    "E",
    "F"
}
```

Find:

1. Students in both groups.
2. Students only in the morning group.
3. Students only in the evening group.
4. All students.
5. Students belonging to only one group.
6. Check whether the morning group is a subset of all students.
7. Check whether all students are a superset of the morning group.
8. Check whether the two groups are disjoint.

---

# 🧪 32. Mini Project: Skill Tracker

Create a simple skill tracker using sets.

```python
skills = {
    "Python",
    "SQL"
}

print("Current skills:", skills)

skills.add("Git")

skills.update(["HTML", "CSS"])

print("Updated skills:", skills)

skills.discard("Java")

print("Final skills:", skills)
```

Expected behavior:

* Start with Python and SQL.
* Add Git.
* Add HTML and CSS.
* Safely attempt to remove Java.
* Display the final set.

---

# 🎤 33. Interview Questions

* [ ] What are set methods in Python?
* [ ] What does `add()` do?
* [ ] What is the difference between `add()` and `update()`?
* [ ] What does `remove()` do?
* [ ] What happens if `remove()` cannot find an element?
* [ ] What is the difference between `remove()` and `discard()`?
* [ ] What does `pop()` do in a set?
* [ ] Why can't we use an index with `set.pop()`?
* [ ] What does `clear()` do?
* [ ] What does `copy()` do?
* [ ] What is the difference between `union()` and `intersection()`?
* [ ] What does `difference()` return?
* [ ] What is symmetric difference?
* [ ] What does `issubset()` check?
* [ ] What does `issuperset()` check?
* [ ] What does `isdisjoint()` check?
* [ ] Which set methods modify the original set?
* [ ] Which set methods return a new set?
* [ ] What is the difference between `intersection()` and `intersection_update()`?
* [ ] What is the difference between `difference()` and `difference_update()`?

---

# 📝 34. Assignment

Complete the following programs without looking at the solutions.

### Task 1

Create a set containing:

```text
Python
SQL
Git
```

Add:

```text
HTML
```

---

### Task 2

Create a set containing five numbers and remove one number using `remove()`.

---

### Task 3

Try to remove an element that does not exist using `discard()`.

Observe what happens.

---

### Task 4

Create two sets and find their union.

---

### Task 5

Create two sets and find their intersection.

---

### Task 6

Create two sets and find their difference in both directions.

---

### Task 7

Create two sets and find their symmetric difference.

---

### Task 8

Check whether one set is a subset of another set.

---

### Task 9

Check whether one set is a superset of another set.

---

### Task 10

Create two sets with no common elements and use `isdisjoint()`.

---

# 🧠 35. Memory Tricks

Remember the most important methods:

```text
add()
 ↓
Add ONE element

update()
 ↓
Add MULTIPLE elements

remove()
 ↓
Remove + error if missing

discard()
 ↓
Remove + no error if missing

pop()
 ↓
Remove arbitrary element

clear()
 ↓
Remove EVERYTHING
```

---

For set relationships:

```text
issubset()
 ↓
Is A inside B?

issuperset()
 ↓
Does A contain B?

isdisjoint()
 ↓
Do A and B have NOTHING common?
```

---

For set operations:

```text
union()
 ↓
Everything from both

intersection()
 ↓
Common elements

difference()
 ↓
Only in first set

symmetric_difference()
 ↓
Only in one set, NOT both
```

---

# 📌 36. Important Things to Remember

### 1. Sets do not allow duplicates

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

---

### 2. Sets are unordered

Do not rely on the displayed order of elements.

---

### 3. Sets are mutable

You can modify a set after creating it.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

---

### 4. Set elements must be hashable

You can store immutable/hashable objects such as:

```python
numbers = {1, 2, 3}

names = {"Asha", "Priya"}

values = {(1, 2), (3, 4)}
```

But you cannot directly store a list inside a set:

```python
numbers = {[1, 2, 3]}
```

This raises:

```text
TypeError: unhashable type: 'list'
```

---

# ⚠️ 37. Important: `set` vs `frozenset`

A normal set is mutable:

```python
skills = {"Python", "SQL"}

skills.add("Git")
```

A `frozenset` is immutable:

```python
skills = frozenset({"Python", "SQL"})
```

You cannot use methods such as `add()` or `remove()` on a `frozenset`.

We will study `frozenset` in the next topic.

---

# 📚 38. Complete Set Methods Cheat Sheet

```python
# Adding
set.add(element)
set.update(iterable)

# Removing
set.remove(element)
set.discard(element)
set.pop()
set.clear()

# Copying
set.copy()

# Set operations
set.union(other)
set.intersection(other)
set.difference(other)
set.symmetric_difference(other)

# Set relationships
set.issubset(other)
set.issuperset(other)
set.isdisjoint(other)

# Updating operations
set.intersection_update(other)
set.difference_update(other)
set.symmetric_difference_update(other)
```

---

# 📊 39. Quick Revision Table

| Method                          | Meaning                 | Changes Set? |
| ------------------------------- | ----------------------- | ------------ |
| `add()`                         | Add one item            | ✅            |
| `update()`                      | Add many items          | ✅            |
| `remove()`                      | Remove item             | ✅            |
| `discard()`                     | Safely remove item      | ✅            |
| `pop()`                         | Remove arbitrary item   | ✅            |
| `clear()`                       | Remove all items        | ✅            |
| `copy()`                        | Copy set                | ❌            |
| `union()`                       | Combine sets            | ❌            |
| `intersection()`                | Common items            | ❌            |
| `difference()`                  | Items only in first set | ❌            |
| `symmetric_difference()`        | Items in only one set   | ❌            |
| `intersection_update()`         | Keep common items       | ✅            |
| `difference_update()`           | Remove common items     | ✅            |
| `symmetric_difference_update()` | Keep non-common items   | ✅            |
| `issubset()`                    | Check subset            | ❌            |
| `issuperset()`                  | Check superset          | ❌            |
| `isdisjoint()`                  | Check no common items   | ❌            |

---

# 📚 40. Summary

In this lesson, you learned:

* What set methods are.
* How to add elements using `add()`.
* How to add multiple elements using `update()`.
* How to remove elements using `remove()`.
* How to safely remove elements using `discard()`.
* How `pop()` works with sets.
* How to remove all elements using `clear()`.
* How to copy a set using `copy()`.
* How to combine sets using `union()`.
* How to find common elements using `intersection()`.
* How to find differences using `difference()`.
* How to find non-common elements using `symmetric_difference()`.
* How to check subsets and supersets.
* How to check whether sets are disjoint.
* How update methods modify the original set.
* The difference between methods that return new sets and methods that modify existing sets.
* Common mistakes when working with set methods.

---

# 🎯 Topic Completion Checklist

* [x] I understand what set methods are.
* [x] I know how to use `add()`.
* [x] I know how to use `update()`.
* [x] I understand `remove()`.
* [x] I understand `discard()`.
* [x] I know the difference between `remove()` and `discard()`.
* [x] I understand `pop()`.
* [x] I understand `clear()`.
* [x] I know how to use `copy()`.
* [x] I understand `union()`.
* [x] I understand `intersection()`.
* [x] I understand `difference()`.
* [x] I understand `symmetric_difference()`.
* [x] I understand `intersection_update()`.
* [x] I understand `difference_update()`.
* [x] I understand `symmetric_difference_update()`.
* [x] I understand `issubset()`.
* [x] I understand `issuperset()`.
* [x] I understand `isdisjoint()`.
* [x] I know which methods modify the original set.
* [x] I completed all practice programs.
* [x] I completed the challenge.
* [x] I completed the assignment.
* [x] I can explain set methods without referring to my notes.

---

# 🚀 Final Challenge

Without looking at your notes, create a program that manages two groups of students.

Your program should:

1. Create two sets.
2. Add a new student to one set.
3. Add multiple students to the other set.
4. Remove a student.
5. Safely discard a student who may not exist.
6. Find students in both groups.
7. Find students unique to each group.
8. Find all students.
9. Find students who belong to only one group.
10. Check whether one group is a subset of all students.
11. Check whether all students are a superset of one group.
12. Check whether the two original groups are disjoint.

If you can complete this without looking at the notes, you have a strong understanding of **Python Set Methods**.

---

# 🏆 Set Methods Mastery

```text
                  SET METHODS
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     MODIFY         OPERATIONS      CHECK
        │              │              │
   add()          union()        issubset()
   update()       intersection() issuperset()
   remove()       difference()   isdisjoint()
   discard()      symmetric_
   pop()          difference()
   clear()
        │
        ↓
     UPDATE
        │
 intersection_update()
 difference_update()
 symmetric_difference_update()
```

---

# 📚 Next Topic

➡️ **Next Topic: Frozen Sets (`frozenset`)**

In the next topic, you will learn:

* What a `frozenset` is.
* How to create a `frozenset`.
* Difference between `set` and `frozenset`.
* Why `frozenset` is immutable.
* Which methods work with `frozenset`.
* Why `frozenset` can be used as a dictionary key.
* Real-world uses of `frozenset`.
* Practice programs and challenges.

---

## ⭐ Quote of the Day

> **"Sets help you manage unique data, and set methods give you the power to work with that data efficiently."** 🐍
