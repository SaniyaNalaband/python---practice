fruits = ["Apple", "Banana"]
fruits.append('Orange')
print(fruits)


numbers = [10, 20, 30]
numbers.append(40)
print(numbers)



prices = [99.99, 149.50]
prices.append(199.99)
print(prices)


status = [True, False]
status.append(True)
print(status)


numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)



students = []
students.append({"name": "Saniya", "marks": 95})
print(students)



square = []
for i in range(1,10):
    square.append(2**i)
print(square)


even_numbers = []
for i in range(1,10):
    if i%2==0:
     even_numbers.append(i)
print(even_numbers)



primes = []
for num in [2, 3, 5, 7, 11]:
    primes.append(num)
print(primes)


numbers = [1, 2, 3]
numbers.extend([4,5])
print(numbers)


fruits = ["Apple", "Banana"]
fruits.extend(["Mango", "Orange"])
print(fruits)




letters = ["A", "B"]
letters.extend("CD")
print(letters)




fruits = []
fruits.extend(["Apple", "Banana", "Mango"])
print(fruits)


numbers = [1, 2, 3]
numbers.extend((4, 5, 6))
print(numbers)



letters = ["A", "B"]
letters.extend({"C", "D"})
print(letters)



class_a = ["Riya", "Priya"]
class_b = ["Saniya", "Aman"]
class_a.extend(class_b)
print(class_a)




students1 = [
    {"name": "Rahul"}
]
students2 = [
    {"name": "Saniya"},
    {"name": "Priya"}
]
students1.extend(students2)
print(students1)




fruits = ["Apple", "Banana", "Orange"]
fruits.insert(1, "Mango")
print(fruits)



numbers = [10, 20, 40]
numbers.insert(2, 30)
print(numbers)


numbers = [20, 30]
numbers.insert(0, 10)
print(numbers)



numbers = [10, 20]
numbers.append(30)
numbers.insert(1, 15)
print(numbers)



