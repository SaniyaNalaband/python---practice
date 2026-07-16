# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 10:** Identifiers in Python

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what an identifier is.
- [ ] Know the rules for naming identifiers.
- [ ] Differentiate between keywords and identifiers.
- [ ] Write valid identifiers.
- [ ] Identify invalid identifiers.
- [ ] Follow Python naming conventions (PEP 8).
- [ ] Solve identifier-related problems.

---

# 📖 1. What is an Identifier?

An **identifier** is the **name** given to a variable, function, class, module, or any other object in Python.

Simply put:

> **Identifiers are names created by programmers.**

Examples:

```python
age = 20
```

Here:

```
age
```

is an identifier.

---

Another example:

```python
student_name = "Saniya"
```

`student_name` is an identifier.

---

# 🤔 2. Why Do We Need Identifiers?

Imagine writing this:

```python
20 = 20
```

Does this tell us what the value means?

No.

Instead:

```python
age = 20
```

Now everyone understands that **20 represents age**.

Identifiers make programs:

- Easier to read
- Easier to understand
- Easier to maintain

---

# 📚 3. Rules for Naming Identifiers

Python has strict rules.

## Rule 1

An identifier can contain:

- Letters (A-Z, a-z)
- Numbers (0-9)
- Underscore (_)

Example:

```python
student
```

```python
student1
```

```python
student_name
```

---

## Rule 2

An identifier **cannot start with a number**.

❌ Wrong

```python
1student
```

✅ Correct

```python
student1
```

---

## Rule 3

No special characters.

❌ Wrong

```python
student-name
```

```python
student@name
```

```python
student#1
```

✅ Correct

```python
student_name
```

---

## Rule 4

Identifiers cannot be Python keywords.

❌ Wrong

```python
if = 10
```

```python
class = "BCA"
```

---

## Rule 5

Identifiers are **case-sensitive**.

```python
name = "Saniya"

Name = "Rahul"
```

These are two different identifiers.

---

# 📊 4. Valid Identifiers

```python
age
```

```python
student_name
```

```python
roll_number
```

```python
totalMarks
```

```python
_marks
```

```python
course2026
```

---

# ❌ 5. Invalid Identifiers

```python
1age
```

Starts with a number.

---

```python
student-name
```

Contains `-`.

---

```python
student name
```

Contains a space.

---

```python
for
```

Keyword.

---

```python
student@
```

Contains a special character.

---

# ⚙️ 6. Identifier Naming Styles

## Snake Case (Recommended)

```python
student_name
```

```python
total_marks
```

This is the Python standard (PEP 8).

---

## Camel Case

```python
studentName
```

```python
totalMarks
```

Common in Java and JavaScript.

---

## Pascal Case

```python
StudentName
```

```python
TotalMarks
```

Usually used for class names in Python.

---

# 🌍 7. Real-World Example

Imagine a classroom.

Every student has a name.

Instead of calling students:

```
Student 1
Student 2
Student 3
```

We use names like:

```
Rahul
Saniya
Ananya
```

Similarly, variables need meaningful names.

---

# ⚠️ 8. Common Mistakes

## ❌ Using Keywords

```python
while = 5
```

---

## ❌ Starting with Numbers

```python
100marks
```

---

## ❌ Using Spaces

```python
student name
```

---

## ❌ Using Special Characters

```python
student-name
```

---

# 💡 9. Best Practices

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

Good:

```python
total_marks
```

Bad:

```python
x
```

---

Use **snake_case** for variables and functions.

---

# 🚀 10. Memory Trick

Remember:

> **LNU Rule**

**L** → Letters

**N** → Numbers (not at the beginning)

**U** → Underscore

Nothing else.

---

# 📌 11. Keywords vs Identifiers

| Keywords | Identifiers |
|----------|-------------|
| Reserved by Python | Created by programmer |
| Cannot be changed | Can be any valid name |
| Have predefined meaning | Represent variables, functions, classes, etc. |
| Example: `if`, `for`, `while` | Example: `age`, `name`, `total_marks` |

---

# ❓ Interview Questions

- [ ] What is an identifier?
- [ ] What are the rules for naming identifiers?
- [ ] Can an identifier start with a number?
- [ ] Can an identifier contain spaces?
- [ ] Are identifiers case-sensitive?
- [ ] What is snake_case?
- [ ] What is the difference between keywords and identifiers?

---

# 🏋️ Practice Problems

## Easy

Which of these are valid identifiers?

```python
age
```

```python
student_name
```

```python
marks2026
```

---

## Medium

Which are invalid?

```python
1name
```

```python
student-name
```

```python
for
```

```python
student name
```

Explain why each one is invalid.

---

## Hard

Correct the following identifiers:

```python
1student
```

```python
student-name
```

```python
class
```

```python
total marks
```

Possible answers:

```python
student1
```

```python
student_name
```

```python
course_name
```

```python
total_marks
```

---

# 💼 Mini Challenge

Create identifiers for the following:

- Your name
- Your age
- Your college
- Your course
- Your city
- Your phone number
- Your percentage

Use meaningful and valid names following Python conventions.

---

# 📝 Assignment

Complete the following:

- [x] Write 10 valid identifiers.
- [x] Write 10 invalid identifiers.
- [x] Explain why each invalid identifier is incorrect.
- [x] Write five identifiers using snake_case.
- [x] Write five identifiers using camelCase.
- [x] Write five identifiers using PascalCase.
- [x] Compare keywords and identifiers in your own words.

---

# 🧠 Quick Revision

- Identifier = Name given by the programmer.
- Cannot start with a number.
- Cannot contain spaces.
- Cannot contain special characters (except `_`).
- Cannot be a keyword.
- Python identifiers are case-sensitive.
- Use **snake_case** for variables.

---

# 📚 Summary

In this lesson, you learned:

- What identifiers are.
- Rules for naming identifiers.
- Valid and invalid identifiers.
- Naming conventions.
- Difference between keywords and identifiers.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what an identifier is.
- [x] I know all naming rules.
- [x] I can identify valid and invalid identifiers.
- [x] I understand snake_case, camelCase, and PascalCase.
- [x] I know the difference between keywords and identifiers.
- [x] I completed all practice problems.
- [x] I completed the assignment.
- [x] I answered the interview questions.

---

# 📚 Next Topic

➡️ **Topic 11: Variables**

---

## ⭐ Quote of the Day

> **"Good programmers choose meaningful names. Great programmers choose meaningful names consistently."** 🐍