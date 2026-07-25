data =  bytes([65,66,67])
view = memoryview(data)
print(view)
print(data)
print(type(view))


data = bytes([65, 66, 67])
view = memoryview(data)
print(view[0])
print(view[1])
print(view[2])



data = bytes([65, 66, 67, 68])
view = memoryview(data)
print(view[1:3].tolist())

data = b"ABC"
view = memoryview(data)
print(view.tolist())


data = bytearray(b'ABC')
view = memoryview(data)
view[0] = 90
print(data)


data = bytearray(b"Python")
view = memoryview(data)
print(view.tobytes())



data = b"ABC"
view = memoryview(data)
print(bytearray(view))


data = b"Programming"
view = memoryview(data)
print(view[3:8].tobytes())


data = b"ABC"
view = memoryview(data)
for i in view:
    print(i)


data = b"Machine Learning"
view = memoryview(data)
print(len(view))


data = b"Python"
view = memoryview(data)
print(view.itemsize)


