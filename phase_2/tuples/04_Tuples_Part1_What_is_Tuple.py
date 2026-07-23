student = ("Saniya", 20, "AI ML", 8.9)
print(student)

empty = ()
print(empty)


# single element tuple (wrong way of writing a tuple)
num = (10)
print(type(num))


# correct way of writing a tuple 

num = (10,)
print(type(num))


data = ( "Python", 100, True, 95.5)
print(data)

# allows duplicates

numbers = (10, 20, 20, 30)
print(numbers)


fruits = ("Apple", "Banana", "Mango")
print(fruits)


data = ('Saniya',20,98.9,True)
print(data)

colorss =('red','green','yellow','blue')
print(colorss[1])
print(colorss[0])


numbers = (10,20,30,40,50)
print(numbers[-1])

alpha = ('a','b','c','d','e')
print(alpha[0:4])

animals = ('cat','dog','elephan','cow')
print('cat' in animals)
print('tiger' in animals)

marks = (80, 90, 80, 70, 80)
print(marks.count(80))
print(marks.count(100))


cities = ("Delhi", "Mumbai", "Bengaluru", "Goa")
print(cities.index("Bengaluru"))


student = ("Saniya", 95, "A")
name, marks, grade = student
print(name)
print(marks)
print(grade)

students = ( ("Rahul", 85),("Saniya", 95), ("Aisha", 90))
print(students[0])
print(students[1][0])
print(students[2][1])


data = (10, 20, 30, 20, 40)
print(data.count(20))
print(data.index(30))
print(data[-2])
print(data[1:4])

