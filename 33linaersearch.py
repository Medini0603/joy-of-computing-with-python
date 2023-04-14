def linearsearch(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    # print(element)
    flag=0
    cnt=0
    for i in element:
        cnt=cnt+1
        if(i==x):
            flag=1
            print("Yes I found number at "+str(i))
            break
    if(flag==0):
        print("Not found")
    print(cnt)


linearsearch(1001,30000)
linearsearch(1001,30)