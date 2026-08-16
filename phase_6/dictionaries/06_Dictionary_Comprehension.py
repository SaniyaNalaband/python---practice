squares = {x:x*x for x in range(1,6)} # --> x is a key and x*x is a value
print(squares)


numbers = {x:x*2 for x in range(1,6)}
print(numbers)


number = {x: x for x in range(1,6)}
print(number)

squares = {x: x**2 for x in range(1,6)}
print(squares)


names = ["Asha", "Neha", "Kiran"]
name_length = {name:len(name) for name in names }
print(name_length)



names = ["Asha", "Neha", "Kiran"]
upper_Case = {name:name.upper() for name in names}
print(upper_Case)



even_numbers = {x:x*x for x in range(1,10) if x%2==0}
print(even_numbers)


odd_numbers = {x: x ** 2 for x in range(1, 11) if x % 2 != 0}
print(odd_numbers)



numbers = {x: x for x in range(1, 11) if x > 5}
print(numbers)


result = {x: "Even" if x % 2 == 0 else "Odd" for x in range(1, 6)}
print(result)




marks = {
    "Python": 90,
    "SQL": 72,
    "Git": 85,
    "HTML": 68
}

passed = {subject: mark for subject, mark in marks.items()  if mark >= 75}
print(passed)





prices = {
    "laptop": 50000,
    "phone": 30000,
    "tablet": 20000
}

uppercase_keys = {product.upper(): price   for product, price in prices.items()}
print(uppercase_keys)



result = {x: {y: x * y for y in range(1, 4)}for x in range(1, 4)}
print(result)



data = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = { value: key for key, value in data.items()}
print(inverted)