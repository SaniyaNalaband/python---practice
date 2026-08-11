student = ('Aisha',21,90)
name,age,marks = student
print(name)
print(age)
print(marks)




number = 1,2,3
a,b,c = number
print(a)
print(b)
print(c)



languages = ('python','java','css','html')
first,second,third,fourth = languages
print(first)
print(second)
print(third)
print(fourth)



student = ("Aisha", 21, 89.5, True)
name, age, marks, status = student
print(name)
print(age)
print(marks)
print(status)



student = "Aisha", 21, 90
name, age, marks = student
print(name)
print(age)
print(marks)




student = (
    "Aisha",
    21,
    "BCA",
    92
)

name, age, course, marks = student
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)



point = (10, 20)
x, y = point
print("X:", x)
print("Y:", y)



a = 10
b = 20
b, a
print(b,a)


numbers = (10, 20, 30, 40, 50)
a,*b = numbers
print(a)
print(b)




numbers = (10, 20, 30, 40, 50)
*remaining, last = numbers
print(remaining)
print(last)





numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)
print(middle)
print(last)




student =  (("Aisha", 85), ("Saniya", 92))
(first_name, first_marks), (second_name, second_marks) = student
print(first_name)
print(first_marks)
print(second_name)
print(second_marks)




data = ((10, 20), (30, 40))
(a, b), (c, d) = data
print(a)
print(b)
print(c)
print(d)



def calculate(a, b):
    return a + b, a - b
addition, subtraction = calculate(20, 10)
print(addition)
print(subtraction)




def student_details():
    return "Aisha", 21, 90
name, age, marks = student_details()
print(name)
print(age)
print(marks)



students = [ ("Aisha", 85),("Saniya", 92), ("Rohan", 78)]
for name, marks in students:
    print(name, marks)



names = ["Aisha", "Saniya", "Rohan"]
for index, name in enumerate(names):
    print(index, name)





names = ["Aisha", "Saniya", "Rohan"]
marks = [85, 92, 78]
for name, mark in zip(names, marks):
    print(name, mark)



students = [ ("Aisha", 85),("Saniya", 92), ("Rohan", 78)]
for name, marks in students:
    print(f"{name} scored {marks}")




products = [("Laptop", 55000),("Keyboard", 1200),("Mouse", 800)]
for product, price in products:
    print(f"{product}: ₹{price}")




points = [(10, 20),(30, 40), (50, 60)]
for x, y in points:
    print("X =", x, "Y =", y)




student = ("Aisha", 21, "BCA", 90)
name, _, course, _ = student
print(name)
print(course)