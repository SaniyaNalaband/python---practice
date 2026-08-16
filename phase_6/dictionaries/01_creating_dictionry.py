student = {'name' : 'saniya', 'age':21,'course':'BCA'}
print(student)

print(student.keys())
print(student.values())
print(student.items())



dictionary = {}
print(dictionary)
print(type(dictionary))



student = {'name' : 'sana', 'age' : 21, 'collge' : 'ABC college', 'year' : 3}
print(student)


student = {'name' : 'saniya','skills' : ['python','git','html']}
print(student)


triangle = {'shape' : 'triangle','coordinates' : (5,4,3)}
print(triangle)




student = {"name": "Neha","skills": {"Python", "SQL", "Git"}}
print(student)



student = {'name' : 'ayesha','address' : {'city = Bengluru', 'state = Karnataka'}}
print(student)



data = {"name": "Asha",1: "One",2.5: "Two Point Five",True: "Yes",(1, 2): "Tuple"}
print(data)




marks = {1: 85,  2: 90, 3: 78}
print(marks)


data = {'score' : 90, 'score':95,'score':99}
print(data)




students = {"student1": "Python","student2": "Python","student3": "SQL"}
print(students)




phone = { "brand": "Samsung", "model": "Galaxy","price": 45000, "storage": "256GB"}
print(phone)


student = dict(name='sana',age=21,course='bca')
print(student)



student = dict([ ("name", "Asha"), ("age", 20),("course", "BCA")])
print(student)



data = [('python',80),('java',85),('html',90)]
marks = dict(data)
print(marks)
print(dict(marks))


keys = ["name", "age", "course"]
values = ["Asha", 20, "BCA"]
dictionary = dict(zip(keys,values))
print(dictionary)





keys = ["name", "age", "course"]
values = ["Asha", 20]
student = dict(zip(keys,values))
print(student)



keys = ["name", "age", "course"]
student = dict.fromkeys(keys)
print(student)



subjects = ["Python", "SQL", "Git"]
marks = dict.fromkeys(subjects,0)
print(marks)




student = {"id": 101,  "name": "Asha","age": 20,"course": "BCA", "skills": ["Python","SQL","Git"]}
print(student)



product = {'product_id' : 101, 'name' : 'S24 Ultra', 'brand' : 'samsung', 'price' : 5000, 'in_stock' : 5, 'rating' : 5,  }
print(product)




product = {"product_id": 101,  "name": "Laptop", "brand": "Dell","price": 55000,"category": "Electronics","in_stock": True,"rating": 4.5,"features": [ "16GB RAM","512GB SSD","WiFi"]}
print(product)




student_information = {'student_id' : 101, 'name' : 'sana', 'age' : 21, 'course' : 'BCA', 'Semister' : '5th', 'percentage' : 99.8, 'skills' :['python','java','html'],  }
print(student_information)



dictionary = {}
print(dictionary)
print(type(dictionary))


example = dict(name = 'sana', age = 20,)
print(example)



dictionary = dict([('string' ,'yes'),('number',99),('year',2026)])
print(dictionary)


keys = ['name','age','course']
values = ['siya', 21,'BCA']
result = dict(zip(keys,values))
print(result)




key = ['string','boolean','charecter']
result = dict.fromkeys(keys)
print(result)



