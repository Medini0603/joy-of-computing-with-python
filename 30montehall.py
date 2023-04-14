
import random
# from secrets import choice
# montehall problem
# 3 doors 2 hv goat one has bmw
# u choose one
# the organizer opens one door and says if we want to swap
# the probability of winning if we swap is high
# how ??
# lets seee


#def montehall(swap,notswap):
doors=[0]*3
goatdoors=[0]*2
swap=0  #number of swap wins
notswap=0  #number of not swap wins
j=0
while(j<10):
    x=random.randint(0,2) #xth door will have bmw rest have goats
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoors.append(i)
    choice=int(input("Enter choice "))

    # After taking choice we should open one goatdoor and show 
    dooropen=random.choice(goatdoors)
    # now dooropen should not be same as the door selected by participant 
    while(dooropen==choice):
        dooropen=random.choice(goatdoors)

    # Ask if participant want to swap 
    ch=input("Print y to swap n if not ")
    if(ch=='y'):
        #i.e if he swaps and original choice before swap was goat then he wins as he has swapped
        if(doors[choice]=='Goat'):
            print("Player wins")
            swap=swap+1
        else:
            print("Player lost")

    else:
        if(doors[choice]=='Goat'):
            print("Player lose")
        else:
            print("Player wins")
            notswap=notswap+1
    j=j+1
print(swap)
print(notswap)
