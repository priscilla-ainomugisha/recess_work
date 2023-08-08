"""import module
module.product(20,7)

#importing squareroot and factorial from  MATH MODULE
from math import sqrt,factorial

print(sqrt(16))
print(factorial(10))

import math as mt
print(mt.sqrt(20))
print(mt.factorial(6))"""

#input and ouput in python
name = input("Enter your name:")
print("My name is " + name)

#example2
number =int( input("Enter your number:"))
product =number *10
print(product)
#multiple inputs in python
s,r,w =map(int,input("Enter your values:").split())
print("tHE VALUES ARE :", END = "")
print(s,r,w)

#how to capture input from a turple
w=(2,4,6,8,10)
print("current tuple")
print(w)

E = list(w)
E.append(int(input("Enter new value:")))
w=tuple(E)
print("updated tuple")

prnt(w)

mylist =list(map(int, input("Enter the list values:"),split()))
myset =set(map(int, input("enter the set values"),split()))
print(mylist)
print(myset)