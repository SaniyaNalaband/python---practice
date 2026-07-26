# 🐍 Python Master Course

> **Phase 3:** Operators  
> **Topic 5:** Identity Operators

**Difficulty:** ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand identity operators.
- [ ] Differentiate between `is` and `==`.
- [ ] Use `is` and `is not` correctly.
- [ ] Understand object identity in memory.
- [ ] Avoid common mistakes when comparing objects.

---

# 📖 What are Identity Operators?

Identity operators are used to check **whether two variables refer to the same object in memory**.

Python provides two identity operators:

| Operator | Meaning |
|----------|---------|
| `is` | Returns `True` if both variables refer to the same object |
| `is not` | Returns `True` if both variables refer to different objects |

Unlike comparison operators, identity operators **do not compare values**. They compare **memory locations (object identity)**.

---

# 📖 Identity vs Equality

There is an important difference between `==` and `is`.

| Operator | Checks |
|----------|---------|
| `==` | Values are equal |
| `is` | Objects are the same in memory |

---

# 1️⃣ Identity Operator (`is`)

Checks whether two variables point to the **same object**.

### Syntax

```python
a is b
```

---

### Example 1

```python
a = [10, 20, 30]
b = a

print(a is b)
```

Output

```text
True
```

Explanation:

Both `a` and `b` refer to the same list object.

---

### Example 2

```python
a = [10, 20]
b = [10, 20]

print(a is b)
```

Output

```text
False
```

Explanation:

The values are the same, but Python created two different list objects.

---

### Example 3

```python
a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)
```

Output

```text
True
False
```

Explanation:

- `==` compares values.
- `is` compares object identity.

---

# 🌍 Real-World Example

```python
employee = {
    "name": "Rahul"
}

manager = employee

print(employee is manager)
```

Output

```text
True
```

Both variables refer to the same dictionary.

---

# 2️⃣ Identity Operator (`is not`)

Checks whether two variables refer to **different objects**.

### Syntax

```python
a is not b
```

---

### Example

```python
a = [1, 2]
b = [1, 2]

print(a is not b)
```

Output

```text
True
```

---

### Example

```python
a = [1, 2]
b = a

print(a is not b)
```

Output

```text
False
```

---

# 📖 Identity with `None`

The recommended way to check for `None` is using `is`.

```python
value = None

print(value is None)
```

Output

```text
True
```

---

### Checking for Not None

```python
name = "Python"

print(name is not None)
```

Output

```text
True
```

---

# 📖 Using `id()`

The `id()` function returns the memory identity of an object.

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

Output

```text
140245678912
140245678912
```

The numbers may be different on your computer, but they will be the **same** because both variables reference the same object.

---

### Different Objects

```python
a = [1, 2]
b = [1, 2]

print(id(a))
print(id(b))
```

Output

```text
140245678912
140245679360
```

The memory identities are different.

---

# 📊 Summary Table

| Expression | Meaning |
|------------|---------|
| `a is b` | Same object |
| `a is not b` | Different objects |
| `a == b` | Same value |

---

# ⚠️ Common Mistakes

## ❌ Using `is` Instead of `==`

Incorrect

```python
a = 100
b = 100

print(a is b)
```

Although this may print `True` on some systems, **do not use `is` to compare numbers or strings**.

Correct

```python
print(a == b)
```

Use:

- `==` → compare values
- `is` → compare object identity

---

## ❌ Comparing Strings with `is`

Incorrect

```python
name = "Python"

print(name is "Python")
```

Correct

```python
print(name == "Python")
```

---

## ❌ Forgetting That Lists Are Separate Objects

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Output

```text
True
False
```

---

# 💡 Best Practices

- Use `==` to compare values.
- Use `is` only to compare object identity.
- Use `is None` and `is not None` when checking for `None`.
- Avoid using `is` for numbers, strings, and other immutable values.

---

# 🚀 Pro Tips

Identity operators are commonly used:

- Checking for `None`
- Object comparison
- Singleton objects
- Advanced Python programming
- Frameworks like Django and Flask

---

# 🌍 Real-World Programs

## Check Login Session

```python
session = None

print(session is None)
```

Output

```text
True
```

---

## Shared Shopping Cart

```python
cart1 = ["Laptop", "Mouse"]
cart2 = cart1

print(cart1 is cart2)
```

Output

```text
True
```

---

## Compare Two Lists

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)
print(list1 is list2)
```

Output

```text
True
False
```

---

# ❓ Interview Questions

- [ ] What are identity operators?
- [ ] What is the difference between `==` and `is`?
- [ ] When should you use `is`?
- [ ] Why is `is None` recommended?
- [ ] What does `id()` return?

---

# 🏋️ Practice Programs

## Easy

```python
a = [10]
b = a

print(a is b)
```

---

```python
a = [10]
b = [10]

print(a is not b)
```

---

```python
value = None

print(value is None)
```

---

## Medium

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

---

```python
name = "Python"

print(name is not None)
```

---

## Advanced

```python
employee = {
    "id": 101,
    "name": "Saniya"
}

manager = employee

print(employee == manager)
print(employee is manager)

manager["id"] = 102

print(employee)
```

---

# 🎯 Challenge

Write a program that:

1. Creates a list called `numbers`.
2. Assigns it to another variable.
3. Creates a third list with the same values.
4. Print:
   - `numbers == second`
   - `numbers is second`
   - `numbers == third`
   - `numbers is third`

Expected Output

```text
True
True
True
False
```

---

# 📝 Assignment

- [x] Compare two lists using `==`.
- [x] Compare two lists using `is`.
- [x] Compare two variables using `is not`.
- [x] Check whether a variable is `None`.
- [x] Print the `id()` of two variables and compare them.

---

# 📚 Summary

You learned:

- ✅ `is`
- ✅ `is not`
- ✅ Difference between `==` and `is`
- ✅ Using `id()`
- ✅ Checking `None` correctly

Remember:

- `==` → compares **values**
- `is` → compares **memory identity**

---

# 🎯 Topic Completion Checklist

- [x] I understand `is`.
- [x] I understand `is not`.
- [x] I know the difference between `==` and `is`.
- [x] I know when to use `is None`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 6: Membership Operators**