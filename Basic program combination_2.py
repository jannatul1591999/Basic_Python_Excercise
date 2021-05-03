#shape calculate
base = int(5)
height = float(9)
area = .5 * base * height
print(area)
#library function
from math import *
a = max(20, 15)
print(a)
print(max(10,20,50))
print(sqrt(25))
print(round(3.8))
print(abs(-4))
print(float(6.6))
print(ceil(3.9))
#type function
num = 20
print(type(num))
n1 = 20
n2 = 30
print(f'{n1} + {n2} = {n1+n2}')
print('t', end="")
print('sk')
result = 20>30
print(result)

# max num find
n1 = 20
n2 = 30
if n1>n2:
    print('n1 large')
else:
    print('n2 large')
#even odd
n1 = 20
n2 = 21
if n1%2==1:
    print('even')
elif n1 % 2 == 0:
    print('odd')
# find 3 large num
n1 = 25
n2 = 30
n3 = 45
if n1>n2:
    if n1 > n3:
        print('n1')
    elif n2> n3:
        print('n2')
print(n2 if n2<n3 else n1)
# logical operator
ch = 'w'
if ch == 'a':
    print('vowel')
else:
    print('cons')
mark = 50
if mark > 60 and mark < 100:
    print('pass')
elif 40 <= mark <= 100:
    print('pass avg')
#while loop
i = 1
while i<= 20:
    print(i)
    i = i+5
print('bd')
i = 2
sum = 0
i = 1
while i <= 100:
    sum = sum + i
    print(i)
    i = i+2
print(sum)
# 2+ 4 + ..+ n
i = 2
sum = 0
n = int(input("num"))
while i<= n:
    print(i)
    i = i + 2














