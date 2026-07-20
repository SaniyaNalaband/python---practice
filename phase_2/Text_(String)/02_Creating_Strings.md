# 🐍 Python Master Course

> **Phase 2:** Data Types  
> **Text (`str`) - Part 2:** Creating Strings

**Difficulty:** ⭐ Beginner → ⭐⭐ Intermediate

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Create strings using single quotes.
- [ ] Create strings using double quotes.
- [ ] Create multiline strings.
- [ ] Use triple quotes correctly.
- [ ] Know when to use each type of quote.
- [ ] Avoid common mistakes.

---

# 📖 1. Ways to Create Strings

Python provides four common ways to create strings.

```
String

├── Single Quotes (' ')
├── Double Quotes (" ")
├── Triple Single Quotes (''' ''')
└── Triple Double Quotes (""" """)
```

All of them create objects of type `str`.

---

# 2. Single Quotes

Use single quotes for simple text.

```python
name = 'Saniya'

print(name)
print(type(name))
```

Output:

```text
Saniya
<class 'str'>
```

---

Another example:

```python
city = 'Mysuru'

print(city)
```

---

# 3. Double Quotes

Double quotes work exactly like single quotes.

```python
language = "Python"

print(language)
```

Output:

```text
Python
```

---

Another example:

```python
country = "India"

print(country)
```

---

# 4. Single vs Double Quotes

Both produce the same result.

```python
a = 'Python'
b = "Python"

print(a)
print(b)
```

Output:

```text
Python
Python
```

Both are strings.

```python
print(type(a))
print(type(b))
```

Output:

```text
<class 'str'>
<class 'str'>
```

---

# 5. Why Do We Have Two Types of Quotes?

They make it easier to include quotation marks inside strings.

Example:

```python
sentence = "It's a beautiful day."

print(sentence)
```

Output:

```text
It's a beautiful day.
```

Because the string uses **double quotes**, the apostrophe (`'`) in `It's` doesn't end the string.

Another example:

```python
quote = 'He said, "Python is awesome!"'

print(quote)
```

Output:

```text
He said, "Python is awesome!"
```

---

# 6. Triple Single Quotes

Triple single quotes are useful for **multiline strings**.

```python
message = '''
Hello
Welcome
to Python
'''

print(message)
```

Output:

```text
Hello
Welcome
to Python
```

---

# 7. Triple Double Quotes

Triple double quotes also create multiline strings.

```python
poem = """
Roses are red,
Violets are blue,
Python is fun,
And powerful too.
"""

print(poem)
```

---

# 8. Multiline Strings

Without triple quotes:

❌ Wrong

```python
text = "Hello
World"
```

This causes a `SyntaxError`.

Correct:

```python
text = """Hello
World"""

print(text)
```

---

# 9. Empty String

You can create an empty string.

```python
empty = ""

print(empty)
print(type(empty))
```

Output:

```text

<class 'str'>
```

---

# 10. String Constructor

Python provides the `str()` constructor.

```python
text = str("Python")

print(text)
```

Output:

```text
Python
```

---

You can also convert values into strings.

```python
age = str(20)

print(age)
print(type(age))
```

Output:

```text
20
<class 'str'>
```

---

```python
price = str(99.99)

print(price)
```

Output:

```text
99.99
```

---

# 🌍 11. Real-World Examples

Student Name

```python
student_name = "Saniya"
```

---

Address

```python
address = """
House No. 10
Main Road
Mysuru
"""
```

---

Email

```python
email = "student@example.com"
```

---

Password

```python
password = "Python@123"
```

---

# ⚠️ 12. Common Mistakes

## ❌ Missing Closing Quote

Wrong:

```python
name = "Python
```

Result:

```text
SyntaxError
```

---

## ❌ Mixing Quotes Incorrectly

Wrong:

```python
text = "Python'
```

Result:

```text
SyntaxError
```

Always open and close with the same type of quote.

---

## ❌ Using Single Quotes with Apostrophes

Wrong:

```python
text = 'It's raining'
```

Python thinks the string ends after `It`.

Correct:

```python
text = "It's raining"
```

or

```python
text = 'It\'s raining'
```

---

# 💡 13. Best Practices

✅ Use double quotes if your text contains apostrophes.

```python
"It's easy."
```

---

✅ Use triple quotes for multiline text.

---

✅ Use meaningful variable names.

```python
student_name = "Saniya"
```

instead of

```python
x = "Saniya"
```

---

# 🚀 14. Pro Tips

Use triple quotes for documentation strings (docstrings).

```python
def greet():
    """Prints a welcome message."""
    print("Hello!")
```

Docstrings are widely used in professional Python code.

---

# 🧠 Memory Trick

```
' '

↓

Single Line

----------------

" "

↓

Single Line

----------------

''' '''

↓

Multiline

----------------

""" """

↓

Multiline
```

---

# ❓ Interview Questions

- [ ] How many ways can you create a string in Python?
- [ ] What is the difference between single and double quotes?
- [ ] Why are triple quotes used?
- [ ] What is `str()`?
- [ ] When should you use double quotes instead of single quotes?

---

# 🏋️ Practice Programs

## Easy

```python
name = "Saniya"

print(name)
```

---

```python
city = 'Mysuru'

print(city)
```

---

## Medium

```python
message = """
Welcome
to
Python
"""

print(message)
```

---

```python
number = str(500)

print(number)
print(type(number))
```

---

## Advanced

```python
bio = """
Name   : Saniya
Course : AI ML and Data Science
City   : Mysuru
"""

print(bio)

print(type(bio))
print(len(bio))
```

---

# 🎯 Challenge

Create the following using strings:

- Your full name
- Your college name
- Your address (multiline)
- A motivational quote containing quotation marks
- Your age converted to a string using `str()`

Print each one.

---

# 📝 Assignment

Complete the following:

- [x] Create strings using single quotes.
- [x] Create strings using double quotes.
- [x] Create a multiline string.
- [x] Convert an integer to a string.
- [x] Convert a float to a string.
- [x] Create an empty string.
- [x] Explain when to use triple quotes.

---

# 📚 Summary

In this lesson, you learned:

- Four ways to create strings.
- Single vs double quotes.
- Triple quotes.
- Multiline strings.
- `str()` constructor.
- Common mistakes.
- Best practices.

---

# 🎯 Topic Completion Checklist

- [x] I know all the ways to create strings.
- [x] I know when to use each type of quote.
- [x] I can create multiline strings.
- [x] I can convert values using `str()`.
- [x] I completed the practice programs.
- [x] I completed the assignment.

---

# 📚 Next Lesson

➡️ **Part 3: String Indexing**