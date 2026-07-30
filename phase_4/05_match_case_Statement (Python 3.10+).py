day = 1 

match day:
    case 1:
        print('Monday')
    case 2 :
        print('Tuesday')
    case 3 :
        print('Wednesday')
    case _:
        print('Invalid day')




month = 4 
match month:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case 4:
        print('April')
    case 5:
        print('May')
    case _:
        print('Invalid month')






grade = "A"
match grade:

    case "A":
        print("Excellent")

    case "B":
        print("Very Good")

    case "C":
        print("Good")

    case "D":
        print("Pass")

    case _:
        print("Fail")








operator = "+"
match operator:

    case "+":
        print(20 + 10)

    case "-":
        print(20 - 10)

    case "*":
        print(20 * 10)

    case "/":
        print(20 / 10)

    case _:
        print("Invalid Operator")





choice = 2
match choice:

    case 1:
        print("Add Student")

    case 2:
        print("Delete Student")

    case 3:
        print("Update Student")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")






match day:

    case "Saturday" | "Sunday":
        print("Weekend")

    case _:
        print("Weekday")






status = True
match status:

    case True:
        print("Login Successful")

    case False:
        print("Login Failed")





language = "Python"
match language:

    case "Python":
        print("Programming Language")

    case "HTML":
        print("Markup Language")

    case _:
        print("Unknown")




Fruits = ' Orange'
match Fruits:
    case 'Apple':
        print('Apple')
    case 'Banana':
            print(' Banana')
    case " Orange":
            print(' Orange')
    case _:
            print(' invalid Fruit')







choice = 3
match choice:

    case 1:
        print("Balance")

    case 2:
        print("Deposit")

    case 3:
        print("Withdraw")

    case 4:
        print("Exit")

    case _:
        print("Invalid Option")





food = "Pizza"
match food:

    case "Pizza":
        print("₹250")

    case "Burger":
        print("₹120")

    case "Pasta":
        print("₹180")

    case _:
        print("Item Not Available")





signal = "Green"
match signal:

    case "Green":
        print("Go")

    case "Yellow":
        print("Slow Down")

    case "Red":
        print("Stop")

    case _:
        print("Invalid Signal")







