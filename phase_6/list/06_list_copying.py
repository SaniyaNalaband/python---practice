original = [10, 20, 30]
copy_list = original
print(original)
print(copy_list)
print(id(original))
print(id(copy_list))
copy_list.append(40)
print(original)
print(copy_list)





original = [10, 20, 30]
copy_list = original.copy()
print(original)
print(copy_list)
print(id(original))
print(id(copy_list))
copy_list.append(40)
print(copy_list)
print(original)


original = [10, 20, 30]
copy_list = original[:]
print(original)
print(copy_list)
print(id(original))
print(id(copy_list))



original = [
    [10, 20],
    [30, 40]
]
copy_list = original.copy()
print(copy_list)
copy_list[0][0] = 100
print(copy_list)
print(original)
copy_list[0] = [50,60]
print(copy_list)
print(original)





import copy

original = [
    [10, 20],
    [30, 40]
]
copy_list = copy.deepcopy(original)
copy_list[0].append(50)
print("Original:", original)
print("Copy:", copy_list)




numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(numbers is new_numbers)




numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(numbers == new_numbers)
print(numbers is new_numbers)


numbers = [
    [10, 20],
    [30, 40]
]
new_numbers = numbers.copy()
new_numbers[0].append(50)
print(numbers)
print(new_numbers)




numbers = [
    [10, 20],
    [30, 40]
]
new_numbers = copy.deepcopy(numbers)
new_numbers[0].append(50)
print(numbers)
print(new_numbers)



