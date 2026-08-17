def greet():
    return 'hello'



def welcome():
    return ("Welcome to the course")



def calculate_total():
    pass


def display_student():
    pass 



def check_password():
    pass 


def task1():
    pass 




def show_function():
    print('Learning python')
show_function()


def greet():
    print('hi')
greet()
greet()
greet()



def student_details():
    name = 'sana'
    age = 20
    course = 'bca'

    print(name)
    print(age)
    print(course)

student_details()



def calculate_squares():
    number = 8 
    print(number ** 2)
calculate_squares()



def greet():
    'this message prints welcome message'
    print('welcome')
print(greet.__doc__)




def student():
    name = 'saniya'
    print(name)
student()



name = 'asha'
def students():
    print(name)
students()
print(name)


def numbers():
    for number in range(1,10):
        print(number)
numbers()



def check_age():
    age = 20 
    if age>19:
        print('adult')
    else:
        print('minor')
check_age()



def calculate_total():
    price = 500
    quantity = 10 
    total = price*quantity
    print('totalt :' , total)
calculate_total()




def greeting():
    print('hello!  welcome to python')
greeting()


def show_message():
    '''displays message'''
    print('Hi!! im learning python')

print(show_message.__doc__)
show_message()  


def course_info():
    course = 'BCA'
    subject = 'python'
    print(course)
    print(subject)
course_info()


def dispaly_number():
    for number in range(1,6):
        print(number)
dispaly_number()




def student_details():
    name = 'Riya'
    age = 21
    course = 'BCA'
    college =  'ABC colllege'
    print(name ,age,course,college )
student_details()




def student_result():
    total_marks = 400
    average_marks = 80
    result = 'pass' if average_marks>=70 and total_marks>=400 else 'fail'
    print(result)

student_result()




def calculate_cart_total():
    prices = [250, 120, 500, 80, 300]
    total = 0 
    for price in prices:
     total = total =+  price
    print('total', total)
calculate_total()




def stock_check():
    stock = {'laptop' : 12, 'keyboard' : 0, 'mouse':10}
    for product,quantity in stock.items():
     availability =  'available' if quantity>0 else 'not available'
     print(product,quantity,availability)

stock_check()






def student_information():
    name = 'Riya'
    age = 21
    course = 'BCA'
    marks = [90,89,85,98,98]
    total = sum(marks)
    average_marks = sum(marks)/len(marks)
    result = 'passed' if average_marks>=50 else 'failed'

    print('name : ', name,'\n','age : ',   age,'\n','course :', course,'\n','marks : ', marks,'\n', 'total : ',total, '\n', 'average :',average_marks,result)
student_information()




def display_employee():
    pass