'''1. `get()`
Returns the value of a given key.'''

student = {
    "name": "Saniya",
    "age": 20
}
print(student.get("name"))
print(student.get('age'))
print(student.get('marks'))


student = {'name':'aisha','age':22}
print(student.get('city','not availaible'))

marks = {'python':99,'java':98,'html':99}
print(marks.get('python'))

settings = { 'dark_mode': True, 'notifications':False}
print(settings.get('dark_mode'))



student = { 'name' : 'alisha', 'marks':{'css':98,'python':99}}
print(student.get('marks','python'))

student = {'name' : 'ayeza', 'skills':['sql','python','html']} 
print(student.get('skills'))


products = {'Laptop':10,'mouse':25,'keyboard':15}
print(products.get('Laptop'))
print(products.get('mouse'))




'''2. `keys()`
Returns a view containing all keys.'''

student = {
    "name": "Saniya",
    "age": 20,
    "city": "Hubli"
}
print(student.keys())

for key in student.keys():
    print(key)


student = {
    "name": "Riya",
    "age": 21,
    "city": "Bengaluru"
}
keys = list(student.keys())
print(keys)



student = {
    "name": "Saniya",
    "age": 20,
    "course": "Python"
}
for key in student.keys():
    print(key, ":", student[key])



student = {
    "name": "Saniya",
    "age": 20
}
print('name'in student.keys())
print('age' in student.keys())


employee = {'id' :101, 'name':'Siya','salary':10000,'city':'Belgum'}
print(len(employee.keys()))


student = {'name':'Jhon','age':20,}
print(student.keys())
student['course']='python'
print(student.keys())


''' 3. `values()`
Returns a view containing all values.'''


student = {
    "name": "Saniya",
    "age": 20,
    "city": "Hubli"
}
print(student.values())

for value in student.values():
    print(value)



employee = {
    "id": 101,
    "name": "Riya",
    "salary": 50000,
    "city": "Bengaluru"
}

print(len(employee.values()))


student = {'name':'Jokey','age':20,'marks':{'python':99,'java':90}}
print(student.values())

print('jhony' in student)
print('java' in student['marks'])
print('java' in student)


marks = {'python':99,'java':98,'html':97}
print(sum(marks.values()))

'''4. `items()`
Returns all key-value pairs as tuples.'''

student = {
    "name": "Saniya",
    "age": 20
}
print(student.items())

for key,value in student.items():
  print(key,value)


student = {
    "name": "Aisha",
    "age": 22,
    "city": "Mysuru"
}
for key, value in student.items():
    print(key, ":", value)


marks = {
    "Math": 95,
    "Science": 90,
    "English": 88
}
for subject, mark in marks.items():
    print(subject, "=", mark)


student = {
    "name": "Saniya",
    "marks": {
        "Math": 95,
        "Python": 100
    }
}
for key, value in student.items():
    print(key, ":", value)