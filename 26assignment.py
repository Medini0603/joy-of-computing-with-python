'''
This is a sentence
'''

# perfect number 
from turtle import numinput


n=int(input("Enter a number"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i

if(sum==n):
    print("Perfect number")
else:
    print("Not perfect number")

L1=['starwars','godfather','passenger','jurrasic park']
L2=['spiderman','jumanji','Passenger','Starwars']

for i in L1:
    for j in L2:
        if(i[0]==j[0]):
            print(j)