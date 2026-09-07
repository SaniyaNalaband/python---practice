def greet(name):  # ---> name is the parameter 
    print("Hello", name)

greet("Asha")  # --- > asha is an arguments
greet("Neha")
greet("Priya")




def add(a,b):  # ---> a,b are parameters 
    print(a+b)
add(5,10)



def student_info(name,age,course):
    print(f"name : {name} \nage : {age}\ncourse : {course}")
student_info('asha',21,'bca') 
student_info(name='riya',age=21,course='bca')



def greet(name="Guest"):
    print("Hello", name)
greet()



def greet(name="Guest"):
    print("Hello", name)
greet("Asha")
greet()




def calculate_bill(price, quantity, discount):
    total = price * quantity
    total = total - discount
    print("Final Bill:", total)
calculate_bill(1000, 3, 200)





def calculate_cart(price, quantity):
    total = price * quantity
    print("Cart Total:", total)
calculate_cart(1500, 2)



def display_skills(skills):
    for skill in skills:
        print(skill)
display_skills(['python','html','css'])



def display_number(numbers):
    for number in numbers:
        print(number)
display_number((10,20,30,40,50))




def display_student(student):
    for key,value in student.items():
        print(key, ':', value)
display_student({'name' : 'Saniya', 'age': 20, 'Course': 'BCA' })




def calculate_total(price,quantity):
    total = price*quantity
    print('Total : ', total)
calculate_total(500,5)







def print_numbers(numbers):
    for number in numbers:
        print(number)
print_numbers([10,20,30,40,50,60,70,80,90])



def check_marks(marks):
    if marks>=55:
        print('You passed')
    else:
        print('Better luck next time!!')
check_marks(89)





def add(a,b):
    return a+b
result = add(5,10)
print(result)




def employee(name,department,year):
    print(f'{name} is in  {department} department and {year}')
employee(name='Riya',department='BCA',year='3rd')




def create_profle(name,city='Bengluru'):
    print('name : ',  name)
    print('city :', city)
# when city is not provided
create_profle('Sana')
#when city is provided
create_profle('Sana', 'Chenai')



def employee_salary(basic_salary,bonous = 5000):
    total_salry = basic_salary + bonous
    print('total : ', total_salry)
employee_salary(20000)



def  login(username, role='Admin'):
    print('Username : ', username)
    print('Role : ', role)
login('Saniya_1792005')


def add_skills(skill):
    skill.append('Python')
skills = ["GitHub","SQL",'HTML']
add_skills(skills)
print(skills)



def add_number(*numbers):
    total = 0
    for number in numbers:
        total += number
    print('Total of numbers : ', total)
add_number(10,20,30,40,50)
add_number(50,40,30,20,10,1)




def display_skills(*skills):
    for skill in skills:
        print(skill)
display_skills('Python','SQL','HTML')




def student_details(**details):
    print(details)
student_details(name='Saniya', age = 21, Course = 'BCA')



def show_data(**data):
    for key,value in data.items():
        print(key, ':', value)
show_data(name='Asiya', City='Chennai')




def Show(name,*skills,**details):
    print('name :', name)
    print('Skills :', skills)
    print('Details :', details)
Show('Asiya',["Python","SQL","HTML"],city='Bengaluru', course = "BCA")

