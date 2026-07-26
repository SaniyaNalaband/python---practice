''' 1️⃣ Bitwise AND (`&`)
Returns `1` only if **both bits are 1**.'''



print(5 & 3)

read = 4      # 100
write = 6     # 110
print(read & write)



lights = 13      # 1101
fan = 11         # 1011
print(lights & fan)

class1 = 14      # 1110
class2 = 10      # 1010
print(class1 & class2)



'''2️⃣ Bitwise OR (`|`)
Returns `1` if **either bit is 1**.'''


read = 4      # 100
write = 2     # 010
print(read | write)


lights = 8     # 1000
fan = 4        # 0100
print(lights | fan)

employee = 5      # 0101
manager = 2       # 0010
print(employee | manager)


'''3️⃣ Bitwise XOR (`^`)
Returns `1` when the bits are **different**.'''


print(5 ^ 3)

read = 5      # 0101
write = 3     # 0011
print(read ^ write)

lights = 12      # 1100
fan = 10         # 1010
print(lights ^ fan)


class1 = 14      # 1110
class2 = 10      # 1010
print(class1 ^ class2)


user = 15      # 1111
required = 7   # 0111
print(user ^ required)


''' 4️⃣ Bitwise NOT (`~`)
Flips every bit.'''


print(~5)


permission = 10
print(~permission)


ip_mask = 7
print(~ip_mask)


flag = 20
print(~flag)


'''5️⃣ Left Shift (`<<`)
Moves bits to the left.
Each left shift multiplies the number by **2**.'''


print(5 << 1)

salary = 1000
print(salary << 1)


salary = 8
print(salary << 2)

items = 6
print(items << 1)

devices = 7
print(devices << 3)

packet = 12
print(packet << 2)


''' 6️⃣ Right Shift (`>>`)
Moves bits to the right.
Each right shift divides the number by **2** (discarding any remainder).'''


print(20 >> 1)


stock = 40
print(stock >> 1)

marks = 20
print(marks >> 1)


salary = 32
print(salary >> 2)


devices = 56
print(devices >> 3)