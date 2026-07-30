marks = int(input('enter the marks : '))
if marks >= 90:
    print('A grade')
elif marks>=75:
    print('B grade')
elif marks>=50:
    print('C grade')
else:
    print('Fail')



number = int(input('enter the number : '))
if number<0:
    print('negative')
elif number>0:
    print('positive')
else:
    print('zero')



signal = 'Red'
if signal=='Green':
    print('Go')
elif signal=='Yellow':
    print('Ready')
elif signal=='Red':
    print('Stop')
else:
    print('Invalid signal')



weather = 'Rainy'
if weather == 'Sunny':
    print('Wear sunglases')
elif weather == 'Rainy':
    print('Carry umbrella')
elif weather == 'Cold':
    print('wear jacket')
else:
    print('Check weather forecast')



age = 95 
if age>1 and age<11:
    print('Child')
elif age>12 and age<20:
    print('teen age')
elif age>20 and age<60:
    print('Adult')
else:
    print("Senior citizen")



language = 'Python'
if language in ['Python','java']:
    print('programming language')
elif language in ['HTML','CSS']:
    print('Web Technology')
else:
    print('Unknown')



balance = 3000
amount = 1500
if amount <= 0:
    print('Invalid amount')
elif amount>balance:
    print('Insufficient balance')
else:
    print("Withdraw successfull")



role = 'Admin'
if role == 'Admin':
    print('All access')
elif role == 'Teacher':
    print('Teaching access')
elif role == 'Student':
    print('Learning access' )
else:
    print('Guest access')


age = 2
if age<5:
    print('Free entry')
elif age>5 and age < 18:
    print('Childe ticket')
elif age>18 and age<60:
    print('Adult Ticket')
else:
    print('Senior citize ticket')


username = 'admin'
password = 'python123'
if username != 'admin':
    print('invalid username')
elif password != 'python123':
    print('incorect password')
else:
    print('Login successfull')



language = "Python"
if language == "Java":
    print("Java Selected")
elif language == "Python":
    print("Python Selected")
else:
    print("Other Language")




bill = 2500
if bill >= 5000:
    print("30% Discount")
elif bill >= 2000:
    print("10% Discount")
else:
    print("No Discount")



bmi = 27
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")



x = 15
if x > 20:
    print("A")
elif x > 10:
    print("B")
else:
    print("C")



text = ""
if text == "":
    print('empty')
elif len(text)<5:
    print('Short')
else:
    print('Long')



items = []
if len(items) == 0:
    print("No Items")
elif len(items) < 5:
    print("Few Items")
else:
    print("Many Items")



password = "admin123"
if password == "python":
    print("Python User")
elif password == "admin123":
    print("Administrator")
else:
    print("Unknown User")



num1 = int(input('enter the number1 : '))
num2 = int(input('enter th number2 :'))
num3 = int(input('enter th number3 :'))
if num1>num2 and num1>num3:
    print('num1 is greater')
elif num2>num3 :
    print('num2 is greater')
else:
    print('num3 is greater')





num1 = int(input('enter the number1 : '))
num2 = int(input('enter th number2 :'))
num3 = int(input('enter th number3 :'))
num4 = int(input('enter th number4 :'))
if num1>num4 and num1>num2 and num1>num3:
    print('num1 is greater')
elif num2>num3 and num2>num4 :
    print('num2 is greater')
elif num3>num4 :
    print('num3 is greater')
else:
    print('num4 is greater')


