def numbers(*args):
    print(args)
numbers(10,20,30,40)




def add_numbers(*args):
    return sum(args)
print(add_numbers(10,20,30,40))




def all_numbers(*args):
    for number in args:
        print(number)
all_numbers(10,20,30,40,50)



def tuplee(*args):
    print(args)
tuplee('python')





def calculate_sum(*args):
    total = 0 
    for number in args:
        total += number
    print(total)
calculate_sum(10,20,30)





def calculate_sum(*args):
    return sum(args)
print(calculate_sum(10,20,30,40))



def highest_max(*args):
    return max(args)
print(highest_max(10,20,50,60))



def min_number(*args):
    return min(args)
print(min_number(10,20,5,1))






def avg_numbers(*args):
    return sum(args)/len(args)
print(avg_numbers(10,20,30,40,50))





def dispaly(*args):
    print(args[0])
    print(args[1])
    print(args[2])
dispaly(10,20,30)




def display(*args):
    print(args[1:3])
display('css','python','sql','git','html')







def student_info(name,*subjects):
    print('Name : ',name)
    for subject in subjects:
        print('Subject : ',subject)
student_info('Anie','python','java','html')




def total_marks(name,*marks):
    total = sum(marks)
    print('Name : ', name)
    print('Total :',total)
total_marks('Riya',98,99,89)





def count_values(*args):
     print('Number of argumnets : ',len(args))
count_values(10,'Japan',True)




def process(*args):
    if len(args) == 0:
        print('No arguments  provided')
    else:
        print('Provided argumnets  : ',len(args))
process()
process(20,10)


def display(*args):
    print(args)
numbers = [1,2,3,4,5]
display(numbers)
display(*numbers)



def show(*numbers):
    print(numbers)
show([1,2,3,4,5])






def multiply(*numbers):
    result = 1 
    for number in numbers:
        result *= number 
    return result
print(multiply(2,3,4,5))





def separate_numbers(*numbers):
    for number in numbers:
        if number % 2 == 0:
            print('Even number : ',number)
        else:
            print('Odd number : ',number)
separate_numbers(10,20,2,3,4,5,6)






def searching_value(target,*numbers):
    if target in numbers:
        print(target,'found')
    else:
        print(target,'Not found')
searching_value(5,10,60,35,15,4,5,6)
searching_value(10,20,5,29,45,60)






def count_greater(limit,*numbers):
    count = 0 
    for number in numbers:
        if number > limit :
            count += 1
    print('Count :', count)
count_greater(50,20,10,35,40)
count_greater(20,50,30,80)





def student_info(name,*marks):
    print('Name : ',name)
    print('Marks : ',marks)
    print('Number of subjects : ', len(marks))
    print('Total marks : ', sum(marks))
    print('Average : ', sum(marks)/len(marks))
    print('Highest marks :', max(marks))
    print('Lowest marks :', min(marks))
    for mark in marks:
        if mark >= 80:
            print(mark)
        else:
            pass
    average = sum(marks)/len(marks)
    if average >= 80:
        print('Excellent!!')
    elif average >=60 and average <=79 :
        print('Good')
    else:
        print('Need impovement')

    

student_info('Anie',99,85,79,89,88)








def calculate_expence(*expenses):
    print('All expenses : ', expenses)
    print('Number of expenses : ', len(expenses))
    print('Total expenses : ', sum(expenses))
    print('Average expense : ', sum(expenses)/len(expenses))
    print('Highest expense :',max(expenses))
    print('Lowest expense : ', min(expenses))
    total = sum(expenses)
    for expense in expenses:
        if expense >=1000:
            print(expense)
    
    if total >= 4000:
         print('High spending')
    else:
        print('Spending is under control')
calculate_expence(1000,500,700,2000)
















































































































































































































































































































































































