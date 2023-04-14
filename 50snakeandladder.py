# Python Imaging Library----PIL
from PIL import Image
import random
end=100
def show_board():
    img=Image.open('49Snakeandladder.png')
    img.show()
def checkladder(points):
    # based on board in image 
    if(points==8):
        print("Ladder")
        return 26
    if(points==21):
        print("Ladder")
        return 82
    if(points==43):
        print("Ladder")
        return 77
    if(points==50):
        print("Ladder")
        return 91
    if(points==54):
        print("Ladder")
        return 93
    if(points==62):
        print("Ladder")
        return 96
    if(points==66):
        print("Ladder")
        return 87
    if(points==80):
        print("Ladder")
        return 100
    return points

def checksnake(points):
    if(points==44):
        print("Snake")
        return 22

    if(points==46):
        print("Snake")
        return 5
    if(points==48):
        print("Snake")
        return 9
    if(points==52):
        print("Snake")
        return 11
    if(points==55):
        print("Snake")
        return 7
    if(points==59):
        print("Snake")
        return 17
    if(points==64):
        print("Snake")
        return 36
    if(points==69):
        print("Snake")
        return 33
    if(points==73):
        print("Snake")
        return 1
    if(points==83):
        print("Snake")
        return 19
    if(points==92):
        print("Snake")
        return 51
    if(points==95):
        print("Snake")
        return 24
    if(points==98):
        print("Snake")
        return 28
    return points

def reached_end(point):
    if(point==end):
        return True
    return False
def play():
    # p1name=raw_input("Player 1 please enter your name : ")
    # p1name=raw_input("Player 2 please enter your name : ")
    p1name=input("Player 1 please enter your name : ")
    p2name=input("Player 2 please enter your name : ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            # Player 1 turn 
            print(p1name+" Your turn ")
            c=input("Enter 1 to continue 0 to quit : ")
            # quit by choice 
            if(c==0):
                print(p1name+" scored "+str(pp1))
                print(p2name+" scored "+str(pp2))
                print("Quitting game")
                break
            # if not 0 i.e. to continue 
            dice=random.randint(1,6)
            print("Dice showed the number "+str(dice))
            pp1=pp1+dice
            pp1=checkladder(pp1)
            pp1=checksnake(pp1)
            # if player goes beyond the board i.e goes to 102
            if(pp1>end):
                pp1=end
            print(p1name+" Your score "+str(pp1))
            print()

            # quit due to winning 
            if(reached_end(pp1)):
                print(p1name+" won ")
                break
        else:
             # Player 2 turn 
            print(p2name+" Your turn ")
            c=input("Enter 1 to continue 0 to quit : ")
            if(c==0):
                print(p1name+" scored "+str(pp1))
                print(p2name+" scored "+str(pp2))
                print("Quitting game")
                break
            # if not 0 i.e. to continue 
            dice=random.randint(1,6)
            print("Dice showed the number "+str(dice))
            pp2=pp2+dice
            pp2=checkladder(pp2)
            pp2=checksnake(pp2)
            # if player goes beyond the board i.e goes to say 102
            if(pp2>end):
                pp2=end
            print(p2name+" Your score "+str(pp2))
            print()
            if(reached_end(pp2)):
                print(p2name+" won ")
                break
        turn+=1

show_board()
play()