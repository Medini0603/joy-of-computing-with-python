# Iterative definition 
# def fact(n):
#     if(n<0):
#         print("Invalid input")
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f)

# fact(7)

def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

i=int(input("Enter n"))
if(i<1):
    print("Enter valid input")
else:
    n=fact(i)
print(n)