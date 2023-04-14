from traceback import print_tb


x=[3,1,4,2]
print(sorted(x))
print(sorted(x,reverse=True))

y=['q','w','e','r','t','y']
print(sorted(y))
print(sorted(y,reverse=True))

z="Python"
print(sorted(z))
print(sorted(z,reverse=True))

d={'q':1,'w':2,'e':3,'r':4,'t':5,'y':6}
#sorts based on value of keys
print(sorted(d))

l=["aaaa","bb","ccccc","ddd"]
#sorts based on length of strings
print(sorted(l,key=len))


str1=input("Enter string one :")
str2=input("Enter string two : ")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("Anagrams")
else:
    print("Not anagrams")