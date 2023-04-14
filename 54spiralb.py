import turtle
import random
turtle.bgcolor("black")
t=turtle.Turtle()
t.penup()
listcolor=["red","yellow","green","cyan","pink","violet","grey","violet","white","magenta"]
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
    t.color(random.choice(listcolor))
    flag=0
    t.color("white")
    while(k<m and l<n):

        # if(flag==1):
        #     t.right(90)
        # we are printing the first row among the remaining rows 
        t.color(random.choice(listcolor))
        for i in range(l,n):
            t.dot()
            t.forward(dotdist)
            # print(a[k][i],end=" ")
        k+=1
        f=1
        t.right(90)

        # printing last column from remianing columns 
        t.color(random.choice(listcolor))
        for i in range(k,m):
            # print(a[i][n-1],end=" ")
            t.dot()
            t.forward(dotdist)
        n-=1
        t.right(90)
        t.color(random.choice(listcolor))
        if(k<m):
            #printing last rows from remianing rows in reverse order
            for i in range (n-1,l-1,-1):#i.e i-- 
                # print(a[m-1][i],end=" ")
                t.dot()
                t.forward(dotdist)
            m-=1
        t.right(90)


        t.color(random.choice(listcolor))
        if(l<n):
            #printing the first column of remainining column
            for i in range(m-1,k-1,-1):
                # print(a[i][l],end=" ")
                t.dot()
                t.forward(dotdist)
            l+=1
        t.right(90)


spiral(20,20)
turtle.done()
