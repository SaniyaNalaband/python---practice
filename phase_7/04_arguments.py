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





def calculate_total(prices):
    total = 0 
    for price in prices:
        total += price 
    print('Total : ',total)
prices = [50,50,50,10000]
calculate_total(prices)




def check_result(marks):
    if marks>=45:
        print('Pass')
    else:
        print('Fail')
check_result(99)





def check_result(name,marks):
    if marks>=45:
        print(name , 'has passed')
    else:
        print(name,'has failed')
check_result('Sana',99)




def calculate_total(quantity,price):
    total = quantity*price
    print('Total : ',total)
calculate_total(5,50000)




def display_profile(username,city='Not Provided'):
    print('Username : ',username)
    print('City : ',city)
display_profile('Sana2005')





def add(*numbers):
    print(numbers)
add(10,20,30,40,50)




def add(*numbers):
    total = 0 
    for number in numbers:
        total += number
    print('Total : ',total)
add(10,20,30,40,50)





def display(catogery,*items):
    print('Catogery : ', catogery)

    for item in items : 
        print(item)
display('Skills',  'Python' ,'Html' , 'CSS')


def show(*values):
    print(values)
show('Python',21,'Hello')


def display_details(**details):
    print('Details : ', details)
display_details(name='SANA',age=21,course='BCA')



def display_details(**details):
    for key,value in details.items():
        print(f'{key} : {value}')
display_details(name='SANA',age=21,course='BCA')




def display(*args,**kwargs):
    print('Positional : ',args)
    print('Keyword : ',kwargs)
display(10,20,30,40,50, country='India',proffesion="Student")




def student(name, *, age, course):
    print(name)
    print(age)
    print(course)
student("Asha", age=20, course="BCA")








def student(name,age,/,*, skill,course):
    print('name : ',name)
    print('age :',age)
    print('skill : ',skill)
    print('course : ', course)
student('Sana',21,skill = 'python', course='bca')





def add(a,b,c):
    print(a+b+c)
numbers = [10,20,30]
add(*numbers)



def student(name,age,course):
    print(name)
    print(age)
    print(course)
details = {'name' : 'Sana', 'age':21, 'course' : 'Bca'}
student(**details)




def calcualte_discount(price,discount):
    amount = price*discount/100
    final_price = price - amount 
    return final_price

result = calcualte_discount(10000,10)
print('Final price : ',result)
print('Final price :', calcualte_discount(10000,15))





def display_employee(name,Department = 'general',experience=0):
    print('Name :',name)
    print('department : ', Department)
    print('experience : ',experience)
display_employee('SANA')
display_employee('siya',Department='Developper',experience=2)






def calculate_total(*prices):
    total = 0 
    for price in prices:
        total += price
        return total
total = calculate_total(90,100,120,50,90)
print('total : ',total)



def dispaly_profile(**details):
    for key,value in details.items() :
        print(key,':', value)
dispaly_profile(Username='zee@123', city = 'Bengluru',course='BCA' )





def student_report(name,*marks,**info):
    total_marks = 0
    print('Name : ',name)
    for mark in marks:
        print('Marks : ',mark)
    for mark in marks:
     total_marks += mark 
    print('Total_marks : ',total_marks)
    avg = total_marks/ len(marks)
    print('Additional info : ', info)
    return avg 
student_report('San',99,98,97,city='Bangluru',course='BCA')
                       

result = student_report(
    'San', 99, 98, 97,
    city='Bengaluru', course='BCA'
)

print('Average:', result)




def cart_total(*prices,**cust_info,):
    total_price = 0 
    for price in prices:
     total_price+=price
    print('Total price :', total_price)
    print('CUSTOMER DETAILS')
    for key,value in cust_info.items():
     print(key, ':', value)
    total_amount = total_price
    return total_amount
total = cart_total(10,50,200,35, name='Jhon', place = 'Japan' )
print('total : ', total)



def cart_total(*prices,**cust_info):
    total = sum(prices)
    print('CUSTOMER DETAILS')
    for key,value in cust_info.items():
        print(key,':',value)
    return total
total = cart_total(10,50,200,35, name='Jhony', place = 'california' )
print('total : ', total)



def info(name,age,city):
    print('name :', name)
    print('age : ', age)
    print('city : ',city)
info('Riya',21,'Bengluru')


def add(*numbers):
    total_sum = sum(numbers)
    return total_sum
sum = add(10,20)
print('Sum :',sum)



