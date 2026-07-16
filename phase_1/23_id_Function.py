x = 10
print(id(x))

x =10
x =10
print(id(x))


# after changing the value of x


x =15
print(id(x))


price = 99.3
print(id(price))

print(id(x))


# diifferent variable with same object ---> returns same id 

name1 = 'python' 
name2 = 'python'
print(id(name1))
print(id(name2))


# Mutable object  ---> returns different id

lis1 = [1,2,3]
list2 = [1,2,3]
print(id(lis1))
print(id(list2))


# assigning one variable to another ---> returns same id 

x = [1,2,3]
z = x
print(id(x))
print(id(z))
