'''1. `pop()`
Removes a specified key and returns its value.'''


student = { "name": "Saniya", "age": 20}
age = student.pop("age")
print(age)
print(student)

# student = {"name": "Saniya"}
# student.pop("age")

student = {  "name": "Saniya"}
result = student.pop("age", "Not Found")
print(result)
print(student)

student = {'name':'ayesha','age':21}
result = student.pop('city','not found')
print(result)
print(student)

student = {  "name": "Saniya",  "marks": {  "Math": 95, "English": 9 }}
marks = student.pop("marks")
print(marks)
print(student)

employee = {'id':201,'age':22,'skills':'python,java','salary':50000}
salary  = employee.pop('salary')
print('removed salary :'  , salary)
print(employee)

# # student = { "name": "Saniya", "age": 20, "course": "Python"}
# key = input("Enter key to remove: ")
# value = student.pop(key, "Key Not Found")
# print(value)
# print(student)


'''2. `popitem()`
Removes and returns the **last inserted key-value pair**.'''


student = { "name": "Saniya", "age": 20, "city": "Hubli"}
item = student.popitem()
print(item)
print(student)


data = {  "a": 1, "b": 2,  "c": 3,  "d": 4}
print(data.popitem())
print(data.popitem())
print(data)

numbers = {"one": 1,"two": 2,"three": 3}
while numbers:
    print(numbers.popitem())

student = {  "name": "Riya",  "marks": {  "Math": 90,  "Science": 95  }}
print(student.popitem())
print(student)

student = {'name':'jackey' , 'age':22}
key,value = student.popitem()
print('key : ',key)
print('value : ', value)
print(student)


data = {}
data["A"] = 10
data["B"] = 20
data["C"] = 30
print(data.popitem())
print(data.popitem())
print(data.popitem())


'''3. `clear()`
Removes all key-value pairs from the dictionary.
'''

student = {  "name": "Saniya",  "age": 20}
student.clear()
print(student)


session = {  "user": "Saniya",  "logged_in": True}
session.clear()
print(session)

