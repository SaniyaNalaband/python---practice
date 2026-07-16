# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 5:** Python Interactive Shell (REPL)

---

# 📚 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what the Python Interactive Shell (REPL) is.
- [ ] Know what REPL stands for.
- [ ] Start the Python Interactive Shell.
- [ ] Execute Python statements interactively.
- [ ] Exit the Interactive Shell.
- [ ] Understand when to use REPL and when to use `.py` files.
- [ ] Identify common beginner mistakes.

---

# 🤔 1. What is the Python Interactive Shell?

The **Python Interactive Shell** is an environment where you can write and execute Python code **one line at a time**.

Unlike a `.py` file, you don't need to save your code before running it.

As soon as you press **Enter**, Python executes the statement immediately.

Think of it as a calculator for Python.

---

# 📖 2. What Does REPL Stand For?

REPL stands for:

| Letter | Meaning |
|---------|----------|
| **R** | Read |
| **E** | Evaluate |
| **P** | Print |
| **L** | Loop |

### How REPL Works

```
You Type Code
       ↓
Python Reads It
       ↓
Python Evaluates It
       ↓
Python Prints the Result
       ↓
Waits for Your Next Input
```

This cycle repeats until you exit the shell.

---

# 🚀 3. How to Open the Python Interactive Shell

### Method 1: Using Command Prompt / PowerShell

Open:

- Command Prompt
- PowerShell
- VS Code Terminal

Type:

```bash
python
```

or

```bash
py
```

If Python is installed correctly, you'll see something like:

```text
Python 3.12.4 (tags/v3.12.4)
>>>
```

The `>>>` symbol is called the **Python Prompt**.

It means Python is waiting for your next command.

---

# 💻 4. Writing Your First Command

Type:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

Python executes it immediately.

---

# 🔢 5. Using REPL as a Calculator

Example:

```python
5 + 3
```

Output:

```text
8
```

Another example:

```python
10 * 5
```

Output:

```text
50
```

More examples:

```python
100 / 5
```

Output:

```text
20.0
```

```python
7 % 3
```

Output:

```text
1
```

---

# 🧪 6. Trying Multiple Commands

```python
print("Python")
```

Output:

```text
Python
```

```python
print("Learning")
```

Output:

```text
Learning
```

```python
print("REPL")
```

Output:

```text
REPL
```

Each command is executed immediately.

---

# 📌 7. Why Use REPL?

REPL is useful for:

- ✅ Testing small code snippets
- ✅ Learning Python
- ✅ Performing calculations
- ✅ Experimenting with new functions
- ✅ Debugging simple problems

Professional developers also use REPL frequently.

---

# 📄 8. REPL vs Python File

| REPL | Python File (`.py`) |
|------|----------------------|
| Executes one line at a time | Executes the entire file |
| No need to save | Must be saved |
| Best for testing | Best for projects |
| Temporary | Permanent |
| Great for beginners | Great for real applications |

---

# 🚪 9. How to Exit REPL

### Windows

Press:

```
Ctrl + Z
```

Then press:

```
Enter
```

---

### macOS / Linux

Press:

```
Ctrl + D
```

or type:

```python
exit()
```

or

```python
quit()
```

---

# ⚠️ 10. Common Beginner Mistakes

### ❌ Typing Python Commands in the Wrong Place

Wrong:

```text
C:\Users\Saniya>
print("Hello")
```

This gives an error because you're in the Windows Command Prompt.

Correct:

```text
>>> print("Hello")
```

Python commands should be entered **after** the `>>>` prompt.

---

### ❌ Forgetting Quotes

Wrong:

```python
print(Hello)
```

Output:

```text
NameError
```

Correct:

```python
print("Hello")
```

---

### ❌ Expecting Variables to Stay Forever

Variables created in REPL disappear when you close the shell.

If you need to keep your code, save it in a `.py` file.

---

# 💡 11. Tips

✅ Use REPL for quick experiments.

✅ Use `.py` files for assignments and projects.

✅ Don't be afraid to try different commands.

Experimenting is one of the best ways to learn Python.

---

# 📌 Summary

The Python Interactive Shell (REPL):

- Executes Python code instantly.
- Is perfect for beginners.
- Is useful for testing ideas.
- Does not require saving files.
- Uses the `>>>` prompt.

---

# 📝 Practice Questions

- [ ] What does REPL stand for?
- [ ] What is the Python Interactive Shell?
- [ ] What is the purpose of the `>>>` prompt?
- [ ] How do you open the Python Interactive Shell?
- [ ] Name three uses of REPL.
- [ ] What is the difference between REPL and a `.py` file?
- [ ] How do you exit the REPL?
- [ ] Why do professional developers use REPL?

---

# 💻 Hands-on Practice

Open the Python Interactive Shell and try these commands:

```python
print("Hello")
```

```python
10 + 20
```

```python
25 * 4
```

```python
100 / 5
```

```python
50 - 12
```

```python
7 % 2
```

```python
2 ** 5
```

```python
print("Python is fun!")
```

---

# 💼 Assignment

Complete the following:

- [x] Open the Python Interactive Shell.
- [x] Run all the practice commands.
- [x] Perform three calculations of your own.
- [x] Print your name.
- [x] Exit the REPL using `exit()` or `quit()`.
- [x] Explain the difference between REPL and a `.py` file in your own words.

---

# 🎯 Topic Completion Checklist

Mark this topic as completed only if:

- [x] I know what REPL stands for.
- [x] I can open the Python Interactive Shell.
- [x] I can execute Python commands.
- [x] I know when to use REPL.
- [x] I know when to use `.py` files.
- [x] I know how to exit the REPL.
- [x] I completed the practice questions.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 6: Writing Your First Python Program**

---

## ⭐ Keep Learning

> **"The best way to learn programming is by experimenting. REPL lets you do that instantly."** 🐍