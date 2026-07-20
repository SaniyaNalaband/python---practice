# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Text (`str`) - Part 11:** Replace & Split Methods

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Replace text using `replace()`.
- [ ] Split strings using `split()` and `rsplit()`.
- [ ] Split multiline text using `splitlines()`.
- [ ] Divide strings using `partition()` and `rpartition()`.
- [ ] Join strings using `join()`.
- [ ] Understand when to use each method.

---

# 📖 1. `replace()`

Replaces one substring with another.

Syntax:

```python
string.replace(old, new)
```

Example:

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I like Python
```

---

### Replace All Occurrences

```python
text = "apple apple apple"

print(text.replace("apple", "orange"))
```

Output:

```text
orange orange orange
```

---

### Replace Only First Occurrence

```python
text = "apple apple apple"

print(text.replace("apple", "orange", 1))
```

Output:

```text
orange apple apple
```

The third argument (`count`) limits the number of replacements.

---

# 📖 2. `split()`

Splits a string into a **list**.

Default separator: space.

```python
text = "Python Java C++"

print(text.split())
```

Output:

```python
['Python', 'Java', 'C++']
```

---

### Split by Comma

```python
data = "Apple,Banana,Mango"

print(data.split(","))
```

Output:

```python
['Apple', 'Banana', 'Mango']
```

---

### Split with Maximum Splits

```python
text = "one two three four"

print(text.split(" ", 2))
```

Output:

```python
['one', 'two', 'three four']
```

---

# 📖 3. `rsplit()`

Works like `split()`, but starts splitting from the **right**.

```python
text = "one two three four"

print(text.rsplit(" ", 2))
```

Output:

```python
['one two', 'three', 'four']
```

---

# 📖 4. `splitlines()`

Splits a multiline string into a list of lines.

```python
text = "Python\nJava\nC++"

print(text.splitlines())
```

Output:

```python
['Python', 'Java', 'C++']
```

---

# 📖 5. `partition()`

Splits a string into **three parts**:

- Before separator
- Separator
- After separator

```python
email = "student@gmail.com"

print(email.partition("@"))
```

Output:

```python
('student', '@', 'gmail.com')
```

---

If the separator is not found:

```python
text = "Python"

print(text.partition("@"))
```

Output:

```python
('Python', '', '')
```

---

# 📖 6. `rpartition()`

Like `partition()`, but starts searching from the **right**.

```python
path = "folder/subfolder/file.txt"

print(path.rpartition("/"))
```

Output:

```python
('folder/subfolder', '/', 'file.txt')
```

---

# 📖 7. `join()`

`join()` combines elements of an iterable (like a list) into a single string.

Syntax:

```python
separator.join(iterable)
```

Example:

```python
words = ["Python", "is", "fun"]

print(" ".join(words))
```

Output:

```text
Python is fun
```

---

### Join with Comma

```python
fruits = ["Apple", "Banana", "Mango"]

print(", ".join(fruits))
```

Output:

```text
Apple, Banana, Mango
```

---

### Join with Hyphen

```python
letters = ["A", "B", "C"]

print("-".join(letters))
```

Output:

```text
A-B-C
```

---

# 🌍 Real-World Examples

### CSV Data

```python
csv = "101,Saniya,AI ML"

print(csv.split(","))
```

Output:

```python
['101', 'Saniya', 'AI ML']
```

---

### Email Username

```python
email = "student@gmail.com"

print(email.partition("@")[0])
```

Output:

```text
student
```

---

### Build a Sentence

```python
words = ["Learning", "Python", "is", "awesome"]

print(" ".join(words))
```

Output:

```text
Learning Python is awesome
```

---

# ⚠️ Common Mistakes

## ❌ `split()` Returns a List

```python
text = "Python Java"

result = text.split()

print(type(result))
```

Output:

```text
<class 'list'>
```

It is **not** a string.

---

## ❌ `join()` Works on Iterables

Wrong:

```python
print("-".join(100))
```

Output:

```text
TypeError
```

Correct:

```python
print("-".join(["1", "0", "0"]))
```

Output:

```text
1-0-0
```

---

# 💡 Best Practices

- Use `split()` to process user input.
- Use `replace()` for cleaning text.
- Use `join()` to combine lists into readable strings.
- Use `partition()` when you only need one split.

---

# 🚀 Pro Tips

Convert a sentence into words:

```python
sentence = "Python is powerful"

words = sentence.split()

print(words)
```

Output:

```python
['Python', 'is', 'powerful']
```

---

Convert words back into a sentence:

```python
print(" ".join(words))
```

Output:

```text
Python is powerful
```

---

# 🧠 Memory Trick

```
replace()

↓

Change text

------------------

split()

↓

String → List

------------------

join()

↓

List → String

------------------

partition()

↓

3 Parts
```

---

# ❓ Interview Questions

- [ ] What is the difference between `split()` and `rsplit()`?
- [ ] What does `replace()` return?
- [ ] What is the return type of `split()`?
- [ ] What is the purpose of `join()`?
- [ ] How does `partition()` differ from `split()`?

---

# 🏋️ Practice Programs

## Easy

```python
text = "I love Java"

print(text.replace("Java", "Python"))
```

---

```python
text = "Apple Banana Mango"

print(text.split())
```

---

## Medium

```python
email = "student@gmail.com"

print(email.partition("@"))
```

---

```python
words = ["Python", "is", "fun"]

print(" ".join(words))
```

---

## Advanced

```python
text = "Python\nJava\nC++"

print(text.splitlines())

sentence = "one two three four"

print(sentence.split(" ", 2))
print(sentence.rsplit(" ", 2))

path = "folder/subfolder/file.txt"

print(path.rpartition("/"))
```

---

# 🎯 Challenge

Create:

```python
sentence = "AI ML Data Science Python"
```

Print:

- Replace `"Python"` with `"Java"`
- Split into a list
- Join the list using `"-"`
- Partition using `"Data"`

---

# 📝 Assignment

- [x] Replace a word in a sentence.
- [x] Split a CSV string.
- [x] Join a list using commas.
- [x] Partition an email address.
- [x] Split a multiline string.
- [x] Explain the difference between `split()` and `join()`.

---

# 📚 Summary

You learned:

- `replace()`
- `split()`
- `rsplit()`
- `splitlines()`
- `partition()`
- `rpartition()`
- `join()`

These methods are essential for text processing and are widely used in real-world Python programs.

---

# 🎯 Topic Completion Checklist

- [x] I understand `replace()`.
- [x] I understand `split()` and `rsplit()`.
- [x] I understand `splitlines()`.
- [x] I understand `partition()` and `rpartition()`.
- [x] I understand `join()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 4: Cleaning & Alignment Methods**