# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 11:** Variables in Python

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a variable is.
- [ ] Learn why variables are used.
- [ ] Assign values to variables.
- [ ] Understand Python's dynamic typing.
- [ ] Learn variable naming conventions.
- [ ] Understand how variables are stored in memory.
- [ ] Write Python programs using variables.
- [ ] Avoid common beginner mistakes.

---

# 📖 1. What is a Variable?

A **variable** is a **named storage location** that holds a value.

Think of a variable as a **labeled box**.

The **label** is the variable's name, and the **box** stores the value.

Example:

```python
age = 20
```

Here:

- `age` → Variable name (identifier)
- `=` → Assignment operator
- `20` → Value

---

# 🤔 2. Why Do We Need Variables?

Imagine printing your age without a variable:

```python
print(20)
```

If your age changes, you have to change the value everywhere.

Instead:

```python
age = 20
print(age)
```

Later, if your age changes:

```python
age = 21
```

Only one place needs updating.

Variables make programs:

- Easy to read
- Easy to modify
- Easy to reuse

---

# 📦 3. How Variables Work (Memory Concept)

When you write:

```python
age = 20
```

Python stores the value in memory and links the name `age` to it.

```
RAM

+---------+
|   20    |
+---------+
     ▲
     │
    age
```

The variable doesn't contain the value itself—it refers to the value stored in memory.

---

# ⚙️ 4. Variable Assignment

General syntax:

```python
variable_name = value
```

Examples:

```python
name = "Saniya"
```

```python
age = 20
```

```python
height = 5.4
```

```python
is_student = True
```

---

# 💻 5. Printing Variables

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

# 🔄 6. Changing Variable Values

Variables can change during program execution.

```python
age = 20

print(age)

age = 21

print(age)
```

Output:

```text
20
21
```

---

# 🧠 7. Dynamic Typing

Python is **dynamically typed**.

This means you do **not** declare the data type.

Example:

```python
x = 10
```

Later:

```python
x = "Python"
```

Even later:

```python
x = True
```

Python automatically understands the type.

---

# 🌍 8. Real-World Example

Imagine a student's information.

```python
student_name = "Saniya"
age = 20
college = "ABC College"
percentage = 89.5
```

Now display it:

```python
print(student_name)
print(age)
print(college)
print(percentage)
```

---

# 📌 9. Multiple Variable Assignment

Python allows assigning multiple variables in one line.

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

---

# 📌 10. Assigning the Same Value

```python
x = y = z = 100

print(x)
print(y)
print(z)
```

Output:

```text
100
100
100
```

---

# ⚠️ 11. Common Mistakes

## ❌ Using a Variable Before Creating It

```python
print(age)
```

Output:

```text
NameError
```

Correct:

```python
age = 20
print(age)
```

---

## ❌ Using Quotes Around the Variable Name

Wrong:

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

## ❌ Invalid Variable Name

```python
1age = 20
```

Error:

```text
SyntaxError
```

---

# 💡 12. Best Practices

✅ Use meaningful names.

Good:

```python
student_name
```

Bad:

```python
a
```

---

Use `snake_case` for variable names.

Example:

```python
total_marks
```

---

Avoid names like:

```python
x1
abc
temp123
```

unless their purpose is obvious.

---

# 🚀 13. Pro Tips

Use descriptive names.

Instead of:

```python
a = 50000
```

Write:

```python
employee_salary = 50000
```

Your future self (and teammates) will thank you.

---

# 📊 14. Variable Memory Diagram

```python
name = "Saniya"
age = 20
```

```
RAM

+----------------+
| "Saniya"       |
+----------------+
        ▲
        │
      name

+----------------+
|      20        |
+----------------+
        ▲
        │
       age
```

---

# ❓ Interview Questions

- [ ] What is a variable?
- [ ] Why are variables used?
- [ ] What is dynamic typing?
- [ ] Can a variable's value change?
- [ ] What does the assignment operator (`=`) do?
- [ ] What happens if you use a variable before assigning a value?

---

# 🏋️ Practice Programs

## Easy

```python
name = "Saniya"

print(name)
```

---

```python
age = 20

print(age)
```

---

## Medium

```python
city = "Mysuru"
country = "India"

print(city)
print(country)
```

---

```python
x = 10

print(x)

x = 50

print(x)
```

---

## Advanced

```python
name = "Saniya"
age = 20
college = "ABC College"
course = "BCA"

print("Name:", name)
print("Age:", age)
print("College:", college)
print("Course:", course)
```

---

## Challenge

Create variables for:

- Your name
- Your age
- Your college
- Your course
- Your city
- Your state
- Your country
- Your favorite programming language

Then print all of them.

---

# 📝 Assignment

Complete the following:

- [x] Create five variables of your choice.
- [x] Change the value of a variable and print it before and after the change.
- [x] Use multiple assignment.
- [x] Assign one value to three variables.
- [x] Explain variables in your own words.

---

# 🧠 Quick Revision

- Variable = Named storage location.
- Created using `=`.
- Can store different types of values.
- Python is dynamically typed.
- Variable names should be meaningful.
- Use `snake_case`.

---

# 📚 Summary

In this lesson, you learned:

- What variables are.
- Why variables are important.
- Assignment operator.
- Dynamic typing.
- Memory concept.
- Multiple assignment.
- Best practices.
- Common mistakes.

---

# 🎯 Topic Completion Checklist

- [x] I know what a variable is.
- [x] I know how to create variables.
- [x] I understand the assignment operator.
- [x] I understand dynamic typing.
- [x] I know how Python stores variables.
- [x] I completed all practice programs.
- [x] I completed the assignment.
- [x] I answered the interview questions.

---

# 📚 Next Topic

➡️ **Topic 12: Data Types in Python**

---

## ⭐ Quote of the Day

> **"Variables are the containers that give meaning to your data."** 🐍