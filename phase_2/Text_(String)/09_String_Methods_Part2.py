filename = "report.pdf"

print("Starts with rep :", filename.startswith("rep"))
print("Ends with pdf   :", filename.endswith(".pdf"))
print("Count of p      :", filename.count("p"))
print("Find 'o'        :", filename.find("o"))
print("Last 'p'        :", filename.rfind("p"))



# FIND METHOD

text = 'python programming'
print(text.find('python'))
print(text.find('programming'))
print(text.find('gram'))


print('programmin'.find('m'))

# RFIND METHOD 

text = 'banana'
print(text.rfind('n'))
print(text.rfind('a'))

text = "Python Programming Python"
print(text.rfind('a'))
print(text.rfind('g'))
print(text.rfind('n'))


print('banana'.rfind('a'))

print('banana'.rfind('n'))

print('banana'.rfind('na'))

print('banana'.rfind('x'))

print('python programming python'.rfind('python'))

print('mississippi'.rfind('s'))


# INDEX() METHOD 

print('python programming'.index('python'))
print('python programming'.index('programming'))
print('python programming'.index('o'))
# print('python programming'.index('java'))  # ---> throws an error


print('programming'.index('g'))


# RINDEX() METHOD 

print('banana'.rindex('a'))
print('creativity'.rindex('y'))
print('creaticity'.rindex('ty'))
print('creativity'.rindex('i'))


# COUNT() METHOD 

print('practice'.count('i'))
print('practice'.count('c'))
print('good feature'.count('o'))
print('googd deeds'.count('e'))
print('engineering'.count('e'))
print('mississippi'.count('s'))

# STARTSWITH() METHOD 

print("hello i'm learning python".startswith('hello'))
print("hello i'm learning python".startswith('hi'))

print('pythondeveloper@gmail.com'.startswith('p'))
print('http://exampleurl//.com'.startswith('http'))


# ENDSWITH() METHOD

print('python programming'.endswith('programming'))
print('This is a python practice repo'.endswith('repo'))
print('im writing it to practice python'.endswith('html'))
print('pythpn and html is my favourite languages'.endswith('subject'))
print('the file ends with report.pdf'.endswith('.pdf'))


# MIXED CHALLENGES 

print('banana'.find('na'))
print()

print("banana".find("a", 2))  # ---> starts finding after index 2