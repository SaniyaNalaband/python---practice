student = {'student1' : {'name' : 'asha', 'age':21}, 'student2':{'name':'siya','age':20}}
print(student)
print(student['student1'])
print(student['student2'])


print(student['student1']['name'])
print(student['student2']['name'])



print(student['student1']['name'])
print(student['student1']['age'])
print(student['student2']['name'])
print(student['student2']['age'])


company = {'employee' : {'profile' : { 'name' : 'sana', 'age': 20}}}
print(company)
print(company['employee'])
print(company['employee']['profile'])
print(company['employee']['profile']['name'])
print(company['employee']['profile']['age'])


company['employee']['profile']['age'] = 21
print(company)

company['employee']['experience'] = '2 years'
print(company)

company['employee']['profile']['course'] = 'BCA'
print(company)



company['employee2'] = {'name': 'riya', 'age':20}
print(company)



del company['employee2']['age']
print(company)


del company['employee2']
print(company)



students = {"student1": {"name": "Asha","age": 20},"student2": {"name": "Neha","age": 21 }}
removed = students.pop("student2")
print(removed)
print(students)


print(students.get('student2'))
print(students.get('student1'))

print(students.get('student1').get('name'))
print(students.get('student1').get('age'))


students = { "student1": {"name": "Asha","age": 20},"student2": {"name": "Neha","age": 21}}
print(students.keys())


print(students['student1'].keys())
print(students['student2'].keys())

print(students.values())
print(students['student1'].values())




students = {"student1": {"name": "Asha","age": 20},"student2": {"name": "Neha",  "age": 21}}
print(students.items())


