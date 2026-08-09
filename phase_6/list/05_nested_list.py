numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(numbers[0])
print(numbers[1])
print(numbers[2])


print(numbers[0][0])
print(numbers[2][2])

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


numbers[2][2] = 100
print(numbers)



numbers[0].append(35)
print(numbers)



numbers.append([150,200])
print(numbers)


numbers[0].remove(35)
print(numbers)




numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in numbers:
    for value in row:
        print(value, end=" ")
    print()



marks = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]
for student in marks:
    for mark in student:
        if mark>=90:
            print(mark)






marks = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80]
]
for studet in marks:
    print(sum(studet))

for studetn in marks:
    print(max(studetn))



numbers = [
    [1, 2],
    [3, 4, 5],
    [6]
]
for number in numbers:
    print(len(number))




numbers = [
    [1, 2],
    [3, 4, 5],
    [6]
]
for row in numbers:
    for value in row:
        print(value)





numbers = [
    [10, 20, 30],
    [40, 50, 60]
]
total = 0
for row in numbers:
    for value in row:
        total+=value
print(total)





numbers = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]
count = 0

for row in numbers:
    for value in row:
        if value%2==0:
            count+=1
print(count)




numbers = [
    [15, 20, 35],
    [40, 12, 60],
    [25, 80, 10]
]
largest = numbers[0][0]
for row in numbers:
    for value in row:
        if value>largest:
            largest = value

print('Largest : ',largest)




count = 0
for row in numbers:
    for value in row:
        if value>50:
            count += 1
print(count)




students = [ ['Riya', 99],['Sana',98],['Siya',89]]
for row in students:
    print(row[0])


for row in students:
    print(row[0],':',row[1])


students = [
    ["Aisha", 80, 85, 90],
    ["Saniya", 90, 95, 88],
    ["Rohan", 75, 82, 79]
]
for row in students:
    print(row[0])



for row in students:
    print(row[0],':',row[1:])


for row in students:
    print(row[0],':', sum(row[1:]))



for row in students:
    average = sum(row[1:])/len(row[1:])
    print(f'average of {row[0]}',':', average )
  
   

highest_average = 0
highest_student = ""
for row in students:
    average = sum(row[1:]) / len(row[1:])
    print(f"Average of {row[0]} : {average}")
    if average > highest_average:
        highest_average = average
        highest_student = row[0]
print("Highest Average:", highest_student, "=", highest_average)


 