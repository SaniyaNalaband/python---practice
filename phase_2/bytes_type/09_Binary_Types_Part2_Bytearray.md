# 🐍 Python Master Course

> **Phase 2:** Data Types
> **Binary Types → Part 2: bytearray**

**Difficulty:** ⭐⭐⭐ Beginner → ⭐⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what `bytearray` is.
- [ ] Create a `bytearray`.
- [ ] Modify bytes.
- [ ] Add and remove bytes.
- [ ] Compare `bytes` and `bytearray`.
- [ ] Know real-world uses of `bytearray`.

---

# 📖 What is a Bytearray?

A **bytearray** is a **mutable sequence of bytes**.

Unlike `bytes`, a `bytearray` can be modified after it is created.

Think of it like this:

```
bytes
↓

Immutable

↓

Cannot Change

--------------------

bytearray

↓

Mutable

↓

Can Change
```

---

# 📖 Syntax

```python
bytearray(iterable)
```

or

```python
bytearray(size)
```

---

# 📖 Example 1 – Create from a List

```python
data = bytearray([65, 66, 67])

print(data)
print(type(data))
```

Output

```text
bytearray(b'ABC')
<class 'bytearray'>
```

---

# 📖 Example 2 – Create from a String

```python
text = "Python"

data = bytearray(text, "utf-8")

print(data)
```

Output

```text
bytearray(b'Python')
```

---

# 📖 Example 3 – Create Empty Bytearray

```python
data = bytearray()

print(data)
```

Output

```text
bytearray(b'')
```

---

# 📖 Example 4 – Create with Size

```python
data = bytearray(5)

print(data)
```

Output

```text
bytearray(b'\x00\x00\x00\x00\x00')
```

Creates five bytes initialized to zero.

---

# 📖 Accessing Values

```python
data = bytearray(b"Python")

print(data[0])
print(data[1])
```

Output

```text
80
121
```

Like `bytes`, indexing returns integers.

---

# 📖 Indexing

```python
data = bytearray(b"Python")

print(data[2])
print(data[-1])
```

Output

```text
116
110
```

---

# 📖 Slicing

```python
data = bytearray(b"Programming")

print(data[0:4])
```

Output

```text
bytearray(b'Prog')
```

---

# 📖 Modifying a Byte

```python
data = bytearray(b"ABC")

data[0] = 90

print(data)
```

Output

```text
bytearray(b'ZBC')
```

ASCII value:

```
90 → Z
```

---

# 📖 Changing Multiple Bytes

```python
data = bytearray(b"Python")

data[0:2] = b"JA"

print(data)
```

Output

```text
bytearray(b'JAthon')
```

---

# 📖 append()

Adds one byte at the end.

```python
data = bytearray(b"ABC")

data.append(68)

print(data)
```

Output

```text
bytearray(b'ABCD')
```

---

# 📖 extend()

Adds multiple bytes.

```python
data = bytearray(b"ABC")

data.extend(b"DEF")

print(data)
```

Output

```text
bytearray(b'ABCDEF')
```

---

# 📖 insert()

Insert one byte.

```python
data = bytearray(b"ABC")

data.insert(1, 90)

print(data)
```

Output

```text
bytearray(b'AZBC')
```

---

# 📖 pop()

Removes and returns one byte.

```python
data = bytearray(b"ABC")

print(data.pop())

print(data)
```

Output

```text
67
bytearray(b'AB')
```

---

# 📖 remove()

Removes the first matching byte.

```python
data = bytearray(b"ABCA")

data.remove(65)

print(data)
```

Output

```text
bytearray(b'BCA')
```

---

# 📖 clear()

Removes all bytes.

```python
data = bytearray(b"Python")

data.clear()

print(data)
```

Output

```text
bytearray(b'')
```

---

# 📖 reverse()

```python
data = bytearray(b"ABC")

data.reverse()

print(data)
```

Output

```text
bytearray(b'CBA')
```

---

# 📖 decode()

Convert bytearray back into a string.

```python
data = bytearray(b"Python")

print(data.decode())
```

Output

```text
Python
```

---

# 🌍 Real-World Examples

## Reading Binary Data

```python
with open("photo.jpg", "rb") as file:
    image = bytearray(file.read())

print(type(image))
```

Output

```text
<class 'bytearray'>
```

---

## Editing Binary Data

```python
data = bytearray(b"ABC")

data[1] = 90

print(data)
```

Output

```text
bytearray(b'AZC')
```

---

## Network Packets

```python
packet = bytearray()

packet.extend(b"HEADER")

print(packet)
```

---

# 📊 bytes vs bytearray

| Feature | bytes | bytearray |
|---------|--------|------------|
| Mutable | ❌ No | ✅ Yes |
| Ordered | ✅ Yes | ✅ Yes |
| Indexing | ✅ | ✅ |
| Slicing | ✅ | ✅ |
| append() | ❌ | ✅ |
| remove() | ❌ | ✅ |
| insert() | ❌ | ✅ |
| clear() | ❌ | ✅ |
| decode() | ✅ | ✅ |

---

# ⚠️ Common Mistakes

## ❌ Value Greater Than 255

```python
data = bytearray([300])
```

Output

```text
ValueError: byte must be in range(0, 256)
```

---

## ❌ append() Accepts One Byte

```python
data = bytearray()

data.append(500)
```

Output

```text
ValueError
```

---

## ❌ Confusing Characters with ASCII Values

```python
data = bytearray(b"A")

print(data[0])
```

Output

```text
65
```

It returns the integer value, not the character.

---

# 💡 Best Practices

- Use `bytes` when data should not change.
- Use `bytearray` when binary data needs modification.
- Decode binary data before displaying it as text.
- Ensure all byte values are between 0 and 255.

---

# 🚀 Pro Tips

Convert a `bytes` object into a `bytearray`.

```python
data = b"Python"

mutable = bytearray(data)

mutable[0] = 74

print(mutable)
```

Output

```text
bytearray(b'Jython')
```

---

# 🧠 Memory Trick

```text
bytes

↓

Read Only

----------------

bytearray

↓

Read + Write
```

---

# ❓ Interview Questions

- [ ] What is `bytearray`?
- [ ] How is `bytearray` different from `bytes`?
- [ ] Can you modify a `bytearray`?
- [ ] Why must byte values be between 0 and 255?
- [ ] Which methods are available only on `bytearray`?

---

# 🏋️ Practice Programs

## Easy

```python
data = bytearray(b"ABC")

print(data)
```

---

```python
data = bytearray([65, 66, 67])

print(data)
```

---

## Medium

```python
data = bytearray(b"Python")

data[0] = 74

print(data)
```

---

```python
data = bytearray(b"ABC")

data.append(68)

print(data)
```

---

## Advanced

```python
data = bytearray(b"Programming")

data.remove(80)

data.append(90)

data.reverse()

print(data)
```

---

# 🎯 Challenge

Create:

```python
data = bytearray(b"Python")
```

Perform the following:

1. Change `P` to `J`.
2. Append `!`.
3. Insert `A` at index `1`.
4. Remove `!`.
5. Reverse the bytearray.
6. Decode it into a string.

---

# 📝 Assignment

- [x] Create a `bytearray` from a string.
- [x] Modify one byte.
- [x] Append two new bytes.
- [x] Remove one byte.
- [x] Decode the final `bytearray`.
- [x] Explain the difference between `bytes` and `bytearray`.

---

# 📚 Summary

You learned:

- What `bytearray` is.
- How to create it.
- How to modify bytes.
- Common methods like `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `clear()`, `reverse()`, and `decode()`.
- The difference between `bytes` and `bytearray`.

---

# 🎯 Topic Completion Checklist

- [x] I understand `bytearray`.
- [x] I can create a `bytearray`.
- [x] I can modify bytes.
- [x] I understand the available methods.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Binary Types – Part 3: `memoryview`**