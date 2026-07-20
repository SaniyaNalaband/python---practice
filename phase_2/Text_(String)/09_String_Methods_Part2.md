# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Text (`str`) - Part 10:** String Methods – Searching & Counting

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Search for text using `find()`.
- [ ] Search from the end using `rfind()`.
- [ ] Understand `index()` and `rindex()`.
- [ ] Count occurrences using `count()`.
- [ ] Check prefixes using `startswith()`.
- [ ] Check suffixes using `endswith()`.

---

# 📖 1. `find()`

Returns the **index of the first occurrence** of a substring.

If not found, it returns **-1**.

```python
text = "Python Programming"

print(text.find("P"))
```

Output:

```text
0
```

---

```python
print(text.find("Programming"))
```

Output:

```text
7
```

---

```python
print(text.find("Java"))
```

Output:

```text
-1
```

---

# 📖 2. `rfind()`

Returns the **last occurrence** of a substring.

```python
text = "banana"

print(text.rfind("a"))
```

Output:

```text
5
```

---

```python
print(text.rfind("n"))
```

Output:

```text
4
```

---

# 📖 3. `index()`

Works like `find()` **except**:

If the substring is not found, it raises a **ValueError**.

```python
text = "Python"

print(text.index("t"))
```

Output:

```text
2
```

---

```python
print(text.index("z"))
```

Output:

```text
ValueError: substring not found
```

---

# 📖 4. `rindex()`

Returns the **last occurrence**.

Raises **ValueError** if not found.

```python
text = "banana"

print(text.rindex("a"))
```

Output:

```text
5
```

---

# 📖 5. `count()`

Counts how many times a substring appears.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

```python
print(text.count("na"))
```

Output:

```text
2
```

---

```python
print(text.count("z"))
```

Output:

```text
0
```

---

# 📖 6. `startswith()`

Checks whether the string starts with a given substring.

Returns `True` or `False`.

```python
text = "Python Programming"

print(text.startswith("Python"))
```

Output:

```text
True
```

---

```python
print(text.startswith("Java"))
```

Output:

```text
False
```

---

# 📖 7. `endswith()`

Checks whether the string ends with a given substring.

```python
file = "notes.pdf"

print(file.endswith(".pdf"))
```

Output:

```text
True
```

---

```python
print(file.endswith(".txt"))
```

Output:

```text
False
```

---

# 🌍 Real-World Examples

## Email Validation

```python
email = "student@gmail.com"

print(email.endswith(".com"))
```

Output:

```text
True
```

---

## File Type

```python
filename = "project.py"

print(filename.endswith(".py"))
```

Output:

```text
True
```

---

## URL Check

```python
url = "https://openai.com"

print(url.startswith("https"))
```

Output:

```text
True
```

---

# ⚠️ Common Mistakes

## ❌ Confusing `find()` and `index()`

```python
text = "Python"

print(text.find("z"))
```

Output:

```text
-1
```

---

```python
print(text.index("z"))
```

Output:

```text
ValueError
```

Remember:

| Method | If Not Found |
|---------|--------------|
| `find()` | Returns `-1` |
| `index()` | Raises `ValueError` |

---

## ❌ Case Sensitivity

```python
text = "Python"

print(text.find("python"))
```

Output:

```text
-1
```

Use:

```python
print(text.lower().find("python"))
```

Output:

```text
0
```

---

# 💡 Best Practices

✅ Use `find()` if the text may not exist.

✅ Use `index()` only when you're sure it exists.

✅ Use `startswith()` and `endswith()` instead of slicing when checking prefixes and suffixes.

---

# 🚀 Pro Tips

Search from a specific position:

```python
text = "banana"

print(text.find("a", 2))
```

Output:

```text
3
```

Count within a range:

```python
text = "banana"

print(text.count("a", 2, 6))
```

Output:

```text
2
```

---

# 🧠 Memory Trick

```
find()

↓

First occurrence

↓

Returns -1 if missing

--------------------

index()

↓

First occurrence

↓

Raises Error if missing

--------------------

count()

↓

How many?

--------------------

startswith()

↓

Beginning

--------------------

endswith()

↓

Ending
```

---

# ❓ Interview Questions

- [ ] What is the difference between `find()` and `index()`?
- [ ] What does `count()` return?
- [ ] What does `startswith()` return?
- [ ] What happens if `index()` doesn't find the substring?
- [ ] Is `find()` case-sensitive?

---

# 🏋️ Practice Programs

## Easy

```python
text = "banana"

print(text.find("a"))
print(text.count("a"))
```

---

```python
text = "Python"

print(text.startswith("Py"))
print(text.endswith("on"))
```

---

## Medium

```python
sentence = "Python Programming"

print(sentence.find("Programming"))
print(sentence.index("P"))
print(sentence.rfind("m"))
```

---

## Advanced

```python
filename = "report.pdf"

print("Starts with rep :", filename.startswith("rep"))
print("Ends with pdf   :", filename.endswith(".pdf"))
print("Count of p      :", filename.count("p"))
print("Find 'o'        :", filename.find("o"))
print("Last 'p'        :", filename.rfind("p"))
```

---

# 🎯 Challenge

Create a string:

```python
text = "Artificial Intelligence"
```

Print:

- Position of `"I"`
- Position of `"g"`
- Number of `"i"`
- Does it start with `"Art"`?
- Does it end with `"ence"`?

---

# 📝 Assignment

- [x] Use `find()` to locate a character.
- [x] Use `rfind()` on a repeated character.
- [x] Use `index()` and observe the error for a missing substring.
- [x] Count a word in a sentence.
- [x] Check a file extension using `endswith()`.
- [x] Check a URL using `startswith()`.

---

# 📚 Summary

You learned:

- `find()`
- `rfind()`
- `index()`
- `rindex()`
- `count()`
- `startswith()`
- `endswith()`

These are among the most commonly used string methods in Python.

---

# 🎯 Topic Completion Checklist

- [x] I understand `find()` and `rfind()`.
- [x] I understand `index()` and `rindex()`.
- [x] I can use `count()`.
- [x] I can use `startswith()` and `endswith()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 3: Replace & Split Methods**