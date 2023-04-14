# Given a sqaure matrix M, write a function DiagCalc which calculate the sum of left and right diagonals and print it respectively.
def DiagCalc(m):
    n = len(m)
    # print(n)
    sum = 0
    for i in range(n):
        sum += m[i][i]
    print(sum)

    sum2 = 0
    j = n-1
    i = 0
    while (j >= 0 and i < n):
        sum2 += m[i][j]
        i += 1
        j -= 1
    print(sum2)

# Given a matrix M write a function Transpose which accepts a matrix M and return the transpose of M.
# Transpose of a matrix is a matrix in which each row is changed to a column or vice versa.


def Transpose(m):
  n = len(m)#number of rows
  x = len(m[0])#number of columns
  t = [[0 for i in range(n)] for j in range(x)]
  for i in range(n):
    for j in range(x):
      t[j][i] = m[i][j]
  return t

# Given a matrix M write a function snake that accepts a matrix M and returns a list which contain elements in snake pattern of matrix M. (See explanation to know what is snake pattern)

# Input
# A matrix M
# 91 59 21 63 
# 81 39 56 8 
# 28 43 61 58 
# 51 82 45 57

# Output
# [91, 59, 21, 63, 8, 56, 39, 81, 28, 43, 61, 58, 51, 82, 45, 57]

def snake(m):
  l=[]
  n=len(m)
  x=len(m[0])
  for i in range(n):
    if(i%2==0):
      j=0
      while(j<x):
        l.append(m[i][j])
        j+=1
    else:
      j=x-1
      while(j>=0):
        l.append(m[i][j])
        j-=1
  return l


#main program to run functions..
n = int(input())#number of rows
M = []
for i in range(n):
    L = list(map(int, input().split()))
    # split terminates for enter so numbers entered seperated by comas form one row 
    # next column by pressing enter 
    M.append(L)
# sample input
# 4
# 91 59 21 63 
# 81 39 56 8 
# 28 43 61 58 
# 51 82 45 57

DiagCalc(M)#only for square matrices
t = Transpose(M)#for all
print(t)
l=snake(M)#for all
print(l)
