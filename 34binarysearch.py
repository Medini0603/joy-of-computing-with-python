from cgi import print_arguments


def binary(a,x):

    flag=0
    cnt=0
    low=0
    high=len(a)-1
    while(low<=high and flag==0):
        cnt=cnt+1
        mid=int((low+high)/2)
        if(x==a[mid]):
            flag=1
            print("The element found at pos "+str(mid))
            return
        elif(x<a[mid]):
            high=mid-1
        else:
            low=mid+1
    print("Number not present")
    print("Count= "+str(cnt))

a=[]
for i in range(1,500000000):
    a.append(i)
binary(a,70)


        