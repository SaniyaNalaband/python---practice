# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 8:** Indentation in Python

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what indentation is.
- [ ] Know why indentation is important in Python.
- [ ] Write properly indented Python code.
- [ ] Identify indentation errors.
- [ ] Follow Python's indentation rules.
- [ ] Understand code blocks.
- [ ] Solve indentation-related practice problems.

---

# 📖 1. Introduction

**Indentation** means leaving spaces (or a tab) at the beginning of a line of code.

In many programming languages, indentation is only used to make code look neat.

**Python is different.**

In Python, indentation tells the interpreter which statements belong together.

Without proper indentation, Python cannot understand your program.

---

# 🤔 2. Why is Indentation Important?

Python uses indentation to define **blocks of code**.

Instead of using curly braces `{}` like C, C++, or Java, Python uses indentation.

Example:

```python
if True:
    print("Hello")
```

The four spaces before `print()` tell Python that it belongs to the `if` block.

---

# 🧠 3. What is a Code Block?

A **code block** is a group of statements that belong together.

Example:

```python
if True:
    print("Welcome")
    print("Python")
    print("Course")
```

All three `print()` statements are inside the same block because they have the same indentation.

---

# ⚙️ 4. Python Indentation Rules

### Rule 1

Use **4 spaces** for each indentation level.

PEP 8 (Python's official style guide) recommends **4 spaces**.

Example:

```python
if True:
    print("Correct")
```

---

### Rule 2

All statements in the same block must have the same indentation.

Correct:

```python
if True:
    print("Line 1")
    print("Line 2")
```

Incorrect:

```python
if True:
    print("Line 1")
       print("Line 2")
```

---

### Rule 3

Never mix **tabs** and **spaces** in the same program.

Choose one style.

Professional developers use **4 spaces**.

VS Code automatically inserts spaces when you press the **Tab** key.

---

# 💻 5. Examples

## Example 1

```python
if True:
    print("Hello")
```

Output:

```text
Hello
```

---

## Example 2

```python
if True:
    print("Python")
    print("Programming")
```

Output:

```text
Python
Programming
```

---

## Example 3

```python
if True:
    print("Line 1")
    print("Line 2")
    print("Line 3")
```

Output:

```text
Line 1
Line 2
Line 3
```

---

# 📊 6. Visual Representation

```
if True:
│
├── print("Hello")
├── print("Python")
└── print("Course")
```

All statements belong to the same block.

---

# 🌍 7. Real-World Example

Imagine a classroom.

Teacher says:

```
If the bell rings,
    Students leave.
    Teacher closes the classroom.
```

Both actions happen only if the bell rings.

Similarly:

```python
if bell_rings:
    students_leave()
    teacher_closes_room()
```

The indentation shows that both actions belong to the same condition.

---

# ⚠️ 8. Common Errors

## ❌ Error 1: Missing Indentation

```python
if True:
print("Hello")
```

Output:

```text
IndentationError: expected an indented block
```

Correct:

```python
if True:
    print("Hello")
```

---

## ❌ Error 2: Inconsistent Indentation

```python
if True:
    print("One")
        print("Two")
```

Output:

```text
IndentationError
```

Correct:

```python
if True:
    print("One")
    print("Two")
```

---

## ❌ Error 3: Mixing Tabs and Spaces

Avoid mixing tabs and spaces.

Always use **4 spaces**.

---

# 💡 9. Best Practices

✅ Use **4 spaces** for every indentation level.

✅ Let VS Code handle indentation automatically.

✅ Keep indentation consistent throughout your program.

✅ Never mix tabs and spaces.

---

# 🚀 10. Pro Tips

- Press **Tab** in VS Code to indent.
- Press **Shift + Tab** to remove one indentation level.
- Enable **Format on Save** in VS Code to keep code neatly formatted.

---

# 📌 11. Quick Revision

| Term | Meaning |
|------|---------|
| Indentation | Spaces at the beginning of a line |
| Code Block | Group of related statements |
| Standard Indentation | 4 Spaces |
| Error | `IndentationError` |

---

# ❓ Interview Questions

- [ ] What is indentation?
- [ ] Why is indentation important in Python?
- [ ] How many spaces are recommended?
- [ ] What is a code block?
- [ ] What happens if indentation is missing?
- [ ] Can tabs and spaces be mixed?
- [ ] Which error is raised for incorrect indentation?

---

# 🏋️ Practice Programs

## Easy

```python
if True:
    print("Python")
```

---

## Easy

```python
if True:
    print("Line 1")
    print("Line 2")
```

---

## Medium

```python
if True:
    print("Welcome")
    print("to")
    print("Python")
print("Outside the block")
```

Observe which statement is inside the `if` block and which is outside.

---

## Hard

Fix the following program:

```python
if True:
print("A")
 print("B")
```

Expected Output:

```text
A
B
```

---

# 📝 Assignment

Complete the following:

- [x] Write a program with one correctly indented `if` block.
- [x] Write a program with three statements inside the same block.
- [x] Intentionally create an `IndentationError` and observe the error message.
- [x] Correct the error and run the program again.
- [x] Explain in your own words why indentation is required in Python.

---

# 📚 Summary

In this lesson, you learned:

- What indentation is.
- Why Python uses indentation.
- What code blocks are.
- Python's indentation rules.
- Common indentation errors.
- Best practices for writing readable Python code.

---

# 🎯 Topic Completion Checklist

- [x] I understand what indentation is.
- [x] I know why Python uses indentation.
- [x] I can write properly indented code.
- [x] I know what a code block is.
- [x] I can identify and fix `IndentationError`.
- [x] I completed all practice programs.
- [x] I completed the assignment.
- [x] I answered the interview questions.

---

# 📚 Next Topic

➡️ **Topic 9: Keywords in Python**

---

## ⭐ Quote of the Day

> **"Indentation is not decoration in Python—it is part of the language."** 🐍