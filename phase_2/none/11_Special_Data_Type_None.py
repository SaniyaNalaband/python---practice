x = None
print(type(x))


x = None
print(x == None)
print(x is None)


if x is None:
    print('No Value!!!')



print(None == 0 )


def greet():
    print('hello')

result = greet()
print(result)


def find_username(name):
    if name == 'Saniya':
     return 'found'
    return None
print(find_username('Siya'))


def devide(a,b):
   if b==0:
      return None
   return a/b

result = devide(10,0)
if result is None:
   print('canot be devided by zero')
else:
   print(result)


age = None
if age is None:
   age=18
print(age)