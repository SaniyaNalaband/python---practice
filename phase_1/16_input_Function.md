# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 16:** The `input()` Function

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the `input()` function is.
- [ ] Learn the syntax of `input()`.
- [ ] Accept input from the user.
- [ ] Store user input in variables.
- [ ] Understand that `input()` always returns a string.
- [ ] Avoid common beginner mistakes.
- [ ] Prepare for type conversion in later topics.

---

# 📖 1. What is the `input()` Function?

The `input()` function is a **built-in Python function** used to receive data from the user through the keyboard.

Think of it like asking the user a question.

Example:

```
What is your name?
```

The user types an answer, and Python stores it.

---

# 🤔 2. Why Do We Use `input()`?

Without `input()`, your programs only work with fixed values.

Example:

```python
name = "Saniya"
print(name)
```

The program always prints:

```
Saniya
```

Using `input()`:

```python
name = input("Enter your name: ")

print(name)
```

Now every user can enter their own name.

---

# 📝 3. Syntax

```python
input("Message")
```

General syntax:

```python
variable = input("Prompt")
```

Example:

```python
name = input("Enter your name: ")
```

---

# 💻 4. Basic Example

```python
name = input("Enter your name: ")

print(name)
```

Output:

```
Enter your name: Saniya
Saniya
```

---

# 💻 5. Printing a Greeting

```python
name = input("Enter your name: ")

print("Hello", name)
```

Output:

```
Enter your name: Rahul
Hello Rahul
```

---

# 💻 6. Taking Multiple Inputs

```python
name = input("Enter your name: ")
city = input("Enter your city: ")

print(name)
print(city)
```

Output:

```
Enter your name: Saniya
Enter your city: Mysuru

Saniya
Mysuru
```

---

# 📦 7. Storing User Input

The value entered by the user is stored in a variable.

```python
college = input("Enter your college: ")

print(college)
```

---

# ⚠️ 8. Important: `input()` Always Returns a String

This is one of the most important things to remember.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```
20
```

Output:

```
<class 'str'>
```

Even though the user typed a number, Python stores it as a **string**.

We'll learn how to convert it into an integer in the **Type Conversion** topic.

---

# 🌍 9. Real-World Example

```python
name = input("Enter your name: ")
course = input("Enter your course: ")

print("Student Name:", name)
print("Course:", course)
```

Output:

```
Enter your name: Saniya
Enter your course: BCA

Student Name: Saniya
Course: BCA
```

---

# ⚠️ 10. Common Mistakes

## ❌ Forgetting Parentheses

Wrong:

```python
name = input
```

Correct:

```python
name = input("Enter your name: ")
```

---

## ❌ Forgetting to Store the Input

Wrong:

```python
input("Enter your name: ")
```

The value is not saved anywhere.

Correct:

```python
name = input("Enter your name: ")
```

---

## ❌ Assuming the Input Is a Number

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```
<class 'str'>
```

Remember: `input()` always returns a string.

---

# 💡 11. Best Practices

✅ Give clear prompts.

Good:

```python
input("Enter your age: ")
```

Instead of:

```python
input("Age:")
```

---

✅ Store the input in meaningful variable names.

```python
student_name = input("Enter your name: ")
```

---

# 🚀 12. Pro Tips

Use prompts that tell the user exactly what to enter.

Example:

```python
marks = input("Enter your marks out of 100: ")
```

This reduces confusion.

---

# 🧠 Memory Trick

Remember:

```
input()

↓

Receives data from the user
```

Think:

> **"Input goes into the program."**

---

# ❓ Interview Questions

- [ ] What is the `input()` function?
- [ ] Why do we use `input()`?
- [ ] What does `input()` return?
- [ ] Can `input()` return an integer automatically?
- [ ] Why do we store input in variables?

---

# 🏋️ Practice Programs

## Easy

```python
name = input("Enter your name: ")

print(name)
```

---

```python
city = input("Enter your city: ")

print(city)
```

---

## Medium

```python
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name)
print(age)
```

---

```python
college = input("Enter your college: ")

print("College:", college)
```

---

## Advanced

```python
name = input("Enter your name: ")
city = input("Enter your city: ")
course = input("Enter your course: ")

print("Name:", name)
print("City:", city)
print("Course:", course)
```

---

## Challenge

Write a program that asks the user for:

- Name
- Age
- City
- College
- Course

Then display all the information in a neat format.

---

# 📝 Assignment

Complete the following:

- [ ] Ask the user for their name.
- [ ] Ask the user for their age.
- [ ] Ask the user for their city.
- [ ] Ask the user for their college.
- [ ] Display all the information using `print()`.
- [ ] Check the data type of the age using `type()`.

---

# 📚 Summary

In this lesson, you learned:

- What `input()` is.
- Why `input()` is used.
- How to receive user input.
- How to store input in variables.
- That `input()` always returns a string.
- Best practices.
- Common mistakes.

---

# 🎯 Topic Completion Checklist

- [ ] I know what the `input()` function is.
- [ ] I can accept user input.
- [ ] I can store input in variables.
- [ ] I know that `input()` returns a string.
- [ ] I completed all practice programs.
- [ ] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 17: Escape Characters**

---

## ⭐ Quote of the Day

> **"Great programs don't just display information—they listen to the user too."** 🐍