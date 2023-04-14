import string
import random
# print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

symbols=[]
# Typecast to list 
symbols=list(string.ascii_letters)
# Initailise size to 5 with all values 0 in list
card1=[0]*5
card2=[0]*5

#the ppos1 and pos2 gives postion of common symbols in card1 and card2 respectively
pos1=random.randint(0,4)
pos2=random.randint(0,4)

# generate random symbol 
samesymbol=random.choice(symbols)
# remove that symbol 
symbols.remove(samesymbol)

card1[pos1]=samesymbol
card2[pos2]=samesymbol

i=0
while(i<5):
    if(pos1!=i):
        card1[i]=random.choice(symbols)
        symbols.remove(card1[i])
    if(pos2!=i):
        card2[i]=random.choice(symbols)
        symbols.remove(card2[i])
    i=i+1
print(card1)
print(card2)
c=input("Enter common symbol ")
if(c==samesymbol):
    print("Right")
else:
    print("Wrong")
