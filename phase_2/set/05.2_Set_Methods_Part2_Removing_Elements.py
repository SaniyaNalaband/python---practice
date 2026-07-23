'''1. `remove()`
Removes a specified element.'''

fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Banana")
print(fruits)



# removes an error
# numbers = {10, 20, 30}
# numbers.remove(50)

numbers = {12,13,14,15,16}
numbers.remove(13)
print(numbers)


status = {True, False}
status.remove(False)
print(status)


number = {20, 12+5j,34}
number.remove(12+5j)
print(number)

numbers = {10, 20, 30, 40, 50}
for value in [20, 40]:
    numbers.remove(value)
print(numbers)


items = {(1, 2), (3, 4), (5, 6)}
items.remove((3, 4))
print(items)


'''2. `discard()`
Removes a specified element.'''

numbers = {10, 20, 30}
numbers.discard(20)
print(numbers)

numbers = {10, 20, 30}
numbers.discard(50)
print(numbers)


colors = {"Red", "Green", "Blue"}
color = input("Enter color to discard: ")
colors.discard(color)
print(colors)


numbers = {10, 20, 30, 40, 50}
for value in [20, 60, 40]:
    numbers.discard(value)
print(numbers)


