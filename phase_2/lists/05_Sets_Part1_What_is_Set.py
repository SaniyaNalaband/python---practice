fruits = {"Apple", "Banana", "Mango"}
print(fruits)

ids = {101, 102, 103, 102, 101}
print(ids)


# returns dictionary type
empty = {}
print(type(empty))


# returns set type
empty = set()
print(type(empty))

numbers = {10, 20, 20, 30, 30}
print(numbers)

data = {"Python", 100, True, 95.5}
print(data)

letters = {"A", "B", "C"}
print(letters)


numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

data = {"Saniya", 20, 89.5, True, 2 + 3j}
print(data)

numbers = [10, 20, 10, 30, 20, 40]
unique_numbers = set(numbers)
print(unique_numbers)

colors = {"Red", "Green", "Blue"}
print("Green" in colors)
print("Yellow" in colors)


languages = {"python","java","html"}
for language in languages:
    print(languages)


languages = {"Python", "Java", "SQL","html"}
for language in languages:
    print(language)



cities = {"Delhi", "Mumbai"}
cities.add("Bengaluru")
print(cities)


animals = {"Cat", "Dog", "Lion"}
animals.remove("Dog")
print(animals)