count = 1
while True:
    print(count)
    if count==5:
        break
    count+=1
print('Loop ended')



for i in range(1,11):
    if i == 5:
        break
    print(i)



numbers = [10, 20, 35, 40, 50]
for num in numbers:
    if num==35:
        print('found')
        break 
    print(num)


# while True:
#     text = input("Enter something (type 'exit' to quit): ")
#     if text == "exit":
#         break

#     print("You entered:", text)
# print("Program Ended")




fruits = ["Apple", "Banana", "Mango", "Orange"]
search = "Mango"
for fruit in fruits:

    if fruit == search:
        print("Fruit Found")
        break



for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)




for i in range(1, 6):
    if i == 4:
        break
    print(i)



# secret = 7
# while True:
#     guess = int(input("Guess: "))
#     if guess == secret:
#         print("Correct!")
#         break





students = ["Rahul", "Aisha", "Saniya", "Rohan"]
for student in students:
    if student == "Saniya":
        print("Student Found")
        break
    print(student)





for i in range(0,11):
    print(i)
    if i == 10:
        break
    i +=1



hidden_number = 12
while True:
 number = int(input('enter a number : '))
 if hidden_number == number:
    print('correct!!')
    break
 



while True:
    password = input('enter the pasword : ')
    if password == 'python1234':
        print('login successfull!')
        break
    else:
        print('Incorrect password')




