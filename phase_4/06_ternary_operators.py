age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)


number = 12
ans = 'even' if number%2==0 else 'odd'
print(ans)


number = -0 
result = 'positive' if number>0 else "negaive"
print(result)


a = 10 
b = 15 
output = 'greater' if b>a else 'smaller'
print(output)


marks = 85
result = 'pass' if marks>=35 else "fail"
print(result)

number = 10 
reality_check = 'equal' if number == 10 else 'not equal'
print(reality_check)


age = 25
citizen = True
status = 'eligible' if age>=18 and citizen else 'not eligible'
print(status)

fruit = 'Apple'
message = "Available" if fruit in ["Apple", "Banana"] else "Not Available"
print(message)

value = None
result = "Empty" if value is None else "Not Empty"
print(result)

age = 21
print("Adult" if age >= 18 else "Minor")