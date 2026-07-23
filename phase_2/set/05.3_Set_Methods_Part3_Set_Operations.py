''' 1. `union()`
Returns a **new set** containing all unique elements from both sets.'''

a = {1,2,3,4}
b = {4,5,6,7}
print(a.union(b))

a = {1,2,3,4}
b = {4,5,6,7}
print(a|b)


language = {'java','python','html','css'}
language1 = {'sql'}
print(language.union(language1))

a = {'a','b','c'}
b = {'d','e','f'}
c = {'g','h','i'}
print(a.union(b,c))


'''2. `intersection()`
Returns elements common to both sets.'''

a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))

city = {'landon','paris','tokyo','italy'}
city2 = {'new york','tokyo','italy','istambul'}
print(city.intersection(city2))


fruits1 = {"Apple", "Banana", "Mango"}
fruits2 = {"Banana", "Orange", "Mango"}
result = fruits1.intersection(fruits2)
print(result)

a = {100, 200, 300}
b = {200, 300, 400}
print( a & b)


'''3. `difference()`
Returns elements present in the first set but not in the second.'''

a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))



set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.difference(set2)
print(result)

a = {1, 2, 3}
b = {4, 5, 6}
print(a.difference(b))


a = {100, 200, 300}
b = {200}
result = a - b
print(result)

a = {1, 2, 3, 4, 5}
b = {2, 3}
c = {5}
result = a.difference(b, c)
print(result)


'''4. `symmetric_difference()`
Returns elements that are in **either set**, but **not in both**.'''

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))


set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
result = set1.symmetric_difference(set2)
print(result)


a = {100, 200, 300}
b = {200, 300, 400}
print( a ^ b)


a = {True, False}
b = {False}
result = a.symmetric_difference(b)
print(result)


