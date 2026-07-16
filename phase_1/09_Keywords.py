# python provides keyword module

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# wrong keyword

# if = 10 ----> shows syntax error

# represents the boolean value

print(True)

if True:
    print('hello')


# reeeeeepresents the boolean value 

print(False)

if False:
    print('hi')

print('good')


# represents nothing no value

x = None
print(x)


# decision making key words

age = 20
if age>=20:
    print('you are adult')

age = 16
if age>16:
    print('adult')
else:
    print('minor')


# if else decison keyword

marks = 90
if marks>=90:
    print("A grade")
elif marks>=75:
    print('B grade')
else:
    print('C grade')
     


# loop keywords

for i in range(5):
    print(i)

i = 1
while i<=11:
    print('hello')
    i+=1


# breaks the loop (stops the loop)

for i in range(10):
    if i ==5 :
        
        break
    print(i)

# continue skip the itration in a loop

for i in range(10):
    if i == 5:
        continue
    print(i)


# pass does nothing its a placeholder

for i in range(10):
    pass
print('done')


# function keyword use to creat fucntion

def greet():
    print('hello')


# return returns a value 

def add(a,b):
    return a+b
print(add(4,5))



# lambda  creats small anonymous function
square = lambda x:x*x
print(square(5))


# class creates a class
class Animal:
    pass


# import imports a built in module

import math
print(math.sqrt(25))


# from

from math import sqrt 
print(sqrt(25))


# as 
import math as m
print(m.pi)
    

# try and exception
 
try:
    x=5/0
except:
    print('cannot be devided')


# finally runs no matter what happens

try:
    print('hello')
finally:
    print('finished')


# raise --> raises and exception 

raise ValueError('wrong value')

