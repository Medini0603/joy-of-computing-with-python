# related to Josephus problem 

import string
def remove_matching_letters(s1,s2,l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if(l1[i]==l2[j]):
                c=l1[i]
                # l1[l1.index(c)]='*'
                # l2[l2.index(c)]='*'
                l1[i]='*'
                l2[j]='*'
                break
    print(l1)
    print(l2)
    cnt=0
    for i in range(len(l1)):
        if(l1[i]!='*'):
            cnt+=1
    for i in range(len(l2)):
        if(l2[i]!='*'):
            cnt+=1
    return cnt

def flames(cnt):
    result=['Friends','Love','Affection','Marriage','Enemy','Sibling']
    
    while(len(result)>1):
        split_index=(cnt%len(result))-1

        if(split_index>=0):
            right=result[split_index+1:]
            left=result[:split_index]
            result=right+left
        else:
            result=result[:len(result)-1]

    print(result[0])
    


                

p1=input("Enter name 1 : ")
p1=p1.lower()
p1=p1.replace(" ","")

p2=input("Enter name 2 : ")
p2=p2.lower()
p2=p2.replace(" ","")

s1=list(p1)
s2=list(p2)
print(remove_matching_letters(p1,p2,s1,s2))
cnt=remove_matching_letters(p1,p2,s1,s2)
(flames(cnt))

        
