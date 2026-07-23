'''1. `add()`
Adds **one element** to a set.'''

fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits)


numbers = {10, 20}
numbers.add(30)
print(numbers)

numbers = {10, 20}
numbers.add(20)
print(numbers)



data = {"Python"}
data.add(100)
data.add(True)
print(data)


items = {"Apple"}
items.add(("Banana", "Mango"))
print(items)


a = {1, 2}
b = {3, 4}
a.update(b)
print(a)

numbers = {1, 2}
numbers.update((3, 4))
print(numbers)