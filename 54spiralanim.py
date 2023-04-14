import turtle
turtle.bgcolor("black")
t=turtle.Turtle()

widht=5
height=7

dotdist=25
t.setpos(-250,250)
def spiral(m,n):
    '''m is the number of rows
       n is the number of columns
       a is the matrix'''
    k=0#index of start row
    l=0#index of start column
    flag=0
    t.color("white")
    while(k<m and l<n):

        # if(flag!=1):
        #     t.right(90)
        # we are printing the first row among the remaining rows 
        for i in range(l,n):
            t.forward(dotdist)
            # print(a[k][i],end=" ")
        k+=1
        flag=1
        t.right(90)

        # printing last column from remianing columns 
        for i in range(k,m):
            # print(a[i][n-1],end=" ")
            t.forward(dotdist)
        n-=1
        t.right(90)

        if(k<m):
            #printing last rows from remianing rows in reverse order
            for i in range (n-1,l-1,-1):#i.e i-- 
                # print(a[m-1][i],end=" ")
                t.forward(dotdist)
            m-=1
        t.right(90)

        if(l<n):
            #printing the first column of remainining column
            for i in range(m-1,k-1,-1):
                # print(a[i][l],end=" ")
                t.forward(dotdist)
            l+=1
        t.right(90)


spiral(10,10)
turtle.done()


        

