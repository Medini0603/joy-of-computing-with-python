n=input()
n=int(n)
for i in range(1,n+1):
	for j in range(i):
		print("*",end=" ")	
	print()

i=n-1
while(i>0):
    for j in range(i):
        print("*",end=" ")
    print()
    i-=1