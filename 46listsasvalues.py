# Given a list L containing integers, write a program that creates and prints a dictionary 'd' containing all the the numbers that occur twice or more in the list as keys and their indexes as values. Both the keys are and their values should be in the same order as given the list.

lst=list(map(int,input().split()))
d={}
for i in range(len(lst)):
  if(lst.count(lst[i])==1):
    continue
  else:
    try:
      d[lst[i]].append(i)
    except:
      # i.e to initialize that key with first element 
      d[lst[i]]=[i,]
print(d)
    
    