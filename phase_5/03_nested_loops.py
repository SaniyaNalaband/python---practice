for i in range(1,4):
    for j in range(1,4):
        print(i,j)



for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)




for i in range(3):
    for j in range(3):
        print(i, j)





i = 3
while i<=3:
    j=1
    while j<=3:
        
        print(i,j)
        j+=1
    i +=1



i = 1
while i <= 3:
    for j in range(1, 4):
        print(i, j)
    i += 1


for i in range(1,6):
    for j in range(1,11):
        print(f'{i}X{j}={i*j}')



for i in range(5):
    for j in range(5):
        print('*',end=" ")
    print()


for i in range(1,6):
    for j in range(i):
        print('*',end="")
    print()



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()



for row in range(1, 4):
    for seat in range(1, 6):
        print(f"Row {row} Seat {seat}")



for row in range(1,9):
    for colomn in range(1,9):
        print(f'{row}{colomn}',end="")
    print()




students = ["Rahul", "Aisha"]
subjects = ["Math", "Science", "English"]
for student in students:
    for subject in subjects:
        print(student, "-", subject)





for table in range(1, 4):
    print(f"\nTable of {table}")

    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")



for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3}", end=" ")
    print()




for i in range(3):
    for j in range(5):
        print('*',end=" ")
    print()



for i in range(1,5):
    print('\ntable of ',i)
    for j in range(1,11):
        print(f'{i}X{j}={i*j}')



for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()




for i in range(5,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()



for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()