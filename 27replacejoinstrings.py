s=input("Enter string")
for i in s:
    if(i=='a' or i=='e' or i=='o' or i=='i' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        s=s.replace(i,"*")
print(s)

def unlock(quesname,moviename,letter):
    n=len(moviename)

    #typecast string to list
    movie=list(moviename)
    ques=list(quesname)
    temp=[]

    for i in range(n):
        if(movie[i]==letter or movie[i]==' '):
            temp.append(movie[i])
        else:
            temp.append(ques[i])

# convert the list temp to string using join 
# typecast each element x in temp to string and join to qn 
    qn=''.join(str(x) for x in temp)
    # convert list back to singlE string 
    # qn=str(temp)-->not possible from this use join only
    return qn