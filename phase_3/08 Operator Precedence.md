# 🐍 Python Master Course

> **Phase 3:** Operators  
> **Topic 8:** Operator Precedence

**Difficulty:** ⭐⭐ Beginner → ⭐⭐⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand operator precedence.
- [ ] Predict the order in which Python evaluates expressions.
- [ ] Use parentheses to control evaluation.
- [ ] Avoid common mistakes in mathematical expressions.
- [ ] Write clear and accurate Python code.

---

# 📖 What is Operator Precedence?

Operator precedence determines **the order in which Python evaluates operators** in an expression.

Just like in mathematics:

```
2 + 3 × 4 = 14
```

Multiplication happens before addition.

Python follows the same rule.

Example:

```python
print(2 + 3 * 4)
```

Output

```text
14
```

Python first calculates:

```text
3 * 4 = 12

2 + 12 = 14
```

---

# 📖 Why is Operator Precedence Important?

Without understanding precedence, your program may produce unexpected results.

Example

```python
print(10 - 2 * 3)
```

Output

```text
4
```

Calculation

```text
2 × 3 = 6

10 − 6 = 4
```

Not:

```text
10 − 2 = 8

8 × 3 = 24 ❌
```

---

# 📚 Python Operator Precedence Table

| Priority | Operators | Description |
|----------|-----------|-------------|
| 1 (Highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary operators |
| 4 | `*`, `/`, `//`, `%` | Multiplication, Division, Floor Division, Modulus |
| 5 | `+`, `-` | Addition, Subtraction |
| 6 | `<<`, `>>` | Bitwise Shift |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparison, Identity, Membership |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |
| 14 (Lowest) | `=` , `+=`, `-=`, `*=`, etc. | Assignment |

---

# 1️⃣ Parentheses (`()`)

Parentheses have the **highest precedence**.

### Example

```python
print((2 + 3) * 4)
```

Output

```text
20
```

Without parentheses

```python
print(2 + 3 * 4)
```

Output

```text
14
```

---

# 2️⃣ Exponentiation (`**`)

Exponentiation is evaluated before multiplication.

### Example

```python
print(2 + 3 ** 2)
```

Output

```text
11
```

Calculation

```text
3² = 9

2 + 9 = 11
```

---

# 3️⃣ Multiplication, Division, Floor Division, Modulus

These operators have the same precedence.

Python evaluates them **from left to right**.

Example

```python
print(20 / 2 * 5)
```

Output

```text
50.0
```

Calculation

```text
20 / 2 = 10

10 * 5 = 50
```

---

# 4️⃣ Addition and Subtraction

Performed after multiplication and division.

Example

```python
print(10 + 5 * 2)
```

Output

```text
20
```

Calculation

```text
5 * 2 = 10

10 + 10 = 20
```

---

# 5️⃣ Comparison Operators

Arithmetic operations are completed before comparisons.

Example

```python
print(5 + 5 == 10)
```

Output

```text
True
```

---

# 6️⃣ Logical Operators

Logical operators are evaluated after comparisons.

Example

```python
print(10 > 5 and 20 > 10)
```

Output

```text
True
```

---

# 📖 Associativity

When operators have the **same precedence**, Python follows associativity.

Most operators are evaluated **from left to right**.

Example

```python
print(20 / 5 * 2)
```

Output

```text
8.0
```

Calculation

```text
20 / 5 = 4

4 × 2 = 8
```

---

## Exception: Exponentiation (`**`)

Exponentiation is evaluated **from right to left**.

Example

```python
print(2 ** 3 ** 2)
```

Output

```text
512
```

Calculation

```text
3² = 9

2⁹ = 512
```

Not

```text
(2³)² = 64 ❌
```

---

# 📊 Step-by-Step Examples

## Example 1

```python
print(10 + 5 * 2)
```

Output

```text
20
```

---

## Example 2

```python
print((10 + 5) * 2)
```

Output

```text
30
```

---

## Example 3

```python
print(100 / 10 + 3)
```

Output

```text
13.0
```

---

## Example 4

```python
print(10 > 5 and 8 < 12)
```

Output

```text
True
```

---

## Example 5

```python
print(not 10 > 5)
```

Output

```text
False
```

Equivalent to:

```python
print(not (10 > 5))
```

---

# 📊 Summary Table

| Expression | Result |
|------------|--------|
| `2 + 3 * 4` | `14` |
| `(2 + 3) * 4` | `20` |
| `2 + 3 ** 2` | `11` |
| `20 / 2 * 5` | `50.0` |
| `5 + 5 == 10` | `True` |
| `10 > 5 and 8 < 12` | `True` |

---

# ⚠️ Common Mistakes

## ❌ Ignoring Parentheses

```python
print(2 + 3 * 4)
```

Output

```text
14
```

If you wanted 20:

```python
print((2 + 3) * 4)
```

---

## ❌ Forgetting That `**` Has Higher Precedence

```python
print(2 + 2 ** 3)
```

Output

```text
10
```

---

## ❌ Misunderstanding Logical Expressions

```python
print(5 > 2 and 10 < 20)
```

Python first evaluates:

```text
5 > 2

10 < 20
```

Then applies `and`.

---

# 💡 Best Practices

- Use parentheses to make expressions clear.
- Do not rely only on precedence when writing complex expressions.
- Break long expressions into smaller parts if needed.
- Use meaningful variable names.

---

# 🚀 Pro Tips

Whenever an expression looks confusing, use parentheses.

Instead of:

```python
result = a + b * c - d / e
```

Write:

```python
result = (a + (b * c)) - (d / e)
```

This improves readability.

---

# 🌍 Real-World Programs

## Calculate Total Bill

```python
price = 500
quantity = 3
discount = 200

total = price * quantity - discount

print(total)
```

Output

```text
1300
```

---

## Student Pass Check

```python
marks = 75

print(marks >= 35 and marks <= 100)
```

Output

```text
True
```

---

## Area of Rectangle

```python
length = 10
width = 5

area = length * width

print(area)
```

Output

```text
50
```

---

# ❓ Interview Questions

- [ ] What is operator precedence?
- [ ] Which operator has the highest precedence?
- [ ] Why are parentheses important?
- [ ] What is associativity?
- [ ] Why is `2 ** 3 ** 2` equal to `512`?

---

# 🏋️ Practice Programs

## Easy

```python
print(5 + 3 * 2)
```

---

```python
print((5 + 3) * 2)
```

---

```python
print(10 - 4 / 2)
```

---

## Medium

```python
print(2 ** 3 + 4)
```

---

```python
print(10 > 5 and 20 < 50)
```

---

```python
print(100 // 3 + 2)
```

---

## Advanced

```python
a = 5
b = 3
c = 2

result = (a + b) * c ** 2 - 10 / 5

print(result)
```

---

# 🎯 Challenge

Predict the output **before running** the code.

```python
print(5 + 2 * 3)
```

---

```python
print((5 + 2) * 3)
```

---

```python
print(2 ** 3 ** 2)
```

---

```python
print(20 // 3 + 5 * 2)
```

---

```python
print(10 > 5 and 8 == 8)
```

After predicting, run the programs and verify your answers.

---

# 📝 Assignment

- [x] Write five expressions using different arithmetic operators.
- [x] Use parentheses to change the result of an expression.
- [x] Practice exponentiation with `**`.
- [x] Combine comparison and logical operators.
- [x] Predict the output before executing each program.

---

# 📚 Summary

You learned:

- ✅ What operator precedence is.
- ✅ Python's precedence order.
- ✅ Parentheses have the highest precedence.
- ✅ Exponentiation is evaluated before multiplication.
- ✅ Arithmetic happens before comparison.
- ✅ Comparison happens before logical operators.
- ✅ Most operators are evaluated left to right.
- ✅ `**` is evaluated right to left.

---

# 🎯 Topic Completion Checklist

- [x] I understand operator precedence.
- [x] I know the order in which Python evaluates expressions.
- [x] I understand associativity.
- [x] I can use parentheses effectively.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 🎉 Phase 3 Completed!

You have successfully completed **Phase 3: Operators**.

## ✅ Topics Covered

- [x] Arithmetic Operators
- [x] Assignment Operators
- [x] Comparison Operators
- [x] Logical Operators
- [x] Identity Operators
- [x] Membership Operators
- [x] Bitwise Operators
- [x] Operator Precedence

---

