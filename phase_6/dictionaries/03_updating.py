student = { "name": "Asha",  "age": 20 } 
student['age'] = 21
print(student)



student = {   "name": "Asha", "age": 20 }
student['name'] = 'siya'
print(student)


student = { "name": "Asha", "skills": ["Python", "SQL"] } 
student['skills'] = ['python','SQL','java']
print(student)



student = { "name": "Asha", "location": (12.97, 77.59) } 
student["location"] = (13.08, 80.27) 
print(student) 




student = {  "name": "Asha", "age": 20 } 
student['course' ] = 'BCA'
print(student)





student = { "name": "Asha", "age": 20, "course": "BCA" } 
student["name"] = "Neha" 
student["age"] = 21 
student["course"] = "MCA" 
print(student)





student = { "name": "Asha", "age": 20 } 
student.update({"age": 21}) 
print(student)



student = {  "name": "Asha",  "age": 20,  "course": "BCA" } 
student.update({ "age": 21,  "course": "MCA" }) 
print(student) 


student = { 
    "name": "Asha", 
    "age": 20 
} 
 
student.update([ ("age", 21),  ("course", "BCA") ]) 
print(student) 



student = { "name": "Asha" } 
keys = ["age", "course"] 
values = [20, "BCA"] 
student.update(zip(keys, values)) 
print(student)




product = { "name": "Laptop",   "price": 50000 } 
product["price"] = product["price"] + 5000 
print(product)



scores = {  "Python": 80, "SQL": 75} 
scores["Python"] += 5 
print(scores)


