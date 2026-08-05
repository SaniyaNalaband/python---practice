for i in range(1,6):
    print(i)
else:
    print('Loop finished')


count = 1 
while count<=5:
    print(count)
    count+=1
else:
    print('Done')



count = 0
while count <=10:
    if count == 5:
        break
    count+=1
    print(count)
else:
    print('seccessfully prited')




fruits = ["Apple", "Banana", "Orange"]
search = "Mango"
for fruit in fruits:
    if fruit == search:
        print("Fruit Found")
        break
else:
    print("Fruit Not Found")




numbers = [10, 20, 30, 40]
search = 30
for num in numbers :
    if num == search:
        print('Found')
        break
else:
    print('Not found')




correct_password = "python123"
attempts = ["abc", "123", "python123"]
for password in attempts:
    if password == correct_password:
        print("Login Successful")
        break
else:
    print("All Attempts Failed")


secret = 5
guesses = [2, 7, 8]
for guess in guesses:
    if guess == secret:
        print("Correct Guess")
        break
else:
    print("No Correct Guess")




count = 1
while count <= 5:
    print(count)
    count += 1
else:
    print("While Loop Finished")





correct_password = 'python1234'
attempts = 3
while attempts>0:
    password = input('enter the password : ')
    if password == correct_password:
        print('Login successfull')
        break
    attempts -=1
else:
    print('Account blocked')



secret = 8 
attempts  = 1
while attempts>0:
    guess = int(input('Guess the number : '))
    if guess == secret:
        print('you win')
        break
    attempts-=1
else:
    print('Game over!!')