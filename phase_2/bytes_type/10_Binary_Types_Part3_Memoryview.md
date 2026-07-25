# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Binary Types → Part 3: memoryview**

**Difficulty:** ⭐⭐⭐⭐ Intermediate → ⭐⭐⭐⭐⭐ Advanced

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what `memoryview` is.
- [ ] Create a memoryview.
- [ ] Access binary data without copying it.
- [ ] Modify data through a memoryview.
- [ ] Understand why memoryview is memory-efficient.
- [ ] Know real-world uses of memoryview.

---

# 📖 What is memoryview?

A **memoryview** is an object that provides a **view** of another binary object **without copying the data**.

Imagine you have a huge image file.

Without memoryview:

```
Image

↓

Copy

↓

Process
```

Python creates another copy in memory.

With memoryview:

```
Image

↓

memoryview

↓

Process

(No Copy)
```

This saves memory and improves performance.

---

# 📖 Why Use memoryview?

Suppose you have:

```python
image = bytearray(10000000)
```

Without memoryview:

```
Another copy is created

↓

More RAM

↓

Slower
```

With memoryview:

```
Same Memory

↓

No Copy

↓

Fast
```

---

# 📖 Syntax

```python
memoryview(object)
```

The object must support the buffer protocol, such as:

- bytes
- bytearray

---

# 📖 Example 1 – Create a memoryview

```python
data = bytes([65, 66, 67])

view = memoryview(data)

print(view)
print(type(view))
```

Output

```text
<memory at 0x...>
<class 'memoryview'>
```

---

# 📖 Example 2 – Access Values

```python
data = bytes([65, 66, 67])

view = memoryview(data)

print(view[0])
print(view[1])
print(view[2])
```

Output

```text
65
66
67
```

---

# 📖 Example 3 – Slicing

```python
data = bytes([65, 66, 67, 68])

view = memoryview(data)

print(view[1:3].tolist())
```

Output

```text
[66, 67]
```

---

# 📖 Example 4 – Convert to List

```python
data = b"ABC"

view = memoryview(data)

print(view.tolist())
```

Output

```text
[65, 66, 67]
```

---

# 📖 Example 5 – Modify Data

A memoryview can modify data **only if the original object is mutable**.

```python
data = bytearray(b"ABC")

view = memoryview(data)

view[0] = 90

print(data)
```

Output

```text
bytearray(b'ZBC')
```

Notice:

The original bytearray changed.

---

# 📖 Example 6 – Modifying bytes

```python
data = b"ABC"

view = memoryview(data)

view[0] = 90
```

Output

```text
TypeError
```

Because `bytes` is immutable.

---

# 📖 Converting Back to Bytes

```python
data = bytearray(b"Python")

view = memoryview(data)

print(view.tobytes())
```

Output

```text
b'Python'
```

---

# 📖 Convert to Bytearray

```python
data = b"ABC"

view = memoryview(data)

print(bytearray(view))
```

Output

```text
bytearray(b'ABC')
```

---

# 🌍 Real-World Examples

## Reading Large Files

```python
with open("video.mp4", "rb") as file:
    data = file.read()

view = memoryview(data)
```

No extra copy is created.

---

## Image Processing

```python
image = bytearray(b"IMAGE")

view = memoryview(image)

view[0] = 88

print(image)
```

Output

```text
bytearray(b'XMAGE')
```

---

## Networking

```python
packet = bytearray(b"HEADERDATA")

view = memoryview(packet)

print(view[:6].tobytes())
```

Output

```text
b'HEADER'
```

---

# 📊 bytes vs bytearray vs memoryview

| Feature | bytes | bytearray | memoryview |
|---------|--------|------------|------------|
| Mutable | ❌ | ✅ | Depends on source |
| Stores Binary Data | ✅ | ✅ | ❌ (Views existing data) |
| Copy Needed | Yes | Yes | No |
| Memory Efficient | ❌ | ❌ | ✅ |
| Indexing | ✅ | ✅ | ✅ |
| Slicing | ✅ | ✅ | ✅ |

---

# ⚠️ Common Mistakes

## ❌ Expecting memoryview to Store Data

```python
view = memoryview(b"ABC")
```

A memoryview does not own the data.

It only views another object.

---

## ❌ Modifying Immutable bytes

```python
view = memoryview(b"ABC")

view[0] = 65
```

Raises

```text
TypeError
```

---

## ❌ Forgetting `tolist()`

```python
view = memoryview(b"ABC")

print(view)
```

Output

```text
<memory at 0x...>
```

Use

```python
print(view.tolist())
```

---

# 💡 Best Practices

- Use memoryview when working with large binary data.
- Use it to avoid unnecessary memory copies.
- Use `bytearray` if you need to modify the original data.
- Convert to bytes only when needed.

---

# 🚀 Pro Tips

One memoryview can modify the original bytearray.

```python
data = bytearray(b"Hello")

view = memoryview(data)

view[0] = ord("Y")

print(data)
```

Output

```text
bytearray(b'Yello')
```

---

# 🧠 Memory Trick

```text
bytes

↓

Owns Data

Immutable

----------------

bytearray

↓

Owns Data

Mutable

----------------

memoryview

↓

Views Data

No Copy
```

---

# ❓ Interview Questions

- [ ] What is a memoryview?
- [ ] Why is memoryview faster?
- [ ] Can memoryview modify bytes?
- [ ] Can memoryview modify bytearray?
- [ ] Why is memoryview memory-efficient?
- [ ] What does `tobytes()` do?

---

# 🏋️ Practice Programs

## Easy

```python
data = b"ABC"

view = memoryview(data)

print(view.tolist())
```

---

```python
data = bytearray(b"XYZ")

view = memoryview(data)

print(view[0])
```

---

## Medium

```python
data = bytearray(b"Python")

view = memoryview(data)

view[1] = ord("A")

print(data)
```

---

```python
data = b"Programming"

view = memoryview(data)

print(view[3:7].tobytes())
```

---

## Advanced

```python
data = bytearray(b"MachineLearning")

view = memoryview(data)

view[0] = ord("m")
view[-1] = ord("!")

print(data)
print(view.tolist())
```

---

# 🎯 Challenge

Create:

```python
data = bytearray(b"Python")
```

Perform the following:

1. Create a memoryview.
2. Change `P` to `J`.
3. Print the bytearray.
4. Slice the first three bytes.
5. Convert the slice to bytes.
6. Print the list of byte values.

---

# 📝 Assignment

- [x] Create a memoryview from a bytes object.
- [x] Create a memoryview from a bytearray.
- [x] Access elements using indexing.
- [x] Slice the memoryview.
- [x] Modify a bytearray through a memoryview.
- [x] Explain why memoryview does not copy data.

---

# 📚 Summary

You learned:

- What `memoryview` is.
- How to create one.
- Indexing and slicing.
- `tolist()` and `tobytes()`.
- Modifying mutable binary data.
- Why memoryview is memory-efficient.

---

# 🎯 Topic Completion Checklist

- [x] I understand memoryview.
- [x] I can create a memoryview.
- [x] I know it does not copy data.
- [x] I can modify a bytearray through it.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Special Data Type – `None`**