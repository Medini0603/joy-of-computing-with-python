import numpy as np
def closestSchool(x,y,l):
  dist=[]
  minimum=123456
  for i in range(len(l)):
    #print(l[i][0])
    #print(l[i][1])
    d=np.sqrt(np.square(x-l[i][0])-np.square(y-l[i][1]))
    dist.append(d)
  
  mini=0
  for i in range(len(l)):
    if(minimum>=dist[i]):
      minimum=dist[i]
      mini=i
    
  print(dist) 
  print(l[mini])

closestSchool(0,0,[[3, 0], [0, 0], [5, -9], [-6, 2], [-4, -5]])



l=[10,2,2,5,8]
print(min(l))


import numpy as np
def closestSchool(x,y,l):
  dist=[]
  minimum=123456
  for i in range(len(l)):
    d=np.sqrt(np.square(x-l[i][0])+np.square(y-l[i][1]))
    dist.append(d)
  
  mini=0
  for i in range(len(l)):
    if(minimum>=dist[i]):
      minimum=dist[i]
      mini=i
    
  if(len(l)==0):
    print()
  else:    
    res=[]
    res.append(l[mini])
    for i in range(len(dist)):
        if(i==mini):
            continue
        if(dist[i]==minimum):
            res.append(l[i])

    for i in range (len(res)) :
        print(res[i])
