# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Text (`str`) - Part 3:** String Indexing

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what indexing is.
- [ ] Access characters using positive indexes.
- [ ] Read characters one by one.
- [ ] Understand why indexing starts from 0.
- [ ] Avoid IndexError.
- [ ] Apply indexing in real programs.

---

# 📖 1. What is String Indexing?

A **string** is a sequence of characters.

Each character has a **position**, called an **index**.

Python uses these indexes to access individual characters.

Example:

```python
language = "Python"
```

Memory representation:

```text
Character :  P   y   t   h   o   n
Index     :  0   1   2   3   4   5
```

---

# 🤔 2. Why Does Indexing Start From 0?

Python follows **zero-based indexing**.

The first character is stored at position `0`, the second at `1`, and so on.

Example:

```python
word = "Code"

Character :  C   o   d   e
Index     :  0   1   2   3
```

Zero-based indexing is used in many programming languages because it maps naturally to memory locations.

---

# 💻 3. Accessing Characters

Use square brackets `[]` with the index.

```python
text = "Python"

print(text[0])
```

Output:

```text
P
```

---

```python
print(text[1])
```

Output:

```text
y
```

---

```python
print(text[2])
```

Output:

```text
t
```

---

```python
print(text[5])
```

Output:

```text
n
```

---

# 📊 4. Complete Index Table

```python
word = "Python"
```

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

Examples:

```python
print(word[0])
print(word[3])
print(word[5])
```

Output:

```text
P
h
n
```

---

# 🌍 5. Real-World Examples

Student ID

```python
student_id = "BCA2026"

print(student_id[0])
```

Output:

```text
B
```

---

Email

```python
email = "student@gmail.com"

print(email[0])
```

Output:

```text
s
```

---

Country

```python
country = "India"

print(country[2])
```

Output:

```text
d
```

---

# ⚠️ 6. IndexError

Every string has a fixed number of characters.

Example:

```python
name = "Python"
```

Indexes available:

```text
0 1 2 3 4 5
```

Trying to access index `6` causes an error.

```python
print(name[6])
```

Output:

```text
IndexError: string index out of range
```

Always make sure the index exists.

---

# 💡 7. Using len() with Indexing

The `len()` function returns the number of characters.

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```

The last valid positive index is always:

```text
len(string) - 1
```

Example:

```python
name = "Python"

print(name[len(name)-1])
```

Output:

```text
n
```

---

# ⚠️ 8. Common Mistakes

## ❌ Starting from 1

Wrong:

```python
word = "Python"

print(word[1])
```

Thinking it prints `P`.

Output:

```text
y
```

Remember:

```
First character = index 0
```

---

## ❌ Using an Invalid Index

```python
print(word[100])
```

Output:

```text
IndexError
```

---

## ❌ Using Floats

Wrong:

```python
print(word[2.5])
```

Output:

```text
TypeError
```

Indexes must be integers.

---

# 💡 9. Best Practices

✅ Use meaningful variable names.

```python
student_name = "Saniya"
```

---

✅ Use `len()` when you are not sure about the string length.

---

# 🚀 10. Pro Tips

You can store an index in a variable.

```python
word = "Python"

index = 3

print(word[index])
```

Output:

```text
h
```

---

You can also calculate indexes.

```python
print(word[1 + 2])
```

Output:

```text
h
```

Because `1 + 2 = 3`.

---

# 🧠 Memory Trick

```
Python

P  y  t  h  o  n

0  1  2  3  4  5
```

Remember:

> **The first character always starts at index `0`.**

---

# ❓ Interview Questions

- [ ] What is string indexing?
- [ ] Why does Python start indexing from 0?
- [ ] How do you access the first character?
- [ ] What error occurs when the index is out of range?
- [ ] Can indexes be floats?

---

# 🏋️ Practice Programs

## Easy

```python
name = "Python"

print(name[0])
print(name[1])
```

---

```python
city = "Mysuru"

print(city[2])
```

---

## Medium

```python
college = "OpenAI"

for i in range(len(college)):
    print(i, "->", college[i])
```

---

```python
language = "Programming"

print(language[len(language)-1])
```

---

## Advanced

```python
text = "Artificial Intelligence"

print("First Character :", text[0])
print("Middle Character:", text[len(text)//2])
print("Last Character  :", text[len(text)-1])
```

---

# 🎯 Challenge

Create a string containing your full name.

Print:

- First character
- Second character
- Third character
- Last character (using `len()`)

---

# 📝 Assignment

Complete the following:

- [x] Create three strings.
- [x] Print the first character of each.
- [x] Print the last character using `len()`.
- [x] Explain why indexing starts at 0.
- [x] Intentionally produce an `IndexError` and explain why it occurs.
---

# 📚 Summary

In this lesson, you learned:

- What string indexing is.
- How positive indexing works.
- Why indexing starts at 0.
- How to use `len()` with indexing.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I understand string indexing.
- [x] I can access characters using indexes.
- [x] I know why indexing starts at 0.
- [x] I know how to avoid `IndexError`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 4: Negative Indexing**