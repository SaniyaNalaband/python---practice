# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 4:** Running Python Programs

---

# 📚 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand what it means to run a Python program.
- [ ] Learn different ways to run Python programs.
- [ ] Run Python programs using VS Code.
- [ ] Run Python programs using the terminal.
- [ ] Understand the Python execution process.
- [ ] Identify and solve common errors.

---

# 🤔 1. What Does "Running a Python Program" Mean?

Writing a Python program is only the first step.

A program becomes useful when it is **executed**.

**Running a Python program** means asking the Python Interpreter to read your code, execute it line by line, and produce the desired output.

For example:

```python
print("Hello, World!")
```

When executed, Python displays:

```text
Hello, World!
```

---

# ⚙️ 2. How Python Executes Your Code

Whenever you run a Python file, the following happens:

```text
Python Code (.py file)
        │
        ▼
Python Interpreter
        │
        ▼
Bytecode (.pyc)
        │
        ▼
Python Virtual Machine (PVM)
        │
        ▼
Output
```

### Explanation

1. You write Python code.
2. The Python Interpreter checks the code.
3. Python converts it into **Bytecode**.
4. The **Python Virtual Machine (PVM)** executes the bytecode.
5. The result is displayed.

---

# 📂 3. Python File Extension

Python programs are saved using the extension:

```text
.py
```

Examples:

```text
hello.py
calculator.py
student.py
game.py
```

---

# 💻 4. Running a Program in VS Code

### Step 1

Open VS Code.

---

### Step 2

Open your project folder.

---

### Step 3

Create a file.

Example:

```text
hello.py
```

---

### Step 4

Write:

```python
print("Hello from VS Code!")
```

---

### Step 5

Save the file.

Shortcut:

```
Ctrl + S
```

---

### Step 6

Run the program by:

- Clicking the ▶ Run button
- OR

Open the terminal:

```
Ctrl + `
```

Type:

```bash
python hello.py
```

Output:

```text
Hello from VS Code!
```

---

# 🖥️ 5. Running from Command Prompt / PowerShell

Open:

- Command Prompt
- PowerShell

Navigate to the folder:

```bash
cd Desktop
```

Example:

```bash
cd Python
```

Run:

```bash
python hello.py
```

Output:

```text
Hello from VS Code!
```

---

# 🐍 6. Running Using the Python Launcher

Windows also installs the Python Launcher.

Instead of:

```bash
python hello.py
```

You can run:

```bash
py hello.py
```

Both commands execute the program.

---

# ▶️ 7. Running from IDLE

Python also includes **IDLE**.

Steps:

1. Open IDLE.
2. Click:

```
File → New File
```

3. Write:

```python
print("Hello")
```

4. Save the file.
5. Press:

```
F5
```

Output:

```text
Hello
```

---

# ⚠️ 8. Common Errors

## Error 1

```text
python is not recognized...
```

### Cause

Python is not added to PATH.

### Solution

Reinstall Python and enable:

```
Add Python to PATH
```

---

## Error 2

```text
File Not Found
```

### Cause

You are in the wrong folder.

### Solution

Navigate to the correct directory using:

```bash
cd folder_name
```

---

## Error 3

```text
SyntaxError
```

Example:

```python
print("Hello"
```

Correct:

```python
print("Hello")
```

---

## Error 4

```text
IndentationError
```

Example:

```python
if True:
print("Hello")
```

Correct:

```python
if True:
    print("Hello")
```

---

# 💡 9. Tips for Beginners

✅ Save your file before running.

✅ Use meaningful filenames.

Examples:

```text
calculator.py
student.py
```

Avoid names like:

```text
abc.py
test1.py
```

✅ Keep one project per folder.

---

# 📌 Summary

Running a Python program means executing the code using the Python Interpreter.

You can run programs using:

- VS Code
- Terminal
- Command Prompt
- PowerShell
- IDLE
- Python Launcher (`py`)

Python executes code in this order:

```text
Source Code
      ↓
Interpreter
      ↓
Bytecode
      ↓
Python Virtual Machine
      ↓
Output
```

---

# 📝 Practice Questions

- [ ] What does it mean to run a Python program?
- [ ] Which file extension is used for Python programs?
- [ ] Name four ways to run a Python program.
- [ ] What is Bytecode?
- [ ] What is the Python Virtual Machine (PVM)?
- [ ] What does the Python Interpreter do?
- [ ] What causes a File Not Found error?
- [ ] Why should you save your file before running it?

---

# 💻 Practice Programs

## Program 1

```python
print("Python is awesome!")
```

---

## Program 2

```python
print("Welcome")
print("to")
print("Python")
```

---

## Program 3

```python
print(100)
print(200)
print(300)
```

---

## Program 4

```python
print("Name:", "Saniya")
print("Age:", 20)
```

---

# 💼 Assignment

Complete the following tasks:

- [x] Create a file named `hello.py`.
- [x] Write a program that prints your name.
- [x] Run the program using the Run button.
- [x] Run the same program using the terminal.
- [x] Run the same program using `py hello.py`.
- [x] Explain the Python execution process in your own words.

---

# 🎯 Topic Completion Checklist

Mark this topic as completed only if:

- [x] I know what it means to run a Python program.
- [x] I know the `.py` file extension.
- [x] I can run a Python program in VS Code.
- [x] I can run a program using the terminal.
- [x] I understand the Python execution process.
- [x] I know how to solve common errors.
- [x] I completed the practice questions.
- [x] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 5: Python Interactive Shell (REPL)**

---

## ⭐ Keep Learning

> **"Writing code is only half the job—the other half is running, testing, and improving it."** 🚀