fruits = ["Apple", "Banana", "Mango", "Orange"]
position = fruits.index('Orange')
print(position)



numbers = [10, 20, 30, 20, 40]
print(numbers.index(20))


colors = ["Red", "Blue", "Green"]
color = 'Blue'
position = colors.index(color)
print(position)



numbers = [10, 20, 30, 20, 40, 20]
print(numbers.index(20,4))


numbers = [10, 20, 30]
if 50 in numbers:
    print(numbers.index(50))
else:
    print('number not found')



fruits = ["Apple", "Banana", "Mango"]
if 'Mango' in fruits:
    print('the fruit is at index no : ', fruits.index('Mango'))



numbers = [10, 20, 30, 20, 40, 20]
print(numbers.index(30,1,4))


letters = ["P", "Y", "T", "H", "O", "N"]
print(letters.index('O'))



inventory = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]
item = 'MOnitor'
if item in inventory:
    print(inventory.index(item))



numbers = [10, 20, 10, 30, 10, 40]
positons = []
for i in range(len(numbers)):
    if numbers[i] == 10:
        positons.append(i)
print(positons)



numbers = [10, 20, 10, 30, 10]
positions = []
start = 0
while True:
    try:
        positon = numbers.index(10,start)
        positions.append(positon)
        start = position + 1
    except ValueError:
        break






numbers = [10, 20, 20, 30, 20]
print(numbers.count(20))


fruits = ["Apple", "Mango", "Apple", "Orange"]
print(fruits.count('Apple'))

