student = {'name': 'saniya', 'age':21, 'course':'BCA'}
print(student['name'])
print(student['age'])
print(student['course'])




marks = {1:90, 2:95, 3:100}
print(marks[1])
print(marks[2])
print(marks[3])


student = { "name": "Asha", "age": 20}
print(student.get("name"))



student = { "name": "Asha"}
print(student["name"])

print(student.get('name'))



student = {"name": "Asha"}
print(student.get("city"))

# student = {"name": "Asha"}  ----> this throws an error 
# print(student["city"])



student = {"name": "Asha","age": 20}
print(student.get("city", "Not Available"))


product = {"name": "Laptop","price": 55000}
print(product.get("brand", "Brand not provided"))




# products = {"Laptop": 55000,"Phone": 25000,  "Headphones": 3000,"Keyboard": 1500}
# product = input('enter the product name : ')
# price = products.get(product,'invalid product name')
# print('price : ',price)




# accounts = { "A101": 25000,"A102": 18000, "A103": 42000, "A104": 15000}
# account_number = input('enter the account number : ')
# balance = accounts.get(account_number, 'invalid account number')
# print('balance : ', balance)


# marks = {"S001": 85,"S002": 72,"S003": 91, "S004": 68}
# student_id = input('enter the student id : ')
# mark = marks.get(student_id, 'invalid id ')
# print('Your marks is : ',mark)




# menu = {"Pizza": 250,"Burger": 150, "Pasta": 200,"Sandwich": 120}
# food = input('enter the food item : ')
# price = menu.get(food, 'invalid food item')
# print('price is : ', price)




student = {"name": "Asha","skills": ["Python", "SQL", "Git"]}
result = student["skills"][0]
print(result)




student = {"skills": ["Python", "SQL", "Git"]}
print(student["skills"][0])
print(student['skills'][1])
print(student['skills'][2])




student = {"coordinates": (12.97, 77.59)}
print(student["coordinates"])


student = {"coordinates": (12.97, 77.59)}
print(student["coordinates"][0])
print(student["coordinates"][1])



student = {"address": {"city": "Bengaluru","state": "Karnataka"}}
print(student["address"])



student = {"address": {"city": "Bengaluru","state": "Karnataka"}}
print(student["address"]["city"])



student = {"address": {"city": "Bengaluru", "state": "Karnataka","pincode": 560001}}
print(student['address']['city'])
print(student['address']['state'])
print(student["address"]['pincode'])



company = {"employee": {"address": {"city": "Bengaluru","state": "Karnataka"}}}
print(company["employee"])
print(company["employee"]['address'])
print(company['employee']['address']['city'])
# print(company['employee']['address']['city']['state'])



student = { "name": "Asha","age": 20, "course": "BCA"}
for key in student :
    print(key, '=', student[key])


student = { "name": "Asha","age": 20, "course": "BCA"}
for key in student:
    print(key, '=', student.get(key))




student = {"name": "Asha","age": 20}
if 'name' in student:
    print(student['name'])



student = {"name": "Asha","age": 20}
if 'city' in student:
    print(student['city'])
else:
    print('city not available')



data = {'name' : 'sana', 'age' : 21, 'city':'bengluru'}
print(data)
print(data['name'])
print(data["age"])
print(data['city'])




data = {'name' : 'sana', 'age' : 21, 'city':'bengluru'}
print(data.get('name'))
print(data.get('age'))
print(data.get('city'))




dictionary = {'skills':['python','java']}
print(dictionary)