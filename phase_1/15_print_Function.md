# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 15:** The `print()` Function

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `print()` function is.
- [ ] Learn the syntax of `print()`.
- [ ] Print different types of data.
- [ ] Print multiple values.
- [ ] Print variables.
- [ ] Understand string literals and expressions.
- [ ] Avoid common mistakes.
- [ ] Prepare for advanced `print()` topics like `sep` and `end`.

---

# 📖 1. What is the `print()` Function?

The `print()` function is a **built-in Python function** used to display information on the screen.

It is mainly used to:

- Show messages
- Display variable values
- Display calculation results
- Debug programs

---

# 🤔 2. Why Do We Use `print()`?

Without `print()`, your program performs operations internally, but you cannot see the results.

Example:

```python
5 + 3
```

Nothing is displayed because the result isn't printed.

Using `print()`:

```python
print(5 + 3)
```

Output:

```text
8
```

---

# 📝 3. Syntax

```python
print(object)
```

General form:

```python
print(value1, value2, value3, ...)
```

---

# 💻 4. Printing Text

Example:

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

Another example:

```python
print("Welcome to Python")
```

Output:

```text
Welcome to Python
```

---

# 🔢 5. Printing Numbers

```python
print(100)
```

Output:

```text
100
```

---

```python
print(3.14)
```

Output:

```text
3.14
```

---

# 🧮 6. Printing Expressions

Python evaluates expressions before printing them.

```python
print(10 + 5)
```

Output:

```text
15
```

---

```python
print(20 - 4)
```

Output:

```text
16
```

---

```python
print(6 * 7)
```

Output:

```text
42
```

---

```python
print(20 / 4)
```

Output:

```text
5.0
```

---

# 📦 7. Printing Variables

```python
name = "Saniya"

print(name)
```

Output:

```text
Saniya
```

---

```python
age = 20

print(age)
```

Output:

```text
20
```

---

# 📋 8. Printing Multiple Values

```python
name = "Saniya"
age = 20

print(name, age)
```

Output:

```text
Saniya 20
```

Python automatically places a space between values.

---

# 🌍 9. Real-World Example

```python
student_name = "Saniya"
course = "BCA"
marks = 89

print("Student:", student_name)
print("Course:", course)
print("Marks:", marks)
```

Output:

```text
Student: Saniya
Course: BCA
Marks: 89
```

---

# ⚠️ 10. Common Mistakes

## ❌ Forgetting Quotes

Wrong:

```python
print(Hello)
```

Error:

```text
NameError
```

Correct:

```python
print("Hello")
```

---

## ❌ Forgetting Parentheses

Wrong:

```python
print "Hello"
```

Python 3 requires parentheses.

Correct:

```python
print("Hello")
```

---

## ❌ Printing Variable Name Instead of Value

```python
age = 20

print("age")
```

Output:

```text
age
```

Correct:

```python
print(age)
```

Output:

```text
20
```

---

# 💡 11. Best Practices

✅ Use meaningful messages.

Good:

```python
print("Your total marks are:", 450)
```

Instead of:

```python
print(450)
```

---

# 🚀 12. Pro Tips

You can print different data types together.

```python
name = "Saniya"
age = 20
percentage = 89.5

print(name, age, percentage)
```

Output:

```text
Saniya 20 89.5
```

---

# 🧠 Memory Trick

Remember:

```
print()

↓
Displays information
```

Think:

> **"If you want to see it, print it!"**

---

# ❓ Interview Questions

- [ ] What is the `print()` function?
- [ ] Why do we use `print()`?
- [ ] Can `print()` display variables?
- [ ] Can `print()` display calculations?
- [ ] What happens if you forget quotation marks around text?
- [ ] What happens if you forget parentheses in Python 3?

---

# 🏋️ Practice Programs

## Easy

```python
print("Python")
```

---

```python
print(100)
```

---

```python
print(10 + 20)
```

---

## Medium

```python
name = "Saniya"

print(name)
```

---

```python
age = 20

print("Age:", age)
```

---

## Advanced

```python
name = "Saniya"
age = 20
city = "Mysuru"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

---

## Challenge

Create variables for:

- Your name
- Your age
- Your course
- Your college

Display all of them neatly using `print()`.

---

# 📝 Assignment

Complete the following:

- [x] Print your name.
- [x] Print your age.
- [x] Print your city.
- [x] Print the result of `25 + 75`.
- [x] Print three variables in one `print()` statement.
- [x] Write a program that prints your personal details.

---

# 📚 Summary

In this lesson, you learned:

- What `print()` is.
- Why `print()` is used.
- How to print text.
- How to print numbers.
- How to print variables.
- How to print expressions.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what the `print()` function is.
- [x] I can print text.
- [x] I can print numbers.
- [x] I can print variables.
- [x] I can print expressions.
- [x] I completed all practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 16: The `input()` Function**

---

## ⭐ Quote of the Day

> **"A program that cannot communicate with its user is like a conversation with only one speaker."** 🐍