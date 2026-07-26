
# 🐍 Python Master Course

> **Phase 3:** Operators  
> **Topic 7:** Bitwise Operators

**Difficulty:** ⭐⭐⭐⭐ Advanced

> **Prerequisite:** Before learning bitwise operators, you should understand **binary numbers (0s and 1s)**.

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what bitwise operators are.
- [ ] Convert decimal numbers to binary.
- [ ] Perform bitwise operations.
- [ ] Understand left and right shift.
- [ ] Solve real-world problems using bitwise operators.

---

# 📖 What are Bitwise Operators?

Bitwise operators work directly on the **binary (bit)** representation of numbers.

Unlike arithmetic operators that work on decimal numbers, bitwise operators compare **each bit (0 or 1)**.

For example:

```text
Decimal Number: 5

Binary Number : 0101
```

Python converts numbers into binary internally before applying bitwise operators.

---

# 📚 Types of Bitwise Operators

| Operator | Name |
|----------|------|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

---

# 📖 Binary Basics

| Decimal | Binary |
|----------|---------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |

---

# 1️⃣ Bitwise AND (`&`)

Returns `1` only if **both bits are 1**.

### Truth Table

| A | B | A & B |
|---|---|-------|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

---

### Example

```python
print(5 & 3)
```

Binary Calculation

```text
5 = 0101
3 = 0011
------------
    0001
```

Output

```text
1
```

---

# 🌍 Real-World Example

Permission checking.

```python
read = 1
write = 2

permission = 3

print(permission & read)
```

Output

```text
1
```

---

# 2️⃣ Bitwise OR (`|`)

Returns `1` if **either bit is 1**.

### Truth Table

| A | B | A \| B |
|---|---|--------|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

---

### Example

```python
print(5 | 3)
```

Binary

```text
5 = 0101
3 = 0011
------------
    0111
```

Output

```text
7
```

---

# 🌍 Real-World Example

Combining permissions.

```python
read = 1
write = 2

permission = read | write

print(permission)
```

Output

```text
3
```

---

# 3️⃣ Bitwise XOR (`^`)

Returns `1` when the bits are **different**.

### Truth Table

| A | B | A ^ B |
|---|---|-------|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

---

### Example

```python
print(5 ^ 3)
```

Binary

```text
5 = 0101
3 = 0011
------------
    0110
```

Output

```text
6
```

---

# 🌍 Real-World Example

Finding changed bits between two values.

```python
old = 5
new = 3

print(old ^ new)
```

Output

```text
6
```

---

# 4️⃣ Bitwise NOT (`~`)

Flips every bit.

### Example

```python
print(~5)
```

Output

```text
-6
```

---

### Why is the Answer `-6`?

Python stores integers using **two's complement** representation.

Formula:

```text
~x = -(x + 1)
```

Example

```text
~5

= -(5 + 1)

= -6
```

---

# 5️⃣ Left Shift (`<<`)

Moves bits to the left.

Each left shift multiplies the number by **2**.

### Example

```python
print(5 << 1)
```

Binary

```text
5 = 0101

Shift Left

1010
```

Output

```text
10
```

---

Another Example

```python
print(5 << 2)
```

Output

```text
20
```

---

# 🌍 Real-World Example

Doubling a value.

```python
salary = 1000

print(salary << 1)
```

Output

```text
2000
```

---

# 6️⃣ Right Shift (`>>`)

Moves bits to the right.

Each right shift divides the number by **2** (discarding any remainder).

### Example

```python
print(20 >> 1)
```

Binary

```text
20 = 10100

Shift Right

01010
```

Output

```text
10
```

---

Another Example

```python
print(20 >> 2)
```

Output

```text
5
```

---

# 🌍 Real-World Example

Reducing a value by half.

```python
stock = 40

print(stock >> 1)
```

Output

```text
20
```

---

# 📊 Summary Table

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `&` | AND | `5 & 3` | `1` |
| `|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT | `~5` | `-6` |
| `<<` | Left Shift | `5 << 1` | `10` |
| `>>` | Right Shift | `20 >> 2` | `5` |

---

# ⚠️ Common Mistakes

## ❌ Confusing `&` with `and`

Incorrect

```python
print(5 & 3)
```

This performs a **bitwise** operation.

Logical operation:

```python
print(True and False)
```

---

## ❌ Confusing `|` with `or`

Bitwise OR:

```python
print(5 | 3)
```

Logical OR:

```python
print(True or False)
```

---

## ❌ Expecting `~5` to be `-5`

```python
print(~5)
```

Output

```text
-6
```

Remember:

```text
~x = -(x + 1)
```

---

# 💡 Best Practices

- Use bitwise operators only when working with binary data.
- Prefer logical operators (`and`, `or`) for conditions.
- Use parentheses in complex expressions.
- Learn binary conversion before using bitwise operations.

---

# 🚀 Pro Tips

Bitwise operators are widely used in:

- Operating Systems
- Device Drivers
- Embedded Systems
- Networking
- Cryptography
- Image Processing
- Data Compression
- Game Development

---

# 🌍 Real-World Programs

## Check Even or Odd

```python
number = 8

print(number & 1)
```

Output

```text
0
```

If the result is `0`, the number is even.

---

## Multiply by 2

```python
number = 12

print(number << 1)
```

Output

```text
24
```

---

## Divide by 2

```python
number = 40

print(number >> 1)
```

Output

```text
20
```

---

## Combine Flags

```python
read = 1
write = 2

permission = read | write

print(permission)
```

Output

```text
3
```

---

# ❓ Interview Questions

- [ ] What are bitwise operators?
- [ ] Why do they work on binary numbers?
- [ ] What is the difference between `&` and `and`?
- [ ] Why does `~5` return `-6`?
- [ ] What is the difference between `<<` and `>>`?

---

# 🏋️ Practice Programs

## Easy

```python
print(6 & 2)
```

---

```python
print(6 | 2)
```

---

```python
print(6 ^ 2)
```

---

## Medium

```python
print(~10)
```

---

```python
print(8 << 2)
```

---

```python
print(32 >> 3)
```

---

## Advanced

```python
a = 12
b = 5

print("AND :", a & b)
print("OR  :", a | b)
print("XOR :", a ^ b)
print("NOT :", ~a)
print("LEFT SHIFT :", a << 2)
print("RIGHT SHIFT:", a >> 2)
```

---

# 🎯 Challenge

Write a program that:

1. Takes two integers as input.
2. Performs all six bitwise operations.
3. Displays each result with a label.

Example Output

```text
Bitwise AND: 1
Bitwise OR: 7
Bitwise XOR: 6
Bitwise NOT (First Number): -6
Left Shift: 20
Right Shift: 2
```

---

# 📝 Assignment

- [x] Find the binary representation of numbers from 1 to 10.
- [x] Perform `&` on two numbers.
- [x] Perform `|` on two numbers.
- [x] Perform `^` on two numbers.
- [x] Use `~` on a number.
- [x] Use `<<` to multiply by 2.
- [x] Use `>>` to divide by 2.

---

# 📚 Summary

You learned:

- ✅ Bitwise AND (`&`)
- ✅ Bitwise OR (`|`)
- ✅ Bitwise XOR (`^`)
- ✅ Bitwise NOT (`~`)
- ✅ Left Shift (`<<`)
- ✅ Right Shift (`>>`)
- ✅ Binary representation of numbers
- ✅ Real-world uses of bitwise operations

Remember:

- `&` → Both bits must be `1`
- `|` → At least one bit is `1`
- `^` → Bits must be different
- `~` → Flips all bits
- `<<` → Shifts left (approximately ×2 for each shift)
- `>>` → Shifts right (approximately ÷2 for each shift)

---

# 🎯 Topic Completion Checklist

- [x] I understand binary numbers.
- [x] I understand all six bitwise operators.
- [x] I know the difference between logical and bitwise operators.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 8: Operator Precedence**