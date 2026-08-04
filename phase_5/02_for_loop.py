for letter in 'python':
    print(letter)



for fruits in ['apple','banana','mango']:
    print(fruits)



numbers = (10,11,12,13,14)
for number in numbers:
    print(number)




colors = {'red','green','yellow','black'}
for color in colors:
    print(color)



student = {
    "name": "Saniya",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key)

for value in student.values():
    print(value)

for key in student.keys():
    print(key)



for i in range(5):
    print(i)



for _ in range(3):
    print("Hello")



for number in [1, 2, 3, 4, 5]:
    print(number ** 2)



employees = {
    101: "Rahul",
    102: "Aisha",
    103: "Saniya"
}
for emp_id, name in employees.items():
    print(emp_id, "->", name)



numbers = [5, 10, 15, 20]
for number in numbers:
    if number % 10 == 0:
        print(number, "is divisible by 10")




name = 'saniya'
for word in name:
    print(word)

list = [1,'hello',99.9,True]
for element in list:
    print(element)

Tuple = ('hi',1,True,99,0)
for element in Tuple:
    print(element)


Set = {2,'hie',99.3}
for element in Set:
    print(element)


dict = {'number' : 8 , 'string' : 'hello' , 'float':99.9, 'boolean':True}
for element in dict.values():
    print(element)



dict = {'number' : 8 , 'string' : 'hello' , 'float':99.9, 'boolean':True}
for element in dict.keys():
    print(element)



dict = {'number' : 8 , 'string' : 'hello' , 'float':99.9, 'boolean':True}
for element,value in dict.items():
    print(element ,'-', value)



for number in range(1,21):
    print(number)




for i in range (5,0,-1):
    print(i)



for i in range(1,20,2):
    print(i)



total = 0
for i in range(1,10):
    total+=i
print(total)



number = 5
fact = 1
for i in range(1,number+1):
    fact *= i
print(fact)



text = "Programming"
count = 0
for letter in text:
    if letter.lower() in "aeiou":
        count += 1
print(count)



word = 'Education'
for ch in word:
    if ch.lower() in  'aeiou':
        print(ch)



word = 'python'
for ch in word:
    print(ch.upper())


number = [2,4,6,8]
for num in number:
    print(num,'-',num**2)




numbers = [10, 55, 32, 89, 12]
largest = number[0]
for num in numbers:
    if num>largest:
        largest = num 
print(largest)



numbers = [5, -2, 8, -1, 3]
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(count)



number = 17
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not Prime")




text = "Python12345"
count = 0
for ch in text:
    if ch.isdigit():
        count += 1
print(count)



text = "PyTHon"
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print(count)




numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)


