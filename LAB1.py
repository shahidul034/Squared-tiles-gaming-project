import random
from array import *
num = 2132
str="345"
num2 = pow(10,2)
# big integer
bI = pow(10,20)
print("Big integer: ",bI)
#casting
print(int(str)+num2)
#Random number
num3=random.randint(10,23)
print("random int: ",num3)
num4 = random.uniform(10,100)
print("Random floating num: ",num4)

import math
n1=42
n2=56
print("GCD: ",math.gcd(n1,n2))
print("LCM: ",(n1*n2)/math.gcd(n1,n2))
print("Factorial: ",math.factorial(100))
print("Log value: ",math.log2(8))
#inp = input("Enter :")
#print("input num: ",inp)
print("Log value: ",(math.log2(int(inp))))
#if else
a=45
b=67
c=78
if a>b:
    print("a greater")
elif b>c:
    print("b is greater")
else :
    print("c is greater")
ll=[34,23,67,45,90,34,56,78]
print("List: ",ll)
ll.append(34)
print("Append: ",ll)
ll.insert(0,567)  
print("insert: ",ll)    
ll.remove(34)     
print("remove: ",ll)
print("Count: ",ll.count(34))
ll.sort()
print("sort: ",ll)
ll.reverse()
print("reverse: ",ll)
ll.pop(2)
print("pop(2): ",ll)
ar = array('i',[3,4,6,2,8])
print("Array[2] element: ",ar[2])
ar.fromlist(ll)
print("Merze: ",ar)
ar.extend([56,34])
print("Extend: ",ar)
# format specifier
print("format spec:  %.2d" %a)
print("for loop: ")
for x in ll:
    print(x)
ll2 = [12 for x in range(10)]
print(ll2)
i=0
print("while loop: ")
while i< 10:
    print(i,end=" ")
    i+=1
print("")
#function
def name(a,b,c):
    print("function:",a," ",b," ",c)
name(4,3,6)
#variadic function
def name(*arg):
    print("variadic function:",arg)
name(4,3,6,7)
name(56,34,5,7,3)
#lambda function
area = lambda a,b : .5 *a*b
print("Lambda function: ",area(20,10))
print("Class: ")
class A:
    def __init__(self,a,b):
        self.name=a
        self.roll=b
    def printf(self):
        print(self.name," ",self.roll)
    
obj=A("AAS",23345)
obj.printf()    

import numpy
a1=numpy.array([[1,21],
              [23,4]  
                ])
b1=numpy.array([[1,21],
              [23,4]  
                ])
c1=a1+b1
print("Matrix add: ",c1)
c1=a1*b1
print("Matrix mul: ",c1)
d=numpy.dot(a1,b1)
print("Original mat muL: ",d)


mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print(i)


'''
ar=array('l',[2,3,56,67])
print(ar)
ll= [12 for x in range(100)]
print(ll)
def name(*arg):
    print(arg)

name(3,"er",89)
'''

