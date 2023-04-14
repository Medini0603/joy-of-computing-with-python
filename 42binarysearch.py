
def binarysearch(l,start,end,key):
    if(start>end):
        return -1
    m=int((start+end)/2)
    if(l[m]==key):
        return m
    elif(l[m]>key):
        return binarysearch(l,start,m-1,key)
    else:
        return binarysearch(l,m+1,end,key)

l=[1,2,3,4,5]
start=0
end=len(l)-1
key=int(input("Enter key"))
pos=binarysearch(l,start,end,key)
if(pos==-1):
    print("Key not found")
else:
    print("Key is found at "+str(pos+1))

