# Take 3 sides of a triangle as an input and find whether that triangle is a right angled triangle or not. Print 'YES' if a triangle is right angled triangle or 'NO' if it's not.

a=int(input())
b=int(input())
c=int(input())

max=a
s1=b
s2=c
if(b>max):
  s1=a
  s2=c
  max=b
if(c>max):
  max=c
  s1=a
  s2=b

sq=(s1*s1)+(s2*s2)
if(sq==(max*max)):
  print("YES")
else:
  print("NO")

# Write a program that accepts a hash-separated sequence of words as input and prints the words in a hash-separated sequence after sorting them alphabetically in reverse order
txt = input()
x = txt.split("#")
x.sort()
x.reverse()
x='#'.join(str(a) for a in x)
print(x)

# Write a program which takes two integer a and b and prints all composite numbers between a and b. (both numbers are inclusive)
def iscomposite(a):
  for i in range(2,int(a/2)+1):
    if(a%i==0):
      return True
  return False
    

a=int(input())
b=int(input())


for i in range(a,b+1):
  if(i==2 or i==1):
    continue
  if(i%2==0):
    print(i)
  else:
    if(iscomposite(i)):
      print(i)
  
