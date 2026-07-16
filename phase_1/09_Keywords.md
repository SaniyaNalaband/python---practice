# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 9:** Keywords in Python

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what keywords are.
- [ ] Know why keywords are reserved.
- [ ] Identify Python keywords.
- [ ] Avoid using keywords as variable names.
- [ ] Display all Python keywords using code.
- [ ] Solve keyword-related problems.

---

# 📖 1. Introduction

A **keyword** is a **reserved word** in Python that has a predefined meaning.

These words are part of Python's syntax and are used to perform specific tasks.

Since Python already uses these words internally, **you cannot use them as variable names, function names, or class names.**

---

# 🤔 2. Why Are Keywords Reserved?

Keywords help Python understand your program.

For example:

```python
if age >= 18:
    print("Adult")
```

Here:

- `if` is a keyword.
- Python knows that `if` starts a conditional statement.

If Python allowed you to use `if` as a variable name, it would not know whether `if` means a condition or a variable.

---

# 📚 3. Characteristics of Keywords

- They have predefined meanings.
- They are reserved by Python.
- They cannot be used as identifiers.
- They are case-sensitive.
- They are recognized by the Python Interpreter.

---

# 📝 4. List of Python Keywords

As of Python 3.12, Python has **35 keywords**.

| Keyword | Purpose |
|---------|---------|
| False | Boolean value |
| None | Represents no value |
| True | Boolean value |
| and | Logical operator |
| as | Alias |
| assert | Debugging |
| async | Asynchronous programming |
| await | Wait for async task |
| break | Exit loop |
| class | Create class |
| continue | Skip current iteration |
| def | Define function |
| del | Delete object |
| elif | Else if |
| else | Alternative block |
| except | Handle exceptions |
| finally | Always executes |
| for | Loop |
| from | Import specific items |
| global | Global variable |
| if | Conditional statement |
| import | Import module |
| in | Membership operator |
| is | Identity operator |
| lambda | Anonymous function |
| nonlocal | Outer function variable |
| not | Logical operator |
| or | Logical operator |
| pass | Empty block |
| raise | Raise exception |
| return | Return value |
| try | Exception handling |
| while | Loop |
| with | Context manager |
| yield | Generator function |

> **Note:** The exact number of keywords may change in future Python versions as the language evolves.

---

# 💻 5. Viewing Keywords in Python

Python provides the `keyword` module.

Example:

```python
import keyword

print(keyword.kwlist)
```

Output (shortened):

```text
['False', 'None', 'True', 'and', 'as', 'assert', ...]
```

To count the keywords:

```python
import keyword

print(len(keyword.kwlist))
```

---

# ❌ 6. Incorrect Usage

Trying to use a keyword as a variable:

```python
if = 10
```

Output:

```text
SyntaxError
```

---

Another example:

```python
class = "Python"
```

Output:

```text
SyntaxError
```

---

# ✅ 7. Correct Usage

Instead of:

```python
if = 10
```

Use:

```python
age = 10
```

---

Instead of:

```python
class = "BCA"
```

Use:

```python
course = "BCA"
```

---

# 🌍 8. Real-World Analogy

Imagine a school.

Words like:

- Principal
- Teacher
- Student

already have fixed meanings.

You cannot suddenly decide that **Principal** means **Library**.

Similarly, Python keywords already have predefined meanings.

---

# ⚠️ 9. Common Mistakes

### ❌ Using keywords as variables

```python
for = 5
```

---

### ❌ Wrong capitalization

```python
true
```

Correct:

```python
True
```

---

### ❌ Confusing keywords with built-in functions

Example:

```python
print()
```

`print` is **not** a keyword.

It is a **built-in function**.

---

# 💡 10. Memory Trick

Remember this sentence:

> **Keywords are reserved words that control Python's language.**

Think:

```
Keyword = Reserved Word
Identifier = Your Own Name
```

---

# 🚀 11. Best Practices

- Never use keywords as variable names.
- Use meaningful variable names.
- Use the `keyword` module if you want to check the keyword list.

---

# 📌 12. Quick Revision

| Item | Description |
|------|-------------|
| Keyword | Reserved word |
| Can be used as variable? | ❌ No |
| Can be printed? | ✅ Yes (using `keyword.kwlist`) |
| Case-sensitive? | ✅ Yes |

---

# ❓ Interview Questions

- [ ] What is a keyword?
- [ ] Why are keywords reserved?
- [ ] Can keywords be used as variable names?
- [ ] Which module displays Python keywords?
- [ ] Is `print` a keyword?
- [ ] Is `True` a keyword?
- [ ] What happens if you use `if` as a variable?

---

# 🏋️ Practice Problems

## Easy

Write a program to display all Python keywords.

---

## Easy

Write a program to count the number of Python keywords.

---

## Medium

Identify whether the following are keywords:

- `while`
- `student`
- `True`
- `print`
- `class`
- `name`

---

## Hard

Correct the following code:

```python
for = 20
print(for)
```

---

# 📝 Assignment

Complete the following:

- [x] Display all Python keywords.
- [x] Count the number of keywords.
- [x] Write five keywords used in loops and conditions.
- [x] Write five words that are **not** keywords.
- [x] Explain the difference between a keyword and an identifier in your own words.

---

# 📚 Summary

In this lesson, you learned:

- What keywords are.
- Why they are reserved.
- How to view Python keywords.
- Why keywords cannot be used as variable names.
- Common mistakes and best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what a keyword is.
- [x] I know why keywords are reserved.
- [x] I can display all Python keywords.
- [x] I can count the keywords.
- [x] I know the difference between keywords and identifiers.
- [x] I completed the practice problems.
- [x] I completed the assignment.
- [x] I answered the interview questions.

---

# 📚 Next Topic

➡️ **Topic 10: Identifiers**

---

## ⭐ Quote of the Day

> **"Keywords are Python's words. Identifiers are your words."** 🐍