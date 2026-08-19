def welcome():
    print('Welcome!!')
print('start')
welcome()
print('end')



def greet(name):
    print('hello!!', name)
greet('saniya')



def square(number):
    print(number*number)
square(5)



def add (a,b):
    print('total :',a+b)
add(5,10)


def student_info(name,age):
    print(f'name is : {name}\nage is : {age}')
student_info('asha', 20)




def student_info(name,age):
    print(f'name is : {name}\nage is : {age}')

student_info(name='ayera', age=20)



def greet(name):
    print('name :', name)
student_name = 'Riya'
greet(student_name)



def calculate_total(price, quantity):
    print(price * quantity)
price = 500
quantity = 3
calculate_total(price, quantity)



def display_number(number):
    print(number)
display_number(5+10)




def get_number():
    return 5
number = get_number()+5
print(number)



def get_name():
    return 'Asha'
print(get_name())



def get_age():
    return 20
if get_age()>=18:
    print('elligible')



def greet():
    print('hello')
for i in range(1,5):
    greet()




def message():
    print('welcome')

def start():
    message()
start()



def first():
    print('first')
def second():
    print('second')
def third():
    first()
    second()
third()



def square(number):
    return number*number
def dispaly(value):
    print(value)

dispaly(square(5))


def disaplay(value):
    print(value)
dispaly(21)
dispaly('python')
dispaly(99.9)



# def greet(name):
#     print('hello', name)
# name = input('enter your name : ')
# greet(name)



# def square(number):
#     print(number*number)
# number = int(input('enter the number : '))
# square(number)



def check_login(username,password):
    if username == 'admin' and password == '1234':
        return True
    return False
result = check_login('admin','1234')
if result:
    print('Login successfull')
else:
    print('Invalid login')



def display_subjects(subjects):
    for subject in subjects:
        print(subject)
subjects = ['java','python','html']
display_subjects(subjects)




# def even_number(number):
#     if number %2 == 0 :
#         return True
#     return False
# number = int(input('enter the number : '))
# result = even_number(number)
# if result:
#     print('even')
# else:
#     print('odd')




def total_price():
    price = 5000
    quantity = 5
    total_price = price*quantity
    print('total price is : ',total_price)
total_price()



def check_result(number):
    return 'pass' if number>=40 else 'fail'
result =   check_result(40)
print(result)


def list_number(number):
    for num in number:
        print(num)
number = [1,2,3,4,5]
list_number(number)