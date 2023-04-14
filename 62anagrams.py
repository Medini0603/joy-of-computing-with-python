# Anagrams using Ascii values 
print(ord('A'))
print(ord('a'))
print(ord('b'))
print(ord(' '))
print(ord('%'))

str1=input("Enter the first string : ")
str2=input("Enter the second string : ")
if(len(str1)!=len(str2)):
    print("Not Anagrams")
else:
    s1=0
    s2=0
    for i in range(len(str1)):
        s1+=ord(str1[i]) 
        s2+=ord(str2[i])
    if(s1==s2):
        print("Anagrams")
    else:
        print("Not ANagrams")


# but not works for all 
# say carrot  and  casqot 
