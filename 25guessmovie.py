from operator import mod
import random

movies = ['shravani subramanya', 'drishya', 'milana', 'vikrant rona',
          '777 charlie', 'rrr', 'hero', 'kgf', 'love mocktail', 'yuvarathna','eega']
def create_ques(movie):
    n=len(movie)
    #typecast movie name to list
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    # convert list back to singlr string 
    # qn=str(temp)-->not possible from this use join only
    return qn



def ispresent(letter,movie):
    c=movie.count(letter) #to count number of occurances of letter in movie
    if(c==0):
        return False
    else:
        return True



def unlock(quesname,moviename,letter):
    n=len(moviename)
    movie=list(moviename)
    ques=list(quesname)
    temp=[]
    for i in range(n):
        if(movie[i]==letter or movie[i]==' '):
            temp.append(movie[i])
        else:
            temp.append(ques[i])

    qn=''.join(str(x) for x in temp)
    # convert list back to singlE string 
    # qn=str(temp)-->not possible from this use join only
    return qn


def play():
    p1name = input("Player 1 Please enter your name : ")
    p2name = input("Player 2 Please enter your name : ")
    pp1 = 0
    pp2 = 0
    turn = 0  # to alternate turns between 2 players
    # even for player 1 odd for player2
    willing = True  # if player wants to continue or not
    while (willing):
        if (turn % 2 == 0):
            # turn of player 1
            print(p1name+" Its your turn")
            picked_mov = random.choice(movies)
            qn = create_ques(picked_mov)#create ques encodes selected movie name with * for char and space for space
            modifiedques = qn#initialize modified ques to encoded dots and dashes
            # print(qn)
            print(modifiedques)

            notsaid = True#its true until player1 guesses movie correctly
            while notsaid:
                letter = input("Enter letter : ")
                if (ispresent(letter, picked_mov)):
                    modifiedques = unlock(modifiedques, picked_mov, letter)
                    print(modifiedques)
                    
                    if(modifiedques==picked_mov):
                        pp1 = pp1+1
                        print("You guessed it right")
                        notsaid = False
                        print(p1name+" Your score : "+str(pp1))
                        notsaid=False
                        break

                    d = input("Press 1 to guess movie or 0 to unlock next letter : ")
                    print(d)
                    #maccha typecast d to int
                    d=int(d)
                    if(d==1):
                        ans = input("Give ur answer : ")
                        if (ans == picked_mov):
                            pp1 = pp1+1
                            print("You guessed it right")
                            notsaid = False
                            print(p1name+" Your score "+str(pp1))
                        else:
                            print("wrong movie name Try again")

                else:
                    print(letter+" is not there ")
            # end of while i.e movie is guessed properly 

            c=input("press 1 to continue or 0 to quit : ")
            # c=int(c)
            if(int(c)==0):
                print(p1name+" Your score "+str(pp1))
                print(p2name+" Your score "+str(pp2))
                print("Thanks for playing have a nice day")
                willing=False

        else:
            # player2

            print(p2name+" Its your turn")
            picked_mov = random.choice(movies)
            qn = create_ques(picked_mov)#create ques encodes selected movie name with * for char and space for space
            modifiedques = qn#initialize modified ques to encoded dots and dashes
            print(qn)

            notsaid = True#its true until player1 guesses movie correctly
            while notsaid:
                letter = input("Enter letter : ")
                if (ispresent(letter, picked_mov)):
                    modifiedques = unlock(modifiedques, picked_mov, letter)
                    print(modifiedques)

                    if(modifiedques==picked_mov):
                        pp1 = pp1+1
                        print("You guessed it right")
                        notsaid = False
                        print(p1name+" Your score "+str(pp1))
                        notsaid=False
                        break

                    d = input("Press 1 to guess movie or 0 to unlock next letter : ")
                    # d=int(d)
                    if (int(d) == 1):
                        ans = input("Give ur answer : ")
                        if (ans == picked_mov):
                            pp2 = pp2+1
                            print("You guessed it right")
                            notsaid = False
                            print(p2name+" Your score "+str(pp2))
                        else:
                            print("wrong movie name Try again")

                else:
                    print(letter+" is not there ")
            # end of while i.e movie is guessed properly 

            c=input("press 1 to continue or 0 to quit : ")
            # c=int(c)
            if(int(c)==0):
                print(p1name+" Your score "+str(pp1))
                print(p2name+" Your score "+str(pp2))
                print("Thanks for playing have a nice day")
                willing=False

#to alternate turns between 2 users
        turn = turn+1

play()