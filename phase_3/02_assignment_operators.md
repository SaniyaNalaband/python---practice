# 🐍 Python Master Course

> **Phase 3:** Operators
> **Topic 2:** Assignment Operators

**Difficulty:** ⭐ Beginner → ⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand assignment operators.
- [ ] Assign values to variables.
- [ ] Update variable values using shorthand operators.
- [ ] Understand compound assignment operators.
- [ ] Use assignment operators in real-world programs.

---

# 📖 What are Assignment Operators?

Assignment operators are used to **assign values to variables** or **update existing values**.

Example:

```python
x = 10
```

Here,

- `=` is the assignment operator.
- `10` is assigned to the variable `x`.

---

# 📚 Types of Assignment Operators

| Operator | Name | Example | Equivalent To |
|----------|------|----------|---------------|
| `=` | Assignment | `x = 5` | `x = 5` |
| `+=` | Add and Assign | `x += 3` | `x = x + 3` |
| `-=` | Subtract and Assign | `x -= 3` | `x = x - 3` |
| `*=` | Multiply and Assign | `x *= 3` | `x = x * 3` |
| `/=` | Divide and Assign | `x /= 3` | `x = x / 3` |
| `//=` | Floor Divide and Assign | `x //= 3` | `x = x // 3` |
| `%=` | Modulus and Assign | `x %= 3` | `x = x % 3` |
| `**=` | Exponent and Assign | `x **= 3` | `x = x ** 3` |
| `&=` | Bitwise AND and Assign | `x &= y` | `x = x & y` |
| `|=` | Bitwise OR and Assign | `x |= y` | `x = x \| y` |
| `^=` | Bitwise XOR and Assign | `x ^= y` | `x = x ^ y` |
| `<<=` | Left Shift and Assign | `x <<= 2` | `x = x << 2` |
| `>>=` | Right Shift and Assign | `x >>= 2` | `x = x >> 2` |

---

# 1️⃣ Assignment (`=`)

Assigns a value to a variable.

### Syntax

```python
variable = value
```

### Example

```python
age = 21

print(age)
```

Output

```text
21
```

---

# 2️⃣ Add and Assign (`+=`)

Adds a value and stores the result.

### Syntax

```python
x += value
```

Equivalent to:

```python
x = x + value
```

### Example

```python
x = 10

x += 5

print(x)
```

Output

```text
15
```

---

# Real-World Example

```python
wallet = 100

wallet += 50

print(wallet)
```

Output

```text
150
```

---

# 3️⃣ Subtract and Assign (`-=`)

Subtracts a value and stores the result.

```python
marks = 95

marks -= 10

print(marks)
```

Output

```text
85
```

---

# 4️⃣ Multiply and Assign (`*=`)

Multiplies the variable by another value.

```python
salary = 5000

salary *= 2

print(salary)
```

Output

```text
10000
```

---

# 5️⃣ Divide and Assign (`/=`)

Divides the variable and stores the result.

```python
total = 100

total /= 4

print(total)
```

Output

```text
25.0
```

> `/=` always produces a float.

---

# 6️⃣ Floor Divide and Assign (`//=`)

```python
x = 25

x //= 4

print(x)
```

Output

```text
6
```

---

# 7️⃣ Modulus and Assign (`%=`)

```python
x = 25

x %= 4

print(x)
```

Output

```text
1
```

---

# 8️⃣ Exponent and Assign (`**=`)

```python
x = 2

x **= 5

print(x)
```

Output

```text
32
```

---

# 9️⃣ Bitwise Assignment Operators

These operators work with binary numbers.

## `&=`

```python
x = 6
x &= 3

print(x)
```

Output

```text
2
```

---

## `|=`

```python
x = 6
x |= 3

print(x)
```

Output

```text
7
```

---

## `^=`

```python
x = 6
x ^= 3

print(x)
```

Output

```text
5
```

---

## `<<=`

```python
x = 5

x <<= 1

print(x)
```

Output

```text
10
```

---

## `>>=`

```python
x = 20

x >>= 2

print(x)
```

Output

```text
5
```

---

# 📊 Summary Table

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Assign | `x = 10` |
| `+=` | Add and Assign | `x += 5` |
| `-=` | Subtract and Assign | `x -= 5` |
| `*=` | Multiply and Assign | `x *= 5` |
| `/=` | Divide and Assign | `x /= 5` |
| `//=` | Floor Divide and Assign | `x //= 5` |
| `%=` | Modulus and Assign | `x %= 5` |
| `**=` | Power and Assign | `x **= 5` |
| `&=` | Bitwise AND | `x &= y` |
| `\|=` | Bitwise OR | `x \|= y` |
| `^=` | Bitwise XOR | `x ^= y` |
| `<<=` | Left Shift | `x <<= 1` |
| `>>=` | Right Shift | `x >>= 1` |

---

# ⚠️ Common Mistakes

## ❌ Using a Variable Before Assignment

```python
x += 5
```

Output

```text
NameError
```

Correct:

```python
x = 0
x += 5
```

---

## ❌ Expecting `/=` to Return an Integer

```python
x = 10

x /= 2

print(type(x))
```

Output

```text
<class 'float'>
```

---

## ❌ Forgetting That Assignment Updates the Variable

```python
x = 10

x += 5

print(x)
```

Output

```text
15
```

The original value of `x` is changed.

---

# 💡 Best Practices

- Use compound assignment (`+=`, `-=`, etc.) to write shorter and cleaner code.
- Initialize variables before updating them.
- Use descriptive variable names.
- Remember that `/=` always returns a float.

---

# 🚀 Pro Tips

Increase a counter inside a loop.

```python
count = 0

count += 1

print(count)
```

Output

```text
1
```

Compound assignment is commonly used in loops and counters.

---

# 🌍 Real-World Programs

## Bank Balance

```python
balance = 1000

balance += 500
balance -= 200

print(balance)
```

Output

```text
1300
```

---

## Shopping Cart

```python
total = 0

total += 250
total += 120
total += 80

print(total)
```

Output

```text
450
```

---

## Discount

```python
price = 1000

price -= 200

print(price)
```

Output

```text
800
```

---

# ❓ Interview Questions

- [ ] What is an assignment operator?
- [ ] What is the difference between `=` and `+=`?
- [ ] What does `/=` return?
- [ ] Why are compound assignment operators useful?
- [ ] What happens if you use `+=` before assigning a value?

---

# 🏋️ Practice Programs

## Easy

```python
x = 10

x += 5

print(x)
```

---

```python
x = 20

x -= 8

print(x)
```

---

```python
x = 7

x *= 6

print(x)
```

---

## Medium

```python
x = 50

x /= 5

print(x)
```

---

```python
x = 17

x %= 3

print(x)
```

---

```python
x = 4

x **= 3

print(x)
```

---

## Advanced

```python
value = 100

value += 20
value -= 10
value *= 2
value /= 5

print(value)
```

---

# 🎯 Challenge

Write a program that:

1. Creates a variable `score = 50`
2. Adds `20`
3. Multiplies by `2`
4. Subtracts `10`
5. Divides by `4`
6. Prints the final result

---

# 📝 Assignment

- [x] Use `=` to assign a value.
- [x] Use `+=` to increase a number.
- [x] Use `-=` to decrease a number.
- [x] Use `*=` to multiply a value.
- [x] Use `/=` to divide a value.
- [x] Use `//=` to perform floor division.
- [x] Use `%=` to find the remainder.
- [x] Use `**=` to calculate a power.

---

# 📚 Summary

You learned:

- ✅ Assignment (`=`)
- ✅ Add and Assign (`+=`)
- ✅ Subtract and Assign (`-=`)
- ✅ Multiply and Assign (`*=`)
- ✅ Divide and Assign (`/=`)
- ✅ Floor Divide and Assign (`//=`)
- ✅ Modulus and Assign (`%=`)
- ✅ Exponent and Assign (`**=`)
- ✅ Bitwise Assignment Operators (`&=`, `|=`, `^=`, `<<=`, `>>=`)

---

# 🎯 Topic Completion Checklist

- [x] I understand assignment operators.
- [x] I can use compound assignment operators.
- [x] I know the difference between `=` and `+=`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Phase 3 – Topic 3: Comparison Operators**