# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Collections → Frozen Set**

**Difficulty:** ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a frozenset is.
- [ ] Create a frozenset.
- [ ] Know the difference between a set and a frozenset.
- [ ] Know which operations are allowed and which are not.

---

# 📖 What is a Frozen Set?

A **frozenset** is an **immutable set**.

This means:

- Elements cannot be added.
- Elements cannot be removed.
- Elements cannot be modified.

Once created, it cannot be changed.

---

# 📖 Syntax

```python
frozenset(iterable)
```

---

## Example 1

```python
numbers = frozenset([10, 20, 30])

print(numbers)
print(type(numbers))
```

Output

```text
frozenset({10, 20, 30})
<class 'frozenset'>
```

---

# 📖 Creating a Frozen Set from a Set

```python
languages = {"Python", "Java", "SQL"}

frozen_languages = frozenset(languages)

print(frozen_languages)
```

Output

```text
frozenset({'Python', 'Java', 'SQL'})
```

---

# 📖 Frozen Sets Remove Duplicates

```python
numbers = frozenset([10, 20, 20, 30])

print(numbers)
```

Output

```text
frozenset({10, 20, 30})
```

Like sets, duplicate values are removed.

---

# 📖 Frozen Sets Are Unordered

```python
colors = frozenset(["Red", "Green", "Blue"])

print(colors)
```

The output order may vary.

---

# 📖 Frozen Sets Are Immutable

```python
numbers = frozenset([1, 2, 3])

numbers.add(4)
```

Output

```text
AttributeError: 'frozenset' object has no attribute 'add'
```

---

```python
numbers.remove(2)
```

Output

```text
AttributeError
```

Frozen sets cannot be modified.

---

# 📖 Allowed Operations

These methods work because they create **new** sets instead of modifying the existing one.

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
```

Output

```text
frozenset({1, 2, 3, 4, 5})
frozenset({3})
frozenset({1, 2})
frozenset({1, 2, 4, 5})
```

---

# 📖 Not Allowed Methods

These methods modify the object, so they do not exist for frozensets.

```python
add()
update()
remove()
discard()
pop()
clear()
```

Attempting to use them raises `AttributeError`.

---

# 🌍 Real-World Examples

## Fixed Permissions

```python
permissions = frozenset({
    "read",
    "write",
    "execute"
})
```

Permissions should not change accidentally.

---

## Constant Subjects

```python
subjects = frozenset({
    "Math",
    "Physics",
    "Chemistry"
})
```

---

## Days of the Weekend

```python
weekend = frozenset({
    "Saturday",
    "Sunday"
})
```

---

# 📊 Set vs Frozen Set

| Feature | Set | Frozen Set |
|---------|-----|------------|
| Mutable | ✅ Yes | ❌ No |
| Ordered | ❌ No | ❌ No |
| Duplicates | ❌ No | ❌ No |
| add() | ✅ Yes | ❌ No |
| remove() | ✅ Yes | ❌ No |
| update() | ✅ Yes | ❌ No |
| union() | ✅ Yes | ✅ Yes |
| intersection() | ✅ Yes | ✅ Yes |
| difference() | ✅ Yes | ✅ Yes |

---

# ⚠️ Common Mistakes

## ❌ Trying to Modify a Frozen Set

```python
data = frozenset([1, 2])

data.add(3)
```

Raises

```text
AttributeError
```

---

## ❌ Thinking It Is Ordered

```python
letters = frozenset(["A", "B", "C"])

print(letters)
```

The order is not guaranteed.

---

# 💡 Best Practices

- Use `set` when data changes.
- Use `frozenset` when data must remain constant.
- Use `frozenset` as dictionary keys or as elements of another set because it is immutable and hashable.

---

# 🚀 Pro Tips

A normal set **cannot** be an element of another set.

```python
a = {1, 2}

b = {a}
```

Output

```text
TypeError: unhashable type: 'set'
```

But a **frozenset can**.

```python
a = frozenset([1, 2])

b = {a}

print(b)
```

Output

```text
{frozenset({1, 2})}
```

---

# 🧠 Memory Trick

```
Set

↓

Mutable

↓

Can Change

----------------

Frozen Set

↓

Frozen

↓

Cannot Change
```

---

# ❓ Interview Questions

- [ ] What is a frozenset?
- [ ] How is it different from a set?
- [ ] Can you add elements to a frozenset?
- [ ] Why can a frozenset be used as a dictionary key?
- [ ] Can a frozenset contain duplicates?

---

# 🏋️ Practice Programs

## Easy

```python
numbers = frozenset([1, 2, 3])

print(numbers)
```

---

```python
colors = frozenset({"Red", "Green", "Blue"})

print(type(colors))
```

---

## Medium

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print(a.union(b))
print(a.intersection(b))
```

---

## Advanced

```python
permissions = frozenset({"Read", "Write"})

if "Read" in permissions:
    print("Access Granted")

print(permissions)
```

---

# 🎯 Challenge

Create two frozensets:

```python
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
```

Perform:

1. Union
2. Intersection
3. Difference
4. Symmetric Difference
5. Try using `add()` and observe the error.

---

# 📝 Assignment

- [x] Create a frozenset of five numbers.
- [x] Create a frozenset from a list.
- [x] Create a frozenset from a set.
- [x] Perform all four set operations.
- [x] Explain why `add()` is unavailable.

---

# 📚 Summary

You learned:

- What a frozenset is.
- How to create one.
- Why it is immutable.
- Which methods work.
- The differences between `set` and `frozenset`.

---

# 🎯 Topic Completion Checklist

- [x] I understand frozensets.
- [x] I know how to create one.
- [x] I know why they are immutable.
- [x] I understand the difference between a set and a frozenset.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Dictionary (`dict`) – Part 1: What is a Dictionary?**