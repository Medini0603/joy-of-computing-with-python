t=(1,2,3,4)
print(t)
t1=((1), (2), (3), (4))
print(t1)

print(type(10) )

word="nptel"
new=""
for i in word:
    j=ord(i)
    # k=(((j+26)-97)%26)+97
    k=((j-97)%26)+97
    new=new+chr(k)

# Given a list L, write a program to shift all zeroes in list L towards the right by maintaining the order of the list. Also print the new list.

L=[0,1,0,3,12]
cnt=0
l=[]
for i in L:
  if(i==0):
    cnt=cnt+1
  else:
    l.append(i)

for i in range(cnt):
  l.append(0)

print(l)
