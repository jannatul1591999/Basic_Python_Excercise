sub = ['a', 'b', 'c', "d"]
print(sub)
print(sub[2])
print(sub[-0])
print('C' in sub)
print(sub + [28])
print(len(sub))
sub.append('tamu')
print(sub)
sub.insert(2,'selfish')
sub.remove('d')
sub.reverse()
sub.sort()
sub.pop()
sub.clear()
print(sub)
sub = ['1','2','3','4']
sub2 = sub.copy()
print(sub2)
sub = ['1','2','3','4']
sub2 = sub.index('4')
print(sub2)
sub = ['1','2','3','4']
sub2 = sub.count('3')
print(sub2)
#range function
num = list(range(10))
print(num[5])
num = list(range(5,11))
print(num)
num = list(range(2, 101, 2))
print(num)
#for loop
num = [10,20,14,13,12]
sum = 0
for x in num:
    sum = sum + x
print(sum)
'''
#series 1+2+..+n
n = int(input("num:"))
sum = 0
for x in range(1, n+1, 1):
    sum = sum+x
    print(sum)
#series 1*1 +2*2 +..+n*n
n = int(input("num:"))
sum = 0
for x in range(1, n+1, 1):
    sum = sum+x*x
    print(sum)'''
#factorial
n = 7
sum = 1
for x in range(1, n+1, 1):
    sum=sum *x
    print(sum)
'''
#pattern printing
n = 3
for i in range(n+1):
    print(i *'*')
n=3
'''
'''
#guess num
import random
gn = int(input("guess num:"))
random_num = random.randint(1,5)
if gn == random_num:
    print('won')
else:
    print('lost')
    print('num was',random_num)
from random import randint
for x in range (1,6):
     gn= int(input("num:"))
     rn = randint(1,5)
     if gn == rn:
        print('won')
     else:
        print('lost')
        print('rn was:', rn)
        
#list as input from user
n = input("num:")
list = n.split()
sum = 0
for num in list:
    sum = sum + int(num)
print(sum)

nw = 0
nl = 0
nd = 0
text = input('number input:')
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        nl = nl +1
    elif x >= '0' and x <= '9':
        nd = nd +1
    elif x == ' ':
        nw = nw +1
print(nl)
print(nd)
print(nw)
'''
#matrix
mat = [
    [1,2,3],
    [2,5,8]
]
mat[1][2] = 0
print(mat[1][2])
mat = [
    [1, 2, 3],
    [2, 5, 8]
]
for row in mat:
    for col in row:
        print(col)
#dictionary
studentID = {
    '101' : 'tamanna',
'102' : 'tamanna'
}
print(studentID['101'])
print(studentID.get('104', 'unvalid'))
#tuples
stu = (
    't',
    'e',
    'f',
    ('t', 'g', 'h'))
print(stu[3])
print('num:', stu)
#set
num = {
     1,2,3,45,6
}
num2 = set([4,5,6])
num2.add(53)
num2.remove(53)
print(4 in num2)
print(num | num2)
print(num & num2)
print(num - num2)
#stack and queue
books = []
'''books.append('c')
books.append('java')
books.append('pythn')
print(books)'''
books.append('c')
print('books:', books[-1])
books.pop()
if not books:
    print('no books left')
#queye-----

from collections import deque
bank = deque(['x', 'y', 'z'])
print(bank)
bank.popleft()
print(bank)
# introduction to function

def add(x,y):
    sum = x + y
    print(sum)
add(10,12)


def no():
    print('no text')
no()
#returning value from function

def add(a, b):
    sum = a+b
    return  sum
result = add(2,3)
print(result)

def large(a,b):
    if a > b:
        return a
    else:
        return b

result = large(1,2)
print(result)
#xxxargs
def student(*details):
    print(details[0])
student(101, 'tamu')

def math(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
        print(sum)
math(1,2,3,4)

#xxargs

def stu(**info):
    print(info)

stu(id = 190941, name = 'tamanna')

# debugging
def add(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
        return sum
print (add(2,4,7))
print('js')

















