data = bytearray([65,66,67,68])
print(data)
print(type(data))


text = 'python'
data = bytearray(text,'utf-8')
print(data)

data = bytearray()
print(data)

data = bytearray(5)
print(data)


data = bytearray(b'python')
print(data[0])
print(data[1])


data = bytearray(b'python')
data[0] = 90
print(data)


data = bytearray(b'python')
data[0:1] = b'Jy'
print(data)



alpha = bytearray(b'ABC')
alpha.append(68)
print(alpha)


alpha = bytearray(b'ABCD')
alpha.extend(b'EFGH')
print(alpha)



data = bytearray(b"ABC")
data.insert(1, 90)
print(data)

data = bytearray(b"ABC")
print(data.pop())
print(data)


data = bytearray(b"ABC")
data.reverse()
print(data)


data = bytearray(b"ABC")
for i in data:
    print(i)


data = bytearray(b'python')
data.reverse()
print(data)
