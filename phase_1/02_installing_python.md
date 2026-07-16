# 🐍 Python Master Course

> **Phase 1:** Python Basics  
> **Topic 2:** Installing Python

---

# 📚 Learning Objectives

By the end of this lesson, you will be able to:

- [ ] Understand why Python needs to be installed.
- [ ] Download Python from the official website.
- [ ] Install Python correctly.
- [ ] Add Python to PATH.
- [ ] Verify the installation.
- [ ] Understand the Python Launcher.
- [ ] Understand what gets installed.
- [ ] Troubleshoot common installation problems.

---

# 🤔 1. Why Do We Need to Install Python?

Your computer cannot understand Python code by itself.

For example:

```python
print("Hello, World!")
```

The computer only understands **machine language (0s and 1s)**.

Python installation provides a program called the **Python Interpreter**, which translates your Python code into instructions the computer can execute.

Without the interpreter, `.py` files cannot run.

---

# 🌐 2. Downloading Python

Always download Python from the **official website**:

👉 https://www.python.org/downloads/

Never download Python from unofficial websites.

The homepage automatically recommends the latest stable version for your operating system.

---

# 🖥️ 3. Installing Python on Windows

### Step 1

Download the installer from python.org.

---

### Step 2

Run the installer.

You will see a setup window.

✅ **IMPORTANT**

Before clicking **Install Now**, check this box:

```
☑ Add Python to PATH
```

This is one of the most important steps.

---

### Step 3

Click:

```
Install Now
```

Wait until the installation finishes.

---

### Step 4

Click:

```
Close
```

Python is now installed.

---

# ⚙️ 4. What Does "Add Python to PATH" Mean?

PATH is an environment variable used by Windows.

It tells Windows where programs are located.

Without adding Python to PATH, commands like:

```bash
python
```

or

```bash
pip
```

may not work from the terminal.

Adding Python to PATH allows you to run Python from **any folder**.

---

# 📦 5. What Gets Installed?

Installing Python includes several tools:

| Tool | Purpose |
|------|----------|
| Python Interpreter | Runs Python code |
| IDLE | Simple code editor |
| pip | Installs Python packages |
| Python Launcher | Helps manage multiple Python versions |
| Standard Library | Built-in modules like `math`, `os`, `random` |

---

# 🧠 6. What is the Python Interpreter?

The interpreter is the software that executes Python code.

Example:

```python
print("Hello")
```

Execution process:

```
Python Code
      ↓
Python Interpreter
      ↓
Machine Instructions
      ↓
Computer Output
```

Output:

```text
Hello
```

---

# 📥 7. What is pip?

`pip` is Python's package manager.

It allows you to install external libraries.

Example:

```bash
pip install numpy
```

```bash
pip install pandas
```

```bash
pip install flask
```

You'll use `pip` throughout your Python journey.

---

# 🚀 8. What is the Python Launcher?

On Windows, Python also installs the **Python Launcher**.

Instead of:

```bash
python
```

you can use:

```bash
py
```

Example:

```bash
py hello.py
```

The launcher automatically chooses the correct installed version of Python.

---

# ✅ 9. Verify the Installation

Open **Command Prompt**, **PowerShell**, or the **VS Code Terminal**.

Check the Python version:

```bash
python --version
```

or

```bash
py --version
```

Example output:

```text
Python 3.12.4
```

---

Check the pip version:

```bash
pip --version
```

Example output:

```text
pip 24.1
```

---

# 📂 10. Where is Python Installed?

A common installation path on Windows is:

```text
C:\Users\<YourUsername>\AppData\Local\Programs\Python\
```

Example:

```text
C:\Users\Saniya\AppData\Local\Programs\Python\Python312\
```

---

# ⚠️ 11. Common Installation Problems

### ❌ Problem 1

```text
python is not recognized...
```

**Cause**

Python is not in PATH.

**Solution**

- Reinstall Python.
- Make sure **Add Python to PATH** is checked.

---

### ❌ Problem 2

```text
pip is not recognized...
```

**Cause**

PATH is incorrect.

**Solution**

Reinstall Python or repair the installation.

---

### ❌ Problem 3

Multiple Python versions installed.

Example:

- Python 3.10
- Python 3.12

Use:

```bash
py
```

or specify the version:

```bash
py -3.12
```

---

# 📌 Summary

Python installation provides:

- Python Interpreter
- pip
- IDLE
- Python Launcher
- Standard Library

Always download Python from the official website and remember to enable **Add Python to PATH**.

---

# 📝 Practice Questions

- [ ] Why do we need to install Python?
- [ ] What is the Python Interpreter?
- [ ] What is PATH?
- [ ] Why is PATH important?
- [ ] What is pip?
- [ ] What is the Python Launcher?
- [ ] Where should Python be downloaded from?
- [ ] How do you check the installed Python version?
- [ ] How do you check the pip version?
- [ ] Name five things installed with Python.

---

# 💼 Assignment

Complete the following tasks:

- [ ] Install Python from the official website (if not already installed).
- [ ] Verify the Python version.
- [ ] Verify the pip version.
- [ ] Find your Python installation folder.
- [ ] Explain what "Add Python to PATH" means in your own words.

---

# 🎯 Topic Completion Checklist

Mark this topic as completed only if:

- [ ] I know why Python must be installed.
- [ ] I understand the role of the Python Interpreter.
- [ ] I know what PATH is.
- [ ] I know what pip is.
- [ ] I know what the Python Launcher is.
- [ ] I can verify my Python installation.
- [ ] I completed the practice questions.
- [ ] I completed the assignment.

---

# 📚 Next Topic

➡️ **Topic 3: Installing VS Code**

---

## ⭐ Keep Learning

> **"Every expert programmer once installed Python for the first time."** 🐍