import random

def evolve(x):
    # to select random index in dna 
    ind=random.randint(0,len(x)-1)
    # to define a condtion 
    # if p is 1 only then change ind 
    #i.e the probability of mutation is 1/100
    p=random.randint(1,100)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]='1'
        else:
            x[ind]='0'

with open("dna_data.txt","r") as myfile:
    x=myfile.read()
    # convert string to list 
    x=list(x)

for i in range(len(x)):
    evolve(x)
print(x)

