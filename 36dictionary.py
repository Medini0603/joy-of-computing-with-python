import random
import string

a=string.ascii_lowercase
print(a)
d={}

for i in range(26):
    index=random.randint(0,25)#creates random number between 0 to 25 both inclusive
    #now key=a[index]....i.e if index=0 key='a'....index=12 key='m'...
    try:
        d[a[index]]+=1 #if that letter is already added as key in previous iterations increment the value of that key
    except KeyError:
        d[a[index]]=0 #if that key was not added previously add it with value one 

print(d)