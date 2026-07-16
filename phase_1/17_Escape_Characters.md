# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 17:** Escape Characters

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what escape characters are.
- [ ] Learn why escape characters are used.
- [ ] Use the most common escape characters.
- [ ] Print formatted text.
- [ ] Print quotation marks correctly.
- [ ] Print file paths correctly.
- [ ] Avoid common mistakes.

---

# 📖 1. What are Escape Characters?

An **escape character** is a special character that begins with a **backslash (`\`)**.

It tells Python to perform a special action instead of printing the character normally.

Example:

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

Here,

```
\n
```

doesn't print `\n`.

Instead, it tells Python to move to the **next line**.

---

# 🤔 2. Why Do We Need Escape Characters?

Imagine writing:

```python
print("Hello
World")
```

Python will produce an error because strings cannot span multiple lines like that.

Instead:

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

Escape characters help us format text inside a string.

---

# 📚 3. Common Escape Characters

| Escape Character | Meaning |
|-----------------|---------|
| `\n` | New Line |
| `\t` | Horizontal Tab |
| `\\` | Backslash |
| `\'` | Single Quote |
| `\"` | Double Quote |
| `\b` | Backspace |
| `\r` | Carriage Return |

---

# 🔹 4. New Line (`\n`)

Moves the cursor to the next line.

Example:

```python
print("Python\nJava\nC++")
```

Output:

```
Python
Java
C++
```

---

# 🔹 5. Tab (`\t`)

Creates a horizontal tab space.

Example:

```python
print("Name\tAge")
print("Saniya\t20")
```

Output:

```
Name    Age
Saniya  20
```

---

# 🔹 6. Backslash (`\\`)

To print a backslash, use two backslashes.

Example:

```python
print("C:\\Users\\Saniya")
```

Output:

```
C:\Users\Saniya
```

---

# 🔹 7. Double Quotes (`\"`)

Print double quotation marks inside a string.

Example:

```python
print("He said, \"Python is awesome!\"")
```

Output:

```
He said, "Python is awesome!"
```

---

# 🔹 8. Single Quotes (`\'`)

Print a single quotation mark.

Example:

```python
print('It\'s a beautiful day.')
```

Output:

```
It's a beautiful day.
```

---

# 🔹 9. Backspace (`\b`)

Removes the character before it.

Example:

```python
print("AB\bC")
```

Possible Output:

```
AC
```

(Some terminals may display this differently.)

---

# 🔹 10. Carriage Return (`\r`)

Moves the cursor back to the beginning of the line.

Example:

```python
print("Hello\rHi")
```

Possible Output:

```
Hillo
```

or

```
Hi
```

The exact result depends on the terminal.

---

# 🌍 11. Real-World Examples

### Printing an Address

```python
print("Name : Saniya\nCity : Mysuru\nState : Karnataka")
```

Output:

```
Name : Saniya
City : Mysuru
State : Karnataka
```

---

### Printing a Table

```python
print("Name\tCourse\tMarks")
print("Saniya\tBCA\t89")
```

Output:

```
Name    Course  Marks
Saniya  BCA     89
```

---

### Printing a Windows Path

```python
print("C:\\Program Files\\Python")
```

Output:

```
C:\Program Files\Python
```

---

# ⚠️ 12. Common Mistakes

## ❌ Forgetting to Escape Quotes

Wrong:

```python
print("He said "Hello"")
```

Correct:

```python
print("He said \"Hello\"")
```

---

## ❌ Using a Single Backslash in Windows Paths

Wrong:

```python
print("C:\Users\Saniya")
```

This can produce unexpected results because `\U` starts a Unicode escape.

Correct:

```python
print("C:\\Users\\Saniya")
```

---

# 💡 13. Best Practices

✅ Use `\n` for readable multi-line output.

✅ Use `\t` for simple tables.

✅ Escape quotes only when needed.

✅ Use `\\` when printing Windows file paths.

---

# 🚀 14. Pro Tips

Python also supports **raw strings**, which we'll learn later.

Example:

```python
r"C:\Users\Saniya"
```

Raw strings treat backslashes as normal characters.

---

# 🧠 Memory Trick

Remember:

```
\n  → New Line

\t  → Tab

\\  → Backslash

\"  → Double Quote

\'  → Single Quote
```

Think:

> **`\` = Special Action Begins**

---

# ❓ Interview Questions

- [ ] What is an escape character?
- [ ] Why do we use escape characters?
- [ ] What does `\n` do?
- [ ] What does `\t` do?
- [ ] How do you print a backslash?
- [ ] How do you print quotation marks inside a string?

---

# 🏋️ Practice Programs

## Easy

```python
print("Hello\nWorld")
```

---

```python
print("Python\tJava\tC++")
```

---

```python
print("It's a beautiful day.")
```

---

## Medium

```python
print("She said, \"Good Morning!\"")
```

---

```python
print("C:\\Users\\Saniya\\Desktop")
```

---

## Advanced

```python
print("Student Details")
print("--------------")
print("Name\t: Saniya")
print("Age\t: 20")
print("City\t: Mysuru")
```

---

## Challenge

Write a program that prints the following:

```
***************
Student Details
***************
Name    : Your Name
Age     : Your Age
City    : Your City
Course  : Your Course
***************
```

Use `\n` and `\t` wherever appropriate.

---

# 📝 Assignment

Complete the following:

- [x] Print your address on three different lines.
- [x] Create a table using `\t`.
- [x] Print a Windows file path.
- [x] Print a sentence containing both single and double quotes.
- [x] Explain the purpose of `\n` and `\t` in your own words.

---

# 📚 Summary

In this lesson, you learned:

- What escape characters are.
- Why they are useful.
- Common escape characters.
- Real-world uses.
- Best practices.
- Common mistakes.

---

# 🎯 Topic Completion Checklist

- [x] I know what escape characters are.
- [x] I can use `\n`.
- [x] I can use `\t`.
- [x] I can print quotes correctly.
- [x] I can print Windows paths correctly.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 18: Multiple Print Methods**

---

## ⭐ Quote of the Day

> **"Small characters like `\n` and `\t` make a big difference in making your output readable."** 🐍