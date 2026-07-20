# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Text (`str`) - Part 1:** What is a String?

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what a string is.
- [ ] Learn why strings are important.
- [ ] Identify string values.
- [ ] Distinguish strings from numbers and booleans.
- [ ] Check the type of a string.

---

# 📖 1. What is a String?

A **String (`str`)** is a sequence of **characters** enclosed in quotes.

A character can be:

- A letter
- A number
- A symbol
- A space
- An emoji
- Any Unicode character

Examples:

```python
"Python"
```

```python
'Hello'
```

```python
"123"
```

```python
"Hello World"
```

```python
"😊"
```

All of these are strings.

---

# 🌍 2. Real-World Examples

Strings are everywhere.

### Student Name

```python
name = "Saniya"
```

---

### Email

```python
email = "saniya@gmail.com"
```

---

### Password

```python
password = "Python@123"
```

---

### City

```python
city = "Mysuru"
```

---

### Website

```python
website = "https://example.com"
```

---

# 💻 3. Creating Strings

Using double quotes:

```python
language = "Python"
```

Using single quotes:

```python
language = 'Python'
```

Both are valid.

---

# 📊 4. Checking the Type

```python
text = "Hello"

print(type(text))
```

Output:

```text
<class 'str'>
```

---

# 🔢 5. Numbers vs Strings

```python
a = 100
b = "100"
```

Check the type:

```python
print(type(a))
print(type(b))
```

Output:

```text
<class 'int'>
<class 'str'>
```

Even though they look similar, they are different data types.

---

# ➕ 6. Strings Can Contain Numbers

```python
roll_number = "101"
```

This is still a string because it is inside quotes.

---

# 📦 7. Empty String

A string can also be empty.

```python
name = ""
```

Check its length:

```python
print(len(name))
```

Output:

```text
0
```

---

# 💡 8. Best Practices

✅ Use meaningful variable names.

```python
student_name = "Saniya"
```

Instead of:

```python
x = "Saniya"
```

---

# ⚠️ 9. Common Mistakes

## ❌ Forgetting Quotes

Wrong:

```python
name = Python
```

Python thinks `Python` is a variable.

Correct:

```python
name = "Python"
```

---

## ❌ Confusing `"100"` with `100`

```python
"100"
```

is a string.

```python
100
```

is an integer.

---

# 🧠 Memory Trick

```
String

↓

Text

↓

Inside Quotes
```

Remember:

```
Quotes = String

No Quotes = Variable or Number
```

---

# ❓ Interview Questions

- [ ] What is a string?
- [ ] Can a string contain numbers?
- [ ] Can a string be empty?
- [ ] What is the difference between `"100"` and `100`?

---

# 🏋️ Practice Programs

## Easy

```python
name = "Saniya"

print(name)
print(type(name))
```

---

```python
city = "Mysuru"

print(city)
```

---

## Medium

```python
text1 = "123"
text2 = "Python"
text3 = ""

print(type(text1))
print(type(text2))
print(len(text3))
```

---

## Challenge

Create variables for:

- Your name
- Your college
- Your favorite programming language
- Your city

Print each variable and its type.

---

# 📝 Assignment

Complete the following:

- [x] Create five string variables.
- [x] Print their values.
- [x] Print their types.
- [x] Create an empty string.
- [x] Explain the difference between `"50"` and `50`.

---

# 📚 Summary

In this lesson, you learned:

- What a string is.
- How to create strings.
- Strings vs numbers.
- Empty strings.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what a string is.
- [x] I can create strings.
- [x] I know the difference between strings and numbers.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 2: Creating Strings**