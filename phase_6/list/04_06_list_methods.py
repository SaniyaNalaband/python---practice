numbers = [10, 20, 30, 40]
print(len(numbers))


fruits = ["Apple", "Banana", "Mango"]
print('total no of fruits  : ', len(fruits))

numbers = []
print(len(numbers))


numbers = [10, 50, 30, 90, 20]
print(max(numbers))



fruits = ["Apple", "Banana", "Mango"]
print(max(fruits))



numbers = [10, 50, 30, 90, 20]
print(min(numbers))



temperatures = [32, 35, 29, 31, 36]
print("Lowest Temperature:", min(temperatures))


numbers = [10, 20, 30, 40]
print(sum(numbers))


marks = [80, 75, 90, 85]
marks1 = [80, 75, 90, 85]
total = marks1+marks
print(sum(total))



marks = [80, 75, 90, 85]
print(sum(marks))


marks = [80, 75, 90, 85]
average = sum(marks)/len(marks)
print(average)


values = [False, False, True, False]
print(any(values))


values = [False, False, False]
print(any(values))



values = [0, 0, 5, 0]
print(any(values))



login_status = [False, False, True, False]
if any(login_status):
    print('At least on sucessull login')





values = [True, True, True]
print(all(values))




values = [True, True, False]
print(all(values))


payments = [True, True, True, True]
if all(payments):
    print('All payements done!!!')




marks = [80, 75, 90, 85, 95]
print('Number of students : ',len(marks))
print('maximum marks : ', max(marks))
print('minimum marks : ',min(marks))
print('Total marks : ',sum(marks))
print('Average : ', sum(marks)/len(marks))