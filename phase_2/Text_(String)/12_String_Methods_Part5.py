'''1. `isalpha()`
Returns `True` if **all characters are alphabetic letters** and the string is not empty.'''

print("Python".isalpha())
print("Python123".isalpha())

'''2. `isdigit()`
Returns `True` if **all characters are digits (0–9)**.'''

print("12345".isdigit())
print("12.5".isdigit())

'''3. `isalnum()`
Returns `True` if the string contains **only letters and digits**.'''

print("Python123".isalnum())
print("Python 123".isalnum())

'''4. `islower()`
Returns `True` if **all alphabetic characters are lowercase**.'''

print("python".islower())
print("Python".islower())

'''5. `isupper()`
 `True` if **all alphabetic characters are uppercase**.'''

print("PYTHON".isupper())
print("Python".isupper())

'''6. `istitle()`
Returns `True` if **every word starts with a capital letter**.
'''

print("Python Programming".istitle())
print("python Programming".istitle())

'''7. `isspace()`
Returns `True` if the string contains **only whitespace characters**.
'''

print("   ".isspace())
print(" Python ".isspace())

'''
# 📖 8. `isdecimal()`
eturns `True` if the string contains **decimal digits only**.'''

print("123".isdecimal())
print("12.3".isdecimal())

'''9. `isnumeric()`
Returns `True` for **numeric characters**, including some Unicode numerals.'''

print("123".isnumeric())
print("Ⅳ".isnumeric())

'''10. `isidentifier()`

Checks whether the string is a **valid Python identifier**.'''

print("student_name".isidentifier())
print("123name".isidentifier())

'''11. `isascii()`
Returns `True` if **all characters are ASCII**.'''

print("Python".isascii())
print("Pythön".isascii())

'''12. `isprintable()`
Returns `True` if **all characters are printable**.
'''

print("Hello".isprintable())
print("Hello\nWorld".isprintable()) 