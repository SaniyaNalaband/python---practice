'''1. `update()`
Updates an existing key or adds new key-value pairs.'''


student = {'name':'Kity','age':20}
student.update({'age':21})
print(student)


student = {'name':'kity'}
student.update({'city':'Bengluru'})
print(student)

student = {"name": "Saniya"}

student.update({"age": 20,"course": "AI ML","city": "Hubli"})
print(student)


student = { "name": "Saniya","age": 20}

extra = { "city": "Hubli", "country": "India"}
student.update(extra)
print(student)


student = { "name": "Saniya"}
student.update(age=20, city="Hubli")
print(student)


dict1 = { "a": 10,"b": 20}
dict2 = {"c": 30,"d": 40}
dict1.update(dict2)
print(dict1)


student = {"name": "Aisha"}
student.update(age=20, city="Mysuru")
print(student)

student = { "name": "Saniya","marks": {"Math": 90}}
student.update({"grade": "A"})
print(student)

user = {"username": "saniya123"}
user.update({  "email": "saniya@gmail.com", "verified": True})
print(user)



'''2. `setdefault()`
Returns the value of a key.'''


student = { "name": "Saniya","age": 20}
result = student.setdefault("age", 25)
print(result)
print(student)


student = { "name": "Saniya"}
result = student.setdefault("age", 20)
print(result)
print(student)


student = {"name": "Saniya"}
student.setdefault("city")
print(student)

