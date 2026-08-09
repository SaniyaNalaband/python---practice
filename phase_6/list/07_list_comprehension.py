numbers = []
for number in range(1,6):
    numbers.append(number)
print(numbers)
        

numbers = [ number for number in range(1,6) ]
print(numbers)


squares = [number ** 2 for number in range(1,6)]
print(squares)


cubes = [number ** 3 for number in range(1,6)]
print(cubes)




numbers = [1, 2, 3, 4, 5]
result = [number * 10 for number in numbers]
print(result)



numbers = [10, 20, 30, 40]
result = [number+5 for number in numbers]
print(result)



names = ["aisha", "saniya", "rohan"]
upper_names = [name.upper() for name in names]
print(upper_names)



names = ["APPLE", "BANANA", "MANGO"]
lower_names = [fruit.lower() for fruit in names]
print(lower_names)


names = ["Aisha", "Saniya", "Rohan"]
string_length = [len(names) for names in names]
print(string_length)



numbers = [number for number in range(1,11)]
print(numbers)



numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number%2==0 for number in numbers]
print(even_numbers)


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number%2==0]
print(even_numbers)



numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = [number for number in numbers if number%2!=0]
print(odd_numbers)


numbers = [5, 12, 8, 20, 15, 3]
greater = [number for number in numbers if number>10]
print('Number greater than ten : ', greater)



numbers = [10, 12, 15, 22, 25, 31, 40]
result = [number for number in numbers if number%5==0]
print(result)



numbers = [1, 2, 3, 4, 5]
result =  [ 'even' if number%2==0 else 'odd' for number in numbers]
print(result)



marks = [85, 32, 76, 28, 90]
result = ['pass' if mark>=35 else 'fail' for mark in marks]
print(result)





numbers = [10, -5, 20, -8, 0]
result = ['positive' if number>0  else 'negative' for number in numbers]
print(result)




word = "Python"
letters = [letter for letter in word]
print(letters)


letters = [letter.upper() for letter in word]
print(letters)



word = "programming"
vowels = [letter for letter in word if letter in 'aeiou']
print(vowels)



text = "Python is easy"
space = [char for char in text if  char!=""]
print(space)



words = ["Python", "Java", "Programming", "C", "Developer"]
result=[word for word in words if len(word)>5]
print(result)



prices = [10.567, 20.432, 30.876]
rounded_price = [round(price,2) for price in prices]
print(rounded_price)



numbers = [10, 20, 30]
str_converted = [str(number) for number in numbers]
print(str_converted)




values = ["10", "20", "30"]
numbers = [int(value) for value in values]
print(numbers)



matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = [ value for row in matrix for value in row ]
print(result)




matrix = [
    [0 for column in range(3)]
    for row in range(3)
]
print(matrix)






matrix = [
    [row * column for column in range(1, 4)]
    for row in range(1, 4)
]
print(matrix)




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
even_numbers = [value for row in matrix for value in row if value%2==0]
print(even_numbers)





numbers = range(1, 21)
result = [number for number in numbers if number%2==0 if number>10]
print(result)



numbers = range(1, 21)
result = [
    number
    for number in numbers
    if number % 2 == 0 and number > 10
]
print(result)






numbers = range(1, 11)
result = [
    number
    for number in numbers
    if number < 3 or number > 8
]
print(result)






prices = [100, 200, 300, 400]
new_prices = [price * 1.10 for price in prices]
new_prices = [round(price * 1.10, 2) for price in prices]
print(new_prices)




celsius = [0, 10, 20, 30, 40]
fahrenheit = [
    (temperature * 9 / 5) + 32
    for temperature in celsius
]
print(fahrenheit)





contacts = [
    "aisha@gmail.com",
    "rohan@yahoo.com",
    "saniya@gmail.com",
    "admin@company.com"
]
gmail = [email for email in contacts if email.endswith('gmail.com')]
print(gmail)





names = [" Aisha ", " Saniya ", " Rohan "]
clean = [name.strip() for name in names]
print(clean)




table = [
    [row * column for column in range(1, 6)]
    for row in range(1, 6)
]
for row in table:
    print(row)



marks = [
    [80, 90, 70],
    [75, 85, 95],
    [88, 92, 84]
]
updated_marks = [ mark + 5 for student in marks  for mark in student]
print(updated_marks)


numbers = [x for x in range(1,11)]
print(numbers)



numbers = [1, 2, 3, 4, 5]
result = [x * 5 for x in numbers]
print(result)



prices = [500, 1200, 800, 2500, 300]
result = [price for price in prices if price>1000]
print(result)
result = [price for price in prices if price<1000]
print(result)
result = [price for price in prices if price%2==0]
print(result)



words = ["Python", "Java", "JavaScript", "C", "HTML"]
string_length = [len(word) for word in words ]
print(string_length)
string_upper = [word.upper()  for word in words ]
print(string_upper)
string_length = [word for word in words  if len(word)>4]
print(string_length)
string_start = [word for word in words if word.startswith('J')]
print(string_start)




matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
result = [value for row in matrix for value in row]
print(result)
result = [value for row in matrix for value in row if value%2==0]
print(result)
result = [value for row in matrix for value in row if value>50]
print(result)
result = [value*2 for row in matrix for value in row ]
print(result)