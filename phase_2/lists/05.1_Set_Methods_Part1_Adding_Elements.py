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