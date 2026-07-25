numbers = bytes([65,66,67,68])
print(numbers)

text = 'Python'
data = text.encode()
print(data)

data = b'hello'
print(data)
print(type(data))



data = b'ABCD'
print(data[0])
print(data[1])
print(data[2])
print(data[3])



print(chr(65))
print(chr(66))
print(chr(67))

data = 'Python'
print(data[3])
print(data[-1])
print(data[4])



text = 'hello'
binary = text.encode('utf-8')
print(binary)

binary = b'hello'
text = binary.decode('utf-8')
print(text)

# with open('photo.jpg','rb') as file:
#     data=file.read()
# print(type(data))



text = bytes("Python", "utf-8")
print(text)


data = b'ABC'
for i in data:
    print(i)


a = b"Hello "
b = b"World"
print(a + b)


data = b"Python"
print(80 in data)
print(100 in data)

numbers = [72, 101, 108, 108, 111]
result = bytes(numbers)
print(result)


text = b'hello'
binary = text.decode('utf-8')
print(binary)
print(bytes(text))



