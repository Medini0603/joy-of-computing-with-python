def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
        print(a)

a = [5,1,4,2,8,-2]
bubble(a)
for i in a:
    print(i)
