# Input: 
# 3 4
# Output:
# +-+-+-+-+
# |.|.|.|.|
# +-+-+-+-+
# |.|.|.|.|
# +-+-+-+-+
# |.|.|.|.|
# +-+-+-+-+
mn=list(map(int,input("Enter 2 numbers seperated by space").split()))
m=mn[0]
n=mn[1]
for i in range(2*m+1):
    if(i%2==0):
        for j in range(2*n+1):
            if(j%2==0):
                print("+",end="")
            else:
                print("-",end="")
    else:
        for j in range(2*n+1):
            if(j%2==0):
                print("|",end="")
            else:
                print(".",end="")
    print()


'''Given a list in which each element is a tuple containing (country, country_code). Write a function convertL that takes the list as an argument and returns a dictionary containing keys as country and values as country_code, arranged in ascending order with respect to country code.
Sample Input:
L = [(Sri Lanka, +94), (India, +91)]
Sample output:
{ ‘India’: ‘+91’, ‘Sri Lanka’: ‘+94’}'''

def bubblesort(L):
  for i in range(len(L)):
    for j in range(len(L)-i-1):
      #print(int(L[j][1]))
      if(int(L[j][1])>int(L[j+1][1])):
        Lst=L[j]
        L[j]=L[j+1]
        L[j+1]=Lst
  return L

    
def convertL(L):
  l=bubblesort(L)
  d={}
  for tup in l:
    d[tup[0]]=tup[1]
  return d

n = int(input())
L = []
for i in range(n):
    L.append(input().split())

print(convertL(L))