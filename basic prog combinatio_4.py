'''def add(*nums):
    sum = 0
    for num in nums:
        sum = sum + num
        return sum
print(add(2, 4, 5))
#lambda function

print((lambda a,b : a*a + 2*a*b + b*b) (2, 3))

#map function

def square(x):
    return x*x
num = [2,3,4]

result = list(map(square, num))
print(result)

#filter func
n = [2,3,4,5,8]
result = list(filter(lambda a: a%2==0 , n))
print(result)

#list comprehension

#comprehension for map
n = [1, 2, 333, 4]
r = [x*x for x in n]
print(r)

#comprehension for filter

num = [2, 3, 4]
r = [x for x in num if x%2 == 0]
print(r)

#zip func

roll = [1, 2, 3, 4, 5]
name = ['a', 'b', 'c', 'd', 'e']

print(list(zip(roll, name, 'ghijk')))

#recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(9))

# read a file

''''''read = open('read.txt', 'r')
print(read.readable())
read.close()

read = open('read.txt', 'w')
print(read.writable())
read.close()

read = open('read.txt', 'r+')
print(read.readable())
read.close()''''''

read = open('read.txt', 'r+')
t = read.read()
print(t)
size = len(t)
print(size)
read.close()

read = open('read.txt', 'r+')
t = read.readlines()
print(t)
read.close()

read = open('read.txt', 'r+')
for line in read:
    print(line)
read.close()

#writing in a file
#add new line/text
read = open('read.txt', 'a')
read.write('\nTamanna-KU')
read.close()
#just only one line print
read = open('read.txt', 'w')
read.write('Tamanna')
read.close()

#html write

read = open('read.html', 'w')
read.write('Tamanna')
read.close()

#exception handling

name = 'tamanna'
print(name[3])

try:
    list = [1,2,3,0]
    r = list[1] / list[5]
    print(r)
except ZeroDivisionError:
    print('not possible')
except IndexError:
    print('no')
finally:
    print('success')


#exception handling part 2

try:
    #n1 = int(input("num1:"))
  #  n2 = int(input("num2:"))
   # n3 = int(input("num3:"))
    #r = n1/n2
#except ValueError:
    #print('Insert only integer')
#except ZeroDivisionError:
    #print('you cant divide a num by zero')
#finally:
   # print('thnaks!!!!!!!!!')
'''

def voter(age):
    if age>18:
        raise ValueError('Invalid Error')
    return "You're allowed to vote"
try:
    print(voter(9))
    print(voter(19))
except ValueError:
    print(voter(0))

#swapping
a = 20
b= 10
'''temp = a
a = b
b = temp'''
a, b = b, a
print(a)
print(b)

#oop
class stu:
    roll = ''
    gpa = ''
rahim = stu()
print(isinstance(rahim, stu))
rahim.gpa = 3.9
rahim.roll = 1
print(f'roll : {rahim.roll}, gpa = {rahim.gpa}')

karim = stu()
karim.gpa = 3
print(f'gpa = {karim.gpa}')

#introduction to methods

class stu:
    roll = ''
    gpa = ''
    def setValue(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f'roll : {self.roll}, gpa = {self.gpa}')

rahim = stu()
print(isinstance(rahim, stu))
rahim.setValue(100, 3)
rahim.display()

karim = stu()
karim.gpa = 3
karim.roll = 2
karim.display()

#constructor

class stu:

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f'roll : {self.roll}, gpa = {self.gpa}')

rahim = stu(100, 2.4)
print(isinstance(rahim, stu))
rahim.display()

#excercise

class triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
    def display(self):
            n = .5 * self.base * self.height * self.height
            print('Area:' ,n)
t1 = triangle(10,20)
t2 = triangle(30, 40)
t1.display()
t2.display()

#inheritance

class phone:
    def call(self):
        print('ur call')
    def messeage(self):
        print('u can text')
class samsung(phone):
    def photo(self):
        print('u can take photo')
p = phone()
p.messeage()
p.call()
t = samsung()
t.photo()
t.call()
print(issubclass(samsung, phone))

#method overriding

class phone:
    def __init__(self):
        print("phone class")
class samsung(phone):
    #override start
    def __init__(self):
        super().__init__()
        print('sm class')
    pass
s = samsung()

#example of inheritance/haircical

class shape:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    def area(self):
        print('area method of shape class')
class triangle(shape):
    def area(self):
        area = .5 * self.d1 * self.d2
        print('shape class', area)
class ractangle(shape):
    def area(self):
        area = self.d1 * self.d2
        print('ractangle class', area)
t = triangle(10, 20)
t.area()
r = ractangle(20, 30)
r.area()

#types of inheritance
#multi-level inheritance

class a:
    def display1(self):
        print('idiffifi')
class b:
    def display2(self):
        print('tm.=')
class c(b, a):
    def display3(self):
        pass
ob1 = c()
ob1.display2()

#abstraction(contains class, method)

from abc import ABC,abstractmethod
class father(ABC):
    @abstractmethod
    def do_study(self):
         print('do study')

class son(father):
    def __init__(self):
        self.name()

    def show(self):
        print(self.name)
    def do_study(self):
        print('yes, father')
a = son('fraud')
a.show()
a.do_study()


#polimorphism

#built-in
print(len('tamanna'))
print(len([10, 20, 30]))
#user define
def add(x, y, z=0):
    return x + y + z
print(add(2, 3))
print(add(4, 6, 7))

#magic method

class bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return(print(f'name = {self.name} , color = {self.color}'))
    def __eq__(self, other):
         return self.name == other.name and self.color == other.color
    def dispaly(self):
        print(f'name = {self.name} , color = {self.color}')
bike1 = bike('yamaha', 'blue')
bike2 = bike('honda', 'red')
#print(bike1)
print(bike1 == bike2)


# creating modules

from math import pow
print(pow(45, 2))
from area import triangle
triangle(10, 20)
#regular expression

import re
pattern = r"color"
if re.match(pattern, 'red color is worst'):
    print('match')
else:
    print('mismatch')

import re
pattern = r"color"
if re.search(pattern, 'red color is worst'):
    print('match')
else:
    print('mismatch')

import re
pattern = r"color"
print(re.findall(pattern, 'red is the worst color. blue is good'))

import re
pattern = r'loved'
text = 'i just hate you. you are a cheated. you never deserve to be loved. you must have to be punished.'
match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

#search and replace

import re
pattern = r'hope'
text = 'i just hate you. you are a cheated. you never deserve to be loved. you must have to be punished. hope'
text2 = re.sub(pattern, 'you are an evil', text, count=1)
print(text2)

#meta characters

import re
pattern = r'^colo.r$'
if re.match(pattern, 'colour'):
    print('match')
import re
pattern = r'(ab)*'
pattern = r'(e)+'
if re.match(pattern, 'colour'):
    print('match')
else:
    print('no')

import re
pattern = r'ice(-)?cream'
if re.match(pattern, 'ice-cream'):
    print('match')
import re
pattern = r'e{1,3}$'
if re.match(pattern, 'e'):
    print('match')
import re
pattern = r'[aeiou]'
pattern = r'[A-Z][a-z][0-9]'
if re.match(pattern, 'agkgjtl'):
    print('match')













