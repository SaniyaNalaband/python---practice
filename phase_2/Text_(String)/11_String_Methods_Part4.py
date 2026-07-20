# LSTRIP()

text = "   Python"
print(text.lstrip())

text = "     Hello World"
print(text.lstrip())

text = 'html'
print(text.lstrip())

text = "*****Python"
print(text.lstrip('*'))

text = "00012345"
print(text.lstrip('0'))

text = "___Welcome"
print(text.lstrip('_'))

print("   AI".lstrip())

print("000789".lstrip("0"))

print("***Hello***".lstrip("*").rstrip('*'))

# RSTRIP()

text = "Python   "
print(text.rstrip())

text = "Hello World     "
print(text.rstrip())

text = "Python*****"
print(text.rstrip('*'))

print("123000".rstrip("0"))

print("***Hello***".rstrip("*").lstrip('*'))

# CENTER()


print("Hi".center(10))
print('python'.center(20))
print('Ai'.center(10))
print('Welcome'.center(30))


# lJUST

print('python'.ljust(20))
print('apple'.ljust(10,'*'))
print("Hi".ljust(10))
print("AI".ljust(8, "."))

# rJUST

print('python'.rjust(20))
print('hello'.rjust(20,'.'))


# zFILL()

text = "123"
print(text.zfill(10))

text = "45"
print(text.zfill(10))

text = "9876"
print(text.zfill(8))

text = "1"
print(text.zfill(4))

roll = "25"
print(text.zfill(2))


# mixed challenges 

print("   Python".lstrip())
print("Python   ".rstrip())
print("Python".ljust(12, "*"))
print("Python".rjust(12, "*"))