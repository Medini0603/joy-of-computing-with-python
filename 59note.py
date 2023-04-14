#NOTE : strings in python are immutable..

a=['a','b','c','d']
print("".join(a))

print(float('inf'))
print(float('inf')+1)
print(float('inf')*0)

import this
import sys

a="Medini"
print(a*5)
b=1
c=[1,2,3,4]
print(min(c))

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))

print(type(a))
print(type(b))
print(type(c))

import time
print(time.time())


# as is imported as alias 
# example 
# import time as t 

# print("beggar".index('a','beg','r'))

import math as m
print(m.floor(1.34))
print(m.floor(-1.34))
print(m.fabs(-123.56))
print(m.fabs(123.56))



l=[1,44,-9,67]
print(min(l))