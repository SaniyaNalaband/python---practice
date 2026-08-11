student = "Saniya", 21, 90
print(student)
print(type(student))


numbers = (10, 20, 30)
print(numbers)



numbers = 10, 20, 30, 40, 50
print(numbers)
print(type(numbers))



languages = "Python", "Java", "C", "JavaScript"
print(languages)


data = "Python", 10, 3.14, True, None
print(data)

name = 'Saniya'
age = 21
marks = 99
student = name,age,marks
print(student)



a = 10
b = 20
result = a,b,a+b
print(result)


student = (True,False,True)
print(student)



data = [1,2],[3,4]
print(data)


data = (1,2),(3,4),(5,6)
print(data)

data = {1,2},{'hello','hi'},{True,False}
print(data)


employee = 101,'Aisha','developer','45000'
print(employee)


# name = input('Enter the name : ')
# age = int(input('Enter the age : '))
# city = input('Enter the city : ')
# data = name,age,city
# print(data)



length = 20
width = 10 
area = length*width
perimeter = 2*(length+width)
result = area,perimeter
print(result)


def calculate(a,b):
    total =a+b
    difference = a-b
    return total,difference
result = calculate(10,20)
print(result)




def student_details():
    name = 'Sana'
    age = 21
    city = 'hubli'
    return name,age,city
student = student_details()
print(student)



data = ([1, 2, 3],{"name": "Aisha"},{10, 20},"Python")
print(data)



product_id = 101
product_name = "Laptop"
price = 55000
category = "Electronics"
product = product_id, product_name, price, category
print(product)



x = 10 
y = 20 
point = x,y
print(point)



employee_id = 1001
name = "Riya"
department = "IT"
salary = 45000
employee = employee_id, name, department, salary
print(employee) 



names = ["Aisha", "Saniya", "Rohan"]
for item in enumerate(names):
    print(item)

data = ['string',True,99.9,45]
for item in enumerate(data):
    print(item)



names = ["Aisha", "Saniya", "Rohan"]
marks = [85, 92, 78]
students = list(zip(names,marks))
print(students)



products = ['laptop','keyboard','mouse','cpu']
prices = [50000,20000,25000,50000]
product_price = list(zip(products,prices))
print(product_price)




a = 10
b = 20
result = a+b,a-b,a*b
print(result)




def calculate(a,b):
    return a+b,a-b
result =calculate(10,20)
print(result)





employee_id = 1001
name = "Aisha"
department = "IT"
salary = 45000
experience = 2
employee = employee_id, name, department, salary, experience
print(employee)




a = 15
b = 25 
result = a+b,a-b,a*b,a/b,a%b
print(result)



def calculate_marks(marks):
    total = sum(marks)
    average = sum(marks)/len(marks)
    highest = max(marks)
    lowest = min(marks)
    return total,average,highest,lowest
result = calculate_marks([88,95,98,68,95])
print(result)


