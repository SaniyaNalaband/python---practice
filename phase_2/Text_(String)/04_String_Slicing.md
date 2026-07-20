# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Text (`str`) - Part 4:** String Slicing & Step Slicing

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand string slicing.
- [ ] Use start and stop indexes.
- [ ] Use step slicing.
- [ ] Reverse a string.
- [ ] Skip characters.
- [ ] Avoid common slicing mistakes.

---

# 📖 1. What is String Slicing?

**Slicing** means extracting a part of a string.

General syntax:

```python
string[start : stop]
```

- `start` → Starting index (included)
- `stop` → Ending index (excluded)

Think of it like this:

```
Take characters

FROM start

UP TO stop

(but don't include stop)
```

---

# 📊 Example

```python
word = "Python"
```

```
Character :  P   y   t   h   o   n
Index     :  0   1   2   3   4   5
```

---

# 2. Basic Slicing

```python
print(word[0:2])
```

Output

```
Py
```

Explanation

```
Start = 0 ✅

Stop = 2 ❌

Characters:

0 → P

1 → y
```

---

```python
print(word[2:5])
```

Output

```
tho
```

---

```python
print(word[1:4])
```

Output

```
yth
```

---

# 3. Omitting Start

If the start is omitted, Python assumes **0**.

```python
print(word[:3])
```

Output

```
Pyt
```

Equivalent to

```python
print(word[0:3])
```

---

# 4. Omitting Stop

If stop is omitted, Python goes to the end.

```python
print(word[2:])
```

Output

```
thon
```

Equivalent to

```python
print(word[2:6])
```

---

# 5. Omitting Both

```python
print(word[:])
```

Output

```
Python
```

This creates a copy of the string.

---

# 📖 6. Step Slicing

Syntax

```python
string[start : stop : step]
```

The **step** tells Python how many characters to jump.

---

## Step = 1 (Default)

```python
print(word[0:6:1])
```

Output

```
Python
```

---

## Step = 2

```python
print(word[0:6:2])
```

Output

```
Pto
```

Explanation

```
Take every 2nd character

0 → P

2 → t

4 → o
```

---

## Step = 3

```python
print(word[0:6:3])
```

Output

```
Ph
```

Indexes used:

```
0

3
```

---

# 7. Negative Step

Negative step means move **backwards**.

```python
print(word[::-1])
```

Output

```
nohtyP
```

This is the easiest way to reverse a string.

---

```python
print(word[::-2])
```

Output

```
nhy
```

Explanation

```
Start from end

Take every 2nd character
```

---

# 8. More Examples

```python
text = "Programming"
```

```
P r o g r a m m i n g
0 1 2 3 4 5 6 7 8 9 10
```

---

First 5 characters

```python
print(text[:5])
```

Output

```
Progr
```

---

Last 5 characters

```python
print(text[6:])
```

Output

```
mming
```

---

Every second character

```python
print(text[::2])
```

Output

```
Pormig
```

---

Reverse

```python
print(text[::-1])
```

Output

```
gnimmargorP
```

---

# 9. Real-World Examples

First Initial

```python
name = "Saniya"

print(name[0])
```

Output

```
S
```

---

Last Name Characters

```python
last = "Nalaband"

print(last[:4])
```

Output

```
Nala
```

---

Masking

```python
password = "Python123"

print(password[:3])
```

Output

```
Pyt
```

---

# ⚠️ 10. Common Mistakes

## Forgetting that Stop is Excluded

```python
word = "Python"

print(word[0:1])
```

Output

```
P
```

Not

```
Py
```

---

## Using Wrong Indexes

```python
print(word[5:2])
```

Output

```

```

Empty string.

Because Python moves forward by default.

---

## Step Cannot Be Zero

Wrong

```python
print(word[::0])
```

Output

```
ValueError
```

---

# 💡 11. Best Practices

✅ Use slicing instead of loops when extracting text.

✅ Use `[::-1]` for reversing strings.

✅ Remember:

```
Start → Included

Stop → Excluded
```

---

# 🚀 12. Pro Tips

Reverse using slicing:

```python
name = "Python"

reverse = name[::-1]

print(reverse)
```

---

Extract every alternate character:

```python
print(name[::2])
```

---

# 🧠 Memory Trick

```
[start : stop : step]

↓

Start

Included

↓

Stop

Excluded

↓

Step

Jump Size
```

---

# ❓ Interview Questions

- [ ] What is slicing?
- [ ] Why is the stop index excluded?
- [ ] What is step slicing?
- [ ] How do you reverse a string?
- [ ] Why does `word[::0]` give an error?

---

# 🏋️ Practice Programs

## Easy

```python
word = "Python"

print(word[:3])
print(word[3:])
```

---

```python
print(word[::2])
```

---

## Medium

```python
language = "Programming"

print(language[1:7])
print(language[::3])
print(language[::-1])
```

---

## Advanced

```python
text = "Artificial Intelligence"

print("First 10 :", text[:10])
print("Last 10  :", text[-10:])
print("Reverse  :", text[::-1])
print("Alternate:", text[::2])
```

---

# 🎯 Challenge

Create a string containing your full name.

Print:

- First 3 characters
- Last 3 characters
- Every second character
- Reverse of the string

---

# 📝 Assignment

Complete the following:

- [x] Slice the first five characters.
- [x] Slice the last four characters.
- [x] Print every second character.
- [x] Print every third character.
- [x] Reverse a string using slicing.
- [x] Explain the difference between indexing and slicing.

---

# 📚 Summary

You learned:

- Basic slicing.
- Start and stop indexes.
- Step slicing.
- Negative step.
- Reversing strings.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I understand string slicing.
- [x] I know start and stop indexes.
- [x] I understand step slicing.
- [x] I can reverse strings.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 5: String Immutability**