# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Text (`str`) - Part 5:** Membership Operators (`in` and `not in`)

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand membership operators.
- [ ] Use `in` and `not in`.
- [ ] Search for characters.
- [ ] Search for words.
- [ ] Understand case sensitivity.
- [ ] Apply membership in real-world programs.

---

# 📖 1. What are Membership Operators?

Membership operators check whether a value exists inside another object.

Python has **two membership operators**:

- `in`
- `not in`

They always return a Boolean value:

- `True`
- `False`

---

# 📘 2. The `in` Operator

The `in` operator checks if a value exists.

```python
word = "Python"

print("P" in word)
```

Output:

```text
True
```

---

```python
print("y" in word)
```

Output:

```text
True
```

---

```python
print("z" in word)
```

Output:

```text
False
```

---

# 📗 3. The `not in` Operator

The `not in` operator checks if a value does **not** exist.

```python
word = "Python"

print("z" not in word)
```

Output:

```text
True
```

---

```python
print("P" not in word)
```

Output:

```text
False
```

---

# 🔍 4. Searching for Words

Membership works for entire words too.

```python
sentence = "Python is easy to learn"

print("easy" in sentence)
```

Output:

```text
True
```

---

```python
print("Java" in sentence)
```

Output:

```text
False
```

---

# 🔤 5. Membership is Case-Sensitive

```python
word = "Python"

print("P" in word)
```

Output:

```text
True
```

---

```python
print("p" in word)
```

Output:

```text
False
```

`"P"` and `"p"` are different characters.

---

# 🌍 6. Real-World Examples

### Email Validation

```python
email = "student@gmail.com"

print("@" in email)
```

Output:

```text
True
```

---

### Website Check

```python
website = "https://openai.com"

print("https" in website)
```

Output:

```text
True
```

---

### Password Check

```python
password = "Python@123"

print("@" in password)
```

Output:

```text
True
```

---

### File Extension

```python
filename = "notes.pdf"

print(".pdf" in filename)
```

Output:

```text
True
```

---

# 🧠 7. Membership with Empty Strings

```python
text = ""

print("a" in text)
```

Output:

```text
False
```

---

```python
print("" in text)
```

Output:

```text
True
```

An empty string is considered to exist in every string.

---

# ⚠️ 8. Common Mistakes

## ❌ Ignoring Case

```python
word = "Python"

print("python" in word)
```

Output:

```text
False
```

Correct:

```python
print("Python" in word)
```

---

## ❌ Assuming Partial Matches Ignore Spaces

```python
text = "Machine Learning"

print("MachineLearning" in text)
```

Output:

```text
False
```

Spaces matter.

---

# 💡 9. Best Practices

✅ Use meaningful variable names.

```python
email = "student@gmail.com"
```

---

✅ Convert to lowercase for case-insensitive checks.

```python
word = "Python"

print("python" in word.lower())
```

Output:

```text
True
```

---

# 🚀 10. Pro Tips

Membership can search for multiple characters.

```python
text = "Programming"

print("gram" in text)
```

Output:

```text
True
```

Python searches for the entire substring.

---

# 🧠 Memory Trick

```
in

↓

Exists?

↓

True

--------------

not in

↓

Doesn't Exist?

↓

True
```

---

# ❓ Interview Questions

- [ ] What does the `in` operator do?
- [ ] What does `not in` do?
- [ ] What type of value do membership operators return?
- [ ] Is membership case-sensitive?
- [ ] Can membership search for entire words?

---

# 🏋️ Practice Programs

## Easy

```python
word = "Python"

print("P" in word)
print("x" in word)
```

---

```python
print("P" not in word)
print("x" not in word)
```

---

## Medium

```python
sentence = "Python is fun"

print("Python" in sentence)
print("fun" in sentence)
print("Java" in sentence)
```

---

```python
email = "student@gmail.com"

print("@" in email)
print(".com" in email)
```

---

## Advanced

```python
password = "Python@123"

print("Contains @ :", "@" in password)
print("Contains digit 1 :", "1" in password)
print("Contains $ :", "$" in password)
print("Contains Python :", "Python" in password)
```

---

# 🎯 Challenge

Create variables:

```python
website = "https://github.com"

email = "example@gmail.com"

filename = "project.py"
```

Check whether they contain:

- `"https"`
- `"@"`
- `".py"`
- `"github"`

Print the results.

---

# 📝 Assignment

Complete the following:

- [x] Check if `"a"` exists in your name.
- [x] Check if `"Python"` exists in a sentence.
- [x] Check if `"@"` exists in an email.
- [x] Check if `".pdf"` exists in a filename.
- [x] Explain the difference between `in` and `not in`.

---

# 📚 Summary

In this lesson, you learned:

- Membership operators.
- `in`.
- `not in`.
- Case sensitivity.
- Searching characters and words.
- Real-world examples.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I understand `in`.
- [x] I understand `not in`.
- [x] I know membership returns Boolean values.
- [x] I know membership is case-sensitive.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 6: String Concatenation**