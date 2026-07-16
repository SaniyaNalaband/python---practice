# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 25:** Memory Basics

**Difficulty:** ⭐⭐⭐ Beginner to Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand how Python stores objects in memory.
- [ ] Learn the difference between variables and objects.
- [ ] Understand references.
- [ ] Learn what happens during assignment and reassignment.
- [ ] Understand object sharing.
- [ ] Connect memory concepts with `id()` and `type()`.

---

# 📖 1. What is Memory?

Memory (RAM) is where Python stores your program's data while it is running.

When you create a variable:

```python
x = 10
```

Python stores the integer object `10` in memory.

---

# 🧠 2. Variables Do Not Store Values

Many beginners think:

```
Variable
↓

Stores value
```

A better way to think in Python is:

```
Variable
↓

Reference

↓

Object

↓

Memory
```

Example:

```python
x = 10
```

```
x
│
▼
10
```

`x` is just a **name** pointing to the integer object `10`.

---

# 💻 3. Assignment

```python
a = 100
```

Python performs these steps:

1. Creates the integer object `100` (or reuses it if it already exists).
2. Makes `a` refer to that object.

---

# 💻 4. Two Variables, One Object

```python
a = 50
b = a

print(id(a))
print(id(b))
```

Possible Output:

```
140562930456240
140562930456240
```

Both variables refer to the **same object**.

Memory view:

```
a ─┐
   │
   ▼
  50
   ▲
   │
b ─┘
```

---

# 💻 5. Reassignment

```python
x = 10

print(id(x))

x = 20

print(id(x))
```

Possible Output:

```
140562930456000
140562930456144
```

Python does **not** change the object `10`.

Instead:

- `x` stops referring to `10`.
- `x` starts referring to `20`.

Memory view:

Before:

```
x
│
▼
10
```

After:

```
10

x
│
▼
20
```

---

# 💻 6. Dynamic Typing and Memory

```python
data = 100

print(type(data))
print(id(data))

data = "Python"

print(type(data))
print(id(data))
```

Possible Output:

```
<class 'int'>
140562930456240

<class 'str'>
140562930457104
```

The variable name stays the same.

The object changes.

---

# 💻 7. Immutable Objects

Numbers and strings are **immutable**.

Immutable means:

> **Their value cannot be changed after they are created.**

Example:

```python
x = 10

x = x + 5
```

Python does **not** change the object `10`.

Instead:

1. Creates a new object `15`.
2. Makes `x` refer to it.

---

# 💻 8. Object Sharing

```python
a = 100
b = 100

print(id(a))
print(id(b))
```

Possible Output:

```
140562930456240
140562930456240
```

Python may reuse the same object for efficiency.

This is called **object sharing**.

---

# 🌍 9. Real-World Analogy

Imagine a house.

```
House = Object

Name Plate = Variable
```

Initially:

```
House A

Name Plate:
Saniya
```

Later:

```
House B

Name Plate:
Saniya
```

The **name plate** moved.

The **house didn't change**.

Variables work the same way.

---

# ⚠️ 10. Common Mistakes

## ❌ Thinking Variables Contain Values

Wrong idea:

```
x contains 10
```

Better idea:

```
x refers to the object 10
```

---

## ❌ Thinking `x = x + 1` Changes the Old Integer

```python
x = 5

x = x + 1
```

Python creates a new integer object `6`.

The object `5` remains unchanged.

---

# 💡 11. Best Practices

✅ Think of variables as **references**, not containers.

✅ Use `id()` to observe object identity.

✅ Use `type()` to observe object type.

---

# 🚀 12. Pro Tips

Use all three together:

```python
x = 50

print("Value :", x)
print("Type  :", type(x))
print("ID    :", id(x))
```

Possible Output:

```
Value : 50
Type  : <class 'int'>
ID    : 140562930456240
```

This gives a complete picture of the object.

---

# 🧠 Memory Trick

Remember:

```
Variable

↓

Reference

↓

Object

↓

Memory
```

Not:

```
Variable

↓

Value
```

---

# ❓ Interview Questions

- [ ] What is memory in Python?
- [ ] Do variables store values?
- [ ] What is a reference?
- [ ] What happens during reassignment?
- [ ] Why can two variables have the same `id()`?
- [ ] What are immutable objects?

---

# 🏋️ Practice Programs

## Easy

```python
x = 10

print(x)
print(type(x))
print(id(x))
```

---

```python
a = 50
b = a

print(id(a))
print(id(b))
```

---

## Medium

```python
x = 10

print(id(x))

x = 20

print(id(x))
```

---

```python
data = "Python"

print(type(data))
print(id(data))

data = 99

print(type(data))
print(id(data))
```

---

## Advanced

```python
a = 100
b = a

print("a:", a, type(a), id(a))
print("b:", b, type(b), id(b))

a = 200

print()

print("After changing a")

print("a:", a, type(a), id(a))
print("b:", b, type(b), id(b))
```

---

## Challenge

Predict the output before running:

```python
x = 25
y = x

print(id(x))
print(id(y))

y = 30

print(id(x))
print(id(y))
```

Explain why the IDs change.

---

# 📝 Assignment

Complete the following:

- [ ] Create one variable and print its value, type, and ID.
- [ ] Create another variable referring to the same object.
- [ ] Reassign one variable.
- [ ] Observe the IDs before and after.
- [ ] Explain the concept of references in your own words.

---

# 📚 Summary

In this lesson, you learned:

- What memory is.
- How Python stores objects.
- Variables are references.
- Assignment and reassignment.
- Object sharing.
- Immutable objects.
- How `id()` and `type()` help understand memory.

---

# 🎯 Topic Completion Checklist

- [x] I understand memory basics.
- [x] I know that variables are references.
- [x] I understand assignment and reassignment.
- [x] I know why IDs change.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 🎉 Phase 1 Completed!

You have successfully completed:

- [x] 1. What is Python?
- [x] 2. Installing Python
- [x] 3. Installing VS Code
- [x] 4. Running Python Programs
- [x] 5. Python Interactive Shell (REPL)
- [x] 6. Writing Your First Program
- [x] 7. Comments
- [x] 8. Indentation
- [x] 9. Keywords
- [x] 10. Identifiers
- [x] 11. Variables
- [x] 12. Rules for Naming Variables
- [x] 13. Constants
- [x] 14. Input and Output
- [x] 15. `print()` Function
- [x] 16. `input()` Function
- [x] 17. Escape Characters
- [x] 18. Multiple Print Methods
- [x] 19. `sep` and `end`
- [x] 20. Type Conversion
- [x] 21. Type Casting
- [x] 22. Dynamic Typing
- [x] 23. `id()` Function
- [x] 24. `type()` Function
- [x] 25. Memory Basics

---

# 🚀 Next Phase

➡️ **Phase 2: Python Operators**

We'll study every operator in depth:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Operator Precedence
9. Expressions
10. Short-Circuit Evaluation

---

## ⭐ Quote of the Day

> **"Understanding memory is the difference between writing Python code and truly understanding how Python works."** 🐍