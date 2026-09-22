def greet(name): #---> name is a parameter
    print('good morning',name)
greet('Sana') #---> 'Sana' is an argument
greet('Roy')
greet('Riya')


def student(name,age):
    print('name is ', name)
    print('age is ',age)
student('Sana',21)


def dispaly(name,age,course):
    print(name)
    print(age)
    print(course)
dispaly('Sana','BCA',21)



def student(name,age):
    print('name:',name)
    print('age:',age)
student(name='Sana',age=21)



def details(name,course,age):
    print('name:',name)
    print('age:',age)
    print('course:',course)
details(name='Sana',course='BCA',age=21)



def student(name, age, course):
    print(name, age, course)
student('Sana',age=21,course='BCA')



def greet(name="Guest"):
    print("Hello", name)
greet() #-- when no arguement supplied python uses default arguement
greet('Sana')  # --> overriding default



def display(name,age,salary,active):
    print(name)
    print(age)
    print(salary)
    print(active)
display('Sana',21,21000.50,True)




def display_skill(skills):
    for skill in skills:
        print(skill)
skillas = ['python','java','html']
display_skill(skillas)



def display_numbers(numbers):
    for number in numbers:
        print(number)
values = (10, 20, 30)
display_numbers(values)



def display_student(student):
    for key, value in student.items():
        print(key, ":", value)

student = {
    "name": "Asha",
    "age": 20,
    "course": "BCA"
}
display_student(student)

