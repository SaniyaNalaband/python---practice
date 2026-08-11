numbers = (10, 20, 10, 30, 10, 40)
result = numbers.count(10)
print(result)
print(numbers.count(20))




languages = (  "Python","Java","Python","C", "Python")
print(languages.count("Python"))


items = (  "Pen", "Book","Pen","Pencil","Pen","Book")
print('Pen :',items.count('Pen'))
print('Book : ',items.count('Book'))
print('Pencil : ',items.count('Pencil'))



numbers = (10, 20, 30, 40)
print(numbers.index(20))




languages = ("Python", "Java", "C", "JavaScript")
print(languages.index("C"))



numbers = (10, 20, 10, 30, 10)
print(numbers.index(10, 1))


numbers = (10, 20, 10, 30, 10)
print(numbers.index(10, 1, 4))



numbers = (10, 20, 10, 30, 10)
value = 10
print("Count:", numbers.count(value))
print("First position:", numbers.index(value))





marks = (85, 90, 78, 90, 92)
print("Number of students with 90:", marks.count(90))
print("First student with 90 is at index:", marks.index(90))




attendance = ( "Present","Absent","Present","Present","Absent")
print("Present:", attendance.count("Present"))
print("Absent:", attendance.count("Absent"))




results = ( "Pass","Fail",  "Pass","Pass","Fail")
passed = results.count("Pass")
failed = results.count("Fail")
print("Passed:", passed)
print("Failed:", failed)


