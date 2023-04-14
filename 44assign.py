from array import array
from turtle import shape
import numpy
s= 'AbraKaDabra'
print(s[1:6])

def recursive(n):
    if(n==0):
        return 0
    else:
        return n+recursive(n-1)

print(recursive(10))

arr=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
print(arr.shape)

print("9a".isalnum()) 

s="Fuse id odio leo In quis laoreet nulla"
d={}
for i in s:
    d[i]+=1
print(d)