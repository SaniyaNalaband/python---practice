'''1️⃣ AND Operator (`and`)
The `and` operator returns **True only if both conditions are True**.'''


age = 25
print(age > 18 and age < 60)


marks = 80
print(marks >= 35 and marks <= 100)

age = 22 
has_license = True
print(age>=18 and has_license)


age = 20
is_citizen = True
print(age >= 18 and is_citizen)


username = "Saniya"
password = "Python123"
print(username == "Saniya" and password == "Python123")

balance = 5000
pin_correct = True
print(balance >= 1000 and pin_correct)

order_amount = 1200
premium_member = True
print(order_amount >= 1000 and premium_member)

python_marks = 70
java_marks = 75
print(python_marks >= 35 and java_marks >= 35)

''' 2️⃣ OR Operator (`or`)
The `or` operator returns **True if at least one condition is True**.'''


age = 16
print(age < 18 or age > 60)


username = "admin"
password = "1234"
print(username == "admin" or password == "admin123")


day = "Saturday"
print(day == "Saturday" or day == "Sunday")

age = 16
special_permission = True
print(age >= 18 or special_permission)

username = "Saniya"
email = "abc@gmail.com"
print(username == "Saniya" or email == "saniya@gmail.com")


balance = 500
overdraft = True
print(balance >= 1000 or overdraft)

order_amount = 500
premium_member = True
print(order_amount >= 1000 or premium_member)

attendence = 100
total_student = 50
print(attendence<90 or total_student>60)


salary = 100000
experience = 6 
print(salary<5000 or experience>8)


'''3️⃣ NOT Operator (`not`)
The `not` operator **reverses** the Boolean result.'''

is_loged_in = True
print(not is_loged_in)

print(not (10 > 5))

shop_open = False
print(not shop_open)


is_registered = False
print(not is_registered)

book_available = False
print(not book_available)

