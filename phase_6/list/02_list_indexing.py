lists = [1,2,3,'python','orange',True]
print(lists[-1])
print(lists[0:6])



numbers = [1,2,3,4,5,6]
index = 3
print(numbers[index])



fruits = ['apple','banana','grapes']
fruits[1] = 'mango'
print(fruits)



numbers = [1,2,3,4,5,5]
numbers[-1] = 100
print(numbers)


matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])
print(matrix[1][0])
print(matrix[1][1])
print(matrix[1][2])
print(matrix[2][0])
print(matrix[2][1])
print(matrix[2][2])

for row in matrix:
    for value in row:
        print(value)




colors = ['red','green','yellow']
last_item = colors[len(colors)-1]
print(last_item)



city = ['hubli','bengluru','dharwad']
middle_item = city[len(city)-2]
print(middle_item)


animals = ["Dog", "Cat", "Lion"]
print(animals[0])
print(animals[-1])




students = ["Rahul", "Aisha", "Saniya"]
students[0] = 'Sana'
print(students)


cities = ['hubli','dharwad','bengluru','mysore','belgum']
print(cities[0])


numbers = [1,2,3,4,5]
print(numbers[-1])

numbers[-3] = 33
print(numbers)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[2][1])



items = ['mouse','keyboar','cpu']
print(items[0])
print(items[-1])


numbers = [10, 20, 30, 40, 50, 60, 70]
print('First :',numbers[0])
print('middle:', numbers[len(numbers)//2])
print('end : ',numbers[-1])


employees = [
    [101, "Aman", 50000],
    [102, "Priya", 65000],
    [103, "Saniya", 70000]
]
print("Employee Name:", employees[1][1])
print("Salary:", employees[1][2])



numbers = [10,20,30,40]
numbers[0],numbers[1] = numbers[1],numbers[0]
print(numbers)




cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad"]
for i in range(len(cities)):
    print(i,cities[i])


numbers = [45, 23, 78, 11, 99, 67]
largest = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
print("Largest =", largest)



numbers = [10, 20, 20, 30, 40]
for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        print("Duplicate Found:", numbers[i])






languages = ["Python", "Java", "C", "Go"]
for i in range(len(languages)-1, -1, -1):
    print(languages[i])



