def spiral(m,n,a):
    '''m is the number of rows
       n is the number of columns
       a is the matrix'''
    k=0#index of start row
    l=0#index of start column

    while(k<m and l<n):
        # we are printing the first row among the remaining rows 
        for i in range(l,n):
            print(a[k][i],end=" ")
        k+=1

        # printing last column from remianing columns 
        for i in range(k,m):
            print(a[i][n-1],end=" ")
        n-=1

        if(k<m):
            #printing last rows from remianing rows in reverse order
            for i in range (n-1,l-1,-1):#i.e i-- 
                print(a[m-1][i],end=" ")
            m-=1

        if(l<n):
            #printing the first column of remainining column
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1

a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
print(a)
spiral(4,4,a)




        

