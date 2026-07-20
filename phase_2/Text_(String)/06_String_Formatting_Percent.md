# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Text (`str`) - Part 6:** String Formatting (`%` Operator)

**Difficulty:** ⭐ Beginner → ⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand string formatting.
- [ ] Use the `%` operator.
- [ ] Format strings, integers, and floats.
- [ ] Format multiple values.
- [ ] Avoid common mistakes.
- [ ] Know when to use `%` formatting.

---

# 📖 1. What is String Formatting?

String formatting means **inserting values into a string**.

Instead of writing:

```python
name = "Saniya"

print("My name is " + name)
```

We can write:

```python
name = "Saniya"

print("My name is %s" % name)
```

Output:

```text
My name is Saniya
```

---

# 📘 2. `%s` – String Placeholder

`%s` is used to insert strings.

```python
name = "Python"

print("Language: %s" % name)
```

Output:

```text
Language: Python
```

---

# 📗 3. `%d` – Integer Placeholder

`%d` is used for integers.

```python
age = 20

print("Age: %d" % age)
```

Output:

```text
Age: 20
```

---

# 📙 4. `%f` – Float Placeholder

`%f` is used for floating-point numbers.

```python
price = 99.99

print("Price: %f" % price)
```

Output:

```text
Price: 99.990000
```

By default, `%f` displays **6 digits after the decimal**.

---

# 📕 5. Controlling Decimal Places

Use `.2f` to show two decimal places.

```python
pi = 3.14159265

print("PI = %.2f" % pi)
```

Output:

```text
PI = 3.14
```

---

```python
print("PI = %.4f" % pi)
```

Output:

```text
PI = 3.1416
```

---

# 📦 6. Multiple Values

Use a tuple.

```python
name = "Saniya"
age = 20

print("Name: %s Age: %d" % (name, age))
```

Output:

```text
Name: Saniya Age: 20
```

---

Another example:

```python
name = "Rahul"
marks = 95

print("%s scored %d marks." % (name, marks))
```

Output:

```text
Rahul scored 95 marks.
```

---

# 🌍 7. Real-World Examples

### Student Record

```python
name = "Saniya"
course = "AI ML"

print("Student: %s | Course: %s" % (name, course))
```

---

### Product

```python
product = "Laptop"
price = 58999.50

print("%s costs ₹%.2f" % (product, price))
```

Output:

```text
Laptop costs ₹58999.50
```

---

# ⚠️ 8. Common Mistakes

## ❌ Wrong Placeholder

```python
age = "20"

print("%d" % age)
```

This raises a `TypeError` because `%d` expects an integer.

Correct:

```python
print("%s" % age)
```

or

```python
age = 20
print("%d" % age)
```

---

## ❌ Forgetting the Tuple

Wrong:

```python
print("%s %d" % name, age)
```

Correct:

```python
print("%s %d" % (name, age))
```

---

# 💡 9. Best Practices

- `%` formatting is useful for reading older Python code.
- In modern Python, prefer **f-strings** whenever possible.
- Use `.2f` for prices and measurements.

---

# 🚀 10. Pro Tips

You can combine different placeholders.

```python
name = "Saniya"
age = 20
height = 165.75

print("Name: %s | Age: %d | Height: %.1f cm" %
      (name, age, height))
```

Output:

```text
Name: Saniya | Age: 20 | Height: 165.8 cm
```

---

# 🧠 Memory Trick

```
%s → String

%d → Integer

%f → Float
```

---

# ❓ Interview Questions

- [ ] What is string formatting?
- [ ] What does `%s` represent?
- [ ] What does `%d` represent?
- [ ] What does `%f` represent?
- [ ] Why is `%` formatting considered old-style?

---

# 🏋️ Practice Programs

## Easy

```python
name = "Python"

print("Language: %s" % name)
```

---

```python
age = 25

print("Age: %d" % age)
```

---

## Medium

```python
price = 123.4567

print("Price: %.2f" % price)
```

---

```python
name = "Saniya"
marks = 92

print("%s scored %d marks." % (name, marks))
```

---

## Advanced

```python
name = "Saniya"
course = "AI ML"
cgpa = 8.92

print("Student: %s | Course: %s | CGPA: %.2f"
      % (name, course, cgpa))
```

---

# 🎯 Challenge

Create variables:

```python
name = "Your Name"
age = 20
height = 165.5
city = "Your City"
```

Print:

```
Name:
Age:
Height:
City:
```

using `%` formatting.

---

# 📝 Assignment

Complete the following:

- [x] Format a string using `%s`.
- [x] Format an integer using `%d`.
- [x] Format a float using `%.2f`.
- [x] Print multiple values in one formatted string.
- [x] Explain the difference between `%s`, `%d`, and `%f`.

---

# 📚 Summary

You learned:

- What string formatting is.
- `%s`, `%d`, `%f`.
- Formatting multiple values.
- Controlling decimal places.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know what string formatting is.
- [x] I can use `%s`, `%d`, and `%f`.
- [x] I can format multiple values.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 7: `str.format()` Method**