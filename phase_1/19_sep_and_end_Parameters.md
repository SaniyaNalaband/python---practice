# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 19:** `sep` and `end` Parameters

**Difficulty:** ⭐ Beginner

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand the `sep` parameter.
- [ ] Understand the `end` parameter.
- [ ] Change the separator between printed values.
- [ ] Change what `print()` ends with.
- [ ] Combine `sep` and `end`.
- [ ] Avoid common mistakes.

---

# 📖 1. Introduction

The `print()` function has many optional parameters.

The two most commonly used are:

- `sep`
- `end`

General syntax:

```python
print(objects, sep=' ', end='\n')
```

By default:

- `sep = " "` (one space)
- `end = "\n"` (new line)

---

# 📌 2. What is `sep`?

`sep` stands for **separator**.

It tells Python **what to print between multiple values**.

Default:

```python
print("Python", "Java", "C++")
```

Output:

```
Python Java C++
```

A space is automatically added.

---

# 💻 3. Using `sep`

### Comma

```python
print("Python", "Java", "C++", sep=", ")
```

Output:

```
Python, Java, C++
```

---

### Dash

```python
print(10, 20, 30, sep="-")
```

Output:

```
10-20-30
```

---

### Arrow

```python
print("A", "B", "C", sep=" -> ")
```

Output:

```
A -> B -> C
```

---

### Star

```python
print(1, 2, 3, 4, sep=" * ")
```

Output:

```
1 * 2 * 3 * 4
```

---

### No Space

```python
print("Python", "Master", sep="")
```

Output:

```
PythonMaster
```

---

# 📌 4. What is `end`?

Normally, every `print()` ends with a **new line**.

Example:

```python
print("Hello")
print("World")
```

Output:

```
Hello
World
```

This happens because:

```python
end="\n"
```

is used automatically.

---

# 💻 5. Using `end`

### Space

```python
print("Hello", end=" ")
print("World")
```

Output:

```
Hello World
```

---

### Dash

```python
print("Python", end="-")
print("Programming")
```

Output:

```
Python-Programming
```

---

### Arrow

```python
print("Step1", end=" -> ")
print("Step2")
```

Output:

```
Step1 -> Step2
```

---

### No Ending Character

```python
print("Hello", end="")
print("World")
```

Output:

```
HelloWorld
```

---

# 📌 6. Using Both `sep` and `end`

```python
print("Python", "Java", sep=" | ", end=" <-- Languages")
```

Output:

```
Python | Java <-- Languages
```

---

Another example:

```python
print(1, 2, 3, sep="-", end=" End")
```

Output:

```
1-2-3 End
```

---

# 🌍 7. Real-World Examples

### Student Details

```python
print("Name", "Age", "City", sep=" | ")
```

Output:

```
Name | Age | City
```

---

### CSV Format

```python
print("Saniya", 20, "Mysuru", sep=",")
```

Output:

```
Saniya,20,Mysuru
```

---

### Countdown

```python
print(3, end="...")
print(2, end="...")
print(1)
```

Output:

```
3...2...1
```

---

# ⚠️ 8. Common Mistakes

## ❌ Forgetting Quotes

Wrong:

```python
print("A", "B", sep=-)
```

Correct:

```python
print("A", "B", sep="-")
```

---

## ❌ Using `end` Without Quotes

Wrong:

```python
print("Hello", end=!)
```

Correct:

```python
print("Hello", end="!")
```

---

## ❌ Expecting `sep` to Work With One Value

```python
print("Python", sep="-")
```

Output:

```
Python
```

`sep` only works when **multiple values** are printed.

---

# 💡 9. Best Practices

✅ Use `sep` to format output neatly.

✅ Use `end` for progress messages and custom layouts.

✅ Keep separators simple and readable.

---

# 🚀 10. Pro Tips

You can use escape characters inside `sep` and `end`.

Example:

```python
print("A", "B", sep="\n")
```

Output:

```
A
B
```

---

```python
print("Hello", end="\t")
print("World")
```

Output:

```
Hello    World
```

---

# 🧠 Memory Trick

```
sep
↓

Separates values

-------------------

end
↓

Ends the print statement
```

Remember:

**SEP = Separate**

**END = Ending**

---

# ❓ Interview Questions

- [ ] What is the default value of `sep`?
- [ ] What is the default value of `end`?
- [ ] What does `sep` do?
- [ ] What does `end` do?
- [ ] Can `sep` and `end` be used together?
- [ ] Give one real-world use of `end`.

---

# 🏋️ Practice Programs

## Easy

```python
print("Python", "Java", sep=", ")
```

---

```python
print(10, 20, 30, sep="-")
```

---

```python
print("A", "B", "C", sep="*")
```

---

## Medium

```python
print("Hello", end=" ")
print("World")
```

---

```python
print("Python", end=" -> ")
print("Programming")
```

---

## Advanced

```python
print("Name", "Age", "City", sep="\t", end="\n")
print("Saniya", 20, "Mysuru", sep="\t")
```

---

## Challenge

Create the following output using `sep` and `end`:

```
Python -> Java -> C++
1,2,3,4,5
Loading...
Done!
```

---

# 📝 Assignment

Complete the following:

- [x] Print five values using different separators.
- [x] Print two lines on the same line using `end`.
- [x] Combine `sep` and `end` in one program.
- [x] Create a simple table using `sep="\t"`.
- [x] Explain the difference between `sep` and `end`.

---

# 📚 Summary

In this lesson, you learned:

- What `sep` is.
- What `end` is.
- Default values of `sep` and `end`.
- Using custom separators.
- Printing without moving to the next line.
- Combining `sep` and `end`.

---

# 🎯 Topic Completion Checklist

- [x] I know what `sep` does.
- [x] I know what `end` does.
- [x] I know their default values.
- [x] I can use both together.
- [x] I completed all practice programs.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 20: Type Conversion**

---

## ⭐ Quote of the Day

> **"Small parameters like `sep` and `end` can make your program's output much more readable and professional."** 🐍