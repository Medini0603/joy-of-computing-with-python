import random
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    # random.sample(word,len(word))

    # means join whatever is character if  "t" is given then it joins only when t is encountered 
    # "".join(random.sample(word,len(word)))
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(n1,n2,p1,p2):
    print(n1,"Your score is :",p1)
    print(n2,"Your score is :",p2)
    print("Thanks for playing\nHave a nice day")


def play():
    p1name=input("Player 1:Enter your name")
    p2name=input("Player 2:Enter your name")
    pp1=0
    pp2=0
    turn=0
    while(1):
        # computers's task 
        pickedword=choose()
        # create ques 
        qn=jumble(pickedword)
        print(qn)
        # player 1
        if(turn%2==0):
            print(p1name," This is your turn")
            ans=input("What is on my mind\t")
            if(ans==pickedword):
                pp1=pp1+1
                print(p1name,"Your current score is ",pp1)
            else:
                print("Better luck next time, I chose"+pickedword)
            c=input("Press 1 to continue 0 to quit\t")
            c=int(c)
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        else:
           
            print(p2name," This is your turn")
            ans=input("What is on my mind\t")
            if(ans==pickedword):
                pp2=pp2+1
                print(p2name,"Your current score is ",pp2)
            else:
                print("Better luck next time, I chose"+pickedword)
            c=input("Press 1 to continue 0 to quit\t")
            c=int(c)
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break

        turn=turn+1

play()