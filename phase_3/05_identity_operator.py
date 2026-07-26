''' 1️⃣ Identity Operator (`is`)
Checks whether two variables point to the **same object**.'''



a = [1,2,3]
b = a
print(a is b )


a = [10,20]
b = [20,10]
print(a is b)

a = [10,20]
b = [10,20]
print(a==b)
print(a is b)
print(b is a)



employee = {'name' : 'Riya'}
manager = employee 
print(employee is manager)
print(manager is employee)


employee1 = {'id':101}
employee2 = {'id':102}
print(employee1 is employee2)
print(employee2 is employee1)

cart = ["Laptop", "Mouse"]
backup_cart = cart
print(cart is backup_cart)

cart1 = ["Laptop", "Mouse"]
cart2 = ["Laptop", "Mouse"]
print(cart1 is cart2)

connection1 = {'status' :'connected'}
connection2 = connection1
print(connection1 is connection2)
print(connection2 is connection1)


user_name = None
print(user_name is None)

student = {"name": "Riya"}
current_student = student
print(student is current_student)


''' 2️⃣ Identity Operator (`is not`)
Checks whether two variables refer to **different objects**.'''


a = [1,2]
b = [1,2]
print(a is not b)


a = [1,2]
b = a
print(a is not b )

student1 = {"name": "Saniya"}
student2 = {"name": "Saniya"}
print(student1 is not student2)

cart1 = ["Laptop", "Mouse"]
cart2 = cart1
print(cart1 is not cart2)

account1 = {"balance": 5000}
account2 = {"balance": 5000}
print(account1 is not account2)

employee = {"id": 101}
backup = employee
print(employee is not backup)

'''📖 Identity with `None`
The recommended way to check for `None` is using `is`.'''

value = None
print(value is None)


name = 'python'
print(name is not None)


username = None
if username is None:
    print("please!!  login.")


profile_picture = None
if profile_picture is None:
    print('Please!! upload your profile picture.')

email = "abc@gmail.com"
print(email is None)



''' 📖 Using `id()`
The `id()` function returns the memory identity of an object.'''


a = [1,2,3]
a = b 
print(id(a))
print(id(b))

# we'll get same id's for both becausse strings are imutable
a = 'python'
b = 'python'
print(id(a))
print(id(b))


a = 'python'
b = 'html'
print(id(a))
print(id(b))

# we'll get differen id's for both becausse lists are mutable
a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))

