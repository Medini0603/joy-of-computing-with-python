# Given a list L, write a program to make a new list to fix the indexes of numbers in the list L to its same value in the new list. Put 0 at remaining indexes. Also print the elements of the new list in the single line. (See explanation for more clarity.)

L = list(map(int, input().split()))


n=len(L)
m=max(L)+1
#print(m)
l=[0 for i in range(m)]

'''for i in range(m):
  if(i in L):
    l[i]=i'''
    
#print(l)

for i in L:
  l[i]=i

for i in l:
  print(i,end=" ")

# Ram shifted to a new place recently. There are multiple schools near his locality. Given the co-ordinates of Ram P(X,Y) and schools near his locality are given in a nested list, find the closest school. Print multiple coordinates in respective order if there exist multiple schools closest to him. Write a function closestSchool that accepts (X ,Y , L) where X and Y are co-ordinates of Ram's house and L contains co-ordinates of different school.

# Distance Formula(To calculate distance between two co-ordinates): √((X2 - X1)² + (Y2 - Y1)²)

# where (x1,y1) is the co-ordinate of point 1 and (x2, y2) is the co-ordinate of point 2.

# Input:
# X, Y (Ram's house co-ordinates)
# N (No of schools)
# X1 Y1
# X2 Y2
# .
# .
# .

# X6 Y6

# Output:
# Closest point/points to X, Y

def closestSchool(x, y, L):
  min=99999
  distance=[]
  for i in L: 
    dis=((x-i[0])**2+(y-i[1])**2)**0.5
    distance.append(dis)
    if dis<min:
      min=dis 
  for i in range(len(distance)):
    if distance[i]==min:
        print(L[i])

'''import numpy as np
def closestSchool(x,y,l):
  dist=[]
  minimum=123456
  for i in range(len(l)):
    d=np.sqrt(np.square(x-l[i][0])+np.square(y-l[i][1]))
    dist.append(d)
    if(minimum>=dist[i]):
      minimum=dist[i]
    
     
  for i in range(len(dist)):
    if(dist[i]==minimum):
      print(l[i])'''
x, y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x, y, L)

# Given a string s write a program to convert uppercase letters into lowercase and lowercase letters into uppercase. Also print the resultant string.

s=input()
s=list(s)
for i in range(len(s)):
  if(ord(s[i])>=97 and ord(s[i])<=122):
    s[i]=chr(ord(s[i])-32)
  elif(ord(s[i])>=65 and ord(s[i])<=90):
    s[i]=chr(ord(s[i])+32)

s="".join(x for x in s )
print(s)