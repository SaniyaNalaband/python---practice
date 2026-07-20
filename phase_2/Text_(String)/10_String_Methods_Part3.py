
# REPLACE METHOD

print('java is good'.replace('java','python'))
print('banana'.replace('a','@'))
print('hello world python'.replace(' ','_'))
print('the year is 2026'.replace('2026','2027'))
print('good morning '.replace('good','great'))

print('banana'.replace('nana','nanana',1))
print('apple apple apple'.replace('apple','orange',1))
print('3.14.15'.replace('.',','))

# SPLIT METHOD 

text = "apple apple apple"
print(text.replace("apple", "orange"))

text = 'python java html'
print(text.split())


text = 'python java html'
print(text.split(','))


text = "one two three four"
print(text.split(" ", 2))

print('a-b-c-d'.rsplit('-',2))
print('python java sql'.rsplit(' ',1))
print('1|2|3|4'.rsplit('|',2))
print('2026-07-19'.rsplit('-',2))
print('x:y:z'.rsplit(':',1))
print('a-b-c-d'.rsplit(',',3))
print('abc'.split('b'))



# SPLITLINES() METHOD
text="""Hello
World"""
print(text.splitlines())


text = "Python\nJava\nC++"
print(text.splitlines())

print("Python".splitlines())


# PARTITION METHOD

print("Python-Programming".partition("-"))
print("name:age".partition(":"))
print("abc".partition("b"))
print("hello world".partition(" "))
print("apple,banana".partition(","))
print('goa mumbai delhi'.partition('goa'))
print("user@gmail.com".partition(".com"))
print("Python".partition("z"))


# R PARTITION

print("Python-Programming".rpartition("-"))

path = "folder/subfolder/file.txt"
print(path.rpartition("/"))

print("A:B:C".rpartition(":"))
print("apple,banana,mango".rpartition(","))
print("Python".rpartition("z"))

# JOIN

words = ["Python", "is", "fun"]
print(" ".join(words))

print("-".join(["A","B","C"]))
print("".join(["P","y","t","h","o","n"]))