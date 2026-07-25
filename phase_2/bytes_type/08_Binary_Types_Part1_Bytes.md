# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Binary Types → Part 1: bytes**

**Difficulty:** ⭐⭐⭐ Beginner → ⭐⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what `bytes` are.
- [ ] Create byte objects.
- [ ] Access bytes using indexing and slicing.
- [ ] Convert strings to bytes and back.
- [ ] Understand why bytes are immutable.
- [ ] Know common real-world uses of bytes.

---

# 📖 What are Bytes?

A **byte** is the basic unit used to store data in computers.

- **1 byte = 8 bits**
- A byte stores a value from **0 to 255**.

Unlike strings, which store **characters**, `bytes` store **raw binary values**.

---

# 📖 What is the `bytes` Data Type?

`bytes` is an **immutable sequence of integers**.

Each element is an integer between **0 and 255**.

---

# 📖 Syntax

```python
bytes(iterable)
```

or

```python
b"Hello"
```

---

# 📖 Example 1 – Create from a List

```python
numbers = bytes([65, 66, 67, 68])

print(numbers)
```

Output

```text
b'ABCD'
```

Explanation:

```
65 → A
66 → B
67 → C
68 → D
```

---

# 📖 Example 2 – Create from a String

```python
text = "Python"

data = text.encode()

print(data)
```

Output

```text
b'Python'
```

---

# 📖 Example 3 – Create Using a Bytes Literal

```python
data = b"Hello"

print(data)
print(type(data))
```

Output

```text
b'Hello'
<class 'bytes'>
```

---

# 📖 Bytes Store Numbers

```python
data = b"ABC"

print(data[0])
print(data[1])
print(data[2])
```

Output

```text
65
66
67
```

Notice:

Bytes return **ASCII/UTF-8 integer values**, not characters.

---

# 📖 Convert Number Back to Character

```python
print(chr(65))
print(chr(66))
```

Output

```text
A
B
```

---

# 📖 Indexing

```python
data = b"Python"

print(data[0])
print(data[3])
print(data[-1])
```

Output

```text
80
104
110
```

---

# 📖 Slicing

```python
data = b"Python"

print(data[0:3])
print(data[2:])
```

Output

```text
b'Pyt'
b'thon'
```

Slicing returns another `bytes` object.

---

# 📖 Encoding

Convert a string into bytes.

```python
text = "Hello"

binary = text.encode("utf-8")

print(binary)
```

Output

```text
b'Hello'
```

---

# 📖 Decoding

Convert bytes back into a string.

```python
binary = b"Python"

text = binary.decode("utf-8")

print(text)
```

Output

```text
Python
```

---

# 📖 Bytes are Immutable

```python
data = b"ABC"

data[0] = 70
```

Output

```text
TypeError: 'bytes' object does not support item assignment
```

You cannot modify a `bytes` object after it is created.

---

# 🌍 Real-World Examples

## Reading an Image

```python
with open("photo.jpg", "rb") as file:
    data = file.read()

print(type(data))
```

Output

```text
<class 'bytes'>
```

---

## Reading a PDF

```python
with open("notes.pdf", "rb") as file:
    pdf = file.read()
```

---

## Sending Data Over a Network

```python
message = "Hello"

binary = message.encode()

print(binary)
```

---

# 📊 String vs Bytes

| Feature | String | Bytes |
|---------|---------|--------|
| Stores | Characters | Numbers (0–255) |
| Mutable | ❌ | ❌ |
| Prefix | None | `b` |
| Encoding Needed | ❌ | ✅ (from string) |
| Decoding Needed | ❌ | ✅ (to string) |

---

# ⚠️ Common Mistakes

## ❌ Values Outside 0–255

```python
data = bytes([300])
```

Output

```text
ValueError: bytes must be in range(0, 256)
```

---

## ❌ Modifying Bytes

```python
data = b"ABC"

data[0] = 65
```

Output

```text
TypeError
```

---

## ❌ Forgetting to Decode

```python
binary = b"Python"

print(binary)
```

Output

```text
b'Python'
```

If you need a normal string:

```python
print(binary.decode())
```

---

# 💡 Best Practices

- Use `bytes` when working with binary files.
- Encode text before sending it over a network.
- Decode received bytes before displaying them.
- Use `bytearray` if you need to modify binary data.

---

# 🚀 Pro Tips

You can create bytes filled with zeros.

```python
data = bytes(5)

print(data)
```

Output

```text
b'\x00\x00\x00\x00\x00'
```

---

# 🧠 Memory Trick

```text
String

↓

Text

↓

"Hello"

----------------

Bytes

↓

Binary Data

↓

b"Hello"
```

---

# ❓ Interview Questions

- [ ] What is the `bytes` data type?
- [ ] Why are bytes immutable?
- [ ] What values can a byte store?
- [ ] What is the difference between `bytes` and `str`?
- [ ] What is encoding?
- [ ] What is decoding?

---

# 🏋️ Practice Programs

## Easy

```python
data = b"Python"

print(data)
```

---

```python
numbers = bytes([65, 66, 67])

print(numbers)
```

---

## Medium

```python
text = "Hello"

binary = text.encode()

print(binary)

print(binary.decode())
```

---

```python
data = b"Programming"

print(data[0])
print(data[-1])
print(data[3:7])
```

---

## Advanced

```python
text = "AI ML"

binary = text.encode("utf-8")

print(binary)

for value in binary:
    print(value)
```

---

# 🎯 Challenge

Create:

```python
text = "Python"
```

Perform the following:

1. Encode the string.
2. Print the bytes object.
3. Print the first byte.
4. Slice the first three bytes.
5. Decode the bytes back into a string.

---

# 📝 Assignment

- [x] Create a bytes object from a list.
- [x] Create a bytes object from a string.
- [x] Print the ASCII value of the first character.
- [x] Decode bytes into a string.
- [x] Explain why bytes are immutable.

---

# 📚 Summary

You learned:

- What `bytes` are.
- How to create them.
- Indexing and slicing.
- Encoding and decoding.
- Why they are immutable.

---

# 🎯 Topic Completion Checklist

- [x] I understand bytes.
- [x] I can create bytes.
- [x] I understand encoding and decoding.
- [x] I know bytes are immutable.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Binary Types – Part 2: `bytearray`**