student = {'name' : 'Asha', 'age': 21}
print(student.keys())


student = {    "name": "Asha",   "age": 20,  "course": "BCA"  }  
print(student.get("name"))  


student = { "name": "Asha",     "age": 20,    "course": "BCA"  }  
key = list(student.keys())
print(key)
print(list(student.keys()))


for key in student.keys():
    print(key)


print(student.values())
print(list(student.values()))
for value in student.values():
    print(value)



student = {    "name": "Asha",  "age": 20,  "course": "BCA"  }  
print(student.items())
print(list(student.items()))
for item in student.items():
    print(item)





for key,value in student.items():
    print(key,'=',value)



student = {    "name": "Asha",  "age": 20  }  
update_studetns = ({'course' : 'BCA'})
print(update_studetns)


update_age = ({'age' : 21})
print(update_age)



student = {  "name": "Asha"  } 
updating = ({'age' : 21, 'course' : 'BCA'})
print(updating)


student = {  "name": "Asha",  "age": 20,  "course": "BCA"  } 
remove = student.pop('age')
print(remove)
print(student)


student = {  "name": "Asha"  }  
result = student.pop("city", "Not Found")  
print(result) 



student =   {"name": "Asha",  "age": 20,  "course": "BCA"  }  
item = student.popitem()  
print(item)  
print(student) 



student =   {"name": "Asha",  "age": 20,  "course": "BCA"  }  
student.clear()
print(student)




student = {  "name": "Asha",  "age": 20  }  
result = student.setdefault("age", 25)  
print(result)  
print(student) 




student = { "name": "Asha",   "age": 20  } 
result = student.setdefault("city", "Bengaluru")  
print(result)  
print(student) 



keys = ["name", "age", "course"]  
student = dict.fromkeys(keys)  
print(student) 

keys = ["name", "age", "course"]  
student = dict.fromkeys(keys,0)  
print(student) 



product = {   "name": "Laptop",   "price": 55000,      "stock": 10  }  
product.update({'brand' : 'dell'})
product["stock"] = product['stock']-1
print(product)



student = {  
    "name": "Asha",  
    "age": 20  
}  
  
student.update({   "course": "BCA",    "city": "Bengaluru" })  
print(student)


product = {   "name": "Laptop",   "price": 55000,      "stock": 10  }  
remove = product.pop('stock')
print(remove)



product = {   "name": "Laptop",   "price": 55000,      "stock": 10  }  
print(product.popitem())
print(product) 


student = {  "name": "Asha",  "age": 20  }  
student.clear()  
print(student) 




student = {   "name": "Asha",  "age": 20  }  
student.setdefault("city", "Bengaluru")  
print(student) 




student = {'name' : 'saniya', 'age': 21, 'course': 'BCA', 'semister' : '4th sem', 'percentage' : 99.9, 'city' : 'Bengluru'}
print(student.get('name'))
print(student.keys())
print(student.values())
print(student.items())
(student.update({'college' : 'ABC collge'}))
print(student)
print(student.pop('city'))
student.setdefault('status')
print(student)




product = {'product_id' : 101, 'product_name' : 'Laptop', 'brand' : 'hp', 'price' : 55000, 'category' : 'electonics', 'stock' : 10}
print(product.get('product_name'))
print(product.keys())
print(product.values())
print(product.items())
product.update({'ratings' : '5 star'})
print(product)
print(product.pop('stock'))
product.setdefault('availability', 'available')
print(product)

