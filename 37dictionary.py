#You are given a string S. Write a function count_letters which accepts the string S and returns a dictionary containing letters (including special character) in string S as keys and their count in string S as values.
def count_letters(S):
  d={}
  for i in S:
    try:
      d[i]+=1
    except KeyError:
      d[i]=1
      
  return d

d=count_letters("The Joy of computing")
print(d)

#You are given a list L. Write a function uniqueE which will return a list of unique elements is the list L in sorted order. (Unique element means it should appear in list L only once.)
def uniqueE(L):
  d={}
  for i in L:
    try:
      d[i]+=1
      #del d[i]
    except KeyError:
      d[i]=1
      
  uniq=[]
  for i in d:
    if(d[i]==1):
      uniq.append(i)
  uniq.sort()
  return uniq

uni=uniqueE([1,2,3,3,4,4,2,5,6,7])
print(uni)

#You are given a list L. Write a program to print first prime number encountered in the list L.(Treat numbers below and equal to 1 as non prime)
def prime(n):
  for i in range(2,int((n/2)+1)):
    if(n%i==0):
      return False
  return True

L=[1,2,3,4,5,6,7,8,9]
for i in L:
  if(i<=1):
    continue
  if(prime(i)):
    print(i)
    break

