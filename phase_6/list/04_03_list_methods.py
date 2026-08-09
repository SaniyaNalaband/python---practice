fruits = ["Apple", "Banana", "Mango", "Orange"]
position = fruits.index("Mango")
print(position)

numbers = [10, 20, 30, 20, 40]
print(numbers.index(20))


colors = ["Red", "Blue", "Green"]
color = 'Blue'
position = colors.index(color)
print('position : ', position)


numbers = [10, 20, 30, 20, 40, 20]
positions  = numbers.index(40,0,5)
print(positions)



numbers = [10, 20, 30]
if 40 in numbers:
    print(numbers.index(40))
else:
    print('Value not found')





fruits = ["Apple", "Banana", "Mango"]
if 'Mango' in fruits:
    postion = fruits.index('Mango')
    print('Mango is at index : ', position)




inventory = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]
item = "Monitor"
if item in inventory:
    position = inventory.index(item)
    print('Item position : ',position)






numbers = [10, 20, 10, 30, 10, 40]
position =  []
for i in range(len(numbers)):
    if numbers[i] == 10:
        position.append(i)
print(position)




numbers = [10, 20, 20, 30, 20]
print(numbers.count(20))


fruits = ["Apple", "Mango", "Apple", "Orange"]
print(fruits.count("Apple"))



numbers = [10, 20, 30]
print(numbers.count(100))



values = [True, False, True, True, False]
print(values.count(True))
print(values.count(False))



numbers = [10, 20, 30, 20, 40]
if numbers.count(20)>1:
    print('Repeated more than once')
else:
    print('not repeated')



numbers = [10, 20, 20, 30, 30, 30, 40]
for number in numbers:
    if numbers.count(number)>1:
        print(number)




numbers = [10, 20, 20, 30, 30, 30, 40]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print(duplicates) 





fruits = ["Apple", "Banana", "Apple", "Mango", "Banana", "Apple"]
unique_fruit = []
for fruit in fruits:
    if fruit not in unique_fruit:
        unique_fruit.append(fruit)

for fruit in unique_fruit:
    print(fruit , ':', fruit.count(fruit))



numbers = [2, 4, 6, 7, 8, 10]
even_numbers = []
for number in numbers:
    if number%2==0:
       even_numbers.append(number)
print(even_numbers)




fruits = ["Apple", "Banana", "Mango"]
print('Apple' in fruits)



fruits = ["Apple", "Banana", "Mango"]
print("Orange" in fruits)



students = ["Aisha", "Saniya", "Rohan"]
if'Aisha' in students:
    print('student found')




products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
product = 'Monitor'
if product in products:
   print('Product vaialable')
else:
    print('Product not available')



cart = ["Laptop", "Mouse", "Keyboard"]
required_items = ["Laptop", "Keyboard"]
for item in required_items:
    if item in cart:
        print(item,' is availabale')
    else:
        print('item not available')


numbers = [10, 20, 30, 20, 40]
seen = []
for number in numbers:
    if number in seen:
        print('duplicate', number)
    else:
        seen.append(number)




fruits = ["Apple", "Banana", "Mango"]
print("Orange" not in fruits)


products = ["Laptop", "Mouse", "Keyboard", "Mouse", "Monitor"]
product = "Mouse"
if product in products:
    print("Product Available")
    print("First Position:", products.index(product))
    print("Quantity:", products.count(product))
else:
    print("Product Not Available")




