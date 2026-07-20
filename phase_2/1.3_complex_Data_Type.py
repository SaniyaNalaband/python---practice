z = 2 + 3j
print(z)
print(type(z))

z = 4 + 2j
print(z)

z = 7 -5j
print(z)

z = -3+9j
print(z)


x = 5j
print(type(x))

# creat complex number using 'complex()' function

a = complex(3,5)
print(a)


# print real and imaginary number seperately

z =  10 + 5j
print('the real number is : ', z.real)
print('the imaginary number is : ',z.imag)

# arithmatic operations


a = 5+2j
b = 6+4j
print(a+b)
print(a-b)
print(a*b)
print(a/b)


print((2+3j)+(4+5j))


# mixing data types

print((3+5j)+10)

print((3+5j)+2.5)

print((5+3j)*2)


# a = int(input('enter the number : '))
# b = int(input('enter the number : '))
# print(complex(a,b))
# print(f'the real number is {a} \n and the imaginary number is {b}')

# a = complex(input('enter first number : '))
# b = complex(input('enter second number : '))
# print(a+b)


# a = int(input('enter a number : '))
# print(complex(a))


print(4j)

print(complex(5,6))

print(complex())

print(abs(3+4j))

print((2+3j)==(2+3j))

print((2+3j)!=(3+2j))


# print(int(3+4j))  ---> throws an error

# print(float(3+4j)) ---> throws error

print(complex("5+3j"))

print(complex(5.5,6.8))

print(complex(True,False))

# finding the magnitude

z = 6+8j
print(abs(z))


# conugate method

z = 3 + 4j
print(z.conjugate())


print((5-7j).conjugate())

z = 4 + 3j
print(z * z.conjugate())

z = 6 - 8j
print(z * z.conjugate())