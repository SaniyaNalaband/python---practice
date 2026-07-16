# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 23:** `id()` Function

**Difficulty:** ⭐⭐ Beginner to Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `id()` function is.
- [ ] Learn what an object's identity means.
- [ ] Understand how Python stores objects in memory.
- [ ] See how object IDs change.
- [ ] Understand the relationship between variables and objects.
- [ ] Avoid common misconceptions.

---

# 📖 1. What is the `id()` Function?

The `id()` function returns the **unique identity (ID)** of an object.

Syntax:

```python
id(object)
```

Example:

```python
x = 10

print(id(x))
```

Possible Output:

```
140722907183312
```

⚠️ The number will be **different on every computer and every program run**.

---

# 🤔 2. What Does the ID Represent?

The ID is a unique identifier for an object during its lifetime.

You can think of it as the object's **identity card**.

```
Object

↓

Unique ID

↓

140722907183312
```

In CPython (the most common Python implementation), this ID is related to the object's memory address.

---

# 💻 3. Basic Example

```python
x = 100

print(x)
print(id(x))
```

Possible Output:

```
100
140722907183312
```

---

# 💻 4. Two Variables Referring to the Same Object

```python
a = 50
b = a

print(id(a))
print(id(b))
```

Possible Output:

```
140722907181712
140722907181712
```

Both variables refer to the **same object**, so they have the same ID.

---

# 💻 5. Reassigning a Variable

```python
x = 10

print(id(x))

x = 20

print(id(x))
```

Possible Output:

```
140722907183312
140722907183856
```

The IDs are different because `x` now refers to a **different object**.

---

# 💻 6. Dynamic Typing and `id()`

```python
x = 10

print(type(x))
print(id(x))

x = "Python"

print(type(x))
print(id(x))
```

Possible Output:

```
<class 'int'>
140722907183312

<class 'str'>
140722907185024
```

Notice:

- The type changes.
- The ID also changes.

This is because `x` now points to a different object.

---

# 📊 7. Memory Representation

Initially:

```python
x = 10
```

```
x
│
▼
10
ID: 12345
```

Later:

```python
x = "Python"
```

```
x
│
▼
"Python"
ID: 67890
```

The variable name stays the same, but it now points to a different object.

---

# 🌍 8. Real-World Analogy

Imagine a hostel.

```
Room Number = Variable

Student = Object
```

Today:

```
Room 101 → Rahul
```

Tomorrow:

```
Room 101 → Priya
```

The room number is the same, but the person changes.

Similarly:

```
Variable = Same

Object = Changes
```

---

# ⚠️ 9. Common Mistakes

## ❌ Thinking `id()` Gives the Variable's Address

Wrong idea:

```
id(x)

↓

Address of variable
```

Correct:

```
id(x)

↓

Identity of the object that x refers to
```

---

## ❌ Expecting the Same ID Every Time

```python
print(id(10))
```

The ID may differ on another computer or another execution.

Never depend on its numeric value.

---

# 💡 10. Best Practices

✅ Use `id()` for learning and debugging.

✅ Do not write program logic based on object IDs.

---

# 🚀 11. Pro Tips

Use `id()` together with `type()`.

Example:

```python
x = 100

print(type(x))
print(id(x))
```

This tells you:

- What the object is.
- Which object it is.

---

# 🧠 Memory Trick

Remember:

```
id()

↓

Identity

↓

Unique object ID
```

Think:

> **"Every object has its own identity."**

---

# ❓ Interview Questions

- [ ] What does `id()` return?
- [ ] Is the ID the same every time a program runs?
- [ ] What happens to the ID when a variable is reassigned?
- [ ] Can two variables have the same ID?
- [ ] Why do `a` and `b` sometimes have the same ID?

---

# 🏋️ Practice Programs

## Easy

```python
x = 10

print(id(x))
```

---

```python
name = "Python"

print(id(name))
```

---

## Medium

```python
a = 100
b = a

print(id(a))
print(id(b))
```

---

```python
x = 10

print(id(x))

x = 20

print(id(x))
```

---

## Advanced

```python
data = 50

print(data, type(data), id(data))

data = 5.5

print(data, type(data), id(data))

data = "Python"

print(data, type(data), id(data))

data = True

print(data, type(data), id(data))
```

---

## Challenge

Create three variables:

```python
a = 25
b = 25
c = 30
```

Print:

- Value
- Type
- ID

Then answer:

- Which variables have the same ID?
- Why?

---

# 📝 Assignment

Complete the following:

- [x] Create a variable and print its ID.
- [x] Reassign the variable and print its new ID.
- [x] Create two variables with the same value and compare their IDs.
- [x] Print the value, type, and ID of different data types.
- [x] Explain in your own words what `id()` returns.

---

# 📚 Summary

In this lesson, you learned:

- What the `id()` function is.
- What object identity means.
- How variables refer to objects.
- Why IDs change after reassignment.
- How `id()` relates to dynamic typing.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what `id()` does.
- [x] I know what an object's identity is.
- [x] I know why IDs change.
- [x] I know that variables refer to objects.
- [x] I completed all practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 24: `type()` Function**

---

## ⭐ Quote of the Day

> **"Variables are names. Objects have identities."** 🐍