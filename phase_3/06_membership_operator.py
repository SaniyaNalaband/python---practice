'''1️⃣ `in` Operator
The `in` operator checks whether a value exists in a sequence.'''

text = 'python'
print('p' in text)

print("z" in "Python")

numbers = [10, 20, 30, 40]
print(20 in numbers)

fruits = ("Apple", "Mango", "Banana")
print("Apple" in fruits)

colors = {"Red", "Blue", "Green"}
print("Blue" in colors)


student = {
    "name": "Saniya",
    "age": 21
}
print("name" in student)

cart = ["Laptop", "Mouse", "Keyboard"]
print("Laptop" in cart)

password = "Saniya@123"
print("@" in password)

movies = ["Inception", "Avatar", "Titanic"]
print("Avatar" in movies)

today = "Monday"
weekend = ("Saturday", "Sunday")
print(today in weekend)

city = "Bengaluru"
print("Delhi" in city)


student = {
    "name": "Saniya",
    "age": 21
}
print(("name", "Saniya") in student.items())


student = {
    "name": "Saniya",
    "age": 21
}
print("Saniya" in student.values())





'''2️⃣ `not in` Operator
Checks whether a value does **not** exist.'''

print("x" not in "Python")


numbers = [1, 2, 3]
print(10 not in numbers)

fruits = ("Apple", "Orange")
print("Banana" not in fruits)

colors = {"Red", "Blue"}
print("Green" not in colors)


student = {
    "name": "Saniya",
    "age": 21
}
print("city" not in student)


password = "Python@123"
print(" " not in password)



email = "saniya@gmail.com"
print(".org" not in email)

