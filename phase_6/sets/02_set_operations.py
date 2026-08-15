A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = A|B
print(result)

another_result = A.union(B)
print(another_result)


numbers = {1,2,3,4,5}
char = {'A','B','C','D'}
print(char|numbers)
print(numbers.union(char))



A = {1, 2}
B = {2, 3}
C = {3, 4}
result = A | B | C
print(result)

result = A.union(B,C)
print(result)



python_students = {"Aisha", "Saniya", "Rohan"}
java_students = {"Saniya", "Kiran", "Meera"}
all_students = python_students|java_students
print(all_students)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = A&B
print(result)

result = A.intersection(B)
print(result)


python_skills = {"Python", "SQL", "Git", "HTML"}
web_skills = {"HTML", "CSS", "JavaScript", "Git"}
commen_students = python_skills.intersection(web_skills)
print(commen_students)


commen_students = python_skills  & web_skills
print(commen_students)



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = A - B
print(result)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = B - A
print(result)


result = A.difference(B)
print(result)


python_students = {"Aisha", "Saniya", "Rohan", "Kiran"}
java_students = {"Saniya", "Kiran"}
only_python = python_students.difference(java_students)
print(only_python)



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = A ^ B
print(result)


result = A.symmetric_difference(B)
print(result)



A = {1, 2, 3}
B = {3, 4, 5}
A.update(B)
print(A)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.intersection_update(B)
print(A)



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.difference_update(B)
print(A)



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.symmetric_difference_update(B)
print(A)




A = {1, 2, 3}
B = {3, 4, 5}
C = {5, 6, 7}
result = A | B | C
print(result)



A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
C = {3, 4, 5, 6}
result = A & B & C
print(result)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 5, 6, 7}
result = (A | B) & C
print(result)



A = {1, 2, 3}
result = A.union([3, 4, 5])
print(result)

result = A.union((4, 5, 6))
print(result)




A = {1, 2, 3}
B = {3, 4, 5}
result = A & B
print(result)



A = {1, 2, 3}
B = {3, 4, 5}
result = A - B
print(result)


A = {1, 2, 3}
B = {3, 4, 5}
result = A ^ B
print(result)



