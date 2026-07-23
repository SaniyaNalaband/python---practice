numbers = frozenset([10, 20, 30])
print(numbers)
print(type(numbers))


languages = {"Python", "Java", "SQL"}
frozen_languages = frozenset(languages)
print(frozen_languages)

numbers = frozenset([10, 20, 20, 30])
print(numbers)


colors = frozenset(["Red", "Green", "Blue"])
print(colors)



a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


a = frozenset([1, 2])
b = {a}
print(b)


