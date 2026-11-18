def introduce(name,age,course):
    print(name)
    print(age)
    print(course)
introduce('Anaa',21,'BCA')



def employee(name,department,salary):
    print(name)
    print(department)
    print(salary)
employee('SANA',"IT",25000)




def multiply(a,b):
    return a*b
print(multiply(5,2))





def message(name,city):
    print(name,'lives in', city)
message('Riya','Bengluru')



def calculate(a,b,c):
    return (a+b)*c
print(calculate(10,20,30))


def print_numbers(start,end):
    for number in range(start,end+1):
        print(number)
print_numbers(1,5)




def display_skills(skills):
    for skill in skills:
        print(skill)
skills = ['Python','SQL','CSS']
display_skills(skills)




def student_result_manegment_system(name,python_marks,SQL_marks,HTML_marks,Git_marks):
    print('Student name :',name)
    print('Python marks : ',python_marks)
    print('SQL marks : ',SQL_marks)
    print('HTML marks : ',HTML_marks)
    print('Git marks : ',Git_marks)
    all = python_marks,Git_marks,HTML_marks,SQL_marks
    total = sum(all)
    print(total)
    average = total/4
    print(average)
    if average>= 35:
        print(name,'You are passed!!')
    else:
        print('Better luck next time')

student_result_manegment_system('Riya',99,66,87,84)





def employee_salary_manegment(emp_name,department,basic_salary,experience):
    print('Employee name :',emp_name)
    print('Department :',department)
    print('Salary :',basic_salary)
    print('Experience :',experience)
    bonus = basic_salary + 2000
    print('Bonus Salary :',bonus)
employee_salary_manegment('Jerry','IT',50000,5)






