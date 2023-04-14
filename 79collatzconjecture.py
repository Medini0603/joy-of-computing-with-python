def collatz(n):
    i=1
    while(n!=1):
        if(n%2==0):
            n=int(n/2)
        else:
            n=(3*n)+1
        i+=1

    print(n," after ",i," iterations")

collatz(20)
