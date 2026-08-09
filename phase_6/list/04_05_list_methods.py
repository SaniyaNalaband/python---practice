original = [10, 20, 30] 
copy_list = original
print(copy_list)
print(original) 

copy_list.append(40)
print(original)
print(copy_list)



print(id(original))
print(id(copy_list))


real = [10,20,30]
copying_list = real.copy()
print(copying_list)
print(real)

print(id(real))
print(id(copying_list))


copying_list.append(40)
print(copying_list)
print(real)



real = [10,20,30,40]
copy = real[:]
print(copy)
print(real)

print(id(real))
print(id(copy))

copy.append(50)
print(copy)
print(real)



original = [10,20,30]
copy = original.copy()
copy[0] = 100
print(copy)
print(original)



original = [[10,20],[30,40]]
copy = original.copy()
print(copy)
print(original)
copy[0].append(100)
print(copy)
print(original)



import copy
original_list = [[10,20],[30,40]]
copy_list = copy.deepcopy(original_list)
print(copy_list)
print(original_list)



copy_list.append(50)
print(copy_list)
print(original_list)



another_list = ['A','B','C']
copy_another = copy.deepcopy(another_list)
print(copy_another)

copy_another.append('D')
print(copy_another)


