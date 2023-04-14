def newlist(L):
  P=[]
  for i in range(len(L)):
    if(L[i]%5==0 or L[i]%7==0 or (L[i]%5==0 and L[i]%7==0)):
      P.append(L[i])
  P.sort()
  return P
  
L = [7, 8, 9, 10, 11]
P=newlist(L)
print(P)