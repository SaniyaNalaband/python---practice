def student_info(**kwargs):
    print(kwargs)
student_info(name='Sana',age=21)



def student(name ,age):
    print(name)
    print(age)
student(name='Anie',age=21)



def student_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
student_info(age=21,city='Bengluru')



def student(**kwargs):
    print(kwargs['name'])
    print(kwargs['city'])
student(name='Sinu',city='Pune')





def display(**kwargs):
    for key in kwargs:
        print(key)
display(colour='Red',city='Bengluru')




def dipaly(**values):
    for key,value in values.items():
        print(key,':',value)
    print(values.keys())
    print(values.values())
dipaly(name='Jhon',age=22,place='Singapore')



def dipaly(**values):
    if "city" in values:
        print('City is available')
    print('City is not available ')
dipaly(name='Jhon',age=22,place='Singapore')






def student_info(**kwargs):
    kwargs['status'] = 'active'
    print(kwargs)
    removed = kwargs.pop('age')
    print('Removed :',removed)
    print(kwargs)
student_info(name='Jhon',age=22,place='Singapore')














