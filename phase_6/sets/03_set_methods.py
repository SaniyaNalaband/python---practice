skills = {'python','SQL'}
skills.add('Github')
print(skills)


numbers = {1,2,3,4}
numbers.add(5)
print(numbers)



languages = {'python','java'}
languages.add('python')
print(languages)



# skilss = {'python','java'}
# skills.add(['SQL','HTML','CSS'])  ----> adding tuple is wrong but updating tuple isn't
# print(skills)


skills = {'pyhton','java'}
skills.update(['SQL','HTML'])
print(skills)



skills = {'python'}
skills.update(["html","java"])
print(skills)




letters = {'A','B'}
letters.update('CD')
print(letters)



skills = {"Python", "SQL", "Git"}
skills.remove('SQL')
print(skills)



# skills = {"Python", "SQL"}
# skills.remove("Java")



skills = {"Python", "SQL", "Git"}
skills.discard("SQL")
print(skills)



skills = {"Python", "SQL"}
skills.discard("Java")
print(skills)



numbers = {10, 20, 30, 40}
remove = numbers.pop()
print('Removed : ',remove)
print('NUmbers : ',numbers)



skills = {"Python", "SQL", "Git"}
skills.clear()
print(skills)



skills = {"Python", "SQL", "Git"}
new = skills.copy()
print(new)
new.add('HTML')
print(new)
print(skills)




python_skills = {"Python", "SQL", "Git"}
web_skills = {"HTML", "CSS", "Git"}
all_skilss = python_skills.union(web_skills)
print(all_skilss)




python_students = {"A", "B", "C", "D"}
web_students = {"C", "D", "E", "F"}
all_students = python_students.intersection(web_students)
print(all_students)



a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = a.intersection(b,c)
print(d)




python_skills = {"Python", "SQL", "Git"}
web_skills = {"HTML", "CSS", "Git"}
result = python_skills.difference(web_skills)
print(result)



a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))
print(b.difference(a))



a = {1, 2, 3}
b = {3, 4, 5}
result = a.symmetric_difference(b)
print(result)


python_skills = {"Python", "SQL"}
all_skills = {"Python", "SQL", "Git", "HTML"}
print(python_skills.issubset(all_skilss))


skills = {"Python", "Java"}
programming = {"Python", "SQL", "Git"}
print(skills.issubset(programming))



all_skills = {"Python", "SQL", "Git", "HTML"}
python_skills = {"Python", "SQL"}
print(all_skills.issuperset(python_skills))




a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))



a = {1, 2, 3}
b = {3, 4, 5}
print(a.isdisjoint(b))


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.intersection_update(b)
print(a)




a = {1, 2, 3, 4}
b = {3, 4, 5}
a.difference_update(b)
print(a)




a = {1, 2, 3}
b = {3, 4, 5}
a.symmetric_difference_update(b)
print(a)




fruits = {"Apple", "Banana"}
fruits.add("Mango")
print(fruits) # ---> modifies original set


fruits = {"Apple", "Banana", "Mango"}
fruits.remove("Banana")
print(fruits)   # ---> modifies original set




numbers = {10, 20, 30}
numbers.discard(40)
print(numbers)



skills = {"Python"}
skills.update(["SQL", "Git", "HTML"])
print(skills)




student1 = {
    "Python",
    "SQL",
    "HTML"
}

student2 = {"SQL","HTML","CSS"}
common = student1.intersection(student2)
print(common)



student1 = {"Python","SQL","Git"}
student2 = {"SQL","HTML","CSS"}
unique = student1.difference(student2)
print(unique)



basic = { "Python","SQL"}
all_skills = {"Python","SQL","Git","HTML"}
print(basic.issubset(all_skills))




python_students = {
    "Asha",
    "Priya",
    "Neha",
    "Ananya"
}

sql_students = {
    "Priya",
    "Ananya",
    "Kavya",
    "Meera"
}

print("Both Python and SQL:")
print(python_students.intersection(sql_students))

print("Python only:")
print(python_students.difference(sql_students))

print("SQL only:")
print(sql_students.difference(python_students))

print("Either Python or SQL:")
print(python_students.union(sql_students))

print("Only one skill:")
print(python_students.symmetric_difference(sql_students))







skills = {
    "Python",
    "SQL"
}
skills.add("Git")
skills.update(["HTML", "CSS"])
skills.discard("Java")
print(skills)



morning_students = {
    "A",
    "B",
    "C",
    "D"
}
evening_students = {
    "C",
    "D",
    "E",
    "F"
}
print(' Students in both groups.')
both = morning_students.intersection(evening_students)
print(both)

print(' Students only in the morning group.')
only_morning = morning_students.difference(evening_students)
print(only_morning)


print(' Students only in the evening group.')
only_evening = evening_students.difference(morning_students)
print(only_evening)

print(' All students.')
all = morning_students.union(evening_students)
print(all)


print('Students belonging to only one group.')
only_onegroup = morning_students.difference(evening_students)
print(only_onegroup)


print(' Check whether the morning group is a subset of all students.')
subset = morning_students.issubset(evening_students.union(morning_students))
print(subset)


print('Check whether all students are a superset of the morning group.')
superset = morning_students.union(evening_students)
all = superset.issuperset(morning_students)
print(all)



print('Check whether the two groups are disjoint.')
disjoint = morning_students.isdisjoint(evening_students)
print(disjoint)




skills = {
    "Python",
    "SQL"
}

print("Current skills:", skills)
skills.add("Git")
skills.update(["HTML", "CSS"])
print("Updated skills:", skills)
skills.discard("Java")
print("Final skills:", skills)




set_example = {'Python','SQL','Git'}
set_example.add('HTML')
print(set_example)


numbers = {1,2,3,4,5}
numbers.remove(4)
print(numbers)

numbers.discard(10)
print(numbers)


set1 = {1,2,3}
set2 = {3,4,5,6}
all = set1.union(set2)
print(all)


intersection = set1.intersection(set2)
print(intersection)

difference = set1.difference(set2)
print(difference)

difference = set2.difference(set1)
print(difference)

symmetric = set1.symmetric_difference(set2)
print(symmetric)

sub = set1.issubset(set2)
print(sub)

