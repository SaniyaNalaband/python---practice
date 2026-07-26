''' 1️⃣ Assignment (`=`)
Assigns a value to a variable.'''

x = 10 
print(x)

age = 21 
print(age)


a = 5
a = a+5
print(a)


name, age, city = "Saniya", 20, "Mysuru"
print(name)
print(age)
print(city)


subject = 'Python'
print(subject)


''' 2️⃣ Add and Assign (`+=`)
Adds a value and stores the result.
'''

x = 10
x += 5
print(x)


wallet = 150
wallet +=50
print('wallet')


a = 20 
b = 30 
a += b
print(a)

price = 98.5
price2 = 56.6
price +=price2
print(price)

word = 'hello'
word1 = ' hi '
word+=word1
print(word)

name = "Python"
name += " Programming"
print(name)

numbers = [10, 20]
numbers += [30, 40]
print(numbers)


colors = ("Red", "Blue")
colors += ("Green",)
print(colors)

a = True
a += 5
print(a)


total = 0 
total += 10 
total += 20 
total += 30 
total += 40 
print(total)


''' 3️⃣ Subtract and Assign (`-=`)
Subtracts a value and stores the result.'''

marks = 95
marks -= 10
print(marks)

a = 20
a -= 5
print(a)


a = 50
b = 18
a -= b
print(a)

price = 25.5
price -= 5.5
print(price)


a = True
a -= 1
print(a)

z = 5 + 8j
z -= 2 + 3j
print(z)


balance = 100
balance -= 20
balance -= 15
balance -= 5
print(balance)


count = 10 
for i in range(count):
    count-=i
print(i)

number = 5
number -= 1
print(number)
number -= 1
print(number)
number -= 1
print(number)



''' 4️⃣ Multiply and Assign (`*=`)
Multiplies the variable by another value.'''


salary = 5000
salary *= 2
print(salary)

a = 10
a *= 5
print(a)


price = 20
price *= 1.5
print(price)


a = 12
a *= -3
print(a)

text = 'python '
text *= 3
print(text)


numbers = [1, 2]
numbers *= 3
print(numbers)


flag = True
flag *= 8
print(flag)


''' 5️⃣ Divide and Assign (`/=`)
Divides the variable and stores the result.'''

total = 100
total /= 4
print(total)





a = 20
a /= 5
print(a)


x = 36 
y = 6 
x /= y 
print(x)



flag = True
flag /= True
print(flag)


z = 8 + 4j
z /= 2
print(z)


num = 200
num /= 2
num /= 5
num /= 4
print(num)


total = 450
subjects = 5
total /= subjects
print("Average =", total)



''' 6️⃣ Floor Divide and Assign (`//=`)'''


a = 20
a //= 3
print(a)

x = 45
y = 6
x //= y
print(x)


price = 25
price //= 4.0
print(price)

''' 7️⃣ Modulus and Assign (`%=`)'''

x = 25
x %= 4
print(x)


a = 17
a %= 5
print(a)

x = 45
y = 8
x %= y
print(x)


x = 45
y = 8
x %= y
print(x)


num = 18.5
num %= 2.5
print(num)

number = 100
number %= 30
number %= 7
print(number)


''' 8️⃣ Exponent and Assign (`**=`)'''


x = 2
x **= 5
print(x)


num = 3
num **= 3
print(num)

x = 2
x **= 4
print(x)


price = 2.5
price **= 2
print(price)


a = 15
a **= 0
print(a)


num = 2
num **= -3
print(num)