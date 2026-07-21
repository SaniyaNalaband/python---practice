'''1. `append()`
Adds **one element** to the **end** of the list.
'''

fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)


numbers = [10, 20]
numbers.append(30)
print(numbers)

data = [1, 2]
data.append(True)
print(data)

A = [1,2]
B = [3,4]
A.append(B)
print(A)

NUMBERS = [10,20,30]
NUMBERS.append(50)
print(NUMBERS)

FLOAT = [23.4,45.5,67.6]
FLOAT.append(65.4)
print(FLOAT)

status = [True,False]
status.append(True)
print(status)

complex_number = [20,40]
complex_number.append(2+4j)
print(complex_number)

matrix = [1,2,3]
matrix.append([2,3])
print(matrix)


# names = []
# name = input('enter the names : ')
# names.append(name)
# print(names)



colors = []
colors.append("Red")
colors.append("Blue")
colors.append("Green")
print(colors)


numbers=[]
for i in range(1,6):
    numbers.append(i)
print(numbers)


'''
2. `extend()`
Adds **all elements** from another iterable.
'''

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)


numbers = [1, 2]
numbers.extend((3, 4))
print(numbers)



letters = ['A']
letters.extend('BC')
print(letters)

numbers = [2,4,5,6]
numbers.extend([3,8,7,6])
print(numbers)

fruits = []
fruits.extend(['apple','banana','mango'])
print(fruits)


numbers =[1,2,3]
numbers.extend({2,3,4})
print(numbers)


numbers = [2,3,4]
numbers.extend((2,5,6))
print(numbers)


number = [1,2]
number.extend(range(3,6))
print(number)



list1 = [2,3,4]
list2 = [5,6,7]
list1.extend(list2)
print(list1)



# names = ["Saniya"]
# new_names = input("Enter names separated by spaces: ").split()
# names.extend(new_names)
# print(names)


numbers = []
for i in range(1, 4):
    numbers.extend([i, i * 10])
print(numbers)

''' 3. `insert()`
Inserts an element at a specific index.'''

fruits = ["Apple", "Mango"]
fruits.insert(1, "Banana")
print(fruits)

numbers = [20, 30]
numbers.insert(0, 10)
print(numbers)

numbers = [1, 2]
numbers.insert(100, 3)
print(numbers)

numbers = [10, 20, 40]
numbers.insert(-1, 30) # ---> python reads it as insert befor -1 i.e [10,20,30,40]
print(numbers)

numbers = [20, 30, 40]
numbers.insert(0, 10)
print(numbers)

colors = ["Red", "Blue"]
colors.insert(len(colors), "Green")
print(colors)

prices = [100, 300]
prices.insert(1, 200.5)
print(prices)

status = [True, True]
status.insert(1, False)
print(status)


numbers = [10, 20]
numbers.insert(1, 2 + 3j)
print(numbers)

numbers = [1, 2, 5]
numbers.insert(2, [3, 4])
print(numbers)

letters = ["A", "B", "D"]
letters.insert(-1, "C")
print(letters)