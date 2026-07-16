# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 20:** Type Conversion

**Difficulty:** ⭐⭐ Beginner to Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what type conversion is.
- [ ] Learn why Python performs type conversion.
- [ ] Understand automatic type conversion.
- [ ] Observe how Python converts data types during expressions.
- [ ] Differentiate type conversion from type casting.
- [ ] Avoid common beginner mistakes.

---

# 📖 1. What is Type Conversion?

**Type Conversion** is the process where **Python automatically changes one data type into another** when it is necessary.

The important word here is:

> **Automatically**

You **do not** ask Python to convert the value.

Python decides to convert it.

---

# 🤔 2. Why Does Python Perform Type Conversion?

Python wants to avoid losing information.

Example:

```python
print(10 + 5.5)
```

Here:

- `10` is an `int`
- `5.5` is a `float`

Python converts:

```python
10
```

into

```python
10.0
```

Then performs:

```python
10.0 + 5.5
```

Output:

```text
15.5
```

---

# 🔄 3. Automatic Type Conversion

Example:

```python
x = 20
y = 3.5

result = x + y

print(result)
```

Output:

```text
23.5
```

Python automatically converts:

```text
20 (int)
```

↓

```text
20.0 (float)
```

---

# 📊 4. Memory View

```python
x = 20
y = 3.5

result = x + y
```

Python internally works like this:

```
20 (int)
↓

20.0 (float)

↓

20.0 + 3.5

↓

23.5
```

---

# 💻 5. More Examples

## Integer + Float

```python
print(5 + 2.5)
```

Output:

```text
7.5
```

---

## Float + Integer

```python
print(4.5 + 6)
```

Output:

```text
10.5
```

---

## Integer + Complex

```python
print(10 + 3j)
```

Output:

```text
(10+3j)
```

Python converts the integer into a complex number internally.

---

# 🚫 6. When Type Conversion Does NOT Happen

Python cannot automatically convert incompatible data.

Example:

```python
print("10" + 5)
```

Output:

```text
TypeError
```

Reason:

Python does **not** automatically convert a string into a number.

---

Another example:

```python
print(True + 5)
```

Output:

```text
6
```

Why?

Because in Python:

```text
True = 1
False = 0
```

---

# 📌 7. Data Type Promotion

Python follows this order when promoting numeric types:

```
bool
   ↓
int
   ↓
float
   ↓
complex
```

Examples:

```python
5 + 2.5
```

↓

```
float
```

---

```python
5 + 3j
```

↓

```
complex
```

---

# 🌍 8. Real-World Example

Imagine adding money:

```python
wallet = 500
bonus = 250.75

total = wallet + bonus

print(total)
```

Output:

```text
750.75
```

Python converts:

```
500
```

↓

```
500.0
```

before adding.

---

# ⚠️ 9. Common Mistakes

## ❌ Expecting Strings to Convert Automatically

```python
print("100" + 50)
```

Output:

```text
TypeError
```

---

## ❌ Confusing Conversion with Casting

Automatic:

```python
10 + 2.5
```

Manual:

```python
int("10")
```

We'll learn manual conversion in the next topic.

---

# 💡 10. Best Practices

✅ Let Python perform automatic conversion when working with compatible numeric types.

✅ Don't assume strings will automatically become numbers.

---

# 🚀 11. Pro Tips

Check the result type.

```python
result = 10 + 2.5

print(type(result))
```

Output:

```text
<class 'float'>
```

---

# 🧠 Memory Trick

Remember:

```
Type Conversion

↓

Python decides
```

```
Type Casting

↓

You decide
```

---

# ❓ Interview Questions

- [ ] What is type conversion?
- [ ] Is type conversion automatic or manual?
- [ ] Why does Python perform type conversion?
- [ ] What happens when an integer and float are added?
- [ ] Why does `"10" + 5` produce an error?

---

# 🏋️ Practice Programs

## Easy

```python
print(10 + 5.5)
```

---

```python
print(type(10 + 5.5))
```

---

## Medium

```python
x = 50
y = 25.5

print(x + y)
print(type(x + y))
```

---

```python
print(5 + True)
```

---

## Advanced

Predict the output:

```python
print(10 + 2.5)
print(type(10 + 2.5))

print(5 + 3j)
print(type(5 + 3j))
```

---

# 📝 Assignment

Complete the following:

- [x] Add an integer and a float.
- [x] Check the result type.
- [x] Add an integer and a complex number.
- [x] Try adding a string and an integer and explain the error.
- [x] Explain type conversion in your own words.

---

# 📚 Summary

In this lesson, you learned:

- What type conversion is.
- Automatic type conversion.
- Data type promotion.
- Compatible and incompatible conversions.
- Common mistakes.
- Difference between conversion and casting.

---

# 🎯 Topic Completion Checklist

- [x] I know what type conversion is.
- [x] I understand automatic conversion.
- [x] I know Python's numeric promotion order.
- [x] I know when conversion does not happen.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 21: Type Casting**

---

## ⭐ Quote of the Day

> **"When Python can safely convert data automatically, that's type conversion. When you tell Python to convert it, that's type casting."** 🐍