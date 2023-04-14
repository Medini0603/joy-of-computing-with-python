def magicsquare(n):
    magsq=[[0 for i in range(n)] for j in range(n)]
    #print(magsq)
    p=n/2
    q=n-1
    p=int(p)
    q=int(q)
    cnt=1
    num=n*n

    print()
    while(cnt<=num):
        if(p==-1 and q==n):
            p=0
            q=n-2
        elif(p<0):
            p=n-1
        elif(q==n):
            q=0
        elif(magsq[p][q]!= 0):
            p=p+1
            q=q-2

        magsq[p][q]=cnt
        cnt=cnt+1
        p=p-1
        q=q+1

    for i in range(n):
        for j in range(n):
            print(magsq[i][j],end=" ")
        print()

    sum=n*(n*n+1)/2
    print("Sum is = ",str(sum))


    
magicsquare(3)
magicsquare(5)
magicsquare(7)