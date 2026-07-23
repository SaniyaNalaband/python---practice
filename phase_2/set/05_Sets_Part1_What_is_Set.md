# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Collections → Set**
> **Part 1:** What is a Set?

**Difficulty:** ⭐⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a set is.
- [ ] Create sets.
- [ ] Know the characteristics of sets.
- [ ] Understand why sets are useful.

---

# 📖 What is a Set?

A **set** is an **unordered collection of unique elements**.

Unlike lists and tuples:

- A set **does not allow duplicate values**.
- A set **does not maintain element order**.

Example:

```python
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

Output (order may vary):

```text
{'Banana', 'Apple', 'Mango'}
```

---

# 📖 Why Use Sets?

Suppose you have duplicate student IDs.

```python
ids = [101, 102, 103, 102, 101]
```

Convert them to a set:

```python
ids = {101, 102, 103, 102, 101}

print(ids)
```

Output

```text
{101, 102, 103}
```

Duplicates are removed automatically.

---

# 📖 Set Syntax

```python
set_name = {item1, item2, item3}
```

Example

```python
colors = {"Red", "Green", "Blue"}
```

---

# 📖 Empty Set

❌ Wrong

```python
empty = {}

print(type(empty))
```

Output

```text
<class 'dict'>
```

`{}` creates an **empty dictionary**, not a set.

---

✅ Correct

```python
empty = set()

print(type(empty))
```

Output

```text
<class 'set'>
```

---

# 📖 Sets Remove Duplicates

```python
numbers = {10, 20, 20, 30, 30}

print(numbers)
```

Output

```text
{10, 20, 30}
```

---

# 📖 Sets Can Store Different Data Types

```python
data = {"Python", 100, True, 95.5}

print(data)
```

Output (order may vary)

```text
{100, True, 95.5, 'Python'}
```

---

# 📖 Unordered Collection

```python
letters = {"A", "B", "C"}

print(letters)
```

Output may be:

```text
{'C', 'A', 'B'}
```

or

```text
{'A', 'C', 'B'}
```

The order is **not guaranteed**.

---

# 📖 Mutable Collection

You can add or remove elements from a set.

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

Output

```text
{1, 2, 3, 4}
```

---

# 📖 Immutable Elements

Elements inside a set must be immutable.

✅ Allowed

```python
data = {1, "Python", (10, 20)}
```

❌ Not Allowed

```python
data = {1, [10, 20]}
```

Output

```text
TypeError: unhashable type: 'list'
```

Lists cannot be stored in sets because they are mutable.

---

# 🌍 Real-World Examples

## Unique Student IDs

```python
student_ids = {101, 102, 103}
```

---

## Unique Email Addresses

```python
emails = {
    "a@gmail.com",
    "b@gmail.com",
    "c@gmail.com"
}
```

---

## Programming Languages

```python
languages = {
    "Python",
    "Java",
    "C++"
}
```

---

# 📊 List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Brackets | `[]` | `()` | `{}` |
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Duplicates | ✅ | ✅ | ❌ |
| Indexing | ✅ | ✅ | ❌ |

---

# ⚠️ Common Mistakes

## ❌ Creating an Empty Set with `{}`

```python
x = {}
```

This creates a dictionary.

Correct:

```python
x = set()
```

---

## ❌ Expecting Order

```python
colors = {"Red", "Green", "Blue"}

print(colors)
```

The output order is unpredictable.

---

## ❌ Trying to Access by Index

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Output

```text
TypeError
```

Sets do not support indexing.

---

# 💡 Best Practices

- Use sets to remove duplicates.
- Use sets for membership testing (`in`) because they are very fast.
- Don't rely on the order of elements.

---

# 🧠 Memory Trick

```
Set

↓

{}

↓

Unique

↓

Unordered

↓

Mutable
```

Remember:

**UUM**

- **U** → Unique
- **U** → Unordered
- **M** → Mutable

---

# ❓ Interview Questions

- [x] What is a set?
- [x] Do sets allow duplicates?
- [x] Are sets ordered?
- [x] Can you access a set using an index?
- [x] How do you create an empty set?

---

# 🏋️ Practice Programs

## Easy

```python
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

---

```python
numbers = {1, 2, 2, 3}

print(numbers)
```

---

## Medium

```python
empty = set()

print(type(empty))
```

---

```python
data = {"Python", 100, True}

print(data)
```

---

## Advanced

```python
students = {"Rahul", "Saniya", "Aisha", "Rahul"}

print(students)
```

Observe that `"Rahul"` appears only once.

---

# 🎯 Challenge

Create the following sets:

- `colors`
- `cities`
- `languages`
- `student_ids`

Then:

- Add a duplicate value and observe the output.
- Try creating an empty set.
- Try accessing an element by index and note the error.

---

# 📝 Assignment

- [x] Create a set of five fruits.
- [x] Create a set with duplicate numbers.
- [x] Create an empty set.
- [x] Create a mixed-data-type set.
- [x] Explain why sets cannot be indexed.

---

# 📚 Summary

You learned:

- What a set is.
- Set syntax.
- Empty sets.
- Unique elements.
- Unordered nature.
- Mutable collection.
- Immutable elements.

---

# 🎯 Topic Completion Checklist

- [x] I understand what a set is.
- [x] I know how to create a set.
- [x] I know that sets remove duplicates.
- [x] I know that sets are unordered.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Set – Part 2: Set Characteristics**