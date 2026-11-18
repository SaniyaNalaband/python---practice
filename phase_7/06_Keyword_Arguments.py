def student_info(name,age):
    print('Name : ',name)
    print('Age : ',age)
student_info(name='Sana',age=21)



def student_info(name,age,course):
    print(f'Name {name}\nAge{age}\nCourse {course} ')
student_info(name='Riya',age=21,course='BCA')





def employee(name,department,salary):
    print(name)
    print(department)
    print(salary)
employee(salary=50000,department='IT',name='Saniya')



def product(name,price,quantity):
    total = price*quantity
    print('Product_name : ',name)
    print('price_of_the_product:',price)
    print('quantity_of_the_product :',quantity)
    print('Total : ',total)
product(quantity=10,name='Keyboard',price=5000)


def greet(name,message='Welcome'):
    print(message,name)
greet(name='Riya',message='Good Morning')




def calculate_bill(price,quantity,discount):
    total = price*quantity
    total -= discount
    print('Price : ', price)
    print('Quantity :',quantity)
    print('Discount : ', discount)
    print('Total : ', total)
calculate_bill(price=1000,quantity=5,discount=150)



def check_result(name,marks,passing_marks=40):
    if marks>= passing_marks:
        print(name , 'Passed')
    else:
        print(name, 'Better luck next time!')
check_result(name='Tom',marks=89)
check_result('Tim', marks=25)




name = 'Ani'
age = 21
def displayl(name,age):
    print(name)
    print(age)
displayl(name=name,age=age)





student_name = 'Jerry'
student_age = 21
def student(name,age):
    print(name)
    print(age)
student(name=student_name,age=student_age)





def students(**kwargs):
    print(kwargs)
students(name='San',age=21,course='BCA')




def display(*args,**kwargs):
    print('Positional : ',args)
    print('Keyword : ',kwargs)
display('SQL','Python',age=21,city='Pune')




student={'name' : 'Tina','age':21,'city' : 'Bengluru'}
def Display(name,age,city):
    print(name)
    print(age)
    print(city)
Display(**student)






student={'name':'Sana','age':21,'course':'BCA','collage':'XYZ Clg','city':'Bengluru'}
def student_registration_system(name,age,course,collage,city='Pune'):
    print('Nmae: ',name)
    print('Age :',age)
    print('Course : ',course)
    print('Colaage :',collage)
    print('City :',city)
student_registration_system(course='MCA',name='Zhen',city='Bengluru',age=21,collage='XYZ Collage')
student_registration_system('Zhen',course='MCA',city='Bengluru',age=21,collage='XYZ Collage')
student_registration_system(**student)







employe={'employee_id' : 'Z101','name':'Anie','dept':'IT','salary':55000,'experience':5,'location':'Mumbai'}
def employee_manegment_system(employee_id,name,dept,salary,experience,location='Chennai'):
    print(employee_id)
    print(name)
    print(dept)
    print(experience)
    print(salary)
    print(location)
employee_manegment_system(employee_id='E101',name='Jhon',dept='IT',salary=60000,experience=5,location='Bengluru')
employee_manegment_system(**employe)



