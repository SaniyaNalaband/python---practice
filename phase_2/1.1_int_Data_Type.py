x = 10 
print(x)
print(type(x))


x = -15 
print(x)
print(type(x))

x = 15 
y = 5
print(x+y)
print(type(x+y))


a = 10
b = 5
print(10-5)
print(type(10-5))

a = 12
b = 5
print(12*5)
print(type(12*5))

a = 25
b = 5
print(12/5) # devider always returns float value
print(type(12/5))

a = 25 
b = 5 
print(a//b)
print(type(a//b))

x = 26 
y = 5
print(x%y)
print(type(x%y))

x = 5
y = 3
print(5**3)
print(type(x**y))


x ='100'
x = (int('100'))
print(x)
print(type(x))


x = 9.99
x = int(x)
print(x)
print(type(x))


print(int(True))

print(int(False))

print(type(int('54')))


# operations on integer 

print(type(5+3*2))
print((5+3*2))

print((5+3)*2)


print(50//6)

print(50%6)

print(2**8)

x = 50
x -= 20
print(x)

x = 10
x  *= 8 
print(x)


x = 100
x //= 6
print(x)

x = 100
x *= 7
print(x)


print(abs(-200))

print(pow(2,10))

print(max(5,10))

print(min(100,200))

print(round(9.9))

print(int(100.99))

a = 50
b = 20
a,b = b,a
print(a)
print(b)

x = 10 
y = 20 
temp = x 
x = y
y = temp 
print(x)
print(y)


a,b,c,d,e = 10,20,30,40,50
print(a+b+c+d+e)

a,b,c = 10,10,10
print((a+b+c)/3)


total_days = int(input('enter the total days : '))
weeks = total_days//7
remaining_days = total_days % 7
print(f'total week is {weeks}')
print(f'the remaining days are {remaining_days}')


a,b,c = 12,13,14
a,b,c = c,b,a
print(a,b,c)