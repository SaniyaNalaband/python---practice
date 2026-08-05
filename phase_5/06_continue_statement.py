for i in range(1,6):
    if i == 3:
        continue
    print(i)



for i in range(1,11):
 if i%2==0:
    continue
 print(i)


 word = 'Education'
 for ch in word:
    if ch.lower() in 'aeiou':
       continue
    print(ch)



count = 0 
while count<5:
   count+=1
   if count == 3:
      continue
   print(count)



fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits:
   if fruit == 'Banana':
      continue
   print(fruit)



for i in range(1,4):
   for j in range(1,4):
      if j == 2:
         continue
      print(i,j)




for i in range(1,6):
   if i == 3:
      continue
   print(i)



marks = [95, -1, 88, 76, -1, 91]
for mark in marks:
   if mark == -1:
      continue
   print(mark)


for i in range(1,50):
   if i%5==0:
      continue
   print(i)



text = 'PYTHON PROGRAMMING'
for ch in text:
   if ch in 'AEIOU':
      continue
   print(ch)