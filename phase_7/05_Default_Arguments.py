def greet(name ='Guest'):
    print('hello',name)
greet()


def show_country(Country='India'):
    print('Country : ',Country)
show_country()
show_country('japaan')


def greet(name):
    print('Name : ',name)
greet('Riya')




def welcome(name='Student'):
    print('Welcome!',name)
welcome()
welcome('Noha')



def calculate_sqaure(number = 5):
    print(number*number)
calculate_sqaure()
calculate_sqaure(10)



def calculate_discount(price,discount=10):
    final_price = price-(price*discount/100)
    print('Final price : ', final_price)
calculate_discount(1000)
calculate_discount(1000,5)



def show_country(name,country='India'):
    print(name,'is from ',country)
show_country('Sana')
show_country('Noha','Japan')



def student_name(name='Unknown', course='BCA'):
    print('Name : ',name)
    print('Course : ',course)
student_name()
student_name('Tom')



def employee(name,department,experience=1,status='Active'):
    print(name)
    print(department)
    print(experience)
    print(status)
employee('Tom','Tech',)



def employee(name,department='Development',status='Active'):
    print(name,department,status)
employee('Noha')





def account(username,active=True):
    print('Username : ', username)
    print('Active : ', active)
account('Tom@zee')



def message(text='Welcome to python'):
    print(text)
message('Good morning!!')




def order(product_name,*Price,Quantity=1,discount=0,delivery='Statndard'):
    print('Name : ', product_name)
    print('Quantity : ', Quantity)
    total = sum(Price)
    Final_price = total - (total-discount/100)
    print('Type : ', delivery)

order('keyboard')
order('Mouse',Quantity=5)
order('Mouse',discount=10)
order('mouse',delivery='express')




def student_registration(name,course='BCA',semister='5th',city='Bengluru',status='present'):
    print('Name : ',name)
    print('Course : ', course)
    print('Semister : ', semister)
    print('City : ', city)
    print('Status : ', status)
student_registration('Sania')
student_registration('Sania',course='Tech',semister='6th')
student_registration('sania',city='California')
student_registration('Sana')





def add_skilll(skill,skills=None):
    if  skills is  None:
        skills = []

    skills.append(skill)
    print(skills)

add_skilll('pythhon')
add_skilll('Sql')




def calculate_power(number,power=2):
    return number ** power
print(calculate_power(6))



def calculate_interest(principal,rate=7):
    intrest = principal*rate/100
    print(intrest)
calculate_interest(10000)




def send_notification(message,priority='Normal'):
    print('Message : ',message)
    print('Priority : ', priority)
send_notification('Your order has been shipped!!')




