# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 22:** Dynamic Typing

**Difficulty:** ⭐⭐ Beginner to Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what dynamic typing is.
- [ ] Learn how Python assigns data types.
- [ ] Compare dynamic typing with static typing.
- [ ] Change a variable's type during execution.
- [ ] Understand the advantages and disadvantages of dynamic typing.
- [ ] Avoid common beginner mistakes.

---

# 📖 1. What is Dynamic Typing?

**Dynamic Typing** means **you do not need to declare the data type of a variable.**

Python automatically determines the variable's type based on the value you assign.

Example:

```python
age = 20
```

Python automatically understands that:

```
age → int
```

Another example:

```python
name = "Saniya"
```

Python automatically understands:

```
name → str
```

You never wrote:

```python
int age = 20
```

or

```python
String name = "Saniya"
```

That's why Python is called a **dynamically typed language**.

---

# 🤔 2. Why is it Called "Dynamic"?

The word **dynamic** means **changing while the program is running**.

In Python, a variable can store different types of values at different times.

Example:

```python
x = 10

print(x)
print(type(x))
```

Output:

```
10
<class 'int'>
```

Now change it:

```python
x = "Python"

print(x)
print(type(x))
```

Output:

```
Python
<class 'str'>
```

The **same variable** now stores a **different data type**.

---

# 💻 3. More Examples

### Integer → Float

```python
value = 100

print(type(value))

value = 99.5

print(type(value))
```

Output:

```
<class 'int'>
<class 'float'>
```

---

### Float → String

```python
price = 250.50

print(type(price))

price = "Two Hundred Fifty"

print(type(price))
```

Output:

```
<class 'float'>
<class 'str'>
```

---

### String → Boolean

```python
status = "Active"

print(type(status))

status = True

print(type(status))
```

Output:

```
<class 'str'>
<class 'bool'>
```

---

# 📊 4. Memory Representation

Initially:

```python
x = 10
```

```
x
│
▼
10
(int)
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
(str)
```

The variable name stays the same, but it now refers to a different object.

---

# ⚖️ 5. Dynamic Typing vs Static Typing

| Dynamic Typing (Python) | Static Typing (C, C++, Java) |
|--------------------------|------------------------------|
| Type is decided automatically | Type must be declared |
| Variable type can change | Variable type cannot change |
| Less code | More code |
| Easier for beginners | More strict |

---

### Python

```python
x = 10
x = "Hello"
x = 5.5
```

Valid ✅

---

### C++

```cpp
int x = 10;
x = "Hello";
```

Invalid ❌

The compiler reports an error because `x` is declared as an integer.

---

# 🌍 6. Real-World Example

Imagine a box.

Today it stores books.

Tomorrow it stores clothes.

Next week it stores toys.

The **box is the variable**, and the **items inside are the values**.

Python allows the contents to change freely.

---

# 💡 7. Advantages of Dynamic Typing

✅ Easy to write.

✅ Less code.

✅ Faster development.

✅ Flexible.

✅ Great for rapid prototyping.

Example:

```python
user = "Saniya"
user = 25
user = True
```

All are valid.

---

# ⚠️ 8. Disadvantages of Dynamic Typing

Because variables can change type, mistakes may appear only when the program runs.

Example:

```python
number = "10"

print(number + 5)
```

Output:

```
TypeError
```

The variable is now a string, not an integer.

---

# 🚫 9. Common Mistakes

## ❌ Assuming a Variable Keeps Its Old Type

```python
x = 100
x = "Hundred"

print(x + 10)
```

Output:

```
TypeError
```

---

## ❌ Forgetting to Check the Type

```python
value = input("Enter a number: ")

print(value + 10)
```

`input()` returns a string.

Convert it first:

```python
value = int(input("Enter a number: "))

print(value + 10)
```

---

# 💻 10. Using `type()`

Use `type()` to check the current data type.

```python
x = 25

print(type(x))
```

Output:

```
<class 'int'>
```

---

```python
x = "Python"

print(type(x))
```

Output:

```
<class 'str'>
```

---

# 🚀 11. Pro Tips

Even though Python allows changing a variable's type, it's usually better to keep a variable's purpose consistent.

Instead of:

```python
data = 10
data = "Python"
data = True
```

Use meaningful variable names:

```python
age = 20
language = "Python"
is_logged_in = True
```

This makes your code easier to read and maintain.

---

# 🧠 Memory Trick

Remember:

```
Dynamic Typing

↓

Python decides the type.

↓

The variable's type can change.
```

Think:

> **"Same variable, different types."**

---

# ❓ Interview Questions

- [ ] What is dynamic typing?
- [ ] Why is Python called a dynamically typed language?
- [ ] Can a variable change its type in Python?
- [ ] What is the difference between dynamic and static typing?
- [ ] How do you check a variable's type?

---

# 🏋️ Practice Programs

## Easy

```python
x = 10
print(type(x))
```

---

```python
x = "Python"
print(type(x))
```

---

## Medium

```python
value = 100

print(type(value))

value = 5.5

print(type(value))
```

---

## Advanced

```python
data = 10
print(data, type(data))

data = "Hello"
print(data, type(data))

data = True
print(data, type(data))

data = 3.14
print(data, type(data))
```

---

## Challenge

Create one variable named `info`.

Store these values one after another and print the value and its type each time:

- Your name
- Your age
- Your height
- `True`

---

# 📝 Assignment

Complete the following:

- [x] Create a variable and store an integer.
- [x] Change it into a string.
- [x] Change it into a float.
- [x] Change it into a Boolean.
- [x] Print the value and type after each change.
- [x] Write the difference between dynamic typing and static typing.

---

# 📚 Summary

In this lesson, you learned:

- What dynamic typing is.
- Why Python is dynamically typed.
- How variable types can change.
- Advantages and disadvantages.
- Dynamic typing vs static typing.
- Common mistakes and best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what dynamic typing is.
- [x] I know why Python is dynamically typed.
- [x] I can change a variable's type.
- [x] I know the difference between dynamic and static typing.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 23: `id()` Function**

---

## ⭐ Quote of the Day

> **"In Python, variables don't have fixed types—objects do."** 🐍