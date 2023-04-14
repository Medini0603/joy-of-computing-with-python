def subStr(s1,s2):
  if(s2 in s1):
    return True
  return False

print(subStr("Bananana","nana"))
print("nana" in "Bananana")

# Given two dictionaries d1 and d2, write a function mergeDic that accepts two dictionaries d1 and d2 and return a new dictionary by merging d1 and d2. 
# Note: Contents of d1 should be appear before contents of d2 in the new dictionary and in same order. In case of duplicate value retain the value present in d1.
def mergeDic(d1,d2):
  d=d1
  
  l=list(d2.keys())
  
  for i in l:
    try:
      d[i]=d[i]
    except:
      d[i]=d2[i]
  return d

key = list(map(int, input().split()))
val = list(map(int, input().split()))

d1 = {}
for i in range(len(key)):
    d1[key[i]] = val[i]
    
d2 = {}
key = list(map(int, input().split()))
val = list(map(int, input().split()))
for i in range(len(key)):
    d2[key[i]] = val[i]

print(mergeDic(d1, d2))


# Given an integer n, print all the indexes of numbers in that integer from left to right.
n=int(input("Enter number"))
l=[int(x) for x in str(n)]
d={}
for i in range(len(l)):
  try:
    d[l[i]].append(i)
  except:
    d[l[i]]=[i,]
for i in d.keys():
  print(i,end=" ")
  for j in d[i]:
    print(j,end=" ")
  print()