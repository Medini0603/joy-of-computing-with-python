from tabnanny import check
import numpy

board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'
# to find dimension of array
arr=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
print(arr.shape)

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if(count==3):
            print(symbol+" won")
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if(board[r][c]==symbol):
                count=count+1
        if(count==3):
            print(symbol+" won")
            return True
    return False

def check_diag(symbol):
    count=0
    for i in range(3):
        if(board[i][i]==symbol):
            count=count+1

        if(count==3):
            print(symbol+" won")
            return True
    
    i=0
    j=2
    count=0
    while(i<=2 and j>=0):
        if(board[i][j]==symbol):
            count=count+1
        i=i+1
        j=j-1

        if(count==3):
            print(symbol+" won")
            return True

    return False



def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_diag(symbol)

def place(symbol):
    print(numpy.matrix(board)) #to print in matrix format
    while(1):
        row=int(input("Enter the row (1,2,3) : "))
        col=int(input("Enter the column (1,2,3) : "))
        if(row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-'):
            break
        else:
            print("Invalid input please enter again")
    board[row-1][col-1]=symbol
        # print(board[row-1][col-1])

def play():
    for turn in range(9):
        if(turn%2==0):
            print("Turn of X")
            place(p1s)
            if(won(p1s)):
                break
        else:
            print("Turn of O")
            place(p2s)
            if(won(p2s)):
                break
    if(not(won(p1s)) and not(won(p2s))):
        print("IT IS A DRAW!!!...")

play()