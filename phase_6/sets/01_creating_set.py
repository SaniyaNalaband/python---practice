numbers = {10,20,30,40,50}
print(numbers)
print(type(numbers))


numbers = {}
print(numbers)
print(type(numbers))

numbers = set()
print(numbers)
print(type(numbers))



fruits = {'apple','banana','mango'}
print(fruits)



numbers = {10, 20, 30, 40}
print(numbers)


numbers = {10, 20, 30}
numbers.add(40)
print(numbers)



prices = {99.5, 149.99, 250.75}
print(prices)


values = {True, False}
print(values)




data = {10, "Python", 3.14, True}
print(data)



numbers = set([1,2,3,4])
print(numbers)



numbers = (10, 20, 30, 20, 10)
unique_numbers = set(numbers)
print(unique_numbers)




letters = set("Python")
print(letters)


letters = set("banana")
print(letters)



numbers = set(range(1,6))
print(numbers)


# values = (input('enter the values : ')).split()
# print(set(values))




# values = (input('enter the values : ')).split()
# numbers = {int(value) for value in values}
# print(numbers)




numbers = {10, 10, 20, 20, 30, 30}
print(numbers)



numbers = [10, 20, 10, 30, 20, 40, 10]
unique_numbers = set(numbers)
print(unique_numbers)




students = [ "Aisha","Saniya","Aisha","Riya","Saniya"]
unique_students = set(students)
print(unique_students)


products = [ "Laptop","Mouse","Laptop","Keyboard","Mouse"]
unique_products = set(products)
print(unique_products)




numbers = {10, 20, 30, 40}
print(len(numbers))



numbers = {10, 20, 10, 30, 20, 40}
print(len(numbers))




student = { "name": "Aisha",  "age": 21,"course": "BCA"}
keys = set(student)
print(keys)

keys = set(student.keys())
print(keys)

keys = set(student.values())
print(keys)

keys = set(student.items())
print(keys)




letters = set("programming")
print(letters)



numbers = [10, 20, 10, 30, 20, 40, 10]
unique_numbers = set(numbers)
print("Unique values:", unique_numbers)
print("Number of unique values:", len(unique_numbers))



students = [ "Aisha","Saniya","Riya","Aisha","Meera","Saniya"]
print('Unique students : ',set(students))
student = set(students)
print('length of unique numbers : ', (len(student)))




numbers = [10, 20, 30, 10, 40,20, 50, 30, 60, 10]
unique = set(numbers)
print(unique)
print(len(unique))



word = "programming"
unique_word = set(word)
print(unique_word)

