fruits = ("Apple", "Banana", "Mango")
print(fruits)


languages = ("Python", "Java", "C", "JavaScript")
print(languages)


prices = (99.5, 149.99, 250.75)
print(prices)



student = ("Saniya", 21, 85.5, True)
print(student)


data = ("Python",3,3.14,True,   None)
print(data)




name = ("Python")
print(type(name))



name = ("Python",)
print(type(name))



numbers = 10, 20, 30
print(numbers)
print(type(numbers))


numbers = tuple([10, 20, 30])
print(numbers)


numbers_list = [10, 20, 30, 40]
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)


print(type(numbers_list))
print(type(numbers_tuple))



word = 'Hello'
list_word = tuple(word)
print(list_word)



numbers = tuple(range(1,6))
print(numbers)


numbers = tuple(range(10, 21, 2))
print(numbers)


data = (("Aisha", 85),("Saniya", 92),   ("Rohan", 78))
print(data)


numbers = ((1, 2, 3),(4, 5, 6),(7, 8, 9))
print(numbers)



data = ("Python",[10, 20, 30])
print(data)



data = ("Python", [10, 20, 30])
data[1].append(40)
print(data)



data = ("Python",3.14,[10, 20],{"name": "Aisha"}, (1, 2),)
print(data)




numbers = {10, 20, 30}
number_tuples = tuple(numbers)
print(number_tuples)




student = {"name": "Aisha","age": 21,"marks": 90}
tuple_student = tuple(student)
print(tuple_student)
result = tuple(student.items())
print(result)




a = 10
b = 20
numbers = (a, b, a + b)
print(numbers)



name = "Saniya"
age = 21
marks = 90
student = (name, age, marks)
print(student)



days = ("Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days)




numbers = (10, 20, 30, 40, 50)
print(numbers)



languages = ( "Python","Java","C","JavaScript")
print(languages)




empty = ()
print(empty)


number = (100,)
print(number)


product = {'name' : 'Laptop', 'ID' : 101, 'price' : 5000, 'category' : 'Electronics', 'stock' : '50pcs'}
print(tuple(product.items()))
print(type(tuple(product.items())))
print(len(tuple(product.items())))

single_tuple = ('single',)
print(single_tuple)

