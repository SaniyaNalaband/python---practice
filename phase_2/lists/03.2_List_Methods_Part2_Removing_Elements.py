'''1. `remove()`
Removes the **first occurrence** of a specified value.'''


fruits = ['mango','orange','banana']
fruits.remove('banana')
print(fruits)

numbers = [10,20,20,30,40]
numbers.remove(20)
print(numbers)


# numbers = [10,20,30]
# numbers.remove(50) #-----> throws an error (value not found)
# print(numbers)

floating_numbers = [12.5,99.0,99.7]
floating_numbers.remove(12.5)
print(floating_numbers)

status = [True,False,True]
status.remove(False)
print(status)


numbers = [2,3+4j,4]
numbers.remove(3+4j)
print(numbers)



# fruits = ['orange','mango','banana']
# fruit = input('enter a fruit you want to remove : ')
# fruits.remove(fruit)
# print(fruits)


list = [1,2,[4,5],5]
list.remove([4,5])
print(list)

'''2. `pop()`
Removes and **returns** an element.
'''


fruits = ["Apple", "Banana", "Mango"]
fruits.pop()
print(fruits)


numbers = [10, 20, 30]
numbers.pop(1)
print(numbers)


numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)


# cities = ['bengluru','hubli','dharwad']
# city = int(input('enter number of index you want to remove :'))
# cities.pop(city)
# print(cities)

'''3. `clear()`
Removes **all elements** from the list.'''


numbers = [10, 20, 30]
numbers.clear()
print(numbers)


students = ["Rahul", "Priya", "Saniya"]
print("Total students before:", len(students))
students.clear()
print("Total students after:", len(students))
print(students)


'''4. `del` Keyword
> **Note:** `del` is a **Python keyword**, not a list method.'''

## Delete One Element

numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)


## Delete Multiple Elements


numbers = [10, 20, 30, 40, 50]
del numbers[1:4]
print(numbers)

## Delete Entire List


numbers = [10, 20, 30]
del numbers
print(numbers)

