numbers = frozenset([1,2,3,4,5])
print(numbers)


numbers = frozenset((1,2,3,4))
print(numbers)


letters = frozenset('python')
print(letters)


numbers = frozenset([1,1,2,2,3,3,4,4])
print(numbers)


a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.union(b))



a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
result = a.union(b)
print(result)



a = frozenset({1, 2, 3})
b = frozenset({2, 3, 4})
result = a.intersection(b)
print(result)



a = frozenset({1, 2, 3})
b = frozenset({2, 3, 4})
result = a.difference(b)
print(result)


set1 = (a,b)
print(set1)




admin = frozenset({
    "read",
    "write",
    "delete"
})

editor = frozenset({
    "read",
    "write"
})

viewer = frozenset({
    "read"
})

print("Admin:", admin)
print("Editor:", editor)
print("Viewer:", viewer)

print("Viewer permissions are included in Editor:",viewer.issubset(editor))
print( "Editor permissions are included in Admin:", editor.issubset(admin))

print( "Admin contains all Editor permissions:",admin.issuperset(editor))